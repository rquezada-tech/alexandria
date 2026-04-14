#!/usr/bin/env python3
"""
Alexandria - Watch mode para indexación incremental.
Observa la carpeta content/ y re-ingesta automáticamente
archivos nuevos o modificados usando watchdog.

Uso:
    python backend/watch.py                    # watch normal
    python backend/watch.py --once             # re-index todo una vez y salir
    python backend/watch.py --content ./content  # carpeta personalizada
"""
import argparse
import re
import sys
import time
import threading
from pathlib import Path
from typing import Optional

import frontmatter
from watchdog.observers import Observer
from watchdog.events import (
    FileSystemEventHandler,
    FileCreatedEvent,
    FileModifiedEvent,
    FileDeletedEvent,
    FileMovedEvent,
)

sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))
from db import init_db, get_db


CHUNK_SIZE = 600
CHUNK_OVERLAP = 50
VALID_DOMAINS = {
    "medicina", "supervivencia", "historia",
    "mapas", "electronica", "manufactura",
    "comunicaciones", "herramientas",
}
DEBOUNCE_SECONDS = 1.5  # esperar a que terminen de escribir


# ── Chunking (copiado de ingest.py para no depender de él) ────────────────

def chunk_text(text: str) -> list[str]:
    text = re.sub(r"\n{3,}", "\n\n", text)
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks, current_words, current_count = [], [], 0

    for para in paragraphs:
        words = para.split()
        if current_count + len(words) <= CHUNK_SIZE:
            current_words.append(para)
            current_count += len(words)
        else:
            if current_words:
                chunks.append(" ".join(current_words))
            if CHUNK_OVERLAP > 0 and current_words:
                overlap_words = " ".join(current_words).split()[-CHUNK_OVERLAP:]
                current_words = [" ".join(overlap_words), para]
                current_count = len(overlap_words) + len(words)
            else:
                current_words = [para]
                current_count = len(words)

    if current_words:
        chunks.append(" ".join(current_words))
    return chunks


def process_file(filepath: Path) -> Optional[list]:
    try:
        post = frontmatter.loads(filepath.read_text(encoding="utf-8"))
    except Exception:
        return None

    domain = post.get("domain", "").lower().strip()
    subtopic = post.get("subtopic", "").lower().strip() or None
    if domain not in VALID_DOMAINS:
        return None

    title = post.get("title", filepath.stem)
    markdown_body = str(post.content)
    text = re.sub(r"#{1,6}\s+", "", markdown_body)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = re.sub(r"!\[[^\]]*]\([^\)]+\)", "", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    chunks = chunk_text(text)
    has_images = int(bool(re.search(r"!\[.*?\]\(.*?\)", markdown_body)))

    return [(title, domain, subtopic, c, i, len(chunks), has_images) for i, c in enumerate(chunks)]


# ── Indexación incremental ─────────────────────────────────────────────────

def upsert_article(filepath: Path):
    """
    Elimina el artículo existente (por source) y re-ingesta el archivo.
    Si el archivo no es procesable (no es markdown válido), solo elimina.
    """
    # Calcular source relativo al content/ padre
    try:
        source = str(filepath.relative_to(filepath.parents[1]))
    except ValueError:
        source = str(filepath)

    rows = process_file(filepath)

    conn = get_db()
    conn.execute("PRAGMA journal_mode=WAL")

    # Eliminar chunks existentes de este artículo
    deleted = conn.execute(
        "DELETE FROM contents WHERE source = ?", (source,)
    ).rowcount
    conn.execute("DELETE FROM contents_fts WHERE rowid IN (SELECT id FROM contents WHERE source = ?)", (source,))
    conn.commit()

    if rows is None or len(rows) == 0:
        conn.close()
        print(f"  [{filepath.name}] Eliminado (no procesable o dominio inválido) — {deleted} chunks borrados")
        return

    # Insertar nuevos chunks
    now = "datetime('now')"
    chunk_records = [
        (source, title, domain, subtopic, chunk, chunk_idx, total_chunks, has_images)
        for title, domain, subtopic, chunk, chunk_idx, total_chunks, has_images in rows
    ]
    conn.executemany(
        "INSERT INTO contents (source,title,domain,subtopic,chunk,chunk_idx,total_chunks,has_images) "
        "VALUES (?,?,?,?,?,?,?,?)",
        chunk_records,
    )

    # Actualizar FTS para cada nuevo chunk
    # Obtener los rowids recién insertados
    for title, domain, subtopic, chunk, *_ in chunk_records:
        cur = conn.execute(
            "SELECT id FROM contents WHERE source=? AND title=? AND chunk=? LIMIT 1",
            (source, title, chunk)
        )
        row = cur.fetchone()
        if row:
            conn.execute(
                "INSERT OR REPLACE INTO contents_fts(rowid, title, domain, subtopic, chunk) "
                "VALUES (?, ?, ?, ?, ?)",
                (row["id"], title, domain, subtopic or "", chunk)
            )

    conn.commit()
    conn.close()
    print(f"  [{filepath.name}] Re-ingestado — {len(rows)} chunks")


def delete_article(filepath: Path):
    """Elimina un artículo de la base cuando el archivo es borrado."""
    try:
        source = str(filepath.relative_to(filepath.parents[1]))
    except ValueError:
        source = str(filepath)

    conn = get_db()
    deleted = conn.execute(
        "DELETE FROM contents WHERE source = ?", (source,)
    ).rowcount
    conn.commit()
    conn.close()

    if deleted > 0:
        print(f"  [{filepath.name}] Eliminado de la base — {deleted} chunks borrados")
    else:
        print(f"  [{filepath.name}] No encontrado en la base")


# ── Debounce para evitar spam ───────────────────────────────────────────────

class DebouncedHandler(FileSystemEventHandler):
    """
    Agrupa eventos rápidos del mismo archivo en uno solo,
    para no re-indexar mientras se está escribiendo.
    """

    def __init__(self, callback, debounce: float = DEBOUNCE_SECONDS):
        super().__init__()
        self.callback = callback
        self.debounce = debounce
        self.pending: dict[str, threading.Timer] = {}

    def _schedule(self, filepath: str, event_type: str):
        key = f"{event_type}:{filepath}"
        if key in self.pending:
            self.pending[key].cancel()

        timer = threading.Timer(self.debounce, self._fire, args=(filepath, event_type))
        self.pending[key] = timer
        timer.start()

    def _fire(self, filepath: str, event_type: str):
        del self.pending[f"{event_type}:{filepath}"]
        try:
            self.callback(filepath, event_type)
        except Exception as e:
            print(f"  ERROR en {event_type} {filepath}: {e}")

    def on_created(self, event: FileCreatedEvent):
        if event.is_directory:
            return
        if not event.src_path.endswith(".md"):
            return
        print(f"\n[+] Archivo nuevo detectado: {event.src_path}")
        self._schedule(event.src_path, "created")

    def on_modified(self, event: FileModifiedEvent):
        if event.is_directory:
            return
        if not event.src_path.endswith(".md"):
            return
        print(f"\n[*] Archivo modificado: {event.src_path}")
        self._schedule(event.src_path, "modified")

    def on_deleted(self, event: FileDeletedEvent):
        if event.is_directory:
            return
        if not event.src_path.endswith(".md"):
            return
        print(f"\n[-] Archivo eliminado: {event.src_path}")
        self._schedule(event.src_path, "deleted")

    def on_moved(self, event: FileMovedEvent):
        if event.is_directory:
            return
        if not event.dest_path.endswith(".md"):
            return
        # Treat as delete + create
        if event.src_path.endswith(".md"):
            print(f"\n[-] Archivo movido/renombrado (origen): {event.src_path}")
            self._schedule(event.src_path, "deleted")
        print(f"\n[+] Archivo movido (destino): {event.dest_path}")
        self._schedule(event.dest_path, "created")


# ── Watch principal ────────────────────────────────────────────────────────

def watch(content_dir: Path, verbose: bool = False):
    """Inicia el observer watchdog sobre content_dir."""
    init_db()

    print(f"=== Alexandria — Watch Mode ===")
    print(f"  Vigilando: {content_dir}")
    print(f"  Presiona Ctrl+C para detener")
    print()

    handler = DebouncedHandler(
        callback=lambda fp, et: _handle_event(fp, et, content_dir),
        debounce=DEBOUNCE_SECONDS,
    )

    observer = Observer()
    observer.schedule(handler, str(content_dir), recursive=True)
    observer.start()

    print("  Watch activo. Esperando cambios...\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n  Deteniendo watch...")
        observer.stop()
    observer.join()
    print("  Detenido.")


def _handle_event(filepath: str, event_type: str, content_dir: Path):
    fp = Path(filepath)
    parent = content_dir

    if event_type == "deleted":
        delete_article(fp)
    else:
        # created or modified
        if not fp.exists():
            return
        upsert_article(fp)


# ── Re-index completo de todo ──────────────────────────────────────────────

def reindex_all(content_dir: Path, verbose: bool = False):
    """Re-indexa todos los archivos del content directory."""
    init_db()

    md_files = list(content_dir.rglob("*.md"))
    print(f"Re-indexando {len(md_files)} archivos...")

    conn = get_db()
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    total = 0

    for fp in md_files:
        try:
            rows = process_file(fp)
            if not rows:
                continue

            source = str(fp.relative_to(fp.parents[1]))

            # Eliminar anterior
            conn.execute("DELETE FROM contents WHERE source = ?", (source,))

            # Insertar nuevo
            records = [
                (source, title, domain, subtopic, chunk, chunk_idx, total_chunks, has_images)
                for title, domain, subtopic, chunk, chunk_idx, total_chunks, has_images in rows
            ]
            conn.executemany(
                "INSERT INTO contents (source,title,domain,subtopic,chunk,chunk_idx,total_chunks,has_images) "
                "VALUES (?,?,?,?,?,?,?,?)",
                records,
            )
            total += len(records)

            if verbose:
                print(f"  {fp.name}: {len(rows)} chunks")

        except Exception as e:
            print(f"  ERROR {fp.name}: {e}")

    conn.commit()
    conn.close()
    print(f"\nRe-index completo: {total} chunks de {len(md_files)} archivos.")


# ── CLI ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Alexandria — Indexación incremental con watch mode"
    )
    parser.add_argument(
        "--content", "-c",
        type=Path,
        default=Path(__file__).parent.parent / "content",
        help="Carpeta content/ a vigilar",
    )
    parser.add_argument(
        "--once", "-1",
        action="store_true",
        help="Re-indexa todo y sale (sin watch)",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Muestra cada archivo procesado",
    )

    args = parser.parse_args()

    if args.once:
        reindex_all(args.content, verbose=args.verbose)
    else:
        watch(args.content, verbose=args.verbose)


if __name__ == "__main__":
    main()

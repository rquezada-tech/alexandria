#!/usr/bin/env python3
"""
Alexandria - Script de ingestión optimizado
"""
import re
import sys
from pathlib import Path
from typing import Optional

import frontmatter

sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))
from db import init_db, clear_content, get_db


CHUNK_SIZE = 600
CHUNK_OVERLAP = 50
VALID_DOMAINS = {"medicina", "supervivencia", "historia", "mapas", "electronica", "manufactura", "comunicaciones", "herramientas"}
BATCH_SIZE = 10000


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
    source = str(filepath.relative_to(filepath.parents[1]))
    has_images = int(bool(re.search(r"!\[.*?\]\(.*?\)", markdown_body)))

    return [(source, title, domain, subtopic, c, i, len(chunks), has_images) for i, c in enumerate(chunks)]


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Ingesta conocimiento en Alexandria")
    parser.add_argument("--content", type=Path, default=Path(__file__).parent.parent / "content")
    parser.add_argument("--clear", action="store_true")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    init_db()

    if args.clear:
        print("Limpiando base de datos...")
        clear_content()

    md_files = list(args.content.rglob("*.md"))
    print(f"Procesando {len(md_files)} archivos...")
    print(f"Batch size: {BATCH_SIZE}")

    conn = get_db()
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA cache_size=100000")
    total_chunks = 0
    batch = []

    for i, fp in enumerate(md_files):
        rows = process_file(fp)
        if rows:
            batch.extend(rows)

        if len(batch) >= BATCH_SIZE:
            conn.executemany("""
                INSERT INTO contents (source,title,domain,subtopic,chunk,chunk_idx,total_chunks,has_images)
                VALUES (?,?,?,?,?,?,?,?)
            """, batch)
            total_chunks += len(batch)
            conn.commit()
            print(f"  {i+1}/{len(md_files)} | {total_chunks} chunks | batch OK")
            batch = []

        if args.verbose and (i + 1) % 1000 == 0:
            print(f"  Progreso: {i+1}/{len(md_files)} archivos")

    if batch:
        conn.executemany("""
            INSERT INTO contents (source,title,domain,subtopic,chunk,chunk_idx,total_chunks,has_images)
            VALUES (?,?,?,?,?,?,?,?)
        """, batch)
        total_chunks += len(batch)
        conn.commit()
        print(f"  {len(md_files)}/{len(md_files)} | {total_chunks} chunks | final batch OK")

    print("Construyendo índice FTS5...")
    conn.commit()
    try:
        conn.execute("INSERT INTO contents_fts(contents_fts) VALUES('rebuild')")
        conn.commit()
        print("  FTS rebuild OK")
    except Exception as e:
        print(f"  FTS rebuild warning: {e}")

    conn.close()
    print(f"\nListo: {len(md_files)} archivos → {total_chunks} chunks ingestados")


if __name__ == "__main__":
    main()

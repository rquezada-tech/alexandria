#!/usr/bin/env python3
"""
Alexandria - Script de ingestión
Convierte archivos Markdown de content/ en chunks y los indexa en SQLite FTS5
"""
import re
import sys
import json
from pathlib import Path
from typing import Optional

import frontmatter
from tqdm import tqdm

sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))
from db import init_db, insert_content, clear_content


CHUNK_SIZE = 600       # palabras por chunk (conservador para embeddings)
CHUNK_OVERLAP = 50    # palabras de solape entre chunks
VALID_DOMAINS = {"medicina", "supervivencia", "historia", "mapas"}


def parse_frontmatter(post):
    """Extrae metadatos del frontmatter."""
    domain = post.get("domain", "").lower().strip()
    subtopic = post.get("subtopic", "").lower().strip() or None

    if domain not in VALID_DOMAINS:
        return None, None

    return domain, subtopic


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """
    Divide el texto en chunks con overlap.
    Split primario: por párrafos (doble newline).
    Split secundario: por oración si el párrafo es muy largo.
    """
    # Limpiar exceso de whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

    chunks = []
    current_words = []
    current_count = 0

    for para in paragraphs:
        words = para.split()

        if current_count + len(words) <= chunk_size:
            current_words.append(para)
            current_count += len(words)
        else:
            # Guardar chunk actual
            if current_words:
                chunks.append(" ".join(current_words))

            # Overlap: mantener últimas palabras
            if overlap > 0 and current_words:
                overlap_text = " ".join(current_words)
                overlap_words = overlap_text.split()[-overlap:]
                current_words = [" ".join(overlap_words), para]
                current_count = len(overlap_words) + len(words)
            else:
                current_words = [para]
                current_count = len(words)

    # Último chunk
    if current_words:
        chunks.append(" ".join(current_words))

    return chunks


def extract_images_from_markdown(markdown: str) -> bool:
    """Detecta si el markdown contiene referencias a imágenes."""
    return bool(re.search(r"!\[.*?\]\(.*?\)", markdown))


def ingest_file(filepath: Path, verbose: bool = False) -> int:
    """Procesa un archivo .md y lo ingiere en la base de datos."""
    try:
        post = frontmatter.loads(filepath.read_text(encoding="utf-8"))
    except Exception as e:
        if verbose:
            print(f"  [SKIP] {filepath.name}: {e}")
        return 0

    domain, subtopic = parse_frontmatter(post)
    if not domain:
        if verbose:
            print(f"  [SKIP] {filepath.name}: domain inválido o ausente")
        return 0

    title = post.get("title", filepath.stem)
    markdown_body = str(post.content)

    # Limpiar markdown para texto (mantener énfasis pero quitar sintaxis)
    text = re.sub(r"#{1,6}\s+", "", markdown_body)  # headers
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)  # links
    text = re.sub(r"!\[[^\]]*]\([^\)]+\)", "", text)  # imágenes
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)  # bold
    text = re.sub(r"\*([^*]+)\*", r"\1", text)  # italic
    text = re.sub(r"`([^`]+)`", r"\1", text)  # inline code
    text = re.sub(r"\n{3,}", "\n\n", text)

    has_images = extract_images_from_markdown(markdown_body)
    chunks = chunk_text(text)

    source = str(filepath.relative_to(filepath.parents[1]))

    for idx, chunk in enumerate(chunks):
        insert_content(
            source=source,
            title=title,
            domain=domain,
            subtopic=subtopic,
            chunk=chunk,
            chunk_idx=idx,
            total_chunks=len(chunks),
            has_images=has_images,
        )

    if verbose:
        print(f"  [OK] {filepath.name}: {len(chunks)} chunks")

    return len(chunks)


def ingest_folder(folder: Path, verbose: bool = False) -> dict:
    """Ingiera todos los .md de una carpeta recursivamente."""
    md_files = list(folder.rglob("*.md"))
    if not md_files:
        if verbose:
            print(f"No se encontraron archivos .md en {folder}")
        return {"files": 0, "chunks": 0}

    total_chunks = 0
    for fp in tqdm(md_files, desc="Ingestando", disable=not verbose):
        total_chunks += ingest_file(fp, verbose=verbose)

    return {
        "files": len(md_files),
        "chunks": total_chunks,
    }


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Ingesta conocimiento en Alexandria")
    parser.add_argument(
        "--content",
        type=Path,
        default=Path(__file__).parent.parent / "content",
        help="Carpeta de contenidos (.md)",
    )
    parser.add_argument(
        "--clear",
        action="store_true",
        help="Limpiar base antes de ingestar",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Salida detallada",
    )
    args = parser.parse_args()

    init_db()

    if args.clear:
        print("Limpiando base de datos...")
        clear_content()

    print(f"Ingestando contenido desde: {args.content}")
    result = ingest_folder(args.content, verbose=args.verbose)

    print(f"\nListo: {result['files']} archivos → {result['chunks']} chunks ingestados")


if __name__ == "__main__":
    main()

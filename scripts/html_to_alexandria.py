#!/usr/bin/env python3
"""
Convierte artículos HTML extraídos de Wikipedia (formato ZIM)
al formato Alexandria (Markdown + YAML frontmatter).
"""

import os
import sys
import re
import html
from pathlib import Path


def make_frontmatter(title: str, domain: str, subtopic: str) -> str:
    return f'''---
title: "{title}"
domain: {domain}
subtopic: {subtopic}
source: wikipedia
has_images: false
---

'''


def extract_title_and_text(html_content):
    """Extrae título y texto plano de artículo HTML de Wikipedia."""
    
    # Extraer título
    title_match = re.search(r'<title>(.*?)</title>', html_content, re.DOTALL | re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else "Sin título"
    title = html.unescape(title).replace(" - Wikipedia, la enciclopedia libre", "").replace(" - Wikipedia, la enciclopèdia lliure", "").strip()
    
    # Eliminar scripts, styles, nav
    content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<nav[^>]*>.*?</nav>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<table[^>]*class="[^"]*wikitable[^"]*"[^>]*>.*?</table>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Obtener el contenido del artículo (body)
    body_match = re.search(r'<div[^>]*id="mw-content-text"[^>]*>(.*?)</div>\s*</div>\s*</div>\s*<div[^>]*class="printfooter"', content, re.DOTALL | re.IGNORECASE)
    if not body_match:
        body_match = re.search(r'<div[^>]*class="mw-parser-output"[^>]*>(.*?)</div>', content, re.DOTALL | re.IGNORECASE)
    
    if body_match:
        text = body_match.group(1)
    else:
        text = content
    
    # Eliminar HTML tags pero preservar párrafos
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'</p>', '\n\n', text)
    text = re.sub(r'</div>', '\n', text)
    text = re.sub(r'<h[1-6][^>]*>', '\n## ', text)
    text = re.sub(r'</h[1-6]>', '\n', text)
    text = re.sub(r'<li[^>]*>', '\n- ', text)
    text = re.sub(r'</li>', '', text)
    text = re.sub(r'<[^>]+>', '', text)
    
    # Decodificar entidades HTML
    text = html.unescape(text)
    
    # Limpiar whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()
    
    return title, text


def make_slug(title: str) -> str:
    """Genera un slug URL-friendly."""
    slug = title.lower()
    slug = re.sub(r'[àáâãäå]', 'a', slug)
    slug = re.sub(r'[èéêë]', 'e', slug)
    slug = re.sub(r'[ìíîï]', 'i', slug)
    slug = re.sub(r'[òóôõö]', 'o', slug)
    slug = re.sub(r'[ùúûü]', 'u', slug)
    slug = re.sub(r'[ñ]', 'n', slug)
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = slug.strip('-')
    return slug[:80]


def process_file(src_path: Path, out_dir: Path, domain: str, subtopic: str):
    """Procesa un archivo HTML individual."""
    try:
        with open(src_path, 'r', encoding='utf-8', errors='replace') as f:
            html_content = f.read()
        
        title, text = extract_title_and_text(html_content)
        
        if len(text) < 200:
            return None  # Muy corto, skip
        
        slug = make_slug(title)
        filename = f"{slug}.md"
        out_path = out_dir / filename
        
        # Evitar sobrescribir si existe
        counter = 1
        while out_path.exists():
            filename = f"{slug}-{counter}.md"
            out_path = out_dir / filename
            counter += 1
        
        content = make_frontmatter(title, domain, subtopic) + text
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return out_path.name
        
    except Exception as e:
        return None


def main():
    if len(sys.argv) < 4:
        print("Uso: html_to_alexandria.py <input_dir> <output_dir> <domain> <subtopic>")
        sys.exit(1)
    
    input_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    domain = sys.argv[3]
    subtopic = sys.argv[4] if len(sys.argv) > 4 else domain
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    files = list(input_dir.glob("*.html"))
    total = len(files)
    converted = 0
    skipped_short = 0
    
    print(f"Procesando {total} archivos HTML...")
    
    for i, f in enumerate(files):
        result = process_file(f, output_dir, domain, subtopic)
        if result:
            converted += 1
        else:
            skipped_short += 1
        
        if (i + 1) % 500 == 0:
            print(f"Progreso: {i+1}/{total} | Convertidos: {converted} | Omitidos: {skipped_short}")
    
    print(f"\nListo: {converted} archivos convertidos, {skipped_short} omitidos (muy cortos)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

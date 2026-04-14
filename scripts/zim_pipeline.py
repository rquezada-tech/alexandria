#!/usr/bin/env python3
"""
Alexandria - Pipeline ZIM completo
Usa el extractor C++ (zim_extract) para extraer artículos HTML desde ZIM,
luego los convierte al formato Alexandria con frontmatter.
"""
import os
import re
import sys
import shutil
import subprocess
import urllib.request
from pathlib import Path


TOPICS = {
    "medicine":    {"dump": "wikipedia_es_medicine",    "domain": "medicina",     "variant": "nopic", "date": "2025-10"},
    "history":     {"dump": "wikipedia_es_history",      "domain": "historia",     "variant": "nopic", "date": "2025-09"},
    "chemistry":   {"dump": "wikipedia_es_chemistry",    "domain": "manufactura",  "variant": "nopic", "date": "2025-10"},
    "physics":     {"dump": "wikipedia_es_physics",      "domain": "manufactura",  "variant": "nopic", "date": "2025-10"},
    "mathematics": {"dump": "wikipedia_es_mathematics",  "domain": "manufactura",  "variant": "nopic", "date": "2025-09"},
    "computer":    {"dump": "wikipedia_es_computer",     "domain": "electronica",  "variant": "nopic", "date": "2025-10"},
    "geography":   {"dump": "wikipedia_es_geography",    "domain": "historia",     "variant": "nopic", "date": "2025-10"},
    "molcell":     {"dump": "wikipedia_es_molcell",     "domain": "medicina",     "variant": "nopic", "date": "2025-10"},
}

ZIM_BASE_URL  = "https://download.kiwix.org/zim/wikipedia/"
EXTRACTOR     = Path(__file__).parent / "zim_extract"
HTML2ALEX     = Path(__file__).parent / "html_to_alexandria.py"
ALEX_ROOT     = Path(__file__).parent.parent
DATA_DIR      = ALEX_ROOT / "data" / "wikipedia"
CONTENT_DIR   = ALEX_ROOT / "content"
VENV_PY       = ALEX_ROOT / ".venv" / "bin" / "python"


def get_zim_filename(cfg: dict) -> str:
    return f"{cfg['dump']}_{cfg['variant']}_{cfg['date']}.zim"


def get_zim_url(cfg: dict) -> str:
    return ZIM_BASE_URL + get_zim_filename(cfg)


def download_zim(topic: str, cfg: dict, data_dir: Path) -> Path | None:
    filename = get_zim_filename(cfg)
    dest = data_dir / filename

    if dest.exists() and dest.stat().st_size > 1024:
        size_mb = dest.stat().st_size / 1024 / 1024
        print(f"  [SKIP] {filename} ({size_mb:.1f} MB, ya existe)")
        return dest

    url = get_zim_url(cfg)
    print(f"  [DOWN] {filename}")
    print(f"         {url}")

    try:
        urllib.request.urlretrieve(url, dest)
        size_mb = dest.stat().st_size / 1024 / 1024
        print(f"  [OK]   {filename} ({size_mb:.1f} MB)")
        return dest
    except Exception as e:
        print(f"  [ERR] Descarga fallida: {e}")
        if dest.exists():
            dest.unlink()
        return None


def extract_zim(zim_path: Path, extract_dir: Path) -> int:
    extract_dir.mkdir(parents=True, exist_ok=True)
    cmd = [str(EXTRACTOR), str(zim_path), str(extract_dir)]
    print(f"  [EXTRACT] {zim_path.name}")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        if result.returncode != 0:
            print(f"  [ERR] Extractor: {result.stderr[:500]}")
            return 0
        html_files = list(extract_dir.glob("*.html"))
        print(f"  [OK]   {len(html_files)} articulos extraidos")
        return len(html_files)
    except subprocess.TimeoutExpired:
        print(f"  [ERR] Timeout extractor (10 min)")
        return 0
    except Exception as e:
        print(f"  [ERR] {e}")
        return 0


def convert_articles(extract_dir: Path, domain: str, subtopic: str) -> int:
    output = CONTENT_DIR / domain / subtopic
    output.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, str(HTML2ALEX), str(extract_dir), str(output), domain, subtopic]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if result.returncode != 0:
            print(f"  [ERR] Conversion: {result.stderr[:300]}")
            return 0
        for line in result.stdout.strip().split("\n"):
            if "convertidos" in line or "archivos convertidos" in line or "Listo" in line:
                print(f"  [OK]   {line.strip()}")
                break
        return 1
    except Exception as e:
        print(f"  [ERR] {e}")
        return 0


def ingest() -> bool:
    venv_python = VENV_PY if VENV_PY.exists() else (ALEX_ROOT / "venv" / "bin" / "python")
    if not venv_python.exists():
        print(f"  [ERR] venv python no encontrado")
        return False

    ingest_script = ALEX_ROOT / "backend" / "ingest.py"
    cmd = [str(venv_python), str(ingest_script), "--clear"]
    print(f"  [INGEST] Re-indexando base de datos (puede tardar unos minutos)...")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ALEX_ROOT), timeout=600)
        if result.returncode != 0:
            print(f"  [ERR] Ingest: {result.stderr[:300]}")
            return False
        for line in result.stdout.strip().split("\n"):
            if "chunk" in line.lower() or "articul" in line.lower() or "listo" in line.lower():
                print(f"  [OK]   {line.strip()}")
        return True
    except subprocess.TimeoutExpired:
        print(f"  [ERR] Ingest timeout (10 min)")
        return False
    except Exception as e:
        print(f"  [ERR] {e}")
        return False


def run_topic(topic: str, cfg: dict) -> bool:
    print(f"\n{'='*60}")
    print(f"  Topic: {topic}  ->  Domain: {cfg['domain']}")
    print(f"{'='*60}")

    zim_path = download_zim(topic, cfg, DATA_DIR)
    if not zim_path:
        return False

    extract_dir = DATA_DIR / "extract" / topic
    count = extract_zim(zim_path, extract_dir)
    if count == 0:
        return False

    convert_articles(extract_dir, cfg["domain"], cfg["domain"])
    return True


def list_topics():
    print("Topics ZIM disponibles:")
    for t, cfg in TOPICS.items():
        fn = get_zim_filename(cfg)
        print(f"  {t:>15}: {fn:50} -> {cfg['domain']}")


def main():
    args = sys.argv[1:]

    if "--list" in args or (not args):
        list_topics()
        print(f"\nUso: {sys.argv[0]} <topic> [topic ...]")
        print(f"     {sys.argv[0]} --all")
        return

    if "--all" in args:
        topics = list(TOPICS.keys())
    else:
        topics = [a for a in args if a in TOPICS]

    if not topics:
        print("Topics no encontrados. Usa --list para ver disponibles.")
        return

    print(f"Pipeline ZIM  |  {len(topics)} topic(s)")
    ok = 0
    for topic in topics:
        if run_topic(topic, TOPICS[topic]):
            ok += 1

    if ok > 0:
        print(f"\n{'='*60}")
        print(f"  Todos los topics descargados. Ejecutando ingest final...")
        ingest()

    print(f"\nListo: {ok}/{len(topics)} topics procesados OK")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Alexandria - Setup de librerías para mapas offline.
Descarga MapLibre GL JS + CSS + PMTiles.js a frontend/lib/

Uso:
    python scripts/setup_maps_libs.py
"""
import urllib.request
import shutil
import sys
from pathlib import Path

LIB_DIR = Path(__file__).parent.parent / "frontend" / "lib"
LIB_DIR.mkdir(parents=True, exist_ok=True)

MAPLIBRE_VERSION = "4.8.2"
PMTILES_URL = "https://unpkg.com/pmtiles@3.2.1/dist/pmtiles.js"

ASSETS = {
    f"maplibre-gl.js": f"https://unpkg.com/maplibre-gl@{MAPLIBRE_VERSION}/dist/maplibre-gl.js",
    f"maplibre-gl.css": f"https://unpkg.com/maplibre-gl@{MAPLIBRE_VERSION}/dist/maplibre-gl.css",
    f"pmtiles.js": PMTILES_URL,
}


def download(url: str, dest: Path):
    print(f"  Descargando {dest.name}...")
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            content = r.read()
        dest.write_bytes(content)
        size_kb = len(content) / 1024
        print(f"    OK: {size_kb:.1f} KB")
    except Exception as e:
        print(f"    ERROR: {e}", file=sys.stderr)
        if dest.exists():
            dest.unlink()
        return False
    return True


def main():
    print("=== Setup de librerías para mapas offline ===\n")
    print(f"Destino: {LIB_DIR}\n")

    all_ok = True
    for filename, url in ASSETS.items():
        dest = LIB_DIR / filename
        if dest.exists():
            size_kb = dest.stat().st_size / 1024
            print(f"  {dest.name}: ya existe ({size_kb:.1f} KB) — skip")
            continue

        ok = download(url, dest)
        if not ok:
            all_ok = False

    print()
    if all_ok:
        print("Setup completo. Archivos en frontend/lib/:")
        for f in sorted(LIB_DIR.iterdir()):
            print(f"  {f.name} ({f.stat().st_size / 1024:.1f} KB)")
    else:
        print("Hubo errores. Puedes descargar manualmente desde:")
        for filename, url in ASSETS.items():
            print(f"  {url}")
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Alexandria - Descargador de mapas offline (PMTiles)
Descarga regiones geográficas en formato PMTiles desde Protomaps.

Uso:
    python scripts/download_pmtiles.py --region chile --bbox -75 -55 -20 -90
    python scripts/download_pmtiles.py --region europe --bbox -30 25 70 80
    python scripts/download_pmtiles.py --list-regions
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path

# ── Regiones predefinidas ────────────────────────────────
REGIONS = {
    "chile": {
        "name": "Chile",
        "bbox": [-75.5, -55.0, -66.0, -17.5],  # [west, south, east, north]
        "zoom": "12",  # zoom mínimo para descarga
        "note": "Chile continental + insular",
    },
    "sudamerica": {
        "name": "Sudamérica",
        "bbox": [-82.0, -56.0, -34.0, 13.0],
        "zoom": "8",
        "note": "Todo el subcontinente",
    },
    "latam": {
        "name": "Latinoamérica",
        "bbox": [-120.0, -56.0, -32.0, 33.0],
        "zoom": "7",
        "note": "Desde México hasta Argentina",
    },
    "europa": {
        "name": "Europa",
        "bbox": [-30.0, 25.0, 70.0, 80.0],
        "zoom": "8",
        "note": "Continente europeo completo",
    },
    "world": {
        "name": "Mundo (baja resolución)",
        "bbox": [-180.0, -85.0, 180.0, 85.0],
        "zoom": "6",
        "note": "Mapa mundial para contexto general (archivo pequeño ~5MB)",
    },
}

PROTOMAPS_DL = "https://download.protomaps.com"
DATA_DIR = Path(__file__).parent.parent / "data" / "maps"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def check_dependencies():
    """Verifica que curl y unzip estén disponibles."""
    for cmd in ["curl", "unzip"]:
        if not shutil.which(cmd):
            print(f"ERROR: '{cmd}' no está instalado.", file=sys.stderr)
            print(f"  Instálalo con: brew install {cmd}  (macOS)")
            print(f"  o: apt-get install {cmd}  (Linux)")
            sys.exit(1)


def download_pmtiles(region_key: str):
    """Descarga un PMTiles pre-compilado de Protomaps para la región."""
    check_dependencies()

    region = REGIONS.get(region_key)
    if not region:
        print(f"Región desconocida: {region_key}")
        print(f"Disponibles: {', '.join(REGIONS.keys())}")
        sys.exit(1)

    bbox = region["bbox"]
    west, south, east, north = bbox
    name = region["name"]
    note = region["note"]

    print(f"=== Descargando: {name} ===")
    print(f"  Bbox: {bbox}")
    print(f"  Zoom mínimo: {region['zoom']}")
    print(f"  Nota: {note}")
    print()

    # Protomaps usa API de descarga por bounding box
    # URL: https://download.protomaps.com/{z}/{x}/{y}.mvt
    # Para PMTiles pre-generados usamos el build API
    # Protomaps ofrece: https://build.protomaps.com/ [para tiles individuales]
    # Alternativa: usar planetiler o generar desde OSM
    #
    # Para este script usamos la estrategia de "tilesbundle" de Protomaps
    # que son archivos PMTiles pre-generados por región
    #
    # Fuente: https://github.com/protomaps/PMTiles/blob/main/docs/server.md#public-download

    output_file = DATA_DIR / f"{region_key}.pmtiles"
    if output_file.exists():
        size_mb = output_file.stat().st_size / (1024 * 1024)
        print(f"  Ya existe: {output_file.name} ({size_mb:.1f} MB)")
        print("  Usa --force para re-descargar.")
        return

    # Estrategia: descargar PMTiles desde Protomaps
    # Protomaps tiene downloads públicos en:
    # https://build.protomaps.com/ - para tiles bajo demanda
    # https://d2hiv4l5b3j5vq.cloudfront.net/ - CDN de tiles
    #
    # Para regiones específicas, Protomaps proporciona archivos ZIP
    # con PMTiles pre-generados. La URL base es:
    # https://download.protomaps.com/{region}

    url = f"{PROTOMAPS_DL}/extracts/{region_key}_no_labels.zip"

    print(f"  URL: {url}")
    print(f"  Destino: {output_file}")
    print()
    print("  Descargando... (puede tardar varios minutos)")

    tmp_zip = DATA_DIR / f"{region_key}.zip"
    tmp_dir = DATA_DIR / f"{region_key}_extract"

    try:
        # Descargar con curl (muestra progreso)
        result = subprocess.run(
            [
                "curl", "-L", "--progress-bar",
                "-o", str(tmp_zip),
                url,
            ],
            check=True,
        )

        print("  Descargado. Extrayendo...")

        # Extraer el ZIP
        with zipfile.ZipFile(tmp_zip, "r") as z:
            z.extractall(str(tmp_dir))

        # Buscar el archivo .pmtiles dentro de la extracción
        pmtiles_files = list(tmp_dir.glob("**/*.pmtiles"))
        if not pmtiles_files:
            #也可能直接解压出 .pmtiles
            pmtiles_files = list(tmp_dir.glob("**/*"))

        print(f"  Archivos extraídos: {[f.name for f in pmtiles_files[:5]]}")

        # Mover el PMTiles al destino final
        extracted_pmtiles = None
        for f in pmtiles_files:
            if f.suffix == ".pmtiles":
                extracted_pmtiles = f
                break

        if not extracted_pmtiles:
            print(f"  ERROR: No se encontró archivo .pmtiles en la extracción.", file=sys.stderr)
            print(f"  Archivos: {list(tmp_dir.glob('**/*'))}", file=sys.stderr)
            sys.exit(1)

        shutil.move(str(extracted_pmtiles), str(output_file))
        size_mb = output_file.stat().st_size / (1024 * 1024)
        print(f"  OK: {output_file.name} ({size_mb:.1f} MB)")

    except subprocess.CalledProcessError as e:
        print(f"  ERROR al descargar: {e}", file=sys.stderr)
        print()
        print("  Alternativa: descarga manualmente desde")
        print(f"  https://download.protomaps.com/extracts/{region_key}_no_labels.zip")
        print(f"  y coloca el archivo .pmtiles en {DATA_DIR}/")
    finally:
        # Limpiar temporales
        if tmp_zip.exists():
            tmp_zip.unlink()
        if tmp_dir.exists():
            shutil.rmtree(tmp_dir)


def list_available():
    """Lista las regiones disponibles y mapas ya descargados."""
    print("=== Regiones disponibles ===\n")
    for key, region in REGIONS.items():
        pmtiles_file = DATA_DIR / f"{key}.pmtiles"
        status = ""
        if pmtiles_file.exists():
            size_mb = pmtiles_file.stat().st_size / (1024 * 1024)
            status = f"  [DESCARGADO: {size_mb:.1f} MB]"
        else:
            status = "  [No descargado]"
        print(f"  {key}: {region['name']}{status}")
        print(f"         Bbox: {region['bbox']} | Zoom: {region['zoom']} | {region['note']}")
        print()


def main():
    parser = argparse.ArgumentParser(
        description="Descarga mapas offline en formato PMTiles para Alexandria"
    )
    parser.add_argument(
        "--region", "-r",
        help="Región a descargar (chile, sudamerica, latam, europa, world)",
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="Lista regiones disponibles y estado de descarga",
    )
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Fuerza re-descarga aunque ya exista",
    )
    parser.add_argument(
        "--bbox",
        nargs=4, type=float, metavar=("WEST", "SOUTH", "EAST", "NORTH"),
        help="Bounding box personalizado: west south east north",
    )
    parser.add_argument(
        "--output", "-o",
        type=Path,
        default=None,
        help="Ruta de salida del archivo PMTiles",
    )

    args = parser.parse_args()

    if args.list:
        list_available()
        return

    if not args.region:
        parser.print_help()
        print()
        list_available()
        return

    download_pmtiles(args.region)


if __name__ == "__main__":
    main()

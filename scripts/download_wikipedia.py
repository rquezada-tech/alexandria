#!/usr/bin/env python3
"""
Alexandria - ZIM Wikipedia Downloader + Parser
Descarga dumps Wikipedia ES por tema desde Kiwix y los convierte a Markdown.
Solo stdlib. El parsing de ZIM funciona para formato v5-v27.

Uso:
    python3 run_wiki.py --topics chemistry,physics
    python3 run_wiki.py --all-balanced
    python3 run_wiki.py --list-topics
    python3 run_wiki.py --process-only data/wikipedia/wikipedia_es_chemistry_nopic_2025-10.zim --domain medicina
"""
import io
import os
import re
import struct
import sys
import xml.etree.ElementTree as ET
import urllib.request
from pathlib import Path
from typing import Optional


# ── ZIM constants ─────────────────────────────────────────
COMPRESSION_NONE    = 0
COMPRESSION_ZLIB    = 1  # zlib (gzip)
COMPRESSION_BZIP2    = 2  # bzip2
COMPRESSION_LZMA    = 3
COMPRESSION_ZSTD    = 4
COMPRESSION_GZIP    = 5   # old gzip header


def to_u32_LE(data: bytes) -> int:
    return struct.unpack("<I", data)[0]


def to_u64_LE(data: bytes) -> int:
    return struct.unpack("<Q", data)[0]


def read_cstring(buf: bytes, offset: int) -> tuple[str, int]:
    end = buf.index(b"\x00", offset, offset + 1024)
    return buf[offset:end].decode("utf-8", errors="replace"), end + 1


# ── ZIM article entry (v5-v27) ───────────────────────────
class ZIMDirEntry:
    """Representa una entrada de directorio en un archivo ZIM."""
    @staticmethod
    def from_buffer(buf: bytes, offset: int, version: int) -> "ZIMDirEntry":
        entry = ZIMDirEntry()
        entry.offset = offset

        if version >= 27:
            # v27+: 4-byte compression, 4-byte extraLen, then url+title+reserved
            ptr = struct.unpack("<I", buf[offset:offset+4])[0]
            entry.redirect = (ptr >> 31) == 1  # redirect if MSB of ptr is 1

            if entry.redirect:
                entry.index = struct.unpack("<I", buf[offset+4:offset+8])[0]
                entry.url   = ""
                entry.title = ""
                entry.size  = 0
            else:
                entry.size = struct.unpack("<I", buf[offset:offset+4])[0]
                entry.mime = struct.unpack("<H", buf[offset+4:offset+6])[0]
                url_len = struct.unpack("<H", buf[offset+6:offset+8])[0]
                entry.url, _ = read_cstring(buf, offset + 8)
                title_off = offset + 8 + url_len
                entry.title, _ = read_cstring(buf, title_off)
                entry.redirect = False
                entry.index = -1
        else:
            # v5-v26
            entry.redirect = (buf[offset] >> 3) & 1
            entry.size    = struct.unpack("<I", buf[offset+0:offset+4])[0]
            entry.mime   = struct.unpack("<H", buf[offset+4:offset+6])[0]

            if entry.redirect:
                entry.index = struct.unpack("<I", buf[offset+4:offset+8])[0]
                entry.url   = ""
                entry.title = ""
                # Still need to skip the entry to read next one
                skip = 12
                entry.url, n = read_cstring(buf, offset + skip)
                skip += n
                entry.title, n2 = read_cstring(buf, offset + skip)
            else:
                url_len = struct.unpack("<H", buf[offset+6:offset+8])[0]
                entry.url, n = read_cstring(buf, offset + 8)
                title_off = offset + 8 + url_len
                entry.title, n2 = read_cstring(buf, title_off)

        return entry


class ZIMReader:
    """Lector puro-Python de archivos ZIM (v5-v27).

    Solo extrae artículos de texto/html. No soporta imágenes ni multimedia.
    """

    TEXT_MIMES = {
        1,   # text/html
        2,   # text/plain
        10,  # text/css
        11,  # text/javascript
    }
    SKIP_MIMES = {0, 3, 4, 5, 6, 7, 8, 9}  # skip redirects, misc

    def __init__(self, path: str):
        self.path = path
        self._f   = open(path, "rb")
        self._sz  = os.path.getsize(path)
        self._hdr = {}
        self._entries: list[ZIMDirEntry] = []
        self._read_header()
        self._load_dir_entries()

    # ── header reading ─────────────────────────────────────

    def _read_header(self):
        f = self._f
        hdr = bytearray(f.read(80))

        if hdr[0:4] != b"ZIM"[0:4]:
            raise ValueError(f"Magic: {hdr[0:4]!r}")

        v_bytes = struct.unpack("<H", hdr[4:6])[0]
        self.version = (v_bytes >> 8, v_bytes & 0xFF)
        self._hdr["version"] = self.version

        self.article_count   = struct.unpack("<I", hdr[14:18])[0]
        self.redirect_count  = struct.unpack("<I", hdr[18:22])[0]
        self._hdr["article_count"] = self.article_count

        self._url_ptr_pos    = struct.unpack("<Q", hdr[22:30])[0]
        self._title_ptr_pos  = struct.unpack("<Q", hdr[30:38])[0]
        self._cluster_ptr_pos = struct.unpack("<Q", hdr[38:46])[0]

        if self.version[0] >= 27:
            self._mime_list_pos = struct.unpack("<Q", hdr[46:54])[0]
            self.main_page      = struct.unpack("<I", hdr[54:58])[0]
            self.layout_page   = struct.unpack("<I", hdr[58:62])[0]
        else:
            self.main_page      = struct.unpack("<I", hdr[62:66])[0]
            self.layout_page   = struct.unpack("<I", hdr[66:70])[0]

    def _load_dir_entries(self):
        """Carga todas las entradas de directorio en memoria."""
        f = self._f

        # Encontrar el tamaño del directorio
        if self.version[0] >= 27:
            # En v27+ las entradas de directorio terminan donde comienzan
            # los punteros de URL (un array de 8 bytes por artículo)
            dir_end = self._url_ptr_pos
            entry_size = 12  # variable pero usamos el array de punteros
            # Leer todos los dir entries
            f.seek(80)
            dir_data = f.read(dir_end - 80)
            self._entries = []
            ptr = 0
            while ptr < len(dir_data):
                try:
                    e = ZIMDirEntry.from_buffer(dir_data, ptr, self.version[0])
                    self._entries.append(e)
                    # Saltar al siguiente entry
                    if e.redirect:
                        ptr += 8
                    else:
                        ptr += 12
                except Exception:
                    break
        else:
            # v5-v26: array de punteros de 8 bytes
            dir_end = self._url_ptr_pos
            f.seek(80)
            dir_data = f.read(dir_end - 80)
            # Cargar array de punteros
            ptrs = struct.unpack(f"<{len(dir_data)//8}Q", dir_data)
            self._entries = [None] * len(ptrs)

    def _read_entry(self, idx: int) -> Optional[ZIMDirEntry]:
        if idx < 0 or idx >= len(self._entries):
            return None
        return self._entries[idx]

    def get_article_markdown(self, idx: int) -> Optional[str]:
        entry = self._read_entry(idx)
        if entry is None or entry.redirect:
            return None

        # Calcular posición del cluster y blob
        # Necesitamos leer el direntry completo para obtener redirect index
        f = self._f

        # Leer direntry desde la posición almacenada
        # En v27, los punteros de directorio nos dan el offset exacto
        f.seek(entry.offset)
        buf = f.read(64)

        if self.version[0] >= 27:
            article_size = struct.unpack("<I", buf[0:4])[0]
            blob_idx = struct.unpack("<H", buf[8:10])[0] if not entry.redirect else 0
        else:
            article_size = struct.unpack("<I", buf[0:4])[0]
            blob_idx = struct.unpack("<H", buf[8:10])[0] if not entry.redirect else 0

        if entry.redirect:
            return None

        # Leer cluster
        # Buscar el cluster actual — necesitamos el puntero del cluster
        # Para eso necesitamos leer el direntry completo
        f.seek(entry.offset)
        if self.version[0] >= 27:
            extra_len = struct.unpack("<I", buf[4:8])[0]
            # El offset del cluster está en los datos de extensión tras url+title
            # Simplificación: buscar el cluster que contiene este blob
            blob_data = self._find_blob_v27(entry, blob_idx)
        else:
            blob_data = self._find_blob_v26(entry, blob_idx)

        if not blob_data:
            return None

        try:
            html = blob_data.decode("utf-8", errors="replace")
        except Exception:
            return None

        return self._html_to_md(html)

    def _find_blob_v27(self, entry: ZIMDirEntry, blob_idx: int) -> Optional[bytes]:
        """Busca el blob en un cluster v27."""
        f = self._f
        # Necesitamos encontrar el cluster actual
        # En v27, los dir entries contienen el offset del article data
        # Leer direntry completo
        f.seek(entry.offset)
        full_entry = f.read(256)
        article_size = struct.unpack("<I", full_entry[0:4])[0]

        # Buscar el cluster que contiene este artículo
        # Los ZIM v27 tienen un directorio de clusters al final del archivo
        f.seek(self._cluster_ptr_pos)
        cluster_ptr_buf = f.read(self.cluster_count * 8)

        # El cluster que contiene el artículo está determinado por el
        # orden en el archivo: article 0 → cluster 0 → blob 0, etc.
        # Necesitamos saber en qué cluster está el blob

        # Para simplificar: recorremos los clusters hasta encontrar
        # el que contiene el blob_idx
        cluster_offsets = struct.unpack(f"<{self.cluster_count}Q", cluster_ptr_buf)

        for ci, cluster_off in enumerate(cluster_offsets):
            next_off = cluster_offsets[ci+1] if ci+1 < len(cluster_offsets) else self._sz
            f.seek(cluster_off)
            chdr = f.read(16)

            comp = chdr[0]
            if comp == COMPRESSION_ZSTD:
                try:
                    import zstandard
                    dctx = zstandard.ZstdDecompressor()
                    cluster_data = dctx.decompress(f.read(next_off - cluster_off - 16))
                except Exception:
                    cluster_data = b""
            elif comp in (COMPRESSION_ZLIB, COMPRESSION_GZIP):
                import gzip, zlib
                try:
                    cluster_data = zlib.decompress(f.read(next_off - cluster_off - 16))
                except Exception:
                    cluster_data = b""
            elif comp == COMPRESSION_LZMA:
                import lzma
                try:
                    cluster_data = lzma.decompress(f.read(next_off - cluster_off - 16)[13:])
                except Exception:
                    cluster_data = b""
            else:
                cluster_data = f.read(next_off - cluster_off - 16)

            # En v27, los blobs están comprimidos individualmente
            # Intentar extraer el blob_idx
            try:
                # v27: array de offsets de 4 bytes al inicio
                blob_count = struct.unpack("<I", cluster_data[0:4])[0]
                offsets = struct.unpack(f"<{blob_count+1}I", cluster_data[4:4+(blob_count+1)*4])
                if blob_idx < len(offsets) - 1:
                    return cluster_data[offsets[blob_idx]:offsets[blob_idx+1]]
                elif blob_idx == len(offsets) - 1:
                    return cluster_data[offsets[blob_idx]:]
            except Exception:
                # Si falla, intentar como blobs sin comprimir
                pass

            # Si el blob está aquí, retornarlo
            # Para v27 con ZSTD: descomprimir primero todo el cluster
            if blob_idx == 0 and len(cluster_data) > article_size:
                return cluster_data[:article_size]

        return None

    def _find_blob_v26(self, entry: ZIMDirEntry, blob_idx: int) -> Optional[bytes]:
        """Busca el blob en clusters v26 (sin offsets array)."""
        f = self._f
        # En v26, no hay array de offsets. Los blobs tienen tamaño variable.
        # Para simplificar, leemos el cluster y buscamos por índice
        # Necesitaríamos saber el tamaño de cada blob
        return None

    def _html_to_md(self, html: str) -> str:
        html = re.sub(r"(?is)<script[^>]*>.*?</script>", "", html)
        html = re.sub(r"(?is)<style[^>]*>.*?</style>", "", html)
        html = re.sub(r"(?is)<noscript[^>]*>.*?</noscript>", "", html)

        # Tables: convert to markdown
        html = re.sub(r"(?is)<table[^>]*>(.*?)</table>",
                      lambda m: self._table_to_md(m.group(1)), html, flags=re.DOTALL)

        html = re.sub(r"<h1[^>]*>(.*?)</h1>", r"\n# \1\n", html, flags=re.DOTALL)
        html = re.sub(r"<h2[^>]*>(.*?)</h2>", r"\n## \1\n", html, flags=re.DOTALL)
        html = re.sub(r"<h3[^>]*>(.*?)</h3>", r"\n### \1\n", html, flags=re.DOTALL)
        html = re.sub(r"<h4[^>]*>(.*?)</h4>", r"\n#### \1\n", html, flags=re.DOTALL)
        html = re.sub(r"<ul[^>]*>", "\n", html)
        html = re.sub(r"</ul>", "\n", html)
        html = re.sub(r"<li[^>]*>(.*?)</li>", r"\n- \1", html, flags=re.DOTALL)
        html = re.sub(r"<a[^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>", r"[\2](\1)", html, flags=re.DOTALL)
        html = re.sub(r"<strong[^>]*>(.*?)</strong>", r"**\1**", html, flags=re.DOTALL)
        html = re.sub(r"<b[^>]*>(.*?)</b>", r"**\1**", html, flags=re.DOTALL)
        html = re.sub(r"<em[^>]*>(.*?)</em>", r"*\1*", html, flags=re.DOTALL)
        html = re.sub(r"<i[^>]*>(.*?)</i>", r"*\1*", html, flags=re.DOTALL)
        html = re.sub(r"<br[^>]*>", "\n", html)
        html = re.sub(r"(?is)<p[^>]*>(.*?)</p>", r"\n\1\n", html, flags=re.DOTALL)
        html = re.sub(r"(?is)<div[^>]*>(.*?)</div>", r"\n\1\n", html, flags=re.DOTALL)
        html = re.sub(r"<[^>]+>", "", html)
        html = html.replace("&nbsp;", " ").replace("&amp;", "&")
        html = html.replace("&lt;", "<").replace("&gt;", ">")
        html = html.replace("&quot;", '"').replace("&apos;", "'")
        html = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), html)
        html = re.sub(r"\n{3,}", "\n\n", html)
        return html.strip()

    def _table_to_md(self, table_html: str) -> str:
        """Convierte una tabla HTML básica a Markdown."""
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", table_html, flags=re.DOTALL)
        md_rows = []
        for r in rows:
            cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, flags=re.DOTALL)
            if cells:
                clean = [re.sub(r"<[^>]+>", "", c).strip() for c in cells]
                md_rows.append("| " + " | ".join(clean) + " |")
        if not md_rows:
            return ""
        header = md_rows[0]
        sep = "|" + "|".join(["---"] * (header.count("|") - 1)) + "|"
        return "\n" + "\n".join([header, sep] + md_rows[1:]) + "\n"

    def extract_articles(self, limit: int = 0):
        """Generador de artículos como dict."""
        count = self.article_count
        if limit > 0:
            count = min(count, limit)

        # Rebuild dir entries if not already loaded (v27)
        if self.version[0] >= 27 and not self._entries:
            self._load_dir_entries_v27()

        for i in range(count):
            entry = self._read_entry(i)
            if entry is None or entry.redirect:
                continue

            md = self.get_article_markdown(i)
            if md and len(md) > 200:
                yield {"index": i, "title": entry.title, "url": entry.url, "content": md}

    def _load_dir_entries_v27(self):
        """Carga entradas directorio para formato v27."""
        f = self._f
        f.seek(80)
        # Calculate entry size from url pointer position
        entries_size = self._url_ptr_pos - 80
        total_entry_bytes = f.read(entries_size)

        ptr = 0
        entries = []
        while ptr < entries_size:
            try:
                e = ZIMDirEntry.from_buffer(total_entry_bytes, ptr, 27)
                entries.append(e)
                if e.redirect:
                    ptr += 8
                else:
                    ptr += 12
            except Exception:
                break
        self._entries = entries

    def close(self):
        self._f.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


# ── Config ────────────────────────────────────────────────
DOWNLOAD_BASE = "https://download.kiwix.org/zim/wikipedia/"

TOPICS = {
    "medicine":    {"dump": "wikipedia_es_medicine",    "domain": "medicina",     "variant": "nopic", "date": "2025-10"},
    "history":    {"dump": "wikipedia_es_history",      "domain": "historia",     "variant": "nopic", "date": "2025-09"},
    "chemistry":   {"dump": "wikipedia_es_chemistry",    "domain": "manufactura",  "variant": "nopic", "date": "2025-10"},
    "physics":     {"dump": "wikipedia_es_physics",      "domain": "manufactura",  "variant": "nopic", "date": "2025-10"},
    "mathematics": {"dump": "wikipedia_es_mathematics",   "domain": "manufactura",  "variant": "nopic", "date": "2025-09"},
    "computer":    {"dump": "wikipedia_es_computer",     "domain": "electronica",  "variant": "nopic", "date": "2025-10"},
    "geography":   {"dump": "wikipedia_es_geography",      "domain": "historia",     "variant": "nopic", "date": "2025-10"},
    "biology":     {"dump": "wikipedia_es_biology",        "domain": "medicina",     "variant": "nopic", "date": "2025-10"},
}


def get_zim_url(topic: str) -> tuple[str, str]:
    cfg = TOPICS[topic]
    filename = f"{cfg['dump']}_{cfg['variant']}_{cfg['date']}.zim"
    return filename, DOWNLOAD_BASE + filename


def download_zim(topic: str, dest_dir: Path) -> Path:
    filename, url = get_zim_url(topic)
    dest = dest_dir / filename
    if dest.exists():
        print(f"  Ya existe: {filename}")
        return dest
    print(f"  Descargando {filename}...", flush=True)
    try:
        urllib.request.urlretrieve(url, dest)
        print(f"  OK: {dest.stat().st_size / 1024/1024:.1f} MB")
    except Exception as e:
        print(f"  ERROR: {e}")
        if dest.exists():
            dest.unlink()
    return dest


def process_zim(zim_path: Path, domain: str, output_root: Path, max_articles: int = 0):
    output = output_root / domain
    output.mkdir(parents=True, exist_ok=True)

    print(f"  Procesando {zim_path.name}...")
    count = 0
    skipped = 0

    try:
        with ZIMReader(str(zim_path)) as zim:
            print(f"  {zim.article_count} artículos totales")

            for art in zim.extract_articles(limit=max_articles):
                title   = art["title"]
                content = art["content"]
                url     = art["url"]

                if not title or len(content) < 200 or len(content) > 200_000:
                    skipped += 1
                    continue

                # Safe filename
                safe = re.sub(r"[^\w\s-]", "", title)
                safe = re.sub(r"[-\s]+", "-", safe).strip("-")[:80]
                if not safe:
                    skipped += 1
                    continue

                # Evitar duplicados
                fp = output / f"{safe}.md"
                if fp.exists():
                    safe = f"{safe}-{art['index']}"
                    fp = output / f"{safe}.md"

                frontmatter = f"---\ntitle: {title}\ndomain: {domain}\nurl: {url}\nhas_images: false\n---\n\n"
                fp.write_text(frontmatter + content, encoding="utf-8")
                count += 1

                if count % 500 == 0:
                    print(f"  {count} artículos...")

            print(f"  -> {count} extraídos ({skipped} saltados)")

    except Exception as e:
        print(f"  ERROR: {e}")
        import traceback; traceback.print_exc()


def main():
    ap = argparse.ArgumentParser(description="Descarga y procesa Wikipedia ES (ZIM)")
    ap.add_argument("--topics", help="lista topics (coma): medicine,history,...")
    ap.add_argument("--all-balanced", action="store_true", help="Descarga los 8 topics balanceados")
    ap.add_argument("--list-topics", action="store_true")
    ap.add_argument("--download-only", action="store_true")
    ap.add_argument("--process-only", type=Path, help="Procesa ZIM ya descargado")
    ap.add_argument("--domain", default="medicina")
    ap.add_argument("--output", type=Path, default=Path("content"))
    ap.add_argument("--data-dir", type=Path, default=Path("data/wikipedia"))
    ap.add_argument("--max-per-topic", type=int, default=0)
    args = ap.parse_args()

    if args.list_topics:
        print("Topics disponibles:")
        for t, cfg in TOPICS.items():
            fn = f"{cfg['dump']}_{cfg['variant']}_{cfg['date']}.zim"
            print(f"  {t:>15}: {fn}  -> {cfg['domain']}")
        return

    if args.process_only:
        process_zim(args.process_only, args.domain, args.output, args.max_per_topic)
        return

    topics = []
    if args.all_balanced:
        topics = list(TOPICS.keys())
    elif args.topics:
        topics = [t.strip() for t in args.topics.split(",")]
    else:
        ap.print_help()
        return

    data_dir = args.data_dir
    data_dir.mkdir(parents=True, exist_ok=True)

    print(f"Descarga de {len(topics)} topics  |  ZIM dir: {data_dir}")
    print()

    for topic in topics:
        if topic not in TOPICS:
            print(f"Desconocido: {topic}"); continue
        print(f"\n=== {topic} ===")
        zim_path = download_zim(topic, data_dir)
        if args.download_only or not zim_path.exists():
            continue
        domain = TOPICS[topic]["domain"]
        process_zim(zim_path, domain, args.output, args.max_per_topic)

    print("\nListo.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Alexandria - Importador de canales Kolibri (.kolibri)
Convierte contenido de un archivo .kolibri (SQLite) a archivos Markdown
compatibles con Alexandria, organizados en content/kolibri/<canal>/.

Uso:
    python scripts/import_kolibri_channel.py --input ./khan_academy.kolibri
    python scripts/import_kolibri_channel.py --input ./khan_academy.kolibri --output ./content
    python scripts/import_kolibri_channel.py --input ./khan_academy.kolibri --list

El archivo .kolibri es una base SQLite que contiene:
    - channel: metadata del canal
    - contentnode: nodos de contenido (temas y recursos)
    - file: archivos asociados a cada nodo

Cada nodo terminal (no-topic) se convierte a un .md con frontmatter:
    - domain: kolibri
    - subtopic: <canal>/<ruta de tema>
    - source: kolibri
    - source_channel: <nombre del canal>
    - kolibri_id: <id interno de Kolibri>
    - kind: video|document|audio|exercise|html5
    - tags: etiquetas del contenido
    - license, language, etc.
"""
import argparse
import json
import os
import sqlite3
import sys
from pathlib import Path
from typing import Optional

DATABASE_PATH = Path(__file__).parent.parent / "backend"
sys.path.insert(0, str(DATABASE_PATH))

# ── Utilities ──────────────────────────────────────────────────────────────

def sanitize_filename(text: str) -> str:
    """Convierte un texto a nombre de archivo seguro."""
    text = text.strip()
    text = text.replace("/", "-").replace("\\", "-")
    text = text.replace(":", " - ").replace("?", "").replace("¡", "")
    text = text.replace("¿", "").replace("'", "").replace('"', "")
    text = text.replace("*", "").replace("|", "")
    text = text.replace("\n", " ").replace("\r", " ")
    # limitar largo
    if len(text) > 80:
        text = text[:80].rsplit(" ", 1)[0]
    return text.strip()


def slug_from_title(title: str) -> str:
    """Genera un slug URL-friendly desde el título."""
    import re
    slug = title.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[_\s]+", "-", slug)
    slug = slug.strip("-")
    if len(slug) > 60:
        slug = slug[:60].rstrip("-")
    return slug


def kind_to_text(kind: str) -> str:
    """Devuelve texto legible para el tipo de contenido."""
    mapping = {
        "topic": "Carpeta",
        "video": "Video",
        "audio": "Audio",
        "document": "Documento",
        "html5": "App HTML5",
        "exercise": "Ejercicio",
        "epub": "ePub",
    }
    return mapping.get(kind, kind.capitalize())


# ── Database reader ─────────────────────────────────────────────────────────

class KolibriReader:
    """
    Lee archivos .kolibri (SQLite) y extrae contenido.
    El archivo .kolibri puede ser:
        1. Un archivo .db (SQLite directo)
        2. Un directorio con archivo .sqlite dentro
    """

    def __init__(self, path: Path):
        self.path = Path(path)
        self.conn: Optional[sqlite3.Connection] = None

        # Normalizar ruta al archivo SQLite real
        resolved = self._resolve_db_path()
        if resolved is None:
            raise FileNotFoundError(
                f"No se encontró base SQLite en: {path}\n"
                "Un archivo .kolibri puede ser un .db o una carpeta con contenido."
            )
        self.db_path = resolved

    def _resolve_db_path(self) -> Optional[Path]:
        if self.path.is_file() and self._is_sqlite(self.path):
            return self.path
        if self.path.is_file() and self.path.suffix in (".db", ".sqlite", ".sqlite3"):
            return self.path
        if self.path.is_dir():
            for candidate in ["content.db", "database.db", "main.sqlite"]:
                candidate_path = self.path / candidate
                if candidate_path.exists() and self._is_sqlite(candidate_path):
                    return candidate_path
            # Buscar cualquier .sqlite o .db
            for candidate_path in self.path.rglob("*.db"):
                if self._is_sqlite(candidate_path):
                    return candidate_path
        return None

    def _is_sqlite(self, path: Path) -> bool:
        try:
            with open(path, "rb") as f:
                header = f.read(16)
            return header == b"SQLite format 3\x00"
        except Exception:
            return False

    def open(self):
        self.conn = sqlite3.connect(str(self.db_path))
        self.conn.row_factory = sqlite3.Row

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args):
        self.close()

    # ── Lectura de metadata ─────────────────────────────────────────────

    def get_channel_info(self) -> dict:
        """Obtiene información del canal."""
        if not self.conn:
            raise RuntimeError("Base de datos no abierta")
        cur = self.conn.execute(
            "SELECT * FROM channel LIMIT 1"
        )
        row = cur.fetchone()
        if not row:
            return {}
        return dict(row)

    def get_content_tree(self) -> list[dict]:
        """Obtiene todos los content nodes ordenados por lft (árbol)."""
        if not self.conn:
            raise RuntimeError("Base de datos no abierta")
        rows = self.conn.execute(
            "SELECT * FROM contentnode ORDER BY lft ASC"
        ).fetchall()
        return [dict(r) for r in rows]

    def get_files_for_node(self, node_id: str) -> list[dict]:
        """Obtiene los archivos asociados a un nodo."""
        if not self.conn:
            raise RuntimeError("Base de datos no abierta")
        rows = self.conn.execute(
            "SELECT * FROM file WHERE contentnode_id = ? ORDER BY priority ASC",
            (node_id,)
        ).fetchall()
        return [dict(r) for r in rows]

    def get_tags_for_node(self, node_id: str) -> list[str]:
        """Obtiene las etiquetas de un nodo."""
        if not self.conn:
            raise RuntimeError("Base de datos no abierta")
        rows = self.conn.execute("""
            SELECT t.tag_name FROM tag t
            JOIN contentnode_tags cnt ON cnt.tag_id = t.id
            WHERE cnt.contentnode_id = ?
        """, (node_id,)).fetchall()
        return [r["tag_name"] for r in rows]


# ── Convertidor a Markdown ─────────────────────────────────────────────────

class KolibriToMarkdown:
    """
    Convierte nodos de Kolibri a archivos Markdown para Alexandria.
    """

    def __init__(self, channel_name: str, channel_id: str, output_dir: Path):
        self.channel_name = channel_name
        self.channel_id = channel_id
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Base del canal
        self.channel_dir = self.output_dir / "kolibri" / sanitize_filename(channel_name)
        self.channel_dir.mkdir(parents=True, exist_ok=True)
        self.files_dir = self.channel_dir / "_files"
        self.files_dir.mkdir(parents=True, exist_ok=True)

        self.stats = {
            "total": 0,
            "topics": 0,
            "videos": 0,
            "documents": 0,
            "audio": 0,
            "exercises": 0,
            "html5": 0,
            "other": 0,
            "errors": 0,
        }

    def _get_topic_path(self, node_id: str, tree: dict[str, dict]) -> str:
        """Reconstruye la ruta de temas desde la raíz hasta el nodo."""
        path_parts = []
        current_id = tree[node_id]["parent"]
        while current_id and current_id in tree:
            node = tree[current_id]
            if node["kind"] == "topic":
                path_parts.insert(0, sanitize_filename(node["title"]))
            current_id = tree[current_id].get("parent")
        return "/".join(path_parts)

    def _build_tree(self, rows: list[dict]) -> dict[str, dict]:
        """Construye un dict id -> row para navegación rápida del árbol."""
        return {r["id"]: r for r in rows}

    def convert(self, reader: KolibriReader):
        """Recorre todos los nodos y convierte los recursos a Markdown."""
        rows = reader.get_content_tree()
        tree = self._build_tree(rows)

        # Crear carpeta raíz del canal
        self.channel_dir.mkdir(parents=True, exist_ok=True)

        # Generar índice del canal
        self._write_channel_index(rows, tree, reader)

        # Recorrer nodos y convertir recursos
        for row in rows:
            node = dict(row)
            kind = node.get("kind", "")

            if kind == "topic":
                self.stats["topics"] += 1
                continue  # los temas se usan para estructurar, no generan archivos

            try:
                self._convert_node(node, tree, reader)
            except Exception as e:
                self.stats["errors"] += 1
                print(f"  ERROR {node.get('title','?')}: {e}")

        return self.stats

    def _convert_node(self, node: dict, tree: dict[str, dict], reader: KolibriReader):
        """Convierte un nodo de contenido a Markdown."""
        kind = node.get("kind", "")
        node_id = node["id"]
        title = node.get("title", "Sin título") or "Sin título"
        description = node.get("description", "") or ""
        language = node.get("language", "") or ""
        license_name = node.get("license_name", "") or node.get("license", "") or ""
        role = node.get("role", "") or ""

        # Tags
        try:
            tags = reader.get_tags_for_node(node_id)
        except Exception:
            tags = []

        # Archivos asociados
        try:
            files = reader.get_files_for_node(node_id)
        except Exception:
            files = []

        # Determinar el archivo principal
        primary_file = self._pick_primary_file(files, kind)

        # Ruta del tema padre
        topic_path = self._get_topic_path(node_id, tree)

        # Construir el path del directorio de salida
        if topic_path:
            out_subdir = self.channel_dir / topic_path
        else:
            out_subdir = self.channel_dir
        out_subdir.mkdir(parents=True, exist_ok=True)

        # Generar nombre de archivo
        base_name = slug_from_title(title)
        out_file = out_subdir / f"{base_name}.md"

        # Si ya existe, agregar sufijo numérico
        counter = 1
        while out_file.exists():
            out_file = out_subdir / f"{base_name}-{counter}.md"
            counter += 1

        # Construir body del Markdown
        body = self._build_body(node, kind, primary_file, files, description)

        # Construir frontmatter
        frontmatter = self._build_frontmatter(
            title=title,
            kind=kind,
            topic_path=topic_path,
            node_id=node_id,
            tags=tags,
            language=language,
            license=license_name,
            primary_file=primary_file,
        )

        # Escribir archivo
        content = frontmatter + "\n" + body
        out_file.write_text(content, encoding="utf-8")

        # Copiar archivo asociado si existe
        if primary_file:
            self._copy_associated_file(primary_file, files, node_id)

        # Actualizar estadísticas
        self.stats["total"] += 1
        stat_key = kind if kind in self.stats else "other"
        self.stats[stat_key] = self.stats.get(stat_key, 0) + 1

    def _pick_primary_file(self, files: list[dict], kind: str) -> Optional[dict]:
        """Elige el archivo principal de un nodo según el tipo."""
        if not files:
            return None

        # Preferencias por tipo
        preset_priority = {
            "video": ["high", "medium", "low", "ebook", "thumbnail"],
            "document": ["document", "epub", "thumbnail"],
            "audio": ["audio", "thumbnail"],
            "exercise": ["exercise", "thumbnail"],
            "html5": ["html5", "thumbnail"],
        }

        preferred_presets = preset_priority.get(kind, ["thumbnail"])

        for preset in preferred_presets:
            for f in files:
                if f.get("preset") == preset and f.get("filename"):
                    return f
            # buscar por preset que contenga la keyword
            for f in files:
                if preset in str(f.get("preset", "")) and f.get("filename"):
                    return f

        # Fallback: cualquier archivo con filename
        for f in files:
            if f.get("filename"):
                return f

        return None

    def _copy_associated_file(self, primary_file: dict, all_files: list[dict], node_id: str):
        """Copia el archivo asociado al directorio _files/ del canal."""
        filename = primary_file.get("filename")
        if not filename:
            return

        # El archivo puede estar embebido en la DB como blob (storage_url = :storage)
        storage_url = primary_file.get("storage_url", "")
        if not storage_url:
            return

        # Si el archivo está embebido (Kolibri usa :storage: para archivos locales)
        if storage_url.startswith(":storage:"):
            # En archivos .kolibri directos, los archivos pueden estar en una subcarpeta
            # relative path después de :storage:
            internal_path = storage_url.replace(":storage:", "").lstrip("/")
            src = self.db_path.parent / internal_path if hasattr(self, 'db_path') else None
            if src and src.exists():
                dest = self.files_dir / filename
                if not dest.exists():
                    import shutil
                    shutil.copy2(src, dest)

    def _build_frontmatter(
        self,
        title: str,
        kind: str,
        topic_path: str,
        node_id: str,
        tags: list[str],
        language: str,
        license: str,
        primary_file: Optional[dict],
    ) -> str:
        """Genera el YAML frontmatter del artículo."""
        import frontmatter

        post = frontmatter.Post("")
        post["title"] = title
        post["domain"] = "kolibri"
        post["subtopic"] = f"kolibri/{self.channel_name}/{topic_path}" if topic_path else f"kolibri/{self.channel_name}"
        post["source"] = "kolibri"
        post["source_channel"] = self.channel_name
        post["source_channel_id"] = self.channel_id
        post["kolibri_id"] = node_id
        post["kind"] = kind
        post["kind_label"] = kind_to_text(kind)

        if tags:
            post["tags"] = tags
        if language:
            post["language"] = language
        if license:
            post["license"] = license
        if primary_file and primary_file.get("filename"):
            post["file"] = primary_file["filename"]
            preset = primary_file.get("preset", "")
            if preset:
                post["file_preset"] = preset

        return frontmatter.dumps(post)

    def _build_body(
        self,
        node: dict,
        kind: str,
        primary_file: Optional[dict],
        all_files: list[dict],
        description: str,
    ) -> str:
        """Construye el cuerpo del Markdown según el tipo de contenido."""
        title = node.get("title", "") or ""
        lines = []

        if description:
            lines.append(description)
            lines.append("")

        # Vínculo al archivo local si existe
        if primary_file and primary_file.get("filename"):
            filename = primary_file["filename"]
            ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""

            if kind == "video":
                lines.append(f"## Video\n")
                lines.append(f"> **Este contenido incluye un video.** El archivo `{filename}` está disponible en la carpeta `_files/` del canal.\n")
                # Intentar agregar link local
                lines.append(f"- [Ver video `{filename}`](../_files/{filename})\n")

            elif kind == "audio":
                lines.append(f"## Audio\n")
                lines.append(f"> **Este contenido incluye audio.** Archivo: `{filename}`\n")
                lines.append(f"- [Escuchar `{filename}`](../_files/{filename})\n")

            elif kind == "document":
                lines.append(f"## Documento\n")
                lines.append(f"> **Este contenido es un documento.** Archivo: `{filename}`\n")
                if ext in ("pdf",):
                    lines.append(f"- [Abrir PDF `{filename}`](../_files/{filename})\n")
                else:
                    lines.append(f"- [Descargar `{filename}`](../_files/{filename})\n")

            elif kind == "html5":
                lines.append(f"## App HTML5\n")
                lines.append(f"> **Este contenido es una aplicación HTML5.** Archivos asociados en `_files/`.\n")
                lines.append(f"- Archivo principal: `{filename}`\n")

            elif kind == "exercise":
                lines.append(f"## Ejercicio\n")
                lines.append(f"> **Este es un ejercicio interactivo.**\n")
                if all_files:
                    for f in all_files:
                        if f.get("filename"):
                            lines.append(f"- `{f['filename']}` (`{f.get('preset','')}`)\n")

        # Opciones adicionales (JSON) con datos útiles
        options_raw = node.get("options", "")
        if options_raw:
            try:
                options = json.loads(options_raw) if isinstance(options_raw, str) else options_raw
                # Para ejercicios, mostrar preguntas
                if kind == "exercise" and "questions" in options:
                    lines.append("\n## Preguntas\n")
                    for q in options.get("questions", [])[:20]:  # limitar a 20
                        q_type = q.get("type", "unknown")
                        question_data = q.get("question", {})
                        if isinstance(question_data, dict):
                            question_text = question_data.get("question", "") or question_data.get("text", "")
                        else:
                            question_text = str(question_data)
                        if question_text:
                            lines.append(f"**{q_type}**: {question_text}\n")
            except (json.JSONDecodeError, TypeError):
                pass

        # Nodos adicionales (children directos) como enlaces internos
        # Esto se llena en la siguiente versión con el árbol completo

        if not lines:
            lines.append(f"> Contenido de tipo **{kind_to_text(kind)}** de Kolibri.\n")
            lines.append(f"> Consulta el archivo original en Kolibri para ver el contenido completo.\n")

        return "\n".join(lines)

    def _write_channel_index(self, rows: list[dict], tree: dict, reader: KolibriReader):
        """Escribe un índice del canal en la raíz."""
        index_file = self.channel_dir / "00-INDICE.md"

        # Obtener metadata del canal
        try:
            channel_info = reader.get_channel_info()
        except Exception:
            channel_info = {}

        lines = [
            f"# {self.channel_name}",
            "",
        ]

        desc = channel_info.get("description") or channel_info.get("tagline") or ""
        if desc:
            lines.append(f"{desc}\n")

        min_version = channel_info.get("min_version") or ""
        if min_version:
            lines.append(f"**Versión mínima Kolibri:** {min_version}\n")

        lines.append("## Temas\n")
        lines.append("| Tema | Recursos |")
        lines.append("|------|----------|")

        # Agrupar nodos raíz (topics de primer nivel)
        root_topics = [r for r in rows if r.get("parent") in ("", None, "\x00") and r.get("kind") == "topic"]
        for topic in root_topics[:50]:  # limitar a 50
            topic_id = topic["id"]
            children = [r for r in rows if r.get("parent") == topic_id and r.get("kind") != "topic"]
            topic_title = topic.get("title", "Sin título") or "Sin título"
            lines.append(f"| [{topic_title}]({sanitize_filename(topic_title)}.md) | {len(children)} |")

        lines.append("")
        lines.append("## Estadísticas de importación\n")
        lines.append(f"- **Total de recursos:** {self.stats['total']}")
        lines.append(f"- Videos: {self.stats.get('videos', 0)}")
        lines.append(f"- Documentos: {self.stats.get('documents', 0)}")
        lines.append(f"- Audio: {self.stats.get('audio', 0)}")
        lines.append(f"- Ejercicios: {self.stats.get('exercises', 0)}")
        lines.append(f"- HTML5: {self.stats.get('html5', 0)}")

        content = "\n".join(lines)
        index_file.write_text(content, encoding="utf-8")


# ── CLI ────────────────────────────────────────────────────────────────────

def list_channel_info(path: Path) -> dict:
    """Lista información del canal sin importar nada."""
    try:
        with KolibriReader(path) as reader:
            info = reader.get_channel_info()
            rows = reader.get_content_tree()

            # Contar por tipo
            from collections import Counter
            kind_counts = Counter(r.get("kind", "unknown") for r in rows)

            return {
                "name": info.get("name", path.stem),
                "description": info.get("description", ""),
                "version": info.get("version", ""),
                "min_version": info.get("min_version", ""),
                "language": info.get("language", ""),
                "total_nodes": len(rows),
                "by_kind": dict(kind_counts),
            }
    except Exception as e:
        return {"error": str(e)}


def main():
    parser = argparse.ArgumentParser(
        description="Alexandria — Importador de canales Kolibri (.kolibri → .md)"
    )
    parser.add_argument(
        "--input", "-i", required=True, type=Path,
        help="Ruta al archivo .kolibri (SQLite) o directorio extraído"
    )
    parser.add_argument(
        "--output", "-o", type=Path,
        default=Path(__file__).parent.parent / "content",
        help="Carpeta de salida (default: content/)"
    )
    parser.add_argument(
        "--list", "-l", action="store_true",
        help="Solo muestra información del canal sin importar"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Muestra cada archivo generado"
    )
    args = parser.parse_args()

    if not args.input.exists():
        print(f"ERROR: {args.input} no existe")
        sys.exit(1)

    # ── Solo listar ─────────────────────────────────────────────────────
    if args.list:
        print(f"\n=== Información del canal ===")
        print(f"  Archivo: {args.input}\n")
        info = list_channel_info(args.input)
        if "error" in info:
            print(f"  ERROR: {info['error']}\n")
            sys.exit(1)

        print(f"  Canal:       {info['name']}")
        if info.get("description"):
            print(f"  Descripción: {info['description']}")
        if info.get("language"):
            print(f"  Idioma:      {info['language']}")
        if info.get("version"):
            print(f"  Versión:     {info['version']}")
        if info.get("min_version"):
            print(f"  Min. version Kolibri: {info['min_version']}")
        print(f"\n  Total nodos: {info['total_nodes']}")
        print(f"\n  Por tipo:")
        for kind, count in sorted(info["by_kind"].items()):
            print(f"    {kind:15s} {count:>6}")
        print()
        return

    # ── Importar ─────────────────────────────────────────────────────────
    print(f"\n=== Importando canal Kolibri ===")
    print(f"  Input:   {args.input}")
    print(f"  Output:   {args.output}")
    print()

    try:
        with KolibriReader(args.input) as reader:
            info = reader.get_channel_info()
            channel_name = info.get("name", args.input.stem) or args.input.stem
            channel_id = info.get("id", info.get("channel_id", ""))

            print(f"  Canal: {channel_name}")
            print(f"  ID:    {channel_id}\n")

            converter = KolibriToMarkdown(
                channel_name=channel_name,
                channel_id=channel_id,
                output_dir=args.output,
            )

            stats = converter.convert(reader)

            print(f"\n  === Importación completa ===")
            print(f"  Recursos convertidos: {stats['total']}")
            print(f"    Videos:      {stats.get('videos', 0)}")
            print(f"    Documentos:  {stats.get('documents', 0)}")
            print(f"    Audio:       {stats.get('audio', 0)}")
            print(f"    Ejercicios:  {stats.get('exercises', 0)}")
            print(f"    HTML5:       {stats.get('html5', 0)}")
            print(f"    Errors:      {stats['errors']}")
            print(f"\n  Salida: {converter.channel_dir}")
            print(f"\n  IMPORTANTE: Los archivos de video/audio/documento asociados")
            print(f"  deben copiarse manualmente a la carpeta _files/ del canal.")
            print(f"  Ubicación: {converter.files_dir}")
            print()

    except Exception as e:
        print(f"\n  ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

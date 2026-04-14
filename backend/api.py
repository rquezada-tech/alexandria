"""
Alexandria - API FastAPI
Endpoints para búsqueda, chat, administración y audio (STT + TTS)
"""
import os
import re
import sys
import uuid
from pathlib import Path
from typing import Optional

import httpx
from fastapi import FastAPI, HTTPException, Query, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

sys_path = Path(__file__).parent.parent
sys.path.insert(0, str(sys_path / "backend"))
from db import (
    init_db,
    search,
    get_content_by_id,
    get_all_content_for_source,
    save_chat,
    get_chat_history,
    get_domains,
    get_stats,
    SearchResult,
)
from audio import (
    transcribe_audio,
    generate_speech,
    is_whisper_available,
    is_mlx_audio_available,
    list_tts_voices,
)

# ── Config ──────────────────────────────────────────────
DATA_DIR = sys_path / "data"
CONTENT_DIR = sys_path / "content"
PORT = int(os.getenv("ALEXANDRIA_PORT", "8080"))
OLLAMA_BASE = os.getenv("OLLAMA_BASE", "http://localhost:11434")

# ── App ─────────────────────────────────────────────────
app = FastAPI(title="Alexandria API", version="0.3.4")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Modelos ──────────────────────────────────────────────
class ChatRequest(BaseModel):
    question: str
    session_id: Optional[str] = None
    domain: Optional[str] = None
    model: Optional[str] = None
    max_context: int = 5


# ── Helpers ──────────────────────────────────────────────
def build_system_prompt(domain: Optional[str] = None) -> str:
    domain_hint = ""
    if domain:
        domain_hint = f"\nRestringe tu búsqueda al dominio: {domain}."

    return f"""Eres el Bibliotecario de Alexandria, la biblioteca de conocimiento offline de la humanidad.
Tu propósito es ayudar a los usuarios a encontrar respuestas verificables en la base de conocimiento local.

REGLAS:
1. Responde SOLO con información recuperada del contexto.
2. Si la información es insuficiente, dilo con honestidad.
3. Cita las fuentes: menciona el título del artículo de donde viene.
4. Usa un tono claro, directo y accesible.
5. Para temas médicos: aclarar que es orientación general y buscar atención profesional.{domain_hint}

FORMATO de respuesta:
- Respuesta clara
- Fuentes: [Título del artículo]"""


def retrieve_context(question: str, domain: Optional[str], limit: int) -> tuple[str, list[SearchResult]]:
    """Recupera los chunks más relevantes para la pregunta."""
    results = search(query=question, domain=domain, limit=limit)

    if not results:
        return "", []

    context_parts = []
    for r in results:
        context_parts.append(f"[{r.title}] ({r.domain}/{r.subtopic or 'general'})\n{r.chunk}")

    return "\n\n---\n\n".join(context_parts), results


def call_ollama(model: str, messages: list[dict]) -> str:
    """Llama a Ollama con Messages API."""
    with httpx.Client(timeout=120) as client:
        response = client.post(
            f"{OLLAMA_BASE}/api/chat",
            json={"model": model, "messages": messages, "stream": False},
        )

    if response.status_code != 200:
        raise HTTPException(status_code=502, detail=f"Ollama error: {response.text}")

    data = response.json()
    return data["message"]["content"]


def select_model() -> str:
    """Selecciona el modelo más apropiado según RAM disponible."""
    try:
        import psutil
        mem = psutil.virtual_memory()
        total_gb = mem.total / (1024**3)
        if total_gb >= 14:
            return "qwen3:14b"
        elif total_gb >= 8:
            return "qwen3:8b"
        elif total_gb >= 4:
            return "phi4-mini"
        else:
            return "qwen2.5:3b"
    except ImportError:
        return "qwen2.5:3b"


# ── Imágenes de un artículo ───────────────────────────────
def extract_images_from_markdown(source: str) -> list[dict]:
    """
    Dado un source path relativo (ej: medicina/primeros-auxilios/heridas.md),
    busca en la misma carpeta imágenes compatibles (jpg, png, gif, webp, svg)
    que podrían estar referenciadas en el markdown.
    """
    # El source viene como "domain/subtopic/article.md"
    # Buscamos imágenes junto al .md o en subcarpetas images/
    source_path = CONTENT_DIR / source
    if not source_path.exists():
        source_path = CONTENT_DIR / source.replace("/", os.sep)
    if not source_path.exists():
        return []

    article_dir = source_path.parent
    images = []

    # Buscar imágenes en la carpeta del artículo
    for pattern in ["*.jpg", "*.jpeg", "*.png", "*.gif", "*.webp", "*.svg"]:
        for img_path in article_dir.glob(pattern):
            # Relativo a CONTENT_DIR para URL
            rel_path = img_path.relative_to(CONTENT_DIR)
            images.append({
                "filename": img_path.name,
                "url": f"/content-images/{rel_path.as_posix()}",
                "alt": img_path.stem.replace("_", " ").replace("-", " "),
            })

    # Buscar en subcarpeta images/
    images_dir = article_dir / "images"
    if images_dir.exists():
        for pattern in ["*.jpg", "*.jpeg", "*.png", "*.gif", "*.webp", "*.svg"]:
            for img_path in images_dir.glob(pattern):
                rel_path = img_path.relative_to(CONTENT_DIR)
                images.append({
                    "filename": img_path.name,
                    "url": f"/content-images/{rel_path.as_posix()}",
                    "alt": img_path.stem.replace("_", " ").replace("-", " "),
                })

    return images


# ── Endpoints: Estado ───────────────────────────────────
@app.on_event("startup")
def startup():
    init_db()


@app.get("/health")
def health():
    return {
        "status": "ok",
        "version": "0.3.4",
        "audio": {
            "stt_available": is_whisper_available(),
            "tts_available": is_mlx_audio_available(),
            "whisper_model": os.getenv("WHISPER_MODEL", "medium"),
            "tts_voices": list_tts_voices(),
            "tts_voice": os.getenv("TTS_VOICE", "af_heart"),
        },
    }


@app.get("/domains")
def list_domains():
    return {"domains": get_domains()}


@app.get("/stats")
def stats():
    return get_stats()


# ── Endpoints: Búsqueda ─────────────────────────────────
@app.get("/search")
def search_endpoint(
    q: str = Query(..., min_length=2),
    domain: Optional[str] = None,
    limit: int = Query(default=10, ge=1, le=50),
):
    results = search(query=q, domain=domain, limit=limit)
    return {
        "query": q,
        "domain": domain,
        "total": len(results),
        "results": [
            {
                "id": r.id,
                "title": r.title,
                "domain": r.domain,
                "subtopic": r.subtopic,
                "chunk": r.chunk[:300] + "..." if len(r.chunk) > 300 else r.chunk,
                "rank": r.rank,
            }
            for r in results
        ],
    }


@app.get("/content/{content_id}")
def get_content(content_id: int):
    content = get_content_by_id(content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Contenido no encontrado")

    all_chunks = get_all_content_for_source(content.source)

    return {
        "id": content.id,
        "source": content.source,
        "title": content.title,
        "domain": content.domain,
        "subtopic": content.subtopic,
        "full_text": " ".join(c.chunk for c in all_chunks),
        "has_images": content.has_images,
        "chunks_count": content.total_chunks,
    }


@app.get("/content/{content_id}/images")
def get_content_images(content_id: int):
    """Retorna las imágenes asociadas a un artículo."""
    content = get_content_by_id(content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Contenido no encontrado")

    images = extract_images_from_markdown(content.source)
    return {"content_id": content_id, "images": images}


# ── Endpoints: Chat ─────────────────────────────────────
@app.post("/chat")
def chat(req: ChatRequest):
    session_id = req.session_id or str(uuid.uuid4())
    model = req.model or select_model()

    context, results = retrieve_context(req.question, req.domain, req.max_context)

    if not results:
        return {
            "session_id": session_id,
            "answer": "No encontré información relevante para tu pregunta en la base de conocimiento. ¿Podrías reformular o usar otros términos?",
            "sources": [],
            "model": model,
        }

    system_msg = {
        "role": "system",
        "content": build_system_prompt(req.domain) + f"\n\nCONTEXTO RECUPERADO:\n{context}",
    }
    user_msg = {"role": "user", "content": req.question}

    try:
        answer = call_ollama(model=model, messages=[system_msg, user_msg])
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Error al generar respuesta: {str(e)}")

    source_ids = [r.id for r in results]
    save_chat(
        session_id=session_id,
        question=req.question,
        answer=answer,
        sources=source_ids,
        model=model,
    )

    return {
        "session_id": session_id,
        "answer": answer,
        "sources": [
            {"id": r.id, "title": r.title, "domain": r.domain, "subtopic": r.subtopic}
            for r in results
        ],
        "model": model,
    }


@app.get("/chat/history/{session_id}")
def chat_history(session_id: str, limit: int = Query(default=20, ge=1, le=100)):
    history = get_chat_history(session_id=session_id, limit=limit)
    return {
        "session_id": session_id,
        "messages": [
            {
                "id": m.id,
                "question": m.question,
                "answer": m.answer,
                "sources": m.sources,
                "model": m.model,
            }
            for m in history
        ],
    }


# ── Endpoints: Audio (STT + TTS) ────────────────────────

@app.post("/audio/stt")
async def audio_stt(
    audio: UploadFile = File(...),
    language: str = Form(default="es"),
):
    """Recibe audio y retorna la transcripción de texto."""
    if not is_whisper_available():
        raise HTTPException(
            status_code=503,
            detail="Whisper no está instalado. Instálalo con: brew install whisper",
        )

    try:
        audio_bytes = await audio.read()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al leer audio: {e}")

    if len(audio_bytes) == 0:
        raise HTTPException(status_code=400, detail="Archivo de audio vacío.")

    if len(audio_bytes) > 50 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="Archivo de audio muy grande (máx 50MB).")

    filename = audio.filename or "audio.wav"

    try:
        text = transcribe_audio(audio_bytes, filename, language=language)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en transcripción: {e}")

    return {"text": text, "language": language, "filename": filename}


@app.get("/audio/tts")
def audio_tts(
    q: str = Query(..., min_length=1, max_length=2000),
    voice: str = Query(default=None),
):
    """Recibe texto y retorna audio WAV con voz sintetizada."""
    if not is_mlx_audio_available():
        raise HTTPException(
            status_code=503,
            detail="mlx-audio no está instalado. Instálalo desde:\n  https://github.com/lucasnewman/mlx-audio",
        )

    active_voice = voice or os.getenv("TTS_VOICE", "af_heart")

    try:
        wav_bytes = generate_speech(q, voice=active_voice)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en síntesis de voz: {e}")

    return Response(
        content=wav_bytes,
        media_type="audio/wav",
        headers={
            "Content-Disposition": 'attachment; filename="alexandria_voice.wav"',
            "X-Voice": active_voice,
        },
    )


@app.get("/audio/capabilities")
def audio_capabilities():
    """Lista las capacidades de audio del sistema."""
    return {
        "stt": {
            "available": is_whisper_available(),
            "cmd": os.getenv("WHISPER_CMD", "whisper"),
            "model": os.getenv("WHISPER_MODEL", "medium"),
        },
        "tts": {
            "available": is_mlx_audio_available(),
            "cmd": os.getenv("MLX_AUDIO_CMD", "mlx-audio"),
            "default_voice": os.getenv("TTS_VOICE", "af_heart"),
            "voices": list_tts_voices(),
        },
    }


# ── Ebooks offline ────────────────────────────────────
import re
import frontmatter as fm

EBOOKS_DIR = sys_path / "content" / "ebooks"


def _scan_ebooks():
    """Escanea content/ebooks/ y devuelve lista de libros con sus capítulos."""
    if not EBOOKS_DIR.exists():
        return []

    books = []
    for book_dir in sorted(EBOOKS_DIR.iterdir()):
        if not book_dir.is_dir():
            continue
        md_files = sorted(book_dir.glob("*.md"))
        if not md_files:
            continue

        # Extraer metadata del primer archivo
        first = md_files[0]
        try:
            post = fm.loads(first.read_text(encoding="utf-8"))
            title = post.get("title", book_dir.name)
            author = post.get("author", "")
        except Exception:
            title = book_dir.name
            author = ""

        # Todos los .md del folder son capítulos
        chapters = []
        for f in md_files:
            fname = f.stem
            # Tratar el primer archivo como book metadata o primer capítulo
            if f == first:
                ch_title = title
            else:
                # Limpiar nombre: "capitulo-01", "01-introduccion", etc.
                ch_title_raw = re.sub(r"^\d+[-_]", "", fname)
                ch_title = ch_title_raw.replace("-", " ").replace("_", " ").title()
                # Extraer title del frontmatter si existe
                try:
                    ch_post = fm.loads(f.read_text(encoding="utf-8"))
                    if ch_post.get("title"):
                        ch_title = ch_post["title"]
                except Exception:
                    pass

            chapters.append({
                "title": ch_title,
                "file": f.name,
                "idx": len(chapters),
            })

        books.append({
            "id": book_dir.name,
            "title": title,
            "author": author,
            "path": str(book_dir.relative_to(sys_path)),
            "chapters": chapters,
        })

    return books


@app.get("/ebooks")
def serve_ebooks():
    """Sirve el lector de ebooks."""
    ebooks_html = sys_path / "frontend" / "ebooks.html"
    if not ebooks_html.exists():
        raise HTTPException(status_code=404, detail="Ebooks viewer no encontrado")
    return FileResponse(str(ebooks_html))


@app.get("/ebooks/list")
def list_ebooks():
    """Lista libros y capítulos disponibles en content/ebooks/."""
    return {"ebooks": _scan_ebooks()}


@app.get("/ebooks/chapter")
def get_ebook_chapter(book: str, idx: int):
    """Devuelve el contenido Markdown de un capítulo específico."""
    books = _scan_ebooks()
    target = next((b for b in books if b["id"] == book), None)
    if not target:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    if idx < 0 or idx >= len(target["chapters"]):
        raise HTTPException(status_code=404, detail="Capítulo no encontrado")

    chapter = target["chapters"][idx]
    chapter_file = EBOOKS_DIR / book / chapter["file"]
    if not chapter_file.exists():
        raise HTTPException(status_code=404, detail="Archivo de capítulo no encontrado")

    content = chapter_file.read_text(encoding="utf-8")
    return Response(content=content, media_type="text/plain; charset=utf-8")


# ── Notas personales ────────────────────────────────────
from datetime import datetime

NOTES_DIR = sys_path / "content" / "notes"
NOTES_DIR.mkdir(parents=True, exist_ok=True)

# Dominio reservado para notas
DOMAIN_NOTES = "notes"


def _slugify(title: str) -> str:
    """Genera un slug URL-safe desde el título."""
    slug = title.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[_\s]+", "-", slug)
    slug = slug.strip("-")
    if len(slug) > 60:
        slug = slug[:60].rstrip("-")
    return slug or "nota"


def _note_path(slug: str) -> Path:
    """Ruta del archivo .md para un slug dado."""
    return NOTES_DIR / f"{slug}.md"


def _read_note_meta(fp: Path) -> dict:
    """Lee frontmatter y nombre de archivo como título fallback."""
    try:
        post = fm.loads(fp.read_text(encoding="utf-8"))
        title = post.get("title", fp.stem.replace("-", " ").replace("_", " ").title())
        tags = post.get("tags", [])
        created = post.get("created", "")
        updated = post.get("updated", "")
        note_id = post.get("note_id", fp.stem)
    except Exception:
        title = fp.stem.replace("-", " ").replace("_", " ").title()
        tags, created, updated, note_id = [], "", "", fp.stem
    return {
        "id": note_id,
        "title": title,
        "tags": tags if isinstance(tags, list) else [],
        "created": created,
        "updated": updated,
        "slug": fp.stem,
    }


@app.get("/notes")
def serve_notes():
    """Sirve el viewer de notas personales."""
    notes_html = sys_path / "frontend" / "notes.html"
    if not notes_html.exists():
        raise HTTPException(status_code=404, detail="Notes viewer no encontrado")
    return FileResponse(str(notes_html))


@app.get("/notes/list")
def list_notes(q: str = Query(default=""), tag: str = Query(default=""), limit: int = Query(default=50, ge=1, le=200)):
    """
    Lista notas personales con búsqueda y filtro por tag.
    Busca en título y tags. Retorna metadata, no contenido completo.
    """
    if not NOTES_DIR.exists():
        return {"notes": [], "total": 0}

    all_notes = []
    for fp in sorted(NOTES_DIR.glob("*.md"), key=lambda f: f.stat().st_mtime, reverse=True):
        meta = _read_note_meta(fp)

        # Filtro por tag
        if tag and tag not in meta["tags"]:
            continue

        # Búsqueda textual en título y tags
        if q:
            ql = q.lower()
            haystack = " ".join([meta["title"].lower()] + [t.lower() for t in meta["tags"]])
            # También buscar en contenido
            try:
                raw = fp.read_text(encoding="utf-8")
                # Quitar frontmatter para buscar en body
                raw = re.sub(r"^---[\s\S]*?---\n", "", raw)
                haystack += " " + raw[:2000].lower()
            except Exception:
                pass
            if ql not in haystack:
                continue

        # Extraer preview del body (primeras líneas sin headers)
        try:
            raw = fp.read_text(encoding="utf-8")
            raw = re.sub(r"^---[\s\S]*?---\n", "", raw)
            lines = [l for l in raw.split("\n") if l.strip() and not l.startswith("#")]
            preview = " ".join(lines)[:200].strip()
        except Exception:
            preview = ""

        all_notes.append({
            **meta,
            "preview": preview,
            "word_count": len(preview.split()),
        })

        if len(all_notes) >= limit:
            break

    return {"notes": all_notes, "total": len(all_notes)}


@app.post("/notes")
def create_note(req: dict = None):
    """
    Crea una nota nueva.
    Body: { "title": "...", "content": "...", "tags": [] }
    Retorna: { "id", "slug", "path" }
    """
    data = req or {}
    title = data.get("title", "Nueva nota").strip() or "Nueva nota"
    content = data.get("content", "")
    tags = data.get("tags", [])
    if not isinstance(tags, list):
        tags = []

    note_id = str(uuid.uuid4())[:8]
    slug = _slugify(title)
    fp = _note_path(slug)

    # Evitar colisiones de nombre
    counter = 1
    original_slug = slug
    while fp.exists():
        slug = f"{original_slug}-{counter}"
        fp = _note_path(slug)
        counter += 1

    now = datetime.now().strftime("%Y-%m-%d")

    # Construir frontmatter
    frontmatter_lines = ["---"]
    frontmatter_lines.append(f"title: {title}")
    frontmatter_lines.append(f"note_id: {note_id}")
    frontmatter_lines.append(f"domain: {DOMAIN_NOTES}")
    frontmatter_lines.append(f"tags: [{', '.join(tags)}]" if tags else "tags: []")
    frontmatter_lines.append(f"created: {now}")
    frontmatter_lines.append(f"updated: {now}")
    frontmatter_lines.append("---")
    frontmatter_lines.append("")

    full_content = "\n".join(frontmatter_lines) + content
    fp.write_text(full_content, encoding="utf-8")

    return {
        "id": note_id,
        "slug": slug,
        "path": str(fp.relative_to(sys_path)),
        "title": title,
        "created": now,
    }


@app.get("/notes/{slug}")
def get_note(slug: str):
    """Devuelve el contenido completo de una nota (Markdown raw)."""
    fp = _note_path(slug)
    if not fp.exists():
        raise HTTPException(status_code=404, detail="Nota no encontrada")

    raw = fp.read_text(encoding="utf-8")
    meta = _read_note_meta(fp)

    return {
        **meta,
        "content": raw,
        "path": str(fp.relative_to(sys_path)),
    }


@app.put("/notes/{slug}")
def update_note(slug: str, req: dict):
    """
    Actualiza una nota existente.
    Body: { "title"?: "...", "content"?: "...", "tags"?: [...] }
    """
    fp = _note_path(slug)
    if not fp.exists():
        raise HTTPException(status_code=404, detail="Nota no encontrada")

    # Leer estado actual
    try:
        post = fm.loads(fp.read_text(encoding="utf-8"))
    except Exception:
        post = fm.Post("")

    # Aplicar cambios
    title = req.get("title", post.get("title", slug.replace("-", " ").title()))
    content = req.get("content", str(post.content))
    tags = req.get("tags", post.get("tags", []))
    if not isinstance(tags, list):
        tags = []

    now = datetime.now().strftime("%Y-%m-%d")
    created = post.get("created", now)
    note_id = post.get("note_id", slug)

    # Si cambió el título, renombrar archivo
    new_slug = _slugify(title)
    new_fp = _note_path(new_slug)

    # Reconstruir archivo
    frontmatter_lines = ["---"]
    frontmatter_lines.append(f"title: {title}")
    frontmatter_lines.append(f"note_id: {note_id}")
    frontmatter_lines.append(f"domain: {DOMAIN_NOTES}")
    frontmatter_lines.append(f"tags: [{', '.join(tags)}]" if tags else "tags: []")
    frontmatter_lines.append(f"created: {created}")
    frontmatter_lines.append(f"updated: {now}")
    frontmatter_lines.append("---")
    frontmatter_lines.append("")

    full_content = "\n".join(frontmatter_lines) + content

    # Si cambió slug, renombrar archivo
    if new_slug != slug:
        counter = 1
        while new_fp.exists() and new_fp.stat().st_ino != fp.stat().st_ino:
            new_fp = _note_path(f"{new_slug}-{counter}")
            counter += 1
        fp.rename(new_fp)

    new_fp.write_text(full_content, encoding="utf-8")

    return {
        "id": note_id,
        "slug": new_fp.stem,
        "title": title,
        "tags": tags,
        "updated": now,
        "created": created,
    }


@app.delete("/notes/{slug}")
def delete_note(slug: str):
    """Elimina una nota."""
    fp = _note_path(slug)
    if not fp.exists():
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    fp.unlink()
    return {"deleted": slug}


@app.get("/notes/tags")
def list_all_tags():
    """Lista todas las tags usadas en notas, con conteo."""
    if not NOTES_DIR.exists():
        return {"tags": []}
    tag_counts: dict[str, int] = {}
    for fp in NOTES_DIR.glob("*.md"):
        try:
            post = fm.loads(fp.read_text(encoding="utf-8"))
            tags = post.get("tags", [])
            if not isinstance(tags, list):
                tags = []
            for t in tags:
                tag_counts[t] = tag_counts.get(t, 0) + 1
        except Exception:
            pass
    sorted_tags = sorted(tag_counts.items(), key=lambda x: -x[1])
    return {"tags": [{"name": t, "count": c} for t, c in sorted_tags]}


# ── Mapas offline ──────────────────────────────────────
MAPS_DIR = sys_path / "data" / "maps"

AVAILABLE_MAPS = [
    {"id": "world", "label": "Mundo", "file": "world.pmtiles", "note": "Mapa mundial (baja resolución)"},
    {"id": "sudamerica", "label": "Sudamérica", "file": "sudamerica.pmtiles", "note": "Cobertura completa"},
    {"id": "chile", "label": "Chile", "file": "chile.pmtiles", "note": "Chile continental + insular"},
    {"id": "latam", "label": "Latinoamérica", "file": "latam.pmtiles", "note": "México a Argentina"},
    {"id": "europa", "label": "Europa", "file": "europa.pmtiles", "note": "Continente europeo"},
]


@app.get("/maps")
def serve_maps():
    """Sirve el visualizador de mapas offline."""
    maps_html = sys_path / "frontend" / "maps.html"
    if not maps_html.exists():
        raise HTTPException(status_code=404, detail="Maps viewer no encontrado")
    return FileResponse(str(maps_html))


@app.get("/maps/available")
def list_maps():
    """Lista los mapas offline disponibles (descargados en data/maps/)."""
    available = []
    if MAPS_DIR.exists():
        for m in AVAILABLE_MAPS:
            pmtiles_file = MAPS_DIR / m["file"]
            if pmtiles_file.exists():
                size_mb = round(pmtiles_file.stat().st_size / (1024 * 1024), 2)
                available.append({**m, "size_mb": size_mb, "status": "available"})
            else:
                available.append({**m, "size_mb": None, "status": "not_downloaded"})
    return {"maps": available}


# Servir archivos PMTiles (mapas offline descargados)
if MAPS_DIR.exists():
    app.mount("/data/maps", StaticFiles(directory=str(MAPS_DIR)), name="maps-pmtiles")


# ── Static: Frontend + Contenido ────────────────────────
frontend_dir = sys_path / "frontend"
if frontend_dir.exists():
    @app.get("/")
    def serve_index():
        idx = frontend_dir / "index.html"
        if idx.exists():
            return FileResponse(str(idx))
        raise HTTPException(status_code=404, detail="Frontend no encontrado")

    app.mount("/static", StaticFiles(directory=str(frontend_dir)), name="static")

# Servir imágenes del contenido (artículos pueden tener imágenes)
if CONTENT_DIR.exists():
    app.mount("/content-images", StaticFiles(directory=str(CONTENT_DIR)), name="content-images")


# ── Entry point ──────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)

"""
Alexandria - API FastAPI
Endpoints para búsqueda, chat y administración
Soporta múltiples proveedores LLM: Ollama (offline) y MiniMax (cloud)
"""
import os
import sys
import uuid
import json
from pathlib import Path
from typing import Optional

import httpx
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
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

# ── Config ──────────────────────────────────────────────
DATA_DIR = sys_path / "data"
CONTENT_DIR = sys_path / "content"
PORT = int(os.getenv("ALEXANDRIA_PORT", "8080"))

# Ollama (proveedor offline por defecto)
OLLAMA_BASE = os.getenv("OLLAMA_BASE", "http://localhost:11434")

# MiniMax (proveedor cloud alternativo)
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama").lower()   # "ollama" | "minimax"
MINIMAX_API_KEY = os.getenv("MINIMAX_API_KEY", "")
MINIMAX_MODEL = os.getenv("MINIMAX_MODEL", "MiniMax-M2.7")
MINIMAX_BASE = os.getenv("MINIMAX_BASE", "https://api.minimaxi.chat/v1")

# ── App ─────────────────────────────────────────────────
app = FastAPI(title="Alexandria API", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Modelo de chat ──────────────────────────────────────
class ChatRequest(BaseModel):
    question: str
    session_id: Optional[str] = None
    domain: Optional[str] = None
    model: Optional[str] = None
    max_context: int = 5  # máximo de chunks de contexto


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


# ── LLM Providers ────────────────────────────────────────

def call_ollama(model: str, messages: list[dict]) -> str:
    """Llama a Ollama con Messages API (modo offline)."""
    with httpx.Client(timeout=120) as client:
        response = client.post(
            f"{OLLAMA_BASE}/api/chat",
            json={"model": model, "messages": messages, "stream": False},
        )

    if response.status_code != 200:
        raise HTTPException(status_code=502, detail=f"Ollama error: {response.text}")

    data = response.json()
    return data["message"]["content"]


def call_minimax(model: str, messages: list[dict]) -> str:
    """Llama a MiniMax via API compatible con OpenAI Chat Completions."""
    if not MINIMAX_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="MINIMAX_API_KEY no configurada. Exporta la variable de entorno antes de iniciar Alexandria.",
        )

    headers = {
        "Authorization": f"Bearer {MINIMAX_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "temperature": 0.7,
        "max_tokens": 1024,
    }

    with httpx.Client(timeout=120) as client:
        response = client.post(
            f"{MINIMAX_BASE}/chat/completions",
            headers=headers,
            json=payload,
        )

    if response.status_code != 200:
        raise HTTPException(status_code=502, detail=f"MiniMax error {response.status_code}: {response.text}")

    data = response.json()
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError) as e:
        raise HTTPException(status_code=502, detail=f"Respuesta inesperada de MiniMax: {data}")


def call_llm(model: str, messages: list[dict], provider: Optional[str] = None) -> str:
    """Enruta la llamada al proveedor de LLM configurado."""
    active_provider = provider or LLM_PROVIDER
    if active_provider == "minimax":
        return call_minimax(model=model, messages=messages)
    else:
        return call_ollama(model=model, messages=messages)


def select_model(provider: Optional[str] = None) -> str:
    """Selecciona el modelo por defecto según el proveedor activo."""
    active_provider = provider or LLM_PROVIDER

    if active_provider == "minimax":
        return MINIMAX_MODEL

    # Ollama: heurística por RAM disponible
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


# ── Endpoints ───────────────────────────────────────────
@app.on_event("startup")
def startup():
    init_db()


@app.get("/health")
def health():
    return {
        "status": "ok",
        "version": "0.2.0",
        "llm_provider": LLM_PROVIDER,
        "default_model": select_model(),
    }


@app.get("/domains")
def list_domains():
    return {"domains": get_domains()}


@app.get("/stats")
def stats():
    return get_stats()


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

    # Obtener todos los chunks del mismo artículo
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


@app.post("/chat")
def chat(req: ChatRequest):
    session_id = req.session_id or str(uuid.uuid4())
    model = req.model or select_model()

    # 1. Recuperar contexto
    context, results = retrieve_context(req.question, req.domain, req.max_context)

    if not results:
        return {
            "session_id": session_id,
            "answer": "No encontré información relevante para tu pregunta en la base de conocimiento. ¿Podrías reformular o usar otros términos?",
            "sources": [],
            "model": model,
            "provider": LLM_PROVIDER,
        }

    # 2. Construir prompt con contexto
    system_msg = {
        "role": "system",
        "content": build_system_prompt(req.domain) + f"\n\nCONTEXTO RECUPERADO:\n{context}",
    }

    user_msg = {"role": "user", "content": req.question}

    # 3. Llamar al LLM (Ollama u otro proveedor)
    try:
        answer = call_llm(model=model, messages=[system_msg, user_msg])
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Error al generar respuesta: {str(e)}")

    # 4. Guardar en historial
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
        "provider": LLM_PROVIDER,
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


# ── Frontend estático ───────────────────────────────────
frontend_dir = sys_path / "frontend" / "dist"
if frontend_dir.exists():
    app.mount("/static", StaticFiles(directory=str(frontend_dir)), name="static")


# ── Entry point ──────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)

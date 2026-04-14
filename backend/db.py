"""
Alexandria - Módulo de base de datos
SQLite + FTS5 para conocimiento offline
"""
import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Optional
import json
from pathlib import Path

DATABASE_PATH = Path(__file__).parent.parent / "data" / "alexandria.db"


@dataclass
class Content:
    id: int
    source: str
    title: str
    domain: str
    subtopic: Optional[str]
    chunk: str
    chunk_idx: int
    total_chunks: int
    has_images: bool


@dataclass
class SearchResult:
    id: int
    title: str
    domain: str
    subtopic: Optional[str]
    chunk: str
    rank: float


@dataclass
class ChatMessage:
    id: int
    session_id: str
    question: str
    answer: str
    sources: list[int]
    model: Optional[str]
    tokens_in: Optional[int]
    tokens_out: Optional[int]


def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@contextmanager
def get_cursor():
    conn = get_db()
    try:
        cursor = conn.cursor()
        yield cursor
        conn.commit()
    finally:
        conn.close()


def init_db():
    """Crea o actualiza el schema de la base de datos."""
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with get_cursor() as cursor:
        # Tabla principal de contenidos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contents (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                source       TEXT    NOT NULL,
                title        TEXT    NOT NULL,
                domain       TEXT    NOT NULL,
                subtopic     TEXT,
                chunk        TEXT    NOT NULL,
                chunk_idx    INTEGER DEFAULT 0,
                total_chunks INTEGER DEFAULT 1,
                has_images   INTEGER DEFAULT 0,
                created_at   TEXT    DEFAULT (datetime('now'))
            )
        """)

        # Índice por dominio para filtrado rápido
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_domain ON contents(domain)
        """)

        # Índice por source para deduplicación
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_source ON contents(source)
        """)

        # Tabla FTS5 para búsqueda full-text
        cursor.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS contents_fts USING fts5(
                title,
                domain,
                subtopic,
                chunk,
                content='contents',
                content_rowid='id',
                tokenize='porter unicode61'
            )
        """)

        # Tabla de historial de chat
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat_history (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id  TEXT    NOT NULL,
                question    TEXT    NOT NULL,
                answer      TEXT    NOT NULL,
                sources     TEXT,
                model       TEXT,
                tokens_in   INTEGER,
                tokens_out  INTEGER,
                created_at  TEXT    DEFAULT (datetime('now'))
            )
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_session
            ON chat_history(session_id)
        """)


def insert_content(
    source: str,
    title: str,
    domain: str,
    chunk: str,
    subtopic: Optional[str] = None,
    chunk_idx: int = 0,
    total_chunks: int = 1,
    has_images: bool = False,
) -> int:
    """Inserta un chunk de contenido y actualiza el índice FTS."""
    with get_cursor() as cursor:
        cursor.execute("""
            INSERT INTO contents
              (source, title, domain, subtopic, chunk, chunk_idx, total_chunks, has_images)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (source, title, domain, subtopic, chunk, chunk_idx, total_chunks, int(has_images)))

        row_id = cursor.lastrowid

        # Actualizar el índice FTS
        cursor.execute("""
            INSERT INTO contents_fts(rowid, title, domain, subtopic, chunk)
            VALUES (?, ?, ?, ?, ?)
        """, (row_id, title, domain, subtopic or "", chunk))

        return row_id


def search(
    query: str,
    domain: Optional[str] = None,
    limit: int = 10,
) -> list[SearchResult]:
    """Búsqueda full-text en el conocimiento."""
    with get_cursor() as cursor:
        if domain:
            fts_query = f"{query} AND domain:{domain}"
        else:
            fts_query = query

        cursor.execute(f"""
            SELECT c.id, c.title, c.domain, c.subtopic, c.chunk,
                   rank
              FROM contents_fts
              JOIN contents c ON c.id = contents_fts.rowid
             WHERE contents_fts MATCH ?
             ORDER BY rank
             LIMIT ?
        """, (fts_query, limit))

        return [
            SearchResult(
                id=row["id"],
                title=row["title"],
                domain=row["domain"],
                subtopic=row["subtopic"],
                chunk=row["chunk"],
                rank=row["rank"],
            )
            for row in cursor.fetchall()
        ]


def get_content_by_id(content_id: int) -> Optional[Content]:
    """Obtiene un contenido completo por ID."""
    with get_cursor() as cursor:
        cursor.execute("""
            SELECT id, source, title, domain, subtopic,
                   chunk, chunk_idx, total_chunks, has_images
              FROM contents
             WHERE id = ?
        """, (content_id,))

        row = cursor.fetchone()
        if not row:
            return None

        return Content(
            id=row["id"],
            source=row["source"],
            title=row["title"],
            domain=row["domain"],
            subtopic=row["subtopic"],
            chunk=row["chunk"],
            chunk_idx=row["chunk_idx"],
            total_chunks=row["total_chunks"],
            has_images=bool(row["has_images"]),
        )


def get_all_content_for_source(source: str) -> list[Content]:
    """Obtiene todos los chunks de un artículo (para contexto completo)."""
    with get_cursor() as cursor:
        cursor.execute("""
            SELECT id, source, title, domain, subtopic,
                   chunk, chunk_idx, total_chunks, has_images
              FROM contents
             WHERE source = ?
             ORDER BY chunk_idx
        """, (source,))

        return [
            Content(
                id=row["id"],
                source=row["source"],
                title=row["title"],
                domain=row["domain"],
                subtopic=row["subtopic"],
                chunk=row["chunk"],
                chunk_idx=row["chunk_idx"],
                total_chunks=row["total_chunks"],
                has_images=bool(row["has_images"]),
            )
            for row in cursor.fetchall()
        ]


def save_chat(
    session_id: str,
    question: str,
    answer: str,
    sources: list[int],
    model: Optional[str] = None,
    tokens_in: Optional[int] = None,
    tokens_out: Optional[int] = None,
) -> int:
    """Guarda un mensaje de chat en el historial."""
    with get_cursor() as cursor:
        cursor.execute("""
            INSERT INTO chat_history
              (session_id, question, answer, sources, model, tokens_in, tokens_out)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (session_id, question, answer, json.dumps(sources), model, tokens_in, tokens_out))

        return cursor.lastrowid


def get_chat_history(session_id: str, limit: int = 20) -> list[ChatMessage]:
    """Obtiene historial de chat de una sesión."""
    with get_cursor() as cursor:
        cursor.execute("""
            SELECT id, session_id, question, answer, sources,
                   model, tokens_in, tokens_out, created_at
              FROM chat_history
             WHERE session_id = ?
             ORDER BY created_at DESC
             LIMIT ?
        """, (session_id, limit))

        return [
            ChatMessage(
                id=row["id"],
                session_id=row["session_id"],
                question=row["question"],
                answer=row["answer"],
                sources=json.loads(row["sources"] or "[]"),
                model=row["model"],
                tokens_in=row["tokens_in"],
                tokens_out=row["tokens_out"],
            )
            for row in cursor.fetchall()
        ]


def get_domains() -> list[str]:
    """Lista todos los dominios disponibles."""
    with get_cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT domain FROM contents ORDER BY domain
        """)
        return [row["domain"] for row in cursor.fetchall()]


def get_stats() -> dict:
    """Estadísticas de la base de conocimiento."""
    with get_cursor() as cursor:
        cursor.execute("""
            SELECT
                COUNT(*) as total_chunks,
                COUNT(DISTINCT source) as total_articles,
                COUNT(DISTINCT domain) as total_domains
            FROM contents
        """)
        row = cursor.fetchone()

        domains = get_domains()

        cursor.execute("""
            SELECT domain, COUNT(DISTINCT source) as articles
              FROM contents
             GROUP BY domain
        """)
        by_domain = {r["domain"]: r["articles"] for r in cursor.fetchall()}

        return {
            "total_chunks": row["total_chunks"],
            "total_articles": row["total_articles"],
            "total_domains": row["total_domains"],
            "domains": domains,
            "by_domain": by_domain,
            "db_size_mb": round(DATABASE_PATH.stat().st_size / (1024 * 1024), 2)
            if DATABASE_PATH.exists()
            else 0,
        }


def clear_content():
    """Limpia todo el contenido (para re-ingest)."""
    with get_cursor() as cursor:
        cursor.execute("DELETE FROM contents")
        cursor.execute("DELETE FROM contents_fts")
        cursor.execute("DELETE FROM chat_history")

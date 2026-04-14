# Alexandria — Arquitectura Técnica

## Visión

Alexandria es una base de conocimiento offline con IA local. Inspirada en la Biblioteca de Alejandría, permite consultar textos, imágenes y mapas sobre supervivencia, medicina básica e historia — sin Internet.

**Diferenciador:** una sola base consolidada (SQLite + FTS5) en vez de capas fragmentadas (ZIM + motor búsqueda + IA separada).

## Principios de diseño

- **Minimalismo:** 1 SQLite, 1 API, 1 carpeta de contenidos, 1 script de ingestión
- **Offline-first:** No requiere red. Ollama corre local.
- **Escalable en conocimiento:** Agregar contenido = agregar archivos .md a una carpeta + correr ingest
- **Hardware flexible:** Funciona en Mac mini viejo (2GB RAM), Raspberry Pi, o servidor

## Stack tecnológico

| Componente | Tecnología | Justificación |
|---|---|---|
| Base de datos | SQLite + FTS5 | Single-file, full-text search embebido, sin servidor |
| Embeddings | SQLite FTS5 BM25 | Sin vector DB externa, rápido, suficiente para recuperación |
| LLM | Ollama (cualquier modelo) | Local, offline, sin API key |
| API | FastAPI (Python) | Minimal, rápida, autodocumentada |
| Ingestión | Python (scripts) | Simple, ejecutable una vez o en watch mode |
| Frontend | React + Vite | UX moderna sin complejidad excesiva |

## Arquitectura

```
┌─────────────────────────────────────────┐
│         Carpeta content/                 │
│   (Markdown + imágenes por tema)         │
└──────────────┬──────────────────────────┘
               │ ingest.py
               ▼
┌─────────────────────────────────────────┐
│         alexandria.db                    │
│  ┌─────────────┐  ┌──────────────────┐  │
│  │contents    │  │chat_history      │  │
│  │(id,path,   │  │(id,session,     │  │
│  │ title,     │  │ question,        │  │
│  │ domain,    │  │ answer,          │  │
│  │ chunk,     │  │ sources,        │  │
│  │ chunk_idx) │  │ created_at)      │  │
│  └─────────────┘  └──────────────────┘  │
│  ┌─────────────────────────────────────┐│
│  │contents_fts (FTS5 virtual table)    ││
│  │ - title, domain, chunk (tokenized)  ││
│  └─────────────────────────────────────┘│
└──────────────┬──────────────────────────┘
               │ query + retrieve
               ▼
┌─────────────────────────────────────────┐
│         FastAPI (backend/)              │
│  GET  /search?q=...   → búsqueda FTS5  │
│  POST /chat           → recupera + genera│
│  GET  /domains        → lista dominios │
│  GET  /content/<id>  → contenido full  │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│         Ollama (puerto 11434)           │
│  Modelo: qwen3:14b (o el que esté)     │
└─────────────────────────────────────────┘
```

## Schema de SQLite

### Tabla `contents`

```sql
CREATE TABLE contents (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  source      TEXT    NOT NULL,      -- ruta del archivo fuente
  title       TEXT    NOT NULL,      -- título del artículo
  domain      TEXT    NOT NULL,      -- 'medicina' | 'supervivencia' | 'historia'
  subtopic    TEXT,                  -- subcategoría (ej: 'primeros-auxilios')
  chunk       TEXT    NOT NULL,      -- texto chunked (max ~800 tokens)
  chunk_idx   INTEGER DEFAULT 0,      -- índice del chunk dentro del artículo
  total_chunks INTEGER DEFAULT 1,    -- total de chunks del artículo
  has_images  INTEGER DEFAULT 0,     -- 1 si el artículo tiene imágenes
  created_at  TEXT    DEFAULT (datetime('now'))
);

CREATE INDEX idx_domain ON contents(domain);
CREATE INDEX idx_source ON contents(source);
```

### Tabla FTS5 `contents_fts`

```sql
CREATE VIRTUAL TABLE contents_fts USING fts5(
  title,
  domain,
  subtopic,
  chunk,
  content='contents',
  content_rowid='id',
  tokenize='porter unicode61'
);
```

### Tabla `chat_history`

```sql
CREATE TABLE chat_history (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  session_id TEXT    NOT NULL,
  question   TEXT    NOT NULL,
  answer     TEXT    NOT NULL,
  sources    TEXT,                  -- JSON array de content_ids recuperados
  model      TEXT,
  tokens_in  INTEGER,
  tokens_out INTEGER,
  created_at TEXT    DEFAULT (datetime('now'))
);

CREATE INDEX idx_session ON chat_history(session_id);
```

## Dominios de conocimiento

```
content/
├── medicina/
│   ├── primeros-auxilios/
│   │   ├── curacion-heridas.md
│   │   ├── rcp.md
│   │   └── quemaduras.md
│   ├── salud-natural/
│   │   └── plantas-medicinales.md
│   └── enfermedades/
│       └── enfermedades-comunes.md
├── supervivencia/
│   ├── agua-y-alimentacion/
│   │   ├── purificacion-agua.md
│   │   └── plantas-comestibles.md
│   ├── refugio-y-fuego/
│   │   ├── construir-refugio.md
│   │   └── hacer-fuego.md
│   └── orientacion/
│       └── lectura-mapas.md
├── historia/
│   ├── civilizaciones/
│   │   ├── egipto.md
│   │   ├── roma.md
│   │   └── Grecia.md
│   ├── eventos/
│   │   └── revoluciones.md
│   └── personajes/
│       └── heroes.md
└── mapas/
    └── region-x/
```

## Pipeline de ingestión

```
1. Walk contenido/
2. Por cada .md:
   a. Extraer frontmatter (title, domain, subtopic)
   b. Chunking: split por ## (headers) con overlap
   c. Por cada chunk → INSERT en contents
3. Rebuild FTS5 index
4. Reporte de artículos/chunks ingestados
```

**Frontmatter esperado:**
```yaml
---
title: Título del artículo
domain: medicina | supervivencia | historia
subtopic: categoria-especifica
has_images: true | false
---
```

## API endpoints

| Método | Path | Descripción |
|---|---|---|
| GET | `/health` | Health check |
| GET | `/domains` | Lista dominios disponibles |
| GET | `/search?q=&domain=&limit=` | Búsqueda full-text |
| GET | `/content/<id>` | Contenido completo de un artículo |
| POST | `/chat` | Chat con contexto recuperado |
| GET | `/chat/history/<session_id>` | Historial de chat |
| GET | `/stats` | Estadísticas: artículos, chunks, dominios |

## Prompt del sistema (Librarian)

```
Eres el Bibliotecario de Alexandria, la biblioteca de conocimiento offline de la humanidad.
Tu propósito es ayudar a los usuarios a encontrar respuestas verificables en la base de conocimiento local.

REGLAS:
1. Responde SOLO con información recuperada del contexto proporcionado.
2. Si la información del contexto es insuficiente, dilo con honestidad.
3. Cita las fuentes: menciona el título del artículo de donde viene la información.
4. Usa un tono claro, directo y accesible.
5. Si la pregunta está fuera de los dominios de Alexandria (medicina, supervivencia, historia), dilo.
6. Para temas médicos: siempre aclarar que es orientación general y buscar atención profesional.

FORMATO de respuesta:
- Respuesta clara
- Fuentes: [Título del artículo]
```

## Roadmap técnico

- [ ] Schema SQLite + migrations
- [ ] Script ingest.py (chunking + indexing)
- [ ] API FastAPI (search + chat + stats)
- [ ] Frontend React (búsqueda + chat)
- [ ] Dockerfile para desplegar en cualquier máquina
- [ ] Pipeline de descarga de contenidos (Wikipedia, WikiMed)
- [ ] Soporte para imágenes (base64 inline en chunks)
- [ ] Mapas offline (Organic Maps tiles)

## Hardware objetivo

| Dispositivo | RAM | Modelo sugerido |
|---|---|---|
| PC moderno | 16GB+ | qwen3:14b |
| Notebook | 8GB | qwen3:8b |
| Mac mini / NUC | 4-8GB | qwen2.5-coder:14b o phi4-mini |
| Raspberry Pi 4 | 2-4GB | qwen2.5:3b o 0.5b |

Ollama selecciona automáticamente según la RAM disponible.

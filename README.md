![Offline First](https://img.shields.io/badge/Offline%20First-Sí-ff6b00?style=for-the-badge)
![Privacidad](https://img.shields.io/badge/Privacidad-Total-2f855a?style=for-the-badge)
![IA Local](https://img.shields.io/badge/IA%20Local-Sí-7c3aed?style=for-the-badge)
![Base de Conocimiento](https://img.shields.io/badge/Base%20de%20Conocimiento-SQLite%20%2B%20FTS5-2563eb?style=for-the-badge)
![LLM](https://img.shields.io/badge/LLM-Ollama-0ea5e9?style=for-the-badge)
![Stack](https://img.shields.io/badge/Backend-FastAPI%20%2B%20Python-22c55e?style=for-the-badge)
![Hardware](https://img.shields.io/badge/Hardware-Raspberry%20Pi%20%2F%20PC-f97316?style=for-the-badge)

<p align="center">
  <img src="https://github.com/rquezada-tech/alexandria/raw/main/logo_alexandria.png" alt="Alexandria Logo" width="340">
</p>

# Alexandria

> *La memoria de la humanidad, preservada offline.*

Alexandria es una base de conocimiento offline con inteligencia artificial local. Inspirada en la legendaria Biblioteca de Alejandría, permite consultar textos sobre supervivencia, medicina básica, historia, herramientas, electrónica y más — sin necesidad de conexión a Internet.

## Qué es

Alexandria responde preguntas usando una base de conocimiento local y un modelo de lenguaje que corre en tu hardware. No envía datos a ninguna nube. Todo funciona offline.

Está diseñada para:
- **Situaciones de emergencia** donde no hay Internet
- **Privacidad total** — ningún dato sale de tu máquina
- **Supervivencia y autonomía** — conocimiento práctico verificable
- **Educación offline** — en zonas rurales, barcos, o simplemente como copia de seguridad

## Dominios de conocimiento

Alexandria cubre estos dominios:

| Dominio | Contenido |
|---|---|
| Medicina | Primeros auxilios, salud básica |
| Supervivencia | Agua, alimentación, refugio |
| Historia | Civilizaciones, eventos, personajes |
| Herramientas | Fabricación, uso, reparación, nudos |
| Electrónica | Componentes, fuentes, paneles solares DIY |
| Manufactura | Química básica, solar, materiales |
| Comunicaciones | Radio FM, Morse, antenas |

El contenido se expande agregando archivos Markdown a la carpeta `content/`.

## Requisitos

- **Python 3.10+**
- **Ollama** corriendo en `localhost:11434`
- **4GB RAM mínimo** (para modelos pequeños como `qwen2.5:3b`)

Ollama puede instalar modelos automáticamente, pero puedes especificar el que prefieras.

## Instalación rápida

```bash
# 1. Clona el repositorio
git clone https://github.com/rquezada-tech/alexandria.git
cd alexandria

# 2. Crea el entorno virtual e instala dependencias
python3 -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate         # Windows
pip install -r requirements.txt

# 3. Instala e inicia Ollama (en otra terminal)
ollama serve
ollama pull qwen3:14b            # o el modelo que prefieras

# 4. Inicia Alexandria
./run.sh
```

Abre **http://localhost:8080/static/index.html** en tu navegador.

## Uso

### Agregar conocimiento nuevo

Crea archivos Markdown con este frontmatter:

```markdown
---
title: Título del artículo
domain: medicina          # medicina | supervivencia | historia | herramientas | electronica | manufactura | comunicaciones
subtopic: primeros-auxilios
has_images: false
---

# Título

Contenido del artículo en Markdown...
```

Guarda el archivo en `content/<dominio>/<subtema>/nombre.md` y ejecuta:

```bash
python backend/ingest.py --verbose
```

El contenido se indexa automáticamente en la base SQLite con búsqueda full-text.

### Ingestar contenido de ejemplo

```bash
# Primer uso: ingesta todo el contenido seed
python backend/ingest.py --clear --verbose
```

### API

Alexandria expone una API REST en `http://localhost:8080`:

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/health` | Health check |
| GET | `/domains` | Lista de dominios disponibles |
| GET | `/stats` | Estadísticas de la base |
| GET | `/search?q=&domain=&limit=` | Búsqueda full-text |
| GET | `/content/<id>` | Contenido completo de un artículo |
| POST | `/chat` | Chat con contexto recuperado |

Ejemplo de chat:

```bash
curl -X POST http://localhost:8080/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "¿Cómo purifico agua en campo?", "domain": "supervivencia"}'
```

### Selector de modelo

Por defecto Alexandria detecta la RAM disponible y elige un modelo apropiado. También puedes especificarlo:

```bash
OLLAMA_MODEL=qwen3:8b ./run.sh
```

Modelos compatibles con Ollama:

| RAM | Modelo recomendado |
|---|---|
| 2-4 GB | `qwen2.5:3b` o `qwen2.5:0.5b` |
| 4-8 GB | `phi4-mini` o `qwen2.5:7b` |
| 8-16 GB | `qwen3:8b` |
| 16+ GB | `qwen3:14b` o mayor |

## Estructura del proyecto

```
alexandria/
├── backend/
│   ├── db.py          # Schema SQLite FTS5 + helpers
│   ├── api.py         # FastAPI (endpoints REST)
│   └── ingest.py      # Script de ingestión de contenido
├── content/           # Carpeta de conocimiento (Markdown)
│   ├── medicina/
│   ├── supervivencia/
│   ├── historia/
│   ├── herramientas/
│   ├── electronica/
│   ├── manufactura/
│   └── comunicaciones/
├── data/              # SQLite DB (generado automáticamente)
├── frontend/
│   └── index.html    # Interfaz web
├── requirements.txt   # Dependencias Python
└── run.sh            # Script de inicio
```

## Arquitectura

Alexandria usa:

- **SQLite + FTS5** — base de datos single-file con búsqueda full-text embebida
- **Chunking semántico** — cada artículo se divide en chunks de ~600 palabras con overlap
- **BM25 ranking** — recuperación por relevancia sobre FTS5 (sin vector DB externa)
- **RAG simple** — los chunks más relevantes se pasan como contexto al LLM
- **Ollama** — cualquier modelo local (qwen, phi, llama, etc.)

No se usa ChromaDB, Pinecone, ni ningún servicio externo. La base de conocimiento es un solo archivo SQLite.

## Diferencia con otros proyectos

| Característica | Alexandria | refugiOS | civilization_node | AnythingLLM |
|---|---|---|---|---|
| Single-file DB | SQLite FTS5 | ZIM + separado | Vector DB | Vector DB |
| Sin Docker | Sí | No | No | Sí |
| Sin servicios intermedios | Sí | ZIM reader | Open WebUI + Docker | Node.js |
| Contenido consolidado | Sí (un DB) | Separado (wiki/IA/map) | Wikipedia (ZIM) | Docs propios |
| Contenido custom | Fácil (.md) | Complejo | Complejo | Fácil |
| Hardware mínimo | 2GB RAM | 8GB RAM | 12GB RAM | 4GB RAM |

## Roadmap

- [ ] Pipeline de descarga masiva de Wikipedia y WikiMed
- [ ] Dockerización (un solo comando)
- [ ] Soporte para imágenes inline en artículos
- [ ] Mapas offline (Organic Maps)
- [ ] Interface de chat conversacional
- [ ] Indexación incremental (watch mode)
- [ ] Exportar/importar base de conocimiento

## Licencia

MIT

---

*Alexandria: la ambición de preservar todo el conocimiento de la humanidad en un solo lugar accesible offline.*

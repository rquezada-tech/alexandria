# Alexandria

<p align="center">
  <img src="https://github.com/rquezada-tech/alexandria/raw/main/logo_alexandria.png" alt="Alexandria Logo" width="340">
</p>

> *La memoria de la humanidad, preservada offline.*

<!-- Badges -->
<div align="center">

![Estado](https://img.shields.io/badge/Estado-Desarrollo-ff6b00?style=flat-square&labelColor=374151)
![Versión](https://img.shields.io/badge/Versión-0.6.0-2563eb?style=flat-square&labelColor=374151)
![Paradigma](https://img.shields.io/badge/Paradigma-Offline%20First-f97316?style=flat-square&labelColor=374151)
![IA](https://img.shields.io/badge/IA-Local%20(Llamafile/Ollama)-7c3aed?style=flat-square&labelColor=374151)
![Hardware](https://img.shields.io/badge/Hardware-Raspberry%20Pi%20%2F%20PC-ec4899?style=flat-square&labelColor=374151)
![RAM](https://img.shields.io/badge/RAM-4GB%20mín.-22c55e?style=flat-square&labelColor=374151)
![Stack](https://img.shields.io/badge/Stack-Python%20%2B%20SQLite%20%2B%20FastAPI-0ea5e9?style=flat-square&labelColor=374151)
![Licencia](https://img.shields.io/badge/Licencia-MIT-2f855a?style=flat-square&labelColor=374151)

</div>

## Qué es

Alexandria es una base de conocimiento offline con inteligencia artificial local. Inspirada en la legendaria Biblioteca de Alejandría, permite consultar textos sobre supervivencia, medicina básica, historia, herramientas, electrónica y más — sin necesidad de conexión a Internet.

**Alexandria responde preguntas usando una base de conocimiento local y un modelo de lenguaje que corre en tu hardware. No envía datos a ninguna nube. Todo funciona offline.**

Está diseñada para:
- **Situaciones de emergencia** donde no hay Internet
- **Privacidad total** — ningún dato sale de tu máquina
- **Supervivencia y autonomía** — conocimiento práctico verificable
- **Educación offline** — en zonas rurales, barcos, o simplemente como copia de seguridad

## Dominios de conocimiento

| Dominio | Contenido | Artículos |
|---|---|---:|
| Medicina | Primeros auxilios, salud básica, biología | 31,342 |
| Historia | Civilizaciones, geografía, eventos | 32,057 |
| Manufactura | Química, física, matemáticas | 34,308 |
| Electrónica | Computación, componentes, DIY | 28,205 |
| Supervivencia | Agua, alimentación, refugio, fuego | 4 |
| Herramientas | Fabricación, reparación, nudos | 4 |
| Comunicaciones | Radio FM, Morse, antenas | 1 |

El contenido se alimenta desde Wikipedia vía dumps ZIM y artículos Markdown propios. Se expande agregando archivos `.md` a la carpeta `content/`.

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

### Ingestar todo el contenido

```bash
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
├── scripts/
│   ├── zim_extract     # Extractor C++ de dumps ZIM
│   ├── zim_pipeline.py # Pipeline completo ZIM → Alexandria
│   └── html_to_alexandria.py  # Conversor HTML → Markdown
├── requirements.txt
└── run.sh
```

## Arquitectura

Alexandria usa:

- **SQLite + FTS5** — base de datos single-file con búsqueda full-text embebida
- **Chunking semántico** — cada artículo se divide en chunks de ~600 palabras con overlap
- **BM25 ranking** — recuperación por relevancia sobre FTS5 (sin vector DB externa)
- **RAG simple** — los chunks más relevantes se pasan como contexto al LLM
- **Ollama** — cualquier modelo local (qwen, phi, llama, etc.)

No se usa ChromaDB, Pinecone, ni ningún servicio externo. La base de conocimiento es un solo archivo SQLite (~2.3GB con Wikipedia completo).

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

- [x] Pipeline de descarga masiva de Wikipedia (ZIM)
- [x] 125,000+ artículos de Wikipedia ingestados
- [ ] Dockerización (un solo comando)
- [ ] Soporte para imágenes inline en artículos
- [ ] Mapas offline (Organic Maps)
- [ ] Indexación incremental (watch mode)
- [ ] Exportar/importar base de conocimiento
- [ ] Métricas de calidad del contenido

---

## Política de contribución

> **Este proyecto eventualmente será público.** Mientras tanto, la colaboración está abierta bajo las mismas reglas.

Alexandria welcomes contributions from the community. This project follows a **open contribution model** with the following principles:

### ¿Cómo contribuir?

**1. Contenido (artículos Markdown)**
- Agrega artículos en español sobre los dominios existentes
- Cada artículo debe tener frontmatter válido: `title`, `domain`, `subtopic`
- El contenido debe ser verificable, práctico y orientado a autonomía
- No aceptamos contenido que requiera conexión a Internet para funcionar

**2. Código (backend, frontend, scripts)**
- Abre un issue primero para discutir cambios mayores
- Los PRs pequeños son mejores: resuelven un problema específico
- Incluye tests si agregas funcionalidad nueva
- Respeta la filosofía del proyecto: offline, simple, sin dependencias externas innecesarias

**3. Reporte de errores**
- Usa issues para reportar bugs con pasos para reproducir
- Incluir el nombre del artículo, la pregunta feita y la respuesta esperada
- Para bugs de búsqueda: incluye la query y los resultados obtenidos

**4. Mejoras y features**
- Discutimos en issues antes de implementar
- Se valora especialmente todo lo que reduzca dependencias o simplifique el stack

### Lo que NO vamos a aceptar

- Contenido que infrinja derechos de autor (copias literales de fuentes con copyright)
- Features que requieran servicios externos o conexión a Internet
- Código que agregue dependencias de runtime innecesarias
- Cambios que rompan la compatibilidad hacia atrás de la API

### Proceso de PR

```
1. Fork del repositorio
2. Crea una rama: git checkout -b feature/mi-mejora
3. Haz tus cambios y commitea: git commit -m "Descripción clara"
4. Push a tu fork: git push origin feature/mi-mejora
5. Abre un Pull Request con descripción clara de qué y por qué
```

### Normas de conducta

- Sé respetuoso con otros colaboradores
- Las discusiones técnicas se resuelven con datos, no con opinión
- Prioriza la utilidad práctica sobre la elegancia teórica

---

## Licencia

MIT

---

*Alexandria: la ambición de preservar todo el conocimiento de la humanidad en un solo lugar accesible offline.*

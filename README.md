# Alexandria

<p align="center">
  <img src="https://github.com/rquezada-tech/alexandria/raw/main/logo_alexandria.png" alt="Alexandria Logo" width="340">
</p>

> *La memoria de la humanidad, preservada offline.*

<!-- Badges -->
<div align="center">

![Estado](https://img.shields.io/badge/Estado-Desarrollo-ff6b00?style=flat-square&labelColor=374151)
![Versión](https://img.shields.io/badge/Versión-0.7.6-2563eb?style=flat-square&labelColor=374151)
![Paradigma](https://img.shields.io/badge/Paradigma-Offline%20First-f97316?style=flat-square&labelColor=374151)
![IA](https://img.shields.io/badge/IA-Ollama%20%2B%20Voz%20Offline-7c3aed?style=flat-square&labelColor=374151)
![Hardware](https://img.shields.io/badge/Hardware-Raspberry%20Pi%20%2F%20PC-ec4899?style=flat-square&labelColor=374151)
![RAM](https://img.shields.io/badge/RAM-4GB%20mín.-22c55e?style=flat-square&labelColor=374151)
![Stack](https://img.shields.io/badge/Stack-Python%20%2B%20SQLite%20%2B%20FastAPI-0ea5e9?style=flat-square&labelColor=374151)
![Licencia](https://img.shields.io/badge/Licencia-MIT-2f855a?style=flat-square&labelColor=374151)

</div>

## Qué es

Alexandria es una base de conocimiento offline con inteligencia artificial local. Inspirada en la legendaria Biblioteca de Alejandría, permite consultar textos sobre supervivencia, medicina básica, historia, herramientas, electrónica y más — sin necesidad de conexión a Internet.

**Alexandria responde preguntas usando una base de conocimiento local y un modelo de lenguaje que corre en tu hardware. No envía datos a ninguna nube. Todo funciona offline. También puede escucharte y responderte por voz — sin necesidad de internet ni servicios cloud.**

Está diseñada para:
- **Situaciones de emergencia** donde no hay Internet
- **Privacidad total** — ningún dato sale de tu máquina
- **Supervivencia y autonomía** — conocimiento práctico verificable
- **Educación offline** — en zonas rurales, barcos, o simplemente como copia de seguridad

## Dominios de conocimiento

> **Al ejecutar `docker compose up` se descarga automáticamente Wikipedia completo (~125,000 artículos)** via pipeline ZIM. La columna "Repo" muestra solo lo que está en el repositorio; la columna "Docker" muestra el total disponible al instante.

| Dominio | Contenido | Repo | Docker |
|---|---|---:|---:|
| Medicina | Primeros auxilios, salud básica | 3 | 31,342 |
| Historia | Civilizaciones, geografía, eventos | 2 | 32,057 |
| Manufactura | Química, física, matemáticas | 3,609 | 34,308 |
| Electrónica | Computación, componentes, DIY | 4 | 28,205 |
| Supervivencia | Agua, refugio, fuego, orientación, fauna, nudos | 11 | 11 |
| Herramientas | Fabricación, reparación, nudos | 4 | 4 |
| Comunicaciones | Radio FM, Morse, antenas | 1 | 1 |
| **Mapas offline** | Chile, Sudamérica, Latinoamérica, Europa, Mundo | 0 | 5 regiones |

**Total repo:** 24 artículos en texto. **Total Docker:** ~126,000 artículos + 5 regiones de mapas.

El contenido se expande agregando archivos `.md` a la carpeta `content/`. Los artículos nuevos se indexan automáticamente al reiniciar.

## Requisitos

- **Python 3.10+**
- **Ollama** corriendo en `localhost:11434`
- **4GB RAM mínimo** (para modelos pequeños como `qwen2.5:3b`)
- **Whisper** (opcional, para control por voz): `brew install whisper`
- **mlx-audio** (opcional, para síntesis de voz): `brew install mlx-audio`

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

Abre **http://localhost:8080** en tu navegador.


## Docker (un solo comando)

La forma más rápida de correr Alexandria:

```bash
# 1. Clona y entra al directorio
git clone https://github.com/rquezada-tech/alexandria.git
cd alexandria

# 2. Copia tu contenido (opcional — sin contenido igualmente funciona)
# cp tu_contenido/*.md content/medicina/

# 3. Arranca todo (API + Ollama + contenido)
docker compose up
```

Abre **http://localhost:8080**

### Modelos disponibles

Por defecto usa `qwen2.5:3b` (~2GB). Para cambiar el modelo:

```bash
OLLAMA_MODEL=qwen3:14b docker compose up --build
```

Modelos compatibles (requieren más RAM):

| Modelo | RAM mínima | Notas |
|---|---|---|
| `qwen2.5:3b` | 4 GB | Por defecto |
| `phi4-mini` | 4 GB | Buena calidad, rápido |
| `qwen2.5:7b` | 8 GB | Mejor calidad |
| `qwen3:8b` | 12 GB | Excelente razonamiento |
| `qwen3:14b` | 16 GB | Máxima calidad |

### Agregar contenido

```bash
# Copia archivos Markdown a content/
cp mis_articulos/*.md content/medicina/

# Reinicia para que se re-ingeste
docker compose restart
```

### Con Ollama externo (avanzado)

Si ya tienes Ollama corriendo en otra máquina:

```yaml
# docker-compose.override.yml
services:
  alexandria:
    environment:
      - OLLAMA_BASE=http://tu-ip:11434
    depends_on: []   # Quitar dependencia de ollama
  ollama:
    image: tainer
```



### Por voz

Alexandria puede escucharte y responderte con voz offline:

```bash
# STT: graba tu voz desde la interfaz web (botón 🎤)
# TTS: presiona 🔊 en cualquier respuesta del Bibliotecario

# También via API:
curl -X POST http://localhost:8080/audio/stt -F "audio=@pregunta.wav"
curl "http://localhost:8080/audio/tts?q=C%C3%B3mo%20purifico%20agua"
```

Endpoints de audio en la API:

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/audio/stt` | Recibe audio WAV/MP3, retorna texto |
| GET | `/audio/tts?q=` | Recibe texto, retorna audio WAV |


### Mapas offline

Alexandria incluye un visualizador de mapas que funciona sin conexión:

```bash
# 1. Descarga las librerías (MapLibre GL + PMTiles)
python scripts/setup_maps_libs.py

# 2. Descarga regiones en formato PMTiles
python scripts/download_pmtiles.py --region chile      # Chile
python scripts/download_pmtiles.py --region sudamerica  # Sudamérica
python scripts/download_pmtiles.py --list               # Ver todas

# 3. Accede desde Alexandria
# Abre http://localhost:8080/maps
```

Regiones disponibles para descarga:

| Región | Archivo | Descripción |
|---|---|---|
| Chile | `chile.pmtiles` | Chile continental + insular |
| Sudamérica | `sudamerica.pmtiles` | Continente completo |
| Latinoamérica | `latam.pmtiles` | México a Argentina |
| Europa | `europa.pmtiles` | Continente europeo |
| Mundo | `world.pmtiles` | Mapa mundial general |

Los mapas se sirven desde `data/maps/` y se accede via `/maps`. No requieren conexión a Internet una vez descargados.

## Ebooks offline

Alexandria incluye un lector de libros en formato Markdown que funciona sin conexión:

```bash
# Los ebooks se organizan en content/ebooks/
# Estructura:
content/ebooks/MI_LIBRO/
  book.md          # metadata (title, author, language)
  capitulo-01.md   # capítulos en .md
  capitulo-02.md
  ...

# Accede desde http://localhost:8080/ebooks
```

El lector incluye navegación por capítulos, tabla de contenidos, tipografía serif optimizada para lectura (Merriweather), drop cap, barra de progreso, temas (oscuro/claro/sepia) y ajustes de fuente. Funciona 100% offline.

## Integración con Kolibri

Alexandria puede importar contenido de canales Kolibri (Khan Academy, CK-12, PhET, etc.) y servirlo como artículos searcheables con la misma interfaz de siempre:

```bash
# 1. Descarga un canal .kolibri desde Kolibri Studio o desde un Kolibri existente
#    (archivo .db o carpeta con content.db)

# 2. Explorar el canal sin importar (solo lectura)
python scripts/import_kolibri_channel.py --input ./mi_canal.kolibri --list

# 3. Importar a content/ (convierte a .md con frontmatter kolibri)
python scripts/import_kolibri_channel.py --input ./mi_canal.kolibri --output ./content

# 4. Re-indexar (si no estás en modo --watch)
python backend/watch.py --once
```

Channels importados generan:

- Un artículo por cada recurso (video, documento, ejercicio, audio, HTML5)
- Frontmatter con `domain: kolibri`, `source_channel`, `kolibri_id`, `kind`
- Archivo índice en `content/kolibri/<canal>/00-INDICE.md`
- Carpeta `_files/` para copiar manualmente los archivos binarios asociados

> Los archivos grandes (videos, documentos) no se copian automáticamente por su tamaño.
> Úsalos directamente desde Kolibri o cópialos manualmente a `_files/`.
> Alexandria los referencia y los busca en texto para contexto de chat.

## Notas personales

Alexandria incluye un editor de notas personales integrado que funciona 100% offline:

```bash
# Accede desde http://localhost:8080/notes
```

Características del sistema de notas:

- **CRUD completo** — crear, editar y eliminar notas
- **Búsqueda full-text** — busca en título, contenido y tags
- **Tags** — organiza con etiquetas, filtra por tag
- **Auto-guardado** — guarda automáticamente 2s después de dejar de escribir
- **Editor Markdown** — toolbar rápido con negrita, cursiva, código, listas, encabezados, enlaces
- **Preview** — alterna entre editor raw y vista renderizada
- **Tags con autocompletado** — sugiere tags existentes mientras escribes

Las notas se guardan en `content/notes/` como archivos `.md` con frontmatter. Puedes editarlos directamente con cualquier editor de texto o moverlos por USB.

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
| GET | `/content/<id>/images` | Imágenes asociadas al artículo |
| GET | `/maps` | Visualizador de mapas offline |
| GET | `/maps/available` | Lista mapas offline descargados |
| GET | `/ebooks` | Lector de ebooks offline |
| GET | `/ebooks/list` | Lista libros y capítulos |
| GET | `/ebooks/chapter?book=&idx=` | Contenido de un capítulo |
| GET | `/notes` | Editor de notas personales |
| GET | `/notes/list?q=&tag=` | Lista notas (búsqueda + filtro) |
| GET | `/notes/tags` | Tags de notas con conteo |
| POST | `/notes` | Crea nota nueva |
| PUT | `/notes/{slug}` | Actualiza nota |
| DELETE | `/notes/{slug}` | Elimina nota |
| POST | `/chat` | Chat con contexto recuperado |
| POST | `/audio/stt` | Transcribe audio a texto (Whisper) |
| GET | `/audio/tts?q=` | Sintetiza texto a audio (mlx-audio) |

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
│   ├── api.py         # FastAPI (endpoints REST + audio STT/TTS)
│   ├── audio.py       # Módulo de audio: Whisper (STT) + mlx-audio (TTS)
│   ├── ingest.py      # Script de ingestión de contenido
│   └── watch.py      # Watch mode (indexación incremental con watchdog)
├── content/           # Carpeta de conocimiento (Markdown)
│   ├── medicina/
│   ├── supervivencia/
│   ├── historia/
│   ├── herramientas/
│   ├── electronica/
│   ├── manufactura/
│   ├── comunicaciones/
│   ├── ebooks/        # Ebooks (libros en Markdown por capítulos)
│   ├── kolibri/       # Contenido importado de canales Kolibri
│   └── notes/         # Notas personales (archivos .md)
├── data/              # SQLite DB + mapas offline + audio
├── frontend/
│   ├── index.html    # Interfaz principal
│   ├── maps.html     # Visualizador de mapas offline
│   ├── ebooks.html   # Lector de ebooks
│   └── notes.html    # Editor de notas personales
├── scripts/
│   ├── zim_extract       # Extractor C++ de dumps ZIM
│   ├── zim_pipeline.py   # Pipeline completo ZIM → Alexandria
│   ├── html_to_alexandria.py  # Conversor HTML → Markdown
│   ├── import_kolibri_channel.py  # Importador de canales Kolibri
│   ├── download_pmtiles.py   # Descargador de mapas PMTiles
│   └── setup_maps_libs.py   # Setup de librerías MapLibre
├── requirements.txt
└── run.sh
```

## Arquitectura

Alexandria usa:

> **Filosofía:** Alexandria es un solo proceso Python + una base SQLite. No usa contenedores adicionales, bases vectoriales, ni servicios intermedios. Cada línea de código debe justificar su existencia.

- **SQLite + FTS5** — base de datos single-file con búsqueda full-text embebida
- **Chunking semántico** — cada artículo se divide en chunks de ~600 palabras con overlap
- **BM25 ranking** — recuperación por relevancia sobre FTS5 (sin vector DB externa)
- **RAG simple** — los chunks más relevantes se pasan como contexto al LLM
- **Ollama** — cualquier modelo local (qwen, phi, llama, etc.)

No se usa ChromaDB, Pinecone, ni ningún servicio externo. La base de conocimiento es un solo archivo SQLite (~2.3GB con Wikipedia completo).

## Diferencia con otros proyectos

| **Característica**       | **Alexandria** | **refugiOS** | **civilization_node** | **AnythingLLM** | **N.O.M.A.D.** |
|---------------------------|----------------|---------------|------------------------|-----------------|----------------|
| **Contenedores extra**    | 0              | 1             | 1                      | 3+              | 7+              |
| **Base vectorial**        | No             | No            | Sí                     | Chroma          | Qdrant          |
| **Servicios intermedios** | No             | ZIM reader    | Open WebUI + Docker    | Redis + Node    | MySQL + varios  |
| **Offline completo**      | Sí             | Sí            | Solo IA                | No              | Sí              |
| **Voz offline (STT+TTS)**| Sí             | No            | No                     | No              | No              |
| **Instalación**           | `docker compose up` | Varios pasos | Docker                | `docker run`    | `curl \| bash`  |
| **Hardware mínimo**       | 2GB RAM        | 8GB RAM       | 12GB RAM              | 4GB RAM         | 8GB RAM+        |
| **Contenido custom**      | Fácil (.md)    | Complejo      | Complejo              | Fácil           | Medio           |
| **Líneas de código**      | ~50MB          | ~1GB          | ~5GB                  | ~2GB            | ~7GB tooling    |

**Alexandria es el único proyecto con control por voz 100% offline** — usa Whisper para transcripción y mlx-audio para síntesis, sin enviar audio a ninguna nube.

Alexandria consume ~50MB de código. Es el proyecto más ligero orientado a autonomía real.

### Completado
- [x] Pipeline de descarga masiva de Wikipedia (ZIM)
- [x] 125,000+ artículos de Wikipedia ingestados
- [x] Dockerización (un solo comando)
- [x] Voz offline (STT con Whisper + TTS con mlx-audio)
- [x] Frontend con interfaz de voz (micrófono + altavoz)
- [x] Imágenes inline en artículos (figcaption, galería, lightbox)
- [x] Mapas offline (PMTiles + MapLibre GL, viewer en /maps)
- [x] Indexación incremental (watch mode con watchdog, re-index automático)
- [x] Lector de ebooks Markdown offline (navegación por capítulos, /ebooks)
- [x] Integración con Kolibri (import_kolibri_channel.py)
- [x] Notas personales (editor Markdown offline con auto-guardado y tags, /notes)
- [x] SVGs visuales en artículos de supervivencia (8 SVGs: nudos, navegación, fauna, refugio, señales)

### Próximos
- [ ] Exportar / importar base (zip: .db + content/)
- [ ] Métricas de calidad de artículos (completitud, enlaces internos)
- [ ] UI mejorada: dark mode, búsqueda avanzada, render de markdown
- [ ] CLI de gestión (`alexandria-cli` para ingestar, exportar, diagnosticar)
- [ ] Script de upgrade: `curl | bash` para actualizar desde GitHub
- [ ] Sync de contenido via filesystem (copiar carpeta content/ por USB)

### No planeados (van contra la filosofía de ser ligero)
- Sistema de autenticación / multi-usuario
- Base de datos vectorial (Qdrant, Chroma, etc.)
- Más contenedores Docker además de Alexandria + Ollama
- CyberChef embebido
- Command Center con panel de control complejo

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

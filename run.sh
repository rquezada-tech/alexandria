#!/bin/bash
# Alexandria - Script de inicio
# Uso:
#   ./run.sh              # modo normal (API)
#   ./run.sh --watch     # API + watch mode (re-index automático)
#   ./run.sh --once      # re-indexa todo y sale
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

WATCH_MODE=false
ONCE_MODE=false

while [[ $# -gt 0 ]]; do
  case $1 in
    --watch) WATCH_MODE=true; shift ;;
    --once) ONCE_MODE=true; shift ;;
    *) echo "Uso: $0 [--watch|--once]"; exit 1 ;;
  esac
done

echo "Iniciando Alexandria..."

# 0. Detectar Docker
if [ -f "/.dockerenv" ] || [ -n "$IN_DOCKER" ]; then
  echo "[Docker] Entorno Docker detectado."
else
  if ! curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "ADVERTENCIA: Ollama no está corriendo en localhost:11434"
    echo "Inicia Ollama con: ollama serve"
    echo ""
  fi
fi

# 1. Capacidades de audio
echo "--- Audio ---"
if command -v whisper &> /dev/null; then
  echo "  STT (Whisper): OK"
else
  echo "  STT (Whisper): NO instalado"
fi
if command -v mlx-audio &> /dev/null; then
  echo "  TTS (mlx-audio): OK"
else
  echo "  TTS (mlx-audio): NO instalado"
fi

# 2. Crear carpetas
mkdir -p data/audio data/maps

# 3. Instalar dependencias Python
if [ ! -f ".venv/bin/python" ]; then
  echo ""
  echo "Creando entorno virtual..."
  python3 -m venv .venv
  .venv/bin/pip install -q -r requirements.txt
fi

# 4. Modo --once: solo re-indexar y salir
if [ "$ONCE_MODE" = true ]; then
  echo ""
  echo "Re-indexando contenido..."
  .venv/bin/python backend/watch.py --once --verbose
  exit 0
fi

# 5. Re-index inicial (solo si hay archivos nuevos)
if [ "$WATCH_MODE" = true ]; then
  echo ""
  echo "Re-index inicial..."
  .venv/bin/python backend/watch.py --once 2>/dev/null || true

  echo ""
  echo "Iniciando watch mode (indexación incremental)..."
  .venv/bin/python backend/watch.py &
  WATCH_PID=$!
  echo "  Watch PID: $WATCH_PID"
  echo "  Ctrl+C para detener"
else
  # Modo normal: ingest clásico
  if [ ! -d "content" ] || [ -z "$(ls -A content 2>/dev/null)" ]; then
    echo "ADVERTENCIA: No hay contenido en content/"
  fi
  echo ""
  echo "Verificando base de conocimiento..."
  .venv/bin/python backend/ingest.py --content content 2>/dev/null || true
fi

# 6. Iniciar API
echo ""
echo "Iniciando API en http://localhost:8080"
echo "Abre http://localhost:8080"
echo ""

if [ "$WATCH_MODE" = true ]; then
  echo "Para detener todo: kill $WATCH_PID \$(pgrep -f 'uvicorn.*alexandria')"
else
  echo "Para detener: pkill -f 'uvicorn.*alexandria'"
fi

# Cleanup al salir
trap 'echo ""; echo "Deteniendo..."; [ -n "$WATCH_PID" ] && kill $WATCH_PID 2>/dev/null; pkill -f "uvicorn.*alexandria" 2>/dev/null; exit 0' INT TERM

.venv/bin/python -m uvicorn backend.api:app \
  --host 0.0.0.0 \
  --port 8080 \
  --reload

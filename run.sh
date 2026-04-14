#!/bin/bash
# Alexandria - Script de inicio (modo desarrollo/nativo)
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "Iniciando Alexandria..."

# 0. Detectar si estamos dentro de Docker
if [ -f "/.dockerenv" ] || [ -n "$IN_DOCKER" ]; then
  echo "[Docker] Entorno Docker detectado."
else
  # 1. Verificar que Ollama esté corriendo
  if ! curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "ADVERTENCIA: Ollama no está corriendo en localhost:11434"
    echo "Inicia Ollama con: ollama serve"
    echo ""
  fi
fi

# 2. Verificar herramientas de audio
echo "--- Capacidades de audio ---"
if command -v whisper &> /dev/null; then
  WHISPER_MODEL=${WHISPER_MODEL:-medium}
  echo "  STT (Whisper): OK ($WHISPER_MODEL)"
else
  echo "  STT (Whisper): NO instalado (brew install whisper)"
fi

if command -v mlx-audio &> /dev/null; then
  VOICE=${TTS_VOICE:-af_heart}
  echo "  TTS (mlx-audio): OK (voz: $VOICE)"
else
  echo "  TTS (mlx-audio): NO instalado (github.com/lucasnewman/mlx-audio)"
fi

# 3. Crear carpeta data si no existe
mkdir -p data/audio

# 4. Verificar contenido
if [ ! -d "content" ] || [ -z "$(ls -A content 2>/dev/null)" ]; then
  echo ""
  echo "ADVERTENCIA: No hay contenido en content/. Ejecuta: python3 backend/ingest.py"
fi

# 5. Instalar dependencias Python si falta
if [ ! -f ".venv/bin/python" ]; then
  echo ""
  echo "Creando entorno virtual..."
  python3 -m venv .venv
  .venv/bin/pip install -q -r requirements.txt
fi

# 6. Ingestar contenido fresco
echo ""
echo "Verificando base de conocimiento..."
.venv/bin/python backend/ingest.py --content content 2>/dev/null || true

# 7. Iniciar API
echo ""
echo "Iniciando API en http://localhost:8080"
echo "Abre http://localhost:8080 para ver la interfaz"
echo ""
echo "Para detener: pkill -f 'uvicorn.*alexandria'"

.venv/bin/python -m uvicorn backend.api:app \
  --host 0.0.0.0 \
  --port 8080 \
  --reload

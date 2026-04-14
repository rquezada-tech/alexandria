#!/bin/bash
# Alexandria - Script de inicio
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "Iniciando Alexandria..."

# 1. Verificar que Ollama esté corriendo
if ! curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
  echo "ADVERTENCIA: Ollama no está corriendo en localhost:11434"
  echo "Inicia Ollama con: ollama serve"
  echo ""
fi

# 2. Crear carpeta data si no existe
mkdir -p data

# 3. Verificar que existe contenido
if [ ! -d "content" ] || [ -z "$(ls -A content 2>/dev/null)" ]; then
  echo "ADVERTENCIA: No hay contenido en content/. Ejecuta: python3 backend/ingest.py"
fi

# 4. Instalar dependencias si falta
if [ ! -f ".venv/bin/python" ]; then
  echo "Creando entorno virtual..."
  python3 -m venv .venv
  .venv/bin/pip install -q -r requirements.txt
fi

# 5. Ingestar contenido fresco
echo "Verificando base de conocimiento..."
.venv/bin/python backend/ingest.py --content content 2>/dev/null || true

# 6. Iniciar API
echo "Iniciando API en http://localhost:8080"
echo "Abre http://localhost:8080/static/index.html para ver la interfaz"
echo ""
echo "Para detener: pkill -f 'uvicorn.*alexandria'"

.venv/bin/python -m uvicorn backend.api:app \
  --host 0.0.0.0 \
  --port 8080 \
  --reload

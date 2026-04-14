#!/bin/bash
set -e

echo "Iniciando Ollama en background..."
ollama serve &

OLLAMA_PID=$!

# Esperar a que Ollama responda
echo "Esperando que Ollama esté listo..."
for i in $(seq 1 30); do
    if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
        echo "Ollama listo."
        break
    fi
    sleep 1
done

# Asegurar carpeta data
mkdir -p /home/alexandria/data

echo "Ajustando permisos..."
chown -R alexandria:alexandria /home/alexandria

# Ingestar contenido si existe y la DB está vacía
if [ -d "/home/alexandria/content" ] && [ -n "$(ls -A /home/alexandria/content 2>/dev/null)" ]; then
    if [ ! -f "/home/alexandria/data/alexandria.db" ]; then
        echo "Ingestando contenido..."
        su alexandria -c "python backend/ingest.py --content content --clear" || true
    fi
fi

echo "Iniciando Alexandria API en http://0.0.0.0:8080..."
echo "Abre http://localhost:8080/static/index.html"

# Ejecutar el comando pasado (CMD del Dockerfile)
exec "$@"

# Alexandria - Dockerfile
# Imagen autocontenida con Alexandria + Ollama
# Uso: docker build -t alexandria . && docker run -p 8080:8080 alexandria
FROM python:3.11-slim

LABEL maintainer="Rodrigo Quezada <rodrigo@codehub.cl>"
LABEL description="Alexandria: base de conocimiento offline con IA local"

# ── Dependencias del sistema ──────────────────────────────
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# ── Usuario no-root ──────────────────────────────────────
RUN groupadd --gid 1000 alexandria \
    && useradd --uid 1000 --gid alexandria --shell /bin/bash --create-home alexandria

WORKDIR /home/alexandria

# ── Ollama (instala y descarga modelo) ───────────────────
# El modelo se baja una vez y queda cacheado
ENV OLLAMA_HOST=0.0.0.0
ENV OLLAMA_PORT=11434

RUN curl -fsSL https://ollama.ai/install.sh | sh

# Modelo por defecto: qwen2.5:3b (funciona en 4GB RAM)
# Cambia OLLAMA_MODEL en docker-compose para otro modelo
ENV OLLAMA_MODEL=qwen2.5:3b

# Descarga el modelo antes del primer arranque (BUILD-time)
RUN ollama pull $OLLAMA_MODEL

# ── Código de Alexandria ──────────────────────────────────
COPY --chown=alexandria:alexandria requirements.txt .
COPY --chown=alexandria:alexandria run.sh .
COPY --chown=alexandria:alexandria backend/ ./backend/
COPY --chown=alexandria:alexandria frontend/ ./frontend/ || true
COPY --chown=alexandria:alexandria content/ ./content/ || true

# Virtualenv
RUN python3 -m venv .venv
ENV PATH="/home/alexandria/.venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

# Base de datos y contenido como volúmenes
VOLUME ["/home/alexandria/data", "/home/alexandria/content"]

# Переменные окружения
ENV ALEXANDRIA_PORT=8080
ENV OLLAMA_BASE=http://localhost:11434

EXPOSE 8080

# Script de inicio: Ollama en background + API
COPY --chown=alexandria:alexandria docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD ["python", "-m", "uvicorn", "backend.api:app", "--host", "0.0.0.0", "--port", "8080"]

# Alexandria

> *La memoria de la humanidad, preservada para siempre.*

Alexandria es una base de conocimiento offline con inteligencia artificial local. Inspirada en la legendaria Biblioteca de Alejandría, permite consultar textos, imágenes y mapas sobre supervivencia, medicina básica e historia — sin necesidad de conexión a Internet.

## Principios

- **Offline First** — Todo funciona sin Internet
- **IA Local** — Modelos que corren en tu hardware
- **Conocimiento verificable** — Fuentes abiertas y verificables
- **Accesible** — Funciona en cualquier hardware, desde un notebook viejo hasta un servidor

## Dominios de conocimiento

- Medicina básica y primeros auxilios
- Supervivencia y técnicas de campo
- Historia universal y regional

## Arquitectura

```
┌─────────────────────────────────────┐
│           Frontend (React)           │
├─────────────────────────────────────┤
│         RAG Engine (Go)              │
│    Vector Search + Full-Text        │
├─────────────────────────────────────┤
│  LLM Local (Ollama) + Contenidos   │
│   Wikipedia · WikiMed · Fuentes CC  │
└─────────────────────────────────────┘
```

## Estado del proyecto

En desarrollo activo. Roadmap y documentación técnica en construcción.

## Licencia

MIT

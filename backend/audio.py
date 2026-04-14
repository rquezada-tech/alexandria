"""
Alexandria - Módulo de Audio (STT + TTS)
STT: Whisper CLI (via subprocess)
TTS: mlx-audio (via subprocess)
"""
import os
import uuid
import subprocess
import tempfile
import shutil
from pathlib import Path
from typing import Optional

# ── Config ──────────────────────────────────────────────
# Whisper CLI (Homebrew en macOS, o instalado de otra forma)
WHISPER_CMD = os.getenv("WHISPER_CMD", "whisper")
# Modelo por defecto para Whisper (debe estar cacheado)
WHISPER_MODEL = os.getenv("WHISPER_MODEL", "medium")
# mlx-audio CLI
MLX_AUDIO_CMD = os.getenv("MLX_AUDIO_CMD", "mlx-audio")
# Voz Kokoro para TTS (disponible: af_heart, bf_heart, etc.)
TTS_VOICE = os.getenv("TTS_VOICE", "af_heart")
# Carpeta para archivos temporales de audio
AUDIO_TMP_DIR = Path(__file__).parent.parent / "data" / "audio"
AUDIO_TMP_DIR.mkdir(parents=True, exist_ok=True)


# ── STT: Whisper ────────────────────────────────────────

def is_whisper_available() -> bool:
    """Verifica si whisper está instalado."""
    return shutil.which(WHISPER_CMD) is not None


def whisper_transcribe(audio_path: str, language: str = "es") -> str:
    """
    Transcribe un archivo de audio a texto usando Whisper CLI.
    Requiere que el modelo ya esté descargado (whisper --model medium ...).
    """
    if not is_whisper_available():
        raise RuntimeError(
            f"Whisper no está instalado. Instálalo con:\n"
            f"  macOS: brew install whisper\n"
            f"  Linux: pip install openai-whisper && whisper --help"
        )

    # Verificar que el archivo existe
    if not Path(audio_path).exists():
        raise FileNotFoundError(f"Archivo de audio no encontrado: {audio_path}")

    cmd = [
        WHISPER_CMD,
        "--model", WHISPER_MODEL,
        "--language", language,
        "--fp16", "False",  # Más compatible (CPU)
        "--quiet", "True",
        "--output-txt", "True",
        str(audio_path),
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=120,
    )

    if result.returncode != 0:
        raise RuntimeError(f"Whisper falló: {result.stderr}")

    # Whisper genera un .txt con el mismo nombre del audio
    txt_path = Path(audio_path).with_suffix(".txt")
    if txt_path.exists():
        return txt_path.read_text(encoding="utf-8").strip()

    # Fallback: extraer del stdout si no generó archivo
    return result.stdout.strip()


def transcribe_audio(audio_bytes: bytes, filename: str, language: str = "es") -> str:
    """
    Recibe audio en bytes, lo guarda temporalmente y lo transcribe.
    Retorna el texto transcrito.
    """
    ext = Path(filename).suffix.lower() or ".wav"
    tmp_path = AUDIO_TMP_DIR / f"stt_{uuid.uuid4().hex}{ext}"
    tmp_path.write_bytes(audio_bytes)

    try:
        return whisper_transcribe(str(tmp_path), language=language)
    finally:
        # Limpiar archivo temporal
        if tmp_path.exists():
            tmp_path.unlink()
        txt_path = tmp_path.with_suffix(".txt")
        if txt_path.exists():
            txt_path.unlink()


# ── TTS: mlx-audio ─────────────────────────────────────

def is_mlx_audio_available() -> bool:
    """Verifica si mlx-audio está instalado."""
    return shutil.which(MLX_AUDIO_CMD) is not None


def generate_speech(text: str, voice: str = TTS_VOICE) -> bytes:
    """
    Genera audio a partir de texto usando mlx-audio + Kokoro-82M.
    Retorna los bytes del archivo WAV generado.
    """
    if not is_mlx_audio_available():
        raise RuntimeError(
            f"mlx-audio no está instalado. Instálalo desde:\n"
            f"  https://github.com/lucasnewman/mlx-audio\n"
            f"O usa conda: conda install -c conda-forge mlx-audio"
        )

    if not text.strip():
        raise ValueError("El texto no puede estar vacío.")

    tmp_input = AUDIO_TMP_DIR / f"tts_{uuid.uuid4().hex}.txt"
    tmp_input.write_text(text, encoding="utf-8")

    output_path = AUDIO_TMP_DIR / f"tts_{uuid.uuid4().hex}.wav"

    try:
        cmd = [
            MLX_AUDIO_CMD,
            str(tmp_input),
            "--output", str(output_path),
            "--voice", voice,
            "--model", "Kokoro-82M",
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60,
        )

        if result.returncode != 0:
            raise RuntimeError(f"mlx-audio falló: {result.stderr}")

        if not output_path.exists():
            raise RuntimeError(
                f"mlx-audio no generó el archivo de audio. "
                f"Stdout: {result.stdout}, Stderr: {result.stderr}"
            )

        return output_path.read_bytes()

    finally:
        if tmp_input.exists():
            tmp_input.unlink()
        if output_path.exists():
            output_path.unlink()


def list_tts_voices() -> list[str]:
    """Lista las voces disponibles en mlx-audio."""
    if not is_mlx_audio_available():
        return []

    try:
        result = subprocess.run(
            [MLX_AUDIO_CMD, "--list-voices"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode == 0:
            return [v.strip() for v in result.stdout.strip().split("\n") if v.strip()]
    except Exception:
        pass

    # Voces conocidas de Kokoro-82M
    return [
        "af_heart",    # Femenina inglés
        "bf_heart",    # Masculino inglés
        "af_bella",    # Femenina inglés
        "bf_david",    # Masculino inglés
    ]

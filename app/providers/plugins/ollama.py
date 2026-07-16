"""
Learning OS — Ollama Local AI Provider Plugin.
Targets http://localhost:11434 for LLM inference (Qwen, DeepSeek, Llama, Gemma).
Falls back to a stub response when the server is unreachable.
"""
import logging
import requests
from typing import Optional
from app.providers.base import AIProvider

logger = logging.getLogger(__name__)

OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_TIMEOUT = 90  # seconds


class OllamaProvider(AIProvider):
    """
    Local Ollama provider.
    Supported models: qwen2.5:14b, deepseek-r1:14b, llama3.1:8b, gemma3:12b
    """

    def __init__(self, model: str = "qwen2.5:14b"):
        self._model = model

    @property
    def name(self) -> str:
        return f"ollama:{self._model}"

    def _is_available(self) -> bool:
        """Health-check the local Ollama server."""
        try:
            r = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=3)
            return r.status_code == 200
        except Exception:
            return False

    def chat(self, prompt: str, system: Optional[str] = None, **kwargs) -> str:
        """Send a generate request to Ollama REST API."""
        if not self._is_available():
            logger.warning("Ollama server unreachable — using fallback stub.")
            return self._fallback_response(prompt)

        payload = {
            "model": self._model,
            "prompt": prompt,
            "stream": False,
        }
        if system:
            payload["system"] = system

        try:
            r = requests.post(
                f"{OLLAMA_BASE_URL}/api/generate",
                json=payload,
                timeout=OLLAMA_TIMEOUT
            )
            r.raise_for_status()
            return r.json().get("response", "").strip()
        except Exception as exc:
            logger.error("Ollama chat error: %s", exc)
            return self._fallback_response(prompt)

    def embeddings(self, text: str) -> list[float]:
        """Return embedding vector from Ollama embed endpoint."""
        if not self._is_available():
            logger.warning("Ollama server unreachable — returning zero vector.")
            return [0.0] * 384  # nomic-embed-text default dim

        try:
            r = requests.post(
                f"{OLLAMA_BASE_URL}/api/embed",
                json={"model": "nomic-embed-text", "input": text},
                timeout=OLLAMA_TIMEOUT
            )
            r.raise_for_status()
            data = r.json()
            # Ollama embed API returns {"embeddings": [[...floats...]]}
            embeds = data.get("embeddings", [[]])
            return embeds[0] if embeds else [0.0] * 384
        except Exception as exc:
            logger.error("Ollama embeddings error: %s", exc)
            return [0.0] * 384

    def _fallback_response(self, prompt: str) -> str:
        """Stub response used when Ollama server is offline."""
        return (
            "[AI Unavailable] The local Ollama server is not running. "
            "Please start Ollama with 'ollama serve' and ensure the model is pulled."
        )

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
OLLAMA_TIMEOUT = 300  # seconds — qwen3 thinking mode needs extra time


class OllamaProvider(AIProvider):
    """
    Local Ollama provider.
    Supported models: qwen3:14b, qwen3-coder:30b, qwen2.5:14b, llama3.1:8b
    """

    def __init__(self, model: str = "qwen3:14b"):
        self._model = model

    @staticmethod
    def _strip_think_tags(text: str) -> str:
        """Remove <think>...</think> blocks emitted by qwen3 reasoning models."""
        import re
        text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
        return text.strip()

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
        """Send request to Ollama, collecting streamed tokens to avoid read timeouts.

        Uses stream=True internally so each token keeps the connection alive.
        This prevents read timeouts that occur with large non-streamed responses.
        """
        if not self._is_available():
            logger.warning("Ollama server unreachable — using fallback stub.")
            return self._fallback_response(prompt)

        payload = {
            "model": self._model,
            "prompt": prompt,
            "stream": True,           # Stream tokens to avoid read timeout
            "think": False,           # qwen3: skip reasoning tokens
            "options": {"num_predict": 1024},
        }
        if system:
            payload["system"] = system

        try:
            import json as _json
            r = requests.post(
                f"{OLLAMA_BASE_URL}/api/generate",
                json=payload,
                stream=True,
                timeout=OLLAMA_TIMEOUT,
            )
            r.raise_for_status()
            chunks = []
            for line in r.iter_lines():
                if line:
                    chunk = _json.loads(line.decode("utf-8"))
                    chunks.append(chunk.get("response", ""))
                    if chunk.get("done"):
                        break
            raw = "".join(chunks).strip()
            return self._strip_think_tags(raw)
        except Exception as exc:
            logger.error("Ollama chat error: %s", exc)
            return self._fallback_response(prompt)

    def chat_stream(self, prompt: str, system: Optional[str] = None, **kwargs):
        """Yield response chunks from Ollama REST API in real-time."""
        if not self._is_available():
            logger.warning("Ollama server unreachable — streaming fallback stub.")
            # Yield in chunks to simulate streaming for fallback/testing
            stub_response = self._fallback_response(prompt)
            # Yield words to simulate active streaming
            for word in stub_response.split(" "):
                yield word + " "
            return

        payload = {
            "model": self._model,
            "prompt": prompt,
            "stream": True,
        }
        if system:
            payload["system"] = system

        try:
            r = requests.post(
                f"{OLLAMA_BASE_URL}/api/generate",
                json=payload,
                stream=True,
                timeout=OLLAMA_TIMEOUT
            )
            r.raise_for_status()
            for line in r.iter_lines():
                if line:
                    import json
                    chunk = json.loads(line.decode("utf-8"))
                    yield chunk.get("response", "")
        except Exception as exc:
            logger.error("Ollama streaming chat error: %s", exc)
            yield "[Error during streaming generation]"

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

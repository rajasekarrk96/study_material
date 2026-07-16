"""
Learning OS — AI Provider Registry.
Resolves and instantiates the correct AI backend based on availability.
Priority: Ollama (local) → future cloud fallback.
"""
import logging
from app.providers.plugins.ollama import OllamaProvider
from app.providers.base import AIProvider

logger = logging.getLogger(__name__)

# Global singleton — lazy-initialized per request or at startup
_active_provider: AIProvider | None = None


def get_provider(model: str = "qwen2.5:14b") -> AIProvider:
    """
    Return the best-available AI provider.
    Attempts Ollama first; logs a warning if unavailable (fallback is built into OllamaProvider).
    """
    global _active_provider
    provider = OllamaProvider(model=model)
    if not provider._is_available():
        logger.warning("AI Provider: Ollama is offline. Responses will use the fallback stub.")
    _active_provider = provider
    return _active_provider

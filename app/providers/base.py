"""
Learning OS — AI Provider Base Interface.
All AI provider plug-ins implement this interface for clean swap-out behaviour.
"""
from abc import ABC, abstractmethod
from typing import Optional


class AIProvider(ABC):
    """Abstract base class every AI backend must implement."""

    @abstractmethod
    def chat(self, prompt: str, system: Optional[str] = None, **kwargs) -> str:
        """Send a chat message and return the generated text string."""
        ...

    @abstractmethod
    def embeddings(self, text: str) -> list[float]:
        """Return an embedding vector for the given text."""
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable provider name for logging."""
        ...

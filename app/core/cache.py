"""
Learning OS — Core Performance Caching.
Thread-safe, lightweight, in-memory caching decorator with TTL support.
"""
import time
from functools import wraps
from threading import Lock

_cache: dict[str, tuple[any, float]] = {}
_lock = Lock()


def cache_memoize(timeout_seconds: int = 300):
    """
    Caches function return values based on arguments.
    Default timeout: 5 minutes.
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Create unique cache key from function name and parameters
            key_parts = [f.__name__]
            if args:
                key_parts.append(str(args))
            if kwargs:
                key_parts.append(str(sorted(kwargs.items())))
            key = ":".join(key_parts)

            now = time.time()
            with _lock:
                if key in _cache:
                    val, expires = _cache[key]
                    if now < expires:
                        return val
                    # Evict expired entry
                    del _cache[key]

            # Calculate and store fresh result
            result = f(*args, **kwargs)
            with _lock:
                _cache[key] = (result, now + timeout_seconds)
            return result
        return decorated_function
    return decorator


def clear_cache():
    """Clears all stored entries in cache."""
    with _lock:
        _cache.clear()

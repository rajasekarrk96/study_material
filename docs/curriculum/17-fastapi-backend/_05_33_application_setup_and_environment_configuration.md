# Application Setup and Environment Configuration

> **Course**: Fastapi | **Module**: Production FastAPI | **Difficulty**: intermediate

---

### 1. Settings with pydantic-settings
```python
# pip install pydantic-settings
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "My FastAPI App"
    debug: bool = False
    database_url: str
    secret_key: str
    allowed_origins: list[str] = ["http://localhost:3000"]
    redis_url: str = "redis://localhost:6379"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
```

### 2. Dependency-Cached Settings
```python
from functools import lru_cache
from fastapi import Depends

@lru_cache
def get_settings():
    return Settings()

@app.get("/info")
async def info(s: Settings = Depends(get_settings)):
    return {"name": s.app_name, "debug": s.debug}
```

### 3. Lifespan Events (startup/shutdown)
```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await db.connect()
    redis = await aioredis.from_url(settings.redis_url)
    app.state.redis = redis
    print("App started")
    yield
    # Shutdown
    await db.disconnect()
    await redis.close()
    print("App stopped")

app = FastAPI(lifespan=lifespan)
```

### 4. Environment-Specific Configuration
```python
# .env.development
DEBUG=true
DATABASE_URL=sqlite+aiosqlite:///./test.db

# .env.production
DEBUG=false
DATABASE_URL=postgresql+asyncpg://user:pass@host/db
```

```python
import os
env = os.getenv("ENVIRONMENT", "development")
Settings(_env_file=f".env.{env}")
```

---

Configure a FastAPI app with environment-specific settings (dev/staging/prod), lifespan DB pool startup/shutdown, settings cached with `lru_cache`, and validated using pydantic-settings.

---

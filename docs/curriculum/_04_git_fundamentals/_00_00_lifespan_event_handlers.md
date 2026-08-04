# Lifespan Event Handlers

> **Course**: Git Fundamentals | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 8.1 Background Tasks](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_05_fastapi/_05_15_fastapi_background_tasks.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Understand the modern **Lifespan** architecture in FastAPI.
2. Define startup and shutdown hooks using **`@asynccontextmanager`**.
3. Pre-load Machine Learning models or database pools on server startup.
4. Execute clean connection pool teardown on server shutdown.

---

---

Open Python REPL or VS Code.

---

---

### 3.1 What are Lifespan Events?
Application **Lifespan Events** allow you to define code that runs **BEFORE** the application starts receiving HTTP requests (Startup) and code that runs **AFTER** the application finishes handling requests (Shutdown).

Modern FastAPI uses Python's `@asynccontextmanager` context manager passed into `FastAPI(lifespan=lifespan)` (replacing deprecated `@app.on_event("startup")`):

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          FASTAPI LIFESPAN EVENT CYCLE                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Code before `yield`: Startup Phase (Preload ML Model, Init DB Tables)   │
│ 2. `yield`: Application handles incoming HTTP client requests               │
│ 3. Code after `yield`: Shutdown Phase (Close DB Connection Pool)            │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

---

```mermaid
flowchart TD
    Start[Uvicorn Server Starts] --> Startup["Lifespan Code before yield: Load ML Model into Memory"]
    Startup --> Yield["yield: Serve HTTP API Requests"]
    Yield --> Stop[Uvicorn Server Shutdown Signal]
    Stop --> Shutdown["Lifespan Code after yield: Close Database Sockets"]
    Shutdown --> Exit[Server Exits Gracefully]
```

---

---

```python
# FastAPI Lifespan Event Handler Demonstration (lifespan_demo.py)
from contextlib import asynccontextmanager
from fastapi import FastAPI

# Simulated Heavy Machine Learning Model or DB Connection Pool
ml_models = {}

# 1. Define Modern Async Lifespan Context Manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- STARTUP PHASE ---
    print("[Lifespan Startup]: Pre-loading Heavy Machine Learning Model into GPU Memory...")
    ml_models["anomaly_detector"] = lambda temp: temp > 80.0
    print("[Lifespan Startup]: Machine Learning Model Ready!")

    yield # Yield control to application to process requests!

    # --- SHUTDOWN PHASE ---
    print("[Lifespan Shutdown]: Flushing In-Memory Caches & Closing DB Connection Pools...")
    ml_models.clear()
    print("[Lifespan Shutdown]: Cleanup Complete. Graceful Exit.")

# 2. Instantiate FastAPI App with Lifespan Argument
app = FastAPI(title="Lifespan Event API", lifespan=lifespan)

@app.get("/api/v1/detect-anomaly")
def detect_anomaly(temperature: float):
    detector = ml_models.get("anomaly_detector")
    is_anomaly = detector(temperature) if detector else False
    return {"temperature": temperature, "is_anomaly": is_anomaly}
```

---

---

- **AI/ML Model Microservices**: Production FastAPI inference services pre-load multi-gigabyte PyTorch/TensorFlow models into GPU memory during the lifespan startup phase, avoiding model load delays on individual API requests.

---

---

1. Save code as `lifespan_demo.py`.
2. Run `uvicorn lifespan_demo:app --reload`.
3. Stop server using `Ctrl+C` $\to$ Inspect terminal logs for both Startup pre-load and Shutdown cleanup messages!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`DeprecationWarning: on_event is deprecated`** | Using legacy `@app.on_event("startup")` or `@app.on_event("shutdown")`. | Migrate to modern `lifespan` context manager using `@asynccontextmanager`. |

---

---

- **Use `lifespan` Argument**: Always pass the lifespan context manager into `FastAPI(lifespan=lifespan)`.

---

---

### Q1: Why did FastAPI deprecate `@app.on_event("startup")` in favor of the `lifespan` context manager?
**Answer**: The `@asynccontextmanager` lifespan pattern unifies startup and shutdown logic into a single function. Variables initialized during startup (like state dictionaries or database connection pools) remain naturally in scope for shutdown cleanup code after `yield`, improving type safety and avoiding global variables.

---

---

```json
{
  "quiz_title": "Lesson 8.2 Lifespan Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which Python decorator from contextlib defines modern lifespan context managers in FastAPI?",
      "options": ["@contextmanager", "@asynccontextmanager", "@lifespan_event", "@startup_event"],
      "correct_answer_index": 1,
      "explanation": "@asynccontextmanager defines modern async lifespan managers."
    }
  ]
}
```

---

---

Build a lifespan context manager pre-loading an in-memory cache and tearing it down on shutdown.

---

---

**Front**: Where is the lifespan function registered on a FastAPI application instance?
**Back**: `app = FastAPI(lifespan=my_lifespan_func)`.
<!-- flashcard:end -->

---

---

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    yield
    # Shutdown code
app = FastAPI(lifespan=lifespan)
```

---

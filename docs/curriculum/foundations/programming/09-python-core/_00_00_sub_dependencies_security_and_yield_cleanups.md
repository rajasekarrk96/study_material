# Sub Dependencies Security And Yield Cleanups

> **Course**: Git Version Control | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 3.1 Dependency Injection](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_05_fastapi/_05_05_dependency_injection_architecture_and_depends.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Construct hierarchical **Sub-Dependency** trees.
2. Implement automatic database resource teardown using **Yield Dependencies (`yield`)**.
3. Enforce global authentication rules using **Router Dependencies**.
4. Mock dependencies during unit testing using **`app.dependency_overrides`**.

---

---

Open Python REPL or VS Code.

---

---

### 3.1 Yield Dependencies & Context Cleanup
When a dependency manages external resources (database connections, network sockets, open file handles), it needs to clean up after the HTTP request finishes.

Using Python's **`yield`** keyword inside a dependency function splits execution into two phases:
1. Everything before `yield` executes **BEFORE** the view function runs.
2. Everything after `yield` executes **AFTER** the HTTP response is sent to the client.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       YIELD DEPENDENCY EXECUTION PHASES                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Code before `yield`: Opens DB Socket ──► Injects Session into View      │
│ 2. View Function executes & returns HTTP Response to Client                 │
│ 3. Code after `yield`: Closes DB Socket safely (`db.close()`)              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

---

```mermaid
flowchart TD
    Req[Request Arrives] --> DepBefore["Dependency: Open DB Connection"]
    DepBefore --> Yield["yield db_session"]
    Yield --> View[Execute Route View Function]
    View --> Resp[Send Response to Client]
    Resp --> DepAfter["Dependency: Close DB Connection"]
```

---

---

```python
# Advanced Dependencies & Yield Teardown (advanced_deps_demo.py)
from typing import Generator
from fastapi import FastAPI, Depends, Header, HTTPException, status

app = FastAPI(title="Advanced Dependencies API")

# 1. Base Security Dependency: Extract Token Header
def get_auth_header(authorization: str = Header(...)) -> str:
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Authorization header format"
        )
    return authorization.split(" ")[1]

# 2. Sub-Dependency: Validates Token using output of get_auth_header!
def get_current_user(token: str = Depends(get_auth_header)) -> dict:
    if token != "SECRET_ACCESS_TOKEN":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired access token"
        )
    return {"user_id": 101, "username": "operator_admin", "role": "ADMIN"}

# 3. Yield Dependency for Resource Teardown
def get_db_session() -> Generator[str, None, None]:
    print("[DB Session]: Opening database connection socket...")
    db_session = "ACTIVE_DB_CONNECTION_HANDLE"
    try:
        yield db_session # Yields resource to view function!
    finally:
        print("[DB Session Teardown]: Closing database connection socket.")

# Route Handler consuming Sub-Dependency & Yield Dependency
@app.get("/api/v1/secure-telemetry")
def get_secure_telemetry(
    current_user: dict = Depends(get_current_user),
    db: str = Depends(get_db_session)
):
    return {
        "user": current_user["username"],
        "db_status": db,
        "telemetry_data": [24.5, 25.1, 24.8]
    }
```

### Mocking Dependencies in Unit Tests:

```python
# Overriding dependencies for Pytest testing!
def mock_get_current_user():
    return {"user_id": 999, "username": "test_user", "role": "TESTER"}

app.dependency_overrides[get_current_user] = mock_get_current_user
```

---

---

- **Database Connection Pool Management**: High-throughput FastAPI backends use `yield` dependencies to fetch database connections from a connection pool and return them safely to the pool after every request.

---

---

1. Save code as `advanced_deps_demo.py`.
2. Run `uvicorn advanced_deps_demo:app --reload`.
3. Send GET request with header `Authorization: Bearer SECRET_ACCESS_TOKEN` $\to$ Inspect terminal logs for opening and teardown messages!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Resource Leak / Unclosed Database Sockets** | Forgetting to wrap post-yield cleanup code in a `try...finally` block. | Always place resource closing calls inside `finally:` blocks following `yield`. |

---

---

- **Always Use `try...finally` with Yield**: Ensures cleanup code executes even if an exception is raised inside the view function.

---

---

### Q1: How do Yield Dependencies work in FastAPI and how do they prevent resource leaks?
**Answer**: Yield dependencies use Python generator syntax. Execution runs up to the `yield` statement before passing the yielded object to the view function. After the HTTP response is sent, execution resumes immediately after `yield`. Placing cleanup code inside a `finally:` block guarantees resource cleanup (closing DB connections or file handles) executes reliably.

---

---

```json
{
  "quiz_title": "Lesson 3.2 Advanced Dependencies Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which Python keyword splits execution in a FastAPI dependency to handle resource teardown after request completion?",
      "options": ["return", "yield", "finally", "await"],
      "correct_answer_index": 1,
      "explanation": "yield handles resource cleanup phases."
    }
  ]
}
```

---

---

Implement a database yield dependency wrapped in `try...finally` and write a pytest override for it.

---

---

**Front**: How do you override a dependency during unit testing in FastAPI?
**Back**: `app.dependency_overrides[original_dep] = mock_dep`.
<!-- flashcard:end -->

---

---

```python
def get_db():
    db = open_db()
    try: yield db
    finally: db.close()
```

---

# Custom Exception Handling

> **Course**: Fastapi | **Module**: Advanced Features | **Difficulty**: intermediate

---

### 1. HTTPException
```python
from fastapi import HTTPException

@app.get("/items/{id}")
async def get_item(id: int):
    item = db.get(id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Item {id} not found",
                            headers={"X-Error": "not-found"})
    return item
```

### 2. Custom Exception Classes
```python
class DomainError(Exception):
    def __init__(self, code: str, message: str, status: int = 400):
        self.code = code
        self.message = message
        self.status = status

@app.exception_handler(DomainError)
async def domain_error_handler(request: Request, exc: DomainError):
    return JSONResponse(
        status_code=exc.status,
        content={"error": exc.code, "message": exc.message}
    )

# Usage
raise DomainError("INVALID_EMAIL", "Email format invalid")
```

### 3. Override Validation Error Format
```python
from fastapi.exceptions import RequestValidationError

@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError):
    errors = [{"field": e["loc"][-1], "message": e["msg"]} for e in exc.errors()]
    return JSONResponse(status_code=422, content={"errors": errors})
```

### 4. Global Error Catch-All
```python
@app.exception_handler(Exception)
async def generic_handler(request: Request, exc: Exception):
    logger.exception("Unhandled error: %s", exc)
    return JSONResponse(status_code=500, content={"error": "Internal server error"})
```

---

Build a standardised error response system with: custom exception base class, field-level validation errors, 404/403/500 handlers, and error logging middleware.

---

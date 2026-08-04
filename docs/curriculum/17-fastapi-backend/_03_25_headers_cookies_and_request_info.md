# Headers Cookies and Request Info

> **Course**: Fastapi | **Module**: Advanced Features | **Difficulty**: intermediate

---

### 1. Reading Headers
```python
from fastapi import Header

@app.get("/auth")
async def auth(
    authorization: Annotated[str, Header()],
    x_api_version: Annotated[str | None, Header()] = None,
):
    return {"auth": authorization, "version": x_api_version}
```

### 2. Reading Cookies
```python
from fastapi import Cookie

@app.get("/session")
async def session(session_id: Annotated[str | None, Cookie()] = None):
    return {"session": session_id}
```

### 3. Setting Response Headers and Cookies
```python
from fastapi import Response

@app.post("/login")
async def login(response: Response, username: str = Form(...)):
    token = create_token(username)
    response.set_cookie(key="session", value=token, httponly=True,
                        samesite="lax", max_age=3600)
    response.headers["X-Auth-Token"] = token
    return {"status": "logged in"}
```

### 4. Raw Request Object
```python
from fastapi import Request

@app.get("/info")
async def info(request: Request):
    return {
        "method":  request.method,
        "url":     str(request.url),
        "headers": dict(request.headers),
        "client":  request.client.host,
        "path_params": request.path_params,
        "query_params": dict(request.query_params),
    }
```

---

Build a middleware-free rate limiter using client IP from `request.client.host`, stored in Redis, enforced via a dependency injection.

---

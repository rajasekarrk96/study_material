# Scope-Based Fine-Grained Authorization

> **Course**: Fastapi | **Module**: Database Integration | **Difficulty**: advanced

---

### 1. JWT with Scopes
```python
SCOPES = {
    "items:read": "Read items",
    "items:write": "Create/update items",
    "users:admin": "Manage users",
}

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes=SCOPES
)
```

### 2. Scope Validation Dependency
```python
from fastapi.security import SecurityScopes

async def get_current_user(
    security_scopes: SecurityScopes,
    token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": f'Bearer scope="{security_scopes.scope_str}"'},
    )
    payload = decode_jwt(token)
    token_scopes = payload.get("scopes", [])
    for scope in security_scopes.scopes:
        if scope not in token_scopes:
            raise HTTPException(403, f"Missing scope: {scope}")
    return payload
```

### 3. Protecting Routes with Scopes
```python
from fastapi import Security

@app.get("/items", dependencies=[Security(get_current_user, scopes=["items:read"])])
async def list_items():
    ...

@app.post("/items", dependencies=[Security(get_current_user, scopes=["items:write"])])
async def create_item(item: ItemIn):
    ...
```

---

Build a multi-tenant API where admins get all scopes, editors get write, viewers get read. Return 403 with `missing_scope` detail when unauthorized.

---

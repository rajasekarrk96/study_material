---
id: "23"
title: "Multi-Source Parameter Declarations"
course: "FastAPI"
module: 3
module_title: "Advanced Features"
lesson: 23
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["Path", "Query", "Body", "Header", "Cookie", "multiple-params", "mixed", "Annotated", "Field"]
prerequisites: []
lab_required: true
---

## Topics Covered

### 1. Mixing Path, Query, Body
```python
from fastapi import Path, Query, Body

@app.put("/users/{user_id}/items/{item_id}")
async def update_item(
    user_id: Annotated[int, Path(title="User ID", ge=1)],
    item_id: Annotated[int, Path(ge=1)],
    q: Annotated[str | None, Query(max_length=50)] = None,
    item: Item | None = None,
    importance: Annotated[int, Body(ge=1, le=5)] = 1,
):
    return {"user_id": user_id, "item_id": item_id, "q": q, "importance": importance}
```

### 2. Multiple Body Parameters
```python
@app.post("/composite")
async def composite(
    user: User,
    item: Item,
    note: Annotated[str, Body(embed=True)] = ""
):
    # JSON body: {"user": {...}, "item": {...}, "note": "..."}
    ...
```

### 3. Body with `embed=True`
```python
@app.post("/single-embed")
async def single(
    item: Annotated[Item, Body(embed=True)]
    # JSON: {"item": {"name": "..."}} instead of {"name": "..."}
):
    ...
```

### 4. Header and Cookie
```python
from fastapi import Header, Cookie

@app.get("/headers")
async def read_headers(
    x_token: Annotated[str, Header()],   # X-Token header
    user_agent: Annotated[str | None, Header()] = None,
    session: Annotated[str | None, Cookie()] = None,
):
    return {"token": x_token, "ua": user_agent, "session": session}
```

## Lab
Create an API endpoint that accepts: path ID, query filter, JSON body, auth header, and session cookie — all in one function with proper validation.

---
id: "22"
title: "Query Parameters and Validation"
course: "FastAPI"
module: 3
module_title: "Advanced Features"
lesson: 22
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["Query", "optional", "required", "alias", "title", "description", "min-length", "max-length", "regex", "ge", "le"]
prerequisites: []
lab_required: true
---

## Topics Covered

### 1. Basic Query Parameters
```python
@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10, q: str | None = None):
    return {"skip": skip, "limit": limit, "q": q}
```

### 2. Annotated with Query()
```python
from fastapi import Query
from typing import Annotated

@app.get("/search")
async def search(
    q: Annotated[str, Query(
        min_length=3,
        max_length=50,
        title="Search Query",
        description="Search string, 3-50 chars",
        alias="search",            # URL uses ?search=
        example="python fastapi",
    )],
    page: Annotated[int, Query(ge=1, le=1000)] = 1,
    size: Annotated[int, Query(ge=5, le=100)] = 20,
):
    ...
```

### 3. List Query Parameters
```python
@app.get("/filter")
async def filter_items(
    tags: Annotated[list[str], Query()] = []
):
    # /filter?tags=a&tags=b&tags=c
    return {"tags": tags}
```

### 4. Regex Validation
```python
from fastapi import Query
@app.get("/validate")
async def validate(
    code: Annotated[str, Query(pattern=r"^[A-Z]{3}-\d{3}$")]
):
    return {"code": code}
```

## Lab
Build a product search endpoint with: keyword (min 2 chars), category list, price range (ge/le), sort field (enum), page/size pagination — all validated with `Query()`.

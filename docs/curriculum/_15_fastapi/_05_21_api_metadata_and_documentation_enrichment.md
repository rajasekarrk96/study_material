---
id: "21"
title: "API Metadata and Documentation Enrichment"
course: "FastAPI"
module: 3
module_title: "Advanced Features"
lesson: 21
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["openapi", "tags", "summary", "description", "response-description", "deprecated", "metadata", "redoc", "swagger-ui"]
prerequisites: []
lab_required: true
---

## Topics Covered

### 1. App-Level Metadata
```python
app = FastAPI(
    title="My API",
    description="# My API\n\nFull **markdown** description.",
    version="2.1.0",
    terms_of_service="https://example.com/terms",
    contact={"name": "Dev Team", "email": "api@example.com"},
    license_info={"name": "MIT"},
    openapi_tags=[
        {"name": "users", "description": "Operations with users"},
        {"name": "items", "description": "Manage items"},
    ]
)
```

### 2. Route-Level Metadata
```python
@app.get(
    "/users/{id}",
    tags=["users"],
    summary="Get a user by ID",
    description="Returns full user details. Requires auth.",
    response_description="The user object",
    responses={
        404: {"description": "User not found"},
        200: {"content": {"application/json": {"example": {"id": 1, "name": "Raja"}}}},
    },
    deprecated=False,
    operation_id="get_user_by_id",
)
async def get_user(id: int):
    ...
```

### 3. Hiding Routes from Docs
```python
@app.get("/internal", include_in_schema=False)
async def internal():
    ...
```

### 4. Customising Docs URLs
```python
app = FastAPI(docs_url="/swagger", redoc_url="/docs", openapi_url="/openapi.json")
```

## Lab
Build an API with rich metadata for three resources, custom tag descriptions, example responses, and disable the default `/docs` URL, replacing it with `/api/docs`.

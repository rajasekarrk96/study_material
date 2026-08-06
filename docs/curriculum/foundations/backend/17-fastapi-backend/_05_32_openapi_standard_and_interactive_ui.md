---
id: "32"
title: "OpenAPI Standard and Interactive UI"
course: "FastAPI"
module: 3
module_title: "Advanced Features"
lesson: 32
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["openapi", "swagger-ui", "redoc", "schema", "examples", "openapi-extra", "custom-openapi", "openapi-json"]
prerequisites: []
lab_required: true
---

## Topics Covered

### 1. Auto-Generated OpenAPI Schema
```python
# Access at:
# /openapi.json  — raw JSON schema
# /docs          — Swagger UI
# /redoc         — ReDoc UI
```

### 2. Request/Response Examples
```python
class Item(BaseModel):
    name: str
    price: float

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"name": "Widget", "price": 9.99}]
        }
    )
```

### 3. Field-Level Examples
```python
from pydantic import Field

class Product(BaseModel):
    name: str = Field(..., examples=["Laptop", "Phone"])
    price: float = Field(..., ge=0, examples=[999.99])
```

### 4. Custom OpenAPI Function
```python
from fastapi.openapi.utils import get_openapi

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    schema = get_openapi(
        title="Custom API",
        version="3.0.0",
        description="Custom docs",
        routes=app.routes,
    )
    schema["info"]["x-logo"] = {"url": "https://example.com/logo.png"}
    app.openapi_schema = schema
    return schema

app.openapi = custom_openapi
```

## Lab
Add rich examples to a 3-resource API, configure a custom OpenAPI schema with logo and contact info, hide internal endpoints from the schema, and serve custom Swagger UI with a CDN.

---
id: "26"
title: "Response Models and Status Codes"
course: "FastAPI"
module: 3
module_title: "Advanced Features"
lesson: 26
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["response_model", "status_code", "exclude_unset", "response_model_include", "response_model_exclude", "JSONResponse", "201", "422", "404"]
prerequisites: []
lab_required: true
---

## Topics Covered

### 1. Response Model
```python
class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

@app.post("/users", response_model=UserOut, status_code=201)
async def create_user(user: UserIn):
    db_user = User(username=user.username, hashed=hash(user.password))
    db.add(db_user); db.commit(); db.refresh(db_user)
    return db_user  # password field auto-stripped
```

### 2. Partial Response Filtering
```python
@app.get("/items/{id}", response_model=Item,
         response_model_include={"name", "price"},
         response_model_exclude_unset=True)
async def get_item(id: int):
    ...
```

### 3. Multiple Response Types
```python
from typing import Union

@app.get("/items/{id}", response_model=Union[ItemFull, ItemBasic])
async def get_item(id: int, full: bool = False):
    item = get_from_db(id)
    return item if full else ItemBasic(**item.dict())
```

### 4. Common Status Codes
```python
from fastapi import status

@app.delete("/items/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(id: int):
    delete_from_db(id)
    # Returns no body
```

## Lab
Design a User API with separate request/response models (hide password), 201 on create, 404 on not found, 204 on delete — all documented in OpenAPI.

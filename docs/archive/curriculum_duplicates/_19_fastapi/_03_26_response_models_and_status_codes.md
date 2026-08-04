# Response Models and Status Codes

> **Course**: Fastapi | **Module**: Advanced Features | **Difficulty**: intermediate

---

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

---

Design a User API with separate request/response models (hide password), 201 on create, 404 on not found, 204 on delete — all documented in OpenAPI.

---

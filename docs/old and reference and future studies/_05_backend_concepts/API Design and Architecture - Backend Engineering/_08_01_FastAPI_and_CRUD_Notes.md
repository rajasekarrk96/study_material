# Module 3: FastAPI, CRUD, REST APIs
## Topic 8: FastAPI & CRUD Operations

---

### 1. The Big Picture

#### What is CRUD?
**CRUD** stands for **Create, Read, Update, and Delete**. These are the four basic functions of persistent storage. In web development, we map these database operations to HTTP methods:

```
┌──────────────────┬─────────────────┬─────────────────────────────────────┐
│ Operation        │ HTTP Method     │ REST Path Example                   │
├──────────────────┼─────────────────┼─────────────────────────────────────┤
│ **Create**       │ `POST`          │ `POST /api/v1/items`                │
│ **Read (List)**  │ `GET`           │ `GET /api/v1/items`                 │
│ **Read (Single)**│ `GET`           │ `GET /api/v1/items/{id}`            │
│ **Update (Full)**│ `PUT`           │ `PUT /api/v1/items/{id}`            │
│ **Update (Part)**│ `PATCH`         │ `PATCH /api/v1/items/{id}`          │
│ **Delete**       │ `DELETE`        │ `DELETE /api/v1/items/{id}`         │
└──────────────────┴─────────────────┴─────────────────────────────────────┘
```

---

### 2. Pydantic for Validation and Serialization
In FastAPI, we use **Pydantic** to define the data structures (schemas) for requests and responses.
* **Input Validation:** Pydantic automatically checks types, string lengths, ranges, and patterns. If the client sends an invalid payload, FastAPI returns a `422 Unprocessable Entity` immediately.
* **Serialization:** Pydantic filters and converts Python objects (including database ORM models) into JSON format.

---

### 3. Implementing CRUD in FastAPI

Here is how we design a clean, production-ready CRUD controller for an e-commerce **Category** resource.

#### 1. The Schemas (`schemas.py`)
```python
from pydantic import BaseModel, Field
from typing import Optional

class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, example="Electronics")
    description: Optional[str] = Field(None, max_length=200, example="Gadgets and devices")

class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    description: Optional[str] = Field(None, max_length=200)

class CategoryResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
```

#### 2. The Router (`router.py`)
```python
from fastapi import APIRouter, status, HTTPException
from typing import List
from schemas import CategoryCreate, CategoryUpdate, CategoryResponse

router = APIRouter(prefix="/api/v1/categories", tags=["Categories"])

CATEGORIES_DB = []
current_id = 1

# CREATE
@router.post("", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category_in: CategoryCreate):
    global current_id
    new_category = {
        "id": current_id,
        "name": category_in.name,
        "description": category_in.description
    }
    CATEGORIES_DB.append(new_category)
    current_id += 1
    return new_category

# READ (List)
@router.get("", response_model=List[CategoryResponse])
def list_categories():
    return CATEGORIES_DB

# READ (Single)
@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int):
    for cat in CATEGORIES_DB:
        if cat["id"] == category_id:
            return cat
    raise HTTPException(status_code=404, detail="Category not found")

# UPDATE (Full - PUT)
@router.put("/{category_id}", response_model=CategoryResponse)
def update_category_full(category_id: int, category_in: CategoryCreate):
    for cat in CATEGORIES_DB:
        if cat["id"] == category_id:
            cat["name"] = category_in.name
            cat["description"] = category_in.description
            return cat
    raise HTTPException(status_code=404, detail="Category not found")

# UPDATE (Partial - PATCH)
@router.patch("/{category_id}", response_model=CategoryResponse)
def update_category_partial(category_id: int, category_in: CategoryUpdate):
    for cat in CATEGORIES_DB:
        if cat["id"] == category_id:
            # Only update fields that were explicitly sent in the request
            update_data = category_in.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                cat[key] = value
            return cat
    raise HTTPException(status_code=404, detail="Category not found")

# DELETE
@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int):
    global CATEGORIES_DB
    for cat in CATEGORIES_DB:
        if cat["id"] == category_id:
            CATEGORIES_DB.remove(cat)
            return
    raise HTTPException(status_code=404, detail="Category not found")
```

---

### 4. Professional Notes: PUT vs PATCH
This is a classic senior-level distinction:
* **`PUT` (Complete Replacement):** The client must send the *entire* representation of the resource. If the client sends `{"name": "New Name"}` but omits `description`, the server will set `description` to `None` or its default value.
* **`PATCH` (Partial Update):** The client only sends the fields they want to change. If the client sends `{"name": "New Name"}`, the server *only* updates the name, leaving the existing `description` completely unchanged. 
* **Best Practice:** Use `exclude_unset=True` in Pydantic's `model_dump()` when processing PATCH requests so you don't accidentally overwrite fields with their default values.

---

### 5. Hands-on Workout & Assessment

#### Part A: API Design Challenge (PATCH Design)
Suppose a user wants to update their profile. The profile has `username`, `email`, `bio`, and `avatar_url`.
- Write down the Pydantic schema for the `PATCH` request (`UserProfileUpdate`). 
- How do you ensure fields are optional, but if they *are* provided, they are validated (e.g., email must be a valid email)?

#### Part B: Quiz
1. Which HTTP method maps to the "Delete" operation in CRUD?
   A. POST
   B. PUT
   C. DELETE
   D. GET
2. What does `exclude_unset=True` do when dumping a Pydantic model?
   A. It removes all fields that are set to None.
   B. It only includes fields that were explicitly passed in the request payload, ignoring defaults.
   C. It excludes fields that are not defined in the database.
   D. It encrypts the output.
3. If a client wants to change just the price of a product, which method is most appropriate?
   A. GET
   B. PUT
   C. PATCH
   D. POST

---

### 6. Progress Tracker

* **Module 3: FastAPI, CRUD, REST APIs:** 0%
* **Topics Completed:** 0/1
* **Coding Exercises:** 0/0
* **Quiz Score:** N/A
* **API Design Challenge Score:** N/A
* **Backend Score:** 0 / 100

---

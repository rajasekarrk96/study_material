# %% [markdown]
# # Topic 8: FastAPI & CRUD Operations Playground
# In this playground, you will interact with a complete CRUD API for a **Category** resource.
# You will observe the difference between a PUT (full replacement) and a PATCH (partial update).
#
# **How to use this:**
# 1. Open this file in VS Code.
# 2. Click **"Run Cell"** above each code block.

# %%
# 1. IMPORT LIBRARIES
from fastapi import FastAPI, status, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field
from typing import List, Optional
import json

# %%
# 2. SCHEMAS
class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    description: Optional[str] = Field(None, max_length=200)

class CategoryUpdate(BaseModel):
    # For PATCH, all fields are optional because the client might send only one of them
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    description: Optional[str] = Field(None, max_length=200)

class CategoryResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]

# %%
# 3. APPLICATION SETUP
app = FastAPI(title="Category CRUD Service")

CATEGORIES_DB = []
current_id = 1

# %%
# 4. ROUTE DEFINITIONS

@app.post("/api/v1/categories", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
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

@app.get("/api/v1/categories", response_model=List[CategoryResponse])
def list_categories():
    return CATEGORIES_DB

@app.get("/api/v1/categories/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int):
    for cat in CATEGORIES_DB:
        if cat["id"] == category_id:
            return cat
    raise HTTPException(status_code=404, detail="Category not found")

@app.put("/api/v1/categories/{category_id}", response_model=CategoryResponse)
def update_category_full(category_id: int, category_in: CategoryCreate):
    for cat in CATEGORIES_DB:
        if cat["id"] == category_id:
            # PUT replaces the entire resource.
            cat["name"] = category_in.name
            cat["description"] = category_in.description
            return cat
    raise HTTPException(status_code=404, detail="Category not found")

@app.patch("/api/v1/categories/{category_id}", response_model=CategoryResponse)
def update_category_partial(category_id: int, category_in: CategoryUpdate):
    for cat in CATEGORIES_DB:
        if cat["id"] == category_id:
            # We dump the model excluding fields that weren't explicitly passed
            update_data = category_in.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                cat[key] = value
            return cat
    raise HTTPException(status_code=404, detail="Category not found")

@app.delete("/api/v1/categories/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int):
    global CATEGORIES_DB
    for cat in CATEGORIES_DB:
        if cat["id"] == category_id:
            CATEGORIES_DB.remove(cat)
            return
    raise HTTPException(status_code=404, detail="Category not found")

# %%
# 5. INITIALIZE TEST CLIENT
client = TestClient(app)

# %% [markdown]
# ### Step 1: Create a Category
# We create a category "Electronics" with a description.

# %%
create_payload = {"name": "Electronics", "description": "Laptops, phones, and accessories"}
response = client.post("/api/v1/categories", json=create_payload)
print(f"POST Status: {response.status_code}")
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ### Step 2: PUT (Full Update)
# We want to rename it to "Computers". Since we are using PUT, we MUST send the entire payload.
# If we do not send the `description` field, it will be set to `null` (None) because PUT replaces the entire object.

# %%
put_payload = {"name": "Computers"} # We omitted the description!
response = client.put("/api/v1/categories/1", json=put_payload)
# Pydantic will fail because CategoryCreate requires name and description (with default None).
# Let's see how FastAPI automatically rejects this because CategoryCreate requires 'name'.
# Wait, let's send a valid PUT payload but without description, to see it set to null.
put_payload_valid = {"name": "Computers", "description": None}
response = client.put("/api/v1/categories/1", json=put_payload_valid)
print(f"PUT Status: {response.status_code}")
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ### Step 3: PATCH (Partial Update)
# Now we want to update ONLY the description, leaving the name ("Computers") untouched.
# We send only the description field.

# %%
patch_payload = {"description": "Supercomputers and laptops"}
response = client.patch("/api/v1/categories/1", json=patch_payload)
print(f"PATCH Status: {response.status_code}")
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ### Step 4: DELETE the Category
# We delete the category. It should return `204 No Content`.

# %%
response = client.delete("/api/v1/categories/1")
print(f"DELETE Status: {response.status_code} (Should be 204)")

# %% [markdown]
# ### Step 5: Verify Deletion
# Trying to GET the category now should return `404 Not Found`.

# %%
response = client.get("/api/v1/categories/1")
print(f"GET Status: {response.status_code} (Should be 404)")
print(json.dumps(response.json(), indent=2))

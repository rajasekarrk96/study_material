# %% [markdown]
# # Topic 2: REST API Design & Constraints Playground
# In this playground, you will learn how RESTful routing works in FastAPI.
# We will compare Path Parameters (identifying a resource) and Query Parameters (filtering/sorting).
#
# **How to use this:**
# 1. Open this file in VS Code.
# 2. Click **"Run Cell"** above each code block.

# %%
# 1. IMPORT LIBRARIES
from fastapi import FastAPI, status, HTTPException, Query
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field
from typing import List, Optional
import json

# %%
# 2. SCHEMAS
class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    price: float = Field(..., gt=0)
    category: str = Field(..., min_length=2)

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    category: str

# %%
# 3. APPLICATION SETUP
app = FastAPI(title="E-Commerce Product Service")

PRODUCTS_DB = [
    {"id": 1, "name": "Wireless Mouse", "price": 29.99, "category": "Electronics"},
    {"id": 2, "name": "Mechanical Keyboard", "price": 89.99, "category": "Electronics"},
    {"id": 3, "name": "Running Shoes", "price": 120.00, "category": "Footwear"},
    {"id": 4, "name": "Coffee Mug", "price": 14.99, "category": "Kitchen"}
]
current_id = 5

# %% [markdown]
# ## RESTful Endpoints
#
# Note the patterns:
# 1. `GET /api/v1/products` (returns list, supports filters)
# 2. `GET /api/v1/products/{product_id}` (returns one item using path parameter)
# 3. `POST /api/v1/products` (creates one item, returns 201 Created)
# 4. `DELETE /api/v1/products/{product_id}` (deletes one item, returns 204 No Content)

# %%
# 4. ROUTE DEFINITIONS

@app.get("/api/v1/products", response_model=List[ProductResponse])
def list_products(
    category: Optional[str] = Query(None, description="Filter by category"),
    max_price: Optional[float] = Query(None, gt=0, description="Filter by maximum price")
):
    results = PRODUCTS_DB
    if category:
        results = [p for p in results if p["category"].lower() == category.lower()]
    if max_price:
        results = [p for p in results if p["price"] <= max_price]
    return results

@app.get("/api/v1/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):
    for p in PRODUCTS_DB:
        if p["id"] == product_id:
            return p
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with ID {product_id} not found"
    )

@app.post("/api/v1/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product_in: ProductCreate):
    global current_id
    new_product = {
        "id": current_id,
        "name": product_in.name,
        "price": product_in.price,
        "category": product_in.category
    }
    PRODUCTS_DB.append(new_product)
    current_id += 1
    return new_product

@app.delete("/api/v1/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    global PRODUCTS_DB
    for p in PRODUCTS_DB:
        if p["id"] == product_id:
            PRODUCTS_DB.remove(p)
            return  # HTTP 204 has no body response
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with ID {product_id} not found"
    )

# %%
# 5. INITIALIZE TEST CLIENT
client = TestClient(app)

# %% [markdown]
# ### Test 1: Get All Products (No Filters)
# Verify we get 4 items with a `200 OK` status code.

# %%
response = client.get("/api/v1/products")
print(f"Status Code: {response.status_code}")
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ### Test 2: Filter by Category (Query Parameter)
# Let's filter for "Electronics". We should only get the mouse and keyboard.

# %%
response = client.get("/api/v1/products?category=electronics")
print(f"Status Code: {response.status_code}")
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ### Test 3: Get Single Product (Path Parameter)
# Let's fetch the product with ID 3 (Running Shoes).

# %%
response = client.get("/api/v1/products/3")
print(f"Status Code: {response.status_code}")
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ### Test 4: Get Non-existent Product
# Let's try to get ID 99. It should return a `404 Not Found`.

# %%
response = client.get("/api/v1/products/99")
print(f"Status Code: {response.status_code}")
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ### Test 5: Delete a Product
# Let's delete the Wireless Mouse (ID 1). It should return `204 No Content`.

# %%
response = client.delete("/api/v1/products/1")
print(f"Status Code: {response.status_code} (Should be 204)")
print(f"Response Content: '{response.content.decode()}' (Should be empty)")

# %% [markdown]
# ### Test 6: Verify Deletion
# Let's try to fetch ID 1 again. It should return `404 Not Found`.

# %%
response = client.get("/api/v1/products/1")
print(f"Status Code: {response.status_code} (Should be 404)")
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# # Topic 10: Pagination Strategies Playground
# In this playground, you will compare **Limit-Offset** and **Cursor-based** pagination.
# We will simulate a database of 100 items and implement both endpoints.
# You will see how cursors are encoded in base64 and used to fetch subsequent pages.
#
# **How to use this:**
# 1. Open this file in VS Code.
# 2. Click **"Run Cell"** above each code block.

# %%
# 1. IMPORT LIBRARIES
import base64
import json
from fastapi import FastAPI, Query, status, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel
from typing import List, Optional

# %%
# 2. APPLICATION SETUP
app = FastAPI(title="Pagination Service")

# Let's generate 100 mock products
PRODUCTS_DB = [{"id": i, "name": f"Product {i}", "price": round(10.0 + i * 1.5, 2)} for i in range(1, 101)]

# %% [markdown]
# ## 1. Limit-Offset Pagination
# Simple and easy. We slice the array using `[offset : offset + limit]`.

# %%
# 3. LIMIT-OFFSET ROUTE

class OffsetPaginationResponse(BaseModel):
    total_items: int
    limit: int
    offset: int
    results: List[dict]

@app.get("/api/v1/products/offset", response_model=OffsetPaginationResponse)
def get_products_offset(
    limit: int = Query(10, ge=1, le=50),
    offset: int = Query(0, ge=0)
):
    sliced = PRODUCTS_DB[offset : offset + limit]
    return {
        "total_items": len(PRODUCTS_DB),
        "limit": limit,
        "offset": offset,
        "results": sliced
    }

# %% [markdown]
# ## 2. Cursor-based Pagination
# For cursor pagination, the cursor is a base64 encoded string containing the last item's ID.
# E.g., if the last item in the page has ID 10, the cursor is `eyJpZCI6IDEwfQ==` (decoded: `{"id": 10}`).
# The next request fetches items where `id > 10`.

# %%
# 4. CURSOR ROUTE

class CursorPaginationResponse(BaseModel):
    next_cursor: Optional[str]
    has_more: bool
    results: List[dict]

def encode_cursor(last_id: int) -> str:
    """Helper to base64 encode the last item's ID."""
    cursor_data = json.dumps({"id": last_id})
    return base64.urlsafe_b64encode(cursor_data.encode()).decode()

def decode_cursor(cursor_str: str) -> int:
    """Helper to decode base64 cursor back to the last item's ID."""
    try:
        decoded_bytes = base64.urlsafe_b64decode(cursor_str.encode())
        cursor_data = json.loads(decoded_bytes.decode())
        return int(cursor_data["id"])
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid cursor format")

@app.get("/api/v1/products/cursor", response_model=CursorPaginationResponse)
def get_products_cursor(
    limit: int = Query(10, ge=1, le=50),
    cursor: Optional[str] = Query(None, description="Base64 encoded cursor")
):
    # 1. Determine starting point
    start_id = 0
    if cursor:
        start_id = decode_cursor(cursor)
        
    # 2. Query database: Fetch items with ID > start_id
    # (In SQL: SELECT * FROM products WHERE id > start_id ORDER BY id LIMIT limit)
    results = [p for p in PRODUCTS_DB if p["id"] > start_id]
    
    # Slice the results to our limit
    paginated_results = results[:limit]
    
    # 3. Determine if there are more items and build the next cursor
    has_more = len(results) > limit
    next_cursor = None
    if paginated_results and has_more:
        last_item_id = paginated_results[-1]["id"]
        next_cursor = encode_cursor(last_item_id)
        
    return {
        "next_cursor": next_cursor,
        "has_more": has_more,
        "results": paginated_results
    }

# %%
# 5. INITIALIZE TEST CLIENT
client = TestClient(app)

# %% [markdown]
# ### Test 1: Testing Limit-Offset Pagination
# Let's fetch page 2 (items 11 to 20) by setting `limit=10` and `offset=10`.

# %%
response = client.get("/api/v1/products/offset?limit=10&offset=10")
print("--- Offset Pagination Results ---")
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ### Test 2: Testing Cursor Pagination (Page 1)
# We fetch page 1 (no cursor sent). We expect 10 items and a `next_cursor` in the response.

# %%
response = client.get("/api/v1/products/cursor?limit=10")
page_1_data = response.json()

print("--- Cursor Page 1 Results ---")
print(f"Next Cursor: {page_1_data['next_cursor']}")
print(f"Has More: {page_1_data['has_more']}")
print("Last item in page 1:", page_1_data["results"][-1])

# %% [markdown]
# ### Test 3: Testing Cursor Pagination (Page 2)
# We use the `next_cursor` returned from Page 1 to fetch Page 2.
# Notice that the first item in Page 2 starts exactly after the last item of Page 1.

# %%
next_cursor = page_1_data["next_cursor"]
response = client.get(f"/api/v1/products/cursor?limit=10&cursor={next_cursor}")
page_2_data = response.json()

print("--- Cursor Page 2 Results ---")
print(f"Next Cursor: {page_2_data['next_cursor']}")
print(f"Has More: {page_2_data['has_more']}")
print("First item in page 2:", page_2_data["results"][0])
print("Last item in page 2:", page_2_data["results"][-1])

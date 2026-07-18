# Module 4: Pagination
## Topic 10: Pagination Strategies (Offset vs. Cursor)

---

### 1. The Big Picture

#### What is Pagination?
**Pagination** is the process of splitting a large dataset into smaller, discrete chunks (pages) before returning it to the client. 

#### Why Companies Use Pagination
If your database contains 10,000,000 products, returning all of them in a single `GET /products` call will:
1. Crash the database (out of memory).
2. Consume gigabytes of network bandwidth.
3. Crash the client's browser/app trying to render it.
Pagination is a **mandatory** performance and security requirement for any list endpoint.

---

### 2. Pagination Strategies

#### A. Limit-Offset Pagination
The client specifies how many records they want (`limit`) and how many records to skip (`offset`).
* **Example URL:** `/api/v1/products?limit=20&offset=40`
* **SQL Query:** `SELECT * FROM products ORDER BY id LIMIT 20 OFFSET 40;`

##### Tradeoffs:
* **Advantages:** Very easy to implement. Allows clients to jump directly to any page (e.g., "Go to page 50").
* **Disadvantages (Scale Killer):** As the offset increases, the database becomes extremely slow. To execute `OFFSET 1000000`, the database must scan and discard 1,000,000 rows before returning the 20 requested rows.
* **Disadvantages (Inconsistency):** If a new item is inserted on page 1 while a user is reading page 2, all items shift down, and the user will see a duplicate item on the next page.

#### B. Cursor Pagination (Keyset Pagination)
Instead of skipping rows, the client is given a pointer (a **cursor**, usually a base64 encoded value of the last item's ID or timestamp). The client requests items *after* this cursor.
* **Example URL:** `/api/v1/products?limit=20&cursor=eyJpZCI6NDJ9` (Decoded: `{"id": 42}`)
* **SQL Query:** `SELECT * FROM products WHERE id > 42 ORDER BY id LIMIT 20;`

##### Tradeoffs:
* **Advantages:** Highly performant. Even at page 10,000, the database uses an index to jump directly to ID 42 and reads 20 rows. Execution time is $O(1)$ instead of $O(N)$. There are no duplicate or skipped items if data changes.
* **Disadvantages:** Clients cannot jump to a specific page (e.g., "Page 5"). They can only navigate sequentially (Next/Previous). Excellent for **Infinite Scroll** (like Twitter, Instagram, or Slack).

---

### 3. Response Structure for Pagination
In production, never return a raw list for paginated endpoints. Always wrap the list in a metadata envelope:

#### Limit-Offset Envelope
```json
{
  "total_items": 1205,
  "limit": 20,
  "offset": 40,
  "results": [...]
}
```

#### Cursor Envelope
```json
{
  "next_cursor": "eyJpZCI6NjJ9",
  "has_more": true,
  "results": [...]
}
```

---

### 4. Python Example: Implementing Limit-Offset in FastAPI

```python
from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/api/v1/products")

class ProductListResponse(BaseModel):
    total_items: int
    limit: int
    offset: int
    results: List[dict]

PRODUCTS_DB = [{"id": i, "name": f"Product {i}"} for i in range(1, 101)]

@router.get("", response_model=ProductListResponse)
def list_products(
    limit: int = Query(20, ge=1, le=100, description="Number of items to return"),
    offset: int = Query(0, ge=0, description="Number of items to skip")
):
    total = len(PRODUCTS_DB)
    paginated_results = PRODUCTS_DB[offset : offset + limit]
    
    return {
        "total_items": total,
        "limit": limit,
        "offset": offset,
        "results": paginated_results
    }
```

---

### 5. Hands-on Workout & Assessment

#### Part A: API Design Challenge (Cursor vs Offset)
You are building an API for a **Chat Application** (like Discord/Slack) where users scroll up to load historical messages.
- Which pagination strategy would you choose? Why?
- Explain the user experience issue that would occur if you used Limit-Offset pagination when new messages are actively arriving.

#### Part B: Quiz
1. Why does Limit-Offset pagination become slow for large datasets?
   A. The network cannot carry offset parameters quickly.
   B. The database must read and discard all rows up to the offset before returning the results.
   C. Python cannot process offsets larger than 1000.
   D. It disables database indexes.
2. Which pagination strategy is ideal for implementing an infinite scroll UI?
   A. Limit-Offset Pagination
   B. Page-based Pagination
   C. Cursor Pagination
   D. No Pagination
3. What is a cursor in cursor-based pagination?
   A. A database connection pointer.
   B. An encoded value pointing to the unique identifier of the last item returned in the previous page.
   C. A mouse pointer coordinate.
   D. An SQL keyword.

---

### 6. Progress Tracker

* **Module 4: Pagination:** 0%
* **Topics Completed:** 0/1
* **Coding Exercises:** 0/0
* **Quiz Score:** N/A
* **API Design Challenge Score:** N/A
* **Backend Score:** 0 / 100

---

# Module 8: Performance
## Topic 16: Caching with Redis & Rate Limiting

---

### 1. Caching with Redis

#### What is Caching?
**Caching** is the process of storing copies of data in a high-speed, temporary storage layer (the cache) so that future requests for that data can be served faster.

#### What is Redis?
**Redis (Remote Dictionary Server)** is an open-source, in-memory, key-value data store. It is extremely fast (sub-millisecond latency) because it keeps all data in RAM rather than writing to disk.

#### Caching Strategies: Cache-Aside (Lazy Loading)
This is the most common caching pattern:
1. The application receives a request for data.
2. The application checks the cache (Redis).
   * **Cache Hit:** If data is found, return it immediately.
   * **Cache Miss:** If data is not found, query the database (PostgreSQL), store a copy of the data in the cache with an expiration time (**TTL - Time To Live**), and return the data.

```
                  ┌────────────────────────┐
                  │      1. Request        │
                  │        Client          │
                  └──────────┬─────────────┘
                             │
                             ▼
                  ┌────────────────────────┐
                  │    2. Check Cache      │  Cache Hit (Return Data)
                  │        (Redis)         ├────────────────────────┐
                  └──────────┬─────────────┘                        │
                             │ Cache Miss                           │
                             ▼                                      ▼
                  ┌────────────────────────┐              ┌──────────────────┐
                  │    3. Query Database   │              │   4. Response    │
                  │      (PostgreSQL)      │              │      Client      │
                  └──────────┬─────────────┘              └──────────────────┘
                             │                                      ▲
                             ▼                                      │
                  ┌────────────────────────┐                        │
                  │   5. Write to Cache    ├────────────────────────┘
                  │       with TTL         │
                  └────────────────────────┘
```

#### Cache Invalidation (The Hardest Part)
If the database updates a product's price, the cache now contains stale data. We must invalidate (delete) the cached item:
* **Active Invalidation:** When a product is updated via `PUT /products/1`, the code must explicitly delete the key `product:1` from Redis.
* **TTL-based Invalidation:** Always set a TTL (e.g., 1 hour) so that even if active invalidation fails, the cache will automatically refresh after the TTL expires.

---

### 2. Rate Limiting
**Rate Limiting** is a strategy to limit network traffic. It puts a cap on how often a client can repeat an action within a certain timeframe (e.g., "100 requests per minute").
* **Why?** It protects your API from brute-force login attacks, scraping, and Denial of Service (DoS) attacks.
* **Implementation:** Redis is ideal for rate limiting because of its fast atomic increment operations (`INCR`). We increment a counter for the client's IP address and set it to expire after 1 minute.

---

### 3. Python Example: Cache-Aside with Redis in FastAPI

```python
import json
from fastapi import APIRouter, Depends
import redis

router = APIRouter()

# Connect to Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

@router.get("/api/v1/products/{product_id}")
def get_product(product_id: int):
    cache_key = f"product:{product_id}"
    
    # 1. Check Redis Cache
    cached_product = redis_client.get(cache_key)
    if cached_product:
        print("--- Cache Hit! ---")
        return json.loads(cached_product)
        
    # 2. Cache Miss: Query Database (Mock query here)
    print("--- Cache Miss! Querying DB... ---")
    product = {"id": product_id, "name": f"Product {product_id}", "price": 99.99}
    
    # 3. Save to Redis with a 5-minute TTL (300 seconds)
    redis_client.setex(cache_key, 300, json.dumps(product))
    
    return product
```

---

### 4. Hands-on Workout & Assessment

#### Part A: API Design Challenge (Cache Invalidation)
You are caching the **Product Catalog** list endpoint `GET /products` under the Redis key `products:all`.
- When a new product is created via `POST /products`, or an existing product is deleted via `DELETE /products/12`, what must your code do to the Redis cache to prevent clients from seeing stale data?
- Explain the difference between deleting the cache key (Write-Through/Cache-Aside) versus updating the cached list directly.

#### Part B: Quiz
1. Why is Redis faster than PostgreSQL for caching?
   A. Redis uses a more secure encryption.
   B. Redis stores data entirely in-memory (RAM), while PostgreSQL writes to disk.
   C. Redis is written in Python.
   D. Redis does not support tables.
2. What does TTL stand for in caching?
   A. Total Transfer Limit
   B. Time To Live
   C. Transaction Transition Lock
   D. Table Type Link
3. Which Redis command is commonly used to implement a rate limiter counter?
   A. `SET`
   B. `INCR`
   C. `DECR`
   D. `GET`

---

### 5. Progress Tracker

* **Module 8: Performance:** 0%
* **Topics Completed:** 0/1
* **Coding Exercises:** 0/0
* **Quiz Score:** N/A
* **API Design Challenge Score:** N/A
* **Backend Score:** 0 / 100

---

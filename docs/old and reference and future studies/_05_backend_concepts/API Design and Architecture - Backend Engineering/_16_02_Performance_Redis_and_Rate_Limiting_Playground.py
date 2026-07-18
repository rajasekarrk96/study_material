# %% [markdown]
# # Topic 16: Caching (Redis) & Rate Limiting Playground
# In this playground, you will learn how to optimize API performance.
# We will use `fakeredis`, which mimics a real Redis server in-memory, so you don't need
# to install or run a local Redis server.
#
# We will cover:
# 1. **Cache-Aside Pattern:** Speeding up slow database queries.
# 2. **IP-based Rate Limiter:** Restricting requests to 3 requests per 10 seconds.
#
# **How to use this:**
# 1. Open this file in VS Code.
# 2. Click **"Run Cell"** above each code block.

# %%
# 1. INSTALL DEPENDENCIES
# We install fakeredis to simulate a Redis server, and httpx/fastapi.
%pip install fakeredis fastapi

# %%
# 2. IMPORT LIBRARIES
import time
import json
import fakeredis
from fastapi import FastAPI, status, HTTPException, Request
from fastapi.testclient import TestClient

# %%
# 3. APPLICATION & REDIS SETUP
app = FastAPI(title="Performance Service")

# Create a mock Redis client
redis_client = fakeredis.FakeRedis(decode_responses=True)

# %% [markdown]
# ## 1. Cache-Aside Pattern
# We simulate a slow database query that takes 1 second to execute.
# Upon a cache miss, we fetch the data, write it to Redis with a 10-second TTL, and return.
# Upon a cache hit, we return immediately.

# %%
# 4. CACHE-ASIDE ENDPOINT

@app.get("/api/v1/heavy-data/{item_id}")
def get_heavy_data(item_id: int):
    cache_key = f"heavy_item:{item_id}"
    
    # Step 1: Check Redis
    cached_val = redis_client.get(cache_key)
    if cached_val:
        return {"source": "cache", "data": json.loads(cached_val)}
        
    # Step 2: Cache Miss - Simulate slow DB query
    time.sleep(1.0) # 1 second delay
    db_data = {"item_id": item_id, "result": f"Complex calculation for item {item_id}"}
    
    # Step 3: Write to Redis with a 10-second TTL
    redis_client.setex(cache_key, 10, json.dumps(db_data))
    
    return {"source": "database", "data": db_data}

# %% [markdown]
# ## 2. IP-Based Rate Limiting
# We write a custom middleware that tracks requests by IP address.
# We allow a maximum of 3 requests every 10 seconds. If the client exceeds this,
# we return `429 Too Many Requests`.

# %%
# 5. RATE LIMITER MIDDLEWARE

@app.middleware("http")
async def rate_limiter(request: Request, call_next):
    # Use client IP as the identifier
    client_ip = request.client.host
    redis_key = f"rate_limit:{client_ip}"
    
    # Get current request count
    current_requests = redis_client.get(redis_key)
    
    if current_requests and int(current_requests) >= 3:
        # Exceeded limit!
        return json_response_429()
        
    # Increment counter
    if not current_requests:
        # First request in this window: set counter and TTL of 10 seconds
        redis_client.setex(redis_key, 10, 1)
    else:
        # Increment atomic counter
        redis_client.incr(redis_key)
        
    response = await call_next(request)
    return response

def json_response_429():
    from fastapi.responses import JSONResponse
    return JSONResponse(
        status_code=status.HTTP_429_TOO_MANY_REQUESTS,
        content={"detail": "Too many requests. You are allowed 3 requests every 10 seconds."}
    )

# %%
# 6. INITIALIZE TEST CLIENT
client = TestClient(app)

# %% [markdown]
# ### Test 1: Verifying Cache-Aside Performance
# Watch the execution times of the first and second calls.
# - Call 1 (Database): Takes ~1.0 second.
# - Call 2 (Cache): Takes ~0.0 seconds!

# %%
# First call (Cache Miss)
start = time.time()
r1 = client.get("/api/v1/heavy-data/42")
print(f"Call 1 Time: {time.time() - start:.4f}s | Source: {r1.json()['source']}")

# Second call (Cache Hit)
start = time.time()
r2 = client.get("/api/v1/heavy-data/42")
print(f"Call 2 Time: {time.time() - start:.4f}s | Source: {r2.json()['source']}")

# %% [markdown]
# ### Test 2: Verifying the Rate Limiter
# We will make 4 requests in rapid succession.
# - Request 1, 2, 3: Should succeed.
# - Request 4: Should fail with `429 Too Many Requests`.

# %%
# Clear rate limit keys to reset test state
redis_client.flushdb()

for i in range(1, 5):
    response = client.get("/api/v1/heavy-data/10")
    print(f"Request {i} | Status Code: {response.status_code}")
    if response.status_code == 429:
        print("Response:", response.json())

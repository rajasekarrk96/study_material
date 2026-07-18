# %% [markdown]
# # Topic 9: API Request Lifecycle & Middleware Playground
# In this playground, you will learn how to intercept requests and responses.
# We will write:
# 1. A custom **timing middleware** that adds a header `X-Process-Time` to every response.
# 2. A custom **security headers middleware** that adds secure headers (`X-Frame-Options`, `X-XSS-Protection`).
# 3. A mock **CORS configuration** to see how the server responds to cross-origin requests.
#
# **How to use this:**
# 1. Open this file in VS Code.
# 2. Click **"Run Cell"** above each code block.

# %%
# 1. IMPORT LIBRARIES
import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient
import json

# %%
# 2. APPLICATION SETUP
app = FastAPI(title="Middleware & CORS Service")

# %% [markdown]
# ## 1. Configuring CORS
# We configure CORS to allow requests originating from `http://localhost:3000` (e.g., a React app).

# %%
# 3. CORS MIDDLEWARE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Allowed origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["X-Custom-Header", "Content-Type", "Authorization"],
)

# %% [markdown]
# ## 2. Custom Timing Middleware
# We write an asynchronous middleware function. It records the start time, calls `call_next`
# to let the request proceed to the route handler, computes the duration, and injects the header.

# %%
# 4. CUSTOM TIMING MIDDLEWARE
@app.middleware("http")
async def add_timing_and_security(request: Request, call_next):
    # --- BEFORE REQUEST ---
    start_time = time.time()
    
    # Let the request proceed to the route handler
    response = await call_next(request)
    
    # --- AFTER RESPONSE ---
    duration = time.time() - start_time
    
    # Inject timing header
    response.headers["X-Process-Time"] = f"{duration:.6f} seconds"
    
    # Inject security headers
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    
    return response

# %%
# 5. ROUTE DEFINITIONS
@app.get("/api/v1/data")
def get_data():
    # Simulate some business logic processing time
    time.sleep(0.05) # 50 milliseconds
    return {"status": "success", "payload": "Here is your secure data."}

# %%
# 6. INITIALIZE TEST CLIENT
client = TestClient(app)

# %% [markdown]
# ### Test 1: Standard Request
# We make a standard request. Notice that the response headers now contain `X-Process-Time`,
# `X-Frame-Options`, and `X-XSS-Protection` which were injected by our middleware!

# %%
response = client.get("/api/v1/data")
print(f"Status Code: {response.status_code}")
print("\n--- Response Headers ---")
for key, val in response.headers.items():
    print(f"{key}: {val}")

# %% [markdown]
# ### Test 2: CORS Pre-flight Request (OPTIONS)
# Let's simulate a browser sending a pre-flight request from `http://localhost:3000`.
# The browser will send an `OPTIONS` request with the `Origin` header.
# The server should respond with `Access-Control-Allow-Origin: http://localhost:3000`.

# %%
cors_headers = {
    "Origin": "http://localhost:3000",
    "Access-Control-Request-Method": "GET",
    "Access-Control-Request-Headers": "X-Custom-Header"
}

response = client.options("/api/v1/data", headers=cors_headers)
print(f"Pre-flight Status Code: {response.status_code} (Should be 200)")
print("\n--- CORS Headers Returned ---")
for key, val in response.headers.items():
    if key.startswith("access-control-"):
        print(f"{key}: {val}")

# %% [markdown]
# ### Test 3: CORS Blocked Origin
# Let's simulate a request from an untrusted origin: `http://hackersite.com`.
# The server should NOT return the `Access-Control-Allow-Origin` header, causing the browser to block the request.

# %%
blocked_headers = {
    "Origin": "http://hackersite.com",
    "Access-Control-Request-Method": "GET"
}

response = client.options("/api/v1/data", headers=blocked_headers)
print(f"Status Code: {response.status_code}")
print("Access-Control-Allow-Origin in headers?")
print("Access-Control-Allow-Origin" in response.headers) # Should be False

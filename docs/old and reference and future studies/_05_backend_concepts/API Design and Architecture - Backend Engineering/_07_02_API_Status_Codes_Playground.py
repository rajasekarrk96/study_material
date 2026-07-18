# %% [markdown]
# # Topic 7: API Status Codes & Error Handling Playground
# In this playground, you will learn how to implement clean error handling.
# Instead of writing try-except blocks inside every route handler, we will throw
# custom domain exceptions and catch them globally using FastAPI's exception handlers.
#
# **How to use this:**
# 1. Open this file in VS Code.
# 2. Click **"Run Cell"** above each code block.

# %%
# 1. IMPORT LIBRARIES
from fastapi import FastAPI, Request, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient
import json

# %% [markdown]
# ## Defining Custom Domain Exceptions
# We define custom Python exceptions representing business logic failures.
# Note that these exceptions are completely independent of HTTP. They do not know about
# FastAPI, routers, or status codes. This keeps our business logic pure.

# %%
# 2. CUSTOM EXCEPTIONS
class UserAlreadyExistsException(Exception):
    def __init__(self, email: str):
        self.email = email

class InsufficientStockException(Exception):
    def __init__(self, product_id: int, requested: int, available: int):
        self.product_id = product_id
        self.requested = requested
        self.available = available

# %%
# 3. APPLICATION SETUP
app = FastAPI(title="Error Handling Service")

# %% [markdown]
# ## Registering Global Exception Handlers
# We map our custom domain exceptions to HTTP responses.
# We will format the error body following the **RFC 7807 (Problem Details)** standard.

# %%
# 4. EXCEPTION HANDLERS

@app.exception_handler(UserAlreadyExistsException)
def user_exists_handler(request: Request, exc: UserAlreadyExistsException):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "type": "https://api.myshop.com/errors/email-conflict",
            "title": "Email Conflict",
            "status": status.HTTP_409_CONFLICT,
            "detail": f"The email address '{exc.email}' is already registered to another account.",
            "instance": request.url.path
        }
    )

@app.exception_handler(InsufficientStockException)
def stock_handler(request: Request, exc: InsufficientStockException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "type": "https://api.myshop.com/errors/insufficient-stock",
            "title": "Insufficient Stock",
            "status": status.HTTP_400_BAD_REQUEST,
            "detail": f"Cannot fulfill request. Requested {exc.requested} units of product {exc.product_id}, but only {exc.available} are available.",
            "instance": request.url.path,
            "error_metadata": {
                "product_id": exc.product_id,
                "available_stock": exc.available
            }
        }
    )

# %% [markdown]
# ## Endpoints That Throw Exceptions
# Our endpoints simulate business logic checks and throw our custom exceptions.

# %%
# 5. ROUTE DEFINITIONS

@app.post("/api/v1/users")
def register_user(email: str):
    # Simulate database check
    existing_emails = ["admin@example.com", "user@example.com"]
    if email in existing_emails:
        raise UserAlreadyExistsException(email=email)
    return {"message": "Registration successful", "email": email}

@app.post("/api/v1/orders")
def place_order(product_id: int, quantity: int):
    # Simulate inventory check
    available_stock = 3
    if quantity > available_stock:
        raise InsufficientStockException(
            product_id=product_id,
            requested=quantity,
            available=available_stock
        )
    return {"message": "Order placed successfully", "product_id": product_id, "quantity": quantity}

# %%
# 6. INITIALIZE TEST CLIENT
client = TestClient(app)

# %% [markdown]
# ### Test 1: Triggering UserAlreadyExistsException
# Let's register "admin@example.com". The server should return `409 Conflict`
# and our custom RFC 7807 JSON error body.

# %%
response = client.post("/api/v1/users?email=admin@example.com")
print(f"Status Code: {response.status_code} (Should be 409)")
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ### Test 2: Triggering InsufficientStockException
# Let's order 5 items. Since we only have 3 in stock, the server should return `400 Bad Request`
# along with the detailed stock metadata.

# %%
response = client.post("/api/v1/orders?product_id=99&quantity=5")
print(f"Status Code: {response.status_code} (Should be 400)")
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ### Test 3: Successful Request
# Let's make a successful order. The server should return `200 OK` and success body.

# %%
response = client.post("/api/v1/orders?product_id=99&quantity=2")
print(f"Status Code: {response.status_code} (Should be 200)")
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# # Topic 4: Monoliths vs. Microservices Playground
# In this playground, you will learn how microservices communicate with each other.
# We will simulate the **Order Service** making an HTTP call to the **User Service**
# to verify a user's existence before creating an order.
#
# We will use `respx` or mock responses to simulate network latency, timeouts,
# and service failures, showing you how to build resilient inter-service calls.

# %%
# 1. INSTALL DEPENDENCIES
# We install httpx for making HTTP calls, and respx for mocking HTTP responses.
%pip install httpx respx fastapi

# %%
# 2. IMPORT LIBRARIES
import httpx
import respx
from fastapi import FastAPI, status, HTTPException
from fastapi.testclient import TestClient
import json

# %%
# 3. DEFINE THE ORDER SERVICE
app = FastAPI(title="Order Service")

# Let's assume the User Service is hosted at this URL in our cluster
USER_SERVICE_URL = "http://user-service.internal/api/v1/users"

@app.post("/api/v1/orders", status_code=status.HTTP_201_CREATED)
def create_order(user_id: int, product_id: int, quantity: int):
    # Before creating the order, we must verify with the User Service:
    # 1. Does this user exist?
    # 2. Is the user's account active?
    
    print(f"[Order Service] Verifying user {user_id} with User Service...")
    
    # We set a strict timeout (e.g., 2.0 seconds) so that if the User Service
    # is hanging, we don't block our client forever.
    try:
        with httpx.Client(timeout=2.0) as client:
            response = client.get(f"{USER_SERVICE_URL}/{user_id}")
            
            if response.status_code == 404:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Order failed: User does not exist"
                )
            elif response.status_code != 200:
                raise HTTPException(
                    status_code=status.HTTP_502_BAD_GATEWAY,
                    detail="Order failed: User Service returned an error"
                )
                
            user_data = response.json()
            if not user_data.get("is_active", False):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Order failed: User account is inactive"
                )
                
    except httpx.TimeoutException:
        # Handle timeout gracefully
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Order failed: User Service timed out"
        )
    except httpx.RequestError:
        # Handle connection failures (e.g., DNS error, service down)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Order failed: Cannot connect to User Service"
        )
        
    # User is valid! Save order...
    return {
        "order_id": 999,
        "user_id": user_id,
        "product_id": product_id,
        "quantity": quantity,
        "status": "Created"
    }

# %%
# 4. INITIALIZE TEST CLIENT
client = TestClient(app)

# %% [markdown]
# ### Mocking the Network using Respx
# Since `user-service.internal` does not exist on the internet, we mock the network responses
# to test how our Order Service handles different scenarios.

# %%
# 5. TEST SCENARIO 1: SUCCESSFUL USER VERIFICATION
# We mock that GET http://user-service.internal/api/v1/users/42 returns a 200 OK with active status.

with respx.mock:
    respx.get("http://user-service.internal/api/v1/users/42").mock(
        return_value=httpx.Response(200, json={"id": 42, "name": "Dwight Schrute", "is_active": True})
    )
    
    response = client.post("/api/v1/orders?user_id=42&product_id=1&quantity=5")
    print(f"Status Code: {response.status_code}")
    print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ### Test Scenario 2: User Does Not Exist (404)
# The User Service returns 404. Our Order Service should return 400 Bad Request.

# %%
with respx.mock:
    respx.get("http://user-service.internal/api/v1/users/99").mock(
        return_value=httpx.Response(404)
    )
    
    response = client.post("/api/v1/orders?user_id=99&product_id=1&quantity=5")
    print(f"Status Code: {response.status_code} (Should be 400)")
    print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ### Test Scenario 3: User Service is Down (Connection Timeout)
# The User Service is hanging. Our HTTP client times out after 2 seconds. 
# Our Order Service should return a `503 Service Unavailable` instead of hanging indefinitely.

# %%
with respx.mock:
    # Simulate a timeout
    respx.get("http://user-service.internal/api/v1/users/100").mock(
        side_effect=httpx.TimeoutException("Connection timed out")
    )
    
    response = client.post("/api/v1/orders?user_id=100&product_id=1&quantity=5")
    print(f"Status Code: {response.status_code} (Should be 503)")
    print(json.dumps(response.json(), indent=2))

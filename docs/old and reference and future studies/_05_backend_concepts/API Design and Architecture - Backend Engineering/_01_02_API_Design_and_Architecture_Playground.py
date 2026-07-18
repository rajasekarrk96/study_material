# %% [markdown]
# # Topic 1: Interactive API Playground
# In this playground, you will learn how FastAPI processes requests and returns responses.
# We use FastAPI's `TestClient` so you can execute HTTP requests directly inside this file
# and see the results in real-time.
#
# **How to use this:**
# 1. Open this file in VS Code.
# 2. Make sure you have the **Jupyter** extension installed.
# 3. Click **"Run Cell"** above each code block (marked by `# %%`).

# %%
# 1. INSTALL DEPENDENCIES (If not already installed)
# Run this cell to ensure you have fastapi and httpx installed.
# (httpx is required by TestClient)
%pip install fastapi uvicorn pydantic email-validator httpx

# %%
# 2. IMPORT LIBRARIES
from fastapi import FastAPI, status, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, EmailStr, Field
from typing import List

# %% [markdown]
# ## Defining the Data Schemas (DTOs)
# Pydantic validates the incoming data. If the client sends invalid data, 
# Pydantic automatically rejects it and returns a `422 Unprocessable Entity` validation error.

# %%
# 3. SCHEMAS
class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="User's full name")
    email: EmailStr = Field(..., description="A valid email address")
    password: str = Field(..., min_length=8, description="Minimum 8 characters password")

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

# %% [markdown]
# ## Creating the FastAPI Application and Router
# We instantiate our app and create an in-memory database (`USERS_DB`).

# %%
# 4. APPLICATION SETUP & ROUTES
app = FastAPI(title="E-Commerce User Service")

USERS_DB = []
current_id = 1

@app.post("/api/v1/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserCreate):
    global current_id
    
    # Check if email already exists
    for user in USERS_DB:
        if user["email"] == user_in.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
            
    # Mock password hashing (In production, use passlib/bcrypt!)
    hashed_password = f"hashed_secure_{user_in.password}"
    
    new_user = {
        "id": current_id,
        "name": user_in.name,
        "email": user_in.email,
        "password": hashed_password  # Saved securely
    }
    
    USERS_DB.append(new_user)
    current_id += 1
    
    # FastAPI automatically filters the output using the `response_model=UserResponse`
    # so the 'password' field is NOT sent back to the client!
    return new_user

@app.get("/api/v1/users", response_model=List[UserResponse])
def get_users():
    return USERS_DB

# %% [markdown]
# ## Testing the API Interactively
# Now we set up the `TestClient`. This simulates a web browser or mobile app making requests to our API.

# %%
# 5. INITIALIZE TEST CLIENT
client = TestClient(app)

# %% [markdown]
# ### Test Case 1: Create a Valid User
# Let's send a `POST` request with valid details. Notice the status code should be `201 Created`.

# %%
valid_payload = {
    "name": "Alice Smith",
    "email": "alice@example.com",
    "password": "supersecretpassword123"
}

response = client.post("/api/v1/users", json=valid_payload)

print(f"Status Code: {response.status_code}")
print("Response JSON:")
import json
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ### Test Case 2: Validation Failure (Invalid Email & Short Password)
# Let's see how Pydantic automatically handles bad data. We send an invalid email and a 3-character password.
# Notice the status code will be `422 Unprocessable Entity` and the JSON will explain exactly what failed.

# %%
invalid_payload = {
    "name": "Bob",
    "email": "bob-is-not-an-email",
    "password": "123"
}

response = client.post("/api/v1/users", json=invalid_payload)

print(f"Status Code: {response.status_code}")
print("Response JSON:")
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ### Test Case 3: Duplicate Email Prevention
# Let's try to register Alice again. The service should return a `400 Bad Request` with our custom detail message.

# %%
response = client.post("/api/v1/users", json=valid_payload)

print(f"Status Code: {response.status_code}")
print("Response JSON:")
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ### Test Case 4: Retrieve Users list
# Let's fetch all registered users.

# %%
response = client.get("/api/v1/users")

print(f"Status Code: {response.status_code}")
print("Response JSON:")
print(json.dumps(response.json(), indent=2))

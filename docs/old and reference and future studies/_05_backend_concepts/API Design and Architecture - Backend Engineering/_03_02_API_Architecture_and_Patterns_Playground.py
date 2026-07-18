# %% [markdown]
# # Topic 3: API Architecture, Layered Patterns, and Dependency Injection Playground
# In this playground, you will learn how to decouple your codebase using a Three-Tier architecture
# (Router -> Service -> Repository) and how Dependency Injection makes your code 100% testable.
#
# **How to use this:**
# 1. Open this file in VS Code.
# 2. Click **"Run Cell"** above each code block.

# %%
# 1. IMPORT LIBRARIES
from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, EmailStr
from typing import Optional
import json

# %% [markdown]
# ## Tier 1: The Data Access Layer (Repository)
# The repository only cares about reading and writing data. It has no business logic.

# %%
# 2. REPOSITORY
class UserRepository:
    def __init__(self):
        # Simulated database table
        self._db = []
        self._current_id = 1

    def get_by_email(self, email: str) -> Optional[dict]:
        for user in self._db:
            if user["email"] == email:
                return user
        return None

    def create(self, name: str, email: str, password_hash: str) -> dict:
        user = {
            "id": self._current_id,
            "name": name,
            "email": email,
            "password_hash": password_hash
        }
        self._db.append(user)
        self._current_id += 1
        return user

# %% [markdown]
# ## Tier 2: The Business Logic Layer (Service)
# The service contains all calculations, rules, and password hashing. It does *not* know about HTTP,
# headers, or FastAPI. It receives dependencies via its constructor (Constructor Injection).

# %%
# 3. SERVICE
class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register_user(self, name: str, email: str, password_raw: str) -> dict:
        # Business Rule 1: Check duplicate email
        if self.user_repo.get_by_email(email):
            raise ValueError("Email already registered")
            
        # Business Rule 2: Password strength check
        if len(password_raw) < 8:
            raise ValueError("Password must be at least 8 characters")
            
        # Business Rule 3: Hash password
        hashed_password = f"secure_hash_{password_raw}"
        
        # Save to database
        return self.user_repo.create(name, email, hashed_password)

# %% [markdown]
# ## Tier 3: The Presentation Layer (Router / FastAPI App)
# The presentation layer defines endpoints, validates JSON payloads, and handles HTTP status codes.
# It uses FastAPI's `Depends` to inject the `UserService`.

# %%
# 4. PRESENTATION LAYER & DEPENDENCY INJECTION SETUP

app = FastAPI()

# 1. We instantiate a single instance of our repository (in-memory database)
user_repository = UserRepository()

# 2. We define a dependency function that provides the UserService.
# This function injects the repository into the service.
def get_user_service() -> UserService:
    return UserService(user_repo=user_repository)

# Schemas
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

# Route Handler
@app.post("/api/v1/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(
    user_in: UserCreate,
    service: UserService = Depends(get_user_service) # Injected here!
):
    try:
        # The route handler simply delegates the work to the service
        new_user = service.register_user(
            name=user_in.name,
            email=user_in.email,
            password_raw=user_in.password
        )
        return new_user
    except ValueError as e:
        # Convert business domain errors into HTTP status codes
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# %%
# 5. INITIALIZE TEST CLIENT
client = TestClient(app)

# %% [markdown]
# ### Test Case 1: Standard API Call (Integration)
# Let's verify everything works together. We register a user successfully.

# %%
payload = {"name": "Bob Vance", "email": "bob@vancerefrigeration.com", "password": "refrigeration123"}
response = client.post("/api/v1/users", json=payload)
print(f"Status Code: {response.status_code}")
print(json.dumps(response.json(), indent=2))

# %% [markdown]
# ## The Power of DI: Unit Testing with Mocks
# Imagine the database is slow, down, or we don't want to write to it during testing.
# We can create a `MockUserRepository` and test the `UserService` in isolation!

# %%
# 6. UNIT TESTING THE SERVICE IN ISOLATION (NO WEB SERVER, NO REAL DATABASE)

class MockUserRepository:
    def __init__(self):
        self.get_by_email_called = False
        self.create_called = False

    def get_by_email(self, email: str):
        self.get_by_email_called = True
        # Simulate that the email already exists for our test
        if email == "duplicate@example.com":
            return {"id": 1, "email": "duplicate@example.com"}
        return None

    def create(self, name: str, email: str, password_hash: str):
        self.create_called = True
        return {"id": 99, "name": name, "email": email}

# Let's test the UserService's duplicate email business rule:
mock_repo = MockUserRepository()
service_to_test = UserService(user_repo=mock_repo)

# Test 1: Expect ValueError when registering a duplicate email
try:
    service_to_test.register_user("Test", "duplicate@example.com", "password123")
except ValueError as e:
    print("Test 1 Passed: Correctly raised ValueError:", e)
    print(f"Mock Repo get_by_email was called: {mock_repo.get_by_email_called}")
    print(f"Mock Repo create was called: {mock_repo.create_called} (Should be False!)")

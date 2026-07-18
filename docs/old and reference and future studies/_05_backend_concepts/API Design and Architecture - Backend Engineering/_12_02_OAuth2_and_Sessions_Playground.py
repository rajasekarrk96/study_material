# %% [markdown]
# # Topic 12: OAuth2 & Session-based Authentication Playground
# In this playground, you will learn how to implement OAuth2 Scopes.
# Scopes are used to restrict access to specific parts of your API.
# E.g., a token might allow reading profile data (`me` scope) but not creating items (`items` scope).
#
# **How to use this:**
# 1. Open this file in VS Code.
# 2. Click **"Run Cell"** above each code block.

# %%
# 1. IMPORT LIBRARIES
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.testclient import TestClient
from jose import jwt, JWTError
from datetime import datetime, timezone, timedelta
import json

# %%
# 2. SECURITY SETUP
SECRET_KEY = "my_oauth2_secret_key"
ALGORITHM = "HS256"

# Define OAuth2PasswordBearer.
# It tells FastAPI that the client must send credentials to '/api/v1/token' to get a token.
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/token",
    scopes={
        "me": "Read information about the current user.",
        "items": "Create and manage catalog items."
    }
)

# %%
# 3. APPLICATION SETUP
app = FastAPI(title="OAuth2 Scopes Service")

# %% [markdown]
# ## 4. Token Generation & Verification
# We embed the granted scopes directly inside the JWT payload under the `scopes` claim.

# %%
def create_access_token(data: dict, scopes: list) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({
        "exp": int(expire.timestamp()),
        "scopes": scopes
    })
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# %%
# 5. ROUTE DEFINITIONS

@app.post("/api/v1/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Mock credential verification
    if form_data.username != "admin" or form_data.password != "admin123":
        raise HTTPException(status_code=400, detail="Incorrect username or password")
        
    # The client requests scopes. We verify and grant them.
    # If no scopes are requested, we grant a default 'me' scope.
    requested_scopes = form_data.scopes
    if not requested_scopes:
        requested_scopes = ["me"]
        
    access_token = create_access_token(
        data={"sub": form_data.username},
        scopes=requested_scopes
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "scope": " ".join(requested_scopes)
    }

# Dependency to verify token and scope
class ScopeChecker:
    def __init__(self, required_scope: str):
        self.required_scope = required_scope

    def __call__(self, token: str = Depends(oauth2_scheme)) -> dict:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            token_scopes = payload.get("scopes", [])
            
            if self.required_scope not in token_scopes:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Not enough permissions. Requires scope: {self.required_scope}"
                )
            return payload
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token"
            )

# %% [markdown]
# ## Securing Endpoints with Scopes
# We use our `ScopeChecker` dependency to enforce permissions.

# %%
@app.get("/api/v1/users/me")
def read_current_user(payload: dict = Depends(ScopeChecker("me"))):
    return {
        "message": "Access granted to profile!",
        "user": payload["sub"]
    }

@app.post("/api/v1/items")
def create_item(payload: dict = Depends(ScopeChecker("items"))):
    return {
        "message": "Item created successfully!",
        "created_by": payload["sub"]
    }

# %%
# 6. INITIALIZE TEST CLIENT
client = TestClient(app)

# %% [markdown]
# ### Test 1: Requesting a Token with ONLY 'me' Scope
# We log in and request only the `me` scope.

# %%
login_payload = {
    "username": "admin",
    "password": "admin123",
    "scope": "me"
}
response = client.post("/api/v1/token", data=login_payload)
token_me_data = response.json()
print("Token with 'me' scope:")
print(json.dumps(token_me_data, indent=2))

# %% [markdown]
# ### Test 2: Accessing /users/me (Should succeed)
# Since we have the `me` scope, this should return `200 OK`.

# %%
headers_me = {"Authorization": f"Bearer {token_me_data['access_token']}"}
response = client.get("/api/v1/users/me", headers=headers_me)
print(f"Status /users/me: {response.status_code}")
print(response.json())

# %% [markdown]
# ### Test 3: Accessing /items (Should be forbidden)
# Since we do NOT have the `items` scope, this should return `403 Forbidden`.

# %%
response = client.post("/api/v1/items", headers=headers_me)
print(f"Status /items: {response.status_code} (Should be 403)")
print(response.json())

# %% [markdown]
# ### Test 4: Requesting a Token with both 'me' and 'items' Scopes
# We log in again, requesting both scopes.

# %%
login_payload_all = {
    "username": "admin",
    "password": "admin123",
    "scope": "me items"
}
response = client.post("/api/v1/token", data=login_payload_all)
token_all_data = response.json()

headers_all = {"Authorization": f"Bearer {token_all_data['access_token']}"}
response = client.post("/api/v1/items", headers=headers_all)
print(f"Status /items with full token: {response.status_code} (Should be 200)")
print(response.json())

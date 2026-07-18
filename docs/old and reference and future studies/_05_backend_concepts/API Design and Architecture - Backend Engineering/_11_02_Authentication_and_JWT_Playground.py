# %% [markdown]
# # Topic 11: Token-based Authentication & JWT Playground
# In this playground, you will learn how to implement secure authentication.
# We will cover:
# 1. Hashing passwords using `bcrypt` (via `passlib`).
# 2. Generating signed JWT access tokens using `python-jose`.
# 3. Protecting routes using FastAPI dependencies.
#
# **How to use this:**
# 1. Open this file in VS Code.
# 2. Click **"Run Cell"** above each code block.

# %%
# 1. INSTALL DEPENDENCIES
# We install python-jose for JWTs, and passlib with bcrypt for password hashing.
%pip install python-jose[cryptography] passlib[bcrypt] fastapi

# %%
# 2. IMPORT LIBRARIES
from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.testclient import TestClient
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from jose import jwt, JWTError
import json

# %%
# 3. SECURITY SETUP
# CryptContext hashes passwords using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT configuration
SECRET_KEY = "my_super_secret_signing_key_keep_this_private"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

# FastAPI's HTTPBearer helper extracts the 'Authorization: Bearer <token>' header
security_scheme = HTTPBearer()

# %%
# 4. UTILITY FUNCTIONS

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": int(expire.timestamp())})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials / Token expired"
        )

# %%
# 5. APPLICATION SETUP
app = FastAPI(title="JWT Auth Service")

# Let's seed a mock user in our database with a hashed password
# Plain text password: "securepassword123"
MOCK_USER_DB = {
    "id": 1,
    "email": "dwight@dundermifflin.com",
    "name": "Dwight Schrute",
    "hashed_password": hash_password("securepassword123")
}

# %% [markdown]
# ## 6. Route Definitions
# 1. `POST /api/v1/login`: Verifies password and returns a JWT.
# 2. `GET /api/v1/users/me`: A protected route that requires a valid JWT.

# %%
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

@app.post("/api/v1/login")
def login(login_data: LoginRequest):
    # 1. Verify user email
    if login_data.email != MOCK_USER_DB["email"]:
        raise HTTPException(status_code=401, detail="Invalid email or password")
        
    # 2. Verify password hash
    if not verify_password(login_data.password, MOCK_USER_DB["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
        
    # 3. Generate access token
    access_token = create_access_token(data={"sub": MOCK_USER_DB["email"], "name": MOCK_USER_DB["name"]})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# Protected dependency
def get_current_user(token: HTTPAuthorizationCredentials = Depends(security_scheme)) -> dict:
    # Extracts the token from the 'Authorization' header
    payload = verify_token(token.credentials)
    return payload

@app.get("/api/v1/users/me")
def read_current_user(current_user: dict = Depends(get_current_user)):
    return {
        "message": "You have accessed a protected route!",
        "user_info": current_user
    }

# %%
# 7. INITIALIZE TEST CLIENT
client = TestClient(app)

# %% [markdown]
# ### Test 1: Failed Login (Wrong Password)
# We expect `401 Unauthorized`.

# %%
wrong_login = {"email": "dwight@dundermifflin.com", "password": "wrongpassword"}
response = client.post("/api/v1/login", json=wrong_login)
print(f"Login Status: {response.status_code}")
print(response.json())

# %% [markdown]
# ### Test 2: Successful Login
# We expect `200 OK` and a JWT token.

# %%
correct_login = {"email": "dwight@dundermifflin.com", "password": "securepassword123"}
response = client.post("/api/v1/login", json=correct_login)
print(f"Login Status: {response.status_code}")
token_data = response.json()
print("JWT Token received:")
print(json.dumps(token_data, indent=2))

# %% [markdown]
# ### Test 3: Access Protected Route Without Token
# We expect `403 Forbidden` (or 401 depending on the scheme). FastAPI's HTTPBearer returns 403 if header is missing.

# %%
response = client.get("/api/v1/users/me")
print(f"Status Code: {response.status_code} (Should be 403)")

# %% [markdown]
# ### Test 4: Access Protected Route With Token
# We attach the token in the `Authorization: Bearer <token>` header. We expect `200 OK` and our user data.

# %%
token = token_data["access_token"]
headers = {"Authorization": f"Bearer {token}"}

response = client.get("/api/v1/users/me", headers=headers)
print(f"Status Code: {response.status_code} (Should be 200)")
print(json.dumps(response.json(), indent=2))

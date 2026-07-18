# Module 5: Authentication
## Topic 12: OAuth2 & Session-based Authentication

---

### 1. The Big Picture

Authentication styles vary depending on the client type and integration needs.

#### Sessions vs. Tokens (JWT)
* **Session-based (Stateful):**
  * **How it works:** The server creates a session in database/memory upon login, returns a `Session ID` to the client in a cookie. The browser sends the cookie with every request. The server looks up the Session ID in its store.
  * **When to use:** Monolithic web applications with a browser client (e.g., standard Django, Ruby on Rails, Laravel, or Spring MVC). Extremely secure against XSS when using `HttpOnly`, `Secure`, and `SameSite` cookies.
* **Token-based (Stateless):**
  * **How it works:** The server returns a signed token (JWT) to the client. The client stores it (e.g., in memory) and sends it in the `Authorization: Bearer <token>` header.
  * **When to use:** Modern APIs, Single Page Applications (React/Vue), mobile apps, and microservices.

---

### 2. What is OAuth2?
**OAuth2** is an **authorization framework** (RFC 6749) that enables a third-party application to obtain limited access to an HTTP service, either on behalf of a resource owner or by allowing the third-party application to obtain access on its own behalf.

> [!NOTE]
> **Authentication vs. Authorization:**
> * **Authentication:** Who are you? (e.g., Log in with username/password).
> * **Authorization:** What are you allowed to do? (e.g., Can this third-party app read your Google Contacts?).

#### The 4 Core Roles in OAuth2
1. **Resource Owner:** The user (e.g., You).
2. **Client:** The third-party application wanting access (e.g., Spotify wanting your Facebook friends list).
3. **Resource Server:** The server hosting the protected data (e.g., Facebook API).
4. **Authorization Server:** The server verifying the user's identity and issuing access tokens (e.g., Facebook Login).

---

### 3. The OAuth2 Authorization Code Flow (The Standard Web Flow)

This is the secure flow used when a client has a secure backend server.

```
┌──────────────┐         1. Redirect to Login Page         ┌──────────────────────┐
│  User /      ├──────────────────────────────────────────►│ Authorization Server │
│  Browser     │◄──────────────────────────────────────────┤ (e.g., Google OAuth) │
└──────┬───────┘          2. User logs in, approves        └──────────┬───────────┘
       │                                                              │
       │ 3. Redirect back to Client with Auth Code                    │
       │◄─────────────────────────────────────────────────────────────┘
       │
       ▼
┌──────────────┐         4. Exchange Auth Code + Client Secret     ┌──────────────────────┐
│  Client App  ├──────────────────────────────────────────►│ Authorization Server │
│  (Backend)   │◄──────────────────────────────────────────┤                      │
└──────┬───────┘             5. Returns Access Token       └──────────────────────┘
       │
       │ 6. Access Resource with Access Token              ┌──────────────────────┐
       ├──────────────────────────────────────────────────►│   Resource Server    │
       │                                                   │     (Google API)     │
       └───────────────────────────────────────────────────┘
```

---

### 4. OAuth2 Scopes
**Scopes** are a mechanism in OAuth2 to limit an application's access to a user's account.
* Instead of full access, a client requests specific permissions:
  * `read:profile` (Read user's name and avatar).
  * `write:orders` (Create orders on behalf of the user).
* The user sees these requested scopes on the consent screen and approves them.

---

### 5. Python Example: OAuth2 Password Flow with Scopes in FastAPI
FastAPI has built-in support for the OAuth2 Password Flow (where the client collects the username and password directly and exchanges them for a token).

```python
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

# OAuth2PasswordBearer tells FastAPI that the token URL is '/token'
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={
        "me": "Read information about the current user.",
        "items": "Read and write items."
    }
)

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # form_data.username and form_data.password contain the credentials.
    # form_data.scopes contains the list of scopes requested by the client.
    return {
        "access_token": "mock_token_value",
        "token_type": "bearer",
        "scopes": form_data.scopes
    }

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"token": token, "user": "active_user"}
```

---

### 6. Hands-on Workout & Assessment

#### Part A: API Design Challenge (OAuth2 Scopes)
You are building an API for a **Document Management System** (like Google Drive). Third-party apps want to integrate with your platform.
- Design three OAuth2 scopes representing different levels of access (e.g., read-only, read-write, delete).
- Write down the names of these scopes and a brief description of what they allow.

#### Part B: Quiz
1. Which OAuth2 role represents the application that wants to access the user's data?
   A. Resource Owner
   B. Client
   C. Resource Server
   D. Authorization Server
2. What is the difference between stateful sessions and stateless tokens?
   A. Stateful sessions store login state on the server (database/Redis); stateless tokens (JWT) store login state on the client inside the signed token itself.
   B. Stateful sessions are only for mobile apps.
   C. Stateless tokens require a database query on every request.
   D. There is no difference.
3. What is the purpose of OAuth2 Scopes?
   A. To speed up token generation.
   B. To limit the permissions and access levels that a third-party application is requesting.
   C. To encrypt the password.
   D. To define the database schema.

---

### 7. Progress Tracker

* **Module 5: Authentication:** 0%
* **Topics Completed:** 0/2
* **Coding Exercises:** 0/0
* **Quiz Score:** N/A
* **API Design Challenge Score:** N/A
* **Backend Score:** 0 / 100

---

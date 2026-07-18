# Module 5: Authentication
## Topic 11: Token-based Authentication & JWT (JSON Web Tokens)

---

### 1. The Big Picture

#### What is JWT?
A **JWT (JSON Web Token)** is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed.

#### Why Companies Use JWT for APIs
In traditional web apps, the server stores session data in memory or a database, and the client sends a `Session ID` in a cookie. For APIs, this approach does not scale well:
1. **API Scalability:** If you have 10 API servers, they must all share a session database (like Redis) to know who is logged in.
2. **Statelessness:** JWTs are **stateless**. The token itself contains all the user data (claims). The server does not need to query a database to verify the token; it only needs to verify the digital signature using a secret key.

---

### 2. Anatomy of a JWT

A JWT is a string divided into three parts separated by dots (`.`): `header.payload.signature`

```
  HEADER (Algorithm & Token Type)
  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
  .
  PAYLOAD (Claims: User ID, Expiry, Roles)
  eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ
  .
  SIGNATURE (Verifies the token hasn't been altered)
  SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

1. **Header:** Specifies the signing algorithm (e.g., HMAC SHA256 or RSA).
2. **Payload:** Contains the **claims** (statements about the user, e.g., `user_id`, `email`, `exp` - expiration time).
3. **Signature:** Created by taking the encoded header, the encoded payload, a secret key, and signing them. If even a single character in the payload is changed, the signature becomes invalid.

---

### 3. JWT Authentication Flow

```
Client (Browser)                                    Server (API)
       │                                                 │
       ├───────────────── 1. POST /login ───────────────►│ (Checks password,
       │                 (Credentials)                   │  generates JWT)
       │                                                 │
       ◄─────────────── 2. Returns JWT ──────────────────┤
       │                                                 │
       │                                                 │
       ├───────── 3. GET /profile ──────────────────────►│ (Verifies signature
       │         (Authorization: Bearer <JWT>)           │  & expiration.
       │                                                 │  Returns profile)
       ◄─────────── 4. Returns Profile ──────────────────┤
```

---

### 4. Password Hashing (Crucial Security)
**Never store plain-text passwords in a database.** If your database is leaked, all user accounts are compromised.
* **Salt + Hash:** A salt is a random string added to the password before hashing. This prevents attackers from using pre-computed tables (Rainbow Tables) to crack passwords.
* **Algorithms:** Use slow, CPU-intensive algorithms designed for password hashing, such as **bcrypt** or **Argon2id**. Do **not** use fast hashing algorithms like MD5 or SHA256.

---

### 5. Python Example: JWT Handling in FastAPI

```python
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from passlib.context import CryptContext

# CryptContext for password hashing (uses bcrypt under the hood)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "my_super_secret_key_change_me_in_production"
ALGORITHM = "HS256"

# Hash password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Create JWT Access Token
def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Verify and Decode JWT Token
def verify_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise ValueError("Invalid or expired token")
```

---

### 6. Hands-on Workout & Assessment

#### Part A: API Design Challenge (Token Security)
A junior developer proposes storing the JWT in the browser's `localStorage` and sending it in the `Authorization` header.
- What security vulnerability does this expose the client to? (Hint: XSS).
- What is the alternative, more secure way to store tokens in a web browser to protect against XSS? (Hint: HttpOnly, Secure, SameSite Cookies).

#### Part B: Quiz
1. Which part of a JWT contains the user ID and token expiration timestamp?
   A. Header
   B. Payload
   C. Signature
   D. Metadata
2. Why is it a bad idea to use SHA256 for password hashing?
   A. SHA256 is not secure enough.
   B. SHA256 is too slow.
   C. SHA256 is a fast hashing algorithm, making it easy for attackers to brute-force millions of passwords per second using GPUs.
   D. SHA256 does not support salting.
3. What happens if a client alters the user ID in the JWT payload from `42` to `1` (admin)?
   A. The server will log them in as admin.
   B. The server will crash.
   C. The signature verification will fail, and the server will reject the token.
   D. The database will automatically update.

---

### 7. Progress Tracker

* **Module 5: Authentication:** 0%
* **Topics Completed:** 0/1
* **Coding Exercises:** 0/0
* **Quiz Score:** N/A
* **API Design Challenge Score:** N/A
* **Backend Score:** 0 / 100

---

# Module 3: FastAPI, CRUD, REST APIs
## Topic 9: API Request Lifecycle, Middleware, and CORS

---

### 1. The Big Picture

#### What is the Request Lifecycle?
The **Request Lifecycle** is the sequence of steps an HTTP request goes through from the moment a client sends it, to the moment the server returns a response. Understanding this flow is critical for debugging performance bottlenecks and implementing cross-cutting concerns like logging, security, and error tracking.

```
Client (Browser)
       │
       ▼ [1. Send Request]
┌────────────────────────────────────────────────────────┐
│               ASGI / Web Server (Uvicorn)              │
├────────────────────────────────────────────────────────┤
│                 [2. Middleware Layer]                  │ (CORS, Logging, Auth)
├────────────────────────────────────────────────────────┤
│                 [3. Routing & Matches]                 │ (Finds the right path)
├────────────────────────────────────────────────────────┤
│             [4. Dependency Injection & Val]            │ (Pydantic / Depends)
├────────────────────────────────────────────────────────┤
│                  [5. Route Handler]                    │ (Your business logic)
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼ [6. Response Formatted]
                         Client
```

---

### 2. What is Middleware?
**Middleware** is a function that runs before every request is processed by the route handler, and after every response is generated. 
* **Key Use Cases:**
  * **Logging:** Logging the HTTP method, path, and processing time of every request.
  * **Timing:** Adding a custom header `X-Process-Time` to measure performance.
  * **Security:** Setting security headers (like HSTS, Content-Security-Policy).
  * **Rate Limiting:** Blocking IPs that make too many requests.

---

### 3. Understanding CORS (Cross-Origin Resource Sharing)
**CORS** is a browser security mechanism. By default, browsers block frontend code (e.g., React running on `http://localhost:3000`) from making API calls to a different origin (e.g., FastAPI running on `http://localhost:8000`).

#### How CORS Works
1. When a browser makes a cross-origin request, it first sends a pre-flight request using the **`OPTIONS`** method.
2. The server must respond to this `OPTIONS` request with headers indicating which origins, methods, and headers are allowed.
3. If the server approves, the browser sends the actual request.

#### CORS Headers
* **`Access-Control-Allow-Origin`:** Specifies which domains can access the API. E.g., `http://localhost:3000` (or `*` for public APIs).
* **`Access-Control-Allow-Methods`:** E.g., `GET, POST, PUT, DELETE`.

---

### 4. Python Example: Configuring CORS and Custom Middleware in FastAPI

```python
import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 1. CONFIGURE CORS
# In production, NEVER use ["*"] for allow_origins. Specify your exact frontend domain.
origins = [
    "http://localhost:3000",
    "https://myshop.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. CUSTOM MIDDLEWARE (Timing and Logging)
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    
    # Process the request and get the response from the route handler
    response = await call_next(request)
    
    process_time = time.time() - start_time
    # Inject the processing time header
    response.headers["X-Process-Time"] = f"{process_time:.4f}s"
    
    print(f"Request: {request.method} {request.url.path} completed in {process_time:.4f}s")
    return response
```

---

### 5. Hands-on Workout & Assessment

#### Part A: API Design Challenge (CORS Security)
You are deploying your API to production at `https://api.mycompany.com`. Your web frontend is hosted at `https://mycompany.com`.
- What value should you set for `allow_origins` in your CORS configuration?
- Why is using `"*"` a major security risk for authenticated APIs that use cookies?

#### Part B: Quiz
1. What HTTP method does a browser use to send a CORS pre-flight request?
   A. GET
   B. OPTIONS
   C. POST
   D. HEAD
2. What is the role of the `call_next` parameter in FastAPI middleware?
   A. It terminates the application.
   B. It passes the request to the next middleware or the route handler and returns the response.
   C. It connects to the database.
   D. It schedules a background task.
3. Which header is returned by the server to tell the browser that a specific origin is allowed to access the API?
   A. `Host`
   B. `Access-Control-Allow-Origin`
   C. `Content-Type`
   D. `Origin`

---

### 6. Progress Tracker

* **Module 3: FastAPI, CRUD, REST APIs:** 0%
* **Topics Completed:** 0/2
* **Coding Exercises:** 0/0
* **Quiz Score:** N/A
* **API Design Challenge Score:** N/A
* **Backend Score:** 0 / 100

---

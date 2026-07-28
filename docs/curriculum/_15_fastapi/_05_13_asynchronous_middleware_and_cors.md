```yaml
schema_version: "2.0"
metadata:
  lesson_id: "FAP-MOD07-LES01"
  course_slug: "course-05-fastapi"
  course_title: "Course 5: FastAPI High-Performance Microservices"
  module_slug: "mod-07-middleware-cors"
  module_title: "Module 7 - Asynchronous Middleware & CORS"
  lesson_slug: "asynchronous-middleware-and-cors"
  lesson_title: "Lesson 7.1 Asynchronous Custom Middleware & CORS"
  sort_order: 701

pedagogy:
  difficulty: "intermediate"
  estimated_time:
    reading_minutes: 15
    practice_minutes: 20
    quiz_minutes: 10
    total_minutes: 45
  bloom_taxonomy_level: "Apply"
  xp_reward: 50

prerequisites:
  required_lesson_ids:
    - "FAP-MOD06-LES02"
  required_skills:
    - "FastAPI APIRouter & Async Request Handling"

skills_acquired:
  - "Writing Custom Asynchronous Middleware (`@app.middleware('http')`)"
  - "Interceptors for Request and Response Objects"
  - "Configuring Cross-Origin Resource Sharing (`CORSMiddleware`)"
  - "Securing Allowed Origins, Methods, and Headers"

dependencies:
  software:
    - "VS Code"
    - "Python 3.12+"
    - "fastapi"
  hardware: []

seo_and_social:
  meta_title: "FastAPI Middleware & CORS: @app.middleware('http') & CORSMiddleware"
  meta_description: "Master FastAPI Middleware & CORS: writing custom async middleware with @app.middleware('http'), request interception, and configuring CORSMiddleware for cross-origin security."
  keywords: ["FastAPI Middleware", "@app.middleware", "CORSMiddleware", "Cross Origin Resource Sharing", "Async Middleware", "FastAPI CORS"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 7.1 Asynchronous Custom Middleware & CORS

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 6.2 Modular Directory Layout](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_05_fastapi/_05_12_modular_directory_structure_and_big_applications.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Construct custom async middleware using **`@app.middleware("http")`**.
2. Intercept incoming `Request` and outgoing `Response` objects.
3. Understand Cross-Origin Resource Sharing (CORS) security risks.
4. Configure **`CORSMiddleware`** to allow cross-origin requests securely.

---

## 2. Environment & Prerequisites [id: prerequisites]

Open Python REPL or VS Code.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 What is FastAPI Middleware?
A **Middleware** is a function that executes on every HTTP request before it reaches a route handler, and on every HTTP response before it is sent back to the client.

In FastAPI, middleware is written asynchronously using `@app.middleware("http")`. It receives the incoming `request` and a `call_next` function:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          FASTAPI MIDDLEWARE PIPELINE                        │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Incoming Request ──► Executes Pre-Processing (Log IP, Check Headers)     │
│                     ──► `response = await call_next(request)`               │
│ 2. Route Handler    ──► Processes business logic & returns Response        │
│ 3. Outgoing Response ──► Executes Post-Processing (Attach custom headers)   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Cross-Origin Resource Sharing (CORS)
Browsers enforce the Same-Origin Policy, blocking frontend web applications (e.g., React on `http://localhost:3000`) from making HTTP API requests to backends on different origins (`http://localhost:8000`). `CORSMiddleware` attaches appropriate `Access-Control-Allow-Origin` headers to authorize cross-origin requests.

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    Browser[Browser / Frontend App: localhost:3000] --> Preflight["Preflight OPTIONS Request"]
    Preflight --> CORS["FastAPI CORSMiddleware"]
    CORS -->|Valid Origin| Allow["Return Access-Control-Allow-Origin: *"]
    Allow --> ActualReq[Browser sends actual POST API Request]
```

---

## 5. Code & Hardware Implementation [id: syntax]

```python
# FastAPI Middleware & CORS Configuration (middleware_demo.py)
import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Middleware & CORS API")

# 1. Configure CORSMiddleware (MUST be added before custom middleware!)
origins = [
    "http://localhost:3000",       # React Dev Server
    "http://127.0.0.1:3000",
    "https://telemetry.example.com" # Production Frontend Domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Allowed cross-origin domains
    allow_credentials=True,     # Allow cookies & authorization headers
    allow_methods=["*"],         # Allowed HTTP verbs (GET, POST, PUT, DELETE)
    allow_headers=["*"],         # Allowed HTTP headers
)

# 2. Custom Async HTTP Middleware
@app.middleware("http")
def add_process_time_header(request: Request, call_next):
    # Pre-processing execution (Before route handler)
    start_time = time.perf_counter()

    # Forward request to view handler
    response = call_next(request)

    # Post-processing execution (After route handler finishes)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time-Sec"] = f"{process_time:.6f}"
    
    return response

@app.get("/api/v1/sensors")
def get_sensors():
    return {"data": ["ESP32-A1", "ESP32-B2"]}
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Multi-Origin Single-Page Applications (SPAs)**: Production microservice APIs configure `CORSMiddleware` to allow cross-origin requests strictly from authorized frontend dashboard domains (`https://dashboard.company.com`).

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `middleware_demo.py`.
2. Run `uvicorn middleware_demo:app --reload`.
3. Send GET request via curl: `curl -i http://127.0.0.1:8000/api/v1/sensors` $\to$ Inspect `X-Process-Time-Sec` header in response!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`CORS Error: No 'Access-Control-Allow-Origin' header`** | Front-end domain missing from `allow_origins` list or using `allow_origins=["*"]` with `allow_credentials=True`. | Specify exact frontend origin URL in `allow_origins` when `allow_credentials=True`. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Avoid Wildcards in Production**: Never use `allow_origins=["*"]` when supporting authentication cookies or authorization headers.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: What is a CORS preflight request and how does FastAPI handle it?
**Answer**: When a web browser makes a cross-origin HTTP request containing non-simple headers or verbs (like `POST` with JSON or `Authorization` headers), it sends an automatic `OPTIONS` preflight request first to check if the server permits the operation. FastAPI's `CORSMiddleware` intercepts `OPTIONS` requests automatically and responds with matching `Access-Control-Allow-*` headers.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 7.1 Middleware & CORS Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which FastAPI decorator registers a custom HTTP request/response middleware function?",
      "options": ["@app.middleware('http')", "@app.use_middleware()", "@app.http_interceptor()", "@app.before_request"],
      "correct_answer_index": 0,
      "explanation": "@app.middleware('http') registers HTTP middleware."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Build a custom middleware attaching `X-Request-ID` headers to all API responses.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What function in custom FastAPI middleware forwards the request to the route handler?
**Back**: `response = await call_next(request)`.
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```python
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"])
@app.middleware("http")
async def log(request: Request, call_next): return await call_next(request)
```


---

## Migrated Notes

> **Source**: `_09_01_Request_Lifecycle_and_Middleware_Notes.md` (from backend concepts archive)
> This content was migrated from existing study notes. Review and merge with topics above.

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

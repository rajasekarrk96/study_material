# Module 2: API Status Codes, HTTP, REST, OpenAPI
## Topic 6: The HTTP Protocol (Deep Dive)

---

### 1. The Big Picture

#### What is HTTP?
**HTTP (Hypertext Transfer Protocol)** is the foundation of data communication on the World Wide Web. It is an application-layer protocol designed to transfer information between networked devices. It operates on a simple **Request-Response** model.

#### How it Fits in Backend Architecture
Every API request from a client is wrapped in an HTTP packet. Your backend web server (e.g., Uvicorn/Gunicorn for Python, Tomcat for Spring Boot) parses this raw TCP/IP stream into an HTTP request object. Your framework (FastAPI or Spring) then routes it to your code.

```
┌──────────┐               HTTP Request               ┌───────────┐
│          ├─────────────────────────────────────────►│           │
│  Client  │                                          │  Server   │
│          │◄─────────────────────────────────────────┤           │
└──────────┘               HTTP Response              └───────────┘
```

---

### 2. Anatomy of an HTTP Request

An HTTP request consists of three parts:
1. **Request Line:** The method, the path, and the HTTP version.
   * *Example:* `POST /api/v1/users HTTP/1.1`
2. **Headers:** Key-value pairs providing metadata about the request.
   * *Example:*
     * `Host: api.myshop.com`
     * `Content-Type: application/json` (Tells the server the body is JSON)
     * `Authorization: Bearer <JWT_TOKEN>` (Authentication)
     * `Accept: application/json` (Tells the server the client wants JSON back)
3. **Body (Optional):** The actual payload (data) being sent to the server. Usually present in `POST`, `PUT`, and `PATCH` requests.

---

### 3. Anatomy of an HTTP Response

An HTTP response consists of three parts:
1. **Status Line:** The HTTP version, the status code, and the status text.
   * *Example:* `HTTP/1.1 201 Created`
2. **Headers:** Metadata about the response.
   * *Example:*
     * `Content-Type: application/json`
     * `Cache-Control: no-store` (Tells the browser not to cache this data)
     * `Set-Cookie: session_id=xyz123` (Sets a cookie on the client)
3. **Body:** The returned data (HTML page, image, or JSON payload).

---

### 4. HTTP Methods & Their Properties

Understanding the properties of HTTP methods is a favorite topic of backend interviewers.

#### 1. Safe Methods
An HTTP method is **safe** if it does not alter the state of the server. In other words, it is a read-only operation.
* **Safe Methods:** `GET`, `HEAD`, `OPTIONS`
* **Unsafe Methods:** `POST`, `PUT`, `PATCH`, `DELETE`

#### 2. Idempotent Methods
An HTTP method is **idempotent** if making multiple identical requests has the exact same effect on the server as making a single request.
* **Idempotent Methods:** `GET`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`
* **Non-idempotent Methods:** `POST`, `PATCH`
  * *Why POST is not idempotent:* Sending `POST /api/v1/orders` three times will create three separate orders and charge the customer three times.
  * *Why PATCH is not idempotent:* If your PATCH request says `"increment_by": 5`, sending it three times increases the value by 15.

---

### 5. HTTP Headers: The Control Knobs of the Web

Headers control how clients and servers interact:
* **`Content-Type`:** Specifies the media type of the body. Common values: `application/json`, `application/x-www-form-urlencoded`, `multipart/form-data` (for file uploads).
* **`User-Agent`:** Identifies the client software (e.g., Chrome, Safari, Python-httpx).
* **`Location`:** Used in redirection (3xx) or to point to the URL of a newly created resource (201).
* **`Cache-Control`:** Directs caching behavior. E.g., `public, max-age=3600` allows caching for 1 hour.

---

### 6. Python Example: Inspecting Request Headers and Body
Here is how you access raw headers and client information in FastAPI.

```python
from fastapi import APIRouter, Request, Header

router = APIRouter()

@router.get("/api/v1/debug")
def debug_request(
    request: Request,
    user_agent: str = Header(None), # Automatically extracts the 'User-Agent' header
    x_custom_header: str = Header(None) # Automatically extracts 'X-Custom-Header'
):
    return {
        "client_host": request.client.host,
        "method": request.method,
        "url": str(request.url),
        "user_agent": user_agent,
        "custom_header": x_custom_header,
        "all_headers": dict(request.headers)
    }
```

---

### 7. Hands-on Workout & Assessment

#### Part A: API Design Challenge (Headers Design)
Suppose you are designing a file download API. The client requests a PDF invoice.
- Which HTTP method should they use?
- What `Content-Type` header should the server return?
- What header should the server use to force the browser to download the file as an attachment (e.g. `invoice_42.pdf`) instead of opening it in the browser?

#### Part B: Quiz
1. Which of the following HTTP methods is safe?
   A. POST
   B. DELETE
   C. GET
   D. PATCH
2. What does the `Content-Type` header do?
   A. It tells the server who is logged in.
   B. It specifies the format of the data in the HTTP body (e.g., JSON, HTML).
   C. It defines the caching duration.
   D. It encrypts the HTTP request.
3. Why is `PUT` considered idempotent, while `POST` is not?
   A. PUT is faster than POST.
   B. PUT completely replaces a resource at a specific URL, so repeating it has no additional effect. POST creates a new resource each time.
   C. PUT is only used for reading data.
   D. PUT requires SSL encryption.

---

### 8. Progress Tracker

* **Module 2: API Status Codes, HTTP, REST, OpenAPI:** 0%
* **Topics Completed:** 0/1
* **Coding Exercises:** 0/0
* **Quiz Score:** N/A
* **API Design Challenge Score:** N/A
* **Backend Score:** 0 / 100

---

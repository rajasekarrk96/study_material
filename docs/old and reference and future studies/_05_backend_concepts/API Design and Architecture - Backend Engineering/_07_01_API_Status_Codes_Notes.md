# Module 2: API Status Codes, HTTP, REST, OpenAPI
## Topic 7: API Status Codes & Error Handling

---

### 1. The Big Picture

#### What are HTTP Status Codes?
HTTP status codes are three-digit numbers returned by a server in response to a client's request. They serve as a standardized vocabulary to communicate the outcome of the request.

#### Why Status Codes Matter
A production API must use status codes correctly so that client applications (frontend) can react appropriately. 
* *Example:* If a client sends an expired token, and you return a `200 OK` but write `{"error": "unauthorized"}` in the body, the client's interceptor won't know to redirect the user to the login page automatically. The client expects a `401 Unauthorized` status code.

---

### 2. The Five Status Code Classes

```
┌──────┬──────────────────────────┬────────────────────────────────────────┐
│ Class│ Category                 │ Description                            │
├──────┼──────────────────────────┼────────────────────────────────────────┤
│ 1xx  │ Informational            │ Request received, continuing process.  │
│ 2xx  │ Success                  │ The action was successfully received.  │
│ 3xx  │ Redirection              │ Further action must be taken.          │
│ 4xx  │ Client Error             │ The request contains bad syntax/error. │
│ 5xx  │ Server Error             │ The server failed to fulfill request.  │
└──────┴──────────────────────────┴────────────────────────────────────────┘
```

---

### 3. Key Status Codes for REST APIs

#### 2xx Success
* **`200 OK`:** General success. Used for successful GET, PUT, or PATCH requests.
* **`201 Created`:** Successful creation. Returned by POST requests. Always include the URI of the new resource in the `Location` header.
* **`204 No Content`:** The request succeeded, but there is no body in the response. Typically returned by DELETE requests.

#### 3xx Redirection
* **`304 Not Modified`:** Used for caching. Tells the client: "The resource hasn't changed since your last request. Use your cached copy." (Saves massive bandwidth).

#### 4xx Client Errors (The client's fault)
* **`400 Bad Request`:** General validation failure. The request body is malformed or invalid.
* **`401 Unauthorized`:** The client is not authenticated. They need to log in or provide a valid API key.
* **`403 Forbidden`:** The client is authenticated but does not have permission to access the resource (e.g., a regular user trying to access `/admin`).
* **`404 Not Found`:** The requested resource does not exist.
* **`409 Conflict`:** The request could not be completed due to a conflict (e.g., trying to register an email that already exists, or edit a record that has been updated by someone else).
* **`422 Unprocessable Entity`:** The request format is correct (valid JSON), but the semantic values are invalid (e.g., age is -5). FastAPI uses this for Pydantic validation errors.

#### 5xx Server Errors (The server's fault - your bug!)
* **`500 Internal Server Error`:** The server crashed or encountered an unhandled exception. **Never** return this intentionally for user input errors.
* **`502 Bad Gateway`:** An intermediate server (like Nginx or an API Gateway) received an invalid response from the upstream application server.
* **`503 Service Unavailable`:** The server is temporarily overloaded or down for maintenance.
* **`504 Gateway Timeout`:** The upstream server took too long to respond.

---

### 4. Designing Standardized Error Responses
In production, your API should always return errors in a consistent format. The industry standard is **RFC 7807 (Problem Details for HTTP APIs)**.

#### Standard Error Body Example
```json
{
  "type": "https://api.myshop.com/errors/validation-failed",
  "title": "Your request parameters did not validate.",
  "status": 400,
  "detail": "The 'email' field must be a valid email address.",
  "instance": "/api/v1/users",
  "invalid_params": [
    {
      "name": "email",
      "reason": "Must contain an @ symbol"
    }
  ]
}
```

---

### 5. Python Example: Global Exception Handling in FastAPI
Instead of wrapping every single route handler in `try-except` blocks, write a **Global Exception Handler** in FastAPI. This catches exceptions globally and formats them consistently.

```python
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

app = FastAPI()

# Custom Exception
class EntityNotFoundException(Exception):
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

# Global Exception Handler
@app.exception_handler(EntityNotFoundException)
async def entity_not_found_handler(request: Request, exc: EntityNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "title": "Resource Not Found",
            "status": 404,
            "detail": f"{exc.name} with ID {exc.id} was not found in our records.",
            "instance": request.url.path
        }
    )
```

---

### 6. Hands-on Workout & Assessment

#### Part A: API Design Challenge (Status Codes)
For each of the following scenarios, choose the most appropriate HTTP status code:
1. A user tries to delete a product that does not exist.
2. A user tries to checkout, but their shopping cart is empty (business rule violation).
3. A user registers successfully.
4. A user tries to access a route without an Authorization header.
5. The database connection drops.

#### Part B: Quiz
1. Which status code should you return if a user tries to create an account with an email that is already taken?
   A. 400 Bad Request
   B. 409 Conflict
   C. 401 Unauthorized
   D. 422 Unprocessable Entity
2. What does a `304 Not Modified` status code tell the client?
   A. The server failed to modify the database.
   B. The client is not allowed to modify this resource.
   C. The resource has not changed since the client last fetched it; use the cached version.
   D. The URL of the resource has changed permanently.
3. What is RFC 7807?
   A. A security protocol.
   B. A standard for defining database indexes.
   C. An RFC specification for standardizing error response bodies in HTTP APIs.
   D. A method for API versioning.

---

### 7. Progress Tracker

* **Module 2: API Status Codes, HTTP, REST, OpenAPI:** 0%
* **Topics Completed:** 0/2
* **Coding Exercises:** 0/0
* **Quiz Score:** N/A
* **API Design Challenge Score:** N/A
* **Backend Score:** 0 / 100

---

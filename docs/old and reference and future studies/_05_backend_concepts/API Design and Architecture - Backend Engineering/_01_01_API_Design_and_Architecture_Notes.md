# Module 1: API Design and Architecture
## Topic 1: Introduction to APIs, Web Services, and Client-Server Architecture

---

### 1. The Big Picture

#### What is an API & Web Service?
An **API (Application Programming Interface)** is a software intermediary that allows two applications to talk to each other. It defines the inputs, outputs, data formats, and behaviors that a system exposes.
A **Web Service** is a specific type of API that is accessed over a network (typically the internet) using standard web protocols (like HTTP).

> [!IMPORTANT]
> **The Golden Rule:** All Web Services are APIs, but not all APIs are Web Services.

### Types of APIs

#### 1. By Release Policy (Access Level)
* **Private (Internal) APIs:** Exclusively used within an organization. They enable communication between different internal backend services (e.g., Netflix recommendations calling Netflix user data).
* **Partner APIs:** Shared only with authorized business partners under agreement (e.g., Ticketmaster sharing live ticket availability with Spotify).
* **Public (Open) APIs:** Available for any external developer to access and integrate with (e.g., OpenWeatherMap, Google Maps).

#### 2. By Technical Execution
* **Library / Programmatic APIs (Local):** Expose functionality directly within a coding language or platform without using a network.
  * *Example:* Python's `math` module, OS kernel APIs.
* **Web APIs / Web Services (Networked):** Require communication over a network (usually HTTP).
  * **REST (Representational State Transfer):** The industry standard utilizing standard HTTP methods and JSON formats. (See Topic 2).
  * **GraphQL:** An API query language where clients fetch exactly the fields they define.
  * **gRPC / RPC:** A high-speed, binary protocol optimized for server-to-server microservice communication.

---

### Key Concepts & Metaphors

#### 1. API: The Wall Outlet Metaphor
Think of a wall outlet:
* The power plant contains complex mechanics, generators, and grid wiring (The Backend System).
* Your phone charger requires electricity (The Client).
* You plug your charger into the **Wall Outlet (The API)**. The physical prongs and sockets form a strict "contract" (110V/220V AC). You get electricity without needing to know how the generator works.

*Local Code Example:*
```python
import math
# The math.sqrt function is a local API.
# You give it a number; it returns the square root without you writing the math logic.
result = math.sqrt(25) # Returns 5.0
```

#### 2. Web Service: The Drive-Thru Metaphor
A Web Service is specifically a network-accessed API. Think of a **Drive-Thru Window**:
* You drive up and speak into the intercom (The Client sends an HTTP Request over the network).
* The kitchen prepares your food (The Server processes the request).
* They hand the meal to you through the window (The Server returns the Response).

*Web Service Example:*
```python
import requests
# Call GitHub's Web Service over the internet using HTTP
response = requests.get("https://api.github.com/users/octocat")
print(response.json()["name"]) # Prints: "The Octocat"
```

#### 3. Client-Server Model: The Restaurant Metaphor
* **The Client (Browser/App):** You (the customer). You look at the menu (UI) and place an order. You are blocked from entering the kitchen for safety and efficiency.
* **The API / Web Service:** The Waiter. Carries your order (Request) to the kitchen and brings back your meal (Response).
* **The Server (Backend / Database):** The Kitchen. The chefs process orders, query the pantry (database), and prepare items according to the rules.

*Why use this?*
* **Security:** Clients never directly read or write to databases.
* **Maintainability:** You can rebuild the entire kitchen (migrate DBs/languages) without changing the menu the customers see.
* **Separation of Concerns:** The customer UI is independent of data storage.

#### Why Companies Use APIs
1. **Separation of Concerns:** Frontend developers can build UI/UX (React, iOS, Android) without knowing how database queries or payment processors work. Backend developers can change database schemas or business logic without breaking the frontend, as long as the API contract remains unchanged.
2. **Reusability and Integration:** Instead of building a credit card processing system, companies use Stripe's API. Instead of building maps, they use the Google Maps API.
3. **Scalability:** By decoupling the client and server, you can scale your backend servers independently of your frontend hosting (e.g., using Kubernetes or Serverless) based on API traffic.

#### Where it Fits in Backend Architecture
```
┌────────────────────────────────────────────────────────┐
│                      CLIENT LAYER                      │
│      ┌───────────┐      ┌───────────┐      ┌───────────┐│
│      │  Web App  │      │ Mobile App│      │ Third-Party││
│      │ (React/JS)│      │(iOS/Android)     │ Integrator││
│      └─────┬─────┘      └─────┬─────┘      └─────┬─────┘│
└────────────┼──────────────────┼──────────────────┼─────┘
             │                  │                  │
             ▼                  ▼                  ▼
       HTTPS Requests (JSON / REST / gRPC / GraphQL)
             │                  │                  │
┌────────────┼──────────────────┼──────────────────┼─────┐
│            ▼                  ▼                  ▼     │
│      ┌───────────────────────────────────────────────┐ │
│      │            API Gateway / Load Balancer        │ │
│      └───────────────────────┬───────────────────────┘ │
│                              │                         │
│                              ▼                         │
│                  ┌───────────────────────┐             │
│                  │  Backend API Server   │             │
│                  │ (FastAPI / Spring)    │             │
│                  └───────────┬───────────┘             │
│                              │                         │
│                              ▼                         │
│                  ┌───────────────────────┐             │
│                  │    Database / Cache   │             │
│                  └───────────────────────┘             │
│                     BACKEND LAYER                      │
└────────────────────────────────────────────────────────┘
```

#### Common Interview Questions
* **"What is the difference between an API and a Web Service?"**
  * *Answer:* An API is any interface that lets software communicate. A Web Service is an API that communicates over a network using web protocols (like HTTP/HTTPS).
* **"Why do we prefer JSON over XML in modern APIs?"**
  * *Answer:* JSON is lightweight, has less syntax overhead (saving bandwidth), and parses natively into JavaScript objects, making it highly efficient for web clients. XML is verbose and requires complex DOM parsing.
* **"What is the client-server model, and what are its main advantages?"**
  * *Answer:* It's an architectural pattern that separates the user interface (client) from data storage and business logic (server). It enables independent scaling, security control (hiding DBs behind servers), and platform independence.

#### Common Mistakes
* **Leaking Database Internals:** Directly exposing database models (like returning a SQLAlchemy or Hibernate entity) in the API response. This leaks sensitive fields (like password hashes) and couples the database schema to the API contract.
* **Ignoring Network Latency:** Assuming network calls are instantaneous. Designing "chatty" APIs where a client must make 10 API calls to render a single page instead of one structured call.
* **Lack of Request Validation:** Trusting the client's input. A production API must validate every byte of incoming data before processing it.

---

### 2. Lesson Objectives
By the end of this lesson, you will:
1. Understand the exact distinction between APIs, Web Services, and the Client-Server model.
2. Master the design of a basic HTTP Request/Response flow.
3. Contrast beginner-level ("script-like") API code with production-ready, enterprise-grade architecture in both Python (FastAPI) and Java (Spring Boot).
4. Initiate our **Enterprise E-Commerce API** project by setting up its directory structure and its first module (Users).

---

### 3. Detailed Explanation & Core Concepts

#### 1. Client-Server Architecture
The client makes a **Request**; the server processes it and sends back a **Response**.
* **Client (Frontend):** The solicitor. It collects user input, formats it, sends it via HTTP, and renders the response. It does *not* connect to the database.
* **Server (Backend):** The gatekeeper and executor. It receives the request, validates it, authenticates the client, runs business logic, interacts with databases/caches, and returns data in a standard format (usually JSON).

#### 2. Protocol & Communication (HTTP)
Web services use **HTTP (Hypertext Transfer Protocol)**.
* **Statelessness:** The server does not keep memory of past requests by default. Each request must contain all the information needed to understand and process it (e.g., authentication tokens).
* **HTTP Methods (Verbs):** 
  * `GET`: Retrieve data (Safe & Idempotent).
  * `POST`: Create data (Not Idempotent).
  * `PUT`: Replace data (Idempotent).
  * `PATCH`: Partially update data (Not Idempotent).
  * `DELETE`: Remove data (Idempotent).

#### 3. Data Serialization
* **Serialization:** Turning an in-memory object (e.g., a Python dictionary or Java Class instance) into a string/byte format (like JSON) that can be sent over the network.
* **Deserialization:** Turning an incoming string/byte stream (JSON) back into an in-memory object that the programming language can manipulate.

---

### 4. Real-world Examples
Imagine ordering food at a restaurant:
1. **Client:** You (the customer). You look at the menu (UI) and decide what you want.
2. **API (The Waiter):** Takes your order (Request), carries it to the kitchen (Server), and returns with your food (Response). You don't know *how* the kitchen cooked the food, what ingredients they used, or who washed the dishes. You only care that the food matches what you ordered.
3. **Server:** The kitchen. They prepare the food based on the order. If you ask for something not on the menu, they return an error ("We don't serve that").

---

### 5. Code Comparison: FastAPI (Python)

Let's look at how a junior developer writes a FastAPI endpoint versus how it is designed in an enterprise environment.

#### A. Beginner Code (`main.py`)
```python
from fastapi import FastAPI

app = FastAPI()

# Database mock
users_db = []

@app.post("/create-user")
def create_user(name: str, email: str, password: str):
    # BAD: Directly accepting raw query parameters
    # BAD: No email validation, no password hashing, no structured response
    new_user = {"name": name, "email": email, "password": password}
    users_db.append(new_user)
    return new_user # BAD: Exposing the raw password back to the client!
```

#### Why the Beginner Code is Bad:
1. **Data Exposure:** Returns the plain text password in the response.
2. **No Input Validation:** Anyone can pass an invalid email (e.g., "not-an-email") or an empty string.
3. **Tight Coupling:** No separation of layers. The route handler handles database operations directly.
4. **Poor Routing:** Uses `/create-user` (RPC style) instead of RESTful nouns `/users` with a `POST` method.

#### B. Production Code (Enterprise Structure)
In production, we separate our concerns into:
1. **Schemas (DTOs):** Define input and output structures using Pydantic.
2. **Routers:** Define the HTTP endpoints.
3. **Services:** Contain business logic.
4. **Models:** Define database schemas.

##### 1. The Schema (`schemas.py`)
```python
from pydantic import BaseModel, EmailStr, Field

# Input schema (Request Body)
class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, example="John Doe")
    email: EmailStr
    password: str = Field(..., min_length=8, description="Must be at least 8 characters")

# Output schema (Response Body) - Prevents password leakage!
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True # Allows compatibility with ORMs (SQLAlchemy)
```

##### 2. The Router (`routers/users.py`)
```python
from fastapi import APIRouter, status, HTTPException
from schemas import UserCreate, UserResponse

router = APIRouter(prefix="/api/v1/users", tags=["Users"])

# Simulated Database
USERS_DB = []
current_id = 1

@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserCreate):
    global current_id
    
    # 1. Business Logic / Validation (e.g., check if email exists)
    for u in USERS_DB:
        if u["email"] == user_in.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
            
    # 2. Process data (In production, hash password here!)
    hashed_password = f"hashed_{user_in.password}" # Mock hash
    
    new_user = {
        "id": current_id,
        "name": user_in.name,
        "email": user_in.email,
        "password": hashed_password
    }
    
    USERS_DB.append(new_user)
    current_id += 1
    
    # 3. Return response (FastAPI automatically filters using UserResponse)
    return new_user
```

---

### 6. Code Comparison: Spring Boot (Java)

For backend engineers, it is crucial to understand multiple stacks. Let’s compare how Java handles the same client-server flow.

#### A. Beginner Code
```java
@RestController
public class UserController {
    private List<Map<String, String>> users = new ArrayList<>();

    @PostMapping("/createUser")
    public Map<String, String> createUser(@RequestParam String name, @RequestParam String email, @RequestParam String password) {
        Map<String, String> user = new HashMap<>();
        user.put("name", name);
        user.put("email", email);
        user.put("password", password); // BAD: Raw password
        users.add(user);
        return user; // BAD: Exposing password
    }
}
```

#### B. Production Code (Enterprise Structure)

##### 1. DTO (Data Transfer Object)
```java
public class UserCreateDTO {
    @NotBlank(message = "Name cannot be blank")
    @Size(min = 2, max = 50)
    private String name;

    @Email(message = "Invalid email format")
    @NotBlank
    private String email;

    @Size(min = 8, message = "Password must be at least 8 characters")
    private String password;
    
    // Getters and Setters
}

public class UserResponseDTO {
    private Long id;
    private String name;
    private String email;
    
    // Getters and Setters
}
```

##### 2. Controller
```java
@RestController
@RequestMapping("/api/v1/users")
public class UserController {

    @Autowired
    private UserService userService;

    @PostMapping
    public ResponseEntity<UserResponseDTO> createUser(@Valid @RequestBody UserCreateDTO userCreateDTO) {
        UserResponseDTO response = userService.createUser(userCreateDTO);
        return new ResponseEntity<>(response, HttpStatus.CREATED);
    }
}
```

---

### 7. Professional Notes

#### Key Definitions
* **API Contract:** An agreement between client and server specifying how requests must look and what responses will be returned. Changes to this contract are "breaking changes" and must be avoided or versioned (e.g., `/v1/` to `/v2/`).
* **Idempotency:** A property of an API operation where making the same request multiple times has the same effect as making it once. `GET`, `PUT`, and `DELETE` are idempotent. `POST` is not (calling it twice creates two resources).
* **Payload:** The actual data transmitted in an HTTP message body (excluding headers).

#### Best Practices
1. **Use HTTP Status Codes Correctly:** 
   * `200 OK` for successful GET/PUT.
   * `201 Created` for successful POST.
   * `400 Bad Request` for validation failures.
   * `401 Unauthorized` for missing/invalid credentials.
   * `403 Forbidden` when authenticated but lacking permissions.
   * `404 Not Found` when a resource doesn't exist.
   * `500 Internal Server Error` only when the server crashes (never return this for user validation errors!).
2. **Never Expose Raw Entities:** Always map database entities to DTOs/Schemas before sending them back to the client.
3. **Validate All Inputs:** Use libraries like Pydantic (FastAPI) or Hibernate Validator (Spring Boot) to enforce rules.

---

### 8. Cheat Sheet

| HTTP Method | Path | Request Body | Status Code (Success) | Idempotent? |
| :--- | :--- | :--- | :--- | :--- |
| **GET** | `/api/v1/users` | No | `200 OK` | Yes |
| **GET** | `/api/v1/users/{id}` | No | `200 OK` | Yes |
| **POST** | `/api/v1/users` | Yes (UserCreate) | `201 Created` | No |
| **PUT** | `/api/v1/users/{id}` | Yes (UserReplace) | `200 OK` | Yes |
| **DELETE**| `/api/v1/users/{id}` | No | `204 No Content` | Yes |

---

### 9. Project Kickoff: Enterprise E-Commerce API
We will build a production-ready e-commerce API. Let's create the base folder structure for our workspace.

```
ecommerce_api/
│
├── app/
│   ├── __init__.py
│   ├── main.py                # Application entrypoint
│   │
│   ├── core/                  # Configuration, Security, Databases
│   │   ├── config.py
│   │   └── database.py
│   │
│   ├── modules/               # Domain-driven modules
│   │   ├── users/
│   │   │   ├── __init__.py
│   │   │   ├── router.py
│   │   │   ├── schemas.py
│   │   │   ├── models.py
│   │   │   └── service.py
│   │   │
│   │   └── products/          # Future module
│   │
│   └── tests/                 # Pytest test suite
│
├── requirements.txt           # Python dependencies
└── Dockerfile                 # Containerization
```

---

### 10. Hands-on Workout & Assessment

#### Part A: Coding Exercise
I want you to implement the very first endpoint of our E-Commerce API: **User Registration**. 
Create the file structure inside `c:\Users\rajas\OneDrive\_00_a_study\_05_backend_concepts\API Design and Architecture - Backend Engineering\ecommerce_api` and write the code for:
1. `app/modules/users/schemas.py` containing `UserCreate` and `UserResponse` Pydantic models.
2. `app/modules/users/router.py` containing the `POST` route for creating a user.
3. `app/main.py` which instantiates the FastAPI app and includes the router.

*Note: For now, you can use an in-memory list `USERS_DB = []` inside your router or service.*

#### Part B: API Design Challenge
Design the API endpoints (methods and paths) for an **Inventory Management** system. The system needs to support:
1. Creating a new inventory item.
2. Viewing a specific item's stock level.
3. Increasing/decreasing the stock of an item.
4. Archiving an item (deleting it from active view but keeping it in the database).

Write your proposed paths, HTTP methods, and status codes.

#### Part C: Quiz
##### 1. Multiple Choice Questions (10)
1. Which of the following is true about APIs and Web Services?
   A. Every API is a Web Service.
   B. Every Web Service is an API.
   C. Web Services do not use HTTP.
   D. APIs must always run over a network.
2. What HTTP status code should be returned when a client successfully creates a new resource?
   A. 200 OK
   B. 202 Accepted
   C. 201 Created
   D. 204 No Content
3. Which HTTP method is considered NOT idempotent?
   A. GET
   B. POST
   C. PUT
   D. DELETE
4. What is the primary purpose of a Data Transfer Object (DTO) / Schema?
   A. To connect directly to the database.
   B. To define the styling of the frontend.
   C. To decouple the internal data models from the external API contract.
   D. To speed up database queries.
5. What does it mean for an API to be "stateless"?
   A. The server does not store any data in a database.
   B. The client must re-authenticate on every single request.
   C. The server treats each request as an independent transaction, containing all necessary context.
   D. The API can only be accessed from one country.
6. Which of the following is a security risk of returning raw database entities from an API?
   A. SQL injection.
   B. Leaking internal implementation details or sensitive fields (like password hashes).
   C. Increasing database CPU usage.
   D. Causing the server to run out of memory.
7. What is the main difference between PUT and PATCH?
   A. PUT is for creating, PATCH is for updating.
   B. PUT is idempotent, PATCH is not.
   C. PUT replaces the entire resource, while PATCH applies a partial update.
   D. PUT does not require a request body, while PATCH does.
8. If a client sends a request with an invalid email format (e.g. "admin@"), which HTTP status code is most appropriate?
   A. 401 Unauthorized
   B. 403 Forbidden
   C. 404 Not Found
   D. 400 Bad Request
9. Which layer of a clean architecture should contain the core business rules and calculations?
   A. Router/Controller Layer
   B. Service/Domain Layer
   C. Database/Repository Layer
   D. Frontend Layer
10. Why is HTTP 500 Internal Server Error bad to return for client input validation failures?
    A. It tells the client that their input was correct.
    B. It indicates a failure on the server's side (bug or crash), triggering false alarms in monitoring systems.
    C. It is slower than returning a 400 Bad Request.
    D. It prevents the database from saving the data.

##### 2. True / False (5)
1. An API is restricted only to web-based communication. (True/False)
2. Sending a GET request should never modify data on the server. (True/False)
3. Using `response_model` in FastAPI helps prevent returning sensitive data. (True/False)
4. A REST API must always use XML. (True/False)
5. Idempotency means that executing an operation multiple times will produce different side-effects each time. (True/False)

##### 3. Fill in the Blanks (5)
1. Turning an in-memory programming language object into a network-transferable format like JSON is called ________.
2. The HTTP method used to completely replace a resource is ________.
3. The Pydantic field parameter used to validate that a string has a minimum length is ________.
4. The HTTP status code `403` stands for ________.
5. The architectural pattern that separates the presentation layer from the data management layer is called the ________-________ model.

##### 4. Debugging Question
Look at this FastAPI code. Identify **three** critical bugs/anti-patterns and explain how to fix them:
```python
@app.post("/users/update")
def update_user(id: int, status: str):
    user = db.get_user(id)
    if not user:
        return {"error": "not found"}
    user.status = status
    db.save(user)
    return user
```


---

### 10. Live Study Q&A & Clarifications

#### Q: What is the difference between REST, SOAP, GraphQL, and gRPC, and why do we have so many different API types?
**Answer:**
We have multiple API protocols because different software systems have conflicting needs (e.g., a bank values strict transaction checks, while a microservice values raw speed).

* **SOAP:** A strict, XML-only protocol. Ideal for banks/legacy systems because of built-in security contracts (WS-Security), but too heavy/slow for modern web apps.
* **REST:** A flexible architectural style that uses HTTP and lightweight JSON. The default standard for public APIs and standard web applications.
* **GraphQL:** A query language allowing the client to request exactly the fields they need in a single call, preventing "over-fetching" (receiving too much data) and "under-fetching" (having to make multiple calls).
* **gRPC:** A binary-serialization protocol (Protocol Buffers) running on HTTP/2. Optimized for ultra-fast internal microservice-to-microservice communication, but not directly usable by web browsers.

| Feature | SOAP | REST | GraphQL | gRPC |
| :--- | :--- | :--- | :--- | :--- |
| **Data Format** | XML | JSON / XML | JSON | Binary (Protobuf) |
| **Speed** | Slow (Heavy payload) | Fast | Very Fast | Lightning Fast |
| **Best For** | Banking / Legacy | General Web APIs | Complex UIs / Dashboards | Internal Microservices |

---

### 11. Flashcards

1. **Q:** What is an API?
   **A:** An Application Programming Interface; a set of protocols and tools that allows different software applications to communicate with each other.
2. **Q:** What is a Web Service?
   **A:** An API that is accessed over a network using web protocols (like HTTP).
3. **Q:** What is the Client-Server model?
   **A:** An architectural model where a client requests resources or services, and a server provides them, separating user interface concerns from data management.
4. **Q:** What does statelessness mean in HTTP?
   **A:** The server does not store any session state about the client. Every request must contain all the information necessary to process it.
5. **Q:** What is the difference between serialization and deserialization?
   **A:** Serialization converts in-memory objects into a format like JSON for transmission. Deserialization converts that format back into in-memory objects.

---

### 12. Progress Tracker

* **Module 1: API Design and Architecture:** 0% (Waiting for Topic 1 completion)
* **Videos Completed:** 0/1
* **Coding Exercises:** 0/1
* **Quiz Score:** N/A (Waiting for submission)
* **API Design Challenge Score:** N/A (Waiting for submission)
* **Backend Score:** 0 / 100

---

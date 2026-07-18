# Module 1: API Design and Architecture
## Topic 3: API Architecture, Layered Patterns, and Dependency Injection

---

### 1. The Big Picture

#### What is API Architecture?
API Architecture is the structural design of your backend application. As a junior, it is tempting to put all your routes, database queries, and business logic into a single `main.py` file. In an enterprise environment, this is a recipe for disaster. 

Professional backend codebases are structured using **Architectural Patterns** to ensure:
* **Maintainability:** Changing how database queries are run shouldn't require changing your HTTP route handlers.
* **Testability:** You must be able to test your business logic without connecting to a real database.
* **Scalability:** Multiple developers must be able to work on different parts of the system (e.g., database vs. routes) without merge conflicts.

#### The Layered (Three-Tier) Architecture
The industry standard for structuring backend applications is the **Three-Tier/Layered Architecture**:

```
┌────────────────────────────────────────────────────────┐
│                   PRESENTATION LAYER                   │
│        (Routers, Controllers, Schemas/DTOs)            │
│   - Receives HTTP requests                             │
│   - Validates input (Pydantic / Hibernate)             │
│   - Returns HTTP responses & status codes              │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼ (Calls Service)
┌────────────────────────────────────────────────────────┐
│                  BUSINESS LOGIC LAYER                  │
│                     (Service Layer)                    │
│   - Executes core business rules and calculations      │
│   - Coordinates transactions                           │
│   - Completely unaware of HTTP (no request/response)   │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼ (Calls Repository)
┌────────────────────────────────────────────────────────┐
│                   DATA ACCESS LAYER                    │
│             (Repository / Data Access Object)          │
│   - Performs raw database queries (SQLAlchemy/SQL)     │
│   - Reads/writes to database or cache                  │
│   - Completely unaware of business rules               │
└────────────────────────────────────────────────────────┘
```

#### What is Dependency Injection (DI)?
**Dependency Injection** is a design pattern in which an object or function receives other objects that it depends on (its dependencies), rather than creating them itself.
* *Without DI:* Class A creates an instance of Class B inside its constructor. Class A is now tightly coupled to Class B. If you want to test Class A, you are forced to run Class B as well.
* *With DI:* Class A is handed (injected with) an instance of Class B. You can easily inject a "Mock B" during testing.

---

### 2. Lesson Objectives
By the end of this lesson, you will:
1. Understand the responsibilities of the Presentation, Service, and Repository layers.
2. Master the **Repository Pattern** to abstract database operations.
3. Implement **Dependency Injection** in FastAPI using the `Depends` system.
4. Refactor our **Enterprise E-Commerce API** into a clean, layered architecture.

---

### 3. Detailed Explanation & Core Concepts

#### 1. Layer Responsibilities
* **Router/Controller:** *The Receptionist.* Its only job is to greet the client, verify they brought the right paperwork (validation), hand the paperwork to the manager (Service), and return the manager's response with a stamp (HTTP Status Code).
* **Service:** *The Manager.* The brain of the application. It decides *what* to do. E.g., "If the user is registering, check if the email exists, hash their password, create their account, and send a welcome email."
* **Repository:** *The Clerk.* Its only job is to fetch or save records from the file cabinet (Database). It does not care *why* it is fetching the data.

#### 2. The Repository Pattern
The Repository Pattern mediates between the domain and data mapping layers using a collection-like interface for accessing domain objects. 
* **Why?** If you decide to migrate from PostgreSQL to MongoDB, you only need to rewrite your Repository classes. Your Service classes and Routers remain completely untouched.

#### 3. SOLID Principles in API Design
* **Single Responsibility Principle (SRP):** A class/file should have only one reason to change. The router only changes if the HTTP contract changes. The service only changes if the business rules change.
* **Dependency Inversion Principle (DIP):** High-level modules should not depend on low-level modules; both should depend on abstractions. (e.g., Services depend on Repository interfaces, not concrete SQL connections).

---

### 4. Code Comparison: FastAPI (Python)

Let's see how a junior developer couples code compared to a production-grade layered implementation.

#### A. Beginner Code (Tightly Coupled)
```python
from fastapi import FastAPI, HTTPException
import psycopg2 # Direct database dependency

app = FastAPI()

@app.post("/users")
def create_user(name: str, email: str):
    # 1. Database Connection (Low-level detail in presentation layer!)
    conn = psycopg2.connect("dbname=test user=postgres")
    cur = conn.cursor()
    
    # 2. Business Logic & Query mixed together
    cur.execute("SELECT id FROM users WHERE email = %s", (email,))
    if cur.fetchone():
        raise HTTPException(status_code=400, detail="Email exists")
        
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id", (name, email))
    user_id = cur.fetchone()[0]
    conn.commit()
    
    return {"id": user_id, "name": name, "email": email}
```

#### B. Production Code (Layered & Decoupled)

##### 1. The Repository Layer (`repository.py`)
```python
from typing import List, Optional

# Concrete Repository (In-memory mock for now, can be swapped with SQLAlchemy later)
class UserRepository:
    def __init__(self):
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
```

##### 2. The Service Layer (`service.py`)
```python
from typing import Optional
from repository import UserRepository

class UserService:
    # Dependency Injection: We inject the UserRepository
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register_user(self, name: str, email: str, password_raw: str) -> dict:
        # 1. Business Logic: Check duplicate
        existing_user = self.user_repo.get_by_email(email)
        if existing_user:
            raise ValueError("Email already registered")
            
        # 2. Business Logic: Hash password
        hashed_password = f"secure_hash_{password_raw}"
        
        # 3. Data Access
        return self.user_repo.create(name, email, hashed_password)
```

##### 3. The Presentation Layer (`router.py`)
```python
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from repository import UserRepository
from service import UserService

router = APIRouter(prefix="/api/v1/users", tags=["Users"])

# --- DEPENDENCY INJECTION SETUP ---
# We create singletons or factory functions to supply our dependencies.
_user_repo = UserRepository()

def get_user_service() -> UserService:
    return UserService(user_repo=_user_repo)

# --- SCHEMAS ---
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

# --- ROUTE ---
@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    user_in: UserCreate, 
    user_service: UserService = Depends(get_user_service) # FastAPI Dependency Injection
):
    try:
        # The router does not know HOW to hash passwords or check duplicate emails.
        # It simply delegates to the Service.
        new_user = user_service.register_user(
            name=user_in.name,
            email=user_in.email,
            password_raw=user_in.password
        )
        return new_user
    except ValueError as e:
        # Service throws a domain exception; router converts it to HTTP Exception
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
```

---

### 5. Code Comparison: Spring Boot (Java)

Spring Boot is built entirely around Dependency Injection using its **Application Context** (Inversion of Control container).

```java
// 1. DATA ACCESS LAYER (Repository)
@Repository
public interface UserRepository extends JpaRepository<UserEntity, Long> {
    Optional<UserEntity> findByEmail(String email);
}

// 2. BUSINESS LOGIC LAYER (Service)
@Service
public class UserService {
    
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    // Constructor Injection (Best Practice)
    public UserService(UserRepository userRepository, PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }

    public UserResponseDTO registerUser(UserCreateDTO dto) {
        if (userRepository.findByEmail(dto.getEmail()).isPresent()) {
            throw new BadRequestException("Email already registered");
        }
        UserEntity entity = new UserEntity();
        entity.setName(dto.getName());
        entity.setEmail(dto.getEmail());
        entity.setPasswordHash(passwordEncoder.encode(dto.getPassword()));
        
        UserEntity saved = userRepository.save(entity);
        return convertToDTO(saved);
    }
}

// 3. PRESENTATION LAYER (Controller)
@RestController
@RequestMapping("/api/v1/users")
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @PostMapping
    public ResponseEntity<UserResponseDTO> createUser(@Valid @RequestBody UserCreateDTO dto) {
        return new ResponseEntity<>(userService.registerUser(dto), HttpStatus.CREATED);
    }
}
```

---

### 6. Professional Notes

#### Why Constructor Injection is Best Practice
In Spring Boot or plain Python, you should always prefer injecting dependencies through the constructor (`__init__`) rather than using field injection (like `@Autowired` on fields or global variables).
* **Easy Testing:** You can instantiate the service in a unit test by simply passing a mock repository to the constructor: `service = UserService(mock_repo)`. No complex framework setup required.
* **Immutability:** Dependencies can be marked as final/read-only, ensuring they are not modified after initialization.

---

### 7. Hands-on Workout & Assessment

#### Part A: Coding Exercise
Refactor your **Enterprise E-Commerce API** in `c:\Users\rajas\OneDrive\_00_a_study\_05_backend_concepts\API Design and Architecture - Backend Engineering\ecommerce_api` to use this Layered Architecture:
1. Move your in-memory database storage into a `UserRepository` in `app/modules/users/repository.py`.
2. Implement a `UserService` in `app/modules/users/service.py` that accepts the `UserRepository` in its constructor.
3. Update `app/modules/users/router.py` to inject the `UserService` using FastAPI's `Depends`.
4. Do the same for the **Products** module! Create `ProductRepository` and `ProductService`.

#### Part B: Architecture Challenge
Suppose you are designing an **Order Processing** system. When an order is placed, the system must:
1. Deduct inventory stock.
2. Charge the customer's credit card via Stripe.
3. Create an order record in the database.
4. Send an email confirmation.

Describe:
- Which layer (Router, Service, or Repository) should coordinate these 4 steps?
- Why it belongs in that layer.
- How you would use Dependency Injection to ensure this system is testable without charging real credit cards or sending real emails.

#### Part C: Quiz
##### 1. Multiple Choice Questions (10)
1. Which layer of the Three-Tier Architecture is responsible for parsing HTTP request bodies?
   A. Service Layer
   B. Presentation Layer
   C. Repository Layer
   D. Database Layer
2. What is the primary benefit of Dependency Injection?
   A. It makes the application run faster.
   B. It decouples components, making them easier to test and maintain.
   C. It automatically secures the database.
   D. It eliminates the need for writing SQL queries.
3. In a layered architecture, which of the following is a violation of the dependency rule?
   A. The Router calling the Service.
   B. The Service calling the Repository.
   C. The Repository calling the Service.
   D. The Repository calling the Database.
4. Why should business logic NOT be placed in the Router?
   A. Routers are not capable of executing Python math operations.
   B. It makes it impossible to reuse that business logic in other interfaces (like a CLI tool or a Cron job) and makes testing difficult.
   C. Routers can only return JSON.
   D. It causes database connection leaks.
5. The Repository Pattern is used to abstract:
   A. The HTTP protocol.
   B. Data storage and retrieval operations.
   C. User authentication.
   D. HTML rendering.
6. What FastAPI function is used to declare and resolve dependencies?
   A. `Inject`
   B. `Depends`
   C. `Autowired`
   D. `Required`
7. In unit testing, what is a "mock"?
   A. A copy of the production database.
   B. A lightweight, simulated object that mimics the behavior of a real dependency.
   C. A tool that checks for syntax errors.
   D. An encrypted password.
8. Which SOLID principle states that "high-level modules should not depend on low-level modules; both should depend on abstractions"?
   A. Single Responsibility Principle (SRP)
   B. Open/Closed Principle (OCP)
   C. Liskov Substitution Principle (LSP)
   D. Dependency Inversion Principle (DIP)
9. Which layer of our architecture should throw an `HTTPException`?
   A. Repository Layer
   B. Service Layer
   C. Presentation (Router) Layer
   D. Database Layer
10. Why is constructor injection preferred over field injection?
    A. It requires fewer lines of code.
    B. It allows classes to be instantiated easily in unit tests without starting a framework container.
    C. It speeds up database queries.
    D. It is only supported in Python.

##### 2. True / False (5)
1. The Service Layer should contain code that directly imports and executes SQL queries. (True/False)
2. Dependency Injection requires you to use a third-party framework; it cannot be done manually. (True/False)
3. Under the Single Responsibility Principle, a class should only have one reason to change. (True/False)
4. The Repository layer should be completely unaware of HTTP requests and responses. (True/False)
5. Injecting dependencies makes unit testing harder because you have to write more boilerplate code. (True/False)

##### 3. Fill in the Blanks (5)
1. The architectural layer responsible for executing core business rules is the ________ layer.
2. In FastAPI, we use the ________ function to inject services into our route functions.
3. The design pattern that abstracts data access behind a collection-like interface is the ________ pattern.
4. A class that depends on an interface rather than a concrete implementation is adhering to the Dependency ________ Principle.
5. The abbreviation SRP stands for ________ ________ Principle.

##### 4. Debugging Question
Identify the architectural violation in this Service class and explain how to fix it:
```python
from fastapi import HTTPException, status
import psycopg2

class ProductService:
    def get_product_price(self, product_id: int):
        conn = psycopg2.connect("dbname=shop")
        cur = conn.cursor()
        cur.execute("SELECT price FROM products WHERE id = %s", (product_id,))
        row = cur.fetchone()
        if not row:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        return row[0]
```

---

### 8. Flashcards

1. **Q:** What is Layered Architecture?
   **A:** A design pattern that organizes code into horizontal layers (Presentation, Service, Data Access), where each layer has a distinct responsibility.
2. **Q:** What is the Service Layer?
   **A:** The layer that contains business logic and orchestrates the application's workflows.
3. **Q:** What is the Repository Layer?
   **A:** The layer responsible for data access, abstracting database-specific operations from the rest of the application.
4. **Q:** Why do we use Dependency Injection?
   **A:** To decouple components, making code more modular, maintainable, and easier to test via mocking.
5. **Q:** What is the difference between a domain exception and an HTTP exception?
   **A:** A domain exception (e.g., ValueError) is raised by business logic, independent of transport. An HTTP exception (e.g., HTTPException) is raised in the presentation layer to map that error to an HTTP response code.

---

### 9. Progress Tracker

* **Module 1: API Design and Architecture:** 0%
* **Topics Completed:** 0/3
* **Coding Exercises:** 0/3
* **Quiz Score:** N/A
* **API Design Challenge Score:** N/A
* **Backend Score:** 0 / 100

---

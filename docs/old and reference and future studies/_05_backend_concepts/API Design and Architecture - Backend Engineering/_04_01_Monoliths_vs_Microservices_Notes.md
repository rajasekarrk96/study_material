# Module 1: API Design and Architecture
## Topic 4: Monoliths vs. Microservices & API Gateways

---

### 1. The Big Picture

When building an enterprise backend, one of the most fundamental architectural decisions is choosing between a **Monolithic Architecture** and a **Microservices Architecture**.

```
    MONOLITHIC ARCHITECTURE                    MICROSERVICES ARCHITECTURE

 ┌───────────────────────────┐             ┌──────────────┐      ┌──────────────┐
 │   Single Application      │             │ User Service │      │Order Service │
 │  ┌─────────────────────┐  │             │ (FastAPI)    │      │ (Spring Boot)│
 │  │    User Module      │  │             └──────┬───────┘      └──────┬───────┘
 │  ├─────────────────────┤  │                    │                     │
 │  │    Order Module     │  │                    │  ┌──────────────┐   │
 │  ├─────────────────────┤  │                    └──┤ API Gateway  │◄──┘
 │  │   Payment Module    │  │                       └──────▲───────┘
 │  └─────────────────────┘  │                              │
 └─────────────┬─────────────┘                              │
               ▼                                            ▼
       [Single Database]                       [Decoupled Databases]
                                           ┌──────────────┐      ┌──────────────┐
                                           │  User DB     │      │  Order DB    │
                                           │ (PostgreSQL) │      │ (MongoDB)    │
                                           └──────────────┘      └──────────────┘
```

#### What is a Monolith?
A **Monolith** is a software system where all components—user management, product catalog, ordering, payment processing—are built, deployed, and run as a single, unified codebase and process.

#### What are Microservices?
A **Microservices Architecture** structures an application as a collection of small, autonomous services. Each service is self-contained, models a specific business domain (e.g., Inventory, Payments), has its own database (Database-per-Service pattern), and communicates with other services via lightweight protocols (REST, gRPC, or Message Brokers like RabbitMQ/Kafka).

---

### 2. Comparison: Monolith vs. Microservices

| Feature | Monolith | Microservices |
| :--- | :--- | :--- |
| **Development** | Simple. Single repository, easy to refactor and navigate. | Complex. Multiple repositories, requires API contracts. |
| **Deployment** | All-or-nothing. A 1-line bug in payments can crash the whole app. | Independent. Can deploy the Catalog service without touching Payments. |
| **Scaling** | Scale the whole app. Heavy memory consumption. | Fine-grained. Scale only the high-traffic services (e.g., Catalog). |
| **Tech Stack** | Single tech stack (e.g., all Python or all Java). | Polyglot. Python for ML, Go for high-speed APIs, Java for legacy. |
| **Data Integrity** | Easy. Local ACID transactions across tables. | Hard. Distributed transactions (requires Saga pattern or Outbox pattern). |
| **Complexity** | Low operational overhead. | High. Requires CI/CD, service mesh, central logging, and monitoring. |

---

### 3. Core Microservices Patterns

#### 1. Database per Service
In microservices, services **must never** access another service's database directly. Doing so couples the services at the database level, defeating the purpose of microservices. If the Order Service needs user data, it must ask the User Service via an API call.

#### 2. The API Gateway
Instead of clients making requests to 20 different microservices (each with its own IP and port), clients talk to a single entrypoint: the **API Gateway**.
* **Responsibilities:**
  * **Routing:** Directs `/api/v1/users` to the User Service and `/api/v1/orders` to the Order Service.
  * **Authentication:** Validates JWT tokens once at the gateway so individual services don't have to.
  * **Rate Limiting:** Prevents DDoS attacks.
  * **Load Balancing:** Distributes requests evenly across service instances.

#### 3. Inter-Service Communication
* **Synchronous (Request-Response):**
  * **REST (HTTP/JSON):** Simple, but high payload size and latency.
  * **gRPC (HTTP/2 / Protobuf):** Extremely fast, binary serialization, strongly typed. Ideal for internal service-to-service communication.
* **Asynchronous (Event-Driven):**
  * **Message Brokers (RabbitMQ, Apache Kafka):** Service A publishes an event ("OrderPlaced"); Service B listens and processes it ("DeductInventory"). Excellent for decoupling and resilience.

---

### 4. Real-World E-Commerce Example
Imagine a Black Friday sale:
1. **Traffic spike:** 99% of users are browsing products; only 1% are checking out.
2. **Monolith:** You must scale the entire monolith, including the payment and user modules, consuming massive server resources.
3. **Microservices:** You scale up 50 instances of the **Product Catalog Service** and keep only 2 instances of the **Payment Service** running. This saves thousands of dollars in cloud hosting costs.

---

### 5. Python Example: Inter-Service Communication
Here is how the **Order Service** calls the **User Service** synchronously using `httpx` to verify a user exists before creating an order.

```python
import httpx
from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/api/v1/orders")

USER_SERVICE_URL = "http://user-service:8000/api/v1/users"

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_order(user_id: int, product_id: int, quantity: int):
    # 1. Communicate with User Service to verify user
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{USER_SERVICE_URL}/{user_id}")
            if response.status_code == 404:
                raise HTTPException(status_code=400, detail="User does not exist")
            elif response.status_code != 200:
                raise HTTPException(status_code=502, detail="User service error")
        except httpx.RequestError:
            raise HTTPException(status_code=503, detail="User service unavailable")
            
    # 2. Proceed with order creation logic...
    return {"message": "Order created successfully", "user_id": user_id}
```

---

### 6. Professional Notes: When NOT to use Microservices
**Do not start with microservices.** This is a massive industry mistake (often called "Resume-Driven Development"). 
* **The Monolith First Rule:** Almost every successful company (including Shopify, Basecamp, and even early Netflix/Amazon) started with a monolith. Build a monolith first. Once your domain boundaries are clear and you have scaling issues on specific modules, split those modules out into microservices.

---

### 7. Hands-on Workout & Assessment

#### Part A: API Design Challenge (Inter-Service Design)
Design the communication flow for a **Payment Processing** event. When a user checks out:
1. The **Order Service** receives the request.
2. The **Payment Service** needs to charge the card.
3. The **Inventory Service** needs to reserve the items.
4. The **Notification Service** needs to send an email.

Write a short paragraph explaining:
- Would you design this using synchronous REST calls or asynchronous event-driven messages (e.g., Kafka/RabbitMQ)? Why?

#### Part B: Quiz
1. What is the "Database-per-Service" pattern?
   A. Every developer gets their own database.
   B. Each microservice has its own database, and other services cannot access it directly.
   C. All microservices share a single database but use different tables.
   D. A database that automatically creates microservices.
2. Which of the following is a responsibility of an API Gateway?
   A. Running database migrations.
   B. Hashing passwords.
   C. Routing, Rate Limiting, and Centralized Authentication.
   D. Writing unit tests.
3. If Service A needs to notify Service B about an event without waiting for a response, which communication pattern is best?
   A. Synchronous REST
   B. gRPC
   C. Asynchronous Message Broker (e.g. RabbitMQ)
   D. Direct SQL database connection

---

### 8. Progress Tracker

* **Module 1: API Design and Architecture:** 0%
* **Topics Completed:** 0/4
* **Coding Exercises:** 0/3
* **Quiz Score:** N/A
* **API Design Challenge Score:** N/A
* **Backend Score:** 0 / 100

---

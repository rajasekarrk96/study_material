# Module 1: API Design and Architecture
## Topic 2: REST API Design & Constraints (REST vs RPC)

---

### 1. The Big Picture

#### What is REST?
**REST (Representational State Transfer)** is an architectural style designed by Roy Fielding in his 2000 doctoral dissertation. It is not a standard, specification, or protocol, but a set of architectural **constraints** that, when followed, produce systems that are highly scalable, maintainable, and decoupled.

#### REST vs RPC (Remote Procedure Call)
* **RPC (Action-Oriented):** Focuses on *actions* or *procedures*. The URLs contain verbs.
  * *Example:* `POST /api/createUser`, `POST /api/deleteProduct?id=5`, `GET /api/getAllActiveOrders`
* **REST (Resource-Oriented):** Focuses on *nouns* (resources) and uses standard HTTP methods to define the action.
  * *Example:* `POST /api/users`, `DELETE /api/products/5`, `GET /api/orders?status=active`

#### Why Companies Use REST
1. **Predictability:** Developers using your API don't have to guess your URL structure. If they know the resource is `products`, they know they can use `GET /products` to list, `POST /products` to create, and `DELETE /products/1` to delete.
2. **Caching:** By using HTTP GET for retrieval, intermediate proxies, Content Delivery Networks (CDNs), and browsers can automatically cache responses, dramatically reducing database load.
3. **Scalability:** The statelessness constraint ensures any server can handle any request, allowing easy horizontal scaling (adding more servers behind a load balancer).

#### Where it Fits in Backend Architecture
REST sits at the interface between the **Client** and the **Core Business Logic**, serving as a uniform contract.

```
Client (React / iOS)
       │
       ▼ (REST: HTTP GET /api/v1/products/42)
┌──────────────────────────────────────────┐
│              API Routing                 │ (Resolves to Product Controller)
├──────────────────────────────────────────┤
│           Uniform Interface              │ (Enforces GET = Safe, 200 OK, JSON)
├──────────────────────────────────────────┤
│         Business Logic / Service         │ (Fetches product 42)
├──────────────────────────────────────────┤
│            Database / Cache              │
└──────────────────────────────────────────┘
```

#### Common Interview Questions
* **"What are the 6 architectural constraints of REST?"**
  * *Answer:* Client-Server, Statelessness, Cacheability, Uniform Interface, Layered System, and Code on Demand (optional).
* **"What is HATEOAS and why is it rarely fully implemented?"**
  * *Answer:* Hypermedia As The Engine Of Application State. It means the API response should contain links guiding the client on what actions they can take next. It is rarely fully implemented because it adds significant payload size and client-side parsing complexity.
* **"Is GET always idempotent?"**
  * *Answer:* Yes. Calling `GET /products/1` once or one million times should return the same result and must never modify the state of the resource on the server.

#### Common Mistakes
* **Using Verbs in URIs:** `GET /api/v1/getProducts` (Should be `GET /api/v1/products`).
* **Using the Wrong HTTP Method:** Using `GET` to delete or update data (e.g., `GET /api/v1/deleteUser?id=5`). This is extremely dangerous because web crawlers or pre-fetching browsers can accidentally delete your entire database!
* **Ignoring Pluralization Consistency:** Mixing `/user` and `/products`. Always use plural nouns: `/users`, `/products`, `/orders`.

---

### 2. Lesson Objectives
By the end of this lesson, you will:
1. Master the 6 REST architectural constraints.
2. Know how to translate business requirements into clean, RESTful resource URIs.
3. Learn the difference between Path Parameters (for identifying a resource) and Query Parameters (for filtering/sorting).
4. Implement the **Products** module in our E-Commerce API using strict RESTful principles.

---

### 3. Detailed Explanation & Core Concepts

#### The 6 REST Constraints

1. **Client-Server:** Decouples user interface concerns from data storage concerns.
2. **Statelessness:** No client context is stored on the server between requests. Each request must contain all information (including authentication tokens) needed to execute it.
3. **Cacheability:** Responses must define themselves as cacheable or non-cacheable to prevent clients from reusing stale data and to optimize network traffic.
4. **Layered System:** A client cannot tell whether it is connected directly to the end server, or to an intermediate (like a load balancer, proxy, or firewall).
5. **Code on Demand (Optional):** Servers can temporarily extend client functionality by transferring executable code (e.g., compiled Java applets or JavaScript scripts).
6. **Uniform Interface:** This is the most critical constraint. It requires:
   * **Resource Identification:** Resources are identified in requests (typically via URIs).
   * **Manipulation through Representations:** The client holds a representation of the resource (like a JSON payload) and has enough information to modify or delete it.
   * **Self-descriptive Messages:** Each message contains enough information to describe how to process it (e.g., `Content-Type: application/json`).
   * **HATEOAS:** The client transitions through states via links provided in the resource representations.

#### Path Parameters vs. Query Parameters

* **Path Parameters (`/resources/{id}`):** Used to identify a *specific* resource.
  * *Good:* `/api/v1/products/102` (Gets product with ID 102).
* **Query Parameters (`/resources?key=value`):** Used to filter, sort, search, or paginate a collection of resources.
  * *Good:* `/api/v1/products?category=electronics&sort=-price&page=2`

---

### 4. Real-world Examples: REST vs RPC

| Requirement | RPC Style (Bad REST) | RESTful Style (Good REST) |
| :--- | :--- | :--- |
| **Get all active products** | `GET /api/getActiveProducts` | `GET /api/products?status=active` |
| **Create a new order** | `POST /api/checkout` | `POST /api/orders` |
| **Delete a user** | `POST /api/deleteUser?id=9` | `DELETE /api/users/9` |
| **Get orders for a specific user**| `GET /api/getUserOrders?userId=4` | `GET /api/users/4/orders` |

---

### 5. Code Comparison: FastAPI (Python)

#### A. Beginner Code (RPC-Style)
```python
from fastapi import FastAPI

app = FastAPI()

products_db = []

# BAD: Verb in URL, using POST for retrieval, inconsistent responses
@app.post("/api/getProductsList")
def get_list():
    return {"data": products_db}

# BAD: Action in URL, using GET to modify state!
@app.get("/api/deleteProduct")
def delete_item(product_id: int):
    global products_db
    products_db = [p for p in products_db if p["id"] != product_id]
    return {"message": "Deleted successfully"}
```

#### B. Production Code (RESTful Structure)

##### 1. The Schema (`schemas.py`)
```python
from pydantic import BaseModel, Field
from typing import Optional

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    price: float = Field(..., gt=0, description="Price must be greater than zero")
    category: str = Field(..., min_length=2)

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    category: str
```

##### 2. The Router (`routers/products.py`)
```python
from fastapi import APIRouter, status, HTTPException, Query
from typing import List, Optional
from schemas import ProductCreate, ProductResponse

router = APIRouter(prefix="/api/v1/products", tags=["Products"])

PRODUCTS_DB = []
current_id = 1

# GET /products - List with filtering (Query Parameters)
@router.get("", response_model=List[ProductResponse])
async def list_products(
    category: Optional[str] = Query(None, description="Filter by category"),
    min_price: Optional[float] = Query(None, gt=0, description="Filter by minimum price")
):
    results = PRODUCTS_DB
    if category:
        results = [p for p in results if p["category"].lower() == category.lower()]
    if min_price:
        results = [p for p in results if p["price"] >= min_price]
    return results

# GET /products/{id} - Get specific item (Path Parameter)
@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int):
    for p in PRODUCTS_DB:
        if p["id"] == product_id:
            return p
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

# POST /products - Create
@router.post("", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(product_in: ProductCreate):
    global current_id
    new_product = {
        "id": current_id,
        "name": product_in.name,
        "price": product_in.price,
        "category": product_in.category
    }
    PRODUCTS_DB.append(new_product)
    current_id += 1
    return new_product

# DELETE /products/{id} - Delete
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int):
    global PRODUCTS_DB
    for p in PRODUCTS_DB:
        if p["id"] == product_id:
            PRODUCTS_DB.remove(p)
            return # 204 No Content returns no body
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
```

---

### 6. Code Comparison: Spring Boot (Java)

#### Production RESTful Controller
```java
@RestController
@RequestMapping("/api/v1/products")
public class ProductController {

    @Autowired
    private ProductService productService;

    @GetMapping
    public ResponseEntity<List<ProductResponseDTO>> listProducts(
            @RequestParam(required = false) String category,
            @RequestParam(required = false) Double minPrice) {
        return ResponseEntity.ok(productService.getProducts(category, minPrice));
    }

    @GetMapping("/{id}")
    public ResponseEntity<ProductResponseDTO> getProduct(@PathVariable Long id) {
        return ResponseEntity.ok(productService.getProductById(id));
    }

    @PostMapping
    public ResponseEntity<ProductResponseDTO> createProduct(@Valid @RequestBody ProductCreateDTO dto) {
        return new ResponseEntity<>(productService.create(dto), HttpStatus.CREATED);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteProduct(@PathVariable Long id) {
        productService.delete(id);
        return ResponseEntity.noContent().build(); // 204 No Content
    }
}
```

---

### 7. Professional Notes

#### Best Practices for REST API Design
1. **Use Plural Nouns:** Do not mix singular and plural. Stick to `/products`, `/orders`, `/users`.
2. **Represent Relationships with Nesting:** To get orders for a specific user: `/users/{userId}/orders`. Do not exceed 2-3 levels of nesting (e.g., `/users/{id}/orders/{orderId}/items` is okay, but `/users/{id}/orders/{orderId}/items/{itemId}/reviews` is too deep. Flatten it: `/items/{itemId}/reviews`).
3. **Use JSON for Payloads:** Always set the `Content-Type` to `application/json`.
4. **Handle 404s and 204s Correctly:**
   * If a list query has no results, return `200 OK` with an empty array `[]` (not a `404 Not Found`).
   * If a specific item is requested (`/products/999`) and doesn't exist, return `404 Not Found`.
   * For successful deletions, return `204 No Content`.

---

### 8. Cheat Sheet: REST URI Rules

* **Rule 1:** `GET /resources` -> Retrieve all resources (can be filtered).
* **Rule 2:** `GET /resources/{id}` -> Retrieve a specific resource.
* **Rule 3:** `POST /resources` -> Create a new resource.
* **Rule 4:** `PUT /resources/{id}` -> Replace/Update the entire resource.
* **Rule 5:** `PATCH /resources/{id}` -> Partially update the resource.
* **Rule 6:** `DELETE /resources/{id}` -> Delete the resource.

---

### 9. Hands-on Workout & Assessment

#### Part A: Coding Exercise
Expand your **Enterprise E-Commerce API** under `c:\Users\rajas\OneDrive\_00_a_study\_05_backend_concepts\API Design and Architecture - Backend Engineering\ecommerce_api`:
1. Create `app/modules/products/schemas.py` containing `ProductCreate` and `ProductResponse` Pydantic models.
2. Create `app/modules/products/router.py` containing the RESTful routes:
   - `GET /api/v1/products` (with optional `category` and `max_price` query parameters).
   - `GET /api/v1/products/{id}`
   - `POST /api/v1/products`
   - `DELETE /api/v1/products/{id}`
3. Register the product router in `app/main.py`.

#### Part B: API Design Challenge
Design a RESTful API for a **Blogging Platform**. The platform has:
- Users
- Posts (created by Users)
- Comments (on Posts, created by Users)
- Likes (on Posts, by Users)

Write out the HTTP Methods, Paths, Request Bodies (if any), and Success Status Codes for:
1. Getting all posts made by user `42`.
2. Creating a comment on post `100`.
3. Liking post `100`.
4. Unliking post `100`.

#### Part C: Quiz
##### 1. Multiple Choice Questions (10)
1. Which of the following is NOT one of the six REST constraints?
   A. Statelessness
   B. Layered System
   C. State Syncing
   D. Cacheability
2. Which URI follows RESTful best practices for deleting a order with ID 5?
   A. `POST /api/v1/deleteOrder?id=5`
   B. `DELETE /api/v1/orders/5`
   C. `GET /api/v1/orders/delete/5`
   D. `DELETE /api/v1/order/5`
3. What should an API return when a client requests `GET /api/v1/products` but there are no products in the database?
   A. `404 Not Found` with an error message.
   B. `200 OK` with an empty array `[]`.
   C. `204 No Content` with an empty body.
   D. `500 Internal Server Error`.
4. Why is using `GET` requests to modify or delete data considered a dangerous practice?
   A. It is slower than using POST.
   B. Web crawlers, browsers, and search engines pre-fetch GET requests and might trigger unintended deletions.
   C. GET requests cannot carry query parameters.
   D. Databases reject modifications originating from GET requests.
5. In REST, what does the "Statelessness" constraint imply?
   A. The database cannot store the state of resources.
   B. The client must store all data on their local disk.
   C. The server does not store any session state about the client; every request must be self-contained.
   D. The API cannot be updated without restarting the server.
6. What is HATEOAS?
   A. An authentication protocol.
   B. A database indexing strategy.
   C. A REST constraint where the server returns links to guide the client's next actions.
   D. A tool to test API performance.
7. Which HTTP method is safe and idempotent?
   A. POST
   B. PATCH
   C. GET
   D. None of the above
8. What is the main difference between a Path Parameter and a Query Parameter?
   A. Path parameters are used to identify a specific resource, while query parameters are used to filter/sort collections.
   B. Path parameters are secure, while query parameters are not.
   C. Query parameters are only used in POST requests.
   D. Path parameters can only be integers.
9. If you want to update only the price of a product, which HTTP method is most appropriate?
   A. PUT
   B. PATCH
   C. POST
   D. GET
10. Which HTTP status code should be returned after successfully deleting a resource when no content is returned in the response body?
    A. `200 OK`
    B. `201 Created`
    C. `204 No Content`
    D. `202 Accepted`

##### 2. True / False (5)
1. REST is a standard protocol just like HTTP. (True/False)
2. A REST API must always pluralize resource nouns (e.g., `/items` instead of `/item`). (True/False)
3. An idempotent operation is one that can be performed multiple times without changing the final result beyond the initial application. (True/False)
4. The "Layered System" constraint means that the client must know all the intermediate servers it passes through. (True/False)
5. `PUT` should be used to replace the entire state of a resource, while `PATCH` is for partial updates. (True/False)

##### 3. Fill in the Blanks (5)
1. In a REST API, the URL `/users/42/orders` represents a ________ relationship between users and orders.
2. The HTTP method that is neither safe nor idempotent is ________.
3. The REST constraint that allows servers to send executable scripts to the client is called ________.
4. When filtering a list of items by their category, we should use a ________ parameter.
5. The author of the REST architectural style is ________.

##### 4. Debugging Question
Look at this FastAPI code. Find **three** REST violations or bugs and explain how to fix them:
```python
@app.get("/api/update_product_price")
def update_price(id: int, new_price: float):
    product = db.get_product(id)
    if not product:
        return {"error": "Product not found"}
    product.price = new_price
    db.save(product)
    return {"status": "success"}
```

---

### 10. Flashcards

1. **Q:** What does REST stand for?
   **A:** Representational State Transfer.
2. **Q:** What is the difference between REST and RPC?
   **A:** REST is resource-oriented (uses nouns and HTTP methods), while RPC is action-oriented (uses verbs in the URL).
3. **Q:** What is an idempotent HTTP method?
   **A:** A method where making multiple identical requests has the same effect as making a single request (e.g., GET, PUT, DELETE).
4. **Q:** What is a safe HTTP method?
   **A:** A method that does not modify resources on the server (e.g., GET, HEAD).
5. **Q:** What is the purpose of the Layered System constraint?
   **A:** It improves scalability and security by allowing intermediaries (like load balancers, caches, and gateways) to be inserted between client and server without client modification.

---

### 11. Progress Tracker

* **Module 1: API Design and Architecture:** 0%
* **Topics Completed:** 0/2
* **Coding Exercises:** 0/2
* **Quiz Score:** N/A
* **API Design Challenge Score:** N/A
* **Backend Score:** 0 / 100

---

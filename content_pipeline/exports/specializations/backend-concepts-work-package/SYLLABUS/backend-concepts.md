# Backend Concepts — Master Syllabus

**Target Role:** Backend Engineer (Junior to Mid-Level)  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 120 Hours  
**Prerequisites:** Any backend language, basic SQL, basic HTTP awareness  

---

## Study Flow

---

### Module 01 — HTTP Protocol

> **Goal:** Understand how the web transport layer works end-to-end.

#### 1.1. HTTP Fundamentals

1. **HTTP Protocol Overview**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is HTTP?
    2. HTTP as a Stateless Application Protocol
    3. HTTP/1.1 vs HTTP/2 vs HTTP/3
    4. TCP, TLS, and QUIC — the transport underneath
    5. Client-Server Communication Model
    6. Lab Exercise

2. **HTTP Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. GET — Retrieve a resource
    2. POST — Submit data, create a resource
    3. PUT — Replace a resource
    4. PATCH — Partial update
    5. DELETE — Remove a resource
    6. HEAD, OPTIONS, CONNECT, TRACE
    7. Idempotency and Safety
    8. Lab Exercise

3. **HTTP Status Codes**
    - **Course Coverage:** 🟢 Covered in Class
    1. 1xx — Informational
    2. 2xx — Success (200, 201, 204)
    3. 3xx — Redirects (301, 302, 307, 308)
    4. 4xx — Client Errors (400, 401, 403, 404, 409, 422, 429)
    5. 5xx — Server Errors (500, 502, 503, 504)
    6. Choosing the Right Status Code
    7. Lab Exercise

4. **Request and Response Structure**
    - **Course Coverage:** 🟢 Covered in Class
    1. Request Line / Request Method + Path + Version
    2. Request Headers (Accept, Content-Type, Authorization, etc.)
    3. Request Body
    4. Response Status Line
    5. Response Headers (Content-Type, Cache-Control, Location, etc.)
    6. Response Body
    7. Content Negotiation
    8. Lab Exercise

5. **URLs, URIs, and Query Strings**
    - **Course Coverage:** 🟢 Covered in Class
    1. URL Structure: Scheme, Host, Port, Path, Query, Fragment
    2. URI vs URL vs URN
    3. URL Encoding / Percent Encoding
    4. Query String Parsing
    5. Lab Exercise

---

### Module 02 — Routing

> **Goal:** Understand how an incoming HTTP request is dispatched to the correct handler.

#### 2.1. Routing Fundamentals

1. **What is Routing?**
    - **Course Coverage:** 🟢 Covered in Class
    1. Route Registration
    2. Request Dispatching
    3. Static vs Dynamic Routes
    4. Route Priority and Conflict Resolution
    5. Lab Exercise

2. **Path Parameters**
    - **Course Coverage:** 🟢 Covered in Class
    1. Dynamic URL Segments
    2. Parameter Extraction
    3. Type Constraints on Path Parameters
    4. Optional Parameters
    5. Lab Exercise

3. **Query Parameters**
    - **Course Coverage:** 🟢 Covered in Class
    1. Query String Parsing
    2. Optional vs Required Query Parameters
    3. Multi-value Query Parameters
    4. Filtering, Pagination, and Sorting via Query Parameters
    5. Lab Exercise

4. **Route Groups and Prefixes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Grouping Routes by Feature / Domain
    2. Route Prefixes (e.g., `/api/v1/`)
    3. API Versioning Strategies
        - URI Versioning
        - Header Versioning
        - Accept Header Versioning
    4. Lab Exercise

5. **Router Internals**
    - **Course Coverage:** 🟢 Covered in Class
    1. How Routers Match Paths (Hash Map, Radix Tree, Regex)
    2. Wildcard Routes and Catch-All Routes
    3. Lab Exercise

---

### Module 03 — Serialization & Deserialization

> **Goal:** Understand how data moves between the client, API layer, and database.

#### 3.1. Serialization Concepts

1. **What is Serialization?**
    - **Course Coverage:** 🟢 Covered in Class
    1. Serialization vs Deserialization
    2. Why Serialization Matters
    3. Common Formats: JSON, XML, MessagePack, Protocol Buffers
    4. Lab Exercise

2. **JSON Serialization**
    - **Course Coverage:** 🟢 Covered in Class
    1. JSON Data Types
    2. Serializing Python/Language Objects to JSON
    3. Deserializing JSON to Language Objects
    4. Handling Dates, Decimals, and Custom Types
    5. Lab Exercise

3. **Data Transfer Objects (DTOs)**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is a DTO?
    2. Request DTOs vs Response DTOs
    3. Separating API Shape from Database Shape
    4. Nested DTOs
    5. Lab Exercise

4. **Schema Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Why Validate Incoming Data?
    2. Required vs Optional Fields
    3. Type Validation
    4. Format Validation (email, URL, UUID)
    5. Custom Validators
    6. Lab Exercise

5. **Data Transformation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Mapping DTOs to Domain Models
    2. Mapping Domain Models to Response DTOs
    3. Field Aliasing and Renaming
    4. Partial Updates (PATCH semantics)
    5. Lab Exercise

---

### Module 04 — Authentication & Authorization

> **Goal:** Secure APIs using industry-standard authentication and authorization patterns.

#### 4.1. Authentication Concepts

1. **Authentication vs Authorization**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is Authentication?
    2. What is Authorization?
    3. Why They Are Different
    4. Common Confusion and Mistakes
    5. Lab Exercise

2. **Session-Based Authentication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Server-Side Sessions
    2. Session Cookies
    3. Session Storage (Memory, Redis, Database)
    4. Session Fixation Attacks
    5. Lab Exercise

3. **Token-Based Authentication — JWT**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is a JWT?
    2. JWT Structure: Header, Payload, Signature
    3. Signing Algorithms: HS256 vs RS256
    4. Access Tokens and Refresh Tokens
    5. Token Expiry and Rotation
    6. JWT Revocation Strategies
    7. Lab Exercise

4. **OAuth2**
    - **Course Coverage:** 🟢 Covered in Class
    1. OAuth2 Roles: Resource Owner, Client, Authorization Server, Resource Server
    2. OAuth2 Grant Types
        - Authorization Code Flow
        - Client Credentials Flow
        - Password Flow (deprecated)
        - Refresh Token Flow
    3. PKCE (Proof Key for Code Exchange)
    4. OpenID Connect (OIDC)
    5. Lab Exercise

5. **Authorization Patterns**
    - **Course Coverage:** 🟢 Covered in Class
    1. Role-Based Access Control (RBAC)
    2. Permission-Based Access Control
    3. Attribute-Based Access Control (ABAC)
    4. Policy Enforcement in Middleware vs Handler
    5. Lab Exercise

---

### Module 05 — Validation & Transformation

> **Goal:** Build robust input pipelines that reject bad data early.

#### 5.1. Validation Strategies

1. **Input Validation Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Validate at the Boundary
    2. Whitelist vs Blacklist Validation
    3. Validation Layers: Network, API, Service, Database
    4. Lab Exercise

2. **Field-Level Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Required Fields
    2. Type Checking
    3. Range and Length Constraints
    4. Regex Pattern Matching
    5. Enum Validation
    6. Lab Exercise

3. **Cross-Field Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Dependent Field Rules
    2. Conditional Validation
    3. Custom Business Rules
    4. Lab Exercise

4. **Validation Error Responses**
    - **Course Coverage:** 🟢 Covered in Class
    1. Returning Structured Validation Errors
    2. Field-Level Error Messages
    3. RFC 7807 Problem Details Standard
    4. Lab Exercise

5. **Data Transformation Pipeline**
    - **Course Coverage:** 🟢 Covered in Class
    1. Trimming and Normalizing Input
    2. Type Coercion
    3. Default Values
    4. Sanitization for Security
    5. Lab Exercise

---

### Module 06 — Middleware

> **Goal:** Understand middleware as the backbone of cross-cutting concerns.

#### 6.1. Middleware Architecture

1. **What is Middleware?**
    - **Course Coverage:** 🟢 Covered in Class
    1. Definition and Purpose
    2. The Middleware Pipeline Model
    3. Middleware Execution Order
    4. Request Phase vs Response Phase
    5. Lab Exercise

2. **Common Middleware Patterns**
    - **Course Coverage:** 🟢 Covered in Class
    1. Logging Middleware
    2. Authentication Middleware
    3. CORS Middleware
    4. Rate Limiting Middleware
    5. Compression Middleware
    6. Lab Exercise

3. **Custom Middleware Implementation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Writing a Request Logger
    2. Writing a Timing Middleware
    3. Writing an API Key Middleware
    4. Short-Circuiting the Pipeline
    5. Lab Exercise

4. **Error Handling Middleware**
    - **Course Coverage:** 🟢 Covered in Class
    1. Global Exception Handler
    2. Mapping Exceptions to HTTP Status Codes
    3. Returning Consistent Error Response Bodies
    4. Lab Exercise

5. **CORS (Cross-Origin Resource Sharing)**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is the Same-Origin Policy?
    2. Preflight Requests (OPTIONS)
    3. Allowed Origins, Methods, Headers
    4. Credentials with CORS
    5. Lab Exercise

---

### Module 07 — Request Context

> **Goal:** Learn how context flows through the entire lifecycle of a request.

#### 7.1. Request Context Concepts

1. **What is Request Context?**
    - **Course Coverage:** 🟢 Covered in Class
    1. Definition
    2. Why Context Propagation Matters
    3. Thread-Local vs Async Context
    4. Lab Exercise

2. **Correlation and Trace IDs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Generating a Unique Request ID
    2. Injecting Request ID into Logs
    3. Returning Request ID in Response Headers
    4. W3C Trace Context Standard
    5. Lab Exercise

3. **User Principal in Context**
    - **Course Coverage:** 🟢 Covered in Class
    1. Attaching Authenticated User to Context
    2. Accessing User in Handlers and Services
    3. Dependency Injection of Current User
    4. Lab Exercise

4. **Request Scoped Dependencies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Request-Scoped Database Sessions
    2. Request-Scoped Cache Clients
    3. Lifecycle: Open → Use → Close
    4. Lab Exercise

5. **Timeouts and Deadlines**
    - **Course Coverage:** 🟢 Covered in Class
    1. Request Timeout Concepts
    2. Propagating Deadlines to Downstream Services
    3. Cancellation Tokens
    4. Lab Exercise

---

### Module 08 — Handlers, Controllers & Services

> **Goal:** Understand layered architecture and clean separation of backend concerns.

#### 8.1. Layered Architecture

1. **The Layered Architecture Pattern**
    - **Course Coverage:** 🟢 Covered in Class
    1. Why Layers Exist
    2. HTTP Layer → Application Layer → Domain Layer → Infrastructure Layer
    3. Separation of Concerns
    4. Dependency Direction Rules
    5. Lab Exercise

2. **Handlers**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is a Handler?
    2. Handler Responsibilities
    3. What Handlers Should NOT Do
    4. Lab Exercise

3. **Controllers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Controller vs Handler
    2. Controller Responsibilities
    3. Thin Controllers
    4. Lab Exercise

4. **Services**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is a Service Layer?
    2. Application Services vs Domain Services
    3. Service Responsibilities
    4. Lab Exercise

5. **CRUD Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Create — POST → INSERT
    2. Read — GET → SELECT
    3. Update — PUT/PATCH → UPDATE
    4. Delete — DELETE → DELETE (hard vs soft)
    5. Pagination — Offset vs Cursor
    6. Filtering and Sorting
    7. Lab Exercise

---

### Module 09 — Data & Persistence

> **Goal:** Understand how backends store, retrieve, and protect data.

#### 9.1. REST Architecture

1. **REST Architectural Constraints**
    - **Course Coverage:** 🟢 Covered in Class
    1. Client-Server
    2. Statelessness
    3. Cacheability
    4. Uniform Interface
    5. Layered System
    6. Code on Demand (optional)
    7. Lab Exercise

2. **RESTful Resource Design**
    - **Course Coverage:** 🟢 Covered in Class
    1. Resource Naming Conventions
    2. Nested Resources
    3. Singleton vs Collection Resources
    4. HATEOAS Basics
    5. Lab Exercise

3. **Database Concepts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Relational vs Non-Relational Databases
    2. Tables, Rows, Columns, Keys
    3. Indexes: B-Tree, Hash, Composite
    4. ACID Properties
    5. Transactions and Isolation Levels
    6. Connection Pooling
    7. ORM Basics and N+1 Problem
    8. Lab Exercise

4. **Business Logic Layer**
    - **Course Coverage:** 🟢 Covered in Class
    1. What Belongs in Business Logic?
    2. Keeping Business Logic Out of Controllers
    3. Domain Validation vs API Validation
    4. Business Rules and Invariants
    5. Lab Exercise

5. **Caching**
    - **Course Coverage:** 🟢 Covered in Class
    1. Why Cache?
    2. Cache-Aside Pattern (Lazy Loading)
    3. Write-Through Cache
    4. Write-Behind Cache
    5. Cache Invalidation Strategies
    6. TTL and Eviction Policies (LRU, LFU)
    7. Cache Stampede and Mitigation
    8. Redis as a Cache
    9. Lab Exercise

---

### Module 10 — Infrastructure & Production

> **Goal:** Build production-grade backend systems that are observable, reliable, and secure.

#### 10.1. Async Infrastructure

1. **Transactional Emails**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is a Transactional Email?
    2. Email Service Providers (Sendgrid, Resend, AWS SES)
    3. Triggering Emails from Backend Events
    4. Email Templates
    5. Handling Delivery Failures
    6. Lab Exercise

2. **Task Queues**
    - **Course Coverage:** 🟢 Covered in Class
    1. Why Task Queues?
    2. Producer and Consumer Model
    3. Queue Brokers: Redis, RabbitMQ, SQS
    4. Retry Logic and Exponential Backoff
    5. Dead Letter Queues (DLQ)
    6. Idempotent Task Design
    7. Lab Exercise

3. **Schedulers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Cron-Based Scheduling
    2. Interval-Based Scheduling
    3. Distributed Schedulers
    4. Idempotency in Scheduled Jobs
    5. Lab Exercise

4. **Elasticsearch**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is Elasticsearch?
    2. Inverted Index
    3. Documents, Indexes, and Shards
    4. Full-Text Search Queries
    5. Indexing Data from PostgreSQL
    6. Lab Exercise

#### 10.2. Observability & Reliability

5. **Error Handling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Structured Error Responses
    2. Exception Hierarchy
    3. Business Errors vs System Errors
    4. RFC 7807 Problem Details
    5. Lab Exercise

6. **Configuration Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Environment Variables
    2. .env Files and Secrets Management
    3. Config Classes and Validation at Startup
    4. 12-Factor App — Config Factor
    5. Lab Exercise

7. **Logging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Why Structured Logging?
    2. Log Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
    3. Log Formatting (JSON vs Text)
    4. Contextual Logging (Request ID, User ID)
    5. Log Aggregation Overview
    6. Lab Exercise

8. **Monitoring**
    - **Course Coverage:** 🟢 Covered in Class
    1. Metrics: Counters, Gauges, Histograms
    2. Prometheus Basics
    3. Health Check Endpoints
    4. Alerting Overview
    5. Lab Exercise

9. **Observability**
    - **Course Coverage:** 🟢 Covered in Class
    1. The Three Pillars: Logs, Metrics, Traces
    2. Distributed Tracing Concepts
    3. OpenTelemetry Basics
    4. Trace IDs and Span IDs
    5. Lab Exercise

10. **Graceful Shutdown**
    - **Course Coverage:** 🟢 Covered in Class
    1. Why Graceful Shutdown Matters
    2. OS Signal Handling (SIGTERM, SIGINT)
    3. Connection Draining
    4. In-Flight Request Completion
    5. Lab Exercise

#### 10.3. Security & Scaling

11. **Security**
    - **Course Coverage:** 🟢 Covered in Class
    1. OWASP Top 10 API Security Risks
    2. Input Sanitization
    3. SQL Injection Prevention
    4. HTTPS Only
    5. Rate Limiting for Security
    6. Secrets Management
    7. Lab Exercise

12. **Scaling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Vertical vs Horizontal Scaling
    2. Stateless Design for Horizontal Scale
    3. Load Balancers
    4. Database Read Replicas
    5. Lab Exercise

13. **Performance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Query Optimization Basics
    2. N+1 Query Prevention
    3. Connection Pool Tuning
    4. Payload Size Reduction
    5. Lab Exercise

14. **Concurrency**
    - **Course Coverage:** 🟢 Covered in Class
    1. Sync vs Async
    2. Threads vs Coroutines
    3. Thread Safety and Race Conditions
    4. Async I/O in Backend
    5. Lab Exercise

15. **Parallelism**
    - **Course Coverage:** 🟢 Covered in Class
    1. Parallelism vs Concurrency
    2. CPU-Bound vs I/O-Bound Work
    3. Process Pools
    4. Worker Processes in Web Servers
    5. Lab Exercise

16. **Object Storage**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is Object Storage?
    2. S3-Compatible APIs
    3. Buckets and Keys
    4. Presigned URLs for Direct Upload
    5. Multipart Upload
    6. Lab Exercise

17. **Real-Time Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. WebSockets Overview
    2. WebSocket Handshake
    3. Server-Sent Events (SSE)
    4. When to Use WebSockets vs SSE vs Polling
    5. Lab Exercise

18. **Testing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Unit Testing Backend Logic
    2. Integration Testing with a Real Database
    3. API/E2E Testing with HTTP Client
    4. Test Database Isolation
    5. Mocking External Services
    6. Lab Exercise

19. **Code Quality**
    - **Course Coverage:** 🟢 Covered in Class
    1. Linting
    2. Formatting
    3. Type Checking
    4. Code Review Standards
    5. Lab Exercise

20. **12 Factor App**
    - **Course Coverage:** 🟢 Covered in Class
    1. Codebase
    2. Dependencies
    3. Config
    4. Backing Services
    5. Build, Release, Run
    6. Processes
    7. Port Binding
    8. Concurrency
    9. Disposability
    10. Dev/Prod Parity
    11. Logs
    12. Admin Processes
    13. Lab Exercise

21. **OpenAPI**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is OpenAPI?
    2. OpenAPI 3.x Specification Structure
    3. Paths, Operations, Parameters, Request Bodies, Responses
    4. Auto-Generated Swagger UI
    5. API-First Design
    6. Lab Exercise

22. **Webhooks**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is a Webhook?
    2. Webhook vs Polling
    3. Webhook Registration and Event Types
    4. Payload Signing and Verification (HMAC-SHA256)
    5. Retry Logic for Failed Deliveries
    6. Lab Exercise

23. **DevOps for Backend Engineers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Docker — Containerizing a Backend App
    2. Dockerfile Best Practices
    3. Docker Compose for Local Development
    4. CI/CD Pipeline Basics
    5. Environment Promotion: Dev → Staging → Production
    6. Lab Exercise

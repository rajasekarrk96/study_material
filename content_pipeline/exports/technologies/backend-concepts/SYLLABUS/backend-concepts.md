# Backend Concepts & System Architecture — Master Syllabus

**Target Role:** Backend Engineer / API Architect / Full Stack Developer  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 120 Hours  
**Prerequisites:** foundations/core-python (or any backend language), foundations/mysql, technologies/rest-api  
**Required Courses:** foundations/core-python, foundations/mysql  
**Optional Courses:** technologies/docker, technologies/auth-jwt  

---

## Study Flow

### Module 1 — HTTP Protocol at the Wire Level
1. **HTTP Fundamentals** (Client-server cycle, HTTP/1.1 vs HTTP/2 vs HTTP/3)
2. **HTTP Methods & Semantics** (GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD, Idempotency)
3. **HTTP Status Codes** (2xx Success, 3xx Redirection, 4xx Client Errors, 5xx Server Errors)
4. **Request & Response Structure** (Headers, Cookies, Payload, Content-Type, Content-Length)
5. **URLs, URIs, and Query Strings** (Encoding, Path Parameters, Query Parameter Parsing)

### Module 2 — Routing Architecture & URL Design
1. **Routing Engines & Trie Matching** (Static vs Dynamic Routes, Regex Routing)
2. **Path & Query Parameters** (Type Casting, Default Values, Matrix Parameters)
3. **API Versioning Strategies** (URI Path, Header, Query Parameter Versioning)
4. **Reverse Routing & Route Grouping** (Prefixes, Namespaces, Blueprint Architecture)

### Module 3 — Serialization, Deserialization & DTOs
1. **Serialization Fundamentals** (JSON, Protocol Buffers, MessagePack, XML)
2. **Data Transfer Objects (DTOs)** (Encapsulation, Input vs Output Schemas)
3. **Schema Validation Pipelines** (Pydantic, Joi, Marshmallow, Bean Validation)
4. **Data Masking & Sanitization** (Excluding sensitive fields, hashing passwords)

### Module 4 — Authentication, Authorization & Security
1. **Session-Based vs Token-Based Auth** (Stateful Cookies vs Stateless JWTs)
2. **OAuth2 & OpenID Connect Protocols** (Authorization Code, Client Credentials, Refresh Tokens)
3. **Role-Based Access Control (RBAC)** (Roles, Permissions, Policy Engines)
4. **Attribute-Based Access Control (ABAC)** (Contextual access rules, resource ownership)
5. **Security Defenses** (CORS, CSRF, Rate Limiting, SQL Injection, XSS Mitigation)

### Module 5 — Input Validation & Data Transformation
1. **Request Validation Boundaries** (Payload validation, query validation, header validation)
2. **Data Transformation & Normalization** (Type coercion, trimming, case normalization)
3. **Business Rule Validation** (Cross-field validation, database constraint checks)

### Module 6 — Middleware & Interceptor Architecture
1. **Middleware Pipeline Pattern** (Request processing pipeline, onion architecture)
2. **Logging & Request Auditing Middleware** (Structured JSON logs, execution duration)
3. **Authentication & Authorization Interceptors** (Bearer token extraction, context injection)
4. **Error Handling & Exception Filter Middleware** (Global exception capture, Problem Details RFC 7807)

### Module 7 — Request Context & Distributed Tracing
1. **Request Scoped Context** (Thread-local, Async context vars, request IDs)
2. **Correlation IDs & Distributed Tracing** (W3C Trace Context, OpenTelemetry)
3. **User Principal Propagation** (Passing authenticated identity to service layers)

### Module 8 — Handlers, Controllers & Service Layer Design
1. **Separation of Concerns** (Controllers vs Services vs Repositories)
2. **Dependency Injection & Inversion of Control** (Service lifetimes, testing mocks)
3. **Transaction Management & Unit of Work** (ACID boundaries, rollback handling)
4. **Domain-Driven Design (DDD) Basics** (Entities, Value Objects, Domain Events)

### Module 9 — Data Persistence, ORM & Connection Management
1. **Connection Pooling Mechanics** (Min/Max pool size, connection timeouts, leakage prevention)
2. **ORM vs Query Builders vs Raw SQL** (Impedance mismatch, N+1 query problem)
3. **Database Migrations & Schema Evolution** (Flyway, Alembic, zero-downtime migrations)
4. **Caching Strategies** (Cache-aside, Write-through, Write-behind, Redis invalidation)

### Module 10 — Production Infrastructure & Reliability
1. **Configuration Management** (12-Factor App, Environment Variables, Secret Managers)
2. **Asynchronous Background Task Queues** (Celery, BullMQ, Dead Letter Queues)
3. **Health Checks & Probes** (Liveness, Readiness, Startup Probes)
4. **Graceful Shutdown & Connection Draining** (Signal handling, inflight request completion)
5. **Observability, Metrics & Alerting** (Prometheus metrics, Grafana dashboards, Sentry)

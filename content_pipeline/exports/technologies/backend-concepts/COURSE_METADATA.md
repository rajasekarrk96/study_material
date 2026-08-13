# Course Metadata

---

## Course Name

Backend Concepts

---

## Slug

`backend-concepts`

---

## Description

Backend Concepts is a comprehensive, framework-agnostic course that teaches the
foundational principles, patterns, and systems that every backend engineer must understand.

The course covers the entire backend engineering stack — from how HTTP works at the
wire level, through routing, serialization, authentication, middleware, CRUD, databases,
caching, async task queues, search engines, real-time systems, observability, security,
and production readiness.

Topics are taught at the concept level, not tied to any single language or framework.
Code examples use Python (FastAPI / Flask) as the reference implementation, but the
concepts apply universally to Node.js, Java, Go, .NET, and any backend runtime.

---

## Target Role

- Backend Engineer (Junior to Mid-level)
- Full Stack Developer moving to backend specialization
- API Developer seeking deeper architectural understanding

---

## Difficulty Level

Intermediate

---

## Prerequisites

The learner should already know:

- Any one backend programming language (Python, JavaScript/Node, Java, Go, etc.)
- Basic HTTP concepts (what a request and response look like)
- Basic SQL (SELECT, INSERT, UPDATE, DELETE)
- How to run a simple web server locally

Recommended prior courses in Learning OS:
- `python-core` or any backend language foundation
- `mysql-database` or equivalent
- `rest-api-design` (helpful but not required)

---

## Estimated Duration

120 Hours

---

## Learning Outcomes

Upon completing this course, the learner will be able to:

1. Explain how HTTP works end-to-end including methods, status codes, headers, and the request/response lifecycle.
2. Implement clean routing architecture with path parameters, query parameters, and versioning.
3. Apply serialization and deserialization patterns using DTOs and schema validation.
4. Build authentication and authorization systems using JWT, OAuth2, and RBAC.
5. Implement input validation and data transformation pipelines.
6. Design and implement middleware pipelines for cross-cutting concerns.
7. Propagate request context (trace IDs, user principals) across the request lifecycle.
8. Build handlers, controllers, and services following separation of concerns.
9. Implement full CRUD operations with proper error handling and validation.
10. Apply REST architectural constraints correctly.
11. Select appropriate databases and implement connection pooling and ORM patterns.
12. Design and implement business logic layers.
13. Build caching layers using cache-aside, write-through, and invalidation strategies.
14. Implement transactional email systems.
15. Design task queues with retry logic and dead letter queues.
16. Build scheduled job systems.
17. Integrate Elasticsearch for full-text search.
18. Implement structured error handling and problem-detail responses.
19. Manage environment configuration using 12-factor principles.
20. Implement structured logging and log levels.
21. Set up monitoring and metrics collection.
22. Implement distributed tracing and observability pipelines.
23. Implement graceful shutdown with connection draining.
24. Apply backend security best practices (OWASP, JWT revocation, input sanitization).
25. Design horizontally scalable backend systems.
26. Optimize backend performance (query optimization, caching, connection pools).
27. Implement concurrent and parallel processing patterns.
28. Integrate object storage (S3-compatible) for file uploads and streaming.
29. Build real-time systems using WebSockets and SSE.
30. Write backend unit tests, integration tests, and API tests.
31. Maintain code quality with linting, formatting, and review standards.
32. Apply 12-Factor App methodology to production-grade backends.
33. Document APIs using OpenAPI / Swagger specifications.
34. Design and consume webhook systems.
35. Apply DevOps fundamentals for backend engineers (Docker, CI/CD, deployment basics).

---

## Required Software

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.12+ | Reference implementation language |
| FastAPI | Latest | Reference web framework |
| Uvicorn | Latest | ASGI server |
| SQLAlchemy | 2.x | ORM |
| PostgreSQL | 15+ | Primary relational database |
| Redis | 7+ | Caching and queue broker |
| Docker | Latest | Containerization |
| Celery | Latest | Task queue |
| Elasticsearch | 8.x | Search engine |
| Pytest | Latest | Testing |

> **Note:** All concepts are language-agnostic. Python is used for examples only.
> Contributors may optionally add parallel examples in Node.js or Go where appropriate.

---

## Course Number

To be assigned during merge into Learning OS (next available slot after `55-database-technologies`).

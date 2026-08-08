# FastAPI — Master Syllabus

---

# Course Information

**Course Name:** FastAPI

**Category:** Technology Course

**Learning Path(s):**

- Python Full Stack
- Backend Development

**Difficulty:** Beginner

**Estimated Duration:** 14 Hours

**Prerequisites:**

- Core Python
- REST API

**Course Status:** COMING_SOON

---

# Module 1 — Modern Async Python & FastAPI Core Architecture

## Lesson 1.1 — Async Python, ASGI Architecture, & Uvicorn Basics

**Course Coverage:** 🟢 Covered in Class

### Topics

- WSGI vs ASGI Architecture
- Running with Uvicorn Server:
- Migrated Notes
- Topic 2: REST API Design & Constraints (REST vs RPC)
- The Big Picture
- Lesson Objectives
- Detailed Explanation & Core Concepts
- Real-world Examples: REST vs RPC
- Code Comparison: FastAPI (Python)
- Code Comparison: Spring Boot (Java)
- Professional Notes
- Hands-on Workout & Assessment
- Flashcards
- Progress Tracker

## Lesson 1.2 — FastAPI Application Instantiation, Routing, & OpenAPI UI

**Course Coverage:** 🟢 Covered in Class

### Topics

- Zero-Configuration Automatic OpenAPI Generation
- Migrated Notes
- Topic 6: The HTTP Protocol (Deep Dive)
- The Big Picture
- Anatomy of an HTTP Request
- Anatomy of an HTTP Response
- HTTP Methods & Their Properties
- HTTP Headers: The Control Knobs of the Web
- Python Example: Inspecting Request Headers and Body
- Hands-on Workout & Assessment
- Progress Tracker

---

# Module 2 — Request Validation & Pydantic Data Models

## Lesson 2.1 — Path Parameters, Query Strings, & Type Annotations

**Course Coverage:** 🟢 Covered in Class

### Topics

- Parameter Parsing & Automatic Type Conversion
- Migrated Notes
- Topic 8: FastAPI & CRUD Operations
- The Big Picture
- Pydantic for Validation and Serialization
- Implementing CRUD in FastAPI
- Professional Notes: PUT vs PATCH
- Hands-on Workout & Assessment
- Progress Tracker

## Lesson 2.2 — Pydantic v2 Models & Schema Validation

**Course Coverage:** 🟢 Covered in Class

### Topics

- Pydantic v2 Architecture

---

# Module 3 — Dependency Injection System

## Lesson 3.1 — Dependency Injection Architecture & Depends()

**Course Coverage:** 🟢 Covered in Class

### Topics

- What is Dependency Injection?

## Lesson 3.2 — Sub-Dependencies, Security Dependencies, & Yield Cleanups

**Course Coverage:** 🟢 Covered in Class

### Topics

- Yield Dependencies & Context Cleanup
- Mocking Dependencies in Unit Tests:

---

# Module 4 — Advanced Features

## Lesson 4.1 — API Metadata and Documentation Enrichment

**Course Coverage:** 🟢 Covered in Class

### Topics

- App-Level Metadata
- Route-Level Metadata
- Hiding Routes from Docs
- Customising Docs URLs

## Lesson 4.2 — Query Parameters and Validation

**Course Coverage:** 🟢 Covered in Class

### Topics

- Basic Query Parameters
- Annotated with Query()
- List Query Parameters
- Regex Validation

## Lesson 4.3 — Multi-Source Parameter Declarations

**Course Coverage:** 🟢 Covered in Class

### Topics

- Mixing Path, Query, Body
- Multiple Body Parameters
- Body with `embed=True`
- Header and Cookie

## Lesson 4.4 — Form Submissions and File Handling

**Course Coverage:** 🟢 Covered in Class

### Topics

- Form Data
- File Upload
- File + Form Together
- Multiple Files
- File Size Limit

## Lesson 4.5 — Headers Cookies and Request Info

**Course Coverage:** 🟢 Covered in Class

### Topics

- Reading Headers
- Reading Cookies
- Setting Response Headers and Cookies
- Raw Request Object

## Lesson 4.6 — Advanced Response Classes

**Course Coverage:** 🟢 Covered in Class

### Topics

- Response Class Variants
- Streaming Response
- ORJSONResponse (faster)
- Custom Headers in Response

## Lesson 4.7 — Custom Exception Handling

**Course Coverage:** 🟢 Covered in Class

### Topics

- HTTPException
- Custom Exception Classes
- Override Validation Error Format
- Global Error Catch-All

## Lesson 4.8 — WebSocket Architecture

**Course Coverage:** 🟢 Covered in Class

### Topics

- Basic WebSocket Endpoint
- Connection Manager (Broadcast)
- Sending JSON
- WebSocket Authentication

## Lesson 4.9 — OpenAPI Standard and Interactive UI

**Course Coverage:** 🟢 Covered in Class

### Topics

- Auto-Generated OpenAPI Schema
- Request/Response Examples
- Field-Level Examples
- Custom OpenAPI Function

---

# Module 5 — Async Database Integration with SQLAlchemy 2.0 & asyncpg

## Lesson 5.1 — SQLAlchemy 2.0 Async Engine & asyncpg

**Course Coverage:** 🟢 Covered in Class

### Topics

- Synchronous vs Asynchronous Database Drivers
- File 1: `database.py` (SQLAlchemy 2.0 Async Engine & Dependency)
- File 2: `main.py` (Using AsyncSession in Route)
- Migrated Notes
- Topic 14: Database Relationships & Normalization
- The Big Picture
- Entity Relationships
- Implementing Relationships in SQLAlchemy
- Hands-on Workout & Assessment
- Progress Tracker

## Lesson 5.2 — Async CRUD Operations & AsyncSession

**Course Coverage:** 🟢 Covered in Class

### Topics

- SQLAlchemy 2.0 Async Query Style
- File 1: `models.py` (Async SQLAlchemy Models)
- File 2: `main.py` (Async CRUD Routes)
- Migrated Notes
- Topic 15: Database Indexes & ACID Transactions
- Database Indexes
- ACID Transactions
- Implementing Transactions in SQLAlchemy
- Hands-on Workout & Assessment
- Progress Tracker

---

# Module 6 — Database Integration

## Lesson 6.1 — Schema Evolution with Alembic

**Course Coverage:** 🟢 Covered in Class

### Topics

- Alembic Setup
- Creating Migrations
- Migration File
- Async Alembic

## Lesson 6.2 — Scope-Based Fine-Grained Authorization

**Course Coverage:** 🟢 Covered in Class

### Topics

- JWT with Scopes
- Scope Validation Dependency
- Protecting Routes with Scopes

---

# Module 7 — Security & Authentication

## Lesson 7.1 — OAuth2 Password Bearer & Password Hashing

**Course Coverage:** 🟢 Covered in Class

### Topics

- OAuth2 Password Bearer Flow
- Migrated Notes
- Topic 12: OAuth2 & Session-based Authentication
- The Big Picture
- What is OAuth2?
- The OAuth2 Authorization Code Flow (The Standard Web Flow)
- OAuth2 Scopes
- Python Example: OAuth2 Password Flow with Scopes in FastAPI
- Hands-on Workout & Assessment
- Progress Tracker

## Lesson 7.2 — JWT Authentication & Current User Dependency

**Course Coverage:** 🟢 Covered in Class

### Topics

- The `get_current_user` Dependency Pipeline
- Migrated Notes
- Topic 11: Token-based Authentication & JWT (JSON Web Tokens)
- The Big Picture
- Anatomy of a JWT
- JWT Authentication Flow
- Password Hashing (Crucial Security)
- Python Example: JWT Handling in FastAPI
- Hands-on Workout & Assessment
- Progress Tracker

---

# Module 8 — Production FastAPI

## Lesson 8.1 — Application Setup and Environment Configuration

**Course Coverage:** 🟢 Covered in Class

### Topics

- Settings with pydantic-settings
- Dependency-Cached Settings
- Lifespan Events (startup/shutdown)
- Environment-Specific Configuration

---

# Module 9 — Modular Application Structuring with APIRouter

## Lesson 9.1 — APIRouter() Architecture & Route Prefixes

**Course Coverage:** 🟢 Covered in Class

### Topics

- What is an APIRouter?
- File 1: `routers/devices.py` (APIRouter Module)
- File 2: `main.py` (Main FastAPI App Registering Router)
- Migrated Notes
- Topic 3: API Architecture, Layered Patterns, and Dependency Injection
- The Big Picture
- Lesson Objectives
- Detailed Explanation & Core Concepts
- Code Comparison: FastAPI (Python)
- Code Comparison: Spring Boot (Java)
- Professional Notes
- Hands-on Workout & Assessment
- Flashcards
- Progress Tracker

## Lesson 9.2 — Modular Directory Structure & Big Applications

**Course Coverage:** 🟢 Covered in Class

### Topics

- Enterprise Production Directory Layout
- File 1: `src/app/core/config.py` (Pydantic-Settings Configuration)
- File 2: `src/app/main.py` (Global Exception Handler & Main App)

---

# Module 10 — Asynchronous Middleware & CORS

## Lesson 10.1 — Asynchronous Custom Middleware & CORS

**Course Coverage:** 🟢 Covered in Class

### Topics

- What is FastAPI Middleware?
- Cross-Origin Resource Sharing (CORS)
- Migrated Notes
- Topic 9: API Request Lifecycle, Middleware, and CORS
- The Big Picture
- What is Middleware?
- Understanding CORS (Cross-Origin Resource Sharing)
- Python Example: Configuring CORS and Custom Middleware in FastAPI
- Hands-on Workout & Assessment
- Progress Tracker

## Lesson 10.2 — Request Timing Headers & Performance Logging

**Course Coverage:** 🟢 Covered in Class

### Topics

- High-Precision Latency Tracking
- Migrated Notes
- Topic 16: Caching with Redis & Rate Limiting
- Caching with Redis
- Rate Limiting
- Python Example: Cache-Aside with Redis in FastAPI
- Hands-on Workout & Assessment
- Progress Tracker

---

# Module 11 — Background Tasks & Asynchronous Event Handlers

## Lesson 11.1 — FastAPI Background Tasks

**Course Coverage:** 🟢 Covered in Class

### Topics

- What are FastAPI BackgroundTasks?

## Lesson 11.2 — Lifespan Event Handlers

**Course Coverage:** 🟢 Covered in Class

### Topics

- What are Lifespan Events?

---

# Module 12 — WebSockets & Real-Time Communication

## Lesson 12.1 — WebSockets Protocol & Endpoint Handling

**Course Coverage:** 🟢 Covered in Class

### Topics

- HTTP Polling vs Full-Duplex WebSockets

## Lesson 12.2 — Real-Time Connection Manager & Broadcasting

**Course Coverage:** 🟢 Covered in Class

### Topics

- The Connection Manager Pattern

---

# Module 13 — Testing & Production Deployment

## Lesson 13.1 — Async Testing with Pytest & httpx.AsyncClient

**Course Coverage:** 🟢 Covered in Class

### Topics

- Why `httpx.AsyncClient` over Starlette `TestClient`?
- File 1: `conftest.py` (Pytest Async Fixtures)
- File 2: `test_main.py` (Async Test Cases)
- Migrated Notes
- Topic 17: Testing with Pytest & Mocking
- The Big Picture
- Testing with Pytest
- What is Mocking?
- Python Example: Writing a FastAPI Test with Pytest
- Hands-on Workout & Assessment
- Progress Tracker

## Lesson 13.2 — Production Deployment with Gunicorn Uvicorn Workers & Docker

**Course Coverage:** 🟢 Covered in Class

### Topics

- Production Process Management: Gunicorn + Uvicorn
- File 1: `gunicorn_conf.py` (Gunicorn Configuration)
- File 2: `Dockerfile` (Production Container Definition)
- File 3: `docker-compose.yml` (Multi-Container Deployment)
- Migrated Notes
- Topic 18: Containerization with Docker & Production Best Practices
- The Big Picture
- Core Docker Concepts
- Production-Grade Dockerfile for FastAPI
- Docker Compose for Local Development
- Hands-on Workout & Assessment
- Progress Tracker

---

# Software & Tools

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

---

# Hardware Requirements

- A computer with Python 3 installed

---

# Course Completion Summary

**Estimated Hours:** 14 Hours

**Modules:** 13

**Lessons:** 32

**Topics:** 188+

**Difficulty:** Beginner

**Course Status:** COMING_SOON

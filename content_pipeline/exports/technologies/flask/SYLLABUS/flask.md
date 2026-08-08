# Flask — Master Syllabus

---

# Course Information

**Course Name:** Flask

**Category:** Technology Course

**Learning Path(s):**

- Python Full Stack
- Backend Development

**Difficulty:** Beginner

**Estimated Duration:** 12 Hours

**Prerequisites:**

- Core Python
- HTML5

**Course Status:** COMING_SOON

---

# Module 1 — WSGI Architecture & Flask Core Basics

## Lesson 1.1 — Web Server Gateway Interface (WSGI) Architecture

**Course Coverage:** 🟢 Covered in Class

### Topics

- What is WSGI (PEP 3333)?

## Lesson 1.2 — Flask Application Factory Pattern & Configuration

**Course Coverage:** 🟢 Covered in Class

### Topics

- Why the Application Factory Pattern?
- File 1: `config.py` (Environment Configurations)
- File 2: `app/__init__.py` (Application Factory)

---

# Module 2 — Routing, Request Handling, & Responses

## Lesson 2.1 — Routing System, Dynamic URL Parameters, & Converter Types

**Course Coverage:** 🟢 Covered in Class

### Topics

- Built-in URL Converters

## Lesson 2.2 — HTTP Methods, Request Object Inspection, & Response Formatting

**Course Coverage:** 🟢 Covered in Class

### Topics

- The Flask `request` Context Local

---

# Module 3 — Jinja2 Templating Engine

## Lesson 3.1 — Jinja2 Syntax, Variables, Control Flow, & Macros

**Course Coverage:** 🟢 Covered in Class

### Topics

- Jinja2 Delimiter Syntax
- File 1: `templates/macros/card.html` (Jinja2 Reusable Macro)
- File 2: `templates/dashboard.html` (Main Page)
- File 3: `app.py` (Python View Function)

---

# Module 4 — Flask Application Contexts & Globals

## Lesson 4.1 — Application Context & Request Context Architecture

**Course Coverage:** 🟢 Covered in Class

### Topics

- Application Context vs Request Context

## Lesson 4.2 — The g Global Object & Request-Scoped State

**Course Coverage:** 🟢 Covered in Class

### Topics

- What is the `g` Object?

---

# Module 5 — Advanced Flask Patterns

## Lesson 5.1 — Flask Response Objects and Streaming

**Course Coverage:** 🟢 Covered in Class

### Topics

- Response Object Basics
- Streaming Responses
- Server-Sent Events (SSE)
- File Streaming
- JSON Responses

## Lesson 5.2 — Advanced Form Validation and File Uploads

**Course Coverage:** 🟢 Covered in Class

### Topics

- WTForms File Field
- Secure File Handling
- MIME Type Validation
- Multiple File Uploads
- Custom Validators

## Lesson 5.3 — SQLAlchemy Relationship Types and Lazy Loading

**Course Coverage:** 🟢 Covered in Class

### Topics

- One-to-Many Relationship
- Many-to-Many with Association Table
- Lazy Loading Strategies
- Association Object Pattern (with extra fields)

## Lesson 5.4 — Access Control and Role Authorization

**Course Coverage:** 🟢 Covered in Class

### Topics

- Role-Based Access Control (RBAC) Pattern
- Role-Required Decorator
- Permission-Based Access (Fine-Grained)
- Flask-Principal Integration

---

# Module 6 — Web Forms & Input Validation (Flask-WTF)

## Lesson 6.1 — WTForms & Flask-WTF Extension

**Course Coverage:** 🟢 Covered in Class

### Topics

- Processing Manual HTML Forms vs Flask-WTF
- File 1: `forms.py` (FlaskForm Class Definition)
- File 2: `app.py` (Flask View Function)

## Lesson 6.2 — Form Validation & Automatic CSRF Protection

**Course Coverage:** 🟢 Covered in Class

### Topics

- Custom In-Class Field Validation
- CSRF Protection Mechanism
- File 1: `forms.py` (Form with Custom & Standard Validators)
- File 2: `templates/register.html` (Rendering Inline Validation Errors)

---

# Module 7 — Production Deployment

## Lesson 7.1 — Reverse Proxy and Nginx Configuration

**Course Coverage:** 🟢 Covered in Class

### Topics

- Nginx as Reverse Proxy for Flask
- Gunicorn Configuration
- SSL/HTTPS with Let's Encrypt
- Flask ProxyFix Middleware
- Systemd Service

## Lesson 7.2 — Containerization with Docker

**Course Coverage:** 🟢 Covered in Class

### Topics

- Flask Dockerfile
- Docker Compose (Flask + MySQL + Redis)
- Environment Management
- Build and Run Commands
- Health Check and Restart Policy

---

# Module 8 — Relational Databases & ORM (Flask-SQLAlchemy)

## Lesson 8.1 — Flask-SQLAlchemy Extension Architecture

**Course Coverage:** 🟢 Covered in Class

### Topics

- Object-Relational Mapping (ORM)
- File 1: `extensions.py` (Unbound Extension Instance)
- File 2: `config.py`
- File 3: `app/__init__.py` (Application Factory Integration)

## Lesson 8.2 — Defining SQLAlchemy Models, Fields, & Relationships

**Course Coverage:** 🟢 Covered in Class

### Topics

- SQLAlchemy Model Mapping
- File: `models.py` (SQLAlchemy Relational Schema)

## Lesson 8.3 — Executing Database CRUD Operations

**Course Coverage:** 🟢 Covered in Class

### Topics

- Unit of Work Transaction Management

## Lesson 8.4 — Schema Migrations with Flask-Migrate & Alembic

**Course Coverage:** 🟢 Covered in Class

### Topics

- Why `db.create_all()` Fails in Production
- File 1: `extensions.py`
- File 2: `app/__init__.py` (Factory Integration)
- File 3: Command Line Execution Sequence

---

# Module 9 — Session Management, Cookies, & Authentication

## Lesson 9.1 — User Authentication with Flask-Login

**Course Coverage:** 🟢 Covered in Class

### Topics

- Flask-Login Architecture
- File 1: `models.py` (User Model with UserMixin)
- File 2: `app.py` (Flask-Login Initialization & Auth Routes)

## Lesson 9.2 — Password Hashing & Cookie Security

**Course Coverage:** 🟢 Covered in Class

### Topics

- One-Way Password Hashing & Salting
- Flask Session Cookie Security Configuration
- File: `security_demo.py` (Password Hashing & Cookie Security Config)

---

# Module 10 — Application Structuring with Blueprints

## Lesson 10.1 — Flask Blueprint Architecture

**Course Coverage:** 🟢 Covered in Class

### Topics

- What is a Flask Blueprint?
- File 1: `app/api/routes.py` (Blueprint Module)
- File 2: `app/__init__.py` (Registering Blueprints in Application Factory)

---

# Module 11 — REST API Development & Serialization

## Lesson 11.1 — RESTful API Principles & Resource Routing

**Course Coverage:** 🟢 Covered in Class

### Topics

- REST Architectural Constraints

## Lesson 11.2 — API Serialization with Flask-Marshmallow

**Course Coverage:** 🟢 Covered in Class

### Topics

- Serialization vs Deserialization
- File 1: `schemas.py` (Flask-Marshmallow Schemas)
- File 2: `routes.py` (Using Schemas in API Views)

## Lesson 11.3 — JWT Authentication with Flask-JWT-Extended

**Course Coverage:** 🟢 Covered in Class

### Topics

- JSON Web Token (JWT) Structure

---

# Module 12 — Advanced Flask Extensions & Background Tasks

## Lesson 12.1 — Application Caching with Flask-Caching & Redis

**Course Coverage:** 🟢 Covered in Class

### Topics

- Why Backend Caching?

## Lesson 12.2 — Asynchronous Background Tasks with Celery & Redis

**Course Coverage:** 🟢 Covered in Class

### Topics

- Why Asynchronous Background Tasks?
- File 1: `celery_app.py` (Celery Integration Helper)
- File 2: `tasks.py` (Celery Tasks)
- File 3: `app.py` (Dispatching Tasks & Checking Status)

## Lesson 12.3 — Email Delivery with Flask-Mail

**Course Coverage:** 🟢 Covered in Class

### Topics

- SMTP Protocol & Synchronous vs Async Delivery

---

# Module 13 — Error Handling, Logging, & Testing

## Lesson 13.1 — Custom Error Pages & Error Handlers

**Course Coverage:** 🟢 Covered in Class

### Topics

- Exception Handling Architecture

## Lesson 13.2 — Application Logging & Sentry Integration

**Course Coverage:** 🟢 Covered in Class

### Topics

- Production Logging Architecture

---

# Module 14 — Testing & Production Deployment

## Lesson 14.1 — Automated Testing with Pytest & Test Client

**Course Coverage:** 🟢 Covered in Class

### Topics

- Flask `test_client()` Architecture
- File 1: `conftest.py` (Pytest Shared Fixtures)
- File 2: `test_api.py` (Pytest Test Cases)

## Lesson 14.2 — Production Deployment with Gunicorn, Nginx, & Docker

**Course Coverage:** 🟢 Covered in Class

### Topics

- Enterprise Production Deployment Architecture
- File 1: `wsgi.py` (Production Entrypoint)
- File 2: `Dockerfile` (Production Multi-Stage Container)
- File 3: `docker-compose.yml` (Multi-Container Orchestration)
- File 4: `nginx.conf` (Nginx Reverse Proxy Configuration)

---

# Software & Tools

- Python 3.10+
- Flask
- Jinja2

---

# Hardware Requirements

- A computer with Python 3 installed

---

# Course Completion Summary

**Estimated Hours:** 12 Hours

**Modules:** 14

**Lessons:** 32

**Topics:** 88+

**Difficulty:** Beginner

**Course Status:** COMING_SOON

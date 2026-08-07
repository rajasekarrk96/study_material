# Flask Blueprint Architecture

> **Course**: Git Version Control | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Prerequisites**: [Lesson 7.2 Password Hashing](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_04_flask/_04_16_password_hashing_and_cookie_security.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Explain the architectural necessity of **Flask Blueprints** in large applications.
2. Instantiate Blueprints using `Blueprint('name', __name__)`.
3. Register Blueprints on the application instance with custom `url_prefix` settings.
4. Reference blueprint-scoped view functions using `url_for('blueprint.view_function')`.

---

---

Open Python REPL or VS Code.

---

---

### 3.1 What is a Flask Blueprint?
A **Blueprint** is a way to organize a group of related view functions, templates, and static files into modular components. A Blueprint is not a standalone Flask application itself, but a set of instructions for registering routes, error handlers, and middleware hooks on an application instance created by `create_app()`.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          FLASK BLUEPRINT ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ Application Factory (`create_app()`)                                        │
│   ├── Register `auth_bp`       ──► Prefix: `/auth`                          │
│   ├── Register `api_bp`        ──► Prefix: `/api/v1`                        │
│   └── Register `telemetry_bp`  ──► Prefix: `/telemetry`                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

---

```mermaid
flowchart TD
    AppFactory[create_app] --> AuthBP["app.register_blueprint(auth_bp, url_prefix='/auth')"]
    AppFactory --> ApiBP["app.register_blueprint(api_bp, url_prefix='/api/v1')"]
    AuthBP --> AuthRoutes["/auth/login, /auth/logout"]
    ApiBP --> ApiRoutes["/api/v1/sensors, /api/v1/readings"]
```

---

---

### File 1: `app/api/routes.py` (Blueprint Module)

```python
from flask import Blueprint, jsonify

# 1. Instantiate Blueprint
api_bp = Blueprint("api", __name__)

@api_bp.route("/status")
def api_status():
    return jsonify({"system": "ONLINE", "blueprint": "api"})

@api_bp.route("/nodes")
def list_nodes():
    return jsonify({"nodes": ["ESP32-A1", "ESP32-B2"]})
```

### File 2: `app/__init__.py` (Registering Blueprints in Application Factory)

```python
from flask import Flask, url_for
from app.api.routes import api_bp

def create_app():
    app = Flask(__name__)

    # 2. Register Blueprint with URL Prefix
    app.register_blueprint(api_bp, url_prefix="/api/v1")

    @app.route("/test-routes")
    def test_routes():
        # Blueprint-scoped url_for requires 'blueprint_name.view_function'!
        status_url = url_for("api.api_status")
        return {"generated_api_url": status_url}

    return app
```

---

---

- **Multi-Tenant Microservice Architectures**: Enterprise web platforms isolate user authentication, billing, administrative tools, and REST APIs into independent, self-contained Flask Blueprints.

---

---

1. Save `app/api/routes.py` and `app/__init__.py`.
2. Run `FLASK_APP="app:create_app()" flask run` $\to$ Inspect `/api/v1/status` and `/test-routes` endpoints in browser!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`BuildError: Could not build url for endpoint 'api_status'`** | Calling `url_for('api_status')` without the blueprint namespace prefix. | Use the full blueprint namespace string: `url_for('api.api_status')`. |

---

---

- **Always Namespace `url_for()`**: Prefix view function names with the blueprint name (`'auth.login'`).

---

---

### Q1: What is a Flask Blueprint and how does it improve code architecture?
**Answer**: A Blueprint is a logical grouping of routes, error handlers, and assets that can be registered on a Flask application instance. It promotes modular software architecture, allows splitting large applications into domain-specific packages, and enables reusing blueprints across multiple projects.

---

---

```json
{
  "quiz_title": "Lesson 8.1 Flask Blueprints Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which `url_for` syntax correctly references a view function named `login` defined inside an `auth` blueprint?",
      "options": ["url_for('login')", "url_for('auth.login')", "url_for('auth/login')", "url_for('Blueprint.login')"],
      "correct_answer_index": 1,
      "explanation": "url_for('auth.login') uses blueprint-scoped syntax."
    }
  ]
}
```

---

---

Modularize a monolithic Flask app into `auth_bp` and `telemetry_bp` blueprints.

---

---

**Front**: What parameter on `app.register_blueprint()` prefixes all routes in that blueprint?
**Back**: `url_prefix='/prefix_name'`.
<!-- flashcard:end -->

---

---

```python
bp = Blueprint("auth", __name__)
@bp.route("/login")
def login(): return "login"
app.register_blueprint(bp, url_prefix="/auth")
```

---

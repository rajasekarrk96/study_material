# Flask Routing And Url Converters

> **Course**: Git Fundamentals | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐ Beginner
- **Prerequisites**: [Lesson 1.2 Application Factory](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_04_flask/_04_02_flask_application_factory_pattern.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Define URL routes using `@app.route()` decorators.
2. Extract dynamic URL parameters using `<variable_name>` syntax.
3. Apply built-in URL converters (`int`, `float`, `path`, `uuid`).
4. Generate reverse URL paths using **`url_for()`**.

---

---

Open Python REPL or VS Code.

---

---

### 3.1 Built-in URL Converters
By default, dynamic URL variables `<param>` are treated as strings. Flask provides built-in URL converter types that automatically validate and convert path parameters into target Python data types before passing them to the view function:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         FLASK BUILT-IN URL CONVERTERS                       │
├─────────────────┬───────────────────────────────────────────────────────────┤
│ Converter Type  │ Description & Python Type Conversion                      │
├─────────────────┼───────────────────────────────────────────────────────────┤
│ `string`        │ Default string (accepts any text without slashes)         │
│ `int`           │ Accepts positive integers (`int`)                         │
│ `float`         │ Accepts positive floating-point numbers (`float`)         │
│ `path`          │ Accepts string including forward slashes `/`              │
│ `uuid`          │ Accepts valid 36-character UUID strings (`uuid.UUID`)     │
└─────────────────┴───────────────────────────────────────────────────────────┘
```

---

---

```mermaid
flowchart TD
    Req["HTTP GET /api/v1/sensors/101"] --> Router[Werkzeug Routing Map]
    Router --> Check{"Matches <int:sensor_id>?"}
    Check -->|Yes| View[View Function receives sensor_id = 101 as int]
    Check -->|No| NotFound[Returns HTTP 404 Not Found]
```

---

---

```python
# Flask Dynamic Routing & URL Converters (routing_demo.py)
import uuid
from flask import Flask, url_for

app = Flask(__name__)

# 1. String & Integer URL Converters
@app.route("/sensors/<string:category>/<int:sensor_id>")
def get_sensor_detail(category, sensor_id):
    # sensor_id is automatically cast to Python int!
    return {
        "category": category,
        "sensor_id": sensor_id,
        "type": str(type(sensor_id))
    }

# 2. UUID Converter
@app.route("/devices/<uuid:device_uuid>")
def get_device_by_uuid(device_uuid):
    # device_uuid is a Python uuid.UUID instance!
    return {"device_uuid": str(device_uuid), "valid": True}

# 3. Reverse URL Generation Test Route
@app.route("/test-urls")
def test_urls():
    # url_for() generates canonical URL paths dynamically!
    detail_url = url_for("get_sensor_detail", category="telemetry", sensor_id=42)
    return {"generated_url": detail_url}

if __name__ == "__main__":
    app.run(debug=True)
```

---

---

- **RESTful Resource Endpoints**: Backend microservices define typed endpoints (`/api/v1/telemetry/<uuid:device_id>`) to ensure invalid non-UUID path parameters automatically return HTTP 404 without reaching business logic.

---

---

1. Save code as `routing_demo.py`.
2. Run `python routing_demo.py` $\to$ Test `/sensors/temp/101` and `/test-urls` in browser!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **HTTP 404 for Float Parameter** | Passing a negative float to `<float:val>` (Flask built-in converters only match positive numbers). | Write a custom Werkzeug URL converter for negative floats. |

---

---

- **Always Use `url_for()`**: Never hardcode internal URLs in templates or Python view functions.

---

---

### Q1: Why should you use `url_for()` instead of hardcoding URL strings in Flask?
**Answer**: `url_for()` generates URLs dynamically based on view function names rather than fixed paths. If you refactor a route path from `/user/profile` to `/account/settings`, `url_for('user_profile')` automatically reflects the change across all templates without breaking links.

---

---

```json
{
  "quiz_title": "Lesson 2.1 Routing Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which URL converter type allows path parameters containing forward slashes `/`?",
      "options": ["string", "path", "text", "all"],
      "correct_answer_index": 1,
      "explanation": "The path converter accepts strings containing forward slashes."
    }
  ]
}
```

---

---

Build a Flask app routing system with typed `int`, `uuid`, and `path` converters.

---

---

**Front**: What function generates reverse URL paths in Flask?
**Back**: `url_for('function_name', **kwargs)`.
<!-- flashcard:end -->

---

---

```python
@app.route("/item/<int:id>")
def get_item(id): return f"Item {id}"
```

---

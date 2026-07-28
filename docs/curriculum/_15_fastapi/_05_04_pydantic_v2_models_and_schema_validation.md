```yaml
schema_version: "2.0"
metadata:
  lesson_id: "FAP-MOD02-LES02"
  course_slug: "course-05-fastapi"
  course_title: "Course 5: FastAPI High-Performance Microservices"
  module_slug: "mod-02-request-validation-pydantic"
  module_title: "Module 2 - Request Validation & Pydantic Data Models"
  lesson_slug: "pydantic-v2-models-and-schema-validation"
  lesson_title: "Lesson 2.2 Pydantic v2 Models & Schema Validation"
  sort_order: 202

pedagogy:
  difficulty: "intermediate"
  estimated_time:
    reading_minutes: 20
    practice_minutes: 25
    quiz_minutes: 10
    total_minutes: 55
  bloom_taxonomy_level: "Apply"
  xp_reward: 60

prerequisites:
  required_lesson_ids:
    - "FAP-MOD02-LES01"
  required_skills:
    - "FastAPI Parameter Parsing & Python Type Annotations"

skills_acquired:
  - "Defining Pydantic v2 Schema Models (`BaseModel`)"
  - "Configuring Field Constraints (`Field(gt=0, max_length=50)`)"
  - "Writing Custom Field Validators (`@field_validator`)"
  - "Writing Custom Root Model Validators (`@model_validator`)"
  - "Nested Pydantic Model Structures"

dependencies:
  software:
    - "VS Code"
    - "Python 3.12+"
    - "fastapi"
    - "pydantic"
  hardware: []

seo_and_social:
  meta_title: "Pydantic v2 in FastAPI: BaseModel, Field Constraints & @field_validator"
  meta_description: "Master Pydantic v2 Schema Validation in FastAPI: BaseModel inheritance, Field constraints, @field_validator methods, @model_validator, and nested JSON schemas."
  keywords: ["Pydantic v2", "BaseModel", "FastAPI Pydantic", "Field validation", "@field_validator", "@model_validator", "JSON Schema"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 2.2 Pydantic v2 Models & Schema Validation

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 2.1 Parameters](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_05_fastapi/_05_03_path_and_query_parameters.md)
- **XP Reward**: +60 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Define request body payloads using **Pydantic v2 `BaseModel`**.
2. Apply declarative field constraints using **`Field()`**.
3. Implement custom field validation rules using **`@field_validator`**.
4. Construct complex multi-field rules using **`@model_validator`** and nested schemas.

---

## 2. Environment & Prerequisites [id: prerequisites]

Open Python REPL or VS Code.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 Pydantic v2 Architecture
**Pydantic v2** is a high-performance data validation library written in Rust (`pydantic-core`). In FastAPI, declaring a parameter annotated with a `BaseModel` subclass automatically parses, validates, and deserializes incoming JSON request bodies:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       PYDANTIC V2 SCHEMA VALIDATION PIPELINE                │
├─────────────────────────────────────────────────────────────────────────────┤
│ Client JSON Payload ──► FastAPI inspects `payload: SensorPayload`            │
│                     ──► Pydantic Core (Rust) validates type & constraints   │
│                     ──► Runs `@field_validator` rules                       │
│                     ──► Passes validated Python object to view function     │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    Req[Incoming POST JSON Payload] --> Pydantic["Pydantic v2 BaseModel Engine"]
    Pydantic --> FieldCheck{Field Constraints & Types Valid?}
    FieldCheck -->|Pass| CustomCheck{"@field_validator Methods"}
    FieldCheck -->|Fail| 422[Return HTTP 422 with detailed JSON error path]
    CustomCheck -->|Pass| ValidModel[Instantiates Validated Python Model]
    CustomCheck -->|Fail| 422
```

---

## 5. Code & Hardware Implementation [id: syntax]

```python
# Pydantic v2 Schema Models & Custom Validation (pydantic_demo.py)
from enum import Enum
from fastapi import FastAPI, status
from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator

app = FastAPI(title="Pydantic v2 Telemetry API")

class SensorType(str, Enum):
    TEMPERATURE = "TEMPERATURE"
    HUMIDITY = "HUMIDITY"
    PRESSURE = "PRESSURE"

# 1. Nested Location Model
class LocationConfig(BaseModel):
    building: str = Field(..., min_length=2, max_length=50)
    floor: int = Field(..., ge=-2, le=100)

# 2. Main Pydantic Request Body Model
class SensorRegistrationPayload(BaseModel):
    node_code: str = Field(..., min_length=3, max_length=20, pattern=r"^[A-Z0-9\-]+$")
    sensor_type: SensorType
    threshold: float = Field(..., gt=-50.0, lt=150.0)
    operator_email: EmailStr
    location: LocationConfig # Nested Schema!

    # Custom Field Validator
    @field_validator("node_code")
    @classmethod
    def validate_node_code(cls, value: str) -> str:
        if "ADMIN" in value:
            raise ValueError("The string 'ADMIN' is reserved and cannot be in node_code!")
        return value

    # Root Model Validator (Multi-field validation)
    @model_validator(mode="after")
    def validate_threshold_range(self) -> "SensorRegistrationPayload":
        if self.sensor_type == SensorType.HUMIDITY and self.threshold > 100.0:
            raise ValueError("Humidity threshold cannot exceed 100.0%!")
        return self

# REST Endpoint accepting Pydantic Payload
@app.post("/api/v1/sensors/register", status_code=status.HTTP_201_CREATED)
def register_sensor(payload: SensorRegistrationPayload):
    # payload is a fully validated Python SensorRegistrationPayload object!
    return {
        "status": "REGISTERED",
        "node_code": payload.node_code,
        "floor": payload.location.floor,
        "sensor_type": payload.sensor_type
    }
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Microservice Data Ingestion Gateways**: FastAPI services validate complex nested JSON payloads sent by IoT edge devices, ensuring bad sensor telemetry is caught and rejected at the API boundary before hitting database storage.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `pydantic_demo.py`.
2. Run `uvicorn pydantic_demo:app --reload`.
3. Send POST request with `"node_code": "ADMIN-NODE"` $\to$ Inspect exact JSON validation error output returned by Pydantic!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`ImportError: cannot import name 'validator'`** | Using Pydantic v1 syntax `@validator` in Pydantic v2. | In Pydantic v2, use `@field_validator` with `@classmethod` or `@model_validator(mode='after')`. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Use `@classmethod` on `@field_validator`**: In Pydantic v2, `@field_validator` functions must be declared as class methods (`@classmethod`).

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: What are the key improvements of Pydantic v2 over Pydantic v1 in FastAPI?
**Answer**: Pydantic v2 re-architected its core validation engine in Rust (`pydantic-core`), resulting in validation performance increases of 5x to 50x over v1. It introduces stricter type safety, improved error messages, clearer validator decorators (`@field_validator`, `@model_validator`), and faster JSON serialization.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 2.2 Pydantic v2 Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which base class must all Pydantic schema models inherit from?",
      "options": ["Schema", "BaseModel", "PydanticModel", "DataModel"],
      "correct_answer_index": 1,
      "explanation": "Pydantic models inherit from pydantic.BaseModel."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Build a Pydantic v2 schema for an e-commerce order with custom field validation rules.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: Which Pydantic v2 decorator handles custom validation rules on individual model fields?
**Back**: `@field_validator("field_name")`.
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```python
class Item(BaseModel):
    name: str = Field(..., min_length=3)
    @field_validator("name")
    @classmethod
    def check(cls, v): return v.upper()
```

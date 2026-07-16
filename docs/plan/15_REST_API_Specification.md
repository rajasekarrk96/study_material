# 15 — REST API Specification

> The REST API exposes programmatic interfaces for both content management and the student dashboard client.

---

## 15.1 API Specifications

All endpoints return JSON responses. Authentication uses session cookies for the main web-app or JWT Bearer tokens for external API accesses.

```
       ┌────────────────────────┐
       │   Bearer JWT Token     │
       └───────────┬────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
┌─────────────────┐ ┌─────────────────┐
│ /api/v1/lessons │ │  /api/v1/auth   │
│ Read Content    │ │ Verify Identity │
└─────────────────┘ └─────────────────┘
```

---

## 15.2 Core API Endpoints

### 1. Authentication
- `POST /api/v1/auth/login` - Authenticate users.
- `POST /api/v1/auth/logout` - Revoke current user session.
- `POST /api/v1/auth/register` - Create student account profile.

### 2. Courses & Modules
- `GET /api/v1/courses` - List published courses (filterable by tags, category, level).
- `GET /api/v1/courses/<id>` - Return course meta structure along with its modules.
- `GET /api/v1/courses/<id>/modules` - Fetch modules for a specific course.

### 3. Lessons & Contents
- `GET /api/v1/lessons/<id>` - Fetch full lesson metadata and visible sections.
- `GET /api/v1/lessons/<id>/sections` - Read content sections of a lesson.
- `POST /api/v1/lessons` - (Admin/Author only) Create new lesson draft.
- `PUT /api/v1/lessons/<id>` - (Admin/Author/Editor only) Edit lesson properties.

### 4. Assessments
- `POST /api/v1/quizzes/<id>/attempts` - Create quiz attempt session.
- `POST /api/v1/quizzes/attempts/<id>/submit` - Submit answers and return grades.
- `POST /api/v1/exercises/<id>/submit` - Submit coding solution for Judge0 grading.

### 5. Progress & Analytics
- `GET /api/v1/progress/summary` - Retrieve user completed lessons, streaks, level, and XP.
- `GET /api/v1/progress/xp-history` - List history of user XP earnings.

---

## 15.3 Endpoint Definition Sample (OpenAPI/Swagger Format)

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Learning OS API Reference",
    "version": "1.0.0"
  },
  "paths": {
    "/api/v1/lessons/{id}": {
      "get": {
        "summary": "Fetch lesson content by ID",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Lesson object details",
            "content": {
              "application": "json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "id": { "type": "integer" },
                    "title": { "type": "string" },
                    "summary": { "type": "string" },
                    "difficulty": { "type": "string" },
                    "sections": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "section_type": { "type": "string" },
                          "content_markdown": { "type": "string" }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

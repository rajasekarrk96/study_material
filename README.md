# Learning OS v3.0 — Bytes and Boards Solutions

> A modular, production-ready Knowledge Operating System built on a **reusable module-based catalog** architecture. Courses exist once as a single source of truth; Learning Paths reference them without duplicating any content — similar to Microsoft Learn and Coursera Learning Paths.

**Live Stack:** Flask 3 · TiDB Cloud (MySQL) · Gunicorn · Render · Ollama (local AI)

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Catalog Architecture (v3.0)](#2-catalog-architecture-v30)
3. [Current Skill Modules](#3-current-skill-modules)
4. [Learning Paths](#4-learning-paths)
5. [Architecture](#5-architecture)
6. [Domain Model](#6-domain-model)
7. [Blueprint Routes](#7-blueprint-routes)
8. [Feature Modules](#8-feature-modules)
9. [AI & Search Layer](#9-ai--search-layer)
10. [Technology Stack](#10-technology-stack)
11. [Directory Structure](#11-directory-structure)
12. [Data Flow](#12-data-flow)
13. [Setup & Local Development](#13-setup--local-development)
14. [Configuration Variables](#14-configuration-variables)
15. [Deployment](#15-deployment)
16. [Scripts Reference](#16-scripts-reference)
17. [Coding Standards](#17-coding-standards)
18. [Changelog](#18-changelog)
19. [Documentation Index](#19-documentation-index)

---

## 1. Project Overview

**Learning OS** is a database-driven knowledge processing platform built for **Bytes and Boards Solutions**. It organizes all learning content into a structured relational database, then exposes it through:

- A **modular skill catalog** — 10 flat skill categories (Programming, Frontend, Backend, Database, DevOps, Testing, AI, IoT, Cloud, Soft Skills)
- **Learning Paths** — curated multi-course programs (Python Full Stack, AI Engineer, IoT Full Stack, etc.) that *reference* existing courses without duplicating content
- An **interactive lesson reader** with section-based content and progress tracking
- An **assessment engine** (MCQ quizzes with XP rewards)
- A **spaced repetition system** (SRS/SM-2 flashcards)
- A **sandboxed code executor** (Judge0 API integration)
- A **hybrid semantic search** (keyword FTS + vector cosine similarity)
- A **local AI tutor** (Ollama) for on-demand lesson Q&A and content drafting
- A **gamification layer** (XP points, daily streaks, two certificate types)

```
  Raw Sources (PDF · YouTube · Markdown · HTML · Docs)
                        │
                        ▼
          [Knowledge Ingestion Pipeline]
          chunker → embedder → vector store
                        │
                        ▼
          [TiDB Cloud — MySQL-compatible DB]
          55+ tables across 10 domain modules
                        │
            ┌───────────┴───────────┐
            ▼                       ▼
  [Skill Catalog]           [Learning Paths]
  10 flat categories        Python Full Stack
  browse by skill           Java Full Stack
  no duplicates             AI Engineer ...
            │
            ▼
  [Student Learning Flow]
  Browse → Enroll Path → Course → Lesson → Quiz → SRS → XP → Certificate
```

---

## 2. Catalog Architecture (v3.0)

### The Core Principle

> Each course exists **exactly once** in the database. Learning Paths reference courses — they never copy lessons.

```
v2.x (OLD — deprecated)           v3.0 (CURRENT)
─────────────────────────          ──────────────────────────────────────
Python Full Stack                  Programming Languages  ← Skill Module
  ├── Python (lessons)               └── Python Course (single source)
  ├── HTML  (lessons)
  ├── Flask (lessons)               Frontend Development  ← Skill Module
                                      ├── HTML Course
IoT Full Stack                        ├── CSS Course
  ├── Python (lessons) ← DUPE!        ├── Bootstrap Course
  ├── Flask  (lessons) ← DUPE!        └── JavaScript Course
  └── Arduino (lessons)
                                    Learning Path: Python Full Stack
                                      references → Python, HTML, CSS,
                                                   Bootstrap, JS, Flask,
                                                   MySQL, Git
                                    Learning Path: IoT Full Stack
                                      references → Python, Flask,
                                                   HTML, CSS, Arduino
                                                   (Python is NOT copied)
```

### Content Hierarchy

```
Category  (10 flat skill groups)
  └── Subject  (topic within a category)
        └── Course  (single reusable unit, soft-delete, versioned)
              └── Module
                    └── Lesson
                          └── LessonSection (concept|syntax|example|pitfall|qa)

LearningPath  (curated program)
  └── PathCourse  (JOIN: path ↔ course, with section_label + is_required)
        └── references → Course (no data copied)
```

---

## 3. Current Skill Modules

### Programming Languages
| Course | Hours |
|--------|------:|
| Core Python | 40h |
| Java (Core Java + Advanced) | 62h |
| C Programming | 16h |

### Frontend Development
| Course | Hours |
|--------|------:|
| HTML5 | 6h |
| CSS3 | 11h |
| Bootstrap | 18h |
| jQuery | 12h |
| JavaScript | 13h |

### Backend Development
| Course | Hours |
|--------|------:|
| Python Flask | 12h |
| FastAPI | 18h |

### Database
| Course | Hours |
|--------|------:|
| MySQL | 25h |
| MongoDB | 13h |

### Git & DevOps
| Course | Hours |
|--------|------:|
| Git Masterclass | 5h |
| Jenkins CI/CD | — |

### Testing & QA
| Course | Hours |
|--------|------:|
| Selenium Java (Automation Testing) | — |
| Manual Testing | — |

### AI & Data Science *(7 courses)*
Machine Learning, Deep Learning, NLP, Computer Vision, AI Agents, Prompt Engineering, Python Data Science

### IoT & Embedded Systems *(in progress)*
Arduino, ESP32, Raspberry Pi, Sensors, MQTT, Embedded C, IoT Cloud

### Cloud Computing *(planned)*
AWS, Azure, Google Cloud, Firebase

### Soft Skills *(planned)*
Aptitude, Interview Prep, Resume Building, Communication

---

## 4. Learning Paths

Learning Paths are curated sequences that guide a student from beginner to job-ready. Each path references existing courses — **zero duplication**.

| Path | Courses | Hours | Featured |
|------|--------:|------:|:--------:|
| Python Full Stack | 11 | 208h | ⭐ |
| Java Full Stack | 7 | 135h | ⭐ |
| IoT Full Stack | 8 | 141h | ⭐ |
| AI Engineer | 4 | 95h | ⭐ |
| Data Scientist | 2 | 65h | — |
| ML Engineer | 1 | 40h | — |
| DevOps Engineer | 1 | 40h | — |
| QA Automation Engineer | 3 | 105h | — |

### Example: Python Full Stack Path

```
Section          Course
────────────     ─────────────────────────────
Programming  →   Core Python          (required)
Frontend     →   HTML5                (required)
Frontend     →   CSS3                 (required)
Frontend     →   Bootstrap            (required)
Frontend     →   JavaScript           (required)
Frontend     →   jQuery               (optional)
Database     →   MySQL                (required)
Backend      →   Flask                (required)
Backend      →   FastAPI              (optional)
Database     →   MongoDB              (optional)
```

### Example: IoT Full Stack Path *(shares courses with Python Full Stack)*

```
Section          Course
────────────     ─────────────────────────────
Programming  →   Core Python          (required) ← same course, no duplicate
Programming  →   C Programming        (required)
Frontend     →   HTML5                (required) ← same course, no duplicate
Frontend     →   CSS3                 (required)
Frontend     →   Bootstrap            (required)
Frontend     →   JavaScript           (required)
Backend      →   Flask                (required) ← same course, no duplicate
Database     →   MySQL                (required)
```

---

## 5. Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                        Flask Application                         │
│                                                                  │
│  ┌─────────┐  ┌──────────┐  ┌──────────┐  ┌───────────────┐    │
│  │  public │  │   auth   │  │  learn   │  │     admin     │    │
│  │  /      │  │  /auth   │  │  /learn  │  │  /admin       │    │
│  │ /catalog│  │          │  │          │  │               │    │
│  │ /paths  │  │          │  │          │  │               │    │
│  └─────────┘  └──────────┘  └──────────┘  └───────────────┘    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌───────────────┐   │
│  │assessment│  │ sandbox  │  │   srs    │  │    study      │   │
│  └──────────┘  └──────────┘  └──────────┘  └───────────────┘   │
│                            ┌─────────┐                          │
│                            │   ai    │                          │
│                            └─────────┘                          │
│                                                                  │
│  ┌───────────────── Domain Services ────────────────────────┐   │
│  │  learning.py · search_service.py · lab.py · gamification │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌───────────────── Domain Models (ORM) ────────────────────┐   │
│  │  auth · content · assessment · srs · gamification        │   │
│  │  learning_path · sandbox · study · knowledge · tutor      │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌──────────────── TiDB Cloud (MySQL) ──────────────────────┐   │
│  │  55+ tables · SSL/TLS · connection pooling               │   │
│  └──────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────┘
```

---

## 6. Domain Model

### Content Domain

```
Category  (10 flat skill groups, sort_order, icon, color)
  └── Subject  (topic area within category)
        └── Course  (SoftDeleteMixin, Certificate auto-seeded)
              └── Module  (is_published, sort_order)
                    └── Lesson  (SoftDeleteMixin, view_count)
                          └── LessonSection  (section_type, is_visible)
```

Supporting models: `Tag`, `Source`, `ContentQualityScore`, `CourseStatistics`, `LessonStatistics`, `GlossaryTerm`, `CommandReference`, `Lab`, `LabStep`, `Assignment`, `DiscussionThread`

### Learning Path Domain *(v3.0 extended)*

| Model | Purpose |
|-------|---------|
| `LearningPath` | A curated program (title, slug, target_role, difficulty, estimated_hours, icon, color, is_featured) |
| `PathCourse` | JOIN: path ↔ course — adds `section_label` (e.g. "Frontend") and `is_required` flag |
| `PathPrerequisite` | Per-course prerequisite graph |
| `UserCourseProgress` | Per-user, per-course completion record |
| `UserLessonProgress` | Per-user, per-lesson completion record |
| `UserLearningPathProgress` | Per-user, per-path enrollment + completed_courses count + percentage |
| `LearningPathCertificate` | Certificate definition for completing a full path |
| `UserLearningPathCertificate` | Issued path-level certificate to a specific user |

### Auth Domain
`User`, `Role` — 7 RBAC levels: `super_admin → admin → editor → reviewer → author → moderator → student`

### Assessment Domain
`Quiz`, `Question`, `Option`, `QuizAttempt`, `QuizAnswer` — MCQ, true/false, free-text, timed sessions, XP rewards

### SRS Domain (Spaced Repetition)
`FlashcardDeck`, `Flashcard`, `UserFlashcardProgress`
- SM-2 algorithm: `ease_factor`, `interval_days`, `repetitions`, `next_review_at`

### Gamification Domain
`UserXPLog`, `UserStreak` — XP per activity, daily streaks

### Knowledge Domain (Vector Search)
`KnowledgeSource`, `SourceDocument`, `KnowledgeChunk`, `ChunkEmbedding`
- 500-char chunks, `nomic-embed-text` embeddings stored as JSON in TiDB

---

## 7. Blueprint Routes

| Blueprint | Prefix | Key Routes |
|-----------|--------|-----------|
| `public` | `/` | Home dashboard, `/catalog` (two-tab UI), `/paths/`, `/paths/<slug>/`, `/paths/<slug>/enroll`, `/search`, `/sitemap.xml` |
| `auth` | `/auth` | `/login`, `/register`, `/logout`, `/profile` |
| `learn` | `/learn` | `/<slug>/` course overview, `/<slug>/<mod>/<lesson>/`, progress, labs, certificates |
| `assessment` | — | Quiz start, submit, results |
| `sandbox` | `/sandbox` | Code editor, run, submit |
| `srs` | `/srs` | Flashcard review, SM-2 scheduling |
| `study` | `/study` | Notes, study sessions |
| `ai` | `/ai` | Tutor chat, lesson Q&A, AI draft generation |
| `admin` | `/admin` | Content CMS, path management, user management, ingestion dashboard |

---

## 8. Feature Modules

### Two-Tab Catalog UI (`/catalog`)

**Tab 1 — Browse Skills:**
- Horizontally scrollable category filter pills (one per skill category, color-coded)
- Clicking a pill filters the course grid to that category
- Each course card shows title, difficulty, hours, views

**Tab 2 — Learning Paths:**
- Path cards with icon, title, target role, difficulty badge, hours, course count, lesson count
- Per-user progress bar if enrolled
- "View Path" / "Continue Path" CTA button
- URL hash routing (`/catalog#paths`)

### Learning Path Detail (`/paths/<slug>/`)
- Hero section: icon, title, target role, description
- Stats bar: courses, hours, lessons, certificate badge
- Enroll button (POST `/paths/<slug>/enroll`)
- Curriculum grouped by section (Programming / Frontend / Backend / Database)
- Per-course completion checkmarks for enrolled users

### Progress Tracking (Multi-Level)
```
Lesson completed
    ↓ UserLessonProgress (is_completed=True)
    ↓ XPService.award(+10 XP)
    ↓ StreakService.update_streak()
Course completed
    ↓ UserCourseProgress (is_completed=True)
    ↓ Course Certificate issued
    ↓ UserLearningPathProgress.completed_courses += 1 (for all paths referencing it)
Path completed
    ↓ UserLearningPathProgress (is_completed=True)
    ↓ LearningPath Certificate issued
```

### Two Certificate Types
1. **Course Certificate** — issued after completing all lessons in an individual course
2. **Learning Path Certificate** — issued after completing all required courses in a path

### Lesson Reader
- Section-based: `concept → syntax → example → pitfall → qa`
- Syntax highlighting (Highlight.js), Mermaid diagrams, Markdown rendering
- View count tracking, next-lesson navigation

### Quiz Engine
- Timed/untimed MCQ with auto-grading, pass/fail, XP reward

### Flashcard SRS (SM-2)
- Per-card ease factor, interval scheduling, `next_review_at` queue

### Code Sandbox
- Multi-language execution via Judge0 API, lab-step validation

### Admin CMS
- Category / Subject / Course / Module / Lesson CRUD
- Learning Path builder: assign courses, set section labels, mark required/optional, reorder
- Knowledge source ingestion dashboard, user and role management

---

## 9. AI & Search Layer

### Hybrid Search Pipeline

```
User Query
    │
    ├──► FTS Keyword Scan  (SQLAlchemy LIKE / full-text)
    │
    └──► Vector Cosine Similarity  (ChunkEmbedding JSON dot product)
              │
              └──► Ranked merged results → /search page
```

### AI Provider Abstraction

```
AI_PROVIDER env var
    ├── "ollama"  → http://localhost:11434  (qwen2.5-coder:7b)
    ├── "openai"  → OpenAI API
    └── "gemini"  → Google Gemini API
```

Switching providers requires only an `.env` change — no code changes.

### Knowledge Ingestion Flow

```
1. Admin adds source (PDF / YouTube / Markdown)
2. chunker.py → 500-char KnowledgeChunks
3. Ollama nomic-embed-text → float vectors
4. ChunkEmbedding stored as JSON in TiDB
5. SearchIndexService.rebuild_search_index() on startup
6. AI Tutor uses hybrid_search() for RAG responses
```

---

## 10. Technology Stack

| Layer | Technology |
|-------|-----------|
| **Web Framework** | Flask 3.0 + Gunicorn 22 |
| **ORM** | SQLAlchemy 2.0 + Flask-SQLAlchemy 3.1 |
| **Database** | TiDB Cloud (MySQL-compatible) via PyMySQL · SSL/TLS |
| **Auth** | Flask-Login 0.6 · Werkzeug · PyJWT |
| **Security** | Flask-WTF (CSRF) · Flask-Limiter · Bleach (XSS) |
| **AI / LLM** | Ollama (local) · OpenAI API · Google Gemini API |
| **Embeddings** | `nomic-embed-text` via Ollama |
| **Code Execution** | Judge0 API · Piston API |
| **Frontend** | Vanilla JS · Bootstrap 5 · Highlight.js · Mermaid · EasyMDE |
| **Templating** | Jinja2 3.1 + Python `markdown` |
| **Schema Migrations** | Alembic 1.13 + raw ALTER TABLE scripts |
| **Deployment** | Render (Web Service) · TiDB Cloud (DB) |

---

## 11. Directory Structure

```
notes/  (Learning OS root)
│
├── app/
│   ├── __init__.py                 # App factory: extensions, blueprints, context processors
│   ├── blueprints/
│   │   ├── admin/routes.py         # CMS, path builder, user management
│   │   ├── ai/routes.py            # AI tutor chat, draft generation
│   │   ├── assessment/routes.py    # Quiz flow: start → submit → results
│   │   ├── auth/routes.py          # Login, register, logout, profile
│   │   ├── learn/routes.py         # Course overview, lesson reader, labs, certificates
│   │   ├── public/routes.py        # Home, /catalog, /paths/, /paths/<slug>/, enroll, sitemap
│   │   ├── sandbox/routes.py       # Code editor and execution
│   │   ├── srs/routes.py           # Flashcard review sessions
│   │   └── study/routes.py         # Notes and study sessions
│   │
│   ├── core/
│   │   ├── base_model.py           # TimestampMixin, SoftDeleteMixin (is_deleted + deleted_at)
│   │   ├── cache.py                # cache_memoize decorator
│   │   ├── config.py               # Config dataclass (DATABASE_TYPE, TiDB, AI)
│   │   ├── constants.py            # Enums: UserRole, ContentStatus, DifficultyLevel, SectionType
│   │   └── extensions.py           # db, login_manager, csrf, limiter singletons
│   │
│   ├── domains/
│   │   ├── auth/models.py          # User, Role, Permission, RolePermission
│   │   ├── content/models.py       # Category, Subject, Course, Module, Lesson, LessonSection, ...
│   │   ├── assessment/models.py    # Quiz, Question, Option, QuizAttempt, QuizAnswer
│   │   ├── gamification/
│   │   │   ├── models.py           # UserXPLog, UserStreak
│   │   │   └── service.py          # XP award + streak update logic
│   │   ├── knowledge/
│   │   │   ├── models.py           # KnowledgeSource, SourceDocument, KnowledgeChunk, ChunkEmbedding
│   │   │   ├── chunker.py          # Text → 500-char segments
│   │   │   └── search.py           # hybrid_search(): FTS + vector cosine
│   │   ├── learning_path/
│   │   │   └── models.py           # LearningPath, PathCourse, PathPrerequisite
│   │   │                           # UserCourseProgress, UserLessonProgress
│   │   │                           # UserLearningPathProgress       ← v3.0 NEW
│   │   │                           # LearningPathCertificate        ← v3.0 NEW
│   │   │                           # UserLearningPathCertificate    ← v3.0 NEW
│   │   ├── sandbox/models.py       # Code submission and result models
│   │   ├── srs/models.py           # FlashcardDeck, Flashcard, UserFlashcardProgress (SM-2)
│   │   ├── study/models.py         # Study session and notes models
│   │   └── tutor/models.py         # AI tutor conversation models
│   │
│   ├── services/
│   │   ├── learning.py             # DashboardService, LearningProgressService, CertificateService
│   │   ├── search_service.py       # SearchIndexService.rebuild_search_index()
│   │   ├── lab.py                  # Lab execution helpers
│   │   └── lab_validation.py       # Judge0 result validation
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── public/
│   │   │   ├── catalog.html              # Two-tab: Browse Skills + Learning Paths
│   │   │   ├── learning_path_detail.html # Path hero, curriculum sections, enroll
│   │   │   ├── home.html
│   │   │   ├── dashboard.html
│   │   │   └── search.html
│   │   ├── learn/                  # course_overview.html, lesson.html, certificate_*.html
│   │   ├── admin/                  # CMS dashboards
│   │   ├── auth/
│   │   └── components/             # _navbar.html, _sidebar.html
│   │
│   └── static/
│       ├── css/
│       ├── js/
│       └── images/
│
├── scripts/
│   ├── schema_migration_v3.py      # ALTER TABLE + CREATE TABLE for v3 new columns/tables
│   ├── migrate_catalog_v3.py       # v3 catalog migration: new categories, subject moves, paths
│   ├── fix_is_deleted_flag.py      # Sync deleted_at → is_deleted boolean
│   ├── audit_catalog.py            # Catalog health audit
│   ├── fix_catalog_issues.py       # Fix category misplacements, merge duplicates
│   ├── scaffold_new_courses.py     # Bulk-create lesson stub files
│   ├── phase2_upgrade.py           # Phase 2 content migration
│   ├── phase3_python_content.py    # Python course content seeder
│   ├── phase4_content.py           # Multi-course content seeder
│   ├── phase5_content_p1.py        # AI/ML course content seeder part 1
│   └── phase5_content_p2.py        # AI/ML course content seeder part 2
│
├── docs/plan/                      # 21 full technical architecture docs
├── .env                            # Local secrets (never committed)
├── .env.example                    # Environment variable template
├── render.yaml                     # Render.com deployment (Gunicorn, 2 workers)
├── requirements.txt                # Python dependencies
├── run.py                          # WSGI entrypoint
└── isrgrootx1.pem                  # TiDB Cloud SSL CA certificate
```

---

## 12. Data Flow

### Student Learning Flow

```
1. /catalog  Tab: Browse Skills
             → Filter by category pill → Course grid → click course

   /catalog  Tab: Learning Paths
             → View path card → /paths/<slug>/
             → POST /paths/<slug>/enroll → UserLearningPathProgress created

2. /learn/<slug>/
             → Course overview: modules, progress bar, next lesson

3. /learn/<slug>/<module>/<lesson>/
             → Lesson reader: concept, syntax, example, pitfall, Q&A
             → POST /learn/lessons/<id>/complete
               → UserLessonProgress(is_completed=True)
               → XPService.award(+10 XP, "lesson_completed")
               → StreakService.update_streak()
               → if all lessons done: UserCourseProgress(is_completed=True)
                                      Course Certificate issued
                                      UserLearningPathProgress.completed_courses += 1
                                      if path complete: Path Certificate issued

4. /quiz/<id>       → MCQ quiz → auto-grade → XP awarded
5. /srs             → Flashcard SM-2 review queue
6. /sandbox         → Code execution via Judge0
7. /learn/certificates/  → Course + Path certificates
```

### Admin Content Authoring Flow

```
1. /admin/sources      → Add KnowledgeSource
2. chunker.py          → KnowledgeChunks (500 chars)
3. Ollama embed        → ChunkEmbedding vectors
4. /admin/lessons      → Create Lesson + LessonSections
5. /ai/draft           → RAG: hybrid_search() + Ollama completion
6. Review              → ContentQualityScore
7. Publish             → lesson.status = "published"
8. /admin/paths        → Create/edit LearningPath, assign courses,
                         set section_label, mark required/optional, reorder
```

---

## 13. Setup & Local Development

### Prerequisites
- Python 3.11+
- Git
- Ollama (for local AI features)

### Installation

```bash
git clone https://github.com/rajasekarrk96/study_material.git
cd study_material
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
copy .env.example .env        # Fill in your values
```

### Database Initialization

Tables are auto-created on first run. For v3.0, run the schema migration first:

```bash
python scripts/schema_migration_v3.py   # Add v3 columns + new tables
python scripts/migrate_catalog_v3.py    # Seed new categories + learning paths
python run.py
```

### Local AI Setup

```bash
ollama pull qwen2.5-coder:7b    # Chat/code model
ollama pull nomic-embed-text    # Embedding model
```

### Run Development Server

```bash
python run.py
# Open http://localhost:5000
```

---

## 14. Configuration Variables

```env
# ── Application ──────────────────────────────────────────────
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-flask-secret-key
ENCRYPTION_KEY=your-fernet-key

# ── Database ─────────────────────────────────────────────────
DATABASE_TYPE=tidb
DATABASE_URL=mysql+pymysql://user:pass@host:4000/db?ssl_ca=isrgrootx1.pem&ssl_verify_cert=true
TIDB_HOST=gateway01.us-east-1.prod.aws.tidbcloud.com
TIDB_PORT=4000
TIDB_USER=your-tidb-user
TIDB_PASSWORD=your-tidb-password
TIDB_DATABASE=test
TIDB_CA_PATH=isrgrootx1.pem

# ── AI Provider ───────────────────────────────────────────────
AI_PROVIDER=ollama
OLLAMA_API_BASE_URL=http://localhost:11434
OLLAMA_MODEL_NAME=qwen2.5-coder:7b
OPENAI_API_KEY=
GEMINI_API_KEY=

# ── Code Execution ────────────────────────────────────────────
JUDGE0_API_URL=https://api.judge0.com
JUDGE0_API_KEY=your-judge0-key

# ── Performance ───────────────────────────────────────────────
SKIP_SEARCH_REBUILD=1
```

---

## 15. Deployment

```yaml
# render.yaml summary
service: learning-os
runtime: python
buildCommand: pip install -r requirements.txt
startCommand: gunicorn run:app --workers 2 --threads 2 --timeout 120 --bind 0.0.0.0:$PORT
healthCheckPath: /
region: oregon
```

**Database:** TiDB Cloud (MySQL 8.0-compatible, serverless) via SSL/TLS (`isrgrootx1.pem`)

---

## 16. Scripts Reference

| Script | Purpose |
|--------|---------|
| `schema_migration_v3.py` | **v3.0** ALTER TABLE + CREATE TABLE for new columns and tables |
| `migrate_catalog_v3.py` | **v3.0** Create 10 skill categories, remap subjects, deactivate old categories, seed 8 learning paths |
| `audit_catalog.py` | Audit categories for duplicates, wrong placements, empty courses |
| `fix_catalog_issues.py` | Fix misplacements, merge duplicates, recalculate hours |
| `fix_is_deleted_flag.py` | Sync `deleted_at` → `is_deleted` boolean |
| `scaffold_new_courses.py` | Bulk-create markdown lesson stub files |
| `phase2_upgrade.py` | Phase 2 DB content migration |
| `phase3_python_content.py` | Python course full content seeder |
| `phase4_content.py` | Multi-course content seeder |
| `phase5_content_p1/p2.py` | AI/ML course content seeders |
| `db_backup.py` | Database backup utility |
| `migrate_html.py` | Import HTML notes into DB |
| `migrate_markdown.py` | Import Markdown notes into DB |

---

## 17. Coding Standards

1. **Courses are the single source of truth** — never copy lesson data between paths. Use `PathCourse` references.
2. **Always soft-delete correctly** — set **both** `is_deleted = True` AND `deleted_at = datetime.utcnow()`.
3. **ORM only** — never raw SQL in application code. Raw SQL only in one-off migration scripts.
4. **Audit trails** — all new models must inherit `TimestampMixin`.
5. **RBAC** — use role-check decorators on all admin/editor routes.
6. **Slug uniqueness** — free old slug with `db.session.flush()` before assigning a new one.
7. **No secrets in code** — all credentials via `.env`.
8. **Schema changes** — add new columns via `schema_migration_*.py` scripts (ALTER TABLE), not just model changes.

---

## 18. Changelog

| Version | Date | Summary |
|---------|------|---------|
| v1.0.0 | 2025 | Initial CMS: courses, quizzes, streak engines, code execution |
| v2.0.0 | 2025 | Vector search (TiDB), Ollama LLM, multi-source ingestion, SRS SM-2 |
| v2.1.0 | 2026-01 | IoT & Hardware Full Stack catalog (7 courses, 150+ lessons) |
| v2.2.0 | 2026-04 | Python AI & Data Science catalog (ML, DL, NLP, CV, MLOps, RAG, Agents) |
| v2.3.0 | 2026-07-29 | Catalog cleanup: fix Java/C in Python Full Stack, merge duplicate Python, recalc hours |
| **v3.0.0** | **2026-07-29** | **Modular catalog redesign: 10 flat skill categories, 8 learning paths (no duplication), extended LearningPath model (target_role, difficulty, icon, color, is_featured), new UserLearningPathProgress + LearningPathCertificate tables, two-tab catalog UI (Browse Skills / Learning Paths), new /paths/ routes** |

---

## 19. Documentation Index

| Document | Purpose |
|----------|---------|
| [Master Plan](docs/plan/00_LEARNING_OS_MASTER_PLAN.md) | Baseline architecture & decisions |
| [Enhancement Plan](docs/plan/00_LEARNING_OS_v2.0_ENHANCEMENT_PLAN.md) | v2.0 evolution guide |
| [Product Vision](docs/plan/01_Product_Vision.md) | Value proposition & universal schema |
| [Information Architecture](docs/plan/02_Information_Architecture.md) | Site map, taxonomy & slugs |
| [User Roles (RBAC)](docs/plan/03_User_Roles_RBAC.md) | Role permissions & CMS state rules |
| [Database ERD](docs/plan/04_Database_ERD.md) | 55+ table schema definitions |
| [Folder Structure](docs/plan/05_Folder_Structure.md) | Project directories blueprint |
| [CMS Design](docs/plan/06_CMS_Design.md) | Editor workflow & source attributions |
| [Learning Engine](docs/plan/07_Learning_Engine.md) | Prerequisites & spaced repetition SM-2 |
| [Progress Engine](docs/plan/08_Progress_Engine.md) | XP levels & streak calculations |
| [Exercise Engine](docs/plan/09_Exercise_Engine.md) | Auto-grading & sandboxes |
| [Quiz Engine](docs/plan/10_Quiz_Engine.md) | Question banks & validations |
| [Achievement Engine](docs/plan/11_Achievement_Engine.md) | Badge allocation & criteria |
| [Search Architecture](docs/plan/12_Search_Architecture.md) | FTS + vector hybrid search |
| [Recommendation Engine](docs/plan/13_Recommendation_Engine.md) | Cosine similarity & RAG |
| [AI Integration](docs/plan/14_AI_Integration_Layer.md) | Provider abstraction & Ollama |
| [REST API Reference](docs/plan/15_REST_API_Specification.md) | OpenAPI endpoint maps |
| [Admin Panels](docs/plan/16_Admin_Dashboard.md) | Reviews, roles & ingestion dashboard |
| [Student Dashboard](docs/plan/17_Student_Dashboard.md) | Spaced repetition & user UI |
| [SEO Strategy](docs/plan/18_SEO_Strategy.md) | JSON-LD schema & sitemap |
| [Security Architecture](docs/plan/19_Security_Architecture.md) | Hashing, CSRF & rate limits |
| [Deployment Architecture](docs/plan/20_Deployment_Architecture.md) | Render & TiDB setup |
| [Implementation Roadmap](docs/plan/21_Implementation_Roadmap.md) | Phase checklists & sprint goals |

---

## License

Private & Proprietary — All Rights Reserved.  
© 2026 Bytes and Boards Solutions.

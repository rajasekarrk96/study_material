# Learning OS — Bytes and Boards Solutions

> A modular, production-ready Knowledge Operating System that transforms scattered learning resources into a structured, interactive education platform with AI assistance, adaptive learning paths, and gamification.

**Live Stack:** Flask 3 · TiDB Cloud (MySQL) · Gunicorn · Render · Ollama (local AI)

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Current Catalog](#2-current-catalog)
3. [Architecture](#3-architecture)
4. [Domain Model](#4-domain-model)
5. [Blueprint Routes](#5-blueprint-routes)
6. [Feature Modules](#6-feature-modules)
7. [AI & Search Layer](#7-ai--search-layer)
8. [Technology Stack](#8-technology-stack)
9. [Directory Structure](#9-directory-structure)
10. [Data Flow](#10-data-flow)
11. [Setup & Local Development](#11-setup--local-development)
12. [Configuration Variables](#12-configuration-variables)
13. [Deployment](#13-deployment)
14. [Scripts Reference](#14-scripts-reference)
15. [Coding Standards](#15-coding-standards)
16. [Changelog](#16-changelog)
17. [Documentation Index](#17-documentation-index)

---

## 1. Project Overview

**Learning OS** is a database-driven knowledge processing platform built for **Bytes and Boards Solutions**. Rather than serving static tutorials, it organizes all learning content into a structured relational database, then exposes it through:

- A **course catalog** with category → subject → course → module → lesson hierarchy
- An **interactive lesson reader** with progress tracking and section-based content
- An **assessment engine** (MCQ quizzes with XP rewards)
- A **spaced repetition system** (SRS/SM-2 flashcards)
- A **sandboxed code executor** (Judge0 API integration)
- A **hybrid semantic search** (keyword FTS + vector cosine similarity)
- A **local AI tutor** (Ollama) for on-demand lesson Q&A and content drafting
- A **gamification layer** (XP points, daily streaks, certificates)

```
  Raw Sources (PDF · YouTube · Markdown · HTML · Docs)
                        │
                        ▼
          [Knowledge Ingestion Pipeline]
          chunker → embedder → vector store
                        │
                        ▼
          [TiDB Cloud — MySQL-compatible DB]
          48+ tables across 10 domain modules
                        │
              ┌─────────┴──────────┐
              ▼                    ▼
    [Lesson CMS / Admin]   [AI Tutor / Search]
    Author → Review → Pub  Hybrid FTS + Vectors
              │
              ▼
    [Student Learning Flow]
    Catalog → Course → Lesson → Quiz → SRS → XP → Certificate
```

---

## 2. Current Catalog

### Python Full Stack *(10 courses)*
End-to-end web development with HTML5, CSS3, JavaScript, Python, Flask, FastAPI, MySQL, and MongoDB.

| Course | Hours | Modules | Lessons |
|--------|------:|--------:|--------:|
| Core Python | 40h | 15 | 44 |
| MySQL | 25h | 6 | 53 |
| Flask | 12h | 3 | 32 |
| FastAPI | 18h | 4 | 33 |
| JavaScript | 13h | 1 | 52 |
| CSS3 | 11h | 1 | 45 |
| HTML5 | 6h | 1 | 24 |
| Bootstrap | 18h | 4 | 18 |
| jQuery | 12h | 4 | 12 |
| MongoDB | 13h | 4 | 13 |

### Programming Languages *(3 courses)*

| Course | Hours | Modules | Lessons |
|--------|------:|--------:|--------:|
| Core Java | 40h | 16 | 160 |
| Java | 22h | 7 | 26 |
| C Programming | 16h | 6 | 18 |

### Software Engineering & DevOps *(4 courses)*
Git Masterclass, Jenkins CI/CD, DevOps fundamentals, and more.

### Python AI & Data Science *(8 courses)*
Machine Learning, Deep Learning, NLP, Computer Vision, MLOps, RAG, AI Agents, Prompt Engineering, and Python Data Science.

### Databases & Business Intelligence *(2 courses)*
SQL Server, Power BI.

### IoT & Hardware Full Stack *(7 courses)*
Arduino, Raspberry Pi, sensors, protocols, and embedded systems.

---

## 3. Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                        Flask Application                         │
│                                                                  │
│  ┌─────────┐  ┌──────────┐  ┌──────────┐  ┌───────────────┐    │
│  │  public │  │   auth   │  │  learn   │  │     admin     │    │
│  │  /      │  │  /auth   │  │  /learn  │  │  /admin       │    │
│  └─────────┘  └──────────┘  └──────────┘  └───────────────┘    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌───────────────┐   │
│  │assessment│  │ sandbox  │  │   srs    │  │    study      │   │
│  │  /quiz   │  │ /sandbox │  │  /srs    │  │  /study       │   │
│  └──────────┘  └──────────┘  └──────────┘  └───────────────┘   │
│                            ┌─────────┐                          │
│                            │   ai    │                          │
│                            │  /ai    │                          │
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
│  │  48+ tables · SSL/TLS connection · connection pooling     │   │
│  └──────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────┘
```

### Security Middleware Stack

```
Request → Rate Limiter (Flask-Limiter)
        → CSRF Protection (Flask-WTF)
        → Login Required (Flask-Login)
        → Role-Level Authorization (RBAC decorator)
        → Route Handler
```

---

## 4. Domain Model

The application is organized into **10 domain modules**, each owning its own models, services, and logic.

### Content Domain
The core content hierarchy:

```
Category
  └── Subject
        └── Course  (soft-delete, versioning, certificates)
              └── Module
                    └── Lesson  (soft-delete, versioning)
                          └── LessonSection  (concept | syntax | example | pitfall | qa)
```

Supporting models: `Tag`, `Source`, `ContentQualityScore`, `CourseStatistics`, `LessonStatistics`, `GlossaryTerm`, `CommandReference`, `Lab`, `LabStep`, `Assignment`, `DiscussionThread`

### Auth Domain
`User`, `Role` — 7 RBAC levels: `super_admin → admin → editor → reviewer → author → moderator → student`

### Assessment Domain
`Quiz`, `Question`, `Option`, `QuizAttempt`, `QuizAnswer`
- Multiple choice, true/false, and free-text question types
- Configurable time limits, passing scores, and XP rewards

### SRS Domain (Spaced Repetition)
`FlashcardDeck`, `Flashcard`, `UserFlashcardProgress`
- SM-2 algorithm: tracks `ease_factor`, `interval_days`, `repetitions`, `next_review_at`

### Gamification Domain
`UserXPLog`, `UserStreak`
- XP earned per activity type: `lesson_read`, `quiz_completed`, `exercise_solved`
- Daily streak tracking with `current_streak` and `longest_streak`

### Knowledge Domain (Vector Search)
`KnowledgeSource`, `SourceDocument`, `KnowledgeChunk`, `ChunkEmbedding`
- Sources: `youtube | docs | book | blog | github`
- Chunks: 500-character segments with JSON-encoded float embeddings
- Model: `nomic-embed-text` (via Ollama)

### Learning Path Domain
Prerequisite graphs and adaptive sequencing.

### Sandbox Domain
Code execution submissions and results via Judge0 API.

### Study Domain
Note-taking and study session tracking.

### Tutor Domain
AI conversation sessions tied to lessons.

---

## 5. Blueprint Routes

| Blueprint | Prefix | Key Routes |
|-----------|--------|-----------|
| `public` | `/` | Home dashboard, `/catalog`, `/search`, `/sitemap.xml`, `/api/v1/stats` |
| `auth` | `/auth` | `/login`, `/register`, `/logout`, `/profile` |
| `learn` | `/learn` | `/courses/<slug>`, `/courses/<slug>/<mod>/<lesson>`, progress tracking |
| `assessment` | — | Quiz start, submit, results |
| `sandbox` | `/sandbox` | Code editor, run, submit |
| `srs` | `/srs` | Flashcard review, SM-2 scheduling |
| `study` | `/study` | Notes, study sessions |
| `ai` | `/ai` | Tutor chat, lesson Q&A, AI draft generation |
| `admin` | `/admin` | Content CMS, user management, ingestion dashboard |

---

## 6. Feature Modules

### Lesson Reader
- Section-based rendering: `concept → syntax → example → pitfall → qa`
- Syntax-highlighted code blocks (Highlight.js)
- Mermaid diagram rendering
- Markdown-to-HTML via Python `markdown` library with `extra`, `codehilite`, `toc` extensions
- View count tracking, progress persistence

### Quiz Engine
- Timed or untimed MCQ sessions
- Automatic grading with pass/fail
- XP awarded on completion
- Attempt history per user

### Flashcard SRS (SM-2)
- Per-card ease factor and interval scheduling
- Review queue sorted by `next_review_at`
- Front/back markdown rendering
- Progress persisted in `user_flashcard_progress`

### Code Sandbox
- Multi-language code execution via Judge0 API
- Submission stored in `sandbox_submissions`
- Lab-step validation via `lab_validation.py`

### Gamification
- XP logged for every learning action
- Daily streak auto-incremented on activity
- Completion certificates auto-generated per course on `_seed_defaults()`

### Admin CMS
- Category / Subject / Course / Module / Lesson CRUD
- Content quality scoring
- Knowledge source ingestion dashboard
- User and role management

---

## 7. AI & Search Layer

### Hybrid Search Pipeline

```
User Query
    │
    ├──► FTS Keyword Scan  (SQLAlchemy LIKE / full-text)
    │         │
    └──► Vector Cosine Similarity  (ChunkEmbedding JSON dot product)
              │
              └──► Ranked merged results → /search page
```

Implemented in `app/domains/knowledge/search.py` (`hybrid_search(query, top_k)`).

### AI Provider Abstraction

```
AI_PROVIDER env var
    ├── "ollama"  → http://localhost:11434  (qwen2.5-coder:7b)
    ├── "openai"  → OpenAI API
    └── "gemini"  → Google Gemini API
```

Switching providers requires only an `.env` change — no application code changes.

### Knowledge Ingestion Flow

```
1. Admin uploads source (PDF / YouTube URL / Markdown)
2. chunker.py splits raw_text into 500-char KnowledgeChunks
3. Ollama nomic-embed-text generates float vectors
4. ChunkEmbedding stored as JSON in TiDB
5. SearchIndexService.rebuild_search_index() called on startup
6. AI Tutor uses hybrid_search() to retrieve context for RAG responses
```

---

## 8. Technology Stack

| Layer | Technology |
|-------|-----------|
| **Web Framework** | Flask 3.0 + Gunicorn 22 |
| **ORM** | SQLAlchemy 2.0 + Flask-SQLAlchemy 3.1 |
| **Database** | TiDB Cloud (MySQL-compatible) via PyMySQL · SSL/TLS |
| **Auth** | Flask-Login 0.6 · Werkzeug password hashing · PyJWT |
| **Security** | Flask-WTF (CSRF) · Flask-Limiter (rate limiting) · Bleach (XSS) |
| **AI / LLM** | Ollama (local) · OpenAI API · Google Gemini API |
| **Embeddings** | `nomic-embed-text` via Ollama |
| **Code Execution** | Judge0 API · Piston API |
| **Frontend** | Vanilla JS · Bootstrap 5 · Highlight.js · Mermaid · EasyMDE |
| **Templating** | Jinja2 3.1 + Python `markdown` library |
| **HTTP** | `requests` 2.31 · BeautifulSoup4 (scraping) |
| **Schema Migrations** | Alembic 1.13 |
| **Deployment** | Render (Web Service) · TiDB Cloud (DB) |
| **Config** | `python-dotenv` · PyYAML · `cryptography` (Fernet) |

---

## 9. Directory Structure

```
notes/  (Learning OS root)
│
├── app/
│   ├── __init__.py                 # App factory: extensions, blueprints, context processors
│   ├── blueprints/
│   │   ├── admin/routes.py         # CMS, ingestion dashboard, user management
│   │   ├── ai/routes.py            # AI tutor chat, draft generation
│   │   ├── assessment/routes.py    # Quiz flow: start → submit → results
│   │   ├── auth/routes.py          # Login, register, logout, profile
│   │   ├── learn/routes.py         # Course overview, lesson reader, progress
│   │   ├── public/routes.py        # Home, catalog, search, sitemap, stats API
│   │   ├── sandbox/routes.py       # Code editor and execution
│   │   ├── srs/routes.py           # Flashcard review sessions
│   │   └── study/routes.py         # Notes and study sessions
│   │
│   ├── core/
│   │   ├── base_model.py           # TimestampMixin, SoftDeleteMixin
│   │   ├── cache.py                # cache_memoize decorator
│   │   ├── config.py               # Config dataclass (DATABASE_TYPE, TiDB, AI)
│   │   ├── constants.py            # Enums: UserRole, ContentStatus, DifficultyLevel, SectionType
│   │   └── extensions.py           # db, login_manager, csrf, limiter singletons
│   │
│   ├── domains/
│   │   ├── auth/models.py          # User, Role
│   │   ├── content/
│   │   │   ├── models.py           # Category, Subject, Course, Module, Lesson, LessonSection, ...
│   │   │   ├── quality.py          # ContentQualityScore helpers
│   │   │   └── sitemap.py          # Sitemap XML generator helpers
│   │   ├── assessment/models.py    # Quiz, Question, Option, QuizAttempt, QuizAnswer
│   │   ├── gamification/
│   │   │   ├── models.py           # UserXPLog, UserStreak
│   │   │   └── service.py          # XP award and streak update logic
│   │   ├── knowledge/
│   │   │   ├── models.py           # KnowledgeSource, SourceDocument, KnowledgeChunk, ChunkEmbedding
│   │   │   ├── chunker.py          # Text splitting into 500-char segments
│   │   │   └── search.py           # hybrid_search(): FTS + vector cosine
│   │   ├── learning_path/models.py # Prerequisite graph models
│   │   ├── sandbox/models.py       # Code submission and result models
│   │   ├── srs/models.py           # FlashcardDeck, Flashcard, UserFlashcardProgress (SM-2)
│   │   ├── study/models.py         # Study session and notes models
│   │   └── tutor/models.py         # AI tutor conversation models
│   │
│   ├── services/
│   │   ├── learning.py             # DashboardService, progress tracking, enrollment
│   │   ├── search_service.py       # SearchIndexService.rebuild_search_index()
│   │   ├── lab.py                  # Lab execution helpers
│   │   └── lab_validation.py       # Judge0 result validation
│   │
│   ├── templates/
│   │   ├── base.html               # Master layout with navbar, sidebar, footer
│   │   ├── public/                 # home.html, catalog.html, search.html, dashboard.html
│   │   ├── learn/                  # course_overview.html, lesson.html
│   │   ├── admin/                  # CMS dashboards, editor forms
│   │   ├── auth/                   # login.html, register.html, profile.html
│   │   └── components/             # _navbar.html, _sidebar.html, _breadcrumb.html
│   │
│   └── static/
│       ├── css/                    # Custom stylesheets
│       ├── js/                     # Vanilla JS: quiz engine, code editor, SRS UI
│       └── images/                 # Logos, icons, course thumbnails
│
├── scripts/                        # One-off DB migration, seeding, and audit scripts
│   ├── audit_catalog.py            # Catalog health audit (duplicates, empty courses)
│   ├── fix_catalog_issues.py       # Fix wrong categories, duplicates, recalc hours
│   ├── fix_is_deleted_flag.py      # Sync deleted_at → is_deleted boolean
│   ├── scaffold_new_courses.py     # Bulk-create lesson stub markdown files
│   ├── phase2_upgrade.py           # Phase 2 DB content migration
│   ├── phase3_python_content.py    # Python course content seeder
│   ├── phase4_content.py           # Multi-course content seeder
│   ├── phase5_content_p1/p2.py     # Advanced content seeders
│   └── ...                         # Additional course seeders and fixers
│
├── docs/plan/                      # Full technical architecture documentation (21 docs)
│
├── .env                            # Local secrets (never committed)
├── .env.example                    # Environment variable template
├── render.yaml                     # Render.com deployment config (2 workers, Gunicorn)
├── requirements.txt                # Python dependencies
├── run.py                          # WSGI entrypoint
├── run_tests.py                    # Test suite runner
└── isrgrootx1.pem                  # TiDB Cloud SSL CA certificate
```

---

## 10. Data Flow

### Student Learning Flow

```
1. /catalog          → Browse categories → subjects → courses
2. /learn/courses/<slug>
                     → Course overview: modules list, progress bar
3. /learn/courses/<slug>/<module>/<lesson>
                     → Lesson reader: sections, code blocks, diagrams
                     → Progress saved: UserLessonProgress
                     → XP awarded: UserXPLog (+10 per lesson read)
                     → Streak updated: UserStreak.last_activity_date
4. /quiz/<lesson>    → Quiz attempt: timed MCQ
                     → Auto-graded → XP awarded (+50 on pass)
5. /srs              → Flashcard review queue (SM-2 scheduled)
                     → ease_factor / interval_days updated per response
6. /sandbox          → Write & run code → Judge0 execution → result
7. Certificate       → Auto-issued on course completion
```

### Content Authoring Flow (Admin)

```
1. /admin/sources    → Add KnowledgeSource (YouTube / PDF / URL)
2. chunker.py        → Split into KnowledgeChunks (500 chars each)
3. Ollama embed      → Generate ChunkEmbedding vectors
4. /admin/lessons    → Create Lesson → add LessonSections
5. AI Draft          → /ai/draft → RAG: hybrid_search() → Ollama completion
6. Review            → ContentQualityScore (readability, plagiarism %)
7. Publish           → lesson.status = "published", published_at = now()
```

---

## 11. Setup & Local Development

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
copy .env.example .env        # Then fill in your values
```

### Database Initialization

The app uses **TiDB Cloud** (MySQL-compatible) in production.  
Tables are auto-created on first run via `db.create_all()` in the app factory.

```bash
python run.py
# Tables created + default roles + admin user seeded automatically
```

### Local AI Setup

```bash
# Install Ollama from https://ollama.com
ollama pull qwen2.5-coder:7b    # Main chat/code model
ollama pull nomic-embed-text    # Embedding model for vector search
# Ollama runs at http://localhost:11434 by default
```

### Run Development Server

```bash
python run.py
# Open http://localhost:5000
```

---

## 12. Configuration Variables

```env
# ── Application ──────────────────────────────────────────────
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-flask-secret-key
ENCRYPTION_KEY=your-fernet-key  # 32-byte base64 key

# ── Database ─────────────────────────────────────────────────
DATABASE_TYPE=tidb              # "sqlite" for local dev | "tidb" for production
DATABASE_URL=mysql+pymysql://user:pass@host:4000/db?ssl_ca=isrgrootx1.pem&ssl_verify_cert=true

# TiDB Cloud individual settings (used alongside DATABASE_URL)
TIDB_HOST=gateway01.us-east-1.prod.aws.tidbcloud.com
TIDB_PORT=4000
TIDB_USER=your-tidb-user
TIDB_PASSWORD=your-tidb-password
TIDB_DATABASE=test
TIDB_CA_PATH=isrgrootx1.pem

# ── AI Provider ───────────────────────────────────────────────
AI_PROVIDER=ollama              # "ollama" | "openai" | "gemini"
OLLAMA_API_BASE_URL=http://localhost:11434
OLLAMA_MODEL_NAME=qwen2.5-coder:7b
OPENAI_API_KEY=                 # Optional
GEMINI_API_KEY=                 # Optional

# ── Code Execution ────────────────────────────────────────────
JUDGE0_API_URL=https://api.judge0.com
JUDGE0_API_KEY=your-judge0-key

# ── Performance ───────────────────────────────────────────────
SKIP_SEARCH_REBUILD=1           # Skip vector index rebuild on startup (dev speed)
```

---

## 13. Deployment

Deployed on **Render** (Web Service) with **TiDB Cloud** as the managed database.

```yaml
# render.yaml summary
service: learning-os
runtime: python
buildCommand: pip install -r requirements.txt
startCommand: gunicorn run:app --workers 2 --threads 2 --timeout 120 --bind 0.0.0.0:$PORT
healthCheckPath: /
region: oregon
plan: free
```

### Production Database
- **TiDB Cloud** (MySQL 8.0-compatible, serverless tier)
- Connection via SSL/TLS using `isrgrootx1.pem` CA certificate
- Connection pooling with `pool_pre_ping=True` (detects stale connections)

---

## 14. Scripts Reference

| Script | Purpose |
|--------|---------|
| `audit_catalog.py` | Audit all categories for duplicates, wrong placements, empty courses |
| `fix_catalog_issues.py` | Fix category misplacements, merge duplicates, recalculate hours |
| `fix_is_deleted_flag.py` | Sync `deleted_at` → `is_deleted` boolean for soft-deleted records |
| `scaffold_new_courses.py` | Bulk-create markdown lesson stub files (Bootstrap, jQuery, SQL Server, MongoDB, Prompt Engineering) |
| `phase2_upgrade.py` | Phase 2 content DB migration (quiz banks, XP, streaks) |
| `phase3_python_content.py` | Python course full content seeder |
| `phase4_content.py` | Multi-course content seeder (DevOps, Java, IoT, etc.) |
| `phase5_content_p1.py` | Advanced AI/ML course content seeder part 1 |
| `phase5_content_p2.py` | Advanced AI/ML course content seeder part 2 |
| `db_backup.py` | Database backup utility |
| `migrate_html.py` | Import existing HTML note files into the DB |
| `migrate_markdown.py` | Import existing Markdown note files into the DB |
| `rename_curriculum.py` | Bulk rename courses/modules in the DB |
| `reorganize_modules.py` | Reorder modules across courses |

---

## 15. Coding Standards

1. **Repository Pattern** — Keep DB queries decoupled from Flask views. Use `services/` for business logic.
2. **Always Soft-Delete** — Set **both** `is_deleted = True` AND `deleted_at = datetime.utcnow()` when removing records.
3. **ORM Only** — Never write raw SQL. Use SQLAlchemy ORM to stay DB-agnostic (SQLite ↔ TiDB/MySQL).
4. **Audit Trails** — All new models must inherit `TimestampMixin` (`created_at`, `updated_at`).
5. **RBAC** — Use role-check decorators on any admin or editor route.
6. **No Hardcoded Secrets** — All credentials via `.env`. Never commit `.env`.
7. **Slug Uniqueness** — When renaming a record's slug, free the old slug with `db.session.flush()` before assigning the new one to avoid unique-constraint conflicts.

---

## 16. Changelog

| Version | Date | Summary |
|---------|------|---------|
| v1.0.0 | 2025 | Initial CMS design: courses, quizzes, streak engines, code execution |
| v2.0.0 | 2025 | Vector search (TiDB), Ollama LLM, multi-source ingestion, SRS SM-2 |
| v2.1.0 | 2026-01 | IoT & Hardware Full Stack catalog (7 courses, 150+ lessons) |
| v2.2.0 | 2026-04 | Python AI & Data Science catalog (ML, DL, NLP, CV, MLOps, RAG, Agents) |
| v2.3.0 | 2026-07 | Catalog clean-up: fix category misplacements (Java/C in Python Full Stack), merge duplicate Python courses, recalc estimated hours for all courses |

---

## 17. Documentation Index

| Document | Purpose |
|----------|---------|
| [Master Plan](docs/plan/00_LEARNING_OS_MASTER_PLAN.md) | Baseline architecture & decisions |
| [Enhancement Plan](docs/plan/00_LEARNING_OS_v2.0_ENHANCEMENT_PLAN.md) | v2.0 evolution guide |
| [Product Vision](docs/plan/01_Product_Vision.md) | Value proposition & universal schema |
| [Information Architecture](docs/plan/02_Information_Architecture.md) | Site map, taxonomy & slugs |
| [User Roles (RBAC)](docs/plan/03_User_Roles_RBAC.md) | Role permissions & CMS state rules |
| [Database ERD](docs/plan/04_Database_ERD.md) | 48-table schema definitions |
| [Folder Structure](docs/plan/05_Folder_Structure.md) | Project directories blueprint |
| [CMS Design](docs/plan/06_CMS_Design.md) | Editor workflow & source attributions |
| [Learning Engine](docs/plan/07_Learning_Engine.md) | Prerequisites & spaced repetition SM-2 |
| [Progress Engine](docs/plan/08_Progress_Engine.md) | XP levels & user streak calculations |
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

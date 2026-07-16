# Enterprise Knowledge Operating System (Learning OS v2.0)

A modular, production-ready Knowledge Operating System (Learning OS) designed to transform scattered learning resources into standardized knowledge. It features multi-source ingestion pipelines, hybrid search models, adaptive learning paths, local AI configurations, and enterprise-grade CMS workflows.

---

## Document Index & Quick Links

| Document | Purpose / Scope | Links |
|---|---|:---:|
| **Master Index** | Baseline Architecture & Decisions | [00_LEARNING_OS_MASTER_PLAN.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/00_LEARNING_OS_MASTER_PLAN.md) |
| **Enhancement Plan** | Evolving guide to Learning OS v2.0 | [00_LEARNING_OS_v2.0_ENHANCEMENT_PLAN.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/00_LEARNING_OS_v2.0_ENHANCEMENT_PLAN.md) |
| **Product Vision** | Value Proposition & Universal Schema | [01_Product_Vision.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/01_Product_Vision.md) |
| **Information Arch** | Site Map, Taxonomy & Slugs | [02_Information_Architecture.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/02_Information_Architecture.md) |
| **User Roles (RBAC)** | Role permissions & CMS state rules | [03_User_Roles_RBAC.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/03_User_Roles_RBAC.md) |
| **Database ERD** | 48-table schema definitions | [04_Database_ERD.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/04_Database_ERD.md) |
| **Folder Structure** | Project directories blueprint | [05_Folder_Structure.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/05_Folder_Structure.md) |
| **CMS Design** | Editors workflow & source attributions | [06_CMS_Design.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/06_CMS_Design.md) |
| **Learning Engine** | Prerequisites & Spaced Repetition (SM-2) | [07_Learning_Engine.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/07_Learning_Engine.md) |
| **Progress Engine** | XP levels & user streaks calculations | [08_Progress_Engine.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/08_Progress_Engine.md) |
| **Exercise Engine** | Auto-grading & Sandboxes configurations | [09_Exercise_Engine.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/09_Exercise_Engine.md) |
| **Quiz Engine** | Question banks & validations | [10_Quiz_Engine.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/10_Quiz_Engine.md) |
| **Achievement Engine**| Badge allocations & criteria checkers | [11_Achievement_Engine.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/11_Achievement_Engine.md) |
| **Search Architecture**| SQLite FTS5 & Hybrid Search specifications | [12_Search_Architecture.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/12_Search_Architecture.md) |
| **Recommendation Engine**| Cosine similarity & RAG recomendations | [13_Recommendation_Engine.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/13_Recommendation_Engine.md) |
| **AI Integration** | Provider abstraction & local Ollama routes | [14_AI_Integration_Layer.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/14_AI_Integration_Layer.md) |
| **REST API Reference** | OpenAPI endpoint maps | [15_REST_API_Specification.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/15_REST_API_Specification.md) |
| **Admin Panels** | Reviews, roles & ingestion dashboard | [16_Admin_Dashboard.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/16_Admin_Dashboard.md) |
| **Student Panels** | Spaced repetition & user dashboards UI | [17_Student_Dashboard.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/17_Student_Dashboard.md) |
| **SEO Strategy** | Schema JSON-LD & Sitemap builders | [18_SEO_Strategy.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/18_SEO_Strategy.md) |
| **Security Architecture**| Password hashing, CSRF & Rate limits | [19_Security_Architecture.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/19_Security_Architecture.md) |
| **Deployment Arch** | Render setups & databases backing schedules | [20_Deployment_Architecture.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/20_Deployment_Architecture.md) |
| **Roadmap Plan** | Phase checklists mapping sprint goals | [21_Implementation_Roadmap.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/21_Implementation_Roadmap.md) |

---

## 1. Project Overview & Vision

The **Learning OS** is a database-driven knowledge processing platform. Rather than serving static tutorials, it organizes learning content into a structured database schema. The system standardizes unstructured sources (PDFs, YouTube transcripts, documentation, personal markdown notes) into structured lessons, generating interactive practice exercises, self-assessments, and adaptive study paths tailored to student mastery level.

```
+------------------------------------------------------------+
|                       Learning OS                          |
|                                                            |
|  Unstructured Sources (Books, Links, YouTube Playlists)     |
|                           │                                |
|                           ▼                                |
|  [Ingestion Engine] -> [Chunker] -> [Embeddings Resolver]   |
|                                                            |
|  Knowledge Store Database  <---->  Vector Hybrid Index     |
|                           │                                |
|                           ▼                                |
|   AI Drafting Workspace  <--->  Collaborative Editor CMS   |
|                           │                                |
|                           ▼                                |
|      Adaptive Learning Paths, Streaks & Gamification        |
+------------------------------------------------------------+
```

---

## 2. Core Architecture & Features

- **Knowledge Ingestion Pipeline**: Auto-parsers process uploaded files (PDFs, Markdown) and video platforms (YouTube API transcripts).
- **Hybrid Semantic Search**: Combines FTS5 keyword lookups with vector distance scans to surface relevant context.
- **Dynamic Quiz & Flashcard Generators**: Analyzes lesson text to generate formatted MCQ option keys and spaced-repetition deck assets.
- **Universal Lesson Layout**: Enforces sections for concepts, syntax, copy-to-clipboard examples, diagrams, common pitfalls, and interview Q&As.
- **Provider Abstraction Layer**: Swaps local AI instances (Ollama daemon runtime) with cloud model providers (Gemini, OpenAI, Claude) without changing application logic.
- **Adaptive Prerequisite Sequencer**: Uses knowledge graph models to dynamically route students around weak topics.

---

## 3. Technology Stack

- **Backend core**: Flask 3.0 (Blueprint structure) + Gunicorn server
- **Database configurations**: SQLite (with VSS extension) for local development; PostgreSQL (with PGVector extension) for production
- **Task Worker Scheduler**: APScheduler backend job queues
- **Code validation sandbox**: Judge0/Piston API code compilation environment
- **Frontend UI frameworks**: Bootstrap 5 + Vanilla JavaScript + EasyMDE + Highlight.js + Mermaid diagrams renderer

---

## 4. Directory Structure

```
learning_os/
├── app/
│   ├── blueprints/         # URL Route Controllers mapped via Blueprints
│   ├── core/               # App Factory configurations, extensions, security middlewares
│   ├── domains/            # Database Domain Entities Models & Repository files
│   ├── services/           # Business domain processing engines (AI, Search, Recs)
│   ├── templates/          # HTML structures matching UI blueprints
│   └── static/             # Stylesheets (CSS), interactions scripts (JS), static images
├── migrations/             # Alembic database revision history scripts
├── scripts/                # Database seeders, imports, CLI migration executables
├── docs/                   # Full Technical Architecture plans folder
├── data/                   # Development runtime database directory (local SQLite)
├── run.py                  # Server runtime wrapper script
├── run_tests.py            # Test suite runner configuration
├── requirements.txt        # Backend dependencies list
└── alembic.ini             # Alembic configuration mappings
```

---

## 5. Development Phases

```
   [Phase 1] Core Engine Setup & Ingestion Migration Script
       │
       ▼
   [Phase 2] Quiz bank builders, Sandboxes integrations, XP and streaks trackers
       │
       ▼
   [Phase 3] Adaptive Learning paths, Flashcards voting screens, SM-2 schedulers
       │
       ▼
   [Phase 4] Embedding computations, Hybrid search indices, AI Prompting templates
       │
       ▼
   [Phase 5] RBAC check decorators, CMS reviewer approvals portals, SEO tags
       │
       ▼
   [Phase 6] Render cloud configuration, Postgres/PGVector deployments, backup scripts
```

---

## 6. Setup Instructions & Local Development

### 1. Project Prerequisites
- Python 3.12+
- Git
- SQLite (Ensure FTS5 extension enabled)

### 2. Environment Configuration
Clone the repository and copy the sample configuration template:
```bash
git clone https://github.com/rajasekarrk96/linkedin_AI.git
cd linkedin_AI
python -m venv .venv
.venv\Scripts\activate      # On Windows
# source .venv/bin/activate # On Unix/macOS
pip install -r requirements.txt
copy .env.example .env
```

### 3. Database Initialization
Run Alembic schema updates to configure SQLite database tables:
```bash
alembic upgrade head
```

### 4. Local AI (Ollama) Setup
1. Download the Ollama runtime client from [ollama.com](https://ollama.com).
2. Install and pull your target models:
   ```bash
   ollama pull qwen2.5-coder:7b
   ollama pull llama3:8b
   ```
3. Expose the server daemon port locally (Default: `http://localhost:11434`).

---

## 7. Configuration Variables

Copy these variables into your local `.env` configuration file:

```env
# Application Settings
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=generate-a-secure-flask-token-here
ENCRYPTION_KEY=generate-a-safe-fernet-key-bytes-here

# Database Configurations
DATABASE_URL=sqlite:///data/learning_os.db
# For production PostgreSQL:
# DATABASE_URL=postgresql://user:password@host:5432/dbname

# AI Integrations
AI_PROVIDER=ollama
OLLAMA_API_BASE_URL=http://localhost:11434
OLLAMA_MODEL_NAME=qwen2.5-coder:7b

# API Integrations (Optional Cloud Gateways)
OPENAI_API_KEY=your-openai-api-key
GEMINI_API_KEY=your-google-gemini-api-key

# Sandboxed Execution API
JUDGE0_API_URL=https://api.judge0.com
JUDGE0_API_KEY=your-api-key-here
```

---

## 8. Executing Applications & Tests

To start the local development server:
```bash
python run.py
```
Open [http://localhost:5000](http://localhost:5000) in your web browser.

To execute the test suite (unit, integration, and end-to-end tests):
```bash
python run_tests.py
```

---

## 9. Ingestion & AI Workflows

### The Knowledge Pipeline
```
Sources Ingest (CLI/UI) ──► Chunks Splitter ──► Embeddings Vector ──► Drafts Review ──► Publish
```

1. **Ingest Source**: Put target PDFs or YouTube link formats into `scripts/ingest_source.py`.
2. **Chunking Processing**: Text is parsed, split into 500-character segments, and indexed.
3. **Embeddings Computation**: Generates semantic vector arrays.
4. **Draft generation**: The admin dashboard pulls context blocks from the vector database to build lesson drafts.
5. **Human review check**: Reviewers approve formatting, adjust content, check plagiarism ratings ($<5\%$), and publish.

---

## 10. Contribution & Coding Standards

1. **Repository Pattern**: Keep database query operations decoupled from Flask views; write operations inside `repository.py` domain scripts.
2. **Database Agnosticism**: Never execute raw SQL. Always use SQLAlchemy ORM wrappers to maintain compatibility between SQLite and PostgreSQL.
3. **Audit Trails**: Ensure new database models inherit from `base_model.py` to inherit `created_at` and `updated_at` properties.
4. **Backward Compatibility**: Never delete schema columns without running deprecation reviews.

---

## 11. Changelog & Architecture Registry

- **v1.0.0 (Baseline)**: Initial design specs for the structured CMS, course paths, quizzes, streak engines, and code execution.
- **v2.0.0 (Enhancement)**: Integrated Vector Search databases (PGVector/SQLite-VSS), Local Ollama LLM provider configurations, multi-source ingestion parsers, and weak-topic learning engines.

---

## 12. Where to Start as a New Developer

1. **Check the database ERD** in [04_Database_ERD.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/04_Database_ERD.md) to understand how courses, users, and progress metrics map together.
2. **Review the architecture roadmap** in [21_Implementation_Roadmap.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/21_Implementation_Roadmap.md) to locate active sprint goals.
3. **Set up local Ollama models** and launch `run.py`.
4. Run `python scripts/migrate_html.py` to import existing note templates.
5. Inspect the `app/domains/` folder to study the models, repositories, and services directory structure.

---

## Document Dependencies Graph

```
                   [01 Product Vision]
                            │
                            ▼
               [02 Information Architecture]
                            │
         ┌──────────────────┴──────────────────┐
         ▼                                     ▼
 [04 Database ERD]                    [05 Folder Structure]
         │                                     │
         ├──────────────────┬──────────────────┤
         ▼                  ▼                  ▼
[06 CMS Design]      [07 Learn Engine]   [14 AI Gateway]
         │                  │                  │
         └────────┬─────────┴────────┬─────────┘
                  ▼                  ▼
          [12 Search Arch]     [15 REST APIs]
                  │                  │
                  ▼                  ▼
          [16 Admin Panels]    [17 Student Dashboard]
```

---

## License
Private & Proprietary — All Rights Reserved.

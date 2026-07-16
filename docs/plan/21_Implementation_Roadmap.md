# 21 — Multi-Phase Implementation Roadmap

> The roadmap splits the system development into 6 sequential phases.

---

## 21.1 Phase Diagram

```
Phase 1: Foundation (Core Engine, CMS, SQLite Migration)
    │
    ▼
Phase 2: Assessments & Gamification (Quizzes, Exercises, XP Engine)
    │
    ▼
Phase 3: Learning Paths & Spaced Repetition (SRS, Learning Paths)
    │
    ▼
Phase 4: AI Layer & Vector Search (AIGateway templates, similarity)
    │
    ▼
Phase 5: Enterprise CMS Dashboard & Roles (RBAC, review queues)
    │
    ▼
Phase 6: Deployment & Monitoring (Render, TiDB, Backups, Autoscale)
```

---

## 21.2 Phase Tasks Breakdown

### Phase 1: Core Foundation & CMS Engine
- Configure project folder structure, create application factory, and configure SQLAlchemy ORM.
- Implement User registration, Login flows, and CSRF protection.
- Create migration script (`migrate_html.py`) to parse existing HTML files (Python basics, Java OOP, MySQL) into markdown content files and insert course structures into the database.
- Build basic lesson viewer UI matching the universal lesson sections.

### Phase 2: Assessment & Gamification Engine
- Build Quiz Models, Option sets, and validation/scoring pipelines.
- Implement sandboxed Code Execution adapters using Piston/Judge0.
- Create the XP logging system, user progress metrics, Level curves, and consecutive activity Streak updates.

### Phase 3: Learning Engine & Spaced Repetition (SRS)
- Create Learning Paths structure, drag-and-drop sequencing, and prerequisite check hooks.
- Code the Spaced Repetition SM-2 scheduling service.
- Implement Flashcards decking screens, confidence voting sliders, and note bookmarking dashboards.

### Phase 4: AI Layer & Advanced Search
- Integrate the AI Gateway service, configure prompts registries (explain, summarize, quiz gen).
- Rebuild search indexing using SQLite FTS5 / Postgres FTS.
- Implement autocomplete routes and typo-tolerant search endpoints.
- Code recommendation algorithms using cosine similarity tag overlaps.

### Phase 5: Enterprise CMS Dashboard & Roles (RBAC)
- Define RBAC roles hierarchy and write min-role check wrappers.
- Build the Admin Dashboard UI including metrics charts, queue tables, and system logs.
- Design the peer review dashboard allowing reviewers to verify submitted drafts.
- Add sitemap xml builders, Canonical redirects policies, and structured schema tags.

### Phase 6: Production Scaling & Deployment
- Set up Render configuration files and configure TiDB serverless cluster connections.
- Set up Redis cache stores to monitor rate limits.
- Deploy database backup procedures syncing with external S3 stores.
- Run end-to-end integration test suites (`run_tests.py`).

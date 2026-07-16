# 05 — Folder Structure

> Complete codebase directory layout for the Learning OS.
> Built as a standalone Flask application in the `notes` project directory.

---

## 5.1 Root Directory

```
learning_os/                         <- Project root
│
├── app/                             <- Main Flask application
├── migrations/                      <- Alembic DB migrations
├── content/                         <- Markdown content files (CMS storage)
├── media/                           <- Uploaded images, PDFs, assets
├── scripts/                         <- Migration, seeding, utility scripts
├── tests/                           <- All test files
├── docs/                            <- Architecture docs (this folder)
├── data/                            <- Runtime data (SQLite in dev)
│
├── run.py                           <- App entrypoint
├── run_tests.py                     <- Test runner
├── requirements.txt                 <- Python dependencies
├── .env.example                     <- Environment template
├── .env                             <- Local secrets (gitignored)
├── alembic.ini                      <- Migration config
├── .gitignore
└── README.md
```

---

## 5.2 Application Directory (`app/`)

```
app/
│
├── __init__.py                      <- App factory: create_app()
│
├── blueprints/                      <- Flask Blueprint modules (URL routing)
│   │
│   ├── public/                      <- Public-facing pages
│   │   ├── __init__.py
│   │   ├── routes.py                <- Home, catalog, search
│   │   └── templates/
│   │       ├── home.html
│   │       ├── catalog.html
│   │       └── search_results.html
│   │
│   ├── learn/                       <- Learning experience
│   │   ├── __init__.py
│   │   ├── routes.py                <- Course, module, lesson views
│   │   └── templates/
│   │       ├── course_overview.html
│   │       ├── lesson.html
│   │       ├── lesson_section.html
│   │       └── partials/
│   │           ├── _concepts.html
│   │           ├── _syntax.html
│   │           ├── _examples.html
│   │           ├── _exercises.html
│   │           ├── _quiz.html
│   │           ├── _cheatsheet.html
│   │           ├── _interview_qa.html
│   │           └── _flashcards.html
│   │
│   ├── auth/                        <- Authentication
│   │   ├── __init__.py
│   │   ├── routes.py                <- login, register, logout, reset
│   │   ├── forms.py
│   │   └── templates/
│   │       ├── login.html
│   │       ├── register.html
│   │       └── forgot_password.html
│   │
│   ├── dashboard/                   <- Student dashboard
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates/
│   │       ├── overview.html
│   │       ├── progress.html
│   │       ├── achievements.html
│   │       ├── bookmarks.html
│   │       ├── my_notes.html
│   │       ├── flashcards.html
│   │       └── revision.html
│   │
│   ├── quiz/                        <- Quiz engine
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates/
│   │       ├── quiz.html
│   │       └── results.html
│   │
│   ├── exercises/                   <- Exercise engine
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates/
│   │       ├── exercise.html
│   │       └── submission.html
│   │
│   ├── paths/                       <- Learning paths
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates/
│   │       ├── path_list.html
│   │       └── path_detail.html
│   │
│   ├── profile/                     <- User profile
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates/
│   │       ├── profile.html
│   │       └── settings.html
│   │
│   ├── admin/                       <- Admin CMS
│   │   ├── __init__.py
│   │   ├── routes.py                <- Admin router / dashboard
│   │   ├── content/
│   │   │   ├── routes.py            <- Course/Module/Lesson CRUD
│   │   │   └── templates/
│   │   │       ├── lesson_list.html
│   │   │       ├── lesson_editor.html    <- Rich Markdown editor
│   │   │       └── lesson_versions.html
│   │   ├── quiz_manager/
│   │   │   ├── routes.py
│   │   │   └── templates/
│   │   ├── user_manager/
│   │   │   ├── routes.py
│   │   │   └── templates/
│   │   ├── analytics/
│   │   │   ├── routes.py
│   │   │   └── templates/
│   │   ├── seo/
│   │   │   ├── routes.py
│   │   │   └── templates/
│   │   ├── sources/
│   │   │   ├── routes.py
│   │   │   └── templates/
│   │   └── templates/
│   │       └── admin_base.html
│   │
│   └── api/                         <- REST API v1
│       ├── __init__.py
│       ├── v1/
│       │   ├── auth.py              <- /api/v1/auth/
│       │   ├── courses.py           <- /api/v1/courses/
│       │   ├── lessons.py           <- /api/v1/lessons/
│       │   ├── quizzes.py           <- /api/v1/quizzes/
│       │   ├── exercises.py         <- /api/v1/exercises/
│       │   ├── progress.py          <- /api/v1/progress/
│       │   ├── paths.py             <- /api/v1/paths/
│       │   ├── users.py             <- /api/v1/users/
│       │   ├── search.py            <- /api/v1/search/
│       │   ├── ai.py                <- /api/v1/ai/
│       │   ├── flashcards.py        <- /api/v1/flashcards/
│       │   ├── bookmarks.py         <- /api/v1/bookmarks/
│       │   ├── notes.py             <- /api/v1/notes/
│       │   └── analytics.py         <- /api/v1/analytics/
│       └── middleware.py            <- API auth, rate limiting
│
├── core/                            <- Framework-level infrastructure
│   ├── config.py                    <- Config dataclasses
│   ├── constants.py                 <- Enums: Status, Types
│   ├── extensions.py                <- db, login_manager, cache, mail
│   ├── exceptions.py                <- Custom exception classes
│   ├── feature_flags.py             <- Feature toggle constants
│   ├── security.py                  <- Password hashing, tokens
│   ├── logging.py                   <- Structured log setup
│   ├── rbac.py                      <- RBAC decorators
│   ├── cache.py                     <- Caching decorators & helpers
│   ├── startup.py                   <- Directory bootstrap
│   └── base_model.py                <- AuditMixin, TimestampMixin
│
├── domains/                         <- Business domain models & repositories
│   │
│   ├── auth/
│   │   ├── models.py                <- User, Role, Permission, Session
│   │   ├── repository.py
│   │   └── service.py
│   │
│   ├── content/
│   │   ├── models.py                <- Category, Subject, Course, Module,
│   │   │                               Lesson, LessonSection, LessonVersion,
│   │   │                               Tag, Source, LessonTag, LessonSource
│   │   ├── repository.py
│   │   └── service.py
│   │
│   ├── learning_paths/
│   │   ├── models.py                <- LearningPath, PathCourse
│   │   ├── repository.py
│   │   └── service.py
│   │
│   ├── quiz/
│   │   ├── models.py                <- Quiz, Question, Option, Attempt
│   │   ├── repository.py
│   │   └── service.py
│   │
│   ├── exercise/
│   │   ├── models.py                <- Exercise, Submission
│   │   ├── repository.py
│   │   └── service.py
│   │
│   ├── flashcard/
│   │   ├── models.py                <- FlashcardDeck, Flashcard, UserProgress
│   │   ├── repository.py
│   │   └── service.py
│   │
│   ├── progress/
│   │   ├── models.py                <- UserProgress, UserLessonProgress, XPLog, Streak
│   │   ├── repository.py
│   │   └── service.py
│   │
│   ├── achievement/
│   │   ├── models.py                <- Badge, BadgeCriteria, UserBadge
│   │   ├── repository.py
│   │   └── service.py
│   │
│   ├── engagement/
│   │   ├── models.py                <- Bookmark, UserNote, LessonRating
│   │   ├── repository.py
│   │   └── service.py
│   │
│   ├── media/
│   │   ├── models.py                <- MediaFile, LessonMedia
│   │   ├── repository.py
│   │   └── service.py
│   │
│   └── notification/
│       ├── models.py                <- Notification
│       ├── repository.py
│       └── service.py
│
├── services/                        <- Cross-domain application services
│   ├── registry.py                  <- Service registry
│   ├── search_service.py            <- Full-text search indexer + query
│   ├── recommendation_service.py    <- Content recommendation engine
│   ├── ai_service.py                <- AI explain, quiz gen, summarize
│   ├── analytics_service.py         <- Platform analytics aggregator
│   ├── export_service.py            <- PDF, Markdown export
│   ├── import_service.py            <- HTML migration, Markdown import
│   ├── notification_service.py      <- Email, in-app notifications
│   └── seo_service.py               <- Sitemap, meta tag generator
│
├── scheduler/                       <- Background jobs
│   ├── worker.py                    <- Polling thread
│   └── dispatcher.py                <- Task router
│
├── templates/                       <- Base Jinja2 templates
│   ├── base.html                    <- Master layout
│   ├── base_auth.html               <- Auth pages layout
│   ├── base_admin.html              <- Admin layout
│   ├── components/
│   │   ├── _navbar.html
│   │   ├── _footer.html
│   │   ├── _sidebar.html
│   │   ├── _lesson_card.html
│   │   ├── _course_card.html
│   │   ├── _progress_bar.html
│   │   ├── _badge_card.html
│   │   └── _breadcrumb.html
│   └── errors/
│       ├── 403.html
│       ├── 404.html
│       └── 500.html
│
└── static/                          <- CSS, JS, images
    ├── css/
    │   ├── main.css
    │   ├── admin.css
    │   ├── lesson.css
    │   └── themes/
    │       ├── light.css
    │       └── dark.css
    ├── js/
    │   ├── main.js
    │   ├── lesson.js                 <- Lesson interactivity
    │   ├── quiz.js                   <- Quiz engine frontend
    │   ├── editor.js                 <- Markdown editor (EasyMDE)
    │   ├── search.js                 <- Search autocomplete
    │   └── flashcard.js              <- Flashcard flip engine
    ├── img/
    │   ├── logo.svg
    │   └── placeholders/
    └── vendor/
        ├── highlight.js/            <- Code syntax highlighting
        ├── mermaid/                  <- Diagram rendering
        └── easymde/                  <- Markdown editor
```

---

## 5.3 Content Directory (`content/`)

```
content/
├── core-python/
│   ├── basics/
│   │   ├── variables.md
│   │   ├── data-types.md
│   │   └── type-casting.md
│   ├── control-flow/
│   │   ├── conditions.md
│   │   └── loops.md
│   └── ...
├── core-java/
│   ├── oop/
│   │   ├── classes.md
│   │   ├── inheritance.md
│   │   └── polymorphism.md
│   └── ...
├── mysql/
│   └── ...
└── java-selenium/
    └── ...
```

**Note**: Content files are the source of truth for editing via CLI tools or Git.
The CMS database stores metadata and parsed content for fast querying.

---

## 5.4 Scripts Directory (`scripts/`)

```
scripts/
├── migrate_html.py        <- Parse existing HTML lessons into Markdown + DB seed
├── seed_content.py        <- Seed database from content/ Markdown files
├── create_admin.py        <- Create first super admin user
├── index_search.py        <- Build/rebuild full-text search index
├── generate_sitemap.py    <- Generate XML sitemap
├── export_course.py       <- Export course as ZIP/PDF
├── backup_db.py           <- Database backup utility
└── check_completeness.py  <- Report content completeness scores
```

---

## 5.5 Tests Directory (`tests/`)

```
tests/
├── conftest.py            <- Fixtures, test client, test DB
├── unit/
│   ├── test_rbac.py
│   ├── test_progress.py
│   ├── test_quiz.py
│   ├── test_achievement.py
│   └── test_search.py
├── integration/
│   ├── test_lesson_api.py
│   ├── test_quiz_api.py
│   ├── test_auth_api.py
│   └── test_progress_api.py
└── e2e/
    ├── test_learn_flow.py
    ├── test_quiz_flow.py
    └── test_admin_flow.py
```

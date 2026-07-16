# Task 01 — Core Foundation & Ingestion Engine

> **Goal**: Initialize the project, setup the SQLAlchemy ORM models, create the migration CLI script, and parse existing HTML lesson notes into Markdown + Seed database elements.

---

## 1.1 Development Environment & Project Structure
- [x] Initialize Python environment:
  - Create standard `.venv` (if not done).
  - Create [requirements.txt](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/requirements.txt) with libraries: Flask, SQLAlchemy, Alembic, Bleach, PyJWT, Cryptography, PyMySQL, Markdown.
- [x] Bootstrap directory tree:
  - Create [app/](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/app/) subdirectory folder structure matching [05_Folder_Structure.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/05_Folder_Structure.md).
  - Setup [run.py](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/run.py) entrypoint script.
- [x] Configure Environment Settings:
  - Create `.env.example` mapping application keys, SQLite database path, and model variables.

---

## 1.2 Database Core & Identity Layer (Alembic Setup)
- [x] Setup Alembic configuration mapping:
  - Initialize Alembic environment in the project.
- [x] Core Database Models:
  - Code core user/role models: `User`, `Role`, `Permission` (refer to [03_User_Roles_RBAC.md](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/03_User_Roles_RBAC.md)).
  - Code baseline content CMS models: `Category`, `Subject`, `Course`, `Module`, `Lesson`, `LessonSection`, `LessonVersion`, `Tag`, `Source`.
- [x] Run Initial Schema Migration:
  - Generate migration script: `alembic revision --autogenerate -m "Initial schema setup"`.
  - Apply migrations: `alembic upgrade head`.

---

## 1.3 Static HTML to Markdown Migration Script
- [x] Ingestion Parsing CLI (`scripts/migrate_html.py`):
  - Parse existing lesson notes from folders (`Core_Python`, `Core_Java`, `My_Sql`) using BeautifulSoup or HTML processors.
  - Extract sections: title, overview description, code snippets, references link patterns.
  - Save parsed outputs as clean Markdown files under `/content/{course}/{module}/{lesson}.md`.
- [x] Database Seeding:
  - Map folder structures (e.g. `Core_Python/basics.html`) to database rows: Category ("Technical"), Subject ("Python"), Course ("Core Python"), Module ("Basics"), and Lesson ("Variables & Data Types").
  - Populate initial records, tags, and source citations mapping.

---

## 1.4 Baseline Lesson Viewer UI
- [x] Flask Route Blueprints:
  - Create `public` blueprint for catalog view.
  - Create `learn` blueprint mapping lessons path: `/learn/<course_slug>/<module_slug>/<lesson_slug>/`.
- [x] Templates rendering:
  - Design master Jinja templates (`base.html`, `navbar.html`, `footer.html`).
  - Code lesson viewer (`lesson.html`) containing content tabs: [Overview], [Concepts], [Syntax], [Examples], [References].

---

## 🛑 CHECKPOINT & BREAK POINT
- Verify SQLite database contains imported records by running query checks.
- Test endpoint URLs: `/` (catalog overview page) and `/learn/core-python/basics/variables` (verifying HTML parsing layouts render clean CSS/syntax highlighting).
- **Action**: Pause and request approval before moving to Quiz & sandbox integrations.

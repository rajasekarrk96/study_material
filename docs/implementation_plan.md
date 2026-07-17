# Implementation Plan — Learning OS v2.0 Architecture & Roadmap

This implementation plan details the setup, code changes, and task checklists for constructing the **Learning Operating System v2.0 (Learning OS v2.0)**, incorporating AI Knowledge Processing, Hybrid Search, and Local Ollama providers.

---

## User Review Required

> [!IMPORTANT]
> Please review the newly generated v2.0 blueprint files:
> - **v2.0 Enhancement Plan**: [00_LEARNING_OS_v2.0_ENHANCEMENT_PLAN.md](./plan/00_LEARNING_OS_v2.0_ENHANCEMENT_PLAN.md)
> - **Main Project README**: [README.md](../README.md)
>
> These files outline the roadmap to integrate the following without breaking compatibility:
> 1. Local AI model support (Ollama) through a unified gateway router.
> 2. Document chunking, vector indexing, and hybrid (semantic + keyword) search.
> 3. Knowledge Graph pathways & automated Quiz/Exercise drafting workspaces.

---

## Open Questions

> [!WARNING]
> These decisions will directly impact the implementation choices in Phase 1 and 2:
>
> 1. **Initial Platform Brand Name**: Is **EduSphere** the desired brand name, or should we use a new name?
> 2. **Authentication Integrations**: Should we support Social logins (Google/Github OAuth) in addition to email/password authentication?
> 3. **Editor Preference**: Do content creators write in Markdown, or is a rich WYSIWYG editor preferred?
> 4. **Exercise Verification**: Shall we use an external Judge0 cloud instance, or deploy a localized Docker sandbox instance during development?

---

## Proposed Changes

We will introduce a modular Flask app workspace inside the `notes` repository. This will be built next to the static notes directories (Core_Java, Core_Python, Java_Selenium, My_Sql), which will be imported into the new database structure.

### [Component Name] Learning OS Application

#### [NEW] [run.py](../run.py)
Entrypoint wrapper starting the webserver.

#### [NEW] [requirements.txt](../requirements.txt)
Python libraries including Flask, SQLAlchemy, Alembic, Bleach, PyJWT, Cryptography, and PyMySQL.

#### [NEW] [app/](../app/)
Modular Blueprints, Domain Services, Repositories, Templates, and Static CSS/JS files.

#### [NEW] [scripts/migrate_html.py](../scripts/migrate_html.py)
Automated migration script to parse existing HTML notes into Markdown lesson documents and import them into the Database CMS schema.

---

## Verification Plan

### Automated Tests
- Build verification tests: `python -m pytest tests/`
- DB Schema Migrations tests: `alembic upgrade head`
- HTML migration validation tests: `python scripts/migrate_html.py --dry-run`

### Manual Verification
- Render check: Verify all lesson elements (overview, syntax, examples, references) show up consistently on dynamic templates compared to the original static HTML equivalents.
- Admin dashboard testing: Access draft editing tools, write new Markdown notes, save, check version histories, and publish.
- Quiz grading checks: Take quizzes as a student, review answers, verify XP accumulation, and check streaks.

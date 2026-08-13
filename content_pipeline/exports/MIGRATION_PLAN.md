# Learning OS v2 — Structural Migration & Architecture Plan

_Version: 2.0.0_  
_Status: PROPOSED / AUDIT COMPLETE — Awaiting User Approval_  
_Execution Rule: DO NOT PERFORM STRUCTURAL CHANGES UNTIL FORMALLY APPROVED_

---

## 1. Overview & Objective

This Migration Plan details the exact, step-by-step structural operations required to transform `content_pipeline/exports/` into the clean, authoritative staging area for the **Learning OS v2 Architecture**.

The plan strictly guarantees:
1. **No Data Loss:** All duplicates, monolithic originals, and legacy structures are safely preserved in `exports/archive/duplicate_courses/`.
2. **Canonical Singularity:** Every course exists in exactly one canonical directory.
3. **Four Strict Tiers:** Clear separation of Foundations (22), Technologies (50), Specializations (11), and Learning Paths (10).
4. **Clean Staging Area:** All `.gdoc` shortcuts, corrupted syllabuses, and duplicate packages are resolved before any notes are generated.

---

## 2. Phased Migration Execution Plan

```
┌─────────────────────────────────────────────────────────────┐
│ PHASE 1: Safety & Archiving Duplicate Packages              │
│ (Safely archive python, java, c-oop, java-selenium, etc.)   │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ PHASE 2: Foundations Relocation                             │
│ (Move 8 Foundation courses from technologies/ to founds/)   │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ PHASE 3: Technologies Relocation                            │
│ (Move 6 Tech from founds/ and 12 Tech from specs/ to tech/) │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ PHASE 4: Conglomerate Monolith Decomposition                │
│ (Decompose data-science, data-analytics, nlp-genai, firebase)│
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ PHASE 5: Syllabus Corrections & Scaffolding Creation        │
│ (Regenerate embedded-c, fix backend-concepts, create stubs) │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ PHASE 6: Learning Path & Prerequisite Synchronization       │
│ (Update referenced_courses.md and roadmap sequence maps)    │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ PHASE 7: Master Index & Documentation Finalization          │
│ (Regenerate course_index.md and README files)               │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Detailed Actions by Phase

### Phase 1: Safety & Duplicate Course Archiving

Create the archive destination: `exports/archive/duplicate_courses/`.

| Source Directory | Action | Destination | Preserved Unique Content |
|---|---|---|---|
| `exports/technologies/python` | Move to Archive | `exports/archive/duplicate_courses/python` | Merged into `foundations/core-python` |
| `exports/technologies/java` | Move to Archive | `exports/archive/duplicate_courses/java` | Merged into `foundations/core-java` |
| `exports/technologies/c-object-oriented-programming` | Move to Archive | `exports/archive/duplicate_courses/c-object-oriented-programming` | Merged into `foundations/cpp` |
| `exports/specializations/java-selenium` | Move to Archive | `exports/archive/duplicate_courses/java-selenium` | Consolidated into `technologies/selenium` |
| `exports/foundations/basic-ml-iot` | Move to Archive | `exports/archive/duplicate_courses/basic-ml-iot` | Merged into `specializations/tinyml` |
| `exports/learning_paths/data-science-learning-path` | Move to Archive | `exports/archive/duplicate_courses/data-science-learning-path` | Replaced by `learning_paths/data-scientist` |

---

### Phase 2: Relocate Foundations from `technologies/` to `foundations/`

Move the 8 zero-prerequisite foundational courses:

```powershell
# Proposed Execution Commands:
Move-Item "exports/technologies/c-programming" "exports/foundations/c-programming"
Move-Item "exports/technologies/core-java"     "exports/foundations/core-java"
Move-Item "exports/technologies/core-python"   "exports/foundations/core-python"
Move-Item "exports/technologies/cpp"           "exports/foundations/cpp"
Move-Item "exports/technologies/css3"          "exports/foundations/css3"
Move-Item "exports/technologies/html5"         "exports/foundations/html5"
Move-Item "exports/technologies/javascript"    "exports/foundations/javascript"
Move-Item "exports/technologies/mysql"         "exports/foundations/mysql"
```

---

### Phase 3: Relocate Technologies to `technologies/`

#### A. Move 6 Tools/Platforms from `foundations/` to `technologies/`:
```powershell
Move-Item "exports/foundations/aws"            "exports/technologies/aws"
Move-Item "exports/foundations/docker"         "exports/technologies/docker"
Move-Item "exports/foundations/github-actions" "exports/technologies/github-actions"
Move-Item "exports/foundations/iot-cloud"      "exports/technologies/iot-cloud"
Move-Item "exports/foundations/jenkins"       "exports/technologies/jenkins"
Move-Item "exports/foundations/kubernetes"    "exports/technologies/kubernetes"
```

#### B. Move 1 Specialization Capstone from `foundations/` to `specializations/`:
```powershell
Move-Item "exports/foundations/iot-projects"   "exports/specializations/iot-projects"
```

#### C. Move 12 Standalone Tools/Platforms from `specializations/` to `technologies/`:
```powershell
Move-Item "exports/specializations/basic-matlab"       "exports/technologies/matlab"
Move-Item "exports/specializations/firebase"           "exports/technologies/firebase"
Move-Item "exports/specializations/manual-testing"     "exports/technologies/manual-testing"
Move-Item "exports/specializations/mqtt"               "exports/technologies/mqtt"
Move-Item "exports/specializations/pcb"                "exports/technologies/pcb-design"
Move-Item "exports/specializations/playwright"         "exports/technologies/playwright"
Move-Item "exports/specializations/postman"            "exports/technologies/postman"
Move-Item "exports/specializations/power-bi"           "exports/technologies/power-bi"
Move-Item "exports/specializations/prompt-engineering" "exports/technologies/prompt-engineering"
Move-Item "exports/specializations/selenium"           "exports/technologies/selenium"
Move-Item "exports/specializations/sql-server"         "exports/technologies/sql-server"
Move-Item "exports/specializations/stm32"              "exports/technologies/stm32"
```

---

### Phase 4: Monolithic Conglomerate Decomposition

1. **`exports/technologies/firebase`:**
   - Archive original monolith to `exports/archive/duplicate_courses/firebase-monolith`.
   - Strip out redundant Section 2 (Auth/JWT) and Section 3 (REST API).
   - Retain only Firebase BaaS modules (Hosting, Realtime DB, Firestore, Functions, Storage, Security Rules).
   - Set prerequisites: `technologies/rest-api` and `technologies/auth-jwt`.

2. **`exports/technologies/data-science`:**
   - Archive original 10,000-line monolith to `exports/archive/duplicate_courses/data-science-monolith`.
   - Ensure roadmap mapping exists in `exports/learning_paths/data-scientist/`.

3. **`exports/technologies/data-analytics`:**
   - Archive original 7,000-line monolith to `exports/archive/duplicate_courses/data-analytics-monolith`.
   - Ensure roadmap mapping exists in `exports/learning_paths/data-analytics/`.

4. **`exports/technologies/nlp-generative-ai`:**
   - Archive original 1,890-line monolith to `exports/archive/duplicate_courses/nlp-generative-ai-monolith`.
   - Ensure individual canonical specializations (`nlp`, `generative-ai-llms`, `prompt-engineering`, `rag-engineering`, `ai-agents`) are referenced in `exports/learning_paths/ai-engineer/`.

---

### Phase 5: Syllabus Bug Corrections & Missing Course Scaffolding

1. **`exports/technologies/embedded-c`:**
   - Regenerate `SYLLABUS/embedded-c.md` to replace HTML5 media/canvas topics with true microcontroller C programming (Memory-mapped registers, bit manipulation, ISR, timers, ADC, PWM, UART/SPI/I2C drivers).
   - Scaffold matching `CURRICULUM/` module folders.

2. **`exports/specializations/backend-concepts-work-package`:**
   - Rename to `exports/technologies/backend-architecture`.
   - Replace `.gdoc` artifact with clean markdown syllabus `backend-architecture.md`.

3. **`exports/specializations/deep-learning`:**
   - Remove raw instructor refactoring notes from syllabus markdown.

4. **Missing Canonical Technology Scaffolds:**
   - Create standard course scaffolds (`README.md`, `COURSE_METADATA.md`, `SYLLABUS/<slug>.md`, `CURRICULUM/`) for:
     1. `exports/technologies/pytorch`
     2. `exports/technologies/tensorflow`
     3. `exports/technologies/opencv`
     4. `exports/technologies/vector-databases`
     5. `exports/technologies/pytest`
     6. `exports/technologies/django`

---

### Phase 6: Learning Path & Reference Synchronization

1. Verify and update all 10 Learning Paths in `exports/learning_paths/` to reference the canonical slugs.
2. Synchronize all `referenced_courses.md` and `roadmap.md` files.

---

### Phase 7: Master Index & Documentation Finalization

1. Regenerate `exports/course_index.md` with complete table of all canonical courses.
2. Update `exports/README.md`, `exports/foundations/README.md`, `exports/technologies/README.md`, and `exports/specializations/README.md`.
3. Produce `exports/FINAL_EXPORT_AUDIT.md`.

---

## 4. Proposed Target Structure Summary

```
exports/
├── ARCHITECTURE_V2.md
├── COURSE_CLASSIFICATION_REPORT.md
├── MIGRATION_PLAN.md
├── MISSING_CANONICAL_COURSES.md
├── AUDIT_BEFORE_MIGRATION.md
├── course_index.md
│
├── foundations/     (22 Pure First-Principles Courses)
├── technologies/    (50 Canonical Standalone Technologies)
├── specializations/ (11 Domain Integration Specializations)
├── learning_paths/  (10 Pure Roadmap Packages)
└── archive/duplicate_courses/ (Safely Preserved Historical Bundles)
```

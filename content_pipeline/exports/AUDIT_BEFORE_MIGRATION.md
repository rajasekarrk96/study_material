# Learning OS v2 — Pre-Migration Baseline Audit (Phase 0)

_Audit Date: 2026-08-09_  
_Scope: Complete inventory of `content_pipeline/exports/`_  
_Status: Authoritative Pre-Migration State Record_

---

## 1. Repository & Directory Verification

- **Repository Root:** `D:\My Drive\all files\PROJECT FILES\notes\content_pipeline\exports`
- **Isolation Check:** Verified that all operations are strictly constrained within `content_pipeline/exports/`. No external application code, production database, or imported production courses will be modified.

---

## 2. Directory & Course Quantities (Current Baseline)

| Directory | Folder Count | Status / Baseline Observation |
|---|---|---|
| `exports/foundations/` | **22 folders** | Contains 8 tools/technologies (`docker`, `kubernetes`, `jenkins`, `aws`, `github-actions`, `iot-cloud`, `basic-ml-iot`, `iot-projects`) that violate the zero-prerequisite Foundation rule. |
| `exports/technologies/` | **44 folders** | Contains 8 Foundations (`core-python`, `c-programming`, `core-java`, `cpp`, `css3`, `html5`, `javascript`, `mysql`), 2 exact duplicates (`python`, `java`), 1 duplicate fragment (`c-object-oriented-programming`), and 3 monolithic conglomerates (`data-science`, `data-analytics`, `nlp-generative-ai`). |
| `exports/specializations/` | **24 folders** | Contains 12 standalone technologies (`basic-matlab`, `firebase`, `java-selenium`, `manual-testing`, `mqtt`, `pcb`, `playwright`, `postman`, `power-bi`, `prompt-engineering`, `selenium`, `sql-server`, `stm32`), 1 misnamed work package with `.gdoc` artifact (`backend-concepts-work-package`), and 1 monolithic multi-course bundle (`firebase`). |
| `exports/learning_paths/` | **10 folders** | Contains 1 legacy-format duplicate path (`data-science-learning-path` vs `data-scientist`). |
| **Total Baseline Folders** | **100 folders** | |

---

## 3. Duplicate Candidates Identified

| Duplicate Pair / Bundle | Location A | Location B | Action in Migration |
|---|---|---|---|
| **Python Foundation** | `technologies/core-python` (323 lines) | `technologies/python` (646 lines) | Consolidate unique topics into canonical `foundations/core-python`. Archive `python`. |
| **Java Foundation** | `technologies/core-java` (1,373 lines) | `technologies/java` (1,664 lines) | Consolidate unique topics into canonical `foundations/core-java`. Archive `java`. |
| **C++ OOP** | `technologies/cpp` (214 lines) | `technologies/c-object-oriented-programming` (131 lines) | Merge OOP classes/templates into `foundations/cpp`. Archive `c-object-oriented-programming`. |
| **Selenium Automation** | `specializations/selenium` (Python) | `specializations/java-selenium` (Java) | Consolidate into canonical `technologies/selenium` with Python and Java sections. Archive `java-selenium`. |
| **Data Science Path** | `learning_paths/data-scientist` | `learning_paths/data-science-learning-path` | Unify into `learning_paths/data-scientist`. Archive legacy path. |
| **TinyML vs Basic ML IoT** | `specializations/tinyml` | `foundations/basic-ml-iot` | Consolidate sensor ML concepts into `specializations/tinyml`. Archive `basic-ml-iot`. |

---

## 4. Monolithic Bundles Requiring Decomposition

1. **`specializations/firebase` (1,054 lines):**
   - Section 1 (Firebase Services: Modules 1–3) — 234 lines
   - Section 2 (Authentication & JWT: Modules 1–6) — 410 lines [Duplicates `auth-jwt`]
   - Section 3 (REST API Architecture: Modules 1–6) — 410 lines [Duplicates `rest-api`]
   - *Plan:* Retain Section 1 as `technologies/firebase`; reference `auth-jwt` and `rest-api` as prerequisites. Archive original monolith.

2. **`technologies/data-science` (10,000+ lines):**
   - Bundles 18 distinct courses into one file.
   - *Plan:* Decompose and archive. Learning path representation maintained in `learning_paths/data-scientist`.

3. **`technologies/data-analytics` (7,000+ lines):**
   - Bundles 11 distinct courses into one file.
   - *Plan:* Decompose and archive. Learning path representation maintained in `learning_paths/data-analytics`.

4. **`technologies/nlp-generative-ai` (1,890 lines):**
   - Bundles Python, NLP, GenAI, Prompt Engineering, RAG, and AI Agents into one file.
   - *Plan:* Decompose and archive. Canonical standalone courses already exist in `specializations/`.

---

## 5. Suspicious / Corrupted / Malformed Folders

| Folder | Path | Specific Defect | Proposed Fix |
|---|---|---|---|
| `embedded-c` | `technologies/embedded-c` | Syllabus contains HTML5 Media (`srcset`, `<picture>`), iFrames, and Canvas 2D API instead of C hardware programming. | Regenerate syllabus with real Embedded C topics (bit manipulation, registers, ISR, timers, memory-mapped I/O). |
| `backend-concepts-work-package` | `specializations/backend-concepts-work-package` | Named with `-work-package` suffix; contains `backend-concepts.md.gdoc` (Google Doc shortcut) instead of clean markdown syllabus. | Normalize folder name to `technologies/backend-architecture` with clean markdown syllabus. |
| `deep-learning` | `specializations/deep-learning` | Syllabus contains raw refactoring instructional notes embedded in text. | Clean up syllabus markdown to present clean course topics. |

---

## 6. Target Reclassification Summary

```
Total Baseline: 100 Folders (22 Found + 44 Tech + 24 Spec + 10 LP)
  │
  ├── Relocate 8 Foundations from technologies/ ──► foundations/
  ├── Relocate 6 Technologies from foundations/ ──► technologies/
  ├── Relocate 2 Specializations from foundations/ ──► specializations/
  ├── Relocate 12 Technologies from specializations/ ──► technologies/
  ├── Merge & Archive 4 Duplicates (python, java, c-oop, java-selenium)
  ├── Decompose & Archive 3 Monolithic bundles (data-science, data-analytics, nlp-genai)
  ├── Consolidate 1 Legacy Learning Path (data-science-learning-path)
  └── Provision 6 Missing Canonical Tech Stubs (pytorch, tensorflow, opencv, vector-databases, pytest, django)
  │
  ▼
Target Post-Migration Architecture:
  ├── foundations/      : 22 Pure First-Principles Courses
  ├── technologies/     : 50 Canonical Standalone Technologies (including 6 new canonical stubs)
  ├── specializations/  : 11 Integration-Only Professional Specializations
  ├── learning_paths/   : 10 Approved Canonical Career Roadmaps
  └── archive/duplicate_courses/ : 8 Archived Original Packages
```

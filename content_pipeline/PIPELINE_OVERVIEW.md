# Pipeline Architecture Overview

**Version:** 1.0.0 | **Created:** 2026-08-06

---

## System Architecture

The Learning OS Content Pipeline has five zones:

```
┌─────────────────────────────────────────────────────┐
│              LEARNING OS (Master Repository)        │
│   docs/syllabus/   docs/curriculum/   app/          │
└─────────────────────────┬───────────────────────────┘
                          │  READ ONLY
              ┌───────────▼────────────┐
              │    EXPORT ZONE         │
              │  content_pipeline/     │
              │  exports/              │
              │  ├── shared/           │
              │  ├── learning_paths/   │
              │  └── specializations/  │
              └───────────┬────────────┘
                          │  SENT TO CONTRIBUTOR
              ┌───────────▼────────────┐
              │  CONTRIBUTOR / AI ZONE │
              │  (External — isolated) │
              │  Edits CURRICULUM/only │
              └───────────┬────────────┘
                          │  RETURNED TO PIPELINE
              ┌───────────▼────────────┐
              │    IMPORT ZONE         │
              │  imports/              │
              │  ├── pending_review/   │
              │  ├── under_review/     │
              │  ├── approved/         │
              │  └── rejected/         │
              └───────────┬────────────┘
                          │  AFTER APPROVAL
              ┌───────────▼────────────┐
              │    MERGE ZONE          │
              │  (Controlled write     │
              │   to Learning OS)      │
              └───────────┬────────────┘
                          │  AFTER MERGE
              ┌───────────▼────────────┐
              │   ARCHIVE ZONE         │
              │  completed/            │
              │  ├── shared/           │
              │  ├── learning_paths/   │
              │  └── specializations/  │
              └────────────────────────┘
```

---

## Package Lifecycle States

```
CREATED → EXPORTED → RETURNED → UNDER_REVIEW → APPROVED → MERGED → ARCHIVED
                                      │
                                      └──→ REJECTED → (back to contributor)
```

| State | Location | Who Acts |
|---|---|---|
| CREATED | (being built) | Admin / System |
| EXPORTED | exports/ | — |
| RETURNED | imports/pending_review/ | Contributor |
| UNDER_REVIEW | imports/under_review/ | Reviewer |
| APPROVED | imports/approved/ | Reviewer |
| REJECTED | imports/rejected/ | Reviewer |
| MERGED | (into Learning OS) | Admin |
| ARCHIVED | completed/ | System |

---

## Package Types

### 1. Shared Course Package

A single standalone course that is reused across multiple learning paths.

```
shared/_06_javascript/
├── PACKAGE_MANIFEST.md
├── README.md
├── COURSE_METADATA.md
├── SYLLABUS/javascript.md
├── CURRICULUM/javascript/
├── STYLE_GUIDE.md
├── NOTE_TEMPLATE.md
├── CHECKLIST.md
├── VALIDATION_RULES.md
├── CONTRIBUTOR_GUIDE.md
├── REPORT.md
└── reports/
```

### 2. Learning Path Package

A full learning path including ordered course references and dedicated course curricula.

```
learning_paths/frontend_engineering/
├── PACKAGE_MANIFEST.md
├── README.md
├── LEARNING_PATH.md
├── REFERENCED_COURSES.md    ← Shared courses — DO NOT copy
├── COURSE_METADATA.md
├── SYLLABUS/
├── CURRICULUM/
├── ...
└── reports/
```

### 3. Specialization Package

A standalone specialization course (not duplicating shared content).

```
specializations/machine_learning/
├── PACKAGE_MANIFEST.md
├── README.md
├── COURSE_METADATA.md
├── SYLLABUS/machine-learning.md
├── CURRICULUM/machine-learning/
├── ...
└── reports/
```

---

## Versioning

Every package carries a version number following semantic versioning:

- **MAJOR** — syllabus changed significantly (restructured modules)
- **MINOR** — new lessons added to existing syllabus
- **PATCH** — content corrections, coverage updates

See [VERSIONING.md](VERSIONING.md) for the full versioning specification.

---

## Concurrency

Multiple contributors can work simultaneously because:

- Each package is **isolated** — one contributor per package at a time
- No two packages share the same `package_id`
- The registry tracks exactly who has what version of what package
- The merge process checks for conflicts before writing to Learning OS

---

## Traceability

Every package action is logged in `registry/PACKAGE_REGISTRY.md` and individual package `PACKAGE_MANIFEST.md` files. The system maintains:

- Full history of every export
- Full history of every review decision
- Full merge log
- Archive of every contributor package ever returned

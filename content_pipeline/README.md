# Learning OS — Content Pipeline

**Version:** 1.0.0  
**Created:** 2026-08-06  
**Owner:** Learning OS Team

---

## What is the Content Pipeline?

The Content Pipeline is the **collaboration infrastructure** that allows multiple contributors and AI agents to generate curriculum notes independently, without ever touching the main Learning OS.

The Learning OS is always the **Master Repository**. Exports are temporary working copies. Imports are returned work awaiting review. Completed packages are archived history.

---

## How It Works

```
Learning OS (Master)
        │
        ▼
  [1] EXPORT PACKAGE
        │  Package created with syllabus + stubs
        │  Assigned to contributor or AI agent
        ▼
  [2] CONTRIBUTOR WORKS
        │  Writes notes into CURRICULUM/ only
        │  Never touches Learning OS
        ▼
  [3] IMPORT (Return)
        │  Package placed in imports/pending_review/
        ▼
  [4] AUDIT & VALIDATION
        │  Automated validation scripts run
        │  Audit report generated
        ▼
  [5] REVIEW
        │  Human reviewer checks content quality
        │  Approved → imports/approved/
        │  Rejected → imports/rejected/ with comments
        ▼
  [6] MERGE
        │  Approved content merged into Learning OS
        │  One course at a time, verified
        ▼
  [7] ARCHIVE
        │  Package moved to completed/
        │  Full history preserved forever
        ▼
  Learning OS (Updated Master)
```

---

## Quick Links

| Document | Purpose |
|---|---|
| [PIPELINE_OVERVIEW.md](PIPELINE_OVERVIEW.md) | Full system architecture |
| [EXPORT_WORKFLOW.md](EXPORT_WORKFLOW.md) | How to create and send export packages |
| [IMPORT_WORKFLOW.md](IMPORT_WORKFLOW.md) | How to receive and log returned packages |
| [REVIEW_WORKFLOW.md](REVIEW_WORKFLOW.md) | How to audit and review content |
| [MERGE_WORKFLOW.md](MERGE_WORKFLOW.md) | How to merge approved content |
| [ARCHIVE_WORKFLOW.md](ARCHIVE_WORKFLOW.md) | How to archive completed work |
| [FOLDER_STRUCTURE.md](FOLDER_STRUCTURE.md) | Complete directory reference |
| [VERSIONING.md](VERSIONING.md) | Package versioning and traceability |
| [CONTRIBUTOR_DOCS.md](CONTRIBUTOR_DOCS.md) | Guide for contributors |
| [REVIEWER_DOCS.md](REVIEWER_DOCS.md) | Guide for reviewers |
| [ADMIN_DOCS.md](ADMIN_DOCS.md) | Guide for administrators |

---

## Directory Structure

```
content_pipeline/
├── README.md
├── PIPELINE_OVERVIEW.md
├── EXPORT_WORKFLOW.md
├── IMPORT_WORKFLOW.md
├── REVIEW_WORKFLOW.md
├── MERGE_WORKFLOW.md
├── ARCHIVE_WORKFLOW.md
├── FOLDER_STRUCTURE.md
├── VERSIONING.md
├── CONTRIBUTOR_DOCS.md
├── REVIEWER_DOCS.md
├── ADMIN_DOCS.md
│
├── exports/                   ← Packages sent to contributors
│   ├── shared/                ← Individual shared/reusable courses
│   ├── learning_paths/        ← Full learning path packages
│   └── specializations/       ← Specialization course packages
│
├── imports/                   ← Packages returned by contributors
│   ├── pending_review/        ← Returned, awaiting audit
│   ├── under_review/          ← Currently being audited
│   ├── approved/              ← Passed audit, ready to merge
│   └── rejected/              ← Needs corrections
│
├── completed/                 ← Merged and archived packages
│   ├── shared/
│   ├── learning_paths/
│   └── specializations/
│
├── reports/                   ← System-wide audit and health reports
├── templates/                 ← Package and document templates
├── scripts/                   ← Validation, audit, merge scripts
└── registry/                  ← Package registry and version tracking
```

---

## Ground Rules

1. **Never modify** `docs/`, `app/`, or any Learning OS file from within this pipeline
2. **Never auto-merge** — all merges require human approval
3. **Never delete** contributor packages — archive them in `completed/`
4. **Every package** must carry a versioned `PACKAGE_MANIFEST.md`
5. **One reviewer** must sign off before any merge

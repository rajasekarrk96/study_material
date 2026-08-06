"""
Learning OS — Content Pipeline Scaffold Builder
================================================
Creates the complete content_pipeline/ directory structure with all
documentation, templates, validation scripts, and workflow files.

Run from project root:
    python scripts/build_content_pipeline.py

Safe: creates only new files under content_pipeline/.
Never modifies any existing Learning OS file.
"""
import sys
import json
import uuid
from pathlib import Path
from datetime import datetime, timezone

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"d:\My Drive\all files\PROJECT FILES\notes")
CP   = ROOT / "content_pipeline"

TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")

# ── Directory skeleton ───────────────────────────────────────────────────────
DIRS = [
    "exports/shared",
    "exports/learning_paths",
    "exports/specializations",
    "imports/pending_review",
    "imports/under_review",
    "imports/approved",
    "imports/rejected",
    "completed/shared",
    "completed/learning_paths",
    "completed/specializations",
    "reports",
    "templates",
    "scripts",
    "registry",
]

# ── File manifest ────────────────────────────────────────────────────────────
FILES = {}

# ════════════════════════════════════════════════════════════════════════════
# ROOT DOCUMENTS
# ════════════════════════════════════════════════════════════════════════════

FILES["README.md"] = f"""# Learning OS — Content Pipeline

**Version:** 1.0.0  
**Created:** {TODAY}  
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
"""

# ════════════════════════════════════════════════════════════════════════════
FILES["PIPELINE_OVERVIEW.md"] = f"""# Pipeline Architecture Overview

**Version:** 1.0.0 | **Created:** {TODAY}

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
"""

# ════════════════════════════════════════════════════════════════════════════
FILES["EXPORT_WORKFLOW.md"] = f"""# Export Workflow

**Updated:** {TODAY}

---

## Overview

An export package is a self-contained working copy of one or more courses, sent to a contributor to write lesson notes.

---

## Step 1 — Identify What to Export

Decide the export type:

| Type | When to use | Script |
|---|---|---|
| Shared course | Single course, reused across paths | `scripts/export_shared.py` |
| Learning path | Full path with multiple courses | `scripts/export_learning_path.py` |
| Specialization | Single specialization course | `scripts/export_specialization.py` |

---

## Step 2 — Create the Package

Run the appropriate export script:

```bash
# Export a single shared course
python scripts/export_shared.py --course javascript --assigned-to "contributor-name"

# Export a learning path
python scripts/export_learning_path.py --path frontend_engineering --assigned-to "team-name"

# Export a specialization
python scripts/export_specialization.py --course machine_learning --assigned-to "ml-team"
```

The script will:
1. Create the package directory under `exports/<type>/<package_slug>/`
2. Generate a unique `package_id`
3. Copy syllabus from `docs/syllabus/`
4. Copy existing curriculum from `docs/curriculum/`
5. Create placeholder stubs for missing lessons
6. Generate all package documents
7. Register the package in `registry/PACKAGE_REGISTRY.md`
8. Write `PACKAGE_MANIFEST.md` with status = EXPORTED

---

## Step 3 — Assign to Contributor

Update `PACKAGE_MANIFEST.md`:

```yaml
assigned_to: contributor-name-or-team
export_date: YYYY-MM-DD
status: EXPORTED
```

Send the contributor:
- The package folder (zip or repo access)
- Link to `CONTRIBUTOR_DOCS.md`
- Deadline for return

---

## Step 4 — Log in Registry

The export script auto-logs to `registry/PACKAGE_REGISTRY.md`.

If logging manually:

```
| package_id | course | type | version | export_date | assigned_to | status |
```

---

## Naming Convention

```
exports/<type>/<order_prefix>_<slug>/

Examples:
exports/shared/_06_javascript/
exports/shared/_09_flask/
exports/learning_paths/frontend_engineering/
exports/specializations/machine_learning/
```

Order prefixes for shared courses follow the Learning OS numbering.

---

## What Gets Included

| File | Source | Action |
|---|---|---|
| `PACKAGE_MANIFEST.md` | Generated | Created with metadata |
| `README.md` | Template | Customized |
| `COURSE_METADATA.md` | Generated | From Learning OS data |
| `SYLLABUS/*.md` | `docs/syllabus/` | Copied read-only |
| `CURRICULUM/**` | `docs/curriculum/` | Copied (real files) + stubs (missing) |
| `STYLE_GUIDE.md` | Template | Shared standard |
| `NOTE_TEMPLATE.md` | Template | Shared standard |
| `CHECKLIST.md` | Template | Customized per course |
| `VALIDATION_RULES.md` | Template | Shared standard |
| `CONTRIBUTOR_GUIDE.md` | Template | Customized |
| `REPORT.md` | Template | Blank for contributor |
| `reports/` | Generated | Health + missing notes |

---

## What Is NEVER Included

- Any file from `app/` (the web application)
- Database files or secrets (`.env`)
- Other courses not in scope (no duplication)
- The complete Learning OS

---

## Multiple Simultaneous Exports

Yes — multiple packages can be active simultaneously.

Each package has a unique `package_id`. The registry prevents two packages for the same course version from being active at the same time.

If a course is already exported to Contributor A, a new export for Contributor B will receive the next patch version.
"""

# ════════════════════════════════════════════════════════════════════════════
FILES["IMPORT_WORKFLOW.md"] = f"""# Import Workflow

**Updated:** {TODAY}

---

## Overview

An import is a returned package from a contributor. It enters the pipeline at `imports/pending_review/` and progresses through audit, review, approval or rejection.

---

## Step 1 — Receive the Package

When a contributor returns a package:

1. Place the entire returned folder into `imports/pending_review/<package_id>/`
2. Run the import validator immediately:

```bash
python scripts/validate_import.py --package imports/pending_review/<package_id>
```

3. Update `PACKAGE_MANIFEST.md`:
```yaml
status: RETURNED
return_date: YYYY-MM-DD
```

4. Log the return in `registry/PACKAGE_REGISTRY.md`

---

## Step 2 — Automated Validation

`scripts/validate_import.py` checks:

| Check | What it verifies |
|---|---|
| Structure | Required files and folders present |
| Manifest | `PACKAGE_MANIFEST.md` has all fields |
| Stubs | All stub files have been written (> 500 bytes) |
| Filenames | No renames, no unauthorized additions |
| Code blocks | All fenced blocks have language identifiers |
| Headings | H1 present in every lesson file |
| References | References section present in every lesson |
| Interview Qs | At least 3 per lesson |
| Checklist | `CHECKLIST.md` is filled |
| Report | `REPORT.md` is filled |

Generates: `reports/VALIDATION_REPORT_<package_id>_<date>.md`

---

## Step 3 — Move to Under Review

If automated validation passes:

```bash
python scripts/move_to_review.py --package imports/pending_review/<package_id>
# Moves to: imports/under_review/<package_id>
```

Update `PACKAGE_MANIFEST.md`:
```yaml
status: UNDER_REVIEW
review_start_date: YYYY-MM-DD
reviewed_by: reviewer-name
```

If automated validation **fails**:
- Move to `imports/rejected/<package_id>/`
- Generate rejection comments from validation errors
- Notify contributor with `templates/REJECTION_NOTICE.md`

---

## Step 4 — Human Review

Reviewer reads the content in `imports/under_review/<package_id>/CURRICULUM/`

Review criteria:
- Technical accuracy
- Depth appropriate for the target audience
- Code examples are runnable
- Interview questions are meaningful
- References are real and valid

Reviewer fills in `templates/REVIEW_COMMENTS.md`

---

## Step 5 — Decision

**APPROVED:**
```bash
python scripts/approve_package.py --package imports/under_review/<package_id>
# Moves to: imports/approved/<package_id>
```

**REJECTED:**
```bash
python scripts/reject_package.py --package imports/under_review/<package_id> --reason "comments"
# Moves to: imports/rejected/<package_id>
```

---

## Step 6 — Notify Contributor

- Approved: Send merge confirmation with timeline
- Rejected: Send `REJECTION_NOTICE.md` with specific correction requests

---

## Import Naming Convention

```
imports/<state>/<package_id>/

Example:
imports/pending_review/PKG-20260806-JS-001/
imports/under_review/PKG-20260806-JS-001/
imports/approved/PKG-20260806-JS-001/
imports/rejected/PKG-20260806-JS-001/
```
"""

# ════════════════════════════════════════════════════════════════════════════
FILES["REVIEW_WORKFLOW.md"] = f"""# Review Workflow

**Updated:** {TODAY}

---

## Overview

The review stage is the human quality gate. Only content that passes both automated validation and human review is approved for merge into the Learning OS.

---

## Reviewer Responsibilities

A reviewer must:

1. Check technical accuracy of all lesson notes
2. Verify code examples compile and run
3. Confirm interview questions are meaningful and correctly answered
4. Ensure depth matches the target audience
5. Validate that no existing notes were modified
6. Confirm no unauthorized files were added
7. Check references are real, accessible URLs

---

## Review Process

### Step 1 — Accept a Package

A package arrives in `imports/under_review/` after passing automated validation.

```bash
# See all packages under review
python scripts/list_packages.py --state under_review
```

### Step 2 — Run Audit

```bash
python scripts/audit_package.py --package imports/under_review/<package_id>
```

This generates `reports/AUDIT_REPORT_<package_id>_<date>.md` with:
- Curriculum health summary
- Syllabus coverage analysis
- Duplicate detection
- Quality score estimate
- Specific flagged issues

### Step 3 — Review Reports

Read in order:
1. `reports/AUDIT_REPORT_<package_id>_<date>.md`
2. `reports/CURRICULUM_HEALTH_<package_id>.md`
3. `reports/SYLLABUS_COVERAGE_<package_id>.md`
4. `reports/QUALITY_REPORT_<package_id>.md`

### Step 4 — Spot-Check Lessons

Manually review a sample of lessons (minimum 10% of new files):

Checklist per lesson:
- [ ] H1 title matches the lesson topic
- [ ] Metadata blockquote on line 3
- [ ] All 16 required sections present
- [ ] Code examples have language identifiers
- [ ] Examples are runnable (not pseudocode)
- [ ] At least 3 interview questions
- [ ] References section has valid links
- [ ] Depth appropriate for course level

### Step 5 — Fill Review Comments

Use `templates/REVIEW_COMMENTS.md` to document:
- Overall quality score (1–10)
- List of specific issues found (file, line, issue, suggested fix)
- Approval recommendation

### Step 6 — Approve or Reject

**Approve:** All lessons pass quality review
```bash
python scripts/approve_package.py --package imports/under_review/<package_id> --reviewer "your-name"
```

**Reject:** Issues found that require correction
```bash
python scripts/reject_package.py --package imports/under_review/<package_id> --reviewer "your-name"
```

---

## Quality Scoring Rubric

| Criterion | Weight | Score/5 |
|---|---|---|
| Technical Accuracy | 30% | |
| Code Quality | 20% | |
| Interview Question Depth | 15% | |
| Writing Clarity | 15% | |
| Style Compliance | 10% | |
| References Quality | 10% | |

**Total Score = Weighted Average**

- 4.0–5.0 → Approve
- 3.0–3.9 → Conditional Approve (minor fixes only)
- < 3.0 → Reject

---

## Review SLA

| Package Size | Review Target |
|---|---|
| < 20 lessons | 24 hours |
| 20–100 lessons | 3 business days |
| > 100 lessons | 5 business days |
"""

# ════════════════════════════════════════════════════════════════════════════
FILES["MERGE_WORKFLOW.md"] = f"""# Merge Workflow

**Updated:** {TODAY}

---

## Overview

Merging is the controlled process of writing approved contributor content into the Learning OS master repository. It must never happen automatically.

---

## Pre-Merge Checklist

Before running any merge:

- [ ] Package is in `imports/approved/`
- [ ] `PACKAGE_MANIFEST.md` status = APPROVED
- [ ] Reviewer signature present in manifest
- [ ] No active exports of the same course at a higher version
- [ ] Learning OS `docs/curriculum/` is in a clean state (no pending changes)

---

## Step 1 — Dry Run

Always run a dry run first:

```bash
python scripts/merge_package.py --package imports/approved/<package_id> --dry-run
```

Output shows:
- Files that will be CREATED (new lessons)
- Files that will be UPDATED (stubs → real content)
- Files that will NOT be touched (existing complete notes)
- Potential conflicts
- Syllabus alignment check

---

## Step 2 — Review Dry Run Output

Check `reports/MERGE_REPORT_<package_id>_dryrun_<date>.md`:

Verify:
- No unexpected file overwrites
- No duplicate lesson filenames
- No syllabus mismatch
- No broken module numbering
- No cross-course contamination

---

## Step 3 — Execute Merge

```bash
python scripts/merge_package.py --package imports/approved/<package_id> --execute
```

The script:
1. For each file in `CURRICULUM/<course>/`:
   - If file exists in `docs/curriculum/<folder>/` and is complete → SKIP
   - If file is a stub → OVERWRITE with new content
   - If file does not exist → CREATE
2. Logs every action to `reports/MERGE_REPORT_<package_id>_<date>.md`
3. Updates `PACKAGE_MANIFEST.md` → status: MERGED
4. Updates `registry/PACKAGE_REGISTRY.md`

---

## Step 4 — Post-Merge Verification

```bash
python scripts/verify_merge.py --package imports/approved/<package_id>
```

Checks:
- All expected files now exist in `docs/curriculum/`
- No files were accidentally deleted
- No corruption in merged files

---

## Step 5 — Archive

```bash
python scripts/archive_package.py --package imports/approved/<package_id>
```

Moves package to `completed/<type>/<package_id>/`

Updates manifest → status: ARCHIVED

---

## Merge Rules (Non-Negotiable)

| Rule | Detail |
|---|---|
| Never auto-merge | Human must explicitly run merge command |
| Never overwrite complete notes | Only stubs (< 500 bytes) can be overwritten |
| One course per merge | Don't merge multiple courses in one operation |
| Version must match | Package version must match the syllabus version it was exported against |
| Log everything | Every file operation is logged |
| Rollback available | Keep original stubs in `completed/` as rollback source |

---

## Conflict Resolution

If a conflict is detected (e.g., the syllabus changed since the package was exported):

1. Do NOT merge
2. Create a conflict report: `reports/CONFLICT_REPORT_<package_id>_<date>.md`
3. Notify contributor that their package is based on an outdated syllabus
4. Offer options:
   - Re-export with new syllabus, re-assign to same contributor
   - Manually reconcile the differences
   - Reject the package and start fresh
"""

# ════════════════════════════════════════════════════════════════════════════
FILES["ARCHIVE_WORKFLOW.md"] = f"""# Archive Workflow

**Updated:** {TODAY}

---

## Overview

Every contributor package is permanently archived after merge. The archive is the complete history of the Learning OS content development.

---

## Archive Locations

```
completed/
├── shared/              ← Archived single shared course packages
├── learning_paths/      ← Archived learning path packages
└── specializations/     ← Archived specialization packages
```

---

## Archive Naming

```
completed/<type>/<package_id>_v<version>_<merged_date>/

Example:
completed/shared/PKG-20260806-JS-001_v1.0.0_20260810/
completed/learning_paths/PKG-20260807-FRONTEND-001_v1.0.0_20260815/
```

---

## What Gets Archived

The **complete returned package** as it was received from the contributor, including:
- All written lesson files
- `PACKAGE_MANIFEST.md` (with full lifecycle history)
- `REPORT.md` (contributor's self-report)
- `CHECKLIST.md` (contributor's checklist)
- The original `CURRICULUM/` with all content
- Review comments from reviewer
- All audit reports generated during review

---

## Why Archive Everything?

1. **Rollback** — If merged content has errors found later, original can be traced
2. **Attribution** — Know which contributor wrote which note
3. **Version history** — Track how the curriculum evolved over time
4. **Dispute resolution** — Evidence of what was submitted and reviewed
5. **Audit trail** — Complete pipeline traceability

---

## Archive Process

```bash
# Run automatically as part of merge, or manually:
python scripts/archive_package.py --package imports/approved/<package_id>
```

Steps performed:
1. Creates `completed/<type>/<package_id>_v<version>_<date>/`
2. Copies all package files to archive
3. Writes final `PACKAGE_MANIFEST.md` with complete lifecycle
4. Updates `registry/PACKAGE_REGISTRY.md` → status: ARCHIVED
5. Removes package from `imports/approved/`

---

## Retention Policy

- Archived packages are **never deleted**
- Archives are compressed after 1 year
- Archives are indexed in `registry/ARCHIVE_INDEX.md`

---

## Searching the Archive

```bash
# Search archive by course
python scripts/search_archive.py --course javascript

# Search archive by contributor
python scripts/search_archive.py --contributor "contributor-name"

# Search archive by date range
python scripts/search_archive.py --from 2026-01-01 --to 2026-12-31
```
"""

# ════════════════════════════════════════════════════════════════════════════
FILES["VERSIONING.md"] = f"""# Package Versioning System

**Updated:** {TODAY}

---

## Overview

Every export package carries a version number. This enables full traceability — if a contributor returns work based on an old syllabus, the version mismatch is detected before merge.

---

## Version Format

```
MAJOR.MINOR.PATCH

Examples:
1.0.0  — Initial export
1.0.1  — Patch: fixed typos in stub titles
1.1.0  — Minor: added 3 new lessons to Module 4
2.0.0  — Major: Module structure reorganized
```

---

## Version Increment Rules

| Change Type | Version Bump | Example |
|---|---|---|
| Syllabus module restructure | MAJOR | 1.x.x → 2.0.0 |
| New lessons added to syllabus | MINOR | 1.0.x → 1.1.0 |
| Stub title or metadata fix | PATCH | 1.0.0 → 1.0.1 |
| Coverage field update only | PATCH | 1.0.0 → 1.0.1 |
| Content corrections in existing notes | PATCH | 1.0.0 → 1.0.1 |

---

## Package ID Format

```
PKG-<YYYYMMDD>-<COURSE_CODE>-<SEQ>

Examples:
PKG-20260806-JS-001
PKG-20260806-FRONTEND-001
PKG-20260807-ML-001
PKG-20260807-ML-002   ← Second ML package exported same day
```

---

## PACKAGE_MANIFEST.md Structure

Every package contains a `PACKAGE_MANIFEST.md` with these fields:

```yaml
# Package Manifest

package_id:      PKG-20260806-JS-001
course_name:     JavaScript Core
learning_path:   Frontend Engineering
package_type:    shared         # shared | learning_path | specialization
version:         1.0.0
syllabus_version: 1.0.0        # Version of the syllabus this was exported from

export_date:     2026-08-06
assigned_to:     contributor-name
deadline:        2026-08-20

status:          EXPORTED       # CREATED | EXPORTED | RETURNED | UNDER_REVIEW |
                               # APPROVED | REJECTED | MERGED | ARCHIVED

# Filled on return:
return_date:     ~
returned_by:     ~

# Filled during review:
review_start_date: ~
reviewed_by:       ~
review_end_date:   ~
review_score:      ~           # 1.0–5.0

# Filled on decision:
decision:          ~           # APPROVED | REJECTED
decision_date:     ~
decision_notes:    ~

# Filled on merge:
merged_by:         ~
merge_date:        ~
merge_report:      ~           # Path to merge report

# Filled on archive:
archive_path:      ~
archive_date:      ~
```

---

## Version Conflict Detection

When a package is returned for review, the system checks:

```
Package syllabus_version == Current Learning OS syllabus version?
```

If **mismatch detected**:
- Warn reviewer with `CONFLICT_REPORT.md`
- Do not auto-reject — human decides
- Options: reconcile, re-export, or reject

---

## Registry

`registry/PACKAGE_REGISTRY.md` tracks all packages:

| package_id | course | type | version | status | assigned_to | export_date | return_date | merge_date |
|---|---|---|---|---|---|---|---|---|

`registry/ARCHIVE_INDEX.md` tracks all completed packages.
`registry/ACTIVE_EXPORTS.md` tracks currently active (unreturned) exports.
"""

# ════════════════════════════════════════════════════════════════════════════
FILES["FOLDER_STRUCTURE.md"] = f"""# Folder Structure Reference

**Updated:** {TODAY}

---

## Complete Directory Tree

```
content_pipeline/
│
├── README.md                    ← System overview
├── PIPELINE_OVERVIEW.md         ← Architecture diagrams
├── EXPORT_WORKFLOW.md           ← Export process
├── IMPORT_WORKFLOW.md           ← Import process
├── REVIEW_WORKFLOW.md           ← Review process
├── MERGE_WORKFLOW.md            ← Merge process
├── ARCHIVE_WORKFLOW.md          ← Archive process
├── FOLDER_STRUCTURE.md          ← This file
├── VERSIONING.md                ← Version and ID system
├── CONTRIBUTOR_DOCS.md          ← For contributors
├── REVIEWER_DOCS.md             ← For reviewers
├── ADMIN_DOCS.md                ← For administrators
│
├── exports/                     ← Active export packages
│   │
│   ├── shared/                  ← Individual reusable course packages
│   │   ├── _01_c_programming/
│   │   ├── _02_cpp_programming/
│   │   ├── _03_git_version_control/
│   │   ├── _04_html5/
│   │   ├── _05_css3/
│   │   ├── _06_bootstrap/
│   │   ├── _07_javascript/
│   │   ├── _08_jquery/
│   │   ├── _09_python_core/
│   │   ├── _10_advanced_python/
│   │   ├── _11_java_core/
│   │   ├── _12_spring_boot/
│   │   ├── _13_mysql/
│   │   ├── _14_sql_server/
│   │   ├── _15_mongodb/
│   │   ├── _16_flask/
│   │   ├── _17_fastapi/
│   │   ├── _18_rest_api/
│   │   ├── _19_auth_jwt/
│   │   ├── _20_react/
│   │   ├── _21_selenium/
│   │   ├── _22_linux/
│   │   ├── _23_docker/
│   │   └── ...
│   │
│   ├── learning_paths/          ← Full learning path packages
│   │   ├── python_full_stack/
│   │   ├── java_full_stack/
│   │   ├── frontend_engineering/
│   │   ├── backend_engineering/
│   │   ├── data_science/
│   │   ├── ai_engineering/
│   │   ├── devops/
│   │   ├── cloud_engineering/
│   │   ├── iot_full_stack/
│   │   └── dotnet_full_stack/
│   │
│   └── specializations/         ← Specialization packages
│       ├── machine_learning/
│       ├── deep_learning/
│       ├── computer_vision/
│       ├── nlp/
│       ├── mlops/
│       ├── powerbi/
│       ├── tableau/
│       ├── excel/
│       ├── mongodb/
│       ├── big_data/
│       ├── hadoop/
│       ├── spark/
│       ├── airflow/
│       ├── kubeflow/
│       ├── mlflow/
│       ├── pcb_design/
│       ├── esp32/
│       └── arduino/
│
├── imports/                     ← Returned packages in various states
│   ├── pending_review/          ← Just returned, not yet audited
│   ├── under_review/            ← Being reviewed right now
│   ├── approved/                ← Passed review, ready to merge
│   └── rejected/                ← Needs corrections
│
├── completed/                   ← Permanently archived packages
│   ├── shared/
│   ├── learning_paths/
│   └── specializations/
│
├── reports/                     ← System-wide reports
│   ├── AUDIT_REPORT_*.md
│   ├── CURRICULUM_HEALTH_*.md
│   ├── SYLLABUS_COVERAGE_*.md
│   ├── DUPLICATE_REPORT_*.md
│   ├── QUALITY_REPORT_*.md
│   ├── MERGE_REPORT_*.md
│   └── CONFLICT_REPORT_*.md
│
├── templates/                   ← Reusable document templates
│   ├── PACKAGE_MANIFEST.md
│   ├── README_template.md
│   ├── COURSE_METADATA_template.md
│   ├── STYLE_GUIDE.md
│   ├── NOTE_TEMPLATE.md
│   ├── CHECKLIST_template.md
│   ├── VALIDATION_RULES.md
│   ├── CONTRIBUTOR_GUIDE_template.md
│   ├── REPORT_template.md
│   ├── REVIEW_COMMENTS.md
│   ├── REJECTION_NOTICE.md
│   └── MERGE_REQUEST.md
│
├── scripts/                     ← Automation scripts
│   ├── export_shared.py
│   ├── export_learning_path.py
│   ├── export_specialization.py
│   ├── validate_import.py
│   ├── audit_package.py
│   ├── move_to_review.py
│   ├── approve_package.py
│   ├── reject_package.py
│   ├── merge_package.py
│   ├── verify_merge.py
│   ├── archive_package.py
│   ├── list_packages.py
│   └── search_archive.py
│
└── registry/                    ← Package tracking
    ├── PACKAGE_REGISTRY.md
    ├── ACTIVE_EXPORTS.md
    └── ARCHIVE_INDEX.md
```

---

## Naming Conventions

### Export Packages

| Type | Convention | Example |
|---|---|---|
| Shared course | `_NN_<slug>/` | `_06_javascript/` |
| Learning path | `<slug>/` | `frontend_engineering/` |
| Specialization | `<slug>/` | `machine_learning/` |

### Import Packages

All imports use the `package_id` as the folder name:
```
imports/pending_review/PKG-20260806-JS-001/
```

### Archive Packages

```
completed/<type>/PKG-<id>_v<version>_<merged_date>/
```

### Reports

```
reports/AUDIT_REPORT_<package_id>_<date>.md
reports/MERGE_REPORT_<package_id>_<date>.md
```
"""

# ════════════════════════════════════════════════════════════════════════════
FILES["CONTRIBUTOR_DOCS.md"] = f"""# Contributor Documentation

**Learning OS Content Pipeline — Contributor Guide**  
**Updated:** {TODAY}

---

## Welcome

Thank you for contributing to the Learning OS curriculum.

This document explains everything you need to know as a content contributor.

---

## Your Role

You receive a **package** — a folder containing syllabus, stubs, and documentation.

Your job is to write lesson notes into the stub files in `CURRICULUM/`.

You **never** touch the main Learning OS. You only edit files inside the package you received.

---

## What You Receive

A package folder containing:

```
<package_name>/
├── PACKAGE_MANIFEST.md    ← Your assignment details
├── README.md              ← Start here
├── COURSE_METADATA.md     ← Course scope
├── STYLE_GUIDE.md         ← Formatting rules
├── NOTE_TEMPLATE.md       ← Note structure template
├── CONTRIBUTOR_GUIDE.md   ← Step-by-step workflow
├── CHECKLIST.md           ← What you must complete
├── VALIDATION_RULES.md    ← Rules enforced during audit
├── REPORT.md              ← Fill this before returning
├── SYLLABUS/              ← Read-only: do not modify
└── CURRICULUM/            ← EDIT ONLY HERE
    └── reports/
        └── MISSING_NOTES.md   ← Your todo list
```

---

## Your Workflow

### 1. Read (required before writing anything)

Read in this exact order:
1. `PACKAGE_MANIFEST.md` — understand your assignment and deadline
2. `README.md` — understand the package scope
3. `COURSE_METADATA.md` — understand the course
4. `reports/MISSING_NOTES.md` — find exactly what to write
5. `NOTE_TEMPLATE.md` — memorize the 16-section structure
6. `STYLE_GUIDE.md` — understand all formatting rules
7. 3 existing notes (calibrate depth and style)

### 2. Write

For each stub file in `reports/MISSING_NOTES.md`:
1. Open the stub (contains only title + metadata)
2. Open `SYLLABUS/<course>.md` — read the lesson topics
3. Write the note following `NOTE_TEMPLATE.md`
4. Verify against `STYLE_GUIDE.md`

### 3. Review Yourself

Complete `CHECKLIST.md` thoroughly.

### 4. Fill the Report

Fill every field in `REPORT.md` — this is required for merge approval.

### 5. Return

Return the **entire package folder** to the Learning OS team by the deadline in `PACKAGE_MANIFEST.md`.

---

## Rules

| Rule | Consequence of violation |
|---|---|
| Edit ONLY `CURRICULUM/` | Unauthorized changes = rejection |
| Never rename files | Package cannot be merged |
| Never add unauthorized files | Files will be removed during merge |
| Never modify existing notes | Changes will be reverted |
| Never modify `SYLLABUS/` files | Package rejected |
| Return by deadline | Package may be reassigned |

---

## File Quality Standards

Every lesson note must have:
- H1 title (matches the stub filename topic)
- Metadata blockquote on line 3
- All 16 required sections (see `NOTE_TEMPLATE.md`)
- Code blocks with language identifiers
- Runnable code examples (not pseudocode)
- At least 3 meaningful interview questions
- At least 2 valid reference links
- No bare URLs in References

---

## Getting Help

If you encounter an unclear topic:
1. Note it in `REPORT.md` under "Issues Encountered"
2. Write your best understanding of the topic
3. Flag it with a blockquote: `> **Review needed:** [explain uncertainty]`

Do NOT leave stubs blank. Always write something, even if imperfect. The reviewer will provide feedback.

---

## What Happens After You Return

1. Your package enters automated validation
2. If validation passes → human reviewer checks quality
3. Reviewer approves or sends feedback
4. Approved content is merged into the Learning OS
5. Your contribution is archived and credited

---

## Version Information

Your `PACKAGE_MANIFEST.md` contains a `version` field. If the Learning OS syllabus changes significantly while you're working, you may receive a notification to update your package. Always return your package based on the version you received.
"""

# ════════════════════════════════════════════════════════════════════════════
FILES["REVIEWER_DOCS.md"] = f"""# Reviewer Documentation

**Learning OS Content Pipeline — Reviewer Guide**  
**Updated:** {TODAY}

---

## Your Role

Reviewers are the quality gate for the Learning OS curriculum.

Your job is to evaluate returned packages in `imports/under_review/` and decide: **APPROVE** or **REJECT**.

---

## Reviewer Responsibilities

- Technical accuracy check
- Code quality verification
- Interview question quality
- Writing clarity and style compliance
- Detection of unauthorized modifications
- Final signature before merge

---

## Review Process

### Step 1 — Pick Up a Package

```bash
# See what's waiting for review
python scripts/list_packages.py --state under_review
```

Update `PACKAGE_MANIFEST.md` → `reviewed_by: your-name`

### Step 2 — Run Audit

```bash
python scripts/audit_package.py --package imports/under_review/<package_id>
```

Read all generated reports in `reports/`.

### Step 3 — Spot-Check Content

Review at minimum 10% of new lesson files (never skip this step).

Focus on:
- First lesson of every module (sets the pattern for the module)
- Any lesson flagged in the audit report
- Random sample from the middle

### Step 4 — Score and Document

Use `templates/REVIEW_COMMENTS.md` to score and document findings.

**Scoring Rubric:**
| Criterion | Weight |
|---|---|
| Technical Accuracy | 30% |
| Code Quality | 20% |
| Interview Question Depth | 15% |
| Writing Clarity | 15% |
| Style Compliance | 10% |
| References Quality | 10% |

### Step 5 — Decide

**Score ≥ 4.0:** Approve
**Score 3.0–3.9:** Conditional approval (reviewer lists specific fixes needed first)
**Score < 3.0:** Reject with detailed comments

### Step 6 — Execute Decision

```bash
# Approve
python scripts/approve_package.py --package imports/under_review/<package_id> --reviewer "your-name" --score 4.5

# Reject
python scripts/reject_package.py --package imports/under_review/<package_id> --reviewer "your-name" --reason "Path to REVIEW_COMMENTS.md"
```

---

## What to Look For

### Technical Accuracy
- Is the information correct?
- Are API signatures accurate for the specified version?
- Are edge cases mentioned?
- Are common misconceptions corrected?

### Code Quality
- Does the code run without errors?
- Is it idiomatic (follows best practices for the language)?
- Are comments on key lines?
- Are examples minimal but complete?

### Interview Questions
- Are questions realistic (would a real interviewer ask this)?
- Are answers accurate and concise?
- Do questions cover different difficulty levels?

### What to Reject

Auto-reject if:
- More than 20% of lessons have pseudocode in code blocks
- Entire sections are missing in more than 10% of lessons
- Existing complete notes were modified
- Files were renamed
- Unauthorized files added

---

## After Review

- Approved → `python scripts/approve_package.py`
- Rejected → `python scripts/reject_package.py` + send `REJECTION_NOTICE.md` to contributor
- Merge (after approval) → `python scripts/merge_package.py`
"""

# ════════════════════════════════════════════════════════════════════════════
FILES["ADMIN_DOCS.md"] = f"""# Administrator Documentation

**Learning OS Content Pipeline — Admin Guide**  
**Updated:** {TODAY}

---

## Administrator Responsibilities

Administrators manage the full pipeline lifecycle:
- Creating and sending export packages
- Managing the contributor registry
- Overseeing merge operations
- Maintaining the package registry
- Running system-wide health checks
- Managing concurrent exports without conflicts

---

## Creating an Export

### Shared Course

```bash
python content_pipeline/scripts/export_shared.py \\
    --course javascript \\
    --assigned-to "contributor-name" \\
    --deadline 2026-08-20 \\
    --version 1.0.0
```

### Learning Path

```bash
python content_pipeline/scripts/export_learning_path.py \\
    --path frontend_engineering \\
    --assigned-to "team-name" \\
    --deadline 2026-09-01
```

### Specialization

```bash
python content_pipeline/scripts/export_specialization.py \\
    --course machine_learning \\
    --assigned-to "ml-team" \\
    --deadline 2026-09-15
```

---

## Managing the Registry

```bash
# View all active exports
python content_pipeline/scripts/list_packages.py --state exported

# View all pending review
python content_pipeline/scripts/list_packages.py --state pending_review

# View pipeline summary
python content_pipeline/scripts/list_packages.py --summary
```

---

## Running a Merge

```bash
# 1. Dry run
python content_pipeline/scripts/merge_package.py \\
    --package imports/approved/<package_id> \\
    --dry-run

# 2. Review dry run output in reports/

# 3. Execute merge
python content_pipeline/scripts/merge_package.py \\
    --package imports/approved/<package_id> \\
    --execute \\
    --admin "your-name"

# 4. Verify
python content_pipeline/scripts/verify_merge.py \\
    --package imports/approved/<package_id>

# 5. Archive
python content_pipeline/scripts/archive_package.py \\
    --package imports/approved/<package_id>
```

---

## Concurrent Export Management

Rules to prevent conflicts:
1. The same course can only have ONE active export per version at a time
2. If you need a second export of the same course, bump the version
3. The registry tracks active exports — always check before creating a new one

```bash
# Check if a course is currently exported
python content_pipeline/scripts/list_packages.py --course javascript --state exported
```

---

## Conflict Detection

If a syllabus changes after a package was exported:

```bash
python content_pipeline/scripts/check_conflicts.py --package imports/pending_review/<package_id>
```

This compares the package's `syllabus_version` against the current Learning OS syllabus and reports:
- Added lessons (new stubs missing from package)
- Removed lessons (package has lessons that no longer exist)
- Renamed modules (structural changes)

---

## System Health Check

```bash
# Full pipeline health check
python content_pipeline/scripts/pipeline_health.py
```

Generates `reports/PIPELINE_HEALTH_<date>.md` with:
- Active exports count and age
- Pending review queue
- Overdue packages
- Registry integrity
- Archive completeness

---

## Registry Maintenance

`registry/PACKAGE_REGISTRY.md` — Master registry of all packages  
`registry/ACTIVE_EXPORTS.md` — Currently active (unreturned) packages only  
`registry/ARCHIVE_INDEX.md` — Index of all archived packages  

These are auto-updated by the scripts. Manual edits should only be made with great care and must be documented.
"""

# ════════════════════════════════════════════════════════════════════════════
# REGISTRY FILES
# ════════════════════════════════════════════════════════════════════════════

FILES["registry/PACKAGE_REGISTRY.md"] = f"""# Package Registry

**Last Updated:** {TODAY}  
**Maintained by:** Content Pipeline Scripts (do not edit manually)

---

## Active Registry

| package_id | course | type | version | status | assigned_to | export_date | return_date | merge_date |
|---|---|---|---|---|---|---|---|---|
| _(empty — no packages exported yet)_ | | | | | | | | |

---

## Legend

| Status | Meaning |
|---|---|
| EXPORTED | Sent to contributor, awaiting return |
| RETURNED | Received back, pending_review |
| UNDER_REVIEW | Currently being audited/reviewed |
| APPROVED | Passed review, ready to merge |
| REJECTED | Failed review, back with contributor |
| MERGED | Merged into Learning OS |
| ARCHIVED | Merged and archived in completed/ |
"""

FILES["registry/ACTIVE_EXPORTS.md"] = f"""# Active Exports

**Last Updated:** {TODAY}  
**Auto-maintained by:** export scripts

---

This file tracks packages currently exported to contributors (status = EXPORTED).

When a package is returned, it is removed from this file.

---

| package_id | course | assigned_to | version | export_date | deadline | days_active |
|---|---|---|---|---|---|---|
| _(no active exports)_ | | | | | | |
"""

FILES["registry/ARCHIVE_INDEX.md"] = f"""# Archive Index

**Last Updated:** {TODAY}

---

Index of all archived (MERGED + ARCHIVED) packages.

| package_id | course | type | version | merge_date | archive_path | contributor |
|---|---|---|---|---|---|---|
| _(no archived packages yet)_ | | | | | | |
"""

# ════════════════════════════════════════════════════════════════════════════
# TEMPLATES
# ════════════════════════════════════════════════════════════════════════════

FILES["templates/PACKAGE_MANIFEST.md"] = f"""# Package Manifest

> Auto-generated and maintained by the content pipeline scripts.  
> Do not edit manually unless performing a manual correction.

---

```yaml
package_id:        PKG-YYYYMMDD-COURSE-NNN
course_name:       Course Name
learning_path:     Learning Path Name (or "standalone")
package_type:      shared        # shared | learning_path | specialization
version:           1.0.0
syllabus_version:  1.0.0

export_date:       YYYY-MM-DD
assigned_to:       ~
deadline:          YYYY-MM-DD

status:            CREATED       # CREATED | EXPORTED | RETURNED | UNDER_REVIEW
                                 # | APPROVED | REJECTED | MERGED | ARCHIVED

# Contributor section (filled on return)
return_date:       ~
returned_by:       ~
lessons_completed: ~
lessons_skipped:   ~

# Review section (filled during review)
review_start_date: ~
reviewed_by:       ~
review_end_date:   ~
review_score:      ~             # 1.0 to 5.0

# Decision section
decision:          ~             # APPROVED | REJECTED
decision_date:     ~
decision_notes:    ~

# Merge section
merged_by:         ~
merge_date:        ~
files_merged:      ~
merge_report:      ~

# Archive section
archive_path:      ~
archive_date:      ~
```
"""

FILES["templates/REVIEW_COMMENTS.md"] = f"""# Review Comments

**package_id:** _(fill)_  
**Reviewer:** _(fill)_  
**Review Date:** _(fill)_

---

## Overall Assessment

**Quality Score:** __ / 5.0

| Criterion | Score /5 | Notes |
|---|---|---|
| Technical Accuracy (30%) | __ | |
| Code Quality (20%) | __ | |
| Interview Question Depth (15%) | __ | |
| Writing Clarity (15%) | __ | |
| Style Compliance (10%) | __ | |
| References Quality (10%) | __ | |

**Weighted Score:** __

---

## Recommendation

- [ ] APPROVE (score ≥ 4.0)
- [ ] CONDITIONAL APPROVE (score 3.0–3.9, minor fixes needed)
- [ ] REJECT (score < 3.0 or critical issues)

---

## Issues Found

| # | File | Line | Issue Type | Description | Severity |
|---|---|---|---|---|---|
| 1 | | | | | low/medium/high |
| 2 | | | | | |

Issue Types: `technical_error`, `pseudocode`, `missing_section`, `broken_reference`, `naming_violation`, `style_violation`, `quality`

---

## Required Fixes (for Rejection)

If rejecting, list exactly what the contributor must fix:

1. **File:** `_01_01_...md` — **Issue:** [describe] — **Fix:** [describe]
2.

---

## Positive Highlights

_(Optional: note sections done exceptionally well)_

---

## Final Notes

_(Any additional context for the admin or contributor)_
"""

FILES["templates/REJECTION_NOTICE.md"] = f"""# Rejection Notice

**Date:** _(auto-filled)_  
**Package ID:** _(auto-filled)_  
**Reviewer:** _(auto-filled)_

---

Dear Contributor,

Thank you for returning your Learning OS curriculum package.

After a thorough review, we are unable to approve this package for merge at this time.

---

## Why Was This Rejected?

**Overall Quality Score:** __ / 5.0

The package did not meet the minimum quality threshold (4.0 / 5.0) due to the issues listed below.

---

## Required Corrections

Please address every issue listed before resubmitting:

| # | File | Issue | Required Fix |
|---|---|---|---|
| 1 | | | |

---

## How to Resubmit

1. Open your original package folder
2. Fix each issue listed above
3. Do NOT re-export — work in your existing package
4. Re-fill `CHECKLIST.md` and `REPORT.md`
5. Return the corrected package by: **[deadline]**

---

## What Was Done Well

_(We highlight positives to guide your corrections.)_

---

## Questions?

Contact the Learning OS team at _(contact)_.

Thank you for your contribution.

— Learning OS Review Team
"""

FILES["templates/MERGE_REQUEST.md"] = f"""# Merge Request

**Date:** _(fill)_  
**Requested by:** _(reviewer name)_  
**Approved by:** _(reviewer name)_

---

## Package Details

| Field | Value |
|---|---|
| package_id | |
| course_name | |
| version | |
| review_score | |
| files_to_merge | |

---

## Pre-Merge Checklist

- [ ] Package is in `imports/approved/`
- [ ] `PACKAGE_MANIFEST.md` status = APPROVED
- [ ] Reviewer signature present
- [ ] No active exports of same course at higher version
- [ ] Dry run completed with no conflicts
- [ ] Dry run output reviewed by admin

---

## Dry Run Summary

Run date: _(fill)_  
Report: `reports/MERGE_REPORT_<package_id>_dryrun_<date>.md`

| Action | Count |
|---|---|
| Files to CREATE | |
| Stubs to OVERWRITE | |
| Files SKIPPED (complete) | |
| Conflicts | |

---

## Merge Authorization

**Admin authorization required:**

- [ ] I have reviewed the dry run report
- [ ] I confirm no conflicts exist
- [ ] I authorize this merge

**Admin Name:** _(sign)_  
**Date:** _(fill)_

---

## Post-Merge Actions

- [ ] Verify merge with `verify_merge.py`
- [ ] Archive package with `archive_package.py`
- [ ] Update `registry/PACKAGE_REGISTRY.md`
- [ ] Notify contributor of successful merge
"""

FILES["templates/NOTE_TEMPLATE.md"] = """# [Lesson Title]

> **Course:** [Course Name] | **Module:** [Module Name] | **Difficulty:** beginner / intermediate / advanced

---

## Overview

[2–4 sentences introducing the concept.]

---

## Learning Objectives

- [Objective 1]
- [Objective 2]
- [Objective 3]

---

## Prerequisites

- [Prerequisite 1]
- [Prerequisite 2]

---

## Theory

[Core explanation.]

---

## Internal Working / How It Works

[Internal mechanism.]

---

## Architecture

[Optional for architectural topics.]

---

## Code Examples

### Example 1 — [Title]

```python
# Example code
```

---

## Hands-on Practice

1. [Task 1]
2. [Task 2]

---

## Real-world Example

[Real project context.]

---

## Best Practices

| Practice | Reason |
|---|---|
| [Practice] | [Why] |

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| [Mistake] | [Fix] |

---

## Interview Questions

**Q1:** [Question]

> [Answer]

**Q2:** [Question]

> [Answer]

**Q3:** [Question]

> [Answer]

---

## Summary

- [Key point 1]
- [Key point 2]
- [Key point 3]

---

## Cheat Sheet

| Concept | Description |
|---|---|
| `[syntax]` | [What it does] |

---

## References

- [Reference 1](https://url)
- [Reference 2](https://url)
"""

FILES["templates/STYLE_GUIDE.md"] = """# Style Guide

> Applies to all Learning OS curriculum notes.

---

## File Naming

- All lowercase with underscores
- Module + lesson prefix required: `_01_01_`, `_03_12_`
- Extension: `.md`

## Heading Hierarchy

- `#` — Lesson title (exactly one per file)
- `##` — Major template sections
- `###` — Subsections

## Code Blocks

Every code block must have a language identifier:

```python
# Python example
```

```javascript
// JavaScript example
```

Allowed: `python`, `javascript`, `sql`, `bash`, `yaml`, `json`, `html`, `css`, `jsx`, `dockerfile`, `mermaid`, `text`

## Emphasis

- **Bold** — key terms on first use
- *Italic* — titles, slight emphasis
- `Inline code` — all code identifiers, method names, attributes

## Required Sections (16)

H1 | Metadata | Overview | Learning Objectives | Prerequisites | Theory | Internal Working | Architecture* | Code Examples | Hands-on Practice | Real-world Example | Best Practices | Common Mistakes | Interview Questions | Summary | Cheat Sheet | References

(*Architecture optional for non-architectural topics)

## References

- Minimum 2 references per lesson
- Markdown links only — no bare URLs
- Format: `- [Description](https://url)`
"""

FILES["templates/CHECKLIST_template.md"] = """# Contributor Checklist

> Complete every item. Change ☐ to ☑.

---

## Pre-Writing

- ☐ Read PACKAGE_MANIFEST.md — understood assignment and deadline
- ☐ Read README.md
- ☐ Read reports/MISSING_NOTES.md — understood all stubs
- ☐ Read NOTE_TEMPLATE.md
- ☐ Read STYLE_GUIDE.md
- ☐ Read 3 existing notes for calibration

---

## Lesson Writing

- ☐ [Module 1 — all stubs complete]
- ☐ [Module 2 — all stubs complete]
- ☐ [Module 3 — all stubs complete]

---

## Quality Checks

- ☐ Every note has H1 + metadata blockquote
- ☐ All 16 required sections in every note
- ☐ All code blocks have language identifiers
- ☐ No pseudocode
- ☐ At least 3 interview questions per note
- ☐ At least 2 references per note
- ☐ No existing notes modified
- ☐ No files renamed or added outside MISSING_NOTES.md

---

## Return

- ☐ REPORT.md completely filled
- ☐ Package ready to return
"""

FILES["templates/VALIDATION_RULES.md"] = """# Validation Rules

Enforced automatically by `scripts/validate_import.py` and during human review.

---

## File Naming

- Lowercase with underscores only
- Module and lesson number prefix required
- Extension must be `.md`
- No renames of existing files
- No new files outside MISSING_NOTES.md

## Required Sections

All 16 sections in NOTE_TEMPLATE.md must be present.

## Code Blocks

- Language identifier required
- No pseudocode in examples
- Lines ≤ 100 characters

## Interview Questions

- Minimum 3 per lesson

## References

- Minimum 2 per lesson
- All must be markdown links (no bare URLs)

## Rejection Criteria

- Missing sections > 5% of lessons
- Pseudocode in code blocks > 10% of lessons
- Renamed files
- Added unauthorized files
- Modified existing complete notes
- Fewer than 3 interview questions per lesson
- References missing or bare URLs
"""

# ════════════════════════════════════════════════════════════════════════════
# REPORT TEMPLATES
# ════════════════════════════════════════════════════════════════════════════

FILES["reports/AUDIT_REPORT_template.md"] = f"""# Audit Report

**package_id:** _(fill)_  
**course:** _(fill)_  
**audit_date:** {TODAY}  
**audited_by:** automated + _(reviewer)_

---

## Automated Validation

| Check | Result | Issues |
|---|---|---|
| Package structure | PASS/FAIL | |
| Manifest completeness | PASS/FAIL | |
| Stub completion (> 500 bytes) | PASS/FAIL | N stubs remaining |
| Filename conventions | PASS/FAIL | |
| H1 in every file | PASS/FAIL | |
| Metadata blockquote | PASS/FAIL | |
| Code block identifiers | PASS/FAIL | |
| References section | PASS/FAIL | |
| Interview questions (min 3) | PASS/FAIL | |
| No renamed files | PASS/FAIL | |
| No unauthorized additions | PASS/FAIL | |
| No existing notes modified | PASS/FAIL | |

**Automated Validation:** PASS / FAIL

---

## Curriculum Health

| Metric | Value |
|---|---|
| Total lesson files | |
| Complete (> 500 bytes) | |
| Stubs remaining | |
| Average file size | |
| Smallest lesson | |
| Largest lesson | |

---

## Syllabus Coverage

| Module | Syllabus Lessons | Curriculum Files | Coverage |
|---|---|---|---|

---

## Quality Indicators

| Indicator | Value |
|---|---|
| Files with code examples | |
| Files with 3+ interview Qs | |
| Files with 2+ references | |
| Files with all 16 sections | |

---

## Issues Requiring Human Review

1. _(list any flagged issues)_

---

## Recommendation

- [ ] Proceed to human review
- [ ] Auto-reject (critical automated failures)
"""

FILES["reports/MERGE_REPORT_template.md"] = f"""# Merge Report

**package_id:** _(fill)_  
**merge_date:** {TODAY}  
**merged_by:** _(fill)_  
**mode:** DRY RUN / EXECUTED

---

## Summary

| Action | Count |
|---|---|
| Files CREATED | |
| Stubs OVERWRITTEN | |
| Files SKIPPED (complete) | |
| Files SKIPPED (conflict) | |
| Errors | |

---

## File Log

| File | Action | Source | Target | Notes |
|---|---|---|---|---|

---

## Conflicts

| File | Conflict Type | Resolution |
|---|---|---|

---

## Post-Merge Status

| Course | Before Merge | After Merge |
|---|---|---|
| Complete files | | |
| Stubs remaining | | |
| Coverage | | |

---

## Verification

- [ ] All expected files exist in docs/curriculum/
- [ ] No accidental deletions
- [ ] No corruption detected
- [ ] Archive created

**Verification signed by:** _(admin)_  
**Date:** _(fill)_
"""

print(f"  Document manifest ready: {len(FILES)} files")
print(f"  Directory manifest ready: {len(DIRS)} directories")


def build():
    print(f"\n{'='*64}")
    print(f"  Content Pipeline Builder")
    print(f"{'='*64}\n")

    # Create directories
    for d in DIRS:
        path = CP / d
        path.mkdir(parents=True, exist_ok=True)
    print(f"  [OK] {len(DIRS)} directories created")

    # Write files
    written = 0
    for rel_path, content in FILES.items():
        dest = CP / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")
        written += 1

    print(f"  [OK] {written} files written")
    print(f"\n  Pipeline scaffold complete at:\n  {CP}\n")


if __name__ == "__main__":
    build()

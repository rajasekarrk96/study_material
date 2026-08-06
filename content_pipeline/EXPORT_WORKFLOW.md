# Export Workflow

**Updated:** 2026-08-06

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

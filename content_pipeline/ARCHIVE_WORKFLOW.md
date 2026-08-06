# Archive Workflow

**Updated:** 2026-08-06

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

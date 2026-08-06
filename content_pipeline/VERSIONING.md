# Package Versioning System

**Updated:** 2026-08-06

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

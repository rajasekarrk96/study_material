# Import Workflow

**Updated:** 2026-08-06

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

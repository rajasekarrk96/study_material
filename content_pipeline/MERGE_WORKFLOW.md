# Merge Workflow

**Updated:** 2026-08-06

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

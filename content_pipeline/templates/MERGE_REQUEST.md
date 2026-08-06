# Merge Request

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

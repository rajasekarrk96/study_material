# Review Workflow

**Updated:** 2026-08-06

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

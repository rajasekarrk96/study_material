# Reviewer Documentation

**Learning OS Content Pipeline — Reviewer Guide**  
**Updated:** 2026-08-06

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

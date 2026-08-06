# Contributor Documentation

**Learning OS Content Pipeline — Contributor Guide**  
**Updated:** 2026-08-06

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

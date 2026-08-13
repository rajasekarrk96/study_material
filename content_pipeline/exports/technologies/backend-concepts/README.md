# Backend Concepts — Course Work Package

> **Version:** 1.0.0  
> **Created:** 2026-08-06  
> **Status:** Ready for Contributor  
> **Package Type:** Isolated Course Work Package

---

## Purpose

This package is a **self-contained unit of work** given to a contributor (developer,
technical writer, or AI model) to generate curriculum notes for the **Backend Concepts**
course.

The contributor **does not** need access to the main Learning OS project.

Everything required to produce notes is inside this folder.

---

## What Is Inside

| File / Folder | Purpose |
|---|---|
| `README.md` | This file — orientation and workflow |
| `COURSE_METADATA.md` | Course details, target audience, outcomes |
| `SYLLABUS.md` | The full course syllabus (authoritative) |
| `STYLE_GUIDE.md` | Markdown, naming, and formatting rules |
| `NOTE_TEMPLATE.md` | Template every lesson note must follow |
| `CHECKLIST.md` | Contributor self-review checklist |
| `VALIDATION_RULES.md` | Machine-checkable rules for notes |
| `CONTRIBUTOR_INSTRUCTIONS.md` | Step-by-step contributor guide |
| `AUDIT_TEMPLATE.md` | To be filled before returning the package |
| `MERGE_INSTRUCTIONS.md` | How the package merges into main Learning OS |
| `OUTPUT/curriculum/` | Folder hierarchy with placeholder `.md` files |

---

## Workflow

```
┌─────────────────────────────────────────────────────────┐
│                  EXPORT MANAGER                         │
│  Created this package from the main Learning OS.        │
│  No main project files were modified.                   │
└───────────────────────────┬─────────────────────────────┘
                            │  hands off package
                            ▼
┌─────────────────────────────────────────────────────────┐
│                   CONTRIBUTOR                           │
│  Reads SYLLABUS.md                                      │
│  Follows NOTE_TEMPLATE.md                               │
│  Writes notes inside OUTPUT/curriculum/                 │
│  Validates using VALIDATION_RULES.md                    │
│  Fills AUDIT_TEMPLATE.md                                │
│  Returns package                                        │
└───────────────────────────┬─────────────────────────────┘
                            │  returns completed package
                            ▼
┌─────────────────────────────────────────────────────────┐
│                   AUDIT MANAGER                         │
│  Reviews notes against VALIDATION_RULES.md              │
│  Checks AUDIT_TEMPLATE.md                               │
│  Runs merge using MERGE_INSTRUCTIONS.md                 │
└─────────────────────────────────────────────────────────┘
```

---

## How to Generate Notes

1. **Read** `COURSE_METADATA.md` — understand the course scope and audience.
2. **Read** `SYLLABUS.md` — understand the full structure (Modules → Lessons → Topics → Subtopics).
3. **Read** `NOTE_TEMPLATE.md` — understand the required sections for every lesson note.
4. **Read** `STYLE_GUIDE.md` — understand Markdown, naming, and formatting rules.
5. **Read** `CONTRIBUTOR_INSTRUCTIONS.md` — read all rules before writing.
6. **Open** `OUTPUT/curriculum/` — find the pre-created placeholder files.
7. **Write** notes into each placeholder file following the template exactly.
8. **Validate** using `VALIDATION_RULES.md`.
9. **Complete** `CHECKLIST.md` and `AUDIT_TEMPLATE.md`.
10. **Return** the entire package folder.

---

## How to Return This Package

Return the **entire** `backend-concepts-work-package/` folder with:

- All `OUTPUT/curriculum/` placeholder files filled with notes.
- `AUDIT_TEMPLATE.md` completed.
- `CHECKLIST.md` checked off.

Do **not** remove or rename any file.  
Do **not** add files outside `OUTPUT/curriculum/`.

---

## Important Constraints

> ⛔ Do NOT modify `SYLLABUS.md`.  
> ⛔ Do NOT modify `NOTE_TEMPLATE.md`.  
> ⛔ Do NOT modify `STYLE_GUIDE.md`.  
> ⛔ Do NOT modify `VALIDATION_RULES.md`.  
> ⛔ Do NOT create notes outside `OUTPUT/curriculum/`.  
> ✅ Only write inside the pre-created `.md` files in `OUTPUT/curriculum/`.

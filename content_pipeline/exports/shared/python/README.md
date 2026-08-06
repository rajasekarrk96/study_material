# Python Programming — Contributor Work Package

> **Version:** 1.0.0  
> **Created:** 2026-08-06  
> **Status:** Ready for Contributor  
> **Source Courses:** `09-python-core` + `10-advanced-python` (Learning OS)

---

## Purpose

This package is a **self-contained unit of work** for a contributor to complete missing
curriculum notes for the **Python Programming** course.

The contributor does **not** need access to the main Learning OS project.

Everything required to produce notes is inside this folder.

---

## What Is Inside

| File / Folder | Purpose |
|---|---|
| `README.md` | This file — orientation and workflow |
| `COURSE_METADATA.md` | Course details, target audience, outcomes |
| `SYLLABUS.md` | Full course syllabus (authoritative) |
| `STYLE_GUIDE.md` | Markdown, naming, and formatting rules |
| `NOTE_TEMPLATE.md` | Template every lesson note must follow |
| `CHECKLIST.md` | Contributor self-review checklist |
| `CONTRIBUTOR_GUIDE.md` | Step-by-step contributor guide |
| `MISSING_NOTES.md` | List of all stubs that need notes written |
| `CURRICULUM_HEALTH.md` | Health report for this exported package |
| `REPORT.md` | Audit and completion report |
| `curriculum/` | All existing and placeholder curriculum files |

---

## Key Rule

> ✅ **The contributor only edits files inside `curriculum/`.**  
> ⛔ All other files in this package are **read-only**.  
> ⛔ The original Learning OS project must never be modified.

---

## Workflow

```
┌────────────────────────────────────────────────────────────┐
│                    EXPORT MANAGER                          │
│  Copied existing curriculum from 09-python-core and        │
│  10-advanced-python into this isolated package.            │
│  Identified 30 stub files needing notes.                   │
└───────────────────────┬────────────────────────────────────┘
                        │  hands off package
                        ▼
┌────────────────────────────────────────────────────────────┐
│                    CONTRIBUTOR                             │
│  Reads MISSING_NOTES.md to identify stub files.            │
│  Writes notes into stub files following NOTE_TEMPLATE.md.  │
│  Does NOT modify existing real notes.                      │
│  Validates using STYLE_GUIDE.md.                           │
│  Fills CHECKLIST.md and REPORT.md.                         │
│  Returns entire package.                                   │
└───────────────────────┬────────────────────────────────────┘
                        │  returns completed package
                        ▼
┌────────────────────────────────────────────────────────────┐
│                    AUDIT MANAGER                           │
│  Reviews new notes against STYLE_GUIDE.md.                 │
│  Checks REPORT.md and CHECKLIST.md.                        │
│  Merges completed notes back into Learning OS.             │
└────────────────────────────────────────────────────────────┘
```

---

## How to Generate Notes

1. **Read** `COURSE_METADATA.md` — understand course scope and audience.
2. **Read** `SYLLABUS.md` — understand the full structure.
3. **Read** `NOTE_TEMPLATE.md` — understand required sections for every note.
4. **Read** `STYLE_GUIDE.md` — understand all formatting rules.
5. **Read** `CONTRIBUTOR_GUIDE.md` — read all rules before writing.
6. **Open** `MISSING_NOTES.md` — see exactly which files need work.
7. **Open** each stub file in `curriculum/` and write the note.
8. **Do NOT edit** files marked as `[HAS NOTES]` in `CURRICULUM_HEALTH.md`.
9. **Check off** `CHECKLIST.md` when done.
10. **Fill** `REPORT.md`.
11. **Return** the entire package.

---

## Existing vs Missing Content

| | Count |
|---|---|
| Total curriculum files | 99 |
| Files with real notes | 69 |
| Stub files (need notes) | **30** |

See `MISSING_NOTES.md` for the exact list of 30 files that need content.

---

## Return Instructions

Return the **entire** `python/` folder with:
- All 30 stub files filled with notes.
- `REPORT.md` completed.
- `CHECKLIST.md` checked off.
- No files outside `curriculum/` modified.

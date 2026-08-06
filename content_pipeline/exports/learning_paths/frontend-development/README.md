# Frontend Development — Contributor Work Package

**Version:** 1.0.0  
**Created:** 2026-08-06  
**Maintained by:** Learning OS Team

---

## Purpose

This package is a **complete, self-contained Contributor Work Package** for the Frontend Development Learning Path.

It contains everything a contributor needs to write curriculum notes for all 6 frontend courses — without touching the main Learning OS project.

---

## Courses in This Package

| # | Course | Folder | Files | Complete | Stubs |
|---|---|---|---|---|---|
| 1 | HTML5 Essentials | `CURRICULUM/html5/` | 95 | **95** | 0 |
| 2 | CSS3 Styling | `CURRICULUM/css3/` | 76 | **76** | 0 |
| 3 | Bootstrap Framework | `CURRICULUM/bootstrap/` | 31 | 28 | **3** |
| 4 | JavaScript Core | `CURRICULUM/javascript/` | 167 | **167** | 0 |
| 5 | jQuery Library | `CURRICULUM/jquery/` | 19 | 16 | **3** |
| 6 | React.js Frontend | `CURRICULUM/react/` | 60 | 30 | **30** |

**Total:** 448 files · 412 with notes · **36 stubs requiring content**

---

## Package Structure

```
frontend-development/
│
├── README.md                   ← You are here
├── COURSE_METADATA.md          ← Learning path overview
├── STYLE_GUIDE.md              ← Writing standards
├── NOTE_TEMPLATE.md            ← Lesson template
├── CONTRIBUTOR_GUIDE.md        ← Step-by-step workflow
├── CHECKLIST.md                ← Pre-return checklist
├── VALIDATION_RULES.md         ← Naming and structure rules
├── REPORT.md                   ← Return audit form
│
├── SYLLABUS/                   ← Read-only: one file per course
│   ├── html5.md
│   ├── css3.md
│   ├── bootstrap.md
│   ├── javascript.md
│   ├── jquery.md
│   └── react.md
│
├── CURRICULUM/                 ← ✏️ EDIT ONLY HERE
│   ├── html5/                  95 files (all complete)
│   ├── css3/                   76 files (all complete)
│   ├── bootstrap/              31 files (3 stubs)
│   ├── javascript/             167 files (all complete)
│   ├── jquery/                 19 files (3 stubs)
│   └── react/                  60 files (30 stubs)
│
└── reports/
    ├── CURRICULUM_HEALTH.md
    ├── MISSING_NOTES.md
    ├── DUPLICATE_NOTES.md
    └── SYLLABUS_VALIDATION.md
```

---

## Contributor Workflow

### Step 1 — Read First (required)

Read in this order:
1. `COURSE_METADATA.md` — understand the learning path scope
2. `SYLLABUS/<course>.md` — understand the lesson structure
3. `NOTE_TEMPLATE.md` — understand the required note format
4. `STYLE_GUIDE.md` — understand writing standards
5. `reports/MISSING_NOTES.md` — find exactly what needs to be written
6. `CONTRIBUTOR_GUIDE.md` — follow the workflow

### Step 2 — Write Notes

- Open each stub file listed in `reports/MISSING_NOTES.md`
- Follow `NOTE_TEMPLATE.md` exactly
- Use `STYLE_GUIDE.md` for all formatting decisions
- Do NOT rename files, add files, or delete files

### Step 3 — Self-Review

- Complete every item in `CHECKLIST.md`
- Fill in `REPORT.md`

### Step 4 — Return

Return the **entire** `frontend-development/` folder.

---

## Rules

> ⛔ Do NOT modify files in `SYLLABUS/`  
> ⛔ Do NOT modify existing notes (files > 500 bytes with content)  
> ⛔ Do NOT rename folders or files  
> ⛔ Do NOT add files outside `CURRICULUM/`  
> ✅ Write notes ONLY into stub files listed in `reports/MISSING_NOTES.md`

---

## Returning the Package

Before returning, confirm all of the following:
- [ ] All 36 stub files are complete
- [ ] `CHECKLIST.md` is fully checked
- [ ] `REPORT.md` is filled in
- [ ] No existing notes were modified
- [ ] No files were renamed or added

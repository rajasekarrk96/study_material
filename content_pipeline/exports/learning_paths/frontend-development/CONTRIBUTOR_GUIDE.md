# Contributor Guide

> Read this document completely before writing a single line.

---

## Your Assignment

You are filling in **missing lesson notes** for the **Frontend Development** Learning Path.

The package already has **412 complete notes**. You are responsible for writing the **36 stub files** listed in `reports/MISSING_NOTES.md`.

---

## What You Must NOT Do

> ⛔ Do NOT modify any note that already has content (files > 500 bytes)  
> ⛔ Do NOT rename any file  
> ⛔ Do NOT add new files  
> ⛔ Do NOT modify any file in `SYLLABUS/`  
> ⛔ Do NOT modify any package document outside `CURRICULUM/`  
> ⛔ Do NOT modify the NOTE_TEMPLATE, STYLE_GUIDE, or CHECKLIST  

---

## What You Must Do

> ✅ Write notes ONLY into the 36 stub files in `reports/MISSING_NOTES.md`  
> ✅ Follow `NOTE_TEMPLATE.md` for structure (all 17 sections)  
> ✅ Follow `STYLE_GUIDE.md` for formatting  
> ✅ Match the depth and tone of existing notes in `CURRICULUM/html5/` and `CURRICULUM/javascript/`  
> ✅ Complete `CHECKLIST.md` before returning  
> ✅ Fill `REPORT.md` before returning  

---

## Step-by-Step Workflow

### Step 1 — Read Everything (30 minutes)

In this exact order:

1. **`COURSE_METADATA.md`** — understand the 6 courses, prerequisites, outcomes
2. **`reports/MISSING_NOTES.md`** — understand exactly what needs writing
3. **`NOTE_TEMPLATE.md`** — memorize the 17-section structure
4. **`STYLE_GUIDE.md`** — understand formatting rules
5. **Read 3 existing notes** to calibrate:
   - `CURRICULUM/html5/_01_01_web_architecture_and_protocols.md`
   - `CURRICULUM/javascript/_03_27_dom_tree_navigation_and_selection.md`
   - `CURRICULUM/react/_01_01_introduction_to_modern_single_page_applications.md`

### Step 2 — Write Notes

For each stub file in `reports/MISSING_NOTES.md`:

1. Open the file — it contains only a `#` title
2. Open the relevant `SYLLABUS/<course>.md` — understand what topics the lesson covers
3. Write the note following `NOTE_TEMPLATE.md`
4. Check: does it match the style of existing notes?
5. Check: does every section exist?

### Step 3 — Self-Review

After completing all 36 stubs:

1. Check every item in `CHECKLIST.md`
2. Fix any issues
3. Fill in `REPORT.md`

### Step 4 — Return

Return the **entire** `frontend-development/` folder.

---

## Stub Breakdown by Course

| Course | Stubs | Key Topics to Cover |
|---|---|---|
| Bootstrap | 3 | Grid components, utility classes, SCSS customization |
| jQuery | 3 | DOM selection, event handling, AJAX |
| React | 30 | Hooks, routing, state, data fetching, testing, deployment |

> The React stubs are the most numerous but have paired full-content files nearby.  
> Use the paired files as context for depth. Do NOT duplicate them — write focused, standalone notes.

---

## Existing Note Structure (Reference)

Existing notes use this pattern consistently:

```
# Lesson Title

> Course | Module | Difficulty

---

## Overview
...

## Theory
...

## Code Examples
...

## Best Practices
...

## Interview Questions
...

## References
...
```

Maintain this structure. The `NOTE_TEMPLATE.md` expands on this with all 17 sections.

---

## Depth by Course

| Course | Depth Target |
|---|---|
| Bootstrap stubs | Practical — show before/after code, explain utility classes |
| jQuery stubs | Intermediate — always compare to modern Vanilla JS equivalent |
| React stubs | Intermediate/Advanced — explain the hook, show real usage, cover gotchas |

---

## Common Mistakes to Avoid

| Mistake | Why It's Wrong |
|---|---|
| Skipping the Interview Questions section | All 36 sections need this — it's required for audit |
| Writing pseudocode in examples | Examples must run without modification |
| Duplicating content from paired files | Each note must be standalone and focused |
| Changing the filename | Breaks the import pipeline |
| Adding extra files | Not auditable — will be rejected |

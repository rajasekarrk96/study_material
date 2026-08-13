# Contributor Instructions

> **Read this entire document before writing a single line of notes.**

---

## 1. Your Role

You are a **curriculum note contributor** for the **Backend Concepts** course.

Your only job is to **write lesson notes** into the placeholder files inside `OUTPUT/curriculum/`.

You are NOT:
- A syllabus designer
- A course architect
- A content reviewer

The syllabus, structure, naming, and file hierarchy are already finalized.
Your job is to fill the content.

---

## 2. What You Must NOT Do

> ⛔ **Do NOT modify `SYLLABUS.md`.**  
> The syllabus is final. Do not add, remove, or rename lessons.

> ⛔ **Do NOT modify `NOTE_TEMPLATE.md`.**  
> The template defines the required structure. Do not change it.

> ⛔ **Do NOT modify `STYLE_GUIDE.md`.**  
> Formatting rules are fixed. Do not override them.

> ⛔ **Do NOT modify `VALIDATION_RULES.md`.**

> ⛔ **Do NOT modify `CHECKLIST.md` until you are done with all notes.**

> ⛔ **Do NOT create new folders inside `OUTPUT/curriculum/`.**  
> The folder hierarchy is already created.

> ⛔ **Do NOT add extra lesson files that are not in the syllabus.**

> ⛔ **Do NOT skip lessons.** Every placeholder file must be filled.

> ⛔ **Do NOT generate quizzes, labs, or assignments.**  
> Only lesson notes.

---

## 3. What You Must Do

> ✅ **Read** every document in the package root before starting.

> ✅ **Write** notes inside each `.md` file in `OUTPUT/curriculum/`.

> ✅ **Follow** `NOTE_TEMPLATE.md` exactly for every lesson.

> ✅ **Follow** `STYLE_GUIDE.md` for every formatting decision.

> ✅ **Validate** your work against `VALIDATION_RULES.md` before returning.

> ✅ **Complete** `CHECKLIST.md` honestly before returning.

> ✅ **Fill** `AUDIT_TEMPLATE.md` with your completion report.

---

## 4. Step-by-Step Workflow

### Step 1 — Read Everything First

Before writing any notes, read:
1. `COURSE_METADATA.md`
2. `SYLLABUS.md`
3. `NOTE_TEMPLATE.md`
4. `STYLE_GUIDE.md`
5. `VALIDATION_RULES.md`
6. This document (`CONTRIBUTOR_INSTRUCTIONS.md`)

### Step 2 — Open the First Placeholder File

Navigate to:

```
OUTPUT/curriculum/01-http-protocol/01_http_fundamentals.md
```

This file currently contains a single comment line identifying the lesson.
Replace the entire contents with a completed note following `NOTE_TEMPLATE.md`.

### Step 3 — Write the Note

- Use `NOTE_TEMPLATE.md` as your structural guide.
- Use `SYLLABUS.md` to find the exact topics and subtopics for this lesson.
- Write every section. Do not skip any.
- If a section is not applicable, write `N/A` — do not delete the section heading.

### Step 4 — Move to the Next File

After completing a file:
1. Self-check against `VALIDATION_RULES.md`.
2. Move to the next placeholder file.
3. Repeat.

Work through modules in order: Module 01 → Module 02 → ... → Module 10.

### Step 5 — Final Validation

After all files are complete:
1. Run through every item in `CHECKLIST.md`.
2. Fix any issues found.
3. Fill `AUDIT_TEMPLATE.md`.
4. Return the package.

---

## 5. Content Standards

### Depth

Notes must be at **intermediate** depth. Assume the reader:
- Has written code before.
- Knows basic programming concepts.
- Does not know the specific backend concept being taught.

Do not write beginner-level filler ("A computer is a machine that...").  
Do not write expert-level deep-dives that require 5 years of experience to understand.

### Examples

- Every example must be **complete and runnable**, not pseudocode.
- Use Python (FastAPI / Flask / SQLAlchemy) as the primary reference language.
- Show realistic, production-adjacent patterns, not toy examples.

### Diagrams

- Use Mermaid for all diagrams. Do not use images unless Mermaid cannot express it.
- Every Architecture section must have at least one diagram.
- Every diagram must have a caption.

### Theory

- Be accurate. Do not invent facts.
- Cite the source in the References section if you rely on a specification.
- Prefer official documentation (MDN, RFC, official docs) over blog posts.

---

## 6. Maintain Folder Hierarchy

The `OUTPUT/curriculum/` folder hierarchy looks like this:

```
OUTPUT/curriculum/
├── 01-http-protocol/
│   ├── 01_http_fundamentals.md
│   ├── 02_http_methods.md
│   ├── 03_http_status_codes.md
│   ├── 04_request_response_structure.md
│   └── 05_urls_uris_and_query_strings.md
├── 02-routing/
│   ├── 01_what_is_routing.md
│   ├── 02_path_parameters.md
│   ├── 03_query_parameters.md
│   ├── 04_route_groups_and_prefixes.md
│   └── 05_router_internals.md
...
└── 10-infrastructure-and-production/
    ├── 01_transactional_emails.md
    ├── ...
    └── 23_devops_for_backend_engineers.md
```

**Never rename a folder or file.**  
**Never add a new folder or file.**  
**Only fill the existing `.md` files with notes.**

---

## 7. When You Are Stuck

If you are unsure how to structure content for a specific lesson:

1. Re-read the matching sub-section in `SYLLABUS.md`.
2. Check the NOTE_TEMPLATE.md section by section.
3. Look at what the learning objectives should be for that lesson.
4. Write to the target audience: an intermediate-level backend developer.

Do NOT leave a file empty or with placeholder text.
If a topic is unfamiliar, research it, then write the note.

---

## 8. Returning the Package

Return the **entire** `backend-concepts-work-package/` folder.

Before returning, confirm:
- `CHECKLIST.md` is fully checked off.
- `AUDIT_TEMPLATE.md` is filled in.
- All placeholder files are completed.
- No files outside `OUTPUT/curriculum/` have been modified.

# Merge Instructions

> **This document is for the Audit Manager / Export Manager.**  
> It describes how the completed Backend Concepts work package is merged into the main Learning OS.

---

## Prerequisites Before Merging

Before beginning the merge, verify:

- [ ] `AUDIT_TEMPLATE.md` is complete and shows ≥ 90% completion.
- [ ] `CHECKLIST.md` is fully checked off by the contributor.
- [ ] All validation categories in `AUDIT_TEMPLATE.md` show ✅ Pass.
- [ ] You have run a spot-check on at least 3 lessons from different modules.
- [ ] You have a clean git status in the main Learning OS project.

---

## Step 1 — Assign Course Number

The main Learning OS `docs/curriculum/` currently has courses `01-c-programming` through `55-database-technologies`.

Backend Concepts will receive the next available number.

**As of package creation:** next slot is `56`.

```
Course slug:   56-backend-concepts
Folder name:   56-backend-concepts
```

Verify the next available number by listing `docs/curriculum/` before merging.

---

## Step 2 — Create Course Folder in Main Project

```bash
mkdir docs/curriculum/56-backend-concepts
```

---

## Step 3 — Copy Output Curriculum

Copy the entire contents of `OUTPUT/curriculum/` from this package into the new course folder.

```bash
# From the work package root:
xcopy /E /I "OUTPUT\curriculum\*" "..\..\..\docs\curriculum\56-backend-concepts\"

# Or on Unix/Mac:
cp -r OUTPUT/curriculum/* ../../../docs/curriculum/56-backend-concepts/
```

**Result:**

```
docs/curriculum/56-backend-concepts/
├── 01-http-protocol/
│   ├── 01_http_fundamentals.md
│   ├── 02_http_methods.md
│   ├── 03_http_status_codes.md
│   ├── 04_request_response_structure.md
│   └── 05_urls_uris_and_query_strings.md
├── 02-routing/
│   └── ...
...
└── 10-infrastructure-and-production/
    └── ...
```

---

## Step 4 — Register the Syllabus

Copy `SYLLABUS.md` from the work package into the main syllabus folder.

```bash
copy "SYLLABUS.md" "..\..\..\docs\syllabus\_34_backend_concepts.md"
```

> **Note:** The syllabus file number (`_34_`) must match the next available slot in `docs/syllabus/`.
> Check the existing files to confirm the correct number before copying.

Update the front matter in the copied syllabus file to match the Learning OS syllabus format:

```markdown
# Backend Concepts — Master Syllabus

**Target Role:** Backend Engineer (Junior to Mid-Level)  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 120 Hours  
**Prerequisites:** core-python, mysql-database  
**Required Courses:** core-python  
**Optional Courses:** rest-api-design, docker-containers  
```

---

## Step 5 — Register in the Database (if applicable)

If the Learning OS uses a database to track courses, register the new course:

```sql
INSERT INTO courses (
    course_number,
    slug,
    name,
    description,
    difficulty,
    estimated_hours,
    status
) VALUES (
    56,
    'backend-concepts',
    'Backend Concepts',
    'Framework-agnostic backend engineering fundamentals covering HTTP, routing, auth, middleware, databases, caching, observability, and production readiness.',
    'intermediate',
    120,
    'active'
);
```

Adjust the SQL to match the actual schema in the main Learning OS.

---

## Step 6 — Update Learning Paths (if applicable)

If Backend Concepts should appear in a learning path, add it to the relevant learning path document in `docs/learning_paths/`.

Likely candidates:
- `01_python_full_stack.md` — add Backend Concepts between REST API Design and Flask/FastAPI
- `02_java_full_stack.md` — add Backend Concepts after Spring Boot basics

---

## Step 7 — Verify the Merge

After merging:

1. Navigate to `docs/curriculum/56-backend-concepts/` and verify all module folders are present.
2. Open 3–5 random lesson files and confirm content is present and well-formed.
3. Run the Learning OS locally and verify the course appears correctly.
4. Check that no other courses were accidentally modified.

```bash
git status
git diff --name-only
```

Only `docs/curriculum/56-backend-concepts/` and `docs/syllabus/_34_backend_concepts.md` should appear in the diff.

---

## Step 8 — Commit and Push

```bash
git add docs/curriculum/56-backend-concepts/
git add docs/syllabus/_34_backend_concepts.md
git commit -m "feat(curriculum): add Backend Concepts course (56-backend-concepts)"
git push origin main
```

---

## Step 9 — Archive the Work Package

After a successful merge:

1. Move the work package folder into `docs/archive/`:

```bash
move "exports\backend-concepts-work-package" "docs\archive\exports\backend-concepts-work-package"
```

2. The work package is now preserved as a historical record of how the course was generated.

---

## Rollback Plan

If the merge introduces issues:

```bash
git revert HEAD
```

Or manually:

```bash
git rm -r docs/curriculum/56-backend-concepts/
git rm docs/syllabus/_34_backend_concepts.md
git commit -m "revert: remove incomplete Backend Concepts course"
```

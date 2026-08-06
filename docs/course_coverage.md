# Course Coverage

**Introduced:** August 2026  
**Scope:** Every lesson in every course  
**Default:** 🟢 Covered in Class

---

## What Is Course Coverage?

Course Coverage is a metadata field on every lesson that tells students and faculty how
that lesson is delivered. It helps students plan their self-study time and lets admin
signal which topics are guaranteed classroom content versus optional extensions.

---

## Values

| Value | Emoji | DB Constant | Meaning |
|---|---|---|---|
| Covered in Class | 🟢 | `covered_in_class` | Official classroom teaching. Included in lectures and practical sessions. **Default value.** |
| Optional Discussion | 🟡 | `optional_discussion` | Notes are available. Faculty may explain during doubt-clearing sessions. Not guaranteed in every class. |
| Self Learning | 🔴 | `self_learning` | Complete notes available. Students should study independently. Useful for interview preparation and industry learning. Not part of classroom teaching. |

---

## Database

### Column

```sql
-- Table: lessons
-- Column added by: scripts/add_course_coverage.py
course_coverage VARCHAR(30) NOT NULL DEFAULT 'covered_in_class'
```

### SQLAlchemy Model

```python
# app/domains/content/models.py — Lesson class
course_coverage = db.Column(
    db.String(30),
    default=CourseCoverage.COVERED_IN_CLASS,
    nullable=False,
    server_default="covered_in_class",
)
```

### Enum Constants

```python
# app/core/constants.py
class CourseCoverage(str, Enum):
    COVERED_IN_CLASS    = "covered_in_class"
    OPTIONAL_DISCUSSION = "optional_discussion"
    SELF_LEARNING       = "self_learning"
```

### Helper Properties (on `Lesson` model)

```python
lesson.course_coverage   # raw DB value: "covered_in_class"
lesson.coverage_emoji    # "🟢" / "🟡" / "🔴"
lesson.coverage_label    # "Covered in Class" / "Optional Discussion" / "Self Learning"
```

---

## API

### GET — Read current coverage

```
GET /admin/lessons/<lesson_id>/coverage
Authorization: admin role required

Response 200:
{
    "status": "ok",
    "lesson_id": 42,
    "lesson_title": "Asyncio and Async/Await",
    "course_coverage": "covered_in_class",
    "coverage_label": "Covered in Class",
    "coverage_emoji": "🟢"
}
```

### POST — Update coverage

```
POST /admin/lessons/<lesson_id>/coverage
Authorization: admin role required
Content-Type: application/json

Body:
{ "course_coverage": "self_learning" }

Response 200:
{
    "status": "ok",
    "lesson_id": 42,
    "lesson_title": "Asyncio and Async/Await",
    "course_coverage": "self_learning",
    "coverage_label": "Self Learning",
    "coverage_emoji": "🔴"
}

Response 400 (invalid value):
{
    "status": "error",
    "message": "Invalid value 'foo'. Allowed: ['covered_in_class', 'optional_discussion', 'self_learning']"
}
```

---

## Admin Workflow

### Coverage Overview Page

Navigate to: **Admin Dashboard → Course Coverage** (green button in top navigation)

`/admin/coverage-overview`

The page shows:
1. **Summary cards** — total count per coverage type across all lessons
2. **Lesson table** — every lesson with a dropdown for live editing
3. **Filter** — show only one coverage type at a time

### Changing a Lesson's Coverage

1. Open the Coverage Overview page.
2. Find the lesson by course/module name.
3. Use the dropdown to change the value.
4. The change saves automatically (AJAX) — a ✓ Saved confirmation appears inline.

No page reload is required.

---

## Student UI

### Course Overview Page (sidebar)

Every lesson in the module sidebar shows a small emoji indicator:
- 🟢 — subtle (default)
- 🟡 — amber pill (draws attention)
- 🔴 — red pill (draws attention)

Hovering the emoji shows the full label in a tooltip.

### Lesson View Page (header)

The coverage badge appears in the lesson metadata row alongside difficulty
and estimated time:

```
[Intermediate]  [⏱ ~45 min]  [👁 120 views]  [🔴 Self Learning]
```

The badge is visually styled:
- 🟢 green pill (soft, doesn't alarm)
- 🟡 amber pill (worth noting)
- 🔴 red pill (student should plan extra time)

---

## Syllabus Markdown

All 33 syllabus files in `docs/syllabus/` have been updated to include the field
under every numbered lesson entry.

**Format:**

```markdown
1. **Lesson Title**
    - **Course Coverage:** 🟢 Covered in Class
    - Sub-topic 1
    - Sub-topic 2
```

Admin can manually update the emoji in the markdown as classification changes.

The script to re-apply or verify is:

```bash
python scripts/add_coverage_to_syllabi.py --dry-run   # preview
python scripts/add_coverage_to_syllabi.py             # apply
```

The script is **idempotent** — it will not add the field twice.

---

## Migration

To run the DB migration on a fresh install or new environment:

```bash
python scripts/add_course_coverage.py            # live run
python scripts/add_course_coverage.py --dry-run  # preview SQL
```

The script:
- Checks if the column already exists (safe to re-run)
- Adds the column with `NOT NULL DEFAULT 'covered_in_class'`
- Backfills any NULL values
- Prints verification stats

---

## Backward Compatibility

- All existing lessons default to `covered_in_class` automatically.
- Templates use `{% if lesson.course_coverage == 'covered_in_class' %}` guards — no crash on NULL.
- The DB column has a `server_default` so existing rows are covered even without running the script.
- No existing API contracts were changed — only new endpoints were added.

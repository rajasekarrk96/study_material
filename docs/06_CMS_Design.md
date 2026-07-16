# 06 — CMS Design

> The Content Management System is the editorial backbone of the Learning OS.
> It governs how content is created, reviewed, versioned, published, and retired.

---

## 6.1 CMS Architecture Overview

```
Author                Editor / Reviewer               System
  │                         │                            │
  │  Create Lesson Draft     │                            │
  │─────────────────────────>│                            │
  │                          │   Auto-save every 30s      │
  │  <─────────────────────────────────────────────────────
  │                          │                            │
  │  Submit for Review       │                            │
  │─────────────────────────>│                            │
  │                          │  Review + Comments         │
  │  <───────────────────────│                            │
  │                          │                            │
  │  Revise & Resubmit       │                            │
  │─────────────────────────>│                            │
  │                          │  Approve                   │
  │                          │─────────────────────────── │
  │                          │  Editor Publishes          │
  │                          │─────────────────────────── │
  │                          │  Search Index Updated      │
  │                          │─────────────────────────────>
  │                          │  SEO Sitemap Updated       │
  │                          │─────────────────────────────>
```

---

## 6.2 Lesson Editor Design

The lesson editor is the most critical CMS component. It is a multi-section form:

```
┌─────────────────────────────────────────────────────┐
│  LESSON EDITOR                              [SAVE DRAFT] [PREVIEW] [SUBMIT]
├─────────────────────────────────────────────────────┤
│  Title: [                                          ] │
│  Slug:  [auto-generated from title, editable]       │
│  Course: [Dropdown] Module: [Dropdown]              │
│  Difficulty: [Beginner ▼]  Estimated: [__] mins     │
├─────────────────────────────────────────────────────┤
│  SECTIONS (tabs)                                     │
│  [Overview] [Concepts] [Syntax] [Examples] [Best    │
│   Practices] [Mistakes] [Interview Q&A] [Exercises] │
│   [Quiz] [Cheatsheet] [Flashcards] [References]     │
│                                                      │
│  ┌─────────────────────────────────────────────┐    │
│  │  MARKDOWN EDITOR (EasyMDE)                  │    │
│  │  Toolbar: B I Code Block Table Image Link   │    │
│  │  ─────────────────────────────────────────  │    │
│  │  # Overview                                 │    │
│  │                                             │    │
│  │  Python is a high-level...                  │    │
│  │  ```python                                  │    │
│  │  print("Hello, World!")                     │    │
│  │  ```                                        │    │
│  └─────────────────────────────────────────────┘    │
│                                                      │
│  PREVIEW (side-by-side toggle)                       │
├─────────────────────────────────────────────────────┤
│  METADATA (collapsible)                             │
│  Meta Title: [                                    ] │
│  Meta Description: [                              ] │
│  Tags: [tag1] [tag2] [+Add]                        │
│  Sources: [+Link YouTube] [+Link Docs] [+Link Book] │
├─────────────────────────────────────────────────────┤
│  COMPLETENESS SCORE: [██████████ 70%]               │
│  Missing: Interview Q&A, Quiz, Flashcards            │
└─────────────────────────────────────────────────────┘
```

---

## 6.3 Section Types & Content Blocks

Each lesson section (`lesson_sections`) stores content in Markdown format.
The `section_type` field determines how it is rendered.

| Section Type | Render Pattern | Notes |
|-------------|----------------|-------|
| `overview` | Prose + definition box | Always visible |
| `concepts` | Key term cards + explanation | Styled cards |
| `syntax` | Code blocks with language tabs | highlight.js |
| `examples` | Numbered examples, expandable | Copy-to-clipboard |
| `diagram` | Mermaid diagram or image | Inline rendering |
| `best_practices` | Checklist / callout boxes | Green highlights |
| `common_mistakes` | Warning boxes + bad vs good | Red/green diff |
| `interview_qa` | Q visible; A hidden until auth | Auth gate |
| `exercises` | Problem statement + input/output | Submit form |
| `quiz` | Embedded quiz widget | JavaScript |
| `cheatsheet` | Dense table / code grid | Print-friendly |
| `revision_notes` | Highlighted summary bullets | Auth gated |
| `flashcards` | Flip card deck | JavaScript |
| `references` | Source cards with icons | Sorted by type |

---

## 6.4 Source Management

Every lesson can link to multiple external sources. Sources are tracked as first-class entities:

```python
# Source types
SOURCE_TYPES = [
    'youtube_video',
    'youtube_playlist',
    'official_docs',
    'book',
    'blog_article',
    'github_repo',
    'stackoverflow',
    'course_platform',   # Udemy, Coursera, etc.
    'pdf',
    'internal',          # Another lesson in this platform
]
```

Source cards render as:
```
┌─────────────────────────────────────────────┐
│  [YouTube Icon] Python Tutorial for Beginners│
│  Corey Schafer • youtube.com                 │
│  [Watch Video ↗]                            │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  [Book Icon] Python Crash Course, 3rd Ed    │
│  Eric Matthes • No Starch Press             │
│  Chapter 2: Variables and Simple Data Types │
└─────────────────────────────────────────────┘
```

---

## 6.5 Content Versioning

```python
# How versioning works
class LessonVersion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'))
    version_number = db.Column(db.Integer)       # Auto-increment per lesson
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    content_snapshot = db.Column(db.JSON)        # Full lesson state at this point
    change_summary = db.Column(db.String(500))   # Author-provided description
    status = db.Column(db.String(50))            # 'draft', 'published', 'archived'
    created_at = db.Column(db.DateTime)

# content_snapshot schema:
{
    "title": "Python Variables",
    "sections": {
        "overview": "# Overview\n\nVariables in Python...",
        "concepts": "# Concepts\n\n## Variable Declaration...",
        "examples": "# Examples\n\n```python\nx = 10\n```",
        ...
    },
    "metadata": {
        "tags": ["python", "variables", "beginner"],
        "difficulty": "beginner",
        "estimated_minutes": 15
    }
}
```

**Rollback Flow**:
1. Admin selects a version from the version history panel
2. System copies `content_snapshot` into current lesson sections
3. Creates a new version record (v5 rollback to v2 creates v6 with v2's content)
4. Logs the rollback action in audit trail

---

## 6.6 Publishing Workflow States

```python
class ContentStatus:
    DRAFT = 'draft'                  # Being written
    SUBMITTED = 'submitted'          # Author submitted for review
    IN_REVIEW = 'in_review'          # Reviewer picked it up
    CHANGES_REQUESTED = 'changes_requested'  # Reviewer asked for changes
    APPROVED = 'approved'            # Reviewer approved, pending publish
    PUBLISHED = 'published'          # Live on platform
    ARCHIVED = 'archived'            # Hidden but not deleted
    SCHEDULED = 'scheduled'          # Will publish at publish_at datetime
```

---

## 6.7 Completeness Score Algorithm

```python
def calculate_completeness(lesson: Lesson) -> int:
    score = 0
    sections = {s.section_type: s for s in lesson.sections}

    scoring_rules = [
        ('overview', 10, lambda s: len(s.content_markdown) > 200),
        ('concepts', 10, lambda s: len(s.content_markdown) > 300),
        ('syntax', 10, lambda s: '```' in s.content_markdown),
        ('examples', 15, lambda s: s.content_markdown.count('```') >= 5),
        ('best_practices', 10, lambda s: len(s.content_markdown) > 150),
        ('common_mistakes', 10, lambda s: len(s.content_markdown) > 150),
        ('interview_qa', 15, lambda s: '?' in s.content_markdown and len(s.content_markdown) > 200),
        ('exercises', 10, lambda s: len(lesson.exercises) >= 2),
        ('quiz', 10, lambda s: lesson.quiz and len(lesson.quiz.questions) >= 5),
    ]

    for section_type, points, check_fn in scoring_rules:
        if section_type in sections and check_fn(sections[section_type]):
            score += points

    lesson.completeness_score = score
    return score
```

---

## 6.8 Admin CMS Modules Summary

| Module | Path | Key Features |
|--------|------|-------------|
| Content Dashboard | /admin/ | Stats, recent drafts, pending reviews, completion report |
| Lesson Editor | /admin/content/lessons/new | Multi-section editor, preview, auto-save, completeness |
| Lesson List | /admin/content/lessons | Filter by status, course, author, score; bulk actions |
| Version History | /admin/content/lessons/:id/versions | Timeline, diff view, rollback |
| Course Manager | /admin/content/courses | CRUD, module ordering, path assignment |
| Learning Paths | /admin/paths | Path builder with drag-and-drop course ordering |
| Quiz Manager | /admin/quiz | Question bank, quiz builder, answer key |
| Exercise Manager | /admin/exercises | Problem editor, test case editor, rubric |
| Source Manager | /admin/sources | Manage YouTube links, books, docs |
| Media Library | /admin/media | Upload, tag, and link media files |
| Tag Manager | /admin/tags | Merge, rename, usage stats |
| User Manager | /admin/users | Role assignment, ban, activity |
| Analytics | /admin/analytics | Lesson views, quiz pass rates, drop-off |
| SEO Manager | /admin/seo | Bulk meta edit, sitemap, redirects |
| Job Monitor | /admin/jobs | Background task status |
| Settings | /admin/settings | Feature flags, platform config |

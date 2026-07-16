# 02 — Information Architecture

---

## 2.1 Sitemap Overview

```
Learning OS (Root)
│
├── / (Home)
│   ├── Hero Section
│   ├── Featured Learning Paths
│   ├── Recent Additions
│   ├── Category Browser
│   └── Stats (lessons, students, courses)
│
├── /catalog/ (Content Catalog)
│   ├── /catalog/categories/
│   ├── /catalog/courses/
│   ├── /catalog/paths/         (Learning Paths)
│   └── /catalog/search/
│
├── /learn/ (Learning Experience)
│   ├── /learn/<course-slug>/
│   │   ├── /learn/<course-slug>/overview/
│   │   └── /learn/<course-slug>/<module-slug>/
│   │       └── /learn/<course-slug>/<module-slug>/<lesson-slug>/
│   │           ├── #concepts
│   │           ├── #syntax
│   │           ├── #examples
│   │           ├── #best-practices
│   │           ├── #mistakes
│   │           ├── #interview-qa
│   │           ├── #exercises
│   │           ├── #quiz
│   │           ├── #cheatsheet
│   │           └── #references
│
├── /dashboard/ (Student Dashboard) [AUTH REQUIRED]
│   ├── /dashboard/overview/
│   ├── /dashboard/progress/
│   ├── /dashboard/achievements/
│   ├── /dashboard/bookmarks/
│   ├── /dashboard/notes/
│   ├── /dashboard/flashcards/
│   ├── /dashboard/revision-schedule/
│   └── /dashboard/analytics/
│
├── /quiz/ [PARTIAL AUTH]
│   ├── /quiz/<quiz-slug>/          (Take quiz)
│   └── /quiz/<quiz-slug>/results/  (Results — AUTH)
│
├── /exercises/ [PARTIAL AUTH]
│   ├── /exercises/<exercise-slug>/   (View problem — public)
│   └── /exercises/<exercise-slug>/submit/ (Submit — AUTH)
│
├── /paths/ (Learning Paths)
│   ├── /paths/<path-slug>/
│   └── /paths/<path-slug>/enroll/  (AUTH)
│
├── /profile/ [AUTH]
│   ├── /profile/settings/
│   ├── /profile/achievements/
│   └── /profile/stats/
│
├── /admin/ [RBAC GATED]
│   ├── /admin/dashboard/
│   ├── /admin/content/
│   │   ├── /admin/content/courses/
│   │   ├── /admin/content/modules/
│   │   ├── /admin/content/lessons/
│   │   ├── /admin/content/lessons/new/
│   │   ├── /admin/content/lessons/<id>/edit/
│   │   └── /admin/content/lessons/<id>/versions/
│   ├── /admin/quiz/
│   ├── /admin/exercises/
│   ├── /admin/users/
│   ├── /admin/roles/
│   ├── /admin/sources/
│   ├── /admin/media/
│   ├── /admin/tags/
│   ├── /admin/paths/
│   ├── /admin/analytics/
│   ├── /admin/seo/
│   ├── /admin/jobs/
│   └── /admin/settings/
│
├── /api/v1/ (REST API)
│   └── [See 15_REST_API_Specification.md]
│
├── /auth/
│   ├── /auth/login/
│   ├── /auth/register/
│   ├── /auth/logout/
│   ├── /auth/forgot-password/
│   └── /auth/reset-password/
│
└── /pages/ (Static-like pages via CMS)
    ├── /pages/about/
    ├── /pages/contact/
    └── /pages/privacy/
```

---

## 2.2 Content Taxonomy

### Hierarchy Levels

```
Category (Technical / Non-Technical)
  └── Subject (Python, Java, MySQL...)
        └── Course (Core Python, Advanced Python...)
              └── Module (Variables & Data Types, Control Flow...)
                    └── Lesson (Variables, Integer, Float, Boolean...)
                          └── Sections (Concepts, Syntax, Examples...)
```

**Examples**:
```
Technical > Python > Core Python > Variables & Data Types > Variables
Technical > Java > Core Java > OOP > Inheritance
Technical > MySQL > MySQL Fundamentals > DDL > CREATE TABLE
Non-Technical > Soft Skills > Communication > Presentations > Storytelling
```

---

## 2.3 Content Types

| Type | Description | Auth Required |
|------|-------------|--------------|
| `lesson` | Full topic page with all sections | View: Public |
| `lesson_section` | Sub-section of a lesson | View: Public |
| `quiz` | MCQ/TF auto-graded assessment | Questions: Public, Answers: Auth |
| `exercise` | Coding/written practice problem | Problem: Public, Submit: Auth |
| `assignment` | Multi-part take-home problems | Problem: Public, Submit: Auth |
| `project` | Real-world mini-project | Spec: Public, Submit: Auth |
| `flashcard` | Q&A pair for spaced repetition | Auth |
| `cheatsheet` | Quick reference PDF/page | Public |
| `interview_qa` | Interview question + answer | Q: Public, A: Auth |
| `revision_note` | Dense lesson summary | Auth |
| `learning_path` | Ordered sequence of courses | Browse: Public, Enroll: Auth |

---

## 2.4 Tag Taxonomy

Every lesson is tagged with multiple taxonomy dimensions:

```
Tags Schema:
  - topic_tags: ["variables", "data-types", "integers"]
  - difficulty: ["beginner", "intermediate", "advanced"]
  - language: ["python", "java", "javascript"]
  - domain: ["backend", "frontend", "data-science", "devops"]
  - source_type: ["official-docs", "youtube", "book", "blog"]
  - content_type: ["concept", "tutorial", "reference", "exercise"]
  - career_relevance: ["interview", "production", "academic"]
```

---

## 2.5 URL Structure Design

URLs are designed for SEO, readability, and permanence:

```
Pattern: /{category-slug}/{course-slug}/{module-slug}/{lesson-slug}/

Examples:
  /python/core-python/basics/variables/
  /java/core-java/oop/inheritance/
  /mysql/fundamentals/ddl/create-table/
  /devops/docker/containers/dockerfile/

API Pattern: /api/v1/{resource}/{id}/
  /api/v1/lessons/142/
  /api/v1/courses/python-core/
  /api/v1/quiz/variables-quiz/attempt/
```

**Slug Rules**:
- Lowercase, hyphen-separated
- Max 60 characters
- Immutable after publishing (301 redirect if changed)
- Unique within scope (course slug unique globally, lesson slug unique within module)

---

## 2.6 Navigation Structure

### Primary Navigation (Public)
```
[Logo] [Catalog] [Learning Paths] [Search...] [Login] [Register]
```

### Student Navigation (Authenticated)
```
[Logo] [Catalog] [My Learning] [Bookmarks] [Notes] [Dashboard] [Profile]
```

### Author Navigation
```
[Logo] [My Courses] [Editor] [My Drafts] [Analytics] [Profile]
```

### Admin Navigation
```
[Logo] [Content] [Users] [Analytics] [SEO] [Settings] [System]
```

---

## 2.7 Search Architecture Overview

Global search covers:
- Lessons (title, summary, body text)
- Courses (title, description)
- Tags
- Authors
- Interview Questions
- Cheatsheets

Filters:
- Category / Subject / Course
- Difficulty Level
- Content Type
- Language / Technology
- Date Added

(Full detail in 12_Search_Architecture.md)

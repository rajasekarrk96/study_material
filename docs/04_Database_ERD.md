# 04 — Database ERD (Entity Relationship Diagram)

> **Total Tables**: 48  
> **ORM**: SQLAlchemy 2.0  
> **Migrations**: Alembic  
> **Databases**: SQLite (dev) / TiDB / PostgreSQL (prod)

---

## 4.1 Domain Groups

```
GROUP 1: Identity & Auth
  users, roles, permissions, role_permissions, user_sessions, password_reset_tokens

GROUP 2: Content CMS
  categories, subjects, courses, modules, lessons, lesson_sections,
  lesson_versions, content_blocks, tags, lesson_tags, lesson_sources

GROUP 3: Learning Paths
  learning_paths, path_courses, path_prerequisites, user_path_enrollments

GROUP 4: Assessments
  quizzes, quiz_questions, quiz_options, quiz_attempts, quiz_answers,
  exercises, exercise_submissions, assignments, assignment_submissions,
  projects, project_submissions

GROUP 5: Flashcards & Revision
  flashcard_decks, flashcards, user_flashcard_progress, revision_schedules

GROUP 6: Progress & Gamification
  user_progress, user_lesson_progress, user_xp_log, streaks,
  badges, badge_criteria, user_badges, achievements, user_achievements

GROUP 7: Social / Engagement
  bookmarks, user_notes, lesson_ratings, lesson_comments

GROUP 8: Sources & Media
  sources, media_files, lesson_media

GROUP 9: Analytics & Search
  search_index, content_analytics, user_analytics, ai_usage_log

GROUP 10: System
  background_jobs, feature_flags, settings, notifications
```

---

## 4.2 Complete ERD (Mermaid)

```mermaid
erDiagram
    %% =====================
    %% GROUP 1: IDENTITY
    %% =====================

    users {
        int id PK
        string email UK
        string username UK
        string display_name
        string password_hash
        int role_id FK
        bool is_active
        bool is_verified
        string avatar_url
        text bio
        datetime created_at
        datetime last_login_at
        string timezone
        string preferred_language
    }

    roles {
        int id PK
        string name UK
        string display_name
        text description
        int level
        datetime created_at
    }

    permissions {
        int id PK
        string code UK
        string description
        string category
    }

    role_permissions {
        int role_id PK FK
        int permission_id PK FK
        datetime granted_at
        int granted_by FK
    }

    user_sessions {
        int id PK
        int user_id FK
        string session_token UK
        string ip_address
        string user_agent
        datetime created_at
        datetime expires_at
        bool is_active
    }

    password_reset_tokens {
        int id PK
        int user_id FK
        string token UK
        datetime expires_at
        bool used
    }

    %% =====================
    %% GROUP 2: CONTENT CMS
    %% =====================

    categories {
        int id PK
        string name UK
        string slug UK
        string type
        text description
        string icon
        string color
        int sort_order
        bool is_active
        datetime created_at
    }

    subjects {
        int id PK
        int category_id FK
        string name
        string slug UK
        text description
        string icon
        string logo_url
        string difficulty_level
        int sort_order
        bool is_active
        datetime created_at
    }

    courses {
        int id PK
        int subject_id FK
        int created_by FK
        string title
        string slug UK
        text description
        text long_description
        string thumbnail_url
        string difficulty_level
        string status
        string language
        int estimated_hours
        bool is_free
        bool is_featured
        json meta_title
        json meta_description
        json meta_keywords
        int view_count
        int enrollment_count
        datetime published_at
        datetime created_at
        datetime updated_at
    }

    modules {
        int id PK
        int course_id FK
        string title
        string slug
        text description
        int sort_order
        bool is_published
        datetime created_at
    }

    lessons {
        int id PK
        int module_id FK
        int created_by FK
        string title
        string slug
        text summary
        string status
        string content_type
        int sort_order
        int estimated_minutes
        string difficulty_level
        bool has_concepts
        bool has_syntax
        bool has_examples
        bool has_exercises
        bool has_quiz
        bool has_cheatsheet
        bool has_flashcards
        int completeness_score
        string meta_title
        string meta_description
        string canonical_url
        int view_count
        datetime published_at
        datetime created_at
        datetime updated_at
    }

    lesson_sections {
        int id PK
        int lesson_id FK
        string section_type
        string title
        text content_markdown
        text content_html
        int sort_order
        bool is_visible
        datetime created_at
        datetime updated_at
    }

    lesson_versions {
        int id PK
        int lesson_id FK
        int version_number
        int created_by FK
        json content_snapshot
        string change_summary
        string status
        datetime created_at
    }

    tags {
        int id PK
        string name UK
        string slug UK
        string category
        int usage_count
        datetime created_at
    }

    lesson_tags {
        int lesson_id PK FK
        int tag_id PK FK
        datetime added_at
    }

    sources {
        int id PK
        string source_type
        string title
        string url
        string author_name
        string platform
        text description
        string thumbnail_url
        datetime published_date
        datetime created_at
    }

    lesson_sources {
        int id PK
        int lesson_id FK
        int source_id FK
        string relation_type
        int sort_order
    }

    %% =====================
    %% GROUP 3: LEARNING PATHS
    %% =====================

    learning_paths {
        int id PK
        int created_by FK
        string title
        string slug UK
        text description
        string thumbnail_url
        string difficulty_level
        string status
        int estimated_hours
        int sort_order
        bool is_featured
        datetime published_at
        datetime created_at
    }

    path_courses {
        int path_id PK FK
        int course_id PK FK
        int sort_order
        bool is_required
    }

    path_prerequisites {
        int path_id PK FK
        int prerequisite_path_id PK FK
    }

    user_path_enrollments {
        int id PK
        int user_id FK
        int path_id FK
        string status
        float completion_percent
        datetime enrolled_at
        datetime completed_at
    }

    %% =====================
    %% GROUP 4: ASSESSMENTS
    %% =====================

    quizzes {
        int id PK
        int lesson_id FK
        int created_by FK
        string title
        text description
        string quiz_type
        int time_limit_minutes
        int passing_score
        int max_attempts
        bool shuffle_questions
        bool show_answers_after
        bool is_published
        datetime created_at
    }

    quiz_questions {
        int id PK
        int quiz_id FK
        string question_text
        string question_type
        int points
        int sort_order
        string difficulty
        text explanation
        datetime created_at
    }

    quiz_options {
        int id PK
        int question_id FK
        string option_text
        bool is_correct
        string explanation
        int sort_order
    }

    quiz_attempts {
        int id PK
        int user_id FK
        int quiz_id FK
        int score
        int total_points
        float percentage
        bool passed
        int time_taken_seconds
        int attempt_number
        datetime started_at
        datetime completed_at
    }

    quiz_answers {
        int id PK
        int attempt_id FK
        int question_id FK
        int selected_option_id FK
        text text_answer
        bool is_correct
        int points_earned
    }

    exercises {
        int id PK
        int lesson_id FK
        int created_by FK
        string title
        text problem_statement
        text input_format
        text output_format
        text constraints
        text sample_input
        text sample_output
        text hints
        string difficulty
        string exercise_type
        int points
        bool is_published
        datetime created_at
    }

    exercise_submissions {
        int id PK
        int user_id FK
        int exercise_id FK
        text solution_text
        string language
        string status
        int points_earned
        text feedback
        int attempt_number
        datetime submitted_at
    }

    %% =====================
    %% GROUP 5: FLASHCARDS
    %% =====================

    flashcard_decks {
        int id PK
        int lesson_id FK
        string title
        text description
        bool is_published
        datetime created_at
    }

    flashcards {
        int id PK
        int deck_id FK
        text question
        text answer
        text hint
        int sort_order
        string difficulty
        datetime created_at
    }

    user_flashcard_progress {
        int id PK
        int user_id FK
        int flashcard_id FK
        int confidence_level
        int review_count
        datetime next_review_at
        datetime last_reviewed_at
    }

    %% =====================
    %% GROUP 6: PROGRESS & GAMIFICATION
    %% =====================

    user_progress {
        int id PK
        int user_id FK
        int total_xp
        int level
        int lessons_completed
        int quizzes_passed
        int exercises_solved
        int current_streak_days
        int longest_streak_days
        datetime last_activity_at
        datetime updated_at
    }

    user_lesson_progress {
        int id PK
        int user_id FK
        int lesson_id FK
        string status
        float completion_percent
        int time_spent_seconds
        int xp_earned
        datetime started_at
        datetime completed_at
        datetime last_accessed_at
    }

    user_xp_log {
        int id PK
        int user_id FK
        int xp_amount
        string action_type
        string description
        int reference_id
        string reference_type
        datetime earned_at
    }

    streaks {
        int id PK
        int user_id FK
        int current_streak
        int longest_streak
        date last_activity_date
        datetime updated_at
    }

    badges {
        int id PK
        string name UK
        string description
        string icon_url
        string badge_type
        string tier
        int xp_reward
        datetime created_at
    }

    badge_criteria {
        int id PK
        int badge_id FK
        string criteria_type
        string criteria_key
        int criteria_value
        string operator
    }

    user_badges {
        int id PK
        int user_id FK
        int badge_id FK
        datetime earned_at
        int reference_id
        string reference_type
    }

    %% =====================
    %% GROUP 7: ENGAGEMENT
    %% =====================

    bookmarks {
        int id PK
        int user_id FK
        int lesson_id FK
        string note
        datetime created_at
    }

    user_notes {
        int id PK
        int user_id FK
        int lesson_id FK
        int section_id FK
        text note_content
        bool is_private
        datetime created_at
        datetime updated_at
    }

    lesson_ratings {
        int id PK
        int user_id FK
        int lesson_id FK
        int rating
        text review
        datetime created_at
    }

    %% =====================
    %% RELATIONSHIPS
    %% =====================

    users ||--o{ user_sessions : "has"
    users ||--o{ password_reset_tokens : "has"
    roles ||--o{ users : "assigned to"
    roles ||--o{ role_permissions : "has"
    permissions ||--o{ role_permissions : "in"

    categories ||--o{ subjects : "contains"
    subjects ||--o{ courses : "contains"
    courses ||--o{ modules : "contains"
    modules ||--o{ lessons : "contains"
    lessons ||--o{ lesson_sections : "has"
    lessons ||--o{ lesson_versions : "versioned by"
    lessons ||--o{ lesson_tags : "tagged with"
    lessons ||--o{ lesson_sources : "sourced from"
    tags ||--o{ lesson_tags : "used in"
    sources ||--o{ lesson_sources : "referenced by"

    learning_paths ||--o{ path_courses : "includes"
    learning_paths ||--o{ path_prerequisites : "requires"
    learning_paths ||--o{ user_path_enrollments : "enrolled in"
    courses ||--o{ path_courses : "part of"
    users ||--o{ user_path_enrollments : "enrolls"

    lessons ||--o{ quizzes : "has"
    quizzes ||--o{ quiz_questions : "contains"
    quiz_questions ||--o{ quiz_options : "has"
    users ||--o{ quiz_attempts : "takes"
    quizzes ||--o{ quiz_attempts : "attempted in"
    quiz_attempts ||--o{ quiz_answers : "records"

    lessons ||--o{ exercises : "has"
    users ||--o{ exercise_submissions : "submits"
    exercises ||--o{ exercise_submissions : "has"

    lessons ||--o{ flashcard_decks : "has"
    flashcard_decks ||--o{ flashcards : "contains"
    users ||--o{ user_flashcard_progress : "tracks"
    flashcards ||--o{ user_flashcard_progress : "tracked in"

    users ||--|| user_progress : "has"
    users ||--o{ user_lesson_progress : "tracks"
    users ||--o{ user_xp_log : "earns"
    users ||--|| streaks : "has"
    users ||--o{ user_badges : "earns"
    badges ||--o{ user_badges : "awarded to"
    badges ||--o{ badge_criteria : "defined by"

    users ||--o{ bookmarks : "saves"
    lessons ||--o{ bookmarks : "bookmarked in"
    users ||--o{ user_notes : "writes"
    lessons ||--o{ user_notes : "annotated in"
    users ||--o{ lesson_ratings : "rates"
    lessons ||--o{ lesson_ratings : "rated by"
```

---

## 4.3 Key Design Decisions

### Content Versioning Strategy
```sql
-- Every save creates a new version record
-- lesson_versions.content_snapshot stores the full lesson JSON snapshot
-- lesson.current_version_id points to the active published version
-- Rollback = update lesson.current_version_id to a previous version
```

### Soft Delete Pattern
All content tables use `is_deleted` + `deleted_at` + `deleted_by` instead of hard DELETE.
This enables:
- Audit trails
- Recovery
- Analytics on deleted content

### Slug Immutability
Once a lesson is published, its slug is frozen.
If changed, the old slug creates a 301 redirect entry in `url_redirects` table.

### XP System Design
```
Action                    XP Earned
Complete a lesson          +10 XP
Pass a quiz (>70%)         +25 XP
Solve an exercise          +15-50 XP (by difficulty)
Daily streak day           +5 XP
7-day streak bonus         +50 XP
First lesson in course     +20 XP
Complete a course          +200 XP
Complete a learning path   +500 XP
Rate a lesson              +2 XP
Write a note               +1 XP
```

### Completeness Score
Each lesson has a `completeness_score` (0-100) calculated from:
- Has overview: +10
- Has concepts: +10
- Has syntax: +10
- Has examples (5+): +15
- Has best practices: +10
- Has common mistakes: +10
- Has interview Q&A: +15
- Has exercises (2+): +10
- Has quiz (5+ questions): +10
Score drives content quality dashboards in admin.

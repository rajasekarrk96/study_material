# STATUS: FROZEN
**Effective Date**: 2026-08-06
**Version**: v2.3

---

# DATABASE SCHEMA SPECIFICATION v2.3

## 1. Platform / Delivery Layer

### `users`
- `id` (int, PK)
- `email` (varchar, unique)
- `username` (varchar, unique)
- `password_hash` (varchar)
- `is_active` (bool)
- `is_verified` (bool)
- `created_at` (datetime)
- `updated_at` (datetime)

### `roles`
- `id` (int, PK)
- `name` (varchar, unique)
- `display_name` (varchar)
- `level` (int)

### `user_role_mappings`
- `id` (int, PK)
- `user_id` (int, FK to `users.id`)
- `role_id` (int, FK to `roles.id`)

### `permission_matrix`
- `id` (int, PK)
- `role_id` (int, FK to `roles.id`)
- `permission_code` (varchar)
- `is_granted` (bool)

### `user_courses` (Enrollments)
- `id` (int, PK)
- `user_id` (int, FK to `users.id`)
- `course_id` (int, FK to `courses.id`)
- `status` (varchar)
- `expiry` (datetime)
- `purchase_type` (varchar)
- `progress` (int)

## 2. Knowledge Layer

### `media`
- `id` (int, PK)
- `filename` (varchar)
- `url` (varchar)
- `file_type` (varchar)
- `file_size` (int)
- `folder_id` (int, FK to `media_folders.id`)
- `created_by_id` (int, FK to `users.id`)

### `media_folders`
- `id` (int, PK)
- `name` (varchar)

### `media_tags`
- `media_id` (int, FK to `media.id`)
- `tag_id` (int, FK to `tags.id`)

### `media_references`
- `id` (int, PK)
- `media_id` (int, FK to `media.id`)
- `target_type` (varchar)
- `target_id` (int)

### `search_documents`
- `id` (int, PK)
- `target_type` (varchar)
- `target_id` (int)
- `content` (text)

### `search_chunks`
- `id` (int, PK)
- `document_id` (int, FK to `search_documents.id`)
- `chunk_index` (int)
- `text_chunk` (text)

### `search_keywords`
- `id` (int, PK)
- `chunk_id` (int, FK to `search_chunks.id`)
- `keyword` (varchar)

### `tags`
- `id` (int, PK)
- `name` (varchar, unique)
- `slug` (varchar, unique)

## 3. Curriculum Layer

### `course_categories`
- `id` (int, PK)
- `name` (varchar)
- `slug` (varchar)
- `status` (varchar)

### `courses`
- `id` (int, PK)
- `category_id` (int, FK to `course_categories.id`)
- `title` (varchar)
- `slug` (varchar, unique)
- `difficulty` (varchar)
- `estimated_minutes` (int)

### `modules`
- `id` (int, PK)
- `course_id` (int, FK to `courses.id`)
- `title` (varchar)
- `slug` (varchar)
- `sort_order` (int)

### `lessons`
- `id` (int, PK)
- `module_id` (int, FK to `modules.id`)
- `title` (varchar)
- `slug` (varchar)
- `content_status` (varchar)
- `difficulty` (varchar)
- `estimated_minutes` (int)

### `lesson_sections`
- `id` (int, PK)
- `lesson_id` (int, FK to `lessons.id`)
- `section_type` (varchar)
- `title` (varchar)
- `content_markdown` (text)
- `sort_order` (int)
- `content_status` (varchar)

### `topic_coverage`
- `id` (int, PK)
- `lesson_section_id` (int, FK to `lesson_sections.id`)
- `coverage_status` (varchar)
- `display_label` (varchar)
- `updated_by_id` (int, FK to `users.id`)

### `topic_coverage_history`
- `id` (int, PK)
- `topic_coverage_id` (int, FK to `topic_coverage.id`)
- `old_coverage_status` (varchar)
- `new_coverage_status` (varchar)
- `updated_by_id` (int, FK to `users.id`)

### `course_prerequisites`
- `course_id` (int, FK to `courses.id`)
- `prerequisite_course_id` (int, FK to `courses.id`)

### `lesson_prerequisites`
- `lesson_id` (int, FK to `lessons.id`)
- `prerequisite_lesson_id` (int, FK to `lessons.id`)

### `roadmap_nodes`
- `id` (int, PK)
- `title` (varchar)
- `node_type` (varchar)
- `course_id` (int, FK to `courses.id`)

### `roadmap_edges`
- `id` (int, PK)
- `source_node_id` (int, FK to `roadmap_nodes.id`)
- `target_node_id` (int, FK to `roadmap_nodes.id`)

### `path_courses`
- `id` (int, PK)
- `path_id` (int, FK to `learning_paths.id`)
- `course_id` (int, FK to `courses.id`)
- `sequence` (int)
- `is_required` (bool)
- `recommended_hours` (int)
- `optional` (bool)
- `unlock_after` (int)

## 4. Editorial Layer

### `draft_lesson_sections`
- `id` (int, PK)
- `lesson_id` (int, FK to `lessons.id`)
- `section_type` (varchar)
- `title` (varchar)
- `content_markdown` (text)
- `sort_order` (int)
- `last_saved_by_id` (int, FK to `users.id`)
- `updated_at` (datetime)

### `content_proposals`
- `id` (int, PK)
- `proposal_type` (varchar)
- `target_type` (varchar)
- `target_id` (int)
- `draft_lesson_id` (int)
- `author_id` (int, FK to `users.id`)
- `description` (text)
- `status` (varchar)
- `grammar_checked` (bool)
- `code_executed` (bool)
- `images_added` (bool)
- `quiz_updated` (bool)
- `references_added` (bool)
- `seo_checked` (bool)
- `accessibility_checked` (bool)

### `content_proposal_sections`
- `id` (int, PK)
- `proposal_id` (int, FK to `content_proposals.id`)
- `lesson_section_id` (int, FK to `lesson_sections.id`)
- `title` (varchar)
- `new_content` (text)

### `ai_proposal_reviews`
- `id` (int, PK)
- `proposal_id` (int, FK to `content_proposals.id`)
- `status` (varchar)
- `feedback_json` (text)
- `ai_generated` (bool)
- `generated_by` (varchar)
- `model_version` (varchar)

### `content_versions`
- `id` (int, PK)
- `target_type` (varchar)
- `target_id` (int)
- `version_number` (int)
- `merged_by_id` (int, FK to `users.id`)
- `snapshot_json` (text)
- `created_at` (datetime)

### `curriculum_releases`
- `id` (int, PK)
- `version_name` (varchar)
- `semesterly_tag` (varchar)
- `snapshot_json` (text)
- `is_active_for_new_enrollments` (bool)
- `created_at` (datetime)

### `approvals`
- `id` (int, PK)
- `proposal_id` (int, FK to `content_proposals.id`)
- `user_id` (int, FK to `users.id`)
- `status` (varchar)
- `comments` (text)

### `review_comments`
- `id` (int, PK)
- `proposal_id` (int, FK to `content_proposals.id`)
- `user_id` (int, FK to `users.id`)
- `comment` (text)

### `activity_logs`
- `id` (int, PK)
- `user_id` (int, FK to `users.id`)
- `action` (varchar)
- `target_type` (varchar)
- `target_id` (int)
- `details` (text)
- `created_at` (datetime)

### `notification_queue`
- `id` (int, PK)
- `user_id` (int, FK to `users.id`)
- `category` (varchar)
- `title` (varchar)
- `message` (text)
- `is_read` (bool)
- `created_at` (datetime)

# Task 03 — Learning Paths & Spaced Repetition (SRS)

> **Goal**: Model curriculum sequencing, build the Spaced Repetition Scheduler matching SuperMemo-2 (SM-2) guidelines, and design user notes annotation layers.

---

## 3.1 Learning Paths Builder & Prerequisites Check
- [ ] Database Schema:
  - Add tables for `LearningPath`, `PathCourse`, and `PathPrerequisite`.
- [ ] Prerequisites Middleware Hooks:
  - Create checks verifying that students have met prerequisite rules (e.g. course completion flags) before accessing locked lessons.
- [ ] Path Listing UI:
  - Build course pathway panels showing checklists and completion status percentages.

---

## 3.2 Spaced Repetition Engine (SM-2 Algorithm)
- [ ] Database Schema:
  - Add tables: `flashcard_decks`, `flashcards`, `user_flashcard_progress`, and `revision_schedules`.
- [ ] SM-2 Algorithm Service:
  - Implement calculations adjusting intervals ($I$) and Ease Factors ($EF$) depending on flashcard session grades (1 to 5 confidence score scales).
  - Code update hooks matching reviews schedules.
- [ ] Flashcards Frontend Panel:
  - Design HTML layouts featuring flip-cards animations and rating options.

---

## 3.3 Study Annotation Layers (Bookmarks & Notes)
- [ ] Personal annotations controllers:
  - Add tables for `bookmarks` and `user_notes` (allowing students to save tags, custom markdown texts, and private notes references inside lessons).
- [ ] Integration endpoints:
  - Code API endpoints to handle bookmarking toggles (`POST /api/v1/bookmarks`) and notebook editing commands.

---

## 🛑 CHECKPOINT & BREAK POINT
- Verify path sequencing checks blocks student requests if they access a course without clearing prerequisites.
- Verify flashcard session triggers correctly reschedule review times based on confidence scores.
- **Action**: Pause and request approval before moving to AI local engines and vector search setups.

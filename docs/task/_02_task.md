# Task 02 — Assessment & Gamification Engine

> **Goal**: Deploy the interactive quiz schemas, integrate the code evaluation sandboxes (Judge0), and build the user leveling, streaks, and XP logging service.

---

## 2.1 Quiz Engine Infrastructure
- [x] Database Schema:
  - Add models for `Quiz`, `Question`, `Option`, `QuizAttempt`, and `QuizAnswer`.
- [x] API Controllers:
  - Code endpoint `/api/v1/quizzes/<id>/attempts` (creates attempt sessions).
  - Code endpoint `/api/v1/quizzes/attempts/<id>/submit` (processes answers, validates time limits, computes scores).
- [x] User Interfaces:
  - Design front-end quiz widget displaying option inputs, timers, and score reports.

---

## 2.2 Sandboxed Code Execution Engine (Exercise Sandbox)
- [x] Database Schema:
  - Add models for `Exercise`, `ExerciseTestCase`, and `ExerciseSubmission`.
- [x] External Sandbox Integration (Judge0 API):
  - Code API request client sending source code, input values, and expected outputs.
  - Implement language mapping (e.g. mapping `python` files to Judge0 ID 71).
- [x] Submissions Portal:
  - Code `/api/v1/exercises/<id>/submit` to process code outputs.
  - Build UI layout containing coding editor (using CodeMirror / Ace Editor integration), input test inputs boxes, and compiler stdout logs view.

---

## 2.3 Progress, XP, and Streaks Logging Service
- [x] XP Allocator Services:
  - Code transaction service calculating and writing XP to the `user_xp_log` table.
  - Apply logic capping max daily XP points (e.g. max 500 XP per user per day).
- [x] Levels Progression Curve:
  - Code levels utility mapping XP totals to level thresholds ($L = \lfloor 0.1 \times \sqrt{XP} \rfloor + 1$).
- [x] Streak Tracking Service:
  - Code background checking algorithm verifying active daily lessons completions.
  - Increment `current_streak` or reset to 1 if user skips consecutive days.

---

## 🛑 CHECKPOINT & BREAK POINT
- run tests: `run_tests.py` ensuring quiz answer evaluations pass correct score checks.
- Test coding execution output by submitting a basic Python print code and checking the sandbox output returns `Accepted` / `PASSED`.
- **Action**: Pause and request approval before implementing Spaced Repetition (SRS) modules.

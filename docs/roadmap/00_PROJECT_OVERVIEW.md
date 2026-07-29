# 00 — Project Overview & Architecture Status

> **Learning OS** — Enterprise Technical Curriculum & Multi-Agent AI Learning System  
> **Last Updated**: `2026-07-29`  
> **Current Version**: `v4.0.0`

---

## 🎯 Project Vision

Learning OS is an enterprise-grade, multi-agent AI learning operating system designed to deliver structured, reusable, and zero-duplication technical education. Micro-courses exist only once in the master catalog and are dynamically sequenced into role-based Learning Paths.

---

## 📊 High-Level Metrics

| Metric | Current Count | Status / Target |
|--------|--------------:|-----------------|
| **Overall Completion %** | **83.8%** | 🟢 2,021 / 2,411 Published Lessons |
| **Learning Paths** | **8 Active** | 🟢 100% Curated & Sequenced |
| **Total Master Courses** | **74 Unique** | 🟢 0% Duplication |
| **Published Courses** | **46 Courses** | 🟢 Fully Populated with Section Markdown |
| **Structure-Ready Courses** | **21 Courses** | 🟡 Modules & Lessons Seeded |
| **Placeholder Stub Courses** | **7 Courses** | 🔴 Needs Module/Lesson Seed |
| **Total Lessons in Catalog** | **2,411 Lessons** | 🟢 2,021 Ready & Published |
| **Published Lessons** | **2,021 Lessons** | 🟢 Published to DB & UI |

---

## ⚙️ Architecture & Technology Stack

- **Backend**: Python 3.11 / Flask / SQLAlchemy ORM / SQLite
- **AI Pipeline**: Local Ollama (`qwen3:14b`) + Agentic Generation Engine
- **Data Model**: `Category` ➔ `Subject` ➔ `Course` ➔ `Module` ➔ `Lesson` ➔ `LessonSection`
- **Learning Path Model**: `LearningPath` ⟷ `PathCourse` (JOIN table with `section_label` & `is_required`)

---

## 🏃 Current Sprint Status

- **Current Sprint**: Sprint 4 — *IoT Full Stack Path Completion & Roadmap Standard*
- **Sprint Goal**: 100% publication of all 23 IoT Full Stack courses and establishment of `docs/roadmap/` tracking suite.
- **Next Sprint**: Sprint 5 — *Python Full Stack & DevOps Foundation Batch Generation*

---

## ⚠️ Known Issues & Mitigations

1. **PowerShell Pipe Encoding**: Windows console defaults to CP1252.  
   *Mitigation*: Enforce `PYTHONIOENCODING=utf-8` and `-u` unbuffered flags on scripts.
2. **Local LLM Timeout**: High-param Ollama models time out on long responses.  
   *Mitigation*: Use Agentic Direct Generation pipeline (`generate_<course>_content_direct.py`).

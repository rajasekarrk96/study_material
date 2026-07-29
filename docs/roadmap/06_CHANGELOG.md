# 06 — Project Changelog

> Master record of system architecture updates, migrations, and content releases.

---

## [v4.0.0] - 2026-07-29

### 🟢 Added
- Created official `docs/roadmap/` suite (`00` through `07`).
- Completed 100% publication of **IoT Full Stack Engineer Path** (23/23 courses).
- Created direct generator pipelines for `electrical-fundamentals`, `electronics-basics`, `stm32`, `firebase`, `tinyml`, and `raspberry-pi`.
- Rebuilt 8 master Learning Paths in DB with `section_label` and `is_required` attributes.
- Seeded structure for 25 new courses (~96 modules, ~490 lessons, ~4900 section placeholders).

### 🟡 Changed
- Upgraded Local AI Provider to `qwen3:14b` with internal streaming for unbuffered execution.
- Fixed Windows PowerShell `PYTHONIOENCODING=utf-8` console output bugs.

### 🟢 Fixed
- Resolved `qa-automation-engineer` duplicate path in database.

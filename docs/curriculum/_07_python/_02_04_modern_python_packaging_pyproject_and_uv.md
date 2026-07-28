```yaml
schema_version: "2.0"
metadata:
  lesson_id: "PY-MOD05-LES03"
  course_slug: "course-02-python"
  course_title: "Course 2: Python 3.12+ Modern Programming"
  module_slug: "mod-05-modern-python-concurrency"
  module_title: "Module 5 - Async Concurrency & Type Hinting"
  lesson_slug: "modern-python-packaging-pyproject-and-uv"
  lesson_title: "Lesson 5.3 Modern Python Packaging (pyproject.toml & uv)"
  sort_order: 503

pedagogy:
  difficulty: "intermediate"
  estimated_time:
    reading_minutes: 15
    practice_minutes: 20
    quiz_minutes: 10
    total_minutes: 45
  bloom_taxonomy_level: "Apply"
  xp_reward: 50

prerequisites:
  required_lesson_ids:
    - "PY-MOD05-LES01"
  required_skills:
    - "Python Package Management & Terminal Usage"

skills_acquired:
  - "PEP 621 Standard Package Manifest (`pyproject.toml`)"
  - "Ultra-Fast Package Management using `uv`"
  - "Virtual Environments Creation (`uv venv`)"
  - "Dependency Lockfiles & Reproducible Builds"

dependencies:
  software:
    - "VS Code"
    - "Python 3.11+ with `uv`"
  hardware: []

seo_and_social:
  meta_title: "Modern Python Packaging: pyproject.toml Standard & High-Speed uv Tooling"
  meta_description: "Master modern Python packaging: PEP 621 pyproject.toml manifests, ultra-fast dependency management with uv, virtual environments, and lockfiles."
  keywords: ["pyproject.toml", "uv package manager", "Python packaging", "PEP 621", "virtual environment", "pip alternative"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 5.3 Modern Python Packaging (`pyproject.toml` & `uv`)

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: Python Package Management
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Write standardized project metadata in **`pyproject.toml`** (PEP 621).
2. Utilize **`uv`**, the ultra-fast Rust-based Python package manager (10–100x faster than `pip`).
3. Manage virtual environments and lockfiles (`uv lock`) for reproducible production builds.

---

## 2. Environment & Prerequisites [id: prerequisites]

Install `uv`:
- Run `pip install uv` or `curl -LsSf https://astral.sh/uv/install.sh | sh`.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 Legacy `setup.py` vs Modern `pyproject.toml`
Legacy Python setups relied on executing arbitrary `setup.py` code during installation. **PEP 518 / PEP 621** unified all Python tooling configuration (build backends, dependencies, linter settings) into a single declarative file: **`pyproject.toml`**.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          MODERN PYTHON TOOLING (`uv`)                       │
├─────────────────┬───────────────────────────────────────────────────────────┤
│ Feature         │ Capability                                                │
├─────────────────┼───────────────────────────────────────────────────────────┤
│ Speed           │ Written in Rust; installs packages 10–100x faster than pip│
│ Management      │ Handles Python version management, venvs, and lockfiles   │
│ Compatibility   │ Drop-in replacement for `pip`, `pip-tools`, and `virtualenv`│
└─────────────────┴───────────────────────────────────────────────────────────┘
```

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    Config["pyproject.toml Manifest"] --> UV[uv Package Manager]
    UV --> Lock[Generates uv.lock Deterministic Lockfile]
    Lock --> Venv[Populates .venv Virtual Environment in Milliseconds]
```

---

## 5. Code & Hardware Implementation [id: syntax]

### Modern `pyproject.toml` Manifest Specification

```toml
[project]
name = "enterprise-ai-service"
version = "0.1.0"
description = "High-performance AI telemetry microservice"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.110.0",
    "pydantic>=2.6.0",
    "httpx>=0.27.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.mypy]
python_version = "3.12"
strict = true
```

### High-Speed `uv` CLI Commands

```bash
# 1. Create Virtual Environment
uv venv

# 2. Activate Virtual Environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install Dependencies at Lightning Speed
uv pip install -r pyproject.toml
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Production Docker Builds**: Enterprise CI/CD pipelines use `uv` inside Docker containers to drop image build times from 5 minutes down to 10 seconds.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Create a folder and initialize `uv`: `uv init`.
2. Run `uv add fastapi pydantic` $\to$ Inspect auto-generated `pyproject.toml` and lightning-fast installation!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`setup.py` Deprecation Warnings** | Building packages using legacy `setup.py` scripts. | Migrate project metadata into standard `pyproject.toml`. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Adopt `pyproject.toml`**: Use it for all modern Python project configurations.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: What is `pyproject.toml` and why is it preferred over `requirements.txt`?
**Answer**: `pyproject.toml` is the PEP 621 standardized declarative configuration file for Python projects. Unlike `requirements.txt` which only lists dependencies, `pyproject.toml` unifies project metadata, build system requirements (Hatch, Flit, Poetry), dependencies, and tool settings (Mypy, Ruff, Black) in one file.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 5.3 Modern Packaging Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which standard specifies project metadata inside pyproject.toml?",
      "options": ["PEP 8", "PEP 621", "PEP 484", "PEP 257"],
      "correct_answer_index": 1,
      "explanation": "PEP 621 defines project metadata fields in pyproject.toml."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Migrate a legacy `requirements.txt` project to `pyproject.toml` managed via `uv`.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What Rust-based package manager replaces `pip` with 100x faster speeds?
**Back**: `uv` (developed by Astral).
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```bash
uv pip install -r pyproject.toml
```


---

## Existing Jupyter Notebooks

> **Note**: Comprehensive Jupyter notebooks exist for this topic in the Python study folder.
> Reference the notebooks when authoring full lesson content.
> Notebooks follow the pattern: `_NN_00_topic.ipynb` (notes), `_NN_01_topic_Questions.ipynb`, `_NN_02_topic_Answers.ipynb`

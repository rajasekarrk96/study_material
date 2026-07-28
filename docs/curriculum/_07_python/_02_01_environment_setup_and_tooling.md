---
id: "02_01_02"
title: "Environment Setup and Tooling"
course: "Python"
module: 1
module_title: "Setup and Overview"
lesson: 2
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["installation", "venv", "virtualenv", "pip", "pyproject.toml", "uv", "conda", "VS-Code", "pycharm", "REPL"]
prerequisites: []
lab_required: true
---

# Environment Setup and Tooling


## Installing Python

```bash
# Windows — via official installer or winget
winget install Python.Python.3.12

# macOS
brew install python@3.12

# Ubuntu/Debian
sudo apt install python3.12 python3.12-venv python3.12-dev
```

## Virtual Environments

Always isolate project dependencies in a virtual environment.

```bash
# Create
python -m venv .venv

# Activate
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate          # Windows PowerShell

# Deactivate
deactivate
```

## Package Management with pip

```bash
pip install requests flask       # install packages
pip install -r requirements.txt  # install from file
pip freeze > requirements.txt    # export current env
pip list --outdated              # check updates
pip uninstall requests           # remove package
pip show flask                   # package details
```

## Modern Tooling — uv (recommended 2024+)

```bash
# Install uv
pip install uv

# Create project
uv init myproject
cd myproject

# Add dependencies
uv add fastapi sqlalchemy

# Run script
uv run main.py

# Sync environment from pyproject.toml
uv sync
```

## pyproject.toml

```toml
[project]
name = "myapp"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["fastapi>=0.110", "sqlalchemy>=2.0"]

[project.optional-dependencies]
dev = ["pytest", "ruff", "mypy"]
```

## Code Quality Tools

| Tool | Purpose | Command |
|---|---|---|
| **ruff** | Linter + formatter (fast) | `ruff check .` / `ruff format .` |
| **black** | Formatter | `black .` |
| **mypy** | Type checker | `mypy src/` |
| **pytest** | Testing | `pytest tests/` |
| **pre-commit** | Git hooks | `pre-commit run --all-files` |

## REPL and Interactive Tools

```bash
python          # Standard REPL
ipython         # Enhanced REPL with magic commands
jupyter lab     # Browser-based notebooks
ptpython        # Pretty REPL with syntax highlighting
```

## Lab Exercise
1. Create a new project folder, set up `.venv`, activate it
2. Install `requests` and `rich`; freeze to `requirements.txt`
3. Configure VS Code with the Python extension and select the venv interpreter

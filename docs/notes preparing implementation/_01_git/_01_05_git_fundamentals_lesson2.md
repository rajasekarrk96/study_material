# Lesson 3: Basic Local Workflow — Tracking and Recording Changes

---

```yaml
lesson_id: "GIT-FND-002"
subject: "Git"
course: "Git Fundamentals"
module: "Basic Local Workflow"
difficulty: "⭐"
time_breakdown:
  reading: "15 min"
  exercise: "20 min"
  quiz: "10 min"
  revision: "5 min"
version: "1.1"
last_updated: "2026-07-17"
status: "Published"
author: "Rajasekar"
reviewed_by: "Admin"
prerequisites:
  - "GIT-FND-001a (Version Control History)"
tags:
  - "Git Init"
  - "Git Config"
  - "Git Status"
  - "Git Clone"
```

---

## 1. Topics Covered [id: topics]
- Git Configurations (`--global`, `--system`, `--local`)
- Initializing a repository vs Cloning a remote repository
- Git status short output representation (`-s`)
- Tracking rules and ignoring files (`.gitignore` rules)
- Committing staged changes to the log history

## 2. Definitions & Core Concepts [id: definitions]
- **Git Config levels**:
  - `--system`: Configurations applied system-wide to all users and all repositories on the machine (stored in `/etc/gitconfig`).
  - `--global`: Configurations applied to the current user's profile across all their repositories (stored in `~/.gitconfig`).
  - `--local`: Configurations limited only to the current repository directory (stored in `.git/.git/config`).
- **`git init`**: Initializes a brand-new local Git repository in the current folder, creating a hidden `.git` folder structure.
- **`git clone <url>`**: Downloads and copies an entire existing remote repository (history, commits, branches) into a new local directory.
- **`.gitignore`**: A plain text configuration file where you declare file path patterns (temporary files, cache, secrets) that Git must completely ignore from tracking.

## 3. Practical Code Examples [id: examples]

### Example A: Setting Up Global Git Identity config
- **Code**:
  ```bash
  git config --global user.name "Rajasekar"
  git config --global user.email "rajasekar@bbsolutions.com"
  git config --list
  ```
- **Input (i/p)**: Run config commands to bind your identity.
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git config --list                                    │
  │ user.name=Rajasekar                                    │
  │ user.email=rajasekar@bbsolutions.com                   │
  └────────────────────────────────────────────────────────┘
  ```

### Example B: Cloning a Repository and Checking Short Status
- **Code**:
  ```bash
  git clone https://github.com/rajasekarrk96/study_material.git
  cd study_material
  echo "# Temp notes" > notes.tmp
  echo "import sys" >> main.py
  git status -s
  ```
- **Input (i/p)**: Create an untracked file (`notes.tmp`) and edit a tracked file (`main.py`).
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git status -s                                        │
  │  M main.py                                             │
  │ ?? notes.tmp                                           │
  └────────────────────────────────────────────────────────┘
  ```
  *(Note: `M` in the second column means modified in working directory; `??` means untracked file)*

### Example C: Configuring a `.gitignore` block to exclude files
- **Code**:
  ```bash
  echo "*.tmp" > .gitignore
  echo "SECRET_KEY=abc" > secrets.env
  echo "secrets.env" >> .gitignore
  git status -s
  ```
- **Input (i/p)**: Stage ignoring rules for `notes.tmp` and `secrets.env`.
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git status -s                                        │
  │ ?? .gitignore                                          │
  └────────────────────────────────────────────────────────┘
  ```
  *(Notice that `notes.tmp` and `secrets.env` do not appear in the status output because they match ignoring rules)*

## 4. Hands-on Workouts [id: workouts]
- **Workout 1**: Set your repository-specific local identity user name to "BB Solutions Developer" inside a test Git repository and inspect `.git/config` to verify.
- **Workout 2**: Write a `.gitignore` pattern that ignores all files inside a folder named `build/` and ignores any files with extension `.log`.

## 5. Workout Answers & Solutions [id: answers]

### Solution to Workout 1:
- **Code & Commands**:
  ```bash
  mkdir test-repo
  cd test-repo
  git init
  git config --local user.name "BB Solutions Developer"
  cat .git/config
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ cat .git/config                                      │
  │ [core]                                                 │
  │         repositoryformatversion = 0                    │
  │         filemode = true                                │
  │ [user]                                                 │
  │         name = BB Solutions Developer                  │
  └────────────────────────────────────────────────────────┘
  ```

### Solution to Workout 2:
- **Code for `.gitignore`**:
  ```text
  # Ignore build directory
  build/

  # Ignore all log files
  *.log
  ```

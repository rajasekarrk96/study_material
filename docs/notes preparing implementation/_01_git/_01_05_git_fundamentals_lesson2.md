# Lesson 2: Basic Local Workflow — Tracking and Recording Changes

---

```yaml
lesson_id: GIT-FND-002
subject: Git
course: Git Fundamentals
module: Basic Local Workflow
difficulty: "\u2B50"
time_breakdown:
  reading: 15 min
  exercise: 20 min
  quiz: 10 min
  revision: 5 min
version: '1.0'
last_updated: '2026-07-17'
status: Published
author: Rajasekar
reviewed_by: Admin
prerequisites:
- GIT-FND-001 (Git Architecture)
tags:
- Git Init
- Git Add
- Git Commit
- Git Status
```

---

## 1. Topics Covered [id: topics]
This lesson covers the primary local version control workflow. You will learn how to initialize a repository, track files, inspect modification status, and write structured commit records to the database log.

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - The life cycle of a file in a Git-controlled directory (untracked, unmodified, modified, staged).
  - How Git represents directories and content files internally using indices and objects.
- **Skills (What you can do)**:
  - Construct local repositories, selectively track files, and commit changes with high-quality descriptions.
- **Outcome (Professional application)**:
  - Maintain a clean and traceable project history through semantic local staging configurations.

## 2. Definitions & Core Concepts [id: definitions]
Inside a directory initialized with Git, files follow a strict lifecycle:
- **Untracked**: The file exists on disk, but Git has no record of it and does not monitor it for changes.
- **Unmodified**: The file is tracked, and its contents match the last committed version.
- **Modified**: A tracked file has been changed in the Working Directory, but these changes are not yet staged.
- **Staged**: The changes in the file are cached in the index file and ready to be committed.

### Internal database mechanics of `git commit`
When you run `git commit`, Git does not save delta differences. Instead:
1. It reads the current binary `.git/index` file to find the SHA-1 hashes of all staged blobs.
2. It constructs a **Tree** object representing the project's root folder directory.
3. It creates a **Commit** object pointing to the root Tree object, identifying the author, committer, timestamp, and the SHA-1 of parent commits.
4. It moves the active branch head pointer (e.g. `refs/heads/main`) to point to this new commit object hash.

### Terminology & Glossary
- **Untracked file**: Any file in your working directory that was not in your last snapshot and is not in your staging area.
- **Modified file**: A file that has changed since it was last committed but has not yet been staged.
- **Index**: Git's binary cache tracking the snapshot state of files slated for the next commit.

## 3. Practical Code Examples [id: examples]
### Easy
Create a new directory and initialize it as a repository:
```bash
mkdir my-app
cd my-app
git init
```

### Medium
Selective addition of multiple files:
```bash
echo "import os" > main.py
echo "SECRET_KEY=123" > secrets.env

# Add only Python files, ignore secrets
git add *.py
git status
```

### Advanced
Creating a commit message containing metadata using multi-line formats:
```bash
git commit -m "feat(auth): add email login controller" -m "Resolves issue #42. Sets up standard auth session handling."
```

## 4. Hands-on Workouts [id: workouts]
### MCQ
- Which state represents a file that has changes prepared for the next commit?
  - A) Untracked
  - B) Modified
  - C) Staged (Correct)

### Coding Challenge
- Initialize a local git repository, write a file named `hello.py` containing `print('hello')`, stage it, and commit it with message "Add greeting".

### Predict the Output
- If you run `git add file.txt` and then run `git status -s`, what code symbol prints next to the filename?
  - Output: `A  file.txt`

### Debugging Task
- A developer runs `git commit` and it opens Vim. How do they save and exit the editor?
  - Answer: Press `Esc`, type `:wq`, and press `Enter`.

### Scenario Question
- A student wants to ignore all `.log` files in their project. What configuration file must they create and what text should it contain?
  - Answer: Create `.gitignore` containing `*.log`.

### Hands-on Lab
- Run `git init`, create `index.html`, run `git status`, add it, and commit.

## 5. Workout Answers & Solutions [id: answers]
- **Standard Syntax**: `git commit -m "<msg>"`
- **Aliases**: `git config --global alias.st status`
- **Shortcut**: Press `Ctrl+Enter` in VS Code source control menu to commit staged changes.
- **Warning**: Do not use `git add .` indiscriminately without review, as you may accidentally stage security keys.

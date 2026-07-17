# Git Architecture and the Three States

---

```yaml
lesson_id: GIT-FND-001
lesson_title: "Git Architecture & Three States"
subject: Git
course: Git Fundamentals
module: Git Architecture
difficulty: "\u2B50"
time_breakdown:
  reading: 12 min
  exercise: 15 min
  quiz: 10 min
  revision: 5 min
version: '1.1'
last_updated: '2026-07-16'
status: Published
author: Learning OS Author
reviewed_by: Admin
prerequisites:
- Basic CLI navigation
tags:
- Git
- Staging
- Commit
- HEAD
```

---

## 1. Topics Covered [id: topics]
This lesson introduces the core version control model of Git. Rather than just memorizing commands, we explore how Git manages files across three distinct environments: the Working Directory, the Staging Area, and the Local Repository.

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - The mechanical boundaries of the Working Directory, Staging Area, and Local Repository.
  - How Git handles internal indexing via checksum hash trees.
- **Skills (What you can do)**:
  - Initialize repositories, selectively stage files, and create structured local snapshots.
- **Outcome (Professional application)**:
  - Organize commits atomically to preserve clean project histories on enterprise codebases.

## 2. Definitions & Core Concepts [id: definitions]
Imagine Git as a shipping warehouse:
1. **Working Directory (Your Desk)**: This is where you write code, delete lines, and create files. Like your desk, it is messy, and items here are subject to change. Git does not track changes here automatically.
2. **Staging Area (The Loading Dock)**: Before shipping, you pack specific items into a shipping box and place them on the loading dock. In Git, the staging area (index) is a binary cached file that registers exactly what changes are slated for the next commit.
3. **Local Repository (The Shipping Container)**: Once the shipping box is complete, you seal it and load it onto the container. In Git, a commit is a permanent snapshot sealed into the history of the local repository (inside the `.git/objects` directory).

### Internal Architecture
Unlike other VCS (like SVN) that track changes as delta lists, Git tracks changes as **snapshots of the directory structure**.
Every file you add to Git is compressed and stored as a **Blob** (Binary Large Object) containing the file contents, indexed by a unique SHA-1 hash.
The **Index** is a binary file stored at `.git/index` that maps file paths to their corresponding SHA-1 blob hashes. When you commit, Git writes a **Tree** object that acts as a directory listing, mapping file names to blobs, and points the **Commit** object to this tree, along with metadata (author, message, parent commit).

### Terminology & Glossary
- **Blob**: Git's internal format representing a file's contents, stripped of metadata.
- **Tree**: Git's internal folder representation, linking filenames to their respective blobs.
- **HEAD**: A reference pointer pointing to the current active branch or commit.
- **Staging Index**: The binary file `.git/index` tracking the snapshot state of files.

## 3. Practical Code Examples [id: examples]
### Easy
Initialize a local repository and commit a file:
```bash
# Initialize repo
git init

# Write file
echo "initial code" > app.py

# Stage and Commit
git add app.py
git commit -m "Initialize app.py with core script"
```

### Medium
Selective staging of files:
```bash
# Modify app.py and add temp log file
echo "print('Hello')" >> app.py
echo "TEMP" > build.log

# Check modified files
git status

# Stage only app.py
git add app.py

# Commit only app.py (build.log remains unstaged)
git commit -m "Add print execution to app.py"
```

### Advanced
Verify Git index database structure:
```bash
# Inspect the raw staging area index entries
git ls-files --stage
```

## 4. Hands-on Workouts [id: workouts]
### MCQ
- Which file holds Git's binary staging area index?
  - A) `.git/config`
  - B) `.git/index` (Correct)
  - C) `.git/HEAD`

### Coding Challenge
- Initialize a git repository and commit `script.py` with the message "Init".

### Predict the Output
- If `status.py` is untracked, what does `git status -s` print next to its name?
  - Output: `?? status.py`

### Debugging Task
- Run `git commit -m "add config"` on a fresh directory. Fix the resulting `nothing to commit` error.

### Scenario Question
- A developer modified `auth.py` and `test.log`. They only want `auth.py` in the commit. What commands should they run?
  - Answer: `git add auth.py` then `git commit -m "update authentication"`.

### Hands-on Lab
- Open terminal, create a directory, run `git init`, write `data.json`, and run `git add data.json`.

## 5. Workout Answers & Solutions [id: answers]
- **Standard Syntax**: `git add <file>`
- **Aliases**: `git config --global alias.co checkout`
- **Shortcut**: Use `Ctrl+Shift+G` in VS Code to open the source control stage interface.
- **Warning**: Never run `git reset --hard` unless you are sure you want to discard all working directory modifications.

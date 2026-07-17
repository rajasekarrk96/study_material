# Inspecting History: Log & Diff

---

```yaml
lesson_id: GIT-FND-003
lesson_title: "Inspecting History: Log & Diff"
subject: Git
course: "Git Fundamentals"
module: "History Management"
difficulty: "⭐"
time_breakdown:
  reading: 15 min
  exercise: 20 min
  quiz: 10 min
  revision: 5 min
version: '1.2'
last_updated: '2026-07-17'
status: Published
author: Rajasekar
reviewed_by: Admin
prerequisites:
- GIT-FND-002 (Local Workflow: Init, Stage & Commit)
tags:
- Git Log
- Git Diff
- Inspect Changes
- Git Show
```

---

## 1. Topics Covered [id: topics]
- Viewing commit history
- Formatting commit logs
- Comparing changes using git diff
- Comparing staged vs unstaged changes
- Searching repository history

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - How Git represents changes between commits using raw diff formats.
  - The differences between working tree diffs, staged diffs, and commit comparisons.
- **Skills (What you can do)**:
  - Walk, filter, and inspect commit history timelines using custom log constraints.
  - Interrogate file edits using line-by-line comparison markers.
- **Professional Outcome**:
  - Debug regressions and trace author ownership lines across collaborative codebase repos.

---

## 2. Definitions & Core Concepts [id: definitions]

### Visual History Diagram
When you run `git log`, Git does not scan a chronological server folder. It starts at the commit pointed to by **HEAD** and walks backward through parent commit pointer references:
```text
           Commit History Traversal
           
                 HEAD (Current Branch)
                  │
                  ▼
               [Commit D]  (Latest Snapshot)
                  │
                  ▼
               [Commit C]
                  │
                  ▼
               [Commit B]
                  │
                  ▼
               [Commit A]  (Root Snapshot)
```

### git diff State Comparisons
`git diff` calculates the line-by-line comparison of file changes between different states in the Git lifecycle:
```text
                    git diff State Comparisons

        Working Directory (Files you are editing)
                │
                │ git diff
                ▼
         Staging Area (Files selected for commit)
                │
                │ git diff --staged (or --cached)
                ▼
         Last Commit (HEAD in Local Repository)
```

### git log Cheat Sheet
| Command | Purpose |
|---|---|
| **`git log`** | Full repository history list. |
| **`git log --oneline`** | Compact commit history with single-line snapshots. |
| **`git log --graph`** | Compact commit history with a branch graph representation. |
| **`git log --stat`** | Lists commit files changed and lines added/deleted. |
| **`git log -p`** | Displays commit history along with the raw diff patch. |
| **`git log --author="name"`** | Filter history commits by a specific author name. |
| **`git log --since="7 days ago"`** | Limit the commits to those made within a relative timeframe. |

### git diff Comparison Chart
| Command | Comparison Scope |
|---|---|
| **`git diff`** | Working Directory $\leftrightarrow$ Staging Area (index). |
| **`git diff --staged`** | Staging Area $\leftrightarrow$ Last Commit (HEAD). |
| **`git diff HEAD`** | Working Directory $\leftrightarrow$ Last Commit (HEAD). |
| **`git diff commit1 commit2`** | Compares two specific commit hashes. |
| **`git diff branch1 branch2`** | Compares two distinct branch pointers. |

### Understanding Diff Output Markers
When reading a diff output, Git uses specific symbols to show line-by-line modifications:
| Symbol | Meaning |
|---|---|
| **`+`** | Added line (green in most terminal configurations). |
| **`-`** | Deleted line (red in most terminal configurations). |
| **`@@`** | Hunk header showing line range coordinates inside the files. |
| **`diff --git`** | Standard metadata header indicating the start of a file comparison. |

### git show
The `git show` command displays commit metadata (author, date, message) and the complete line-by-line diff changes introduced by a single commit:
- `git show HEAD`: Inspects the details of the most recent commit.
- `git show HEAD~1`: Inspects the second-to-last commit.
- `git show <commit_hash>`: Inspects a specific commit by hash.

### Commit Hash Mechanics
Historically, Git used 40-character SHA-1 commit hashes for object identification. Modern Git versions also support SHA-256 repositories, although SHA-1 remains the most common format.

---

## 3. Practical Code Examples [id: examples]

### Example A: Basic log filtering
- **Code**:
  ```bash
  # View commits made by Developer in the last week
  git log --author="Developer" --since="7 days ago" --oneline
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git log --author="Developer" --oneline               │
  │ a1b2c3d feat: add authentication dashboard             │
  │ e5f6g7h fix: resolve token timeout issue               │
  └────────────────────────────────────────────────────────┘
  ```

### Example B: Snoop searching with `git log -S`
- **Code**:
  ```bash
  # Search commits that added or removed a specific string
  git log -S "db_password" --oneline
  ```
  *(Note: This queries commits where occurrences of the targeted string changed, which is useful for audit logs)*

### Example C: Practical Investigation Workflow
- **Code**:
  ```bash
  # 1. Check workspace status
  git status
  
  # 2. View unstaged changes
  git diff
  
  # 3. Stage changes
  git add app.py
  
  # 4. View staged changes
  git diff --staged
  
  # 5. Commit & inspect commit details
  git commit -m "fix: validate login forms"
  git show HEAD
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git show HEAD --oneline                              │
  │ c2b3a4d fix: validate login forms                      │
  │ diff --git a/app.py b/app.py                           │
  │ + if not email or not password:                         │
  └────────────────────────────────────────────────────────┘
  ```

---

## 4. Hands-on Workouts [id: workouts]

### MCQ
- Which command compares staged changes with the last commit?
  - A) `git diff`
  - B) `git diff --staged` (Correct)
  - C) `git diff HEAD`

### Coding Challenge
- Run a command to list all commits that modified a file named `database.json`.
  - Answer: `git log -- database.json`

### Scenario Question: Who updated the file lines?
- A team discovers an issue in `auth.py`. 
  - To view the commit logs affecting this file, run: `git log -- auth.py`
  - To see line-by-line author ownership and discover who last modified each specific line of code, run: `git blame auth.py`

### Common Investigation Commands
Here is a list of commonly used commands for inspecting code revisions:
- `git log --oneline` (compact list)
- `git show` (commit detail inspector)
- `git diff` (unstaged edits comparison)
- `git diff --staged` (staged edits comparison)
- `git blame app.py` (line-by-line author mapper)
- `git shortlog` (author commit count aggregator)

---

## 5. Workout Answers & Solutions [id: answers]

### Common Beginner Mistakes
- **Mistake**: Running `git diff` after staging changes and seeing no output.
  - *Fix*: Once changes are staged, `git diff` yields nothing. You must run `git diff --staged` to compare staged files!
- **Mistake**: Assuming `git log` searches all branches by default.
  - *Fix*: `git log` starts at HEAD (current branch). To search all branches, run `git log --all`.

### Enterprise Best Practices
1. **Sanity Check**: Always review your changes with `git diff` or `git diff --staged` before committing.
2. **Descriptive Logs**: Write descriptive commit messages to make `git log --oneline` clean and meaningful for reviewers.
3. **Graph Inspection**: Use `git log --graph --all` to understand complex branch developments across the team.

### Key Takeaways
- `git log` displays repository history by traversing parent commits backward from HEAD.
- `git diff` compares file snapshots to reveal modifications between different lifecycle states.
- `git diff` targets unstaged work; `git diff --staged` targets staged index files.
- `git show` displays metadata and changes introduced by a single target commit.

# Lesson 5: Undoing Changes — Reset, Revert, and Restore

---

```yaml
lesson_id: "GIT-FND-004"
lesson_title: "Undoing Changes: Reset, Revert & Restore"
subject: "Git"
course: "Git Fundamentals"
module: "Basic Local Workflow"
difficulty: "⭐⭐"
time_breakdown:
  reading: "15 min"
  exercise: "25 min"
  quiz: "10 min"
  revision: "5 min"
version: "1.1"
last_updated: "2026-07-17"
status: "Published"
author: "Rajasekar"
reviewed_by: "Admin"
prerequisites:
  - "GIT-FND-002 (Basic Local Workflow)"
tags:
  - "Git Reset"
  - "Git Revert"
  - "Git Restore"
  - "Undoing Changes"
```

---

## 1. Topics Covered [id: topics]
- Discarding workspace modifications using `git restore`
- Switching branches and checking commits with `git switch`
- The three reset variations (`--soft`, `--mixed`, `--hard`)
- Safely rolling back shared history with `git revert`
- Analyzing Detached HEAD states and Reflog logs

## 2. Definitions & Core Concepts [id: definitions]
- **`git restore`**: Discards changes in files.
  - `git restore <file>`: Discards modifications in the working directory (restores file to staged or last committed state).
  - `git restore --staged <file>`: Unstages a file, moving it back to "modified" status.
- **`git switch`**: Switches active branch context (`git switch main`), or creates and switches to a new branch (`git switch -c new-feature`).
- **`git reset`**: Rewrites history by moving the HEAD branch pointer backward.
  - `--soft`: Keeps changes in Staging Area and Working Directory.
  - `--mixed`: Discards Staging Area but preserves changes in Working Directory.
  - `--hard`: Destroys all changes in both Staging Area and Working Directory.
- **`git revert`**: Safe undo method that adds a new commit containing the exact inverse of changes from a previous commit.
- **Detached HEAD**: Occurs when HEAD points directly to a commit hash instead of a local branch pointer. Edits made here will be lost if you switch branches without saving.

## 3. Practical Code Examples [id: examples]

### Example A: Unstaging and Discarding Edits
- **Code**:
  ```bash
  # Stage a file
  git add main.py
  # Unstage the file
  git restore --staged main.py
  # Discard changes in working directory
  git restore main.py
  ```
- **Input (i/p)**: Run restore commands to discard edits.
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git status -s                                        │
  │  (No outputs, workspace is completely clean!)          │
  └────────────────────────────────────────────────────────┘
  ```

### Example B: Detached HEAD State Simulation
- **Code**:
  ```bash
  git log --oneline
  git switch b1a2c3d
  ```
- **Input (i/p)**: Checkout a past commit hash directly.
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git switch b1a2c3d                                   │
  │ Note: switching to 'b1a2c3d'.                          │
  │                                                        │
  │ You are in 'detached HEAD' state. You can look around, │
  │ make experimental changes and commit them...           │
  │                                                        │
  │ HEAD is now at b1a2c3d Add standard db configurations  │
  └────────────────────────────────────────────────────────┘
  ```

### Example C: Recovering a Hard-Reset Commit via Reflog
- **Code**:
  ```bash
  git reset --hard HEAD~1
  git reflog
  git reset --hard HEAD@{1}
  ```
- **Input (i/p)**: Accidentally hard-reset, then query reflog to recover.
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git reflog                                           │
  │ d3f4g5h HEAD@{0}: reset: moving to HEAD~1              │
  │ a1b2c3d HEAD@{1}: commit: Add advanced analytics script│
  │                                                        │
  │ $ git reset --hard HEAD@{1}                            │
  │ HEAD is now at a1b2c3d Add advanced analytics script   │
  └────────────────────────────────────────────────────────┘
  ```

## 4. Hands-on Workouts [id: workouts]
- **Workout 1**: Run `git revert` on your last commit. Inspect the log output to verify that Git appended a new inverse commit.
- **Workout 2**: Enter a Detached HEAD state by checking out a past commit. Create a new branch named `temp-branch` from this state to preserve changes.

## 5. Workout Answers & Solutions [id: answers]

### Solution to Workout 1:
- **Code**:
  ```bash
  git revert HEAD --no-edit
  git log --oneline -n 3
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git log --oneline -n 2                               │
  │ f9e8d7c Revert "Add advanced analytics script"         │
  │ a1b2c3d Add advanced analytics script                  │
  └────────────────────────────────────────────────────────┘
  ```

### Solution to Workout 2:
- **Code**:
  ```bash
  git switch -c temp-branch
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git switch -c temp-branch                            │
  │ Switched to a new branch 'temp-branch'                 │
  └────────────────────────────────────────────────────────┘
  ```

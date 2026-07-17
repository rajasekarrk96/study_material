# Advanced Workspace Helpers — Stash, Bisect, and Worktree

---

```yaml
lesson_id: GIT-ADV-003
lesson_title: "Workspace Helpers: Stash, Bisect & Worktree"
subject: Git
course: "Git Fundamentals"
module: Advanced Workflows
difficulty: "\u2B50\u2B50\u2B50\u2B50"
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
- GIT-ADV-002 (Rewriting History)
tags:
- Git Stash
- Git Bisect
- Git Worktree
- Advanced Workflows
```

---

## 1. Topics Covered [id: topics]
This lesson covers advanced Git productivity workflows. We analyze how to temporarily cache uncommitted changes using stash, locate code regressions using binary search debugging (bisect), and run multiple branch workspaces concurrently using worktrees.

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - How Git represents stash stacks internally using commit objects.
  - The binary search mechanics of git bisect.
  - The directory mapping differences of git worktree.
- **Skills (What you can do)**:
  - Stash and retrieve changes, debug bugs using bisect automation, and configure concurrent worktrees.
- **Outcome (Professional application)**:
  - Accelerate feature context switching and debugging cycles on enterprise codebases.

## 2. Definitions & Core Concepts [id: definitions]
These advanced utilities solve specific development constraints:
- **`git stash`**: Temporarily saves your uncommitted modifications (working directory + staged changes) to a local stack, returning your branch to a clean HEAD state. Internally, a stash entry is actually stored as a **special commit object** pointing to two parent commits (one for the staging index state and one for the working directory state).
- **`git bisect`**: Uses binary search to find the commit that introduced a bug. You identify a "bad" commit where the bug exists and a "good" commit before the bug was introduced. Git checks out the middle commit, you test it, mark it good or bad, and Git repeats the process until the culprit commit is isolated.
- **`git worktree`**: Allows you to have multiple checked-out branches of the same repository in separate local directory folders concurrently, avoiding branch checkout context switches.

### Terminology & Glossary
- **Stash Stack**: A local stack list storing stashed workspace modifications.
- **Binary Search**: Search algorithm dividing search areas in half recursively.
- **Worktree**: Linked directory containing a checkout of a specific branch.

## 3. Practical Code Examples [id: examples]
### Easy
Stash your uncommitted work and pop it back later:
```bash
# Save changes
git stash

# Work on urgent hotfix...

# Apply changes back
git stash pop
```

### Medium
Running a concurrent branch hotfix using a worktree:
```bash
# Add a new directory checked out to branch hotfix-branch
git worktree add ../hotfix-folder hotfix-branch

# Open hotfix-folder, edit, commit, and push.
# Your main repository directory remains on your active feature branch!
```

### Advanced
Debugging using manual git bisect:
```bash
# Start bisect session
git bisect start

# Mark current state as bad
git bisect bad

# Mark a known working commit hash as good
git bisect good c9f5865a

# Git checks out middle commit. Run test, then label:
git bisect good  # or git bisect bad

# Git isolates the bad commit hash. Reset bisect session:
git bisect reset
```

## 4. Hands-on Workouts [id: workouts]
### MCQ
- Which command lists linked worktree folders?
  - A) `git worktree list` (Correct)
  - B) `git worktree show`
  - C) `git worktree status`

### Coding Challenge
- Stash your changes with label "wip UI".

### Predict the Output
- What does `git stash list` output if there are no stashes?
  - Output: Empty response (no text).

### Debugging Task
- Clean up a stale worktree folder metadata.
  - Answer: `git worktree prune`.

### Scenario Question
- A developer needs to fix a bug in `main` but has unstaged work in `feature`. They want to save the work without committing. What should they run?
  - Answer: `git stash`.

### Hands-on Lab
- Edit a file, run `git stash`, inspect `git status` (clean), then run `git stash pop` to restore.

## 5. Workout Answers & Solutions [id: answers]
- **Standard Syntax**: `git stash pop`
- **Aliases**: None.
- **Shortcut**: None.
- **Warning**: Do not run `git stash clear` unless you want to delete all stashes permanently.

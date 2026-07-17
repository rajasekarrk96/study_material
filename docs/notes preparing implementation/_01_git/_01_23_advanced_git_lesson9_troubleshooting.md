# Advanced Git: Diagnostic and Troubleshooting Guide

---

```yaml
lesson_id: GIT-ADV-009
lesson_title: "Advanced Git: Diagnostic & Troubleshooting Guide"
subject: Git
course: "Git Fundamentals"
module: "Advanced Workflows"
difficulty: "⭐⭐⭐⭐"
time_breakdown:
  reading: 20 min
  exercise: 25 min
  quiz: 15 min
  revision: 5 min
version: '1.0'
last_updated: '2026-07-17'
status: Published
author: Rajasekar
reviewed_by: Admin
prerequisites:
- GIT-ADV-008 (Advanced Git: Credential Management & Security)
tags:
- Troubleshooting
- Diagnostics
- Reflog
- Repository Recovery
```

---

## 1. Topics Covered [id: topics]
- Resolving Detached HEAD states
- Recovering lost commits via reflog
- Fixing commits on the wrong branch
- Aborting stuck merges or rebases
- Recovering from force-push overrides

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - Why Git states get "stuck" during merge/rebase and how to interpret console cues.
  - How reflog preserves commit histories even after branch deletions or resets.
- **Skills (What you can do)**:
  - Recover orphaned commits, reset pointer states, and solve conflict bottlenecks.
- **Professional Outcome**:
  - Act as repository administrator, debugging developer workspace blocks and recovery scenarios.

---

## 2. Common Git Troubleshooting Scenarios [id: definitions]

### Scenario 1: Detached HEAD State
- **Problem**: You switched to a commit hash directly (`git switch <hash>`) instead of a branch. Edits made here are not attached to any branch.
- **Resolution**:
  - To save your changes: Create a new branch: `git switch -c new-feature-branch`.
  - To discard changes: Switch back to your branch: `git switch main`.

---

### Scenario 2: Recovering Lost Commits (Reflog)
- **Problem**: You accidentally ran `git reset --hard HEAD~1` and lost your local changes.
- **Resolution**:
  1. Inspect `git reflog` to identify the hash before the reset (e.g., `HEAD@{1}`).
  2. Restore the commit: `git reset --hard HEAD@{1}`.

---

### Scenario 3: Committed on the Wrong Branch
- **Problem**: You made three commits on `main` instead of `feature-login`.
- **Resolution**:
  ```bash
  # 1. Switch to main and get the hash of the latest commits
  git log --oneline
  
  # 2. Switch to feature branch (create it if needed) and cherry-pick the commits
  git switch feature-login
  git cherry-pick <commit-hashes>
  
  # 3. Switch back to main and reset it back before those commits
  git switch main
  git reset --hard <original-commit-hash>
  ```

---

### Scenario 4: Stuck Merge or Rebase
- **Problem**: You are in the middle of a merge or rebase, conflicts are too complex, and you want to clean your workspace.
- **Resolution**:
  - Abort merge: `git merge --abort`
  - Abort rebase: `git rebase --abort`

---

### Scenario 5: Force Push Recovery
- **Problem**: A teammate force-pushed over a branch, deleting your commits on the remote server.
- **Resolution**:
  1. Inspect your local `git reflog` or local branch logs to find the hash of your commit before the push.
  2. Reset your local branch to it: `git reset --hard <your-commit-hash>`.
  3. Force-push it back safely: `git push --force-with-lease origin <branch-name>`.

---

## 3. Practical Code Examples [id: examples]

### Diagnostic Commands Cheat Sheet
| Command | Purpose |
|---|---|
| **`git status`** | Displays the current workspace status and active merge/rebase states. |
| **`git reflog`** | Lists recent HEAD history positions for recovery. |
| **`git fsck`** | Scans for unreachable commits and corrupt objects. |
| **`git diff`** | Shows line changes in conflicted files. |
| **`git merge --abort`** | Aborts a merge session. |
| **`git rebase --abort`** | Aborts a rebase session. |

### Example A: Finding lost commits using `git fsck`
If reflog has expired or is cleared, you can look for dangling commits directly in the database:
```bash
git fsck --lost-found
```

Output:
```text
Checking object directories: 100% (256/256), done.
dangling commit a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0
```
*(Note: You can inspect the contents of that dangling commit using `git show a1b2c3d4` and restore it if needed).*

---

## 4. Hands-on Workouts [id: workouts]

### MCQ
- Which command allows you to view the local HEAD history positions, including branch switches?
  - A) `git log --all`
  - B) `git reflog` (Correct)
  - C) `git fsck`

### Coding Challenge
- Abort an active rebase session.
  - Answer: `git rebase --abort`

### Scenario Question: Wrong branch commit
- A developer commits changes to `main` by mistake. They have not pushed yet.
  - Action: Switch to the correct feature branch, run `git cherry-pick <commit-hash>` to copy the changes, then switch back to `main` and run `git reset --hard HEAD~1` to roll back the commit on `main`.

---

## 5. Workout Answers & Solutions [id: answers]

### Common Beginner Mistakes
- **Panic Deletion**: Deleting the `.git` directory manually because of complex merge conflicts. (Never delete `.git`! Use `git merge --abort` instead).
- **Hard Resets**: Running `git reset --hard` when working files are dirty, losing unstaged changes permanently.

### Enterprise Best Practices
1. **Status First**: When a command fails or feels stuck, run `git status` immediately. It usually provides the exact diagnostic steps required.
2. **Prefer Lease**: Always use `--force-with-lease` when updating remote histories.
3. **Keep Backups**: Before attempting complex rebases or history rewrites, create a backup tag or branch: `git branch backup-before-rebase`.

### Key Takeaways
- Detached HEAD states occur when checkout points directly to a commit hash. Save work using a branch.
- `git reflog` is the ultimate safety net for recovering lost local commits.
- Stuck merges and rebases can be canceled using the `--abort` flag.
- Never delete the `.git` folder; use diagnostic commands to restore repository health.

# Undoing Changes — Reset, Revert, and Restore

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
version: "1.2"
last_updated: "2026-07-17"
status: "Published"
author: "Rajasekar"
reviewed_by: "Admin"
prerequisites:
  - "GIT-FND-002 (Local Workflow: Init, Stage & Commit)"
tags:
  - "Git Reset"
  - "Git Revert"
  - "Git Restore"
  - "Undoing Changes"
```

---

## 1. Topics Covered [id: topics]

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - The architectural boundaries of `restore`, `reset`, `revert`, and `switch`.
  - How Git manages reference history pointers when rolling back commits.
- **Skills (What you can do)**:
  - Discard local modifications, unstage files, and revert public commits.
  - Diagnose detached HEAD states and recover from destructive actions using Reflog.
- **Professional Outcome**:
  - Reverse edits and mistakes confidently without corrupting collaborative branch history.

### Undo Action Decision Flow
Use this flow chart to determine the correct undo command for your scenario:
```text
                            Undo Decision Flow
                            
                          Need to undo something?
                                    │
                                    ▼
                          Is it already committed?
                                    │
                  ┌─────────────────┴─────────────────┐
                  ▼ (No)                              ▼ (Yes)
           Discard file edits?                 Keep commit history?
                  │                                   │
         ┌────────┴────────┐                 ┌────────┴────────┐
         ▼ (Yes)           ▼ (Staged)        ▼ (Yes)           ▼ (No)
    git restore <file>    git restore       git revert <hash>  Rewrite local?
                          --staged <file>                      │
                                                               ▼
                                                       git reset <hash>
```

---

## 2. Definitions & Core Concepts [id: definitions]

### Command Comparisons
| Command | Changes History? | Safe for Shared Repo? | Typical Use |
|---|---|---|---|
| **`git restore`** | ❌ No | ✅ Yes | Discards uncommitted working directory edits. |
| **`git reset`** | ✅ Yes | ❌ Usually No | Moves branch pointers backward (rewrites local history). |
| **`git revert`** | ❌ No (Adds new commit) | ✅ Yes | Safe rollback for pushed commits. |
| **`git switch`** | ❌ No | ✅ Yes | Changes branch focus or enters detached HEAD state. |

### Visual Explanation of `git reset` Modes
The following modes map what states are preserved or reset (assuming the local directory was clean before running the command):
```text
    Mode      Working Directory    Staging Area    Commit History
 ─────────── ─────────────────── ──────────────── ────────────────
  --soft              ✔                  ✔             Reset
  --mixed             ✔                Reset           Reset
  --hard            Reset              Reset           Reset
```

> [!CAUTION]
> **Danger**: `git reset --hard` permanently discards uncommitted changes from both the Working Directory and Staging Area. If those changes are not recoverable through git reflog or another backup, they may be lost permanently. Avoid using this command unless you fully understand its impact.

### Detached HEAD
A detached HEAD state occurs when HEAD points directly to a commit hash instead of a local branch pointer (e.g. when running `git switch <commit-hash>` since the target is a commit, not a branch). Commits created in a detached HEAD state are not attached to any branch. They remain reachable temporarily but may become unreachable if no branch or tag references them. Create a new branch before switching away if you want to preserve your work.

### git log vs. git reflog
| Command | Shows |
|---|---|
| **`git log`** | Repository commit history (follows active branch parent commits). |
| **`git reflog`** | Every movement of the HEAD pointer on your local machine (including resets and branch switches). |

---

## 3. Practical Code Examples [id: examples]

### Example A: git restore Variations
- **Code**:
  ```bash
  # 1. Discard modifications in working directory
  git restore app.py
  
  # 2. Unstage a file (move from staged back to modified)
  git restore --staged app.py
  
  # 3. Restore a file's state from the previous commit
  git restore --source HEAD~1 app.py
  ```
- **Input (i/p)**: Run restore commands on active modifications.
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git status -s                                        │
  │  (File content successfully restored to target state)  │
  └────────────────────────────────────────────────────────┘
  ```

### Example B: Detached HEAD branch creation
- **Code**:
  ```bash
  # Switch to past commit (Git 2.23+ uses switch; legacy checkout)
  git switch b1a2c3d
  
  # Create a branch to save experimental modifications
  git switch -c experimental-branch
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git switch -c experimental-branch                    │
  │ Switched to a new branch 'experimental-branch'         │
  └────────────────────────────────────────────────────────┘
  ```

### Example C: Realistic Recovery Workflow
- **Code**:
  ```bash
  # 1. Inspect status
  git status
  
  # 2. Soft reset to fix the last local commit metadata
  git reset --soft HEAD~1
  
  # 3. Query reflog to check recent HEAD positions
  git reflog
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git reflog                                           │
  │ c2b3a4d HEAD@{0}: reset: moving to HEAD~1              │
  │ a1b2c3d HEAD@{1}: commit: Add database tables          │
  └────────────────────────────────────────────────────────┘
  ```

---

## 4. Hands-on Workouts [id: workouts]

### MCQ
- Which reset mode preserves your Working Directory and Staging Area but resets Commit History?
  - A) `--hard`
  - B) `--soft` (Correct)
  - C) `--mixed`

### Coding Challenge
- Discard unstaged changes in `config.env` and unstage `app.py`.
  - Answers:
    - `git restore config.env`
    - `git restore --staged app.py`

### When Should I Use... Reference Box
- **Use `git restore` when**:
  - You want to discard uncommitted file edits.
  - You need to unstage files from the loading dock.
- **Use `git reset` when**:
  - You want to undo local commits.
  - You want to rewrite local history before pushing.
- **Use `git revert` when**:
  - You need to undo commits that have already been pushed to a remote shared repo.
  - You need to preserve historical commit logs.
- **Use `git reflog` when**:
  - You want to locate lost commits or recover from accidental hard resets.

---

## 5. Workout Answers & Solutions [id: answers]

### Common Beginner Mistakes
- **Mistake**: Using `git reset --hard` to undo changes in a collaborative remote branch.
  - *Fix*: This corrupts team histories. Always use `git revert` for shared remote commits!
- **Mistake**: Switching away from a detached HEAD state without creating a branch first.
  - *Fix*: Your edits will be orphaned. Create a branch (`git switch -c <name>`) before moving HEAD.

### Enterprise Best Practices
1. **Pushed Commits**: Never use `git reset` on commits that have been pushed to remote repositories. Use `git revert` instead.
2. **Status Audit**: Always run `git status` to audit your workspace before executing any reset or restore actions.
3. **Reflog Safety**: If you accidentally run a hard reset, do not panic. Run `git reflog` to locate the previous commit hash and restore it.

### Key Takeaways
- `git restore` discards or unstages file changes without modifying history.
- `git reset` rewrites history by moving local branch references; `--hard` is destructive.
- `git revert` appends an inverse commit to safely undo pushed commits.
- Detached HEAD states occur when switching to a commit hash directly; save work using a branch.
- `git reflog` tracks every movement of HEAD, acting as a safety net for local operations.

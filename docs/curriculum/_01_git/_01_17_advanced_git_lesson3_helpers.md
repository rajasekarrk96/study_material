# Workspace Helpers: Stash, Bisect & Worktree

---

```yaml
lesson_id: GIT-ADV-003
lesson_title: "Workspace Helpers: Stash, Bisect & Worktree"
subject: Git
course: "Git Fundamentals"
module: "Advanced Workflows"
difficulty: "⭐⭐⭐⭐"
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
- GIT-ADV-002 (Rewriting History: Amend, Rebase & Squash)
tags:
- Git Stash
- Git Bisect
- Git Worktree
- Advanced Workflows
```

---

## 1. Topics Covered [id: topics]
- Git Stash
- Git Bisect
- Git Worktree
- Productivity workflows
- Advanced debugging

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - How Git represents stash stacks internally using commit references.
  - The binary search mechanics of git bisect.
  - The layout and performance differences between git worktree and project clones.
- **Skills (What you can do)**:
  - Cache edits, run automated bisect checks, and configure parallel worktrees.
- **Professional Outcome**:
  - Resolve context-switching bottlenecks and debug codebase regressions in enterprise setups.

### Workspace Helper Decision Guide
```text
                         Workspace Helper Guide
                         
                         What do you need to do?
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          ▼                         ▼                         ▼
   Save work temporarily?     Locate regression bug?    Concurrent branches?
          │                         │                         │
          ▼                         ▼                         ▼
      git stash                 git bisect                git worktree
```

---

## Part 1: Git Stash [id: stash]

### Stash Workflow
`git stash` temporarily saves your uncommitted changes, leaving your working directory clean to switch branches or perform hotfixes:
```text
                      Git Stash Workflow Map
                      
       Working Directory (Dirty) ──► git stash ──► Working Directory (Clean)
                                                          │
                                                    Switch Branch
                                                          │
                                                       Fix Bug
                                                          │
                                                    Switch Branch
                                                          │
       Working Directory (Active) ◄─ git stash pop ◄──────┘
```

### Stash Internals
A stash entry is stored as one or more commit objects referenced from `refs/stash`, allowing Git to preserve both staged and unstaged changes until they are applied or dropped. By default, `git stash` only caches tracked files.
- To include untracked files, use: `git stash -u` (or `--include-untracked`).
- To include ignored files, use: `git stash -a` (or `--all`).

### Stash Commands Cheat Sheet
| Command | Purpose |
|---|---|
| **`git stash`** | Saves all local tracked uncommitted changes to the stash stack. |
| **`git stash push -m "desc"`** | Saves changes with a descriptive custom tag name. |
| **`git stash list`** | Lists all stashed versions (returns empty response if no stashes). |
| **`git stash show -p`** | Shows the line-by-line patch changes stored in the latest stash. |
| **`git stash apply`** | Applies stash modifications to your workspace without deleting the stash entry. |
| **`git stash pop`** | Applies stash modifications and deletes them from the stash stack. |
| **`git stash drop`** | Deletes a specific stash entry from the stack. |
| **`git stash clear`** | Destroys all stash entries permanently. |

### Enterprise Scenario: Stashing
You are developing a feature inside `login.py`. Suddenly, an urgent security bug report hits main. You cannot commit half-finished code.
- *Solution*: Run `git stash -u` to save your work, switch to `main`, write and deploy the security fix, switch back to your branch, and run `git stash pop` to continue development.

---

## Part 2: Git Bisect [id: bisect]

### Bisect Visualization
`git bisect` performs a binary search over your commit history to identify the exact commit that introduced a bug or regression:
```text
                         git bisect Binary Search
                         
       Commit History:
       [A] ──► [B] ──► [C] ──► [D] ──► [E] ──► [F] ──► [G] ──► [H]
      (Good)                                                  (Bad)
                                 │
                           Check Mid [D]
                         (Marked: Good)
                                 │
                                 ▼
                     Search: [E] ──► [F] ──► [G] ──► [H]
                                       │
                                 Check Mid [F]
                                 (Marked: Bad)
                                       │
                                       ▼
                           Search: [E] ──► [F]
                                     │
                               Check Mid [E]
                               (Marked: Bad)  ◄── [Culprit Isolated]
```

### Automated Bisect
Instead of testing each checked-out commit manually, you can automate the process using a test script:
```bash
# Start automated run
git bisect start HEAD v1.0.0
git bisect run ./test.sh
```
Git will automatically execute the test script for each checked-out commit until it identifies the first bad commit, then halt.

### Bisect Commands Cheat Sheet
| Command | Purpose |
|---|---|
| **`git bisect start`** | Initiates a bisect debugging session. |
| **`git bisect bad`** | Marks a commit as broken/buggy. |
| **`git bisect good <hash>`** | Marks a commit as working/bug-free. |
| **`git bisect reset`** | Concludes the session and returns HEAD to your original branch. |

### Enterprise Scenario: Bisecting
A test suite that succeeded in release `v1.2.0` is now failing on `main` after 80 commits.
- *Solution*: Start a bisect session marking `v1.2.0` as `good` and `HEAD` as `bad`. Git will isolate the commit introducing the bug in about 6 steps.

---

## Part 3: Git Worktree [id: worktree]

### Worktree Visualization
Worktrees allow you to have multiple checked-out branches of the same repository in separate local directory folders concurrently:
```text
                         git worktree Layout
                         
                         Repository Object DB
                                  │
          ┌───────────────────────┴───────────────────────┐
          ▼                                               ▼
     main project/                                  hotfix-folder/
     (feature branch)                               (hotfix branch)
```

### Worktree vs. Clone
| Feature | git worktree | git clone |
|---|---|---|
| **Repository Database** | Shares a single repository database. | Creates separate repository databases. |
| **Disk Space** | Extremely efficient (no duplication). | Large disk footprint (duplicates objects). |
| **History Logs** | Synchronized across workspaces. | Independent. |
| **Context Switch** | Instant parallel checkouts. | Requires separate clones and sync steps. |

### Worktree Commands Cheat Sheet
| Command | Purpose |
|---|---|
| **`git worktree add <path> <branch>`** | Creates a new directory linked to a specific branch checkout. |
| **`git worktree list`** | Lists all active linked worktree directories. |
| **`git worktree remove <path>`** | Preferred command to delete a worktree directory. |
| **`git worktree prune`** | Cleans up stale metadata left behind by deleted worktree folders. |

### Enterprise Scenario: Worktrees
You are editing a database migration script on a feature branch. Suddenly, you must review a teammate's PR on `main` without interrupting your active database states.
- *Solution*: Run `git worktree add ../review-dir main`. Open the new directory in your editor to review and test the PR, then delete it with `git worktree remove ../review-dir` when finished.

---

## 4. Hands-on Workouts [id: workouts]

### MCQ
- Which command includes untracked files when stashing changes?
  - A) `git stash --all`
  - B) `git stash --include-untracked` (Correct)
  - C) `git stash --index`

### Coding Challenge
- Remove a worktree directory located at `../temp-fix`.
  - Answer: `git worktree remove ../temp-fix`

---

## 5. Workout Answers & Solutions [id: answers]

### Common Mistakes
- **Stash**: Forgetting that stashed changes exist on the stack and repeating edits.
  - *Fix*: Run `git stash list` frequently to audit cached revisions.
- **Bisect**: Forgetting to run `git bisect reset` after isolating a bug, leaving your HEAD in a detached state.
  - *Fix*: Always reset the bisect session once debugging is complete.
- **Worktree**: Manually deleting a worktree folder using `rm -rf` without running `git worktree remove`.
  - *Fix*: If deleted manually, you must run `git worktree prune` to clean up stale metadata.

### Enterprise Best Practices
1. **Descriptive Stashes**: Always name your stashes using `git stash push -m "description"` to easily identify them.
2. **Automated Testing**: Automate your debugging sessions using script scripts with `git bisect run`.
3. **Parallel Checkouts**: Use worktrees instead of multiple duplicate clones for concurrent feature development.

### Key Takeaways
- `git stash` saves uncommitted modifications, leaving your workspace clean.
- `git bisect` uses binary search to identify the commit that introduced a bug.
- `git worktree` enables multiple parallel branch checkouts from a single repository database.
- Choosing the right helper tool reduces context-switching overhead and improves productivity.

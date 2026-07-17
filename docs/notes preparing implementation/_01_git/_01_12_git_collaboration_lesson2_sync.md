# Syncing Data — Fetch, Pull, and Push

---

```yaml
lesson_id: GIT-COL-002
lesson_title: "Syncing Data: Fetch, Pull & Push"
subject: Git
course: "Git Fundamentals"
module: "Git Collaboration"
difficulty: "⭐⭐"
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
- GIT-COL-001 (Remote Repositories & Origin Config)
tags:
- Git Fetch
- Git Pull
- Git Push
- Syncing
```

---

## 1. Topics Covered [id: topics]
- Git Fetch
- Git Pull
- Git Push
- Pull Rebase workflows
- Ahead/Behind tracking states

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - The core structural difference between `git fetch` and `git pull`.
  - Why `git pull --rebase` is preferred over standard merging pull actions in teams.
  - How tracking branches determine if your workspace is "ahead" or "behind" remote targets.
- **Skills (What you can do)**:
  - Fetch metadata safely, pull and rebase updates, publish local branches with upstream tracking.
- **Professional Outcome**:
  - Maintain clean linear histories in team branch environments, executing safe code updates without duplicate merges.

---

## 2. Definitions & Core Concepts [id: definitions]

### Fetch vs. Pull Architecture Diagram
The core difference between fetch and pull lies in whether changes are integrated into your active workspace automatically:
```text
                           Fetch vs. Pull Data Flow
                           
                           Remote Repository (GitHub)
                                       │
                     ┌─────────────────┴─────────────────┐
                     │ git fetch                         │ git pull
                     ▼                                   ▼
          Local origin/main Pointer             Local origin/main Pointer
             (main unchanged)                            │
                                                         ▼
                                                Merged into local main
                                              (Working Directory updated)
```

### Fetch vs. Pull Comparison
| Feature | `git fetch` | `git pull` |
|---|---|---|
| **What it does** | Downloads remote commits, objects, and references. | Downloads remote changes and merges them into current branch. |
| **Workspace Safety** | 100% safe (does not modify your files). | Potential merge conflicts (modifies local files). |
| **Working Directory** | Unchanged. | Updated (files are modified). |
| **Formula** | Standalone download. | `git fetch` + `git merge` (or `git rebase`). |

---

### git pull: Merge vs. Rebase
When pulling changes, you can choose how Git integrates those changes with your local unpushed commits:

#### 1. Default Pull (Merge)
```text
  Local commits:   A ──► B (origin/main) ──► C (main)
  Remote commits:  A ──► B ──► D (origin/main updated)
  
  After pull (merge):
  A ──► B ──► C ──► D ──► [Merge Commit] (main)
```

#### 2. Rebase Pull (`git pull --rebase`)
```text
  Local commits:   A ──► B (origin/main) ──► C (main)
  Remote commits:  A ──► B ──► D (origin/main updated)
  
  After pull (rebase):
  A ──► B ──► D ──► C' (main)   [No merge commit, clean linear path]
```
> [!TIP]
> **Rebase Pull is standard in many enterprise teams** because it avoids creating cluttering merge commits every time a developer pulls updates.

---

### Ahead and Behind Tracking States
When a local branch is linked to a remote-tracking branch, running `git status` reports how many commits differ:
- **`ahead`**: You have local commits that are not yet pushed to the remote repository.
- **`behind`**: The remote repository has commits that you have not yet fetched and integrated locally.

---

## 3. Practical Code Examples [id: examples]

### Syncing Commands Cheat Sheet
| Command | Purpose |
|---|---|
| **`git fetch origin`** | Safely downloads remote branch updates without changing files. |
| **`git pull`** | Fetches updates and merges them into the active branch. |
| **`git pull --rebase`** | Fetches updates and replays local commits on top of them. |
| **`git push -u origin <branch>`** | Pushes branch and links it to remote upstream tracking. |
| **`git push --force-with-lease`** | Pushes rewritten history commits safely. |

### Example A: Pulling with Rebase
```bash
# Pull changes and replay local work linearly
git pull --rebase origin main
```

Output:
```text
Successfully rebased and updated refs/heads/main.
```

### Example B: Pushing and linking branch
```bash
# Switch to new feature branch
git switch -c feature/checkout-api

# Commit some edits
git commit -am "feat: add secure gateway checkout"

# Push and configure upstream tracking branch
git push -u origin feature/checkout-api
```

Output:
```text
Branch 'feature/checkout-api' set up to track remote branch 'feature/checkout-api' from 'origin'.
```

---

## 4. Hands-on Workouts [id: workouts]

### MCQ
- Which command downloads remote history metadata without altering local working files?
  - A) `git pull`
  - B) `git fetch` (Correct)
  - C) `git push`

### Coding Challenge
- Configure your local repository to always use rebase instead of merge by default when pulling.
  - Answer: `git config --global pull.rebase true`

### Scenario Question: Rejected Push
- A developer attempts to run `git push origin main` but gets a `[rejected - non-fast-forward]` error.
  - Why? The remote repository has newer commits that the developer has not yet fetched and merged.
  - Fix: Run `git pull --rebase origin main`, resolve conflicts if they arise, then run `git push origin main`.

---

## 5. Workout Answers & Solutions [id: answers]

### Common Beginner Mistakes
- **Mistake**: Blindly running `git pull` when working tree files are dirty, causing unexpected merge conflicts.
  - *Fix*: Run `git status` first. Stash your changes (`git stash`) before pulling if your workspace is dirty.
- **Mistake**: Using `--force` instead of `--force-with-lease` after a rebase.
  - *Fix*: Plain `--force` will overwrite teammates' work on the remote server.

### Enterprise Best Practices
1. **Fetch First**: Run `git fetch` first to inspect incoming changes with `git log HEAD..origin/main` before merging.
2. **Standardize Rebase Pulls**: Configure `git config --global pull.rebase true` to preserve linear history records across team forks.
3. **Upstream Linking**: Always use the `-u` flag on your first push to set up automatic tracking.

### Key Takeaways
- `git fetch` is safe; it only downloads files and updates tracking references.
- `git pull` combines `fetch` and `merge`/`rebase`, updating your working files.
- `git pull --rebase` maintains linear histories by preventing empty merge commits.
- Upstream tracking links local branches to remote counterparts for simplified status reporting.

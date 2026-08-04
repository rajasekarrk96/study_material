# Rewriting History: Amend, Rebase & Squash

---

```yaml
lesson_id: GIT-ADV-002
lesson_title: "Rewriting History: Amend, Rebase & Squash"
subject: Git
course: "Git Fundamentals"
module: "Advanced Workflows"
difficulty: "⭐⭐⭐⭐"
time_breakdown:
  reading: 18 min
  exercise: 25 min
  quiz: 15 min
  revision: 5 min
version: '1.2'
last_updated: '2026-07-17'
status: Published
author: Rajasekar
reviewed_by: Admin
prerequisites:
- GIT-ADV-001 (Git Internals: Blobs, Trees & Commits)
tags:
- Rebase
- Amend
- Squash
- Reflog
```

---

## 1. Topics Covered [id: topics]
- git commit --amend
- Interactive rebase
- Squashing commits
- Recovering with reflog

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - Why rewriting history creates new commit object IDs (hashes) while leaving previous commits unreachable.
  - The architectural difference between squashing (combining messages) and fixing up (discarding messages).
  - The Golden Rule of Rebasing: Never rewrite history on public, shared branches.
- **Skills (What you can do)**:
  - Amend, reorder, squash, and drop commits using interactive rebase panels.
  - Recover from broken states or lost commits using reflog coordinates.
- **Professional Outcome**:
  - Produce clean, reviewable, linear commit timelines before integrating pull requests into public streams.

---

## 2. Definitions & Core Concepts [id: definitions]

### History Rewriting Diagram
Commits in Git are immutable. When you "rewrite" history, you do not change existing commits. Instead, Git creates **new commit objects** and redirects branch pointers to them:
```text
                     Before Rewriting History
                     
            [Commit A] ──► [Commit B] ──► [Commit C] ──► [Commit D] (main)
            
                     After Rewriting History
                     
                                       ┌──► [Commit C] ──► [Commit D] (Unreachable)
                                       │
            [Commit A] ──► [Commit B] ──┴──► [Commit C'] ──► [Commit D'] (main)
```
> [!NOTE]
> The original commits `C` and `D` are not deleted immediately. They become **unreachable** commits. They remain in the local database and can be recovered using the reflog until Git's garbage collection (**`git gc`**) prunes them based on repository retention settings.

### Decision Guide
Use this chart to select the correct history rewriting tool for your scenario:
```text
                        History Rewriting Guide
                        
                         What do you need to do?
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          ▼                         ▼                         ▼
   Fix latest commit?      Combine/Reorder commits?   Recover lost history?
          │                         │                         │
          ▼                         ▼                         ▼
  git commit --amend           git rebase -i             git reflog
```

### History Rewriting Command Comparisons
| Command | Typical Use | Rewrites History? |
|---|---|---|
| **`git commit --amend`** | Updates files or corrections on the last commit. | Yes |
| **`git rebase -i`** | Reorders, edits, drops, or merges multiple commits. | Yes |
| **`git squash` (via rebase)** | Combines multiple commits and edits messages. | Yes |
| **`git reflog`** | Lists recent HEAD movements to recover states. | No |

---

### Visualizing Interactive Rebase & Squashing
Interactive rebase (`git rebase -i`) lets you manipulate commits. Squashing combines multiple commits into a single commit:
```text
           Before Squash                     After Squash
           
               [D] (Commit 4)
                │
               [C] (Commit 3)                    [BCD] (Combined Commit)
                │                                  │
               [B] (Commit 2) ───► [Squash] ──────►[A] (Commit 1)
                │
               [A] (Commit 1)
```
- **`squash` (s)**: Combines commit content and prompts for a combined commit message.
- **`fixup` (f)**: Combines commit content but discards the child commit message (keeps only parent message).

---

### reflog Recovery Mechanics
`git reflog` records every position HEAD has pointed to, including resets, rebases, and checkouts:
```text
  HEAD@{0}: rebase -i (finish): returning to refs/heads/feature
  HEAD@{1}: rebase -i (squash): feat: initialize dashboard database
  HEAD@{2}: rebase -i (start): checkout HEAD~3
  HEAD@{3}: commit: fix dashboard query layout
```
> [!IMPORTANT]
> Unreachable commits can be restored by resetting to their specific reflog coordinates. The exact index (e.g. `HEAD@{2}`) depends on your local reflog history; always inspect `git reflog` first to verify the correct recovery target.

---

## 3. Practical Code Examples [id: examples]

### Interactive Rebase Command Reference
| Command | Purpose |
|---|---|
| **`git rebase -i HEAD~N`** | Opens the interactive rebase panel for the last `N` commits. |
| **`git rebase --continue`** | Resumes a rebase session after resolving file conflicts. |
| **`git rebase --abort`** | Aborts the rebase session and returns branch to pre-rebase state. |
| **`git rebase --skip`** | Skips a commit during conflict resolution. |

### Example A: Interactive Rebase Setup
- **Code**:
  ```bash
  # Open interactive rebase for the last 3 commits
  git rebase -i HEAD~3
  ```
- **Panel Editor (Text Interface)**:
  ```text
  pick 9b8c7d6 feat: add database settings
  squash a1b2c3d fix: resolve DB connection timeout
  squash e5f6g7h docs: update database credentials list
  
  # Rebase commands:
  # p, pick = use commit
  # s, squash = use commit, but meld into previous commit
  # f, fixup = like "squash", but discard this commit's log message
  ```

### Example B: Safe Force-Pushing
- **Code**:
  ```bash
  # Push rewritten commits safely to your remote feature branch
  git push origin feature-login --force-with-lease
  ```
  *(Note: Never use simple `--force` as it overwrites remote updates blindly. `--force-with-lease` fails if teammates have pushed new commits to the remote branch since your last fetch)*

### Example C: Complete Cleanup Workflow
- **Code**:
  ```bash
  # 1. Edit files and amend latest commit
  echo "debug = False" > settings.py
  git add settings.py
  git commit --amend --no-edit
  
  # 2. Cleanup local history commits
  git rebase -i HEAD~4
  
  # 3. Verify history looks linear and clean
  git log --oneline
  
  # 4. Push safely
  git push origin feature/login --force-with-lease
  ```

---

## 4. Hands-on Workouts [id: workouts]

### MCQ
- Which rebase action combines a commit but discards its message?
  - A) `squash`
  - B) `fixup` (Correct)
  - C) `drop`

### Coding Challenge
- Abort an interactive rebase process that has run into conflict.
  - Answer: `git rebase --abort`

### Scenario Question: Undoing an amend
- A developer runs `git commit --amend` but realizes they included incorrect files. How do they recover the original commit?
  - Answer: Run `git reflog` to identify the hash of HEAD before the amend (e.g. `HEAD@{1}`), then run `git reset --soft HEAD@{1}` to restore the original files and commit state.

---

## 5. Workout Answers & Solutions [id: answers]

### Common Beginner Mistakes
- **Mistake**: Force-pushing to a shared repository branch (like `main` or `develop`).
  - *Result*: Overwrites changes made by collaborators, corrupting their local tracking.
- **Mistake**: Forgetting to run tests after a rebase.
  - *Fix*: Code may conflict logically even if Git automatically merges it. Verify compiles finish.

### Enterprise Best Practices
1. **Private Branches Only**: Restructure history only on private local branches before sharing code.
2. **Squash Before Merge**: Squash intermediate checkpoint commits (e.g. "wip", "debug") into atomic, descriptive commits before opening PRs.
3. **Lease Protection**: Configure Git templates to default to `--force-with-lease` for push behaviors.

### Key Takeaways
- History rewriting creates new commit objects (IDs/hashes) instead of changing old ones.
- `git commit --amend` modifies the latest commit.
- Interactive rebase provides options to reorder, edit, squash, or drop commits.
- `git reflog` tracks HEAD history, providing a safety net to recover unreachable commits.
- The Golden Rule: Do not rewrite commits that others have based their work on.

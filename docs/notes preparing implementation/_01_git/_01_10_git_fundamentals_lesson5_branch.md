# Branching and Merging Basics — Creating, Switching, and Merging

---

```yaml
lesson_id: "GIT-FND-005"
lesson_title: "Branching Basics & Conflict Resolution"
subject: "Git"
course: "Git Fundamentals"
module: "Branching & Merging Basics"
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
  - "GIT-FND-004 (Undoing Changes)"
tags:
  - "Git Branch"
  - "Git Merge"
  - "Git Tags"
  - "Fast-Forward"
```

---

## 1. Topics Covered [id: topics]
- Viewing branch lists using standard commands
- Understanding Git's lightweight pointer branching model
- Reconciling histories: Fast-Forward vs Three-Way merges
- Detailing conflict markers and manual resolution
- Tagging releases: Annotated vs Lightweight tags

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - Git branching and merge strategies.
  - Why merge conflicts occur when lines of development diverge.
  - The differences between lightweight and annotated tags.
- **Skills (What you can do)**:
  - Create and merge branches, abort merges, and handle conflicts manually.
  - Tag specific commit snapshots locally and push them to remotes.
- **Professional Outcome**:
  - Develop features safely using isolated branch lines and prepare tagged releases for deployment.

---

## 2. Definitions & Core Concepts [id: definitions]

### Branch Visualization Diagrams
Creating a branch in Git does not copy any project files. A branch is simply a lightweight, mutable pointer referencing the latest commit.

#### 1. Before Branching
```text
  [Commit A] ──► [Commit B] ──► [Commit C]  ◄── (main)
```

#### 2. After Creating `feature-login` Branch
```text
  [Commit A] ──► [Commit B] ──► [Commit C]  ◄── (main) & (feature-login)
```

#### 3. After Creating New Commits in Both Branches (Divergence)
```text
                                [Commit F]  ◄── (main)
                               /
  [Commit A] ──► [Commit B] ──► [Commit C]
                               \
                                [Commit D] ──► [Commit E]  ◄── (feature-login)
```

---

### Merging Strategies (FF vs. 3-Way)

#### Fast-Forward Merges
Occur when the target branch has not diverged since the source branch split. Git simply moves the branch pointer forward:
```text
  [Commit A] ──► [Commit B] ──► [Commit C] (main)
                                 \
                                  [Commit D] (feature)
                                  
  After merge:
  [Commit A] ──► [Commit B] ──► [Commit C] ──► [Commit D] (main)  [No merge commit created]
```

#### Three-Way Merges
Occur when both branches have diverged since their common ancestor. Git combines both histories using a new **Merge Commit**:
```text
  [Commit A] ──► [Commit B] ──► [Commit C] ──► [Commit F] (main)
                                 \
                                  [Commit D] ──► [Commit E] (feature)
                                  
  After merge:
  [Commit A] ──► [Commit B] ──► [Commit C] ──► [Commit F] ────► [Commit M] (main)  [Merge commit]
                                 \                             /
                                  [Commit D] ──► [Commit E] ──┘
```

---

### Why Merge Conflicts Occur
Merge conflicts happen when developers edit the **same lines of code** in the **same file** across different branches. Git cannot decide which edit to preserve and inserts visual conflict markers into the file:
```text
  Main Branch:     print("Hello")  ───┐
                                      ├──► Git cannot decide ──► Conflict Markers
  Feature Branch:  print("Hi")     ───┘
```

#### Conflict Markers Decoded
```text
  <<<<<<< HEAD
  print("Hello")        # Code in your current active branch
  =======               # Separator marker line
  print("Hi")           # Code in the incoming merged branch
  >>>>>>> feature-login
```

---

### Tagging Releases (Lightweight vs. Annotated)
Production releases are typically marked with annotated tags because they preserve vital release metadata.

| Lightweight Tag | Annotated Tag |
|---|---|
| A simple pointer referencing a commit hash. | Stored as a full, rich Git database object. |
| Stores no metadata (no author, date, message). | Stores tagger name, email, timestamp, and message. |
| Typically used for temporary local pointers. | Recommended choice for production releases. |
| Cannot be signed. | Can be cryptographically signed using GPG keys. |

---

## 3. Practical Code Examples [id: examples]

### Branch Command Cheat Sheet
| Command | Purpose |
|---|---|
| **`git branch --list`** | Lists all local branches. |
| **`git branch new-feature`** | Creates a new branch named `new-feature`. |
| **`git switch new-feature`** | Switches your active HEAD context to `new-feature`. |
| **`git switch -c new-feature`** | Creates and switches to `new-feature` in one command. |
| **`git branch -d feature`** | Deletes a merged local branch. |
| **`git branch -D feature`** | Force-deletes an unmerged local branch. |

### Merge Command Cheat Sheet
| Command | Purpose |
|---|---|
| **`git merge feature`** | Merges `feature` branch into current active branch. |
| **`git merge --no-ff feature`** | Forces Git to create a merge commit even if FF is possible. |
| **`git merge --abort`** | Cancels an ongoing merge conflict session. |
| **`git status`** | Displays details on files with unresolved conflict markers. |

---

### Example A: Resolving Conflicts with git status Checks
- **Code**:
  ```bash
  # Attempt merge causing conflict
  git merge feature-login
  
  # Inspect conflicting files
  git status
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git status                                           │
  │ On branch main                                         │
  │ You have unmerged paths.                               │
  │   (fix conflicts and run "git commit")                 │
  │ Unmerged paths:                                        │
  │   both modified:   main.py                             │
  └────────────────────────────────────────────────────────┘
  ```

### Example B: Tagging and Remote Operations
- **Code**:
  ```bash
  # Create annotated tag
  git tag -a v1.0.0 -m "Release version 1.0.0"
  
  # Push specific tag to remote origin repository
  git push origin v1.0.0
  
  # Delete tag locally and on remote
  git tag -d v1.0.0
  git push origin --delete v1.0.0
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git tag -d v1.0.0                                    │
  │ Deleted tag 'v1.0.0' (was f8e7d6c)                     │
  └────────────────────────────────────────────────────────┘
  ```

### Example C: Realistic Feature Workflow
- **Code**:
  ```bash
  # 1. Start feature branch using standard naming
  git switch -c feature/login-validation
  
  # 2. Complete edits and commit
  echo "def validate(): pass" >> auth.py
  git commit -am "feat: add form login validations"
  
  # 3. Switch main and merge changes
  git switch main
  git merge feature/login-validation
  
  # 4. Delete feature branch cleanly
  git branch -d feature/login-validation
  ```

---

## 4. Hands-on Workouts [id: workouts]

### MCQ
- Which command deletes a local branch that has been successfully merged?
  - A) `git branch -D`
  - B) `git branch -d` (Correct)
  - C) `git branch --remove`

### Coding Challenge
- Force a merge to create a merge commit even if a fast-forward is possible.
  - Answer: `git merge --no-ff <branch_name>`

### Standard Branch Naming Conventions
In enterprise repositories, branch names are categorized by prefix:
- `feature/login-validation` (new features)
- `bugfix/payment-error` (bug fixes)
- `hotfix/security-patch` (immediate production patches)
- `release/v1.2` (release preparation)
- `experiment/ui-redesign` (exploratory tasks)

---

## 5. Workout Answers & Solutions [id: answers]

### Common Beginner Mistakes
- **Mistake**: Forgetting to delete merged branches, leading to cluttered repositories.
  - *Fix*: Regularly clean up local and remote branch references.
- **Mistake**: Leaving conflict markers (`<<<<<<<` or `=======`) inside files and committing.
  - *Fix*: You must search and resolve markers before staging and committing.

### Enterprise Best Practices
1. **Isolated Branches**: Create a dedicated branch for every single feature or bug fix.
2. **Review Cycles**: Always use Pull Requests (PRs) for code review before merging into `main`.
3. **Tagged Releases**: Tag every production release using annotated GPG-signed tags.

### Key Takeaways
- Git branches are lightweight pointer references, not duplicate file copies.
- Fast-forward merges move branch pointers; three-way merges combine divergent histories.
- Merge conflicts arise from overlapping line changes and must be resolved manually.
- Annotated tags preserve author metadata and messages, making them ideal for releases.

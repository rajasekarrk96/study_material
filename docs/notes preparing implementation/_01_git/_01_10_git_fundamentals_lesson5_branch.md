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
version: "1.1"
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
- Creating, list-checking, and deleting branches
- The mechanics of Fast-Forward merges vs Three-Way merges
- Identifying and resolving merge conflicts manually
- Tagging commits: Lightweight tags vs Annotated tags
- Viewing and deleting git tags

## 2. Definitions & Core Concepts [id: definitions]
- **Branch**: A mutable, lightweight reference pointer directing to a specific commit.
- **Fast-Forward Merge**: Git simply moves the branch pointer forward to point to the incoming commit. This is only possible if there have been no new commits on the target branch since the branches diverged.
- **Three-Way Merge (Recursive)**: Created when the source and target branches have diverged. Git merges the changes based on a common ancestor and creates a new **Merge Commit** pointing to both branches.
- **Lightweight Tag**: A simple bookmark pointer referencing a specific commit hash (created by `git tag <tag_name>`).
- **Annotated Tag**: Stored as full objects in the Git database. They contain the tagger's name, email, date, an optional message, and can be cryptographically signed with GPG keys (created by `git tag -a <tag_name> -m "..."`).

## 3. Practical Code Examples [id: examples]

### Example A: Simulating Fast-Forward and 3-Way merges
- **Code**:
  ```bash
  # Fast-forward merge setup
  git switch main
  git merge feature-login
  
  # Forced non-fast-forward merge (creates merge commit anyway)
  git merge --no-ff feature-login
  ```
- **Input (i/p)**: Run merge on clean feature branch.
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git merge feature-login                              │
  │ Updating a1b2c3d..e4f5g6h                              │
  │ Fast-forward                                           │
  │  main.py | 2 +-                                        │
  │  1 file changed, 1 insertion(+), 1 deletion(-)        │
  └────────────────────────────────────────────────────────┘
  ```

### Example B: Resolving manual conflicts
- **Code**:
  ```bash
  git merge dev-branch
  # Open main.py to fix conflicts:
  # <<<<<<< HEAD
  # print("Hello BB")
  # =======
  # print("Hello Solutions")
  # >>>>>>> dev-branch
  
  # Edit to: print("Hello BB Solutions")
  git add main.py
  git commit -m "Merge dev-branch and resolve conflict"
  ```
- **Input (i/p)**: Stage conflict fix and commit.
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git merge dev-branch                                 │
  │ Auto-merging main.py                                   │
  │ CONFLICT (content): Merge conflict in main.py          │
  │ Automatic merge failed; fix conflicts and commit.      │
  │                                                        │
  │ $ git commit -m "Merge dev-branch and resolve conflict"│
  │ [main d7e8f9c] Merge dev-branch and resolve conflict   │
  └────────────────────────────────────────────────────────┘
  ```

### Example C: Tagging Releases (Lightweight vs Annotated)
- **Code**:
  ```bash
  # 1. Create Lightweight Tag
  git tag v1.0.0-lw
  
  # 2. Create Annotated Tag
  git tag -a v1.0.0 -m "Production release v1.0.0"
  
  # 3. View tag details
  git show v1.0.0
  ```
- **Input (i/p)**: Setup and view release tags.
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git show v1.0.0                                      │
  │ tag v1.0.0                                             │
  │ Tagger: Rajasekar <rajasekar@bbsolutions.com>           │
  │ Date:   Fri Jul 17 18:00:00 2026 +0530                 │
  │                                                        │
  │ Production release v1.0.0                              │
  │                                                        │
  │ commit a1b2c3d4e5f6g7h8i9j0k (HEAD -> main, tag: v1.0.0)│
  └────────────────────────────────────────────────────────┘
  ```

## 4. Hands-on Workouts [id: workouts]
- **Workout 1**: Create a branch named `release-v1`. Tag the last commit on `release-v1` with annotated tag `v1.1.0`. Delete the tag locally using tag options.
- **Workout 2**: Trigger a merge conflict by editing the same line of a file in both `main` and a `test-conflict` branch, and then resolve it.

## 5. Workout Answers & Solutions [id: answers]

### Solution to Workout 1:
- **Code**:
  ```bash
  git switch -c release-v1
  git tag -a v1.1.0 -m "Release v1.1.0"
  git tag -d v1.1.0
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git tag -d v1.1.0                                    │
  │ Deleted tag 'v1.1.0' (was a7b8c9d)                     │
  └────────────────────────────────────────────────────────┘
  ```

### Solution to Workout 2:
- **Code**:
  ```bash
  git switch main
  echo "Main edits" > doc.txt
  git commit -am "Edit line in main"
  
  git switch -c test-conflict
  echo "Conflict edits" > doc.txt
  git commit -am "Edit line in test-conflict"
  
  git switch main
  git merge test-conflict
  # Resolve conflict markers inside doc.txt, then:
  git add doc.txt
  git commit -m "Resolved conflicts"
  ```

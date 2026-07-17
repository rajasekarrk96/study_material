# Lesson 5: Branching and Merging Basics — Creating, Switching, and Merging

---

```yaml
lesson_id: GIT-FND-005
subject: Git
course: Git Fundamentals
module: Branching & Merging Basics
difficulty: "\u2B50\u2B50"
time_breakdown:
  reading: 15 min
  exercise: 25 min
  quiz: 10 min
  revision: 5 min
version: '1.0'
last_updated: '2026-07-17'
status: Published
author: Rajasekar
reviewed_by: Admin
prerequisites:
- GIT-FND-004 (Undoing Changes)
tags:
- Git Branch
- Git Merge
- Switch Branch
- Fast-Forward
```

---

## 1. Topics Covered [id: topics]
This lesson covers Git's core branching model. You will learn how to create independent development lines, switch between them, merge code using fast-forward and three-way strategies, and resolve basic merge conflicts.

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - How branches are implemented as lightweight references pointing to commit hashes.
  - The difference between Fast-Forward merges and Three-Way (Recursive) merges.
- **Skills (What you can do)**:
  - Create and switch branches, merge codebases, identify conflict zones, and resolve merge conflicts.
- **Outcome (Professional application)**:
  - Isolate feature development using branches to keep production code clean and stable.

## 2. Definitions & Core Concepts [id: definitions]
In Git, a branch is simply a lightweight, mutable pointer to a commit hash. When you commit, the branch pointer automatically moves forward to point to the new commit.
The **HEAD** pointer is a reference that points to the current active branch pointer (or to a specific commit if detached).

### Merging Strategies
- **Fast-Forward Merge**: Occurs when the target branch has not diverged from the source branch. Git simply moves the branch pointer forward. No new merge commit is created.
- **Three-Way Merge (Recursive)**: Occurs when the branches have diverged. Git finds the common ancestor commit, compares both branches' latest snapshots, merges the changes, and automatically creates a new **Merge Commit** pointing to both parent commits.

### Terminology & Glossary
- **Fast-Forward**: A merge where the branch pointer is simply moved forward.
- **Merge Commit**: A commit with two or more parent commits, representing a combined state.
- **Merge Conflict**: A state where Git cannot automatically merge changes because line edits overlap.

## 3. Practical Code Examples [id: examples]
### Easy
Create a new feature branch and switch to it:
```bash
git switch -c feature-login
```

### Medium
Merge a feature branch back into main:
```bash
git switch main
git merge feature-login
```

### Advanced
Resolving a merge conflict:
```bash
# Git merge outputs: "Automatic merge failed; fix conflicts..."
# Open conflict file to locate markers:
# <<<<<<< HEAD
# print("Version A")
# =======
# print("Version B")
# >>>>>>> feature-branch

# Edit file to resolve conflict, then stage and commit:
git add conflict_file.py
git commit -m "Merge branch feature-branch and resolve conflicts"
```

## 4. Hands-on Workouts [id: workouts]
### MCQ
- Which command switches to a branch and creates it if it does not exist?
  - A) `git branch -c`
  - B) `git switch -c` (Correct)
  - C) `git checkout -b` (Correct - legacy)

### Coding Challenge
- Create and switch to a branch named `fix-bug`.

### Predict the Output
- If you run `git merge --abort` during a conflict, what state does the repository return to?
  - Output: The state before the merge attempt started.

### Debugging Task
- Resolve a conflict where HEAD has `val = 1` and branch has `val = 2` by selecting `val = 2`.
  - Answer: Replace conflict block with `val = 2`, stage, and commit.

### Scenario Question
- A developer wants to see all local branches. What command should they use?
  - Answer: `git branch` or `git branch -a`.

### Hands-on Lab
- Initialize repo, add file on main, create feature branch, edit file on feature, switch to main, merge.

## 5. Workout Answers & Solutions [id: answers]
- **Standard Syntax**: `git branch -d <branch_name>`
- **Aliases**: `git config --global alias.sw switch`
- **Shortcut**: `git merge --abort` resets merge state.
- **Warning**: Do not merge untested feature branches into main.

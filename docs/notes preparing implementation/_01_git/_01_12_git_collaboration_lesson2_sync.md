# Syncing Data — Fetch, Pull, and Push

---

```yaml
lesson_id: GIT-COL-002
lesson_title: "Syncing Data: Fetch, Pull & Push"
subject: Git
course: "Git Fundamentals"
module: Data Syncing
difficulty: "\u2B50\u2B50"
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
- GIT-COL-001 (Remotes & Origin)
tags:
- Git Fetch
- Git Pull
- Git Push
- Syncing
```

---

## 1. Topics Covered [id: topics]
This lesson covers Git's core network synchronization workflows. We analyze how data flows between local repositories and remotes, comparing the mechanics of fetch, pull (fetch + merge), and push.

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - The difference between `git fetch` (inspect metadata) and `git pull` (fetch + merge).
  - How tracking branches establish local/remote mapping links.
- **Skills (What you can do)**:
  - Download remote commits, update branch HEAD positions, publish code, and configure pull rebase workflows.
- **Outcome (Professional application)**:
  - Maintain clean linear histories in team branches by executing safe retrieval integration protocols.

## 2. Definitions & Core Concepts [id: definitions]
Data flow syncing uses three main operations:
- **`git fetch`**: Downloads all objects and refs from the remote repository that are not in your local workspace. It updates remote-tracking pointers under `refs/remotes/origin/` but does not touch your Working Directory or active branches. It is 100% safe.
- **`git pull`**: Performs a `fetch` and immediately merges the retrieved changes into your active local branch. It modifies your Working Directory.
  - Formula: `git pull` = `git fetch` + `git merge`.
- **`git push`**: Uploads your local commit objects and branch pointers to the remote repository.

### Internals: Upstream Tracking Relationships
A local branch can track a remote branch. When you run `git status`, Git compares your branch commit pointer with the remote tracking pointer (e.g. `origin/main`) and reports if you are "ahead" or "behind" commits.

### Terminology & Glossary
- **Fast-Forward Pull**: A pull operation that simply moves the local branch pointer forward because no local commits diverged.
- **Tracking Branch**: A local branch linked directly to a remote branch, enabling simplified syncing.

## 3. Practical Code Examples [id: examples]
### Easy
Download remote updates without modifying working copy files:
```bash
git fetch origin
```

### Medium
Publishing a new local feature branch to GitHub:
```bash
# Create feature branch
git switch -c feature-ui

# Commit changes, then push and set tracking upstream link
git push -u origin feature-ui
```

### Advanced
Force-pushing changes after rewriting history (using force-with-lease for safety):
```bash
git push --force-with-lease origin main
```

## 4. Hands-on Workouts [id: workouts]
### MCQ
- Which command downloads remote changes but does not alter your working tree?
  - A) `git pull`
  - B) `git fetch` (Correct)
  - C) `git push`

### Coding Challenge
- Push a branch named `main` and set its upstream tracking branch.

### Predict the Output
- If you run `git status` after a fetch and you are 2 commits ahead of remote, what does it output?
  - Output: `Your branch is ahead of 'origin/main' by 2 commits.`

### Debugging Task
- Resolve a rejected push error due to remote changes.
  - Answer: Run `git pull` to fetch and merge, resolve conflicts if any, then run `git push`.

### Scenario Question
- A developer wants to see what changes others pushed before merging them. What commands should they run?
  - Answer: `git fetch` followed by `git diff HEAD..origin/main`.

### Hands-on Lab
- Run `git fetch`, then run `git status` to verify if your branch matches remote.

## 5. Workout Answers & Solutions [id: answers]
- **Standard Syntax**: `git push <remote> <branch>`
- **Aliases**: None.
- **Shortcut**: None.
- **Warning**: Never force push to shared default integration branches.

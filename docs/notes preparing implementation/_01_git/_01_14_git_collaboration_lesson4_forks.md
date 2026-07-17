# Upstream and Forking Workflows — Managing community contributions

---

```yaml
lesson_id: GIT-COL-004
lesson_title: "Forking & Upstream Workflows"
subject: Git
course: Git Collaboration
module: Upstream & Forking Workflows
difficulty: "\u2B50\u2B50\u2B50"
time_breakdown:
  reading: 12 min
  exercise: 15 min
  quiz: 10 min
  revision: 5 min
version: '1.0'
last_updated: '2026-07-17'
status: Published
author: Rajasekar
reviewed_by: Admin
prerequisites:
- GIT-COL-003 (Merge Conflicts)
tags:
- Upstream
- Forking
- Sync Fork
- Pull Request
```

---

## 1. Topics Covered [id: topics]
This lesson covers Git's open-source and enterprise scaling workflows. You will learn how to sync your personal forks with upstream repositories, open pull requests, and organize branch collaborations without write access.

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - The purpose of the `upstream` remote alias in open-source fork structures.
  - How Pull Requests (PRs) handle remote branch evaluations.
- **Skills (What you can do)**:
  - Add upstream tracking remotes, pull updates from parent codebases, sync forks, and submit pull requests.
- **Outcome (Professional application)**:
  - Contribute to major open-source repositories and maintain clean local development forks.

## 2. Definitions & Core Concepts [id: definitions]
In a **forking workflow**, you do not push directly to the official codebase. Instead:
1. You fork the target repository on GitHub/GitLab, creating a server-side clone under your account.
2. You clone this fork to your local machine (configured automatically as the `origin` remote).
3. You add the original repository URL as another remote alias named **`upstream`**.
4. You create feature branches locally, pull updates from `upstream` regularly to stay in sync, and push modifications to your `origin` fork.
5. You open a **Pull Request (PR)** or **Merge Request (MR)** requesting the upstream maintainers pull changes from your fork.

### Terminology & Glossary
- **Forking**: Server-side cloning of a repository to your own account namespace.
- **Upstream**: The original official repository from which your fork was derived.
- **Pull Request**: A request to merge your branch changes into the parent codebase.

## 3. Practical Code Examples [id: examples]
### Easy
Add the upstream repository connection:
```bash
git remote add upstream https://github.com/community/app.git
```

### Medium
Syncing your local fork with upstream main:
```bash
# Fetch latest commits from upstream
git fetch upstream

# Switch to local main and merge upstream
git switch main
git merge upstream/main

# Push clean updates to your personal origin fork
git push origin main
```

### Advanced
Rebasing a feature branch on top of upstream changes to avoid merge commits:
```bash
git fetch upstream
git switch feature-ui
git rebase upstream/main
```

## 4. Hands-on Workouts [id: workouts]
### MCQ
- Which remote alias typically points to the original parent repository?
  - A) `origin`
  - B) `upstream` (Correct)
  - C) `source`

### Coding Challenge
- Fetch all remote branches from `upstream`.

### Predict the Output
- What prints if you run `git remote` after setting up origin and upstream?
  - Output:
    ```text
    origin
    upstream
    ```

### Debugging Task
- Resolve a merge conflict in your PR by pulling the latest upstream commits.
  - Answer: `git fetch upstream`, `git merge upstream/main` inside feature branch, resolve conflicts, and run `git push origin feature-branch`.

### Scenario Question
- A developer wants to sync their fork. They fetch upstream. What is the next step?
  - Answer: Switch to local main and merge `upstream/main`.

### Hands-on Lab
- Add a remote named `upstream`, fetch upstream updates, and check tracking status.

## 5. Workout Answers & Solutions [id: answers]
- **Standard Syntax**: `git remote add upstream <url>`
- **Aliases**: None.
- **Shortcut**: None.
- **Warning**: Do not force push to public upstream repositories.

# Rewriting History — Amend, Rebase, and Squash

---

```yaml
lesson_id: GIT-ADV-002
lesson_title: "Rewriting History: Amend, Rebase & Squash"
subject: Git
course: Advanced Git
module: Rewriting History
difficulty: "\u2B50\u2B50\u2B50\u2B50"
time_breakdown:
  reading: 18 min
  exercise: 25 min
  quiz: 15 min
  revision: 5 min
version: '1.0'
last_updated: '2026-07-17'
status: Published
author: Rajasekar
reviewed_by: Admin
prerequisites:
- GIT-ADV-001 (Git Internals)
tags:
- Rebase
- Amend
- Squash
- Reflog
```

---

## 1. Topics Covered [id: topics]
This lesson covers Git history modification workflows. You will learn how to modify the last commit using amend, reorder/edit historical commits using interactive rebase, combine multiple commits using squash, and recover lost commits using the reflog.

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - Why rewriting history creates new commit hashes while leaving old commits orphaned.
  - The Golden Rule of Rebasing: Never rewrite history on public, shared branches.
- **Skills (What you can do)**:
  - Edit commit messages, squash local commits, perform interactive rebases, and recover deleted commits.
- **Outcome (Professional application)**:
  - Clean up development branches before merging into main, keeping project histories readable and linear.

## 2. Definitions & Core Concepts [id: definitions]
Commits in Git are immutable. When you "rewrite" history, you do not modify existing commit objects. Instead, Git creates **new commit objects** with new SHA-1 hashes and moves the branch HEAD pointer to them. The old commits remain in the database as "orphaned" objects until garbage collection removes them.

### Rewriting Tools
- **`git commit --amend`**: Replaces the last commit of the current branch with a new commit containing staged updates and/or an edited commit message.
- **`git rebase -i`**: Interactive rebase opens an edit checklist list allowing you to:
  - `pick`: Keep the commit.
  - `reword`: Keep the commit but edit the message.
  - `edit`: Halt rebase to edit files.
  - `squash`: Combine the commit with the previous one.
  - `drop`: Remove the commit entirely.

### Terminology & Glossary
- **Rebasing**: Replaying a series of commits on top of a new base commit.
- **Squashing**: Combining two or more consecutive commits into a single commit.
- **Orphaned Commit**: A commit that is no longer reachable by any branch pointer or tag reference.

## 3. Practical Code Examples [id: examples]
### Easy
Correct the message of the last commit:
```bash
git commit --amend -m "fix(auth): correct password hash checking algorithm"
```

### Medium
Squash the last 3 commits into a single commit:
```bash
# Open interactive editor menu for last 3 commits
git rebase -i HEAD~3
# Change 'pick' to 'squash' (or 's') for the 2nd and 3rd commits, save and exit.
```

### Advanced
Recovering a commit lost during an interactive rebase:
```bash
# View reflog to locate the commit hash before rebase started
git reflog
# Output shows: HEAD@{4}: rebase -i (start): checkout HEAD~3

# Reset the branch pointer to the state before rebase
git reset --hard HEAD@{5}
```

## 4. Hands-on Workouts [id: workouts]
### MCQ
- Which interactive rebase command combines a commit with the previous one?
  - A) `reword`
  - B) `squash` (Correct)
  - C) `edit`

### Coding Challenge
- Start an interactive rebase for the last 4 commits.

### Predict the Output
- What does `git log` show after a successful rebase squashes 3 commits into 1?
  - Output: A single commit replacing the 3 old commits.

### Debugging Task
- Resolve a conflict during a rebase, then continue.
  - Answer: `git add <file>` followed by `git rebase --continue`.

### Scenario Question
- A developer accidentally ran `git commit --amend` with wrong files. How do they undo this amend?
  - Answer: Inspect `git reflog` and run `git reset --soft HEAD@{1}` to restore files to staging.

### Hands-on Lab
- Make a commit, run `git commit --amend` to change its message, and verify the hash changes.

## 5. Workout Answers & Solutions [id: answers]
- **Standard Syntax**: `git rebase -i HEAD~<N>`
- **Aliases**: None.
- **Shortcut**: None.
- **Warning**: Do not rewrite history on main production branches.

# Lesson 4: Undoing Changes — Reset, Revert, and Restore

---

```yaml
lesson_id: GIT-FND-004
subject: Git
course: Git Fundamentals
module: Basic Local Workflow
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
- GIT-FND-003 (Log and Diff)
tags:
- Git Reset
- Git Revert
- Git Restore
- Undoing Changes
```

---

## 1. Topics Covered [id: topics]
This lesson covers the primary mechanisms for correcting mistakes and rolling back state changes in Git. We explore the differences between resetting branch histories, reverting committed snapshots, and restoring working copy contents.

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - The behavior of soft, mixed, and hard resets on the three Git states.
  - The architectural difference between modifying history (`reset`) and appending history (`revert`).
- **Skills (What you can do)**:
  - Unstage accidentally added files, discard working tree modifications, and safely revert commits.
- **Outcome (Professional application)**:
  - Perform safe rollback actions on collaborative repositories without destroying project history.

## 2. Definitions & Core Concepts [id: definitions]
Correcting errors requires choosing the right tool:
- **`git restore`**: Discards unstaged modifications in your Working Directory or unstages changes from the Staging Area. It operates on *files*, not commits.
- **`git reset`**: Moves the current branch HEAD pointer to a specific commit. It changes *where* the branch points.
  - `--soft`: Moves HEAD. Staging Area and Working Directory remain unchanged.
  - `--mixed` (default): Moves HEAD and updates Staging Area to match. Working Directory remains unchanged.
  - `--hard`: Moves HEAD, updates Staging Area, and overwrites Working Directory. **Destructive operation!**
- **`git revert`**: Appends a *new* commit that applies the exact inverse of the changes from a target commit. It does not rewrite history, making it safe for public repositories.

### Terminology & Glossary
- **Detached HEAD**: A state where HEAD points to a specific commit rather than a branch.
- **Reflog**: A local log tracking every move of the HEAD pointer, allowing recovery of hard-reset commits.

## 3. Practical Code Examples [id: examples]
### Easy
Unstage a file that was accidentally staged:
```bash
git restore --staged app.py
```

### Medium
Discard all local uncommitted edits:
```bash
git restore .
```

### Advanced
Recover from an accidental `git reset --hard HEAD~1` using the reflog database:
```bash
# Locate the lost commit hash in the reflog list
git reflog

# Reset HEAD back to the lost commit
git reset --hard HEAD@{1}
```

## 4. Hands-on Workouts [id: workouts]
### MCQ
- Which reset mode modifies HEAD and Staging Area but leaves the Working Directory untouched?
  - A) `--soft`
  - B) `--mixed` (Correct)
  - C) `--hard`

### Coding Challenge
- Unstage a file named `config.json`.

### Predict the Output
- If you run `git revert HEAD` on a clean directory, what type of commit is created?
  - Output: A new commit with message "Revert '...'".

### Debugging Task
- Recover a lost commit from `git reflog` by returning HEAD to `HEAD@{3}`.
  - Answer: `git reset --hard HEAD@{3}`.

### Scenario Question
- A developer pushed a broken commit to the remote production branch. What command should they use to fix this?
  - Answer: `git revert <commit_hash>` and push.

### Hands-on Lab
- Make changes to `test.py`, run `git restore --staged test.py` (if staged), then `git restore test.py` to discard.

## 5. Workout Answers & Solutions [id: answers]
- **Standard Syntax**: `git reset --hard <hash>`
- **Aliases**: `git config --global alias.unstage "restore --staged"`
- **Shortcut**: Use `git checkout .` as legacy shortcut for `git restore .`.
- **Warning**: Never run `git reset --hard` on public shared branches.

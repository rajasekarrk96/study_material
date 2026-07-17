# Lesson 4: Customization and Automation — Git Hooks and Aliases

---

```yaml
lesson_id: GIT-ADV-004
lesson_title: "Git Customization: Hooks & Aliases"
subject: Git
course: Advanced Git
module: Customization & Hooks
difficulty: "\u2B50\u2B50\u2B50\u2B50"
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
- GIT-ADV-003 (Workspace Helpers)
tags:
- Git Hooks
- Aliases
- Automation
- Config
```

---

## 1. Topics Covered [id: topics]
This lesson covers Git automation and customization. We inspect how to trigger local check hooks (pre-commit, commit-msg, post-merge) to automate code linting, enforce commit format metrics, and configure global alias shortcuts.

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - How Git hooks run as shell scripts in response to version control events.
  - The difference between client-side hooks and server-side hooks.
- **Skills (What you can do)**:
  - Write executable shell script hooks, block invalid commits, and create custom alias shortcuts.
- **Outcome (Professional application)**:
  - Build automated pre-commit linting and commit-message validation pipelines for your team.

## 2. Definitions & Core Concepts [id: definitions]
**Git Hooks** are scripts that run automatically before or after Git executes major actions (like commit, push, merge).
Hooks are stored in `.git/hooks/`. By default, Git populates this directory with sample shell scripts (e.g. `pre-commit.sample`). To activate a hook:
1. Rename the file to remove the `.sample` extension (e.g. `pre-commit`).
2. Make the file executable: `chmod +x .git/hooks/pre-commit`.

### Client-side vs. Server-side Hooks
- **Client-side Hooks**: Run locally on the developer's machine.
  - `pre-commit`: Runs before writing the commit. Used to check code style/linters.
  - `commit-msg`: Runs to validate the commit message format.
  - `pre-push`: Runs before pushing code to remote.
- **Server-side Hooks**: Run on the hosting server (e.g. GitHub/GitLab).
  - `pre-receive`: Runs when push starts; can reject the entire push (e.g. if files contain passwords).
  - `post-receive`: Runs after push is completed; used to notify slack bots or trigger CI pipelines.

### Terminology & Glossary
- **Hook**: An executable script triggered automatically by a Git lifecycle event.
- **Exit Code**: Integer code returned by scripts (0 indicates success; any non-zero value indicates failure).
- **Git Alias**: Custom shortcut mappings for long Git commands.

## 3. Practical Code Examples [id: examples]
### Easy
Create a global alias to format logs in a compact graph tree:
```bash
git config --global alias.l "log --oneline --graph --all"
# Now running 'git l' outputs the full graph tree!
```

### Medium
Creating a simple `pre-commit` hook to block commits containing debugging markers:
```bash
# Create file .git/hooks/pre-commit with contents:
#!/bin/sh
if git diff --cached | grep -q "TODO: debug"; then
    echo "Error: Unfinished debugging todo found!"
    exit 1
fi
exit 0
```
Make the script executable:
```bash
chmod +x .git/hooks/pre-commit
```

### Advanced
Creating a `commit-msg` hook enforcing Conventional Commits formatting:
```bash
# Create file .git/hooks/commit-msg with contents:
#!/bin/bash
MSG_FILE=$1
COMMIT_MSG=$(cat $MSG_FILE)
REGEX="^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?: .+"

if [[ ! $COMMIT_MSG =~ $REGEX ]]; then
    echo "Error: Commit message does not follow Conventional Commits format!"
    echo "Format: feat(auth): add email login"
    exit 1
fi
exit 0
```

## 4. Hands-on Workouts [id: workouts]
### MCQ
- Which flag bypasses commit hook verification checks?
  - A) `--skip-hooks`
  - B) `--no-verify` (Correct)
  - C) `--force`

### Coding Challenge
- Map a global Git alias named `co` to the `checkout` command.

### Predict the Output
- What does `git co main` execute if `alias.co` is mapped to `checkout`?
  - Output: `git checkout main`

### Debugging Task
- Make a pre-commit script executable on a Linux machine.
  - Answer: `chmod +x .git/hooks/pre-commit`.

### Scenario Question
- A developer wants to reject commits if they don't contain a JIRA issue key like `[JIRA-1234]`. What type of hook should they write?
  - Answer: A `commit-msg` hook.

### Hands-on Lab
- Add a global alias `st` for `status`, and test it by running `git st`.

## 5. Workout Answers & Solutions [id: answers]
- **Standard Syntax**: `git config --global alias.<name> "<command>"`
- **Aliases**: `git config --global alias.c "commit -m"`
- **Shortcut**: `--no-verify` skips hooks.
- **Warning**: Do not rely on client-side hooks for security constraints, as developers can bypass them using `--no-verify`. Use server-side hooks instead.

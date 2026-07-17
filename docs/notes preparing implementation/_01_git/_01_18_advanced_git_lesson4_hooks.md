# Customization and Automation — Git Hooks and Aliases

---

```yaml
lesson_id: GIT-ADV-004
lesson_title: "Git Customization: Hooks & Aliases"
subject: Git
course: "Git Fundamentals"
module: "Customization & Hooks"
difficulty: "⭐⭐⭐⭐"
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
- GIT-ADV-003 (Workspace Helpers: Stash, Bisect & Worktree)
tags:
- Git Hooks
- Aliases
- Automation
- Config
```

---

## 1. Topics Covered [id: topics]
- Git hooks
- Client-side hooks
- Server-side hooks
- Git aliases
- Automation workflows

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - How Git hooks run executable scripts at specific event gates in the developer lifecycle.
  - The architectural difference between local client-side hooks and centralized server-side hooks.
  - The role of branch protection rules vs custom server hooks on hosting services.
- **Skills (What you can do)**:
  - Create, test, and distribute executable hook scripts.
  - Configure global and local command alias overrides.
- **Professional Outcome**:
  - Enforce clean formatting, code validation, and ticket metadata standards across developer teams automatically.

---

## 2. Definitions & Core Concepts [id: definitions]

### Git Hook Lifecycle Diagrams

#### 1. Local Commit Lifecycle
```text
  git commit ──► [pre-commit] ──► [commit-msg] ──► Commit Created ──► [post-commit]
```

#### 2. Remote Push Lifecycle
```text
  git push ──► [pre-push] ──► Remote Server ──► [pre-receive] ──► [update] ──► [post-receive]
```

---

### Client-side vs. Server-side Hooks
| Client-side Hooks | Server-side Hooks |
|---|---|
| Run locally on the developer's workstation. | Run remotely on the hosting Git server. |
| Can be bypassed by the developer using `--no-verify`. | Cannot be bypassed by client configurations. |
| Primarily used for developer formatting and linting. | Primarily used for access control and CI checks. |

---

### Why Hooks Exist
- **Reduce Human Error**: Standardize code linters and checkers automatically before commits are saved.
- **Enforce Team Rules**: Ensure commit messages include issue tracking metadata tags.
- **Prevent Bad Commits**: Prevent developers from committing secrets, temporary markers, or failing tests.
- **Automate Workflows**: Trigger local build scripts or post-commit build runners.

---

### Git Hook Trigger Reference
| Hook | Execution Gate | Typical Use Case |
|---|---|---|
| **`pre-commit`** | Runs before commit messages are written. | Code formatting and syntax checks. |
| **`prepare-commit-msg`** | Runs before commit message editor launches. | Autocomplete messages with branch names. |
| **`commit-msg`** | Runs after message is written to validate text. | Enforce conventional commit formats. |
| **`post-commit`** | Runs immediately after a commit completes. | Trigger local notifications or backups. |
| **`pre-rebase`** | Runs before history rewriting begins. | Block rebases on protected branches. |
| **`pre-push`** | Runs before objects are sent to the remote. | Run test suites before publishing branches. |
| **`pre-receive`** | Runs before the server updates remote refs. | Reject pushes containing credentials. |
| **`post-receive`** | Runs after the server accepts push objects. | Trigger deployment pipelines or Slack bots. |

---

### Modern SaaS Hosting Realities
> [!IMPORTANT]
> Cloud hosting platforms like GitHub, GitLab, and Bitbucket **do not allow custom server-side Git hooks** on their shared SaaS plans for security reasons. Instead, teams enforce integration checks using **Branch Protection Rules**, **Required Status Checks**, and **CI/CD Pipelines**. Custom server-side hooks are only available on self-managed servers.

---

## 3. Practical Code Examples [id: examples]

### Hook & Alias Cheat Sheet
| Command | Purpose |
|---|---|
| **`chmod +x .git/hooks/pre-commit`** | Makes a hook script executable. |
| **`git config core.hooksPath .githooks`** | Changes the hook directory to share scripts with the team. |
| **`git config --global alias.st status`** | Maps `git st` to `git status`. |
| **`git config --global --get-regexp '^alias\.'`** | Lists all configured Git aliases. |

### Common Git Aliases
```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.last "log -1"
git config --global alias.graph "log --graph --oneline --all"
```
*(Note: Although `checkout` is widely mapped in aliases, modern Git uses `git switch` for branch changes and `git restore` for resetting files).*

### Example A: Enterprise Pre-commit Pipeline
```text
  Developer Commit ──► [pre-commit] ──► Run Formatter ──► Run Linter ──► Validate Tests ──► Commit Success
```

### Example B: Portable pre-commit hook (POSIX sh)
To write a pre-commit hook that blocks commits containing temporary debug lines:
```bash
#!/bin/sh
# Stored in .git/hooks/pre-commit
# Verify that staged diffs do not contain TODO: debug markers
if git diff --cached | grep -q "TODO: debug"; then
    echo "Error: Unfinished debugging 'TODO: debug' found!"
    exit 1
fi
exit 0
```
*(Note: To activate hooks, you must manually rename the script from `.sample` and run `chmod +x` to make it executable. Git does not rename sample scripts automatically).*

### Example C: Robust commit-msg message parsing (Bash)
```bash
#!/bin/bash
# Stored in .git/hooks/commit-msg
MSG_FILE="$1"
COMMIT_MSG=$(cat "$MSG_FILE")
REGEX="^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?: .+"

# Double brackets [[ ... ]] are Bash-specific.
if [[ ! "$COMMIT_MSG" =~ $REGEX ]]; then
    echo "Error: Message does not follow Conventional Commits formatting!"
    exit 1
fi
```

---

## 4. Hands-on Workouts [id: workouts]

### MCQ
- Which flag bypasses local `pre-commit` and `commit-msg` verification checks?
  - A) `--force`
  - B) `--no-verify` (Correct)
  - C) `--skip-tests`

### Hook Distribution Strategies
By default, the `.git/hooks/` directory is not tracked by Git, making it difficult to share hooks across a team. Standard distribution options:
- **`core.hooksPath`**: Configure Git to use a version-controlled folder in the repository:
  `git config core.hooksPath .githooks`
- **Hook Managers**: Use automated managers (like Husky for Node.js projects) to configure hooks during dependency installations.

---

## 5. Workout Answers & Solutions [id: answers]

### Common Mistakes
- **Not Executable**: Forgetting to run `chmod +x` on the hook file, causing Git to ignore the script.
- **Client Bypass**: Relying on client-side hooks to enforce security (e.g. blocking API keys). Since developers can bypass client checks using `--no-verify`, **critical validations must run on the server or in CI/CD**.
- **Portability**: Writing Bash-specific scripts using `[[ ... ]]` on systems that only support POSIX `/bin/sh`, causing execution errors.

### Enterprise Best Practices
1. **Keep Hooks Fast**: Ensure hook checks (like linters) compile in milliseconds so they do not interrupt developer output speeds.
2. **Double Enforcement**: Use client-side hooks for developer convenience, but replicate strict security checks on your CI/CD server.
3. **Automate Setup**: Include hook configurations inside your project bootstrap script.

### Key Takeaways
- Git hooks automate checks before and after repository events.
- Client-side hooks run locally; server-side hooks validate remote transfers.
- SaaS platforms use branch protections and CI/CD instead of custom server hooks.
- Version-control shared hooks by configuring `core.hooksPath`.
- Git aliases save time and reduce command line fatigue.

# Local Workflow: Init, Stage & Commit

---

```yaml
lesson_id: "GIT-FND-002"
lesson_title: "Local Workflow: Init, Stage & Commit"
subject: "Git"
course: "Git Fundamentals"
module: "Git Foundations"
difficulty: "⭐"
time_breakdown:
  reading: "15 min"
  exercise: "20 min"
  quiz: "10 min"
  revision: "5 min"
version: "1.2"
last_updated: "2026-07-17"
status: "Published"
author: "Rajasekar"
reviewed_by: "Admin"
prerequisites:
  - "GIT-FND-001a (Version Control History)"
tags:
  - "Git Init"
  - "Git Config"
  - "Git Status"
  - "Git Clone"
```

---

## 1. Topics Covered [id: topics]

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - Git configuration levels (Local, Global, System) and their precedence values.
  - The differences between repository initialization and cloning.
  - How Git tracks, stages, commits, and ignores local workspace files.
- **Skills (What you can do)**:
  - Configure global/local developer identities.
  - Create repositories, pull remote directories, and write custom `.gitignore` filters.
  - Interrogate staging environments using advanced status command forms.
- **Professional Outcome**:
  - Configure repositories correctly and prevent sensitive or garbage files from entering version history.

### Local Git Workflow Flowchart
```text
                         Local Git Workflow

      Configure Git Identity (--global user.name)
                         │
                         ▼
        git init (New)  or  git clone (Copy)
                         │
                         ▼
               Create / Modify Files
                         │
                         ▼
             git status (Check changes)
                         │
                         ▼
              git add (Stage files)
                         │
                         ▼
            git commit (Save snapshots)
```

---

## 2. Definitions & Core Concepts [id: definitions]

### Git Configuration Levels & Precedence
Git configs exist across three layered scopes:
- **System**: Applied to all users and all repositories on the machine (stored in `/etc/gitconfig`).
- **Global**: Applied to the current user's profile across all their repositories (stored in `~/.gitconfig`).
- **Local**: Limited strictly to the current active repository directory (stored in `.git/config`).

```text
                  Configuration Precedence
                  
      Local (.git/config)              <-- [Highest Priority]
              ▲
      Global (~/.gitconfig)
              ▲
      System (/etc/gitconfig)          <-- [Lowest Priority]
```
> [!NOTE]
> If the same setting exists in multiple locations, Git uses the **Local** value first, then **Global**, then **System**.

### git init vs. git clone
| `git init` | `git clone` |
|---|---|
| Creates a brand-new empty local repository. | Copies an existing remote repository to local disk. |
| Starts with no commit history. | Downloads complete history, commits, and logs. |
| Initializes an empty project folder. | Downloads all existing project files and branches. |
| No remote origin configured initially. | Remote configuration is mapped automatically. |
| Used when starting new custom projects. | Used to join and contribute to active team repositories. |

### Interpreting Short Status Outputs (`git status -s`)
The short status command formats output into a two-column status code prefix:
- The **first column** indicates the status of the Staging Area.
- The **second column** indicates the status of the Working Directory.

| Output Code | Meaning |
|---|---|
| **`??`** | Untracked file (never added to Git). |
| **` M`** | Modified in Working Directory but not yet staged. |
| **`M `** | Staged modifications ready for the next commit. |
| **`A `** | Added to the staging area index. |
| **`D `** | Deleted file. |
| **`R `** | Renamed file. |
| **`MM`** | Modified in both the staging area and the working directory since staging. |

### The Rules of `.gitignore`
`.gitignore` is a text file instructing Git to ignore untracked patterns.
Common pattern filters:
```text
# Ignore logs
*.log

# Ignore temporary files
*.tmp

# Ignore Python compiler caches
__pycache__/

# Ignore environment config secrets
.env

# Ignore build output folders
build/

# Ignore local IDE configurations
.vscode/
```

> [!IMPORTANT]
> `.gitignore` only affects **untracked** files. If a file has already been committed, adding it to `.gitignore` does not stop Git from tracking it. To stop tracking a committed file without deleting it from disk, run:
> `git rm --cached secrets.env`

### Repository folder layout after `git init`
```text
project/
├── app.py
├── README.md
├── .gitignore
└── .git/      # Hidden directory containing the entire version database
```

---

## 3. Practical Code Examples [id: examples]

### Example A: Identity Configurations & Inspections
- **Code**:
  ```bash
  # Configure user identity
  git config --global user.name "yourname"
  git config --global user.email "your.email@example.com"
  
  # Inspect configuration scopes
  git config --global --list
  git config --local --list
  git config user.name
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git config user.name                                 │
  │ yourname                                               │
  └────────────────────────────────────────────────────────┘
  ```

### Example B: Cloning over Network (HTTPS/SSH)
- **Code**:
  ```bash
  git clone https://github.com/yourname/demo-repo.git
  ```
  *(Note: Cloning private repositories over HTTPS requires authentication via a Personal Access Token (PAT) or Git Credential Manager)*

### Example C: Untracking a committed file
- **Code**:
  ```bash
  # Stop tracking secrets.env but preserve the file on disk
  git rm --cached secrets.env
  echo "secrets.env" >> .gitignore
  git status -s
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git status -s                                        │
  │  D secrets.env                                         │
  │  M .gitignore                                          │
  └────────────────────────────────────────────────────────┘
  ```

---

## 4. Hands-on Workouts [id: workouts]

### Complete end-to-end Local Workflow Challenge
- **Workout**:
  1. Create a directory named `demo-run` and initialize it.
  2. Configure your local username to `"Developer"` and email to `"dev@example.com"`.
  3. Create `app.py` containing `print("demo")`.
  4. Create `notes.tmp` containing `temp`.
  5. Configure `.gitignore` to filter out `.tmp` files.
  6. Stage `app.py`, commit it with a descriptive message, and run `git log --oneline` to verify.

### Solutions to Workflow Challenge
- **Commands**:
  ```bash
  mkdir demo-run
  cd demo-run
  git init
  git config --local user.name "Developer"
  git config --local user.email "dev@example.com"
  echo "print('demo')" > app.py
  echo "temp" > notes.tmp
  echo "*.tmp" > .gitignore
  git add app.py .gitignore
  git commit -m "feat: initialize core print execution script"
  git log --oneline
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git log --oneline                                    │
  │ e7a8b9c feat: initialize core print execution script   │
  └────────────────────────────────────────────────────────┘
  ```

---

## 5. Workout Answers & Solutions [id: answers]

### Commit Message Best Practices
- **Good (Descriptive, imperative mood)**:
  - `feat: add user login validation controller`
  - `fix: correct payment calculation rounding bug`
  - `docs: update README installation guide`
- **Bad (Vague, non-descriptive)**:
  - `update`
  - `changes`
  - `final version`
  - `bugfix`

### Common Beginner Mistakes
- **Mistake**: Forgetting to configure `user.name` and `user.email` before committing.
  - *Result*: Git tries to guess from local machine usernames, producing messy commit logs.
- **Mistake**: Committing credentials or settings files like `.env` or `.vscode/`.
  - *Fix*: Create your `.gitignore` file **before** running your first `git add .` command.

### Enterprise Best Practices
1. **Config First**: Always configure your identity before creating repository snapshots.
2. **Atomic Scope**: Commit only related changes. If you fix two unrelated bugs, create two commits.
3. **Double Check**: Inspect `git status -s` and run `git config --local --list` to verify local targets before pushing.

### Key Takeaways
- Git configurations prioritize Local settings over Global and System profiles.
- `git init` builds new local roots; `git clone` copies existing remote project structures.
- `git status -s` delivers a short, two-character summary of modified and staged files.
- `.gitignore` ignores untracked files; committed files must be cleared using `git rm --cached`.
- High-quality, semantic commit messages keep team project versions traceable and debuggable.

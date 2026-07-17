# Git Architecture & Three States

---

```yaml
lesson_id: GIT-FND-001
lesson_title: "Git Architecture & Three States"
subject: Git
course: "Git Fundamentals"
module: "Git Foundations"
difficulty: "⭐"
time_breakdown:
  reading: 15 min
  exercise: 20 min
  quiz: 10 min
  revision: 5 min
version: '1.2'
last_updated: '2026-07-17'
status: Published
author: Learning OS Author
reviewed_by: Admin
prerequisites:
- Basic CLI navigation
tags:
- Git
- Staging
- Commit
- HEAD
```

---

## 1. Topics Covered [id: topics]
This lesson introduces the core version control model of Git. Rather than just memorizing commands, we explore how Git manages files across three distinct local environments and how it interfaces with remote servers.

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - The mechanical boundaries of the Working Directory, Staging Area, and Local Repository.
  - The lifecycle transitions of files between states and how Git tracks snapshots.
- **Skills (What you can do)**:
  - Initialize repositories, selectively stage files, trace differences, and write structured commit records.
- **Outcome (Professional application)**:
  - Organize commits atomically and maintain a stable repository structure on collaborative team environments.

---

## 2. Definitions & Core Concepts [id: definitions]

### The Visual Flow Diagram
```text
                          Git Three States

       Working Directory
     (Files you are editing)
               │
               │ git add
               ▼
        Staging Area (Index)
    (Files selected for commit)
               │
               │ git commit
               ▼
        Local Repository (.git)
    (Permanent snapshot history)
               │
               │ git push
               ▼
       Remote Repository (GitHub/GitLab)
```

### Git File States & Environments
- **Working Directory**: The actual folder directory on your computer where you write and edit code.
- **Staging Area (Index)**: A binary cached index file registering changes slated for the next commit snapshot.
- **Local Repository**: The localized historical database stored inside your `.git/` folder containing permanent, immutable commit records.
- **Remote Repository**: External hosting platforms (GitHub, GitLab, Bitbucket) storing and sharing your repository commits over the network.

| File State | Meaning |
|---|---|
| **Untracked** | The file is in the working directory but has never been tracked by Git. |
| **Modified** | The file contains changes made since the last commit snapshot. |
| **Staged** | The changes have been added to the index and are prepared for the next commit. |
| **Committed** | The file has been safely and permanently stored inside the local repository history. |

> [!NOTE]
> Git itself manages three local states (Working Directory, Staging Area, and Local Repository). GitHub, GitLab, and Bitbucket provide a **Remote Repository**, which stores commits outside your computer. Remote repositories are introduced in detail in a later lesson.

### WHY the Staging Area Exists
The staging area allows developers to **build commits intentionally**. Instead of committing all local changes at once, you can modify ten files but stage only two related files, creating small, meaningful commits that are easier to review, test, and revert.

### Git's Snapshot Model
Unlike traditional version control systems (like SVN) that record only differences (deltas), Git records a **complete snapshot** of the project for every commit. Files that have not changed are efficiently reused through internal object references (pointing to existing blobs), minimizing storage requirements and preventing redundant file copies.

### Real .git Folder Structure
When you run `git init`, Git creates a hidden directory named `.git/` containing the following core elements:
```text
project/
│
├── app.py
├── README.md
└── .git/
    ├── HEAD      # Reference pointer to the currently active branch
    ├── config    # Repository-specific configuration options
    ├── index     # Binary file staging area cache database
    ├── objects/  # Content database containing Blobs, Trees, Commits, and Tags
    ├── refs/     # References pointing to local and remote branches and tags
    └── logs/     # Historical logs tracking HEAD revisions (Reflog database)
```

> [!WARNING]
> The `.git` folder contains the entire repository database. Deleting it permanently removes the entire Git history from the project.

### Internal Architecture
Historically, Git used SHA-1 cryptographic hashes (40-character hexadecimal strings) for object identification. Modern Git versions also support SHA-256 repositories, although SHA-1 remains the most common in existing projects.

---

## 3. Practical Code Examples [id: examples]

### Example A: Basic File Lifecycle Simulation
- **Code**:
  ```bash
  # Initialize repository
  git init
  
  # Create a file (State: Untracked)
  echo "import math" > app.py
  
  # Stage the file (State: Staged)
  git add app.py
  
  # Commit the file (State: Committed)
  git commit -m "Add core math script"
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git status -s                                        │
  │  (Clean status, file is successfully committed)        │
  └────────────────────────────────────────────────────────┘
  ```

### Example B: Staging Re-edits & Selective Checks
- **Code**:
  ```bash
  echo "print('App running')" >> app.py
  git status
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git status                                           │
  │ On branch main                                         │
  │ Changes not staged for commit:                         │
  │   modified:   app.py                                   │
  └────────────────────────────────────────────────────────┘
  ```

### Example C: Useful Companion Commands
- **Code**:
  ```bash
  # Verify staged files comparison
  git diff --cached
  
  # Print simplified history logs
  git log --oneline
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git log --oneline                                    │
  │ a1b2c3d Add core math script                           │
  └────────────────────────────────────────────────────────┘
  ```

---

## 4. Hands-on Workouts [id: workouts]

### MCQ
- What state represents a file that Git has never seen before?
  - A) Modified
  - B) Untracked (Correct)
  - C) Staged

### Coding Challenge
- Initialize a local git repository. Create a file `notes.txt`. Modify `notes.txt` to contain `"Hello"`. Check `git status` output.

### Scenario Exercise: Selective Staging
- Create two files in a repository: `app.py` and `notes.txt`. Modify both files. Stage only `app.py` and commit it. Verify that `notes.txt` remains unstaged in your working directory.

### Solutions to Scenario Exercise:
- **Commands**:
  ```bash
  git init
  echo "import os" > app.py
  echo "ideas" > notes.txt
  git add app.py
  git commit -m "Stage only app.py"
  git status -s
  ```
- **Console Output**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ ?? notes.txt                                           │
  └────────────────────────────────────────────────────────┘
  ```
  *(Notice that `notes.txt` remains untracked/unstaged, while `app.py` is safely committed)*

---

## 5. Workout Answers & Solutions [id: answers]

### Common Beginner Mistakes
- **Mistake**: Editing a file after running `git add` and committing directly.
  - *Fix*: You must run `git add` again to stage the new edits, or else they will not be committed!
- **Mistake**: Running `git init` inside an existing Git project.
  - *Fix*: `git init` should be run only once at the root of a project.

### Enterprise Best Practice
- **Atomic Commits**: Stage only related changes. Avoid large "everything" commits.
- **Review Status**: Run `git status` and `git diff --cached` before every commit to review what is staged.

### Memory Tip
- Remember the sequence: **Edit $\rightarrow$ Stage $\rightarrow$ Commit $\rightarrow$ Push** (**ESCP**).

### Key Takeaways
1. Git manages file transitions across the **Working Directory**, **Staging Area**, and **Local Repository**.
2. **`git add`** copies changes to the staging index; **`git commit`** seals them into a snapshot object.
3. Cryptographic hashes index immutable repository content databases.
4. Small, modular commits make codebase histories easier to debug and revert.

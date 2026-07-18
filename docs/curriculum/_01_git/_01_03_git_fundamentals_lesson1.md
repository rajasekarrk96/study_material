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
last_updated: '2026-07-18'
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

### Git File States & Environments
Git does not track files continuously; instead, it observes files across three local environments:
* **Working Directory**: The actual folder directory on your computer where you write and edit code.
* **Staging Area (Index)**: A binary cached index file registering changes slated for the next commit snapshot.
* **Local Repository**: The localized historical database stored inside your `.git/` folder containing permanent, immutable commit records.

### The Lifecycle of a File
As you work, your files transition between four distinct states:
1. **Untracked**: The file exists in your working directory, but Git has never recorded it. It is ignored by Git's snapshots.
2. **Modified**: The file is tracked, and you have edited it since the last commit, but the new edits are not yet staged.
3. **Staged**: You have marked the file changes to be included in the next snapshot.
4. **Committed**: Git has safely and permanently stored the snapshot in the `.git/` database.

### The State Transition Flow Connected to `git status`

```text
  Create app.py
        │
        ▼
  Working Directory
  State: Untracked
  git status ──► Tells you: "Untracked files: app.py"
        │
        │ git add app.py
        ▼
  Staging Area (Index)
  State: Staged
  git status ──► Tells you: "Changes to be committed: app.py"
        │
        │ git commit -m "Initial commit"
        ▼
  Local Repository
  State: Committed
  git status ──► Tells you: "nothing to commit, working tree clean"
```

> [!TIP]
> **Pro Tip:** If you're ever unsure what's happening in your repository, run `git status`. It is a developer's primary diagnostic tool, telling you:
> - Which branch you are currently on
> - Which files are untracked (never checked by Git)
> - Which files are modified (edited since last commit)
> - Which changes are staged (ready to commit)
> - Whether your working tree is clean

> [!NOTE]
> **Why the Staging Area Exists:** The staging area acts as a draft room. Instead of saving all changed files at once, you can choose exactly which files go into which commit, making history clean and easy to revert.

---

## 3. Practical Code Examples [id: examples]

### Step-by-Step Lab 1: First-Time Git Setup (Run Only Once)
Before creating your first commit, you must configure your Git identity. Git stores your name and email in every commit to identify the author.

* **Learning Objective**: Configure Git global user identity variables.
* **Prerequisites**: Git installed on your computer.

#### Command
```bash
git config --global user.name "John Doe"
git config --global user.email "john@example.com"
```
*(Replace "John Doe" and "john@example.com" with your actual name and email)*

#### Verification
To confirm Git saved your identity variables correctly:
```bash
git config --global --list
```

#### Expected Output
```text
user.name=John Doe
user.email=john@example.com
```

#### Explanation & Resulting State
* **What Happened**: Git wrote these settings to a global configuration file on your computer.
* **Resulting State**: Identity registered globally. You will not need to run these commands again on this computer.

> [!WARNING]
> **Common Error (Author identity unknown):** If you skip this configuration step and try to run `git commit`, Git will throw a fatal error. If this happens, run the two configuration commands above to resolve the error.

---

### Step-by-Step Lab 2: Initializing and First Staging
We will create a brand new local repository and track our first file.

* **Learning Objective**: Initialize a repository and stage a new file.
* **Prerequisites**: Global configuration complete (Lab 1).

#### Step 1: Initialize a repository
To turn any local directory into a Git repository:
```bash
git init
```
* **Expected Output**:
  ```text
  Initialized empty Git repository in /path/to/project/.git/
  ```
* **Explanation**: Git created a hidden folder named `.git` inside your folder. This hidden folder acts as the repository database.
* **Resulting State**: Empty Local Repository initialized.

#### Step 2: Create a file
Now we will create a file. In your terminal, run:
```bash
echo "import math" > app.py
```
* **Explanation**: The `echo "content" > filename` syntax means: *Create a file named app.py and write "import math" inside it*.
* **Resulting State**: File `app.py` created in the **Working Directory**.
* **File State**: **Untracked**.

#### Step 3: Check repository status
Let's see what Git detects:
```bash
git status
```
* **Expected Output**:
  ```text
  No commits yet
  
  Untracked files:
    (use "git add <file>..." to include in what will be committed)
          app.py
  
  nothing added to commit but untracked files present (use "git add" to track)
  ```
* **Explanation**: Git tells us it detects `app.py` in the Working Directory, but is not tracking it yet.

#### Step 4: Stage the file
To select `app.py` for our next snapshot, run:
```bash
git add app.py
```
* **Expected Output**: *(None - success is silent)*
* **Explanation**: Git copied `app.py` to the binary Staging Area (Index) cache.
* **File State**: **Staged**.

#### Step 5: Check repository status again
Let's verify that the file was staged:
```bash
git status
```
* **Expected Output**:
  ```text
  No commits yet
  
  Changes to be committed:
    (use "git rm --cached <file>..." to unstage)
          new file:   app.py
  ```
* **Explanation**: The file has moved from Untracked to Staged (listed under "Changes to be committed").

---

### Step-by-Step Lab 3: Creating Your First Commit
We will now seal the staged changes into a permanent snapshot.

* **Learning Objective**: Commit staged files and examine repository history.
* **Prerequisites**: Lab 2 complete (`app.py` staged).

#### Step 1: Commit changes
To commit the staged file:
```bash
git commit -m "Initial commit with math script"
```
* **Expected Output**:
  ```text
  [main (root-commit) a1b2c3d] Initial commit with math script
   1 file changed, 1 insertion(+)
   create mode 100644 app.py
  ```
* **Explanation**: Git created a tree object snapshot containing `app.py` and wrapped it in a commit object containing your author details and commit message.
* **File State**: **Committed**.

#### Step 2: Check repository status
```bash
git status
```
* **Expected Output**:
  ```text
  On branch main
  nothing to commit, working tree clean
  ```
* **Explanation**: Since all changes in the Working Directory are committed and match the Local Repository, Git reports a clean working tree.

#### Step 3: View history log
To print a history list of commits:
```bash
git log --oneline
```
* **Expected Output**:
  ```text
  a1b2c3d Initial commit with math script
  ```
* **Explanation**: Git lists the 7-character commit ID hash and the message.

---

## 4. Hands-on Workouts [id: workouts]

### Checkpoint Questions
1. Which command moves changes from the Working Directory to the Staging Area?
2. What hidden folder does Git create to store its snapshot database?
3. If you run `git add app.py`, then make a new edit to `app.py`, what status will the file show when running `git status`?

---

### Try It Yourself Exercise: Selective Staging
* **Goal**: Modify two files, but stage and commit only one of them.
* **Steps**:
  1. Create `README.md` containing `Documentation`.
  2. Create `settings.json` containing `{"theme": "dark"}`.
  3. Stage only `README.md`.
  4. Commit with message `"Add README documentation"`.
  5. Check `git status` to verify `settings.json` remains untracked.

---

## 5. Workout Answers & Solutions [id: answers]

### Checkpoint Answers
1. `git add <filename>`
2. The `.git` folder.
3. The file will be in **two states simultaneously**: Staged (containing the changes made before the `git add` command) and Modified (containing the new edits made *after* the `git add` command). You must run `git add app.py` again to stage the new edits!

---

### Solution to Try It Yourself Exercise
Run these commands in order:
```bash
echo "Documentation" > README.md
echo '{"theme": "dark"}' > settings.json
git add README.md
git commit -m "Add README documentation"
git status
```
* **Expected Verification Output**:
  ```text
  Untracked files:
    (use "git add <file>..." to include in what will be committed)
          settings.json
  
  nothing added to commit but untracked files present (use "git add" to track)
  ```
*(Notice that `README.md` is committed, while `settings.json` remains untracked/unstaged)*

---

### Common Beginner Mistakes
* **Mistake: Editing a file after `git add` and committing directly.**
  * *Fix*: Always run `git add` *after* your final file edits. Committing only saves what was staged at the moment of the commit.
* **Mistake: Initializing a repo inside a repo.**
  * *Fix*: Avoid running `git init` inside subfolders. Run it only once at the root directory of your project. If you accidentally initialize in a subfolder, remove the hidden `.git` folder by running `rm -rf .git`.

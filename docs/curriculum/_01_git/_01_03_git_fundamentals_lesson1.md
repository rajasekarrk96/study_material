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
version: '1.3'
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
Welcome to your very first Git lesson! This lesson introduces the core model of version control. Rather than copying commands blindly, you will understand how Git operates behind the scenes, how it stamps your identity onto every change, and how to verify your project's state.

### Learning Outcomes
- **Knowledge**: Understand the boundaries of the Working Directory, Staging Area, and Local Repository, and why Git requires your identity.
- **Skills**: Configure your default author profile, initialize local repositories, stage files, read status outputs, and record commits.
- **Outcome**: Confidently record project snapshots and inspect repository history.

---

## 2. Definitions & Core Concepts [id: definitions]

### Git's Three States (Conceptual Model)
Before running any commands, let's understand the three local spaces where files live on your computer:
* **Working Directory**: The actual folder directory on your computer where you write and edit code.
* **Staging Area (Index)**: A draft folder registry cache where you place files you want to include in your next snapshot.
* **Local Repository**: Git's permanent historical database stored inside your `.git/` folder containing completed commit records.

### The Visual Flow Diagram
Every file in a Git project transitions through these environments as you work:

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

> [!NOTE]
> **Why the Staging Area Exists:** Think of it as a draft layout. If you edit 10 files but only want to save changes for 2 files, you can selectively stage only those 2. This creates clean, specific snapshots (commits) instead of a massive, messy save.

### Why Git Needs Your Identity
Before you create your first repository, Git needs to know who you are. Why? Because Git is designed for collaboration. Every single commit you make permanent stores your identity as the author.

An actual Git commit record looks like this:
```text
Commit ID: 8ed7fc512030489...
Author: Rajasekar <rajasekar@gmail.com>
Date: Sat Jul 18 15:45:00 2026
Message: Initial commit
```
Git isn't asking for your email to send you spam or register you for GitHub; it is because your name and email are cryptographically stamped into the history database of every commit.

### git config Explained
To configure your identity, we use the `git config` command. Here is a breakdown of what this command means:

| Command part | Meaning |
|---|---|
| **`git`** | Start the Git program in your terminal. |
| **`config`** | Sub-command to view or modify your settings. |
| **`--global`** | Flag applying this configuration to all projects on your computer. |
| **`user.name`** | The setting variable representing your name. |
| **`user.email`** | The setting variable representing your email. |

### Step 1: Configure Your Identity (Run Only Once)
Open your terminal and run the following commands in order:
```bash
git config --global user.name "John Doe"
git config --global user.email "john@example.com"
```
*(Make sure to replace "John Doe" and "john@example.com" with your actual name and email)*

### Step 2: Verify Your Identity Settings
To check that Git saved your details correctly:
```bash
git config --global --list
```
**Expected Output:**
```text
user.name=John Doe
user.email=john@example.com
```

### Brief Note: Starting Workflows
There are two common ways to start a Git project:
1. **Create a local repository** (`git init`) on your computer.
2. **Clone an existing repository** (`git clone`) from GitHub.

In this lesson, we will focus exclusively on the local-first workflow. Remote repositories (like GitHub) and the cloning process are covered in full in the **Remote Collaboration** module.

---

## 3. Practical Code Examples [id: examples]

Let's put theory into practice. We will build a repository step-by-step and watch a file transition through the three states.

### Step-by-Step Lab: Create Your First Repository and Commit

#### Step 1: Create a folder and navigate inside
We must create a directory for our project and enter it. Run these separate commands:
```bash
mkdir MyProject
cd MyProject
```
* **Objective:** Establish a folder workspace.
* **Resulting State:** Clean working folder. Not a repository yet.

#### Step 2: Initialize the repository
To start tracking this project with Git:
```bash
git init
```
* **Expected Output:**
  ```text
  Initialized empty Git repository in /path/to/MyProject/.git/
  ```
* **Explanation:** Git created a hidden folder named `.git` inside your directory to act as the snapshot database.
* **Resulting State:** Empty local repository.

#### Step 3: Check initial status
Let's see what Git reports:
```bash
git status
```
* **Expected Output:**
  ```text
  No commits yet
  nothing to commit (create/copy files and use "git add" to track)
  ```
* **Explanation:** Git is active but has no files to track.

#### Step 4: Create a file
Let's create a code file using the terminal echo command:
```bash
echo "import math" > app.py
```
* **Explanation:** This creates a file named `app.py` in your folder and writes the line `import math` inside it.
* **Resulting State:** File exists in the **Working Directory**.
* **File State:** **Untracked**.

#### Step 5: Verify status of the untracked file
```bash
git status
```
* **Expected Output:**
  ```text
  No commits yet
  
  Untracked files:
    (use "git add <file>..." to include in what will be committed)
          app.py
  
  nothing added to commit but untracked files present (use "git add" to track)
  ```
* **Explanation:** Git notices `app.py` is in the Working Directory, but is not tracking it.

#### Step 6: Stage the file
To prepare the file for our next snapshot:
```bash
git add app.py
```
* **Explanation:** Git copies the current state of `app.py` to the binary Staging Area (Index) cache.
* **File State:** **Staged**.

#### Step 7: Verify status of the staged file
```bash
git status
```
* **Expected Output:**
  ```text
  No commits yet
  
  Changes to be committed:
    (use "git rm --cached <file>..." to unstage)
          new file:   app.py
  ```
* **Explanation:** The file has moved to the Staging Area (ready to commit).

#### Step 8: Commit the changes
To permanently seal this snapshot:
```bash
git commit -m "Initial commit with math script"
```
* **Expected Output:**
  ```text
  [main (root-commit) a1b2c3d] Initial commit with math script
   1 file changed, 1 insertion(+)
   create mode 100644 app.py
  ```
* **Explanation:** Git writes a permanent tree snapshot block containing `app.py` stamped with your author identity.
* **File State:** **Committed**.

#### Step 9: Verify status after commit
```bash
git status
```
* **Expected Output:**
  ```text
  On branch main
  nothing to commit, working tree clean
  ```
* **Explanation:** Your Working Directory now matches the Local Repository history exactly.

#### Step 10: View the history log
```bash
git log --oneline
```
* **Expected Output:**
  ```text
  a1b2c3d Initial commit with math script
  ```
* **Explanation:** Git lists the unique commit ID hash and message representing your saved snapshot.

---

## 4. Hands-on Workouts [id: workouts]

### Checkpoint Questions
1. Why does Git require you to configure your name and email before committing?
2. If you run `git init` inside a folder, what hidden directory is created?
3. If you edit a file after running `git add`, does the new edit get saved when you run `git commit`?

---

### Try It Yourself Exercise: Selective Staging
* **Goal:** Modify two files, but stage and commit only one of them.
* **Steps:**
  1. Create a file `README.md` containing `Documentation`.
  2. Create a file `settings.json` containing `{"theme": "dark"}`.
  3. Stage only `README.md`.
  4. Commit with message `"Add README documentation"`.
  5. Check `git status` to verify `settings.json` remains untracked.

---

## 5. Workout Answers & Solutions [id: answers]

### Checkpoint Answers
1. Because Git stamps every commit snapshot with the author's identity (name and email) for accountability and tracking.
2. The hidden `.git` folder.
3. No. Git commits only what is currently in the Staging Area at the moment of the commit. Any edits made after running `git add` are unstaged and must be added again before committing.

---

### Solution to Try It Yourself Exercise
Run these sequential commands in order:
```bash
echo "Documentation" > README.md
echo '{"theme": "dark"}' > settings.json
git add README.md
git commit -m "Add README documentation"
git status
```
**Expected Verification Output:**
```text
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        settings.json

nothing added to commit but untracked files present (use "git add" to track)
```

---

### Common Beginner Mistakes
* **Mistake: Author identity unknown error on commit.**
  * *Fix:* Run the `git config --global user.name` and `git config --global user.email` commands detailed in Lab 1.
* **Mistake: Editing a file after `git add` and committing directly without re-adding.**
  * *Fix:* Run `git add` again to stage the latest changes before committing, or the new edits won't be saved.
* **Mistake: Initializing a repository inside another repository folder.**
  * *Fix:* Never nested git repos. Run `git init` only at the project root. If you nested one, delete the hidden `.git` folder in the subfolder.

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
version: "1.3"
last_updated: "2026-07-18"
status: "Published"
author: "Rajasekar"
reviewed_by: "Admin"
prerequisites:
  - "GIT-FND-001 (Git Architecture & Three States)"
tags:
  - "Git Init"
  - "Git Config"
  - "Git Status"
  - "Git Clone"
```

---

## 1. Topics Covered [id: topics]
Now that you understand the three local environments conceptually, we will construct a local Git repository from scratch, inspect configuration locations, create commits, and handle common beginner terminal errors.

### Learning Outcomes
- **Knowledge**: Explain config scopes (Local, Global, System), config paths, and the difference between repository initialization and cloning.
- **Skills**: Create repos, verify hidden directories, read status codes, write ignore parameters, and handle typical terminal errors.
- **Outcome**: Confidently manage local repository workflows and debug setup issues.

---

## 2. Definitions & Core Concepts [id: definitions]

### Git Configuration Scopes & Paths
Git settings are resolved in three layered configuration scopes. If the same setting is configured across multiple scopes, Git prioritizes the most specific local setting first:
1. **Local** (Highest Priority): Applied strictly to the current active repository folder. Stored in `[project_root]/.git/config`.
2. **Global**: Applied to your current OS user profile across all repositories on your computer. Stored in `~/.gitconfig` (typically `C:\Users\YourUser\.gitconfig` on Windows or `/home/user/.gitconfig` on macOS/Linux).
3. **System** (Lowest Priority): Applied to all users and all repositories across the entire machine. Stored in `/etc/gitconfig`.

### git init vs. git clone
There are two distinct entry paths to start a project:

| Feature | `git init` | `git clone <url>` |
|---|---|---|
| **Objective** | Creates a blank local repository. | Downloads a copy of an existing remote repository. |
| **History** | Starts empty with no commits. | Downloads the complete history logs. |
| **Workspace** | Initializes the current folder. | Creates a new folder named after the project. |
| **Remote Link** | None configured (must link manually). | Pre-configured to point to remote origin. |

### Core Command Concepts
* **`git status`**: **The safest command in Git.** Running it will never modify, overwrite, or break anything in your repository; it only reports the current state of files.
* **`git commit`**: Creates a new immutable snapshot. Previous commits are never deleted or overridden; Git keeps all history logs unless explicitly instructed to overwrite them.
* **`git log`**: Every commit is assigned a unique cryptographic ID hash (e.g. `a1b2c3d`). Even if two commits share the same message, they will have different hashes.

---

## 3. Practical Code Examples [id: examples]

### Before You Start
Open your terminal client:
* **Windows**: Open **PowerShell** or **Command Prompt** (or **Git Bash**).
* **macOS / Linux**: Open **Terminal**.

Navigate to a workspace directory where you want to practice. For example:
```bash
# Navigate to your practice path
cd D:\GitPractice
```
*(If the folder does not exist, create it first or cd to your home directory: `cd ~`)*

---

### Step-by-Step Lab: Complete Local Repository Workflow

#### Step 1: Configure Git Identity
* 🎯 **Objective**: Set global author profile variables.
* ⌨ **Command**:
  ```bash
  git config --global user.name "John Doe"
  git config --global user.email "john@example.com"
  ```
* 💻 **Expected Output**: *(None - success is silent)*
* 🧠 **Explanation**: Git registers your profile globally. Git writes these settings to a text configuration file on your user account (typically `~/.gitconfig`). Every repository on your computer will use these values unless overridden locally inside a specific project config.
* ⚠ **Common Errors**:
  * *Error*: `fatal: unable to write config file`
  * *Fix*: Ensure you have write permissions to your user profile directory.

---

#### Step 2: Initialize a Local Repository
* 🎯 **Objective**: Create a blank local Git repository.
* ⌨ **Command**:
  ```bash
  git init MyProject
  cd MyProject
  ```
* 💻 **Expected Output**:
  ```text
  Initialized empty Git repository in D:/GitPractice/MyProject/.git/
  ```
* 🧠 **Explanation**:
  ```text
  Before init:
  MyProject/
  
  After init:
  MyProject/
  └── .git/     <-- Hidden system folder containing the database
  ```
* ✅ **Verification Step**:
  Since `.git` is a hidden directory, it will not show up in regular folder searches. To verify it exists, list the hidden files:
  * *PowerShell*: `dir -Force`
  * *CMD*: `dir /a`
  * *macOS / Linux / Git Bash*: `ls -la`
  You should see the `.git/` folder listed.
* ⚠ **Common Errors**:
  * *Error*: `fatal: permission denied`
  * *Fix*: Run the command in a directory where you have write access.

---

#### Step 3: Check Initial Status
* 🎯 **Objective**: Interrogate the blank repository state.
* ⌨ **Command**:
  ```bash
  git status
  ```
* 💻 **Expected Output**:
  ```text
  On branch main
  No commits yet
  nothing to commit (create/copy files and use "git add" to track)
  ```
* 🧠 **Explanation**: `git status` reports that we are on the default branch (usually `main` or `master`), have no history commits yet, and the working tree is clean.

---

#### Step 4: Create a File and Inspect Structure
* 🎯 **Objective**: Add a file to the Working Directory.
* ⌨ **Command**:
  ```bash
  echo "print('App running')" > app.py
  ```
* 💻 **Expected Output**: *(None - success is silent)*
* 🧠 **Explanation**:
  ```text
  Project folder state:
  MyProject/
  ├── app.py    <-- State: Untracked
  └── .git/
  ```
* ✅ **Verification Step**: Run `git status` again. Git will report `app.py` under `Untracked files` in red.
* ⚠ **Common Errors**:
  * *Error*: `Command not found` on echo (Windows PowerShell)
  * *Fix*: You can create a file using notepad instead: `notepad app.py`.

---

#### Step 5: Stage the File
* 🎯 **Objective**: Move the file changes into the Staging Area.
* ⌨ **Command**:
  ```bash
  git add app.py
  ```
* 💻 **Expected Output**: *(None)*
* 🧠 **Explanation**: Git copies the current state of `app.py` into the binary `.git/index` database cache.
* ✅ **Verification Step**: Run `git status`. You will see `new file: app.py` highlighted in green under `Changes to be committed`.

---

#### Step 6: Create Your First Commit
* 🎯 **Objective**: Record the staged files into a permanent snapshot.
* ⌨ **Command**:
  ```bash
  git commit -m "feat: initial code setup"
  ```
* 💻 **Expected Output**:
  ```text
  [main (root-commit) 8fa1b2c] feat: initial code setup
   1 file changed, 1 insertion(+)
   create mode 100644 app.py
  ```
* 🧠 **Explanation**: Git bundles your staged changes, stamps them with your author identity, and writes a permanent commit record into the `.git/` database folder.
  ```text
  Project state:
  MyProject/
  ├── app.py    <-- State: Committed / Tracked
  └── .git/     <-- Contains Commit #1 (8fa1b2c)
  ```
* ⚠ **Common Errors**:
  * *Error*: `Author identity unknown`
  * *Fix*: Run the configuration commands from Step 1 to set your user details.

---

#### Step 7: Inspect History Logs
* 🎯 **Objective**: View the repository history list and verify clean state.
* ⌨ **Command**:
  ```bash
  git log --oneline
  ```
* 💻 **Expected Output**:
  ```text
  8fa1b2c feat: initial code setup
  ```
* ✅ **Verification Step**:
  Run `git status` after committing:
  ```bash
  git status
  ```
  *Expected Output*:
  ```text
  On branch main
  nothing to commit, working tree clean
  ```
  *(Confirms that all changes are successfully committed and the workspace is clean)*

---

#### Step 8: What Happens Next? (Transitioning Back to Modified)
* 🎯 **Objective**: Make another change to see how Git handles modified tracked files.
* ⌨ **Command**:
  ```bash
  echo "print('App updated')" >> app.py
  git status
  ```
* 💻 **Expected Output**:
  ```text
  On branch main
  Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working directory)
          modified:   app.py
  
  no changes added to commit (use "git add" and/or "git commit -a")
  ```
* 🧠 **Explanation**: Git detects that `app.py` (which is a tracked file) has been modified since our last commit snapshot. The file has shifted from Committed back to **Modified** status. To save this new change, you would need to run `git add app.py` and `git commit` again.

---

## 4. Hands-on Workouts [id: workouts]

### Checkpoint Questions
1. You run a Git command and see the error: `fatal: not a git repository (or any of the parent directories): .git`. What is the issue, and how do you resolve it?
2. When running `git status`, you see:
   ```text
   Changes to be committed:
     new file:   index.html
   Changes not staged for commit:
     modified:   index.html
   ```
   What state is the file `index.html` in, and what happened?
3. Which command is used to safely interrogate the state of the workspace without risking any alterations to code history?

---

### Try It Yourself Exercise: Ignoring Temp Files
* **Goal**: Create and track source files while ensuring temporary cache files are ignored.
* **Steps**:
  1. Create a file `core.py`.
  2. Create a temporary log file `debug.log`.
  3. Create a `.gitignore` file configured to ignore `*.log` file formats.
  4. Run `git status` to verify `debug.log` is not visible.

---

## 5. Workout Answers & Solutions [id: answers]

### Checkpoint Answers
1. **Issue**: You ran a Git command in a terminal folder that has not been initialized with `git init`.
   * **Fix**: Change directory (`cd`) into your project folder that contains the `.git` directory, or run `git init` to initialize a new repository in the current folder.
2. **Explanation**: The file is in **both Staged and Modified states** simultaneously. This happens if you stage a file using `git add index.html`, and then make more edits to that same file *before* running `git commit`. Git only staged the version that existed at the moment of the `git add` command. To commit the new changes, you must run `git add index.html` again to update the index.
3. `git status`

---

### Solution to Try It Yourself Exercise
Run these commands in order:
```bash
echo "print('core')" > core.py
echo "system failure log" > debug.log
echo "*.log" > .gitignore
git status
```
**Expected Output**:
```text
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        core.py

nothing added to commit but untracked files present (use "git add" to track)
```
*(Notice that `debug.log` is completely ignored and does not show up in the status output)*

---

### Common Beginner Troubleshooting
* **Error: `pathspec 'filename' did not match any files`**
  * *Cause*: You typed the name of a file that does not exist in the current terminal directory.
  * *Fix*: Run `dir` (Windows) or `ls` (Unix) to check the spelling of your files, or make sure you are in the correct folder path.
* **Error: `fatal: not a git repository`**
  * *Cause*: Running Git commands in a regular folder instead of inside your repository directory.
  * *Fix*: `cd` into your initialized project folder before running commands.

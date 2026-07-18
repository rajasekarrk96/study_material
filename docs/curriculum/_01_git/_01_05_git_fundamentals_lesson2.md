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
version: "1.4"
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
Building upon the basic lifecycle models learned in Lesson 1, this lesson introduces professional repository controls: configuration hierarchies, cloning existing repositories, scanning status reports efficiently using short status flags, and managing git ignore filters.

### Learning Outcomes
- **Knowledge**: Explain config scopes (Local, Global, System), priority precedence, differences between initialization and cloning, and rules of `.gitignore`.
- **Skills**: Verify active configuration file origins, clone remote repositories, read short status outputs, and write patterns to ignore untracked files.
- **Outcome**: Adapt configuration options for project environments and maintain clean version track lists.

---

## 2. Definitions & Core Concepts [id: definitions]

### Git Configuration Scopes & Precedence
In Lesson 1, we set identity variables using the `--global` flag. Git actually resolves configurations across three distinct scopes. Precedence overrides from the most specific to the most general:

```text
                  Configuration Override Hierarchy
                  
     [Local]   ──► Project Folder (.git/config)        <-- [Highest Priority]
                  Overrides Global & System
        ▲
     [Global]  ──► OS User Account (~/.gitconfig)
                  Overrides System
        ▲
     [System]  ──► Operating System (/etc/gitconfig)   <-- [Lowest Priority]
```

#### Real-world Precedence Example:
Suppose you configure your primary name globally, but need a bot signature for a specific project:
1. **Global Setting**: Name configured as `"Rajasekar"`.
2. **Local Setting** (configured inside your target project): Name configured as `"Bytes & Boards Bot"`.
3. **Outcome**: When you commit inside that specific project, Git records the author as `"Bytes & Boards Bot"`, because Local configurations override Global settings.

> [!NOTE]
> **Checking Config Origins:** You can inspect exactly which file a setting is being loaded from by running `git config --show-origin --list`. This is a vital diagnostic command when troubleshooting profile overrides.

---

### git init vs. git clone
While `git init` creates a blank local repository from scratch, `git clone` downloads an existing repository including its full historical log structure.

```text
                               Cloning a Repository
                               
       Before Cloning:
       GitHub Remote Workspace [LearningSite] ──► URL: https://github.com/company/LearningSite.git
       
       After running `git clone <url>` locally:
       LearningSite/
       ├── .git/         <-- Database downloaded and remote origin configured automatically
       ├── README.md     <-- Project files downloaded
       ├── app.py
       ├── static/
       └── templates/
```

#### When to Use:
* **`git init`**:
  * ✅ Use when creating a brand-new project from scratch.
  * ❌ Don't use when joining an existing project.
* **`git clone`**:
  * ✅ Use when joining a company project, cloning open-source code, or starting from templates.
  * ❌ Don't use for brand-new local code.

---

### Short Status Output (`git status -s`)
For large repositories with hundreds of changes, the default `git status` reports can become long and difficult to scan. Developers use the short status command `git status -s` to get a structured 2-column prefix output:

```text
⌨ Command:
git status -s

💻 Mock Output:
?? app.py
M  README.md
A  login.py
D  old.py
```

* **`??`** (First line): Untracked file (never added to Git).
* **` M`** (Second column has `M`): Modified in Working Directory but not yet staged.
* **`M `** (First column has `M`): Staged modification ready for the next commit.
* **`A `** (First column has `A`): Added to the staging area index.
* **`D `** (First column has `D`): Deleted file.

---

### Git Ignore Filters (`.gitignore`)
The `.gitignore` text file registers file match patterns that Git should completely ignore.
* **`git status` without `.gitignore`**: Reports compile directories, log files, system cache, and secret environment files, cluttering the status screen.
* **`git status` with `.gitignore`**: Ignores junk logs and credentials, showing only your source code.

```text
Before .gitignore (Cluttered status):
Untracked files:
  debug.log
  temp.tmp
  .env
  app.py

After .gitignore (Clean status):
Untracked files:
  .gitignore
  app.py
```

#### When to Use:
* **`.gitignore`**:
  * ✅ Use to ignore logs (`*.log`), node modules, compile cache folders (`__pycache__/`), and developer environment settings.
  * ✅ Use to protect configuration secrets (like `.env` containing keys).

---

## 3. Practical Code Examples [id: examples]

### Before You Start
Open **PowerShell** (Windows) or **Terminal** (macOS/Linux) and navigate to your practice folder:
```bash
cd D:\GitPractice
```

---

### Step-by-Step Lab 1: Configuration Scopes

* 🎯 **Objective**: Set repository-specific configurations and find config file origins.
* ⌨ **Command**:
  ```bash
  # Check global config origins
  git config --global --list
  
  # Check show-origin list
  git config --show-origin --list
  ```
* 💻 **Expected Output**:
  ```text
  file:C:/Users/Rajasekar/.gitconfig   user.name=Rajasekar
  file:C:/Users/Rajasekar/.gitconfig   user.email=rajasekar@example.com
  ```
* 🧠 **Explanation**: Git lists your active global settings next to the absolute file path where they are saved.
* ⚠ **Common Errors**:
  * *Error*: `fatal: not a git repository` when checking local configs.
  * *Fix*: Local configurations (`git config --local --list`) can only be inspected inside directories initialized with `git init`.

---

### Step-by-Step Lab 2: Cloning an Existing Repository

* 🎯 **Objective**: Clone a public sandbox repository to local storage.
* ⌨ **Command**:
  ```bash
  git clone https://github.com/rajasekarrk96/study_material.git sandbox-project
  cd sandbox-project
  git status
  ```
* 💻 **Expected Output**:
  ```text
  Cloning into 'sandbox-project'...
  remote: Enumerating objects... done.
  ...
  On branch main
  Your branch is up to date with 'origin/main'.
  nothing to commit, working tree clean
  ```
* 🧠 **Explanation**: Git created a folder named `sandbox-project`, initialized a hidden `.git` folder inside it, connected it to the remote URL origin, and downloaded all files.
* ⚠ **Common Errors**:
  * *Error*: `fatal: repository not found` or authentication prompts.
  * *Fix*: Verify the spelling of the remote URL link.

---

### Step-by-Step Lab 3: Ignoring Cache & Temp Files

* 🎯 **Objective**: Implement a ignore filter and clean tracked lists.
* ⌨ **Command**:
  ```bash
  # 1. Create a dummy log and database secret file
  echo "error trace log" > app.log
  echo "key=secret123" > db.env
  
  # 2. Add patterns to a new .gitignore file
  echo "app.log" > .gitignore
  echo "db.env" >> .gitignore
  
  # 3. Verify status output is clean of log and env files
  git status -s
  ```
* 💻 **Expected Output**:
  ```text
  ?? .gitignore
  ```
* 🧠 **Explanation**: Even though `app.log` and `db.env` exist in your folder, they are ignored because they match rules defined in `.gitignore`.
* ⚠ **Common Errors**:
  * *Error*: Ignored files still show up in status logs.
  * *Fix*: The file was likely tracked *before* adding it to `.gitignore`. Stop tracking it by running `git rm --cached <filename>`.

---

## 4. Hands-on Workouts [id: workouts]

### Workout Exercises

#### Exercise A: Scope Validation
Initialize a blank project folder `scope-test`. Configure a local user name `git config --local user.name "Project Bot"`. Run `git config user.name` and verify it displays the Local override instead of your Global identity.

#### Exercise B: Cloning Checks
Create a directory. Clone your target repository and run `git config --local --list` to verify Git automatically created remote origin references in your project database.

#### Exercise C: Ignore Re-tracking
Create `secrets.json`, stage it with `git add secrets.json`, and commit it. Now add `secrets.json` to your `.gitignore`. Verify it still shows up when edited. Use `git rm --cached secrets.json` to tell Git to stop tracking it.

---

## 5. Workout Answers & Solutions [id: answers]

### Checkpoint Questions
1. Look at this short status output:
   ```text
   M  README.md
    M index.html
   ?? config.json
   ```
   Explain the state of each of these three files.
2. If you add `secrets.env` to `.gitignore` but it has already been committed in an earlier snapshot, will Git ignore future changes to it? How do you resolve this?

---

### Workout Solutions

#### Answer to Question 1:
* `README.md` is **Staged** (modified, changes added to index, ready to commit).
* `index.html` is **Modified** in your working directory, but the new changes are *not* staged yet.
* `config.json` is **Untracked** (never added to the repository).

#### Answer to Question 2:
No, Git will continue to track it. To ignore it, you must clear it from the index cache using `git rm --cached secrets.env`, then commit that removal.

#### Solution to Exercise C:
```bash
# Untrack secrets file but keep it on your computer
git rm --cached secrets.json
# Commit the removal
git commit -m "remove secrets from tracking list"
```

---

### Summary of New Concepts
Today you learned:
* **Configuration Scopes**: System, Global, and Local priorities, showing how local parameters override global profiles.
* **Clone vs Init**: How `git clone` imports existing histories and configures remotes automatically.
* **Short Status**: Using `git status -s` prefix flags to parse directory changes quickly.
* **`.gitignore`**: Excluding cache, log, and environment credential files from tracking histories.

### Next Lesson Preview
Now that you can initialize and commit file cycles, in the next lesson we will explore **Inspecting History: Log & Diff** to search commits and trace line differences.

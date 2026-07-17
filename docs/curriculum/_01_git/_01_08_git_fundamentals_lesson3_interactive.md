# Interactive Staging: Patch Mode & Partial Commits

---

```yaml
lesson_id: GIT-FND-003a
lesson_title: "Interactive Staging: Patch Mode & Partial Commits"
subject: Git
course: "Git Fundamentals"
module: "History Management"
difficulty: "⭐⭐⭐"
time_breakdown:
  reading: 10 min
  exercise: 15 min
  quiz: 5 min
  revision: 5 min
version: '1.0'
last_updated: '2026-07-17'
status: Published
author: Rajasekar
reviewed_by: Admin
prerequisites:
- GIT-FND-002 (Local Workflow: Init, Stage & Commit)
tags:
- Interactive Staging
- Patch Mode
- Git Add -p
- Selective Commits
```

---

## 1. Topics Covered [id: topics]
- Staging changes interactively via patch mode
- Splitting compound hunks into micro-stages
- Editing staging diffs manually for absolute precision
- Creating highly focused atomic commits

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - The concept of "hunks" in Git's diff engine.
  - Why selective staging is critical for maintaining clear commit logs.
- **Skills (What you can do)**:
  - Run interactive staging sessions using patch mode flags.
  - Stage, skip, split, and edit diff hunks interactively.
- **Professional Outcome**:
  - Author clean, atomic commits containing only related code edits.

---

## 2. Definitions & Core Concepts [id: definitions]

### What is Interactive Staging?
Standard `git add <file>` stages the entire file with all its modifications. Interactive staging via **Patch Mode (`git add -p` or `git add --patch`)** allows you to review individual modifications—known as **hunks**—and selectively stage them.

```text
                       Interactive Staging (Patch Mode)
                       
       Modified File (Multiple unrelated bugfixes/features)
                                │
                                ▼
         [Hunk 1: fix login] ──► Stage? (y/n) ──► Staging Area
                                │
         [Hunk 2: temp print] ──► Stage? (y/n) ──► (Skipped, left in workspace)
```

---

### Patch Mode Options Decoded
When running patch mode, Git displays a hunk and prompts you with a list of character actions:

| Action | Key | Meaning |
|---|---|---|
| **Stage Hunk** | **`y`** | Stage this hunk for the next commit. |
| **Skip Hunk** | **`n`** | Do not stage this hunk (leave it in the Working Directory). |
| **Quit** | **`q`** | Quit patch mode immediately (preserves what was staged so far). |
| **Stage All** | **`a`** | Stage this hunk and all subsequent hunks in the file. |
| **Skip All** | **`d`** | Do not stage this hunk or any subsequent hunks in the file. |
| **Split Hunk** | **`s`** | Split the current hunk into smaller hunks (only if lines have empty space between them). |
| **Edit Hunk** | **`e`** | Manually edit the current hunk to stage custom lines. |
| **Help** | **`?`** | Print a help description mapping all action keys. |

---

## 3. Practical Code Examples [id: examples]

### Interactive Staging Cheat Sheet
| Command | Purpose |
|---|---|
| **`git add -p`** | Starts an interactive patch staging session across all modified files. |
| **`git add -p <file>`** | Starts a patch staging session for a specific file. |
| **`git reset -p`** | Interactively unstages specific hunks from the Staging Area. |
| **`git checkout -p`** | Interactively discards specific hunks from the Working Directory. |

### Example A: Running an Interactive Staging Session
Suppose you modified `auth.py` to fix a session timeout and added a temporary debug comment:
```bash
git add -p auth.py
```

Console Output:
```text
diff --git a/auth.py b/auth.py
index a1b2c3d..e5f6g7h 100644
--- a/auth.py
+++ b/auth.py
@@ -10,6 +10,12 @@ def login():
+    # FIX: correct session timeout limit to 15 minutes
+    session.timeout = 900
+    # TODO: debug temporary log print
+    print("session updated")
 
(1/1) Stage this hunk [y,n,q,a,d,s,e,?]?
```

Action: You want to stage the timeout fix but keep the debug print out of the commit. Because there is a line of difference, you can split the hunk:
- Type **`s`** to split:
```text
Split into 2 hunks.
@@ -10,3 +10,6 @@ def login():
+    # FIX: correct session timeout limit to 15 minutes
+    session.timeout = 900
 
Stage this hunk [y,n,q,a,d,j,J,g,/,e,?]?
```
- Type **`y`** to stage the first split hunk.
- For the second hunk (debug print), type **`n`** to skip.

Checking status:
```bash
git status -s
```

Output:
```text
MM auth.py
```
*(Note: `MM` status indicates that `auth.py` contains both staged and unstaged modifications!)*

---

## 4. Hands-on Workouts [id: workouts]

### MCQ
- Which key split a large commit hunk into smaller sub-hunks during a patch staging session?
  - A) `p`
  - B) `s` (Correct)
  - C) `e`

### Coding Challenge
- Start an interactive patch staging session specifically for `main.py`.
  - Answer: `git add -p main.py`

### Scenario Question: Unrelated modifications
- A developer finishes two unrelated features in `app.py` (added route validation and updated CSS styling). They want to create two distinct, clean commits.
  - Action: Run `git add -p app.py`. Stage the route validation hunks first with `y` (skipping styling hunks with `n`), commit them, then stage and commit the remaining styling changes.

---

## 5. Workout Answers & Solutions [id: answers]

### Common Beginner Mistakes
- **Assuming Split Always Works**: Typing `s` on a hunk where modified lines are contiguous (no empty space lines between edits). Git will report: `Sorry, cannot split hunk`.
  - *Fix*: Use `e` to edit the hunk manually and select which lines to stage.
- **Accidental Discards**: Running `git checkout -p` and typing `y` on important work, permanently losing it from disk.

### Enterprise Best Practices
1. **Atomic Commits**: Group only related changes. If you fix a typo and add a feature, create two commits using patch mode.
2. **Review While Staging**: Use `git add -p` as a final code review pass to make sure no debug prints or secrets enter your index.
3. **Commit Clean**: Always verify your staged hunks using `git diff --staged` before committing.

### Key Takeaways
- Patch mode (`git add -p`) enables line-by-line selective staging.
- Git splits code modifications into segments called hunks.
- Large hunks can be split using `s` or custom-edited using `e`.
- Selective staging ensures team logs are clean, traceable, and regression-proof.

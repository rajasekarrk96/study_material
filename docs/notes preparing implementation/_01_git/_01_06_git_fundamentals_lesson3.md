# Lesson 3: Inspecting History and Comparing Changes — Log and Diff

---

```yaml
lesson_id: GIT-FND-003
lesson_title: "Inspecting History: Log & Diff"
subject: Git
course: Git Fundamentals
module: Basic Local Workflow
difficulty: "\u2B50"
time_breakdown:
  reading: 12 min
  exercise: 15 min
  quiz: 10 min
  revision: 5 min
version: '1.0'
last_updated: '2026-07-17'
status: Published
author: Rajasekar
reviewed_by: Admin
prerequisites:
- GIT-FND-002 (Basic Local Workflow)
tags:
- Git Log
- Git Diff
- Inspect Changes
- Git Show
```

---

## 1. Topics Covered [id: topics]
This lesson teaches you how to query and navigate Git repository history records using the log system, and how to perform line-by-line file content comparison using differences rendering analysis.

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - How Git represents changes between commits using raw diff outputs.
  - The difference between working tree diffs, staged diffs, and commit comparisons.
- **Skills (What you can do)**:
  - Format, filter, and restrict git log history views using advanced flags.
  - Review staged and unstaged edits line-by-line using git diff.
- **Outcome (Professional application)**:
  - Debug regressions by tracking changes, authors, and commit branches history logs.

## 2. Definitions & Core Concepts [id: definitions]
When you request a list of history, Git does not query a central server. It starts at the commit pointed to by **HEAD**, reads its metadata, and follows parent commit hashes pointers backward in time to reconstruct the line of development.

### How `git diff` works internally
Git compares two snapshot tree states. It uses the **Myers Diff Algorithm** to calculate the minimum edit script (insertions and deletions) required to transform one tree structure or file content into another.
- `git diff` (without flags) compares your Working Directory with the Staging Area.
- `git diff --staged` (or `--cached`) compares the Staging Area with the last commit in the Local Repository.

### Terminology & Glossary
- **Commit Hash**: A unique 40-character SHA-1 checksum identifying a specific commit object.
- **Diff marker**: Character flags (`+` for additions, `-` for deletions) showing changes.
- **Oneline Log**: A compacted single-line view formatting commit hashes and messages.

## 3. Practical Code Examples [id: examples]
### Easy
View a compacted history graph list:
```bash
git log --oneline --graph --all
```

### Medium
Compare the Working Directory with the last commit:
```bash
# Edit file.txt
echo "new line" >> file.txt

# Run diff comparing working tree directly to HEAD
git diff HEAD
```

### Advanced
Search for commits affecting a specific file containing a specific word (Snoop search):
```bash
git log -S "API_KEY" --oneline
```

## 4. Hands-on Workouts [id: workouts]
### MCQ
- Which command shows commits as a text graph?
  - A) `git log --graph` (Correct)
  - B) `git log --tree`
  - C) `git log --map`

### Coding Challenge
- Generate a commit history log limit of exactly 2 entries in standard formatting.

### Predict the Output
- If you run `git diff` on a file where you only deleted the word "foo", what does the matching line output prefix with?
  - Output: `- foo`

### Debugging Task
- Fix a slow git search query by limiting search parameters to files within the `src/` directory:
  - Answer: `git log -- src/`

### Scenario Question
- A developer wants to see who changed the file `auth.py` and when. What command should they use?
  - Answer: `git log --oneline -- auth.py` or `git blame auth.py`.

### Hands-on Lab
- Make an edit to `app.py`, run `git diff`, stage it, and verify `git diff` output is empty.

## 5. Workout Answers & Solutions [id: answers]
- **Standard Syntax**: `git diff <commit_a> <commit_b>`
- **Aliases**: `git config --global alias.lg "log --oneline --graph --all"`
- **Shortcut**: Use the `git show <hash>` command to quickly inspect a single commit object data.
- **Warning**: Running `git diff` without parameters may show line endings mismatches if CRLF settings are not aligned.

# Lesson 3: Handling Merge Conflicts in Teams — Visual markers and resolution strategies

---

```yaml
lesson_id: GIT-COL-003
lesson_title: "Merge Conflict Handling in Teams"
subject: Git
course: Git Collaboration
module: Merge Conflicts
difficulty: "\u2B50\u2B50\u2B50"
time_breakdown:
  reading: 15 min
  exercise: 25 min
  quiz: 10 min
  revision: 5 min
version: '1.0'
last_updated: '2026-07-17'
status: Published
author: Rajasekar
reviewed_by: Admin
prerequisites:
- GIT-COL-002 (Data Syncing)
tags:
- Merge Conflicts
- Conflict Resolution
- Git Merge
- Syncing
```

---

## 1. Topics Covered [id: topics]
This lesson covers conflict management in collaborative developer environments. You will learn why merge conflicts occur, how to interpret conflict markers, and strategies for resolving overlaps during merges or rebases.

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - Why Git enters conflict states (overlapping line modifications vs file deletion mismatches).
  - The meaning of `HEAD` (ours) and branch (theirs) references during merge conflicts.
- **Skills (What you can do)**:
  - Read conflict blocks, resolve file conflicts, use git merge tools, and safely abort failed merges.
- **Outcome (Professional application)**:
  - Coordinate code integrations with teammates by resolving conflicts without losing active logic.

## 2. Definitions & Core Concepts [id: definitions]
A **merge conflict** occurs when Git attempts to merge two branches that have divergent edits on the exact same line of a file, or if one developer deletes a file that another developer modified.
When this happens:
1. Git halts the merge process and does not create a merge commit.
2. It marks the conflicted file as "unmerged" in the Staging Area index.
3. It inserts **conflict markers** directly into the conflicted file to show the differences.

### Understanding Conflict Markers
```text
<<<<<<< HEAD
code changes on your active local branch
=======
code changes on the incoming merged branch
>>>>>>> feature-branch
```
- `<<<<<<< HEAD`: Starts the section containing edits from your active branch.
- `=======`: Divides the two conflicted versions.
- `>>>>>>> feature-branch`: Closes the section containing edits from the incoming branch.

### Terminology & Glossary
- **Three-Way Merge Ancestor**: The last shared commit parent of two divergent branches.
- **Ours**: The active branch state you are currently checked out on (represented by HEAD).
- **Theirs**: The incoming branch state you are merging into your active branch.

## 3. Practical Code Examples [id: examples]
### Easy
Abort a conflicted merge to restore previous state:
```bash
git merge --abort
```

### Medium
Checking which files are in conflict:
```bash
# Run status to see unmerged files lists
git status
# Conflicted files are labeled under "Unmerged paths"
```

### Advanced
Using diff3 format to display the common ancestor state in conflict markers:
```bash
# Configure diff3 layout
git config --global merge.conflictstyle diff3

# Conflict markers will now include the shared ancestor baseline:
# <<<<<<< HEAD
# local version
# ||||||| parent of...
# original common ancestor version
# =======
# incoming version
# >>>>>>> feature-branch
```

## 4. Hands-on Workouts [id: workouts]
### MCQ
- What symbol marks the start of your local changes in a conflict block?
  - A) `<<<<<<< HEAD` (Correct)
  - B) `=======`
  - C) `>>>>>>>`

### Coding Challenge
- Abort a merge conflict state.

### Predict the Output
- If you run `git status` during a merge conflict, what header label identifies the conflicted files?
  - Output: `Unmerged paths:`

### Debugging Task
- Clean up a file containing standard conflict markers by keeping only the incoming branch line `active = true`.
  - Answer: Delete markers and local lines, keeping only `active = true`, then run `git add`.

### Scenario Question
- A developer is resolving conflicts. They run `git add resolved.py`. What is the next command to complete the merge?
  - Answer: `git commit` or `git merge --continue`.

### Hands-on Lab
- Edit a file on main, switch to branch, edit same line, merge main to trigger conflict, resolve.

## 5. Workout Answers & Solutions [id: answers]
- **Standard Syntax**: `git merge --abort`
- **Aliases**: None.
- **Shortcut**: None.
- **Warning**: Do not delete conflict markers without reviewing the code.

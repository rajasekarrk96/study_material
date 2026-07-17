# Lesson 1: Git Internals — Blobs, Trees, Commits, and Refs

---

```yaml
lesson_id: GIT-ADV-001
subject: Git
course: Advanced Git
module: Git Internals Deep-Dive
difficulty: "\u2B50\u2B50\u2B50\u2B50"
time_breakdown:
  reading: 20 min
  exercise: 25 min
  quiz: 15 min
  revision: 5 min
version: '1.0'
last_updated: '2026-07-17'
status: Published
author: Rajasekar
reviewed_by: Admin
prerequisites:
- GIT-COL-004 (Upstream Workflows)
tags:
- Git Internals
- Objects
- SHA-1
- Refs
```

---

## 1. Topics Covered [id: topics]
This lesson explores Git's internal storage mechanisms. We inspect the contents of the `.git` directory, analyze Git's content-addressable storage model, and dissect the byte structures of Blobs, Trees, Commits, and References.

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - How Git represents code history in a content-addressable object database.
  - The byte-level structure and relationships between Blobs, Trees, Commits, and Tags.
- **Skills (What you can do)**:
  - Inspect, write, and dissect raw Git objects using low-level plumbing commands.
- **Outcome (Professional application)**:
  - Debug repository corruption errors and analyze Git metadata anomalies directly inside `.git`.

## 2. Definitions & Core Concepts [id: definitions]
At its core, Git is a **content-addressable filesystem** built on a simple key-value store. You insert a piece of content, and Git returns a 40-character SHA-1 checksum key that points to it.

### The Four Object Types
Every object in `.git/objects/` is compressed with zlib and begins with a header defining its type and byte size, followed by a null byte `\0` and the content.
1. **Blob**: Stores raw file content bytes. It does not store filenames, directory paths, or permission metadata.
2. **Tree**: Represents directory structure. It acts as a directory index mapping filenames to blob hashes (files) or other tree hashes (subdirectories), along with file execution modes.
3. **Commit**: Contains metadata pointing to a root Tree hash, list of parent commit hashes, timestamps, author details, and the commit description message.
4. **Tag**: A permanent commit reference pointing to a specific target commit hash, accompanied by a tagger name and signature.

### Terminology & Glossary
- **Plumbing Commands**: Low-level Git utility commands that manipulate internal structures directly (e.g. `hash-object`, `cat-file`).
- **Porcelain Commands**: High-level user-friendly Git commands (e.g. `add`, `commit`, `status`).
- **Content-Addressable**: Hashing content to determine its address/location in database.

## 3. Practical Code Examples [id: examples]
### Easy
Generate the SHA-1 hash key of a string without writing it to database:
```bash
echo "hello world" | git hash-object --stdin
# Output: 3b18e512dba79e4c8300dd08aeb37f8e728b8dad
```

### Medium
Dissect the type and content of a Git object by hash:
```bash
# Get type (returns blob, tree, or commit)
git cat-file -t 3b18e512

# View pretty-printed contents
git cat-file -p 3b18e512
```

### Advanced
Manually write a blob and tree to the Git database using plumbing:
```bash
# Write blob, retrieve hash
BLOB_HASH=$(echo "print('API Code')" | git hash-object -w --stdin)

# Write to staging index directly
git update-index --add --cacheinfo 100644 $BLOB_HASH app.py

# Write index tree snapshot to database, returns tree hash
git write-tree
```

## 4. Hands-on Workouts [id: workouts]
### MCQ
- Which plumbing command prints the contents of a Git object?
  - A) `git show-object`
  - B) `git cat-file` (Correct)
  - C) `git inspect-file`

### Coding Challenge
- Write the string "test content" to Git's object database as a blob and print its SHA-1 hash.

### Predict the Output
- If you run `git cat-file -t` on a commit object hash, what does it output?
  - Output: `commit`

### Debugging Task
- Fix a corrupt reference error by inspecting the HEAD file contents.
  - Answer: View `.git/HEAD` and verify it contains a valid reference path like `ref: refs/heads/main`.

### Scenario Question
- A developer modified a file name but did not change the file content. How many new Blobs are written during addition?
  - Answer: Zero, because content hashing ensures identical files map to the same Blob hash. Only a new Tree object is written.

### Hands-on Lab
- Navigate to `.git/objects/`, locate a subdirectory, and pretty-print an object using `git cat-file -p`.

## 5. Workout Answers & Solutions [id: answers]
- **Standard Syntax**: `git cat-file -p <hash>`
- **Aliases**: None.
- **Shortcut**: None.
- **Warning**: Modifying files inside `.git/refs/` manually is highly discouraged.

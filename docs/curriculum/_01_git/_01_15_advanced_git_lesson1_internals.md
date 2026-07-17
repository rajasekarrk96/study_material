# Git Internals: Blobs, Trees & Commits

---

```yaml
lesson_id: GIT-ADV-001
lesson_title: "Git Internals: Blobs, Trees & Commits"
subject: Git
course: "Git Fundamentals"
module: "Git Internals"
difficulty: "⭐⭐⭐⭐"
time_breakdown:
  reading: 20 min
  exercise: 25 min
  quiz: 15 min
  revision: 5 min
version: '1.2'
last_updated: '2026-07-17'
status: Published
author: Rajasekar
reviewed_by: Admin
prerequisites:
- GIT-COL-004 (Forking & Upstream Workflows)
tags:
- Git Internals
- Objects
- SHA-1
- Refs
```

---

## 1. Topics Covered [id: topics]
- Git object database
- Blob, Tree, Commit, Tag
- Plumbing commands
- .git directory
- Content-addressable storage

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - How Git represents directory paths, file content, and commits inside an immutable database.
  - The differences between Porcelain commands (front-end) and Plumbing commands (under-the-hood).
- **Skills (What you can do)**:
  - Read, write, and trace low-level objects using internal Git diagnostic commands.
  - Inspect the structure of the `.git` metadata folder to identify repository states.
- **Professional Outcome**:
  - Write custom build/deploy tooling, diagnose data corruptions, and debug low-level version issues.

---

## 2. Definitions & Core Concepts [id: definitions]

### Object Relationship Diagram
Git objects form a directed acyclic graph (DAG). The following diagram shows how these objects link together to represent files, folders, and repository histories:
```text
                      Object Relationships
                      
                           HEAD (Pointer File)
                            │
                            ▼
                     Branch / Tag (Ref Pointer)
                            │
                            ▼
                         [Commit] (Points to root Tree & Parents)
                            │
                            ▼
                          [Tree] (Directory snapshot mapping names/modes)
                           /    \
                          /      \
                      [Blob]    [Tree] (Sub-directory structure)
                  (File Content)   │
                                   ▼
                                 [Blob]
```

### Object Hierarchy Flow
- **`HEAD`**: Points to the current active branch (or directly to a commit hash in a detached state).
- **`Branch`**: A simple text pointer pointing to the latest commit.
- **`Commit`**: References a root directory **Tree** snapshot and parent commit hashes.
- **`Tree`**: Represents folder structures, mapping file paths to **Blob** hashes or other nested **Tree** hashes.
- **`Blob`**: Stores raw file content compressed with `zlib`. It does not store filenames or dates.

---

### Inside the `.git` Directory
The hidden `.git` folder contains the metadata and database defining your repository:
```text
.git/
├── HEAD            # Reference file pointing to the current active branch
├── config          # Local configuration settings file
├── index           # Staging Area binary index cache
├── objects/        # The Object Database store
│   ├── [0-9a-f]{2}/# Loose objects stored by hash prefix
│   ├── info/       # Additional database configuration files
│   └── pack/       # Compressed packfiles (optimized bulk archives)
├── refs/           # Pointer reference maps
│   ├── heads/      # Local branch pointer files
│   └── tags/       # Lightweight tag pointers
├── logs/           # HEAD and branch history logs (used for reflog)
└── hooks/          # Client-side automation script hooks
```

---

### SHA-1 vs. SHA-256 Hashes
Historically, Git identifies database objects using SHA-1 hashes (40 hexadecimal characters). Modern Git versions also support SHA-256 repositories, although SHA-1 remains the default for most existing repositories. 

> [!NOTE]
> Object hashes identify the combination of the object header (type + space + size in bytes + null byte) plus the compressed content, ensuring that duplicate files with identical text content always resolve to the exact same hash key.

---

### Content-Addressable Storage & Deduplication
If multiple files in different folders contain the exact same content, Git stores the content **once** as a single Blob, reusing it in all references:
```text
  File A: "hello world" ──┐
                          ├──► SHA Hash: 3b18e5... ──► Stored Once in objects/
  File B: "hello world" ──┘
```

---

### Sample Commit Object Layout
If you inspect a raw commit object using plumbing commands, it looks like this:
```text
tree a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0
parent f4g5h6i7j8k9l0m1n2o3p4q5r6s7t8u9v0w1x2y
author Tester <test@example.com> 1782294726 +0530
committer Tester <test@example.com> 1782294726 +0530

feat: add application gateway validation middleware
```
- **`tree`**: Hash of the root directory tree for this snapshot.
- **`parent`**: Hash of the preceding parent commit.
- **`author` / `committer`**: User identity and timestamp.
- **Message**: The commit description.

---

### Porcelain vs. Plumbing
| Porcelain (High-Level) | Plumbing (Low-Level) |
|---|---|
| `git add` | `git update-index` |
| `git commit` | `git write-tree`, `git commit-tree` |
| `git status` | `git ls-files` |
| `git log` | `git rev-list` |
| `git show` | `git cat-file` |

---

## 3. Practical Code Examples [id: examples]

### Internal Investigation Command Reference
| Command | Purpose |
|---|---|
| **`git rev-parse HEAD`** | Translates HEAD into its raw 40-character commit hash. |
| **`git cat-file -t <hash>`** | Prints the type of an object (`blob`, `tree`, `commit`, `tag`). |
| **`git cat-file -p <hash>`** | Pretty-prints the raw contents of an object. |
| **`git ls-tree <tree-hash>`** | Lists files and sub-folders referenced in a Tree object. |
| **`git fsck`** | Verifies database integrity and searches for dangling/orphaned objects. |
| **`git verify-pack -v <idx>`** | Inspects compressed packfile sizes for debugging. |

### Example A: Inspecting Objects E2E
- **Code**:
  ```bash
  # 1. Translate HEAD to hash
  COMMIT_HASH=$(git rev-parse HEAD)
  
  # 2. Get type of HEAD
  git cat-file -t $COMMIT_HASH
  
  # 3. Print tree content of HEAD
  git ls-tree HEAD
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ $ git ls-tree HEAD                                     │
  │ 100644 blob 3b18e512dba79e4c8300dd08ae   app.py        │
  │ 040000 tree d7e8f9c0a1b2c3d4e5f6g7h8i9   src           │
  └────────────────────────────────────────────────────────┘
  ```
  *(Note: `100644` is the standard non-executable file mode; `040000` indicates a directory)*

### Example B: Tag objects vs References
- **Lightweight Tags**: Simple text files in `.git/refs/tags/` containing a commit hash.
- **Annotated Tags**: Stored as full tag objects in `.git/objects/` with signature metadata.

### Example C: Pack files optimization
As repositories grow, Git automatically aggregates individually zlib-compressed loose files into single compressed pack archives (packfiles) located under `.git/objects/pack/` to save disk space and optimize network transfers.

---

## 4. Hands-on Workouts [id: workouts]

### MCQ
- What type of Git object stores file folder hierarchies and filenames?
  - A) Blob
  - B) Tree (Correct)
  - C) Commit

### Coding Challenge
- Run a command to verify the internal file structure integrity of your database.
  - Answer: `git fsck`

---

## 5. Workout Answers & Solutions [id: answers]

### Common Mistakes
- **Mistake**: Manually modifying or writing files directly inside the hidden `.git/objects/` folder.
  - *Result*: Causes database corruption errors. Always use plumbing commands for manual writes!
- **Mistake**: Assuming Blobs store file metadata (like filenames or modes).
  - *Fact*: Blobs only store raw content. Metadata is stored inside **Tree** objects.

### Enterprise Best Practices
1. **Porcelain for Dev**: Restrict everyday coding tasks to high-level Porcelain commands.
2. **Automated Tooling**: Use Plumbing commands (`git rev-parse`, `git cat-file`) when writing CI/CD scripts or automated tooling.
3. **Database Maintenance**: Run `git fsck` regularly on local development folders to check repository health.

### Key Takeaways
- Git is a zlib-compressed, content-addressable database.
- Blobs store file content; Trees represent directories; Commits record snapshots; Tags mark points.
- Identical file contents reuse the same blob, eliminating duplicate storage.
- Plumbing commands provide low-level access, while Porcelain commands offer developer-friendly interfaces.

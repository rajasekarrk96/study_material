# Advanced Git: Tags and Release Management

---

```yaml
lesson_id: GIT-ADV-006
lesson_title: "Advanced Git: Tags & Release Management"
subject: Git
course: "Git Fundamentals"
module: "Advanced Workflows"
difficulty: "⭐⭐"
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
- GIT-ADV-005 (Advanced Git: Cherry-picking & Backporting)
tags:
- Tags
- Releases
- SemVer
- Versioning
```

---

## 1. Topics Covered [id: topics]
- Lightweight vs Annotated tags
- Semantic Versioning (SemVer) guidelines
- Publishing and pushing tags to remotes
- Deleting local and remote tags
- GPG signed tags for secure builds

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - The structural difference between lightweight references and annotated database tag objects.
  - The Semantic Versioning rules (Major, Minor, Patch).
  - How cloud hosting platforms translate tags into formal Release logs.
- **Skills (What you can do)**:
  - Create annotated tags, sign tags with GPG keys, push tags to remote origins, and delete tags.
- **Professional Outcome**:
  - Implement standard version release tracking and tag deployment gates in project repositories.

---

## 2. Definitions & Core Concepts [id: definitions]

### Tag Types Comparison
Tags act as permanent markers pointing to specific commits in your history (unlike branches, which move as you commit):

| Lightweight Tag | Annotated Tag |
|---|---|
| A simple pointer pointing to a commit hash. | A complete Git database object. |
| Stores no metadata. | Stores tagger name, email, date, and message. |
| Primarily used for local testing. | Standard choice for public and production releases. |
| Cannot be cryptographically signed. | Can be GPG signed (`git tag -s`) for verification. |

---

### Semantic Versioning (SemVer)
Semantic Versioning uses a three-part number format: **`MAJOR.MINOR.PATCH`** (e.g. `v1.4.2`):
```text
                          Semantic Versioning (SemVer)
                          
                                    v 2 . 1 . 4
                                      │   │   │
     Incremental breaking API changes ┘   │   └─ Backward-compatible bugfixes
                                          │
                  Backward-compatible features ┘
```
- **MAJOR**: Incremented when you make incompatible API changes.
- **MINOR**: Incremented when you add functionality in a backward-compatible manner.
- **PATCH**: Incremented when you make backward-compatible bugfixes.

---

### Tags vs. Releases
- **Git Tag**: A git object or reference identifying a commit (local Git functionality).
- **Hosting Release**: A platform feature (GitHub/GitLab) built on top of a Git tag. Releases allow you to attach build assets, release notes, and changelogs.

---

## 3. Practical Code Examples [id: examples]

### Tag Command Cheat Sheet
| Command | Purpose |
|---|---|
| **`git tag`** | Lists all local tags in the repository. |
| **`git tag <name>`** | Creates a lightweight tag at the current commit. |
| **`git tag -a <name> -m "msg"`** | Creates an annotated tag with a release message. |
| **`git tag -s <name> -m "msg"`** | Creates a cryptographically signed tag using GPG keys. |
| **`git push origin <name>`** | Pushes a single tag to the remote repository. |
| **`git push origin --tags`** | Pushes all local tags to the remote repository. |
| **`git tag -d <name>`** | Deletes a local tag. |
| **`git push origin --delete <name>`** | Deletes a tag from the remote repository. |

### Example A: Creating and Pushing an Annotated Release Tag
```bash
# 1. Create an annotated tag for version 1.1.0
git tag -a v1.1.0 -m "Release version 1.1.0 containing core checkout API features"

# 2. Verify tag details
git show v1.1.0
```

Output:
```text
tag v1.1.0
Tagger: Developer <dev@example.com>
Date:   Fri Jul 17 19:20:00 2026 +0530

Release version 1.1.0 containing core checkout API features

commit a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0
Author: Developer <dev@example.com>
...
```

Pushing the tag online:
```bash
git push origin v1.1.0
```

---

## 4. Hands-on Workouts [id: workouts]

### MCQ
- Which semantic version number do you increment when you fix a bug without changing your API?
  - A) MAJOR
  - B) MINOR
  - C) PATCH (Correct)

### Coding Challenge
- Delete a local tag named `v0.9.0-alpha`.
  - Answer: `git tag -d v0.9.0-alpha`

### Scenario Question: Security verification
- A DevOps team wants to verify that release tags are actually created by authorized developers.
  - Action: Enforce GPG signed tags using `git tag -s v1.2.0 -m "release"`. GitLab/GitHub will display a "Verified" badge for these tags.

---

## 5. Workout Answers & Solutions [id: answers]

### Common Beginner Mistakes
- **Assuming Pushes include Tags**: Running `git push` and expecting tags to upload automatically (they do not). You must run `git push origin <tag>` or `git push origin --tags`.
- **Modifying Tags**: Recreating the same tag name on a different commit without deleting the old tag from the remote, causing synchronization mismatches.

### Enterprise Best Practices
1. **Always use Annotated Tags**: Never use lightweight tags for release versions.
2. **Standardize SemVer**: Adhere strictly to SemVer versioning models to avoid breaking dependencies.
3. **Automate Releases**: Link your CI/CD pipelines to trigger builds automatically when a release tag (like `v*`) is pushed.

### Key Takeaways
- Git tags are static references to specific commits.
- Annotated tags contain tagger details, messages, and optional GPG signatures.
- Semantic Versioning defines version formats: MAJOR.MINOR.PATCH.
- Pushing tags online requires explicit commands like `git push origin --tags`.

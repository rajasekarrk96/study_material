# Cherry-picking & Backporting

---

```yaml
lesson_id: GIT-ADV-005
lesson_title: "Cherry-picking & Backporting"
subject: Git
course: "Git Fundamentals"
module: "Advanced Workflows"
difficulty: "⭐⭐⭐"
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
- GIT-ADV-002 (Rewriting History: Amend, Rebase & Squash)
tags:
- Cherry-pick
- Backporting
- Hotfixes
- Release Branches
```

---

## 1. Topics Covered [id: topics]
- Git Cherry-pick mechanics
- Backporting bugfixes to older versions
- Hotfixing release branches
- Conflict resolution during cherry-pick

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - How Git duplicates commits onto other branches using the cherry-pick command.
  - Why cherry-picking creates a brand-new commit hash.
  - When to apply cherry-picking vs standard branch merges.
- **Skills (What you can do)**:
  - Cherry-pick individual commits, resolve cherry-pick conflicts, and skip or abort sessions.
- **Professional Outcome**:
  - Manage hotfixes on release branches and backport critical fixes across concurrent version streams.

---

## 2. Definitions & Core Concepts [id: definitions]

### Cherry-picking Visual Diagram
Cherry-picking takes the changes introduced by a single commit on one branch and applies them as a new commit on another branch:
```text
                         Cherry-picking Commit [D]
                         
        feature branch:  A ──► B ──► C ──► [D]  (Commit to copy)
                                            │
                                            ▼ (git cherry-pick D)
                                            │
        release branch:  E ──► F ────────────────► [D'] (New duplicate commit)
```
> [!NOTE]
> Commit `D'` contains the exact code changes of commit `D`, but it is a **new commit object** with a new commit hash and author timestamp because it has a different parent commit in the branch history.

### What is Backporting?
Backporting is the process of copying a bugfix or feature from a newer version of the codebase (e.g. `main` or development branch) and applying it to an older, supported release branch (e.g. `release-v1.0`).

### Cherry-pick vs. Merge vs. Rebase
- **Merge**: Combines entire branches, including all commits and their history.
- **Rebase**: Moves a series of commits to a new base branch.
- **Cherry-pick**: Selectively copies **one or more specific commits** without merging the rest of the branch.

---

## 3. Practical Code Examples [id: examples]

### Cherry-pick Command Cheat Sheet
| Command | Purpose |
|---|---|
| **`git cherry-pick <commit-hash>`** | Copies changes from the target commit onto the active branch. |
| **`git cherry-pick A B C`** | Cherry-picks multiple commits sequentially. |
| **`git cherry-pick --continue`** | Resumes the cherry-pick process after resolving conflicts. |
| **`git cherry-pick --abort`** | Cancels the cherry-pick and restores the pre-cherry-pick state. |
| **`git cherry-pick --skip`** | Skips the current commit and moves to the next during multi-pick. |

### Example A: Cherry-picking a Hotfix
Suppose a critical bug was fixed in commit `c2d3e4f` on the `develop` branch. We need to deploy this fix to the active production branch `release-v2.0` immediately without deploying unapproved develop features:
```bash
# Switch to the target release branch
git switch release-v2.0

# Cherry-pick the target fix commit
git cherry-pick c2d3e4f
```

Output:
```text
[release-v2.0 a8b9c0d] fix(api): correct authentication token verification
 1 file changed, 2 insertions(+), 2 deletions(-)
```

### Example B: Handling Cherry-pick Conflicts
If code edits conflict with files on the target branch, Git pauses the cherry-pick:
```bash
# Git reports conflict during pick:
# error: could not apply c2d3e4f... fix(api): correct verification
# hint: after resolving conflicts, mark paths with 'git add' and run 'git cherry-pick --continue'

# 1. Open files, resolve markers, then stage:
git add app/auth.py

# 2. Complete cherry-pick
git cherry-pick --continue
```

---

## 4. Hands-on Workouts [id: workouts]

### MCQ
- What happens to the commit history when you cherry-pick a commit?
  - A) The original commit is moved to the target branch.
  - B) A new commit is created on the target branch containing the same changes. (Correct)
  - C) Both branches are merged.

### Coding Challenge
- Abort an active cherry-pick session that has run into conflict.
  - Answer: `git cherry-pick --abort`

### Scenario Question: Hotfixing
- A developer fixes a login bug on the `feature/oauth` branch. The fix needs to go live today on `main`, but the oauth feature is still undergoing QA.
  - Action: Identify the commit hash of the bugfix on `feature/oauth` (e.g. `e3d4c5b`), switch to `main`, and run `git cherry-pick e3d4c5b`.

---

## 5. Workout Answers & Solutions [id: answers]

### Common Beginner Mistakes
- **Creating Duplicates**: Cherry-picking commits repeatedly instead of merging, which clutters repository history with duplicate commit logs.
- **Forgetting to --continue**: Resolving conflicts but running `git commit` instead of `git cherry-pick --continue` to finalize.

### Enterprise Best Practices
1. **Prefer Merge for Complete Features**: Only use cherry-picking for isolated hotfixes or backporting. Use standard merging or rebasing to integrate complete feature branches.
2. **Document the Source**: When cherry-picking, use the `-x` flag (`git cherry-pick -x <hash>`) to automatically append the original commit hash to the new commit message, aiding future history tracking.
3. **Resolve Immediately**: Resolve conflicts immediately on your local release branches and test thoroughly before pushing to production.

### Key Takeaways
- `git cherry-pick` duplicates the changes of a single commit onto your current branch.
- Cherry-picked commits receive new object hashes due to parent history changes.
- Backporting is standard practice for moving fixes to older releases.
- Use `git cherry-pick --continue` or `--abort` to manage conflict flows.

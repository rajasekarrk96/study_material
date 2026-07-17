# Handling Merge Conflicts in Teams — Visual markers and resolution strategies

---

```yaml
lesson_id: GIT-COL-003
lesson_title: "Merge Conflict Handling in Teams"
subject: Git
course: "Git Fundamentals"
module: "Git Collaboration"
difficulty: "⭐⭐⭐"
time_breakdown:
  reading: 15 min
  exercise: 25 min
  quiz: 10 min
  revision: 5 min
version: '1.3'
last_updated: '2026-07-17'
status: Published
author: Rajasekar
reviewed_by: Admin
prerequisites:
- GIT-COL-002 (Syncing Data: Fetch, Pull & Push)
tags:
- Merge Conflicts
- Conflict Resolution
- Git Merge
- Syncing
```

---

## 1. Topics Covered [id: topics]
- Merge conflicts
- Conflict markers
- Resolving conflicts
- Merge abort
- Merge tools
- Rebase conflicts

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - Why merge and rebase conflicts occur when integrating divergent file updates.
  - The different definitions of `HEAD` (ours) vs incoming branches (theirs) during merges and rebases.
- **Skills (What you can do)**:
  - Read complex conflict blocks, navigate git status merge cues, and abort merges.
  - Use visual merge tools and resolve conflicts in local and remote-tracking environments.
- **Professional Outcome**:
  - Coordinate code integrations and collaborate with development teams to resolve conflicts without code loss.

---

## 2. Definitions & Core Concepts [id: definitions]

### Conflict Visualization Diagram
A conflict occurs when two branches modify the **same line** of the **same file** since their last shared ancestor commit:
```text
                          Common Ancestor
                                [A]
                               /   \
                              /     \
                       Branch X     Branch Y
                         [B]          [C]
                          \          /
                           \        /
                            ▼      ▼
                        [Merge Conflict]
             (Same line changed on both branches)
```

### Conflict Resolution Workflow
```text
     Merge Command ──► [Conflict Halt] ──► git status
                                             │
                                             ▼
                                     Edit Conflict File
                                             │
                                             ▼
                                     git add <file>
                                             │
                                             ▼
                                    git merge --continue
                              (or git commit to finalize)
```

### Merge vs. Rebase Conflicts
| Merge | Rebase |
|---|---|
| Conflict occurs during history integration. | Conflict occurs when replaying commits one-by-one. |
| Results in a single **Merge Commit**. | Results in clean, rewritten linear commits. |
| Resume with: `git merge --continue`. | Resume with: `git rebase --continue`. |
| Cancel with: `git merge --abort`. | Cancel with: `git rebase --abort`. |

### Conflict Markers Decoded
When a conflict occurs, Git pauses and writes the competing changes directly into the file:
```text
  <<<<<<< HEAD
  print("Local Branch Version")  # Code in your active branch
  =======                        # Separator line
  print("Incoming Version")      # Code in the incoming merged branch
  >>>>>>> feature-login
```
- **`<<<<<<< HEAD`**: Marks the start of the conflict block containing changes in the active branch (`HEAD`).
- **`=======`**: The boundary line separating both changes.
- **`>>>>>>> <branch_name>`**: Marks the end of the conflict block containing incoming edits.

> [!NOTE]
> Conflict markers separate competing changes from different histories so you can decide how the final merged code should look.

---

### HEAD vs. Theirs Pointer Reference Map
The meanings of `HEAD` (ours) and `theirs` switch depending on whether you are merging or rebasing:
| Operation | HEAD / Ours | Theirs |
|---|---|---|
| **Merge** | Current checked-out branch (active local workspace). | Incoming branch being merged. |
| **Rebase** | Upstream base branch being replayed onto. | Commit currently being replayed. |

---

### Conflict Types
| Conflict Type | Example |
|---|---|
| **Same line edited** | Developer A changes line 5 to X; Developer B changes line 5 to Y. (Most common) |
| **File deleted vs modified** | Developer A modifies `utils.py`; Developer B deletes `utils.py`. |
| **Rename conflict** | Developer A renames `config.py` to `settings.py`; Developer B renames it to `setup.py`. |
| **Binary file conflict** | Overlapping edits in images or compiled binaries (Git cannot merge these automatically). |

---

## 3. Practical Code Examples [id: examples]

### Conflict Commands Cheat Sheet
| Command | Purpose |
|---|---|
| **`git status`** | Queries which files are in conflict and displays the merge state. |
| **`git diff`** | Reviews unresolved conflict sections before editing. |
| **`git diff --name-only --diff-filter=U`** | Shows only the list of conflicted files. |
| **`git merge --abort`** | Aborts the merge process and restores previous commit state. |
| **`git merge --continue`** | Concludes the merge process after files have been resolved and staged. |
| **`git mergetool`** | Launches a configured visual merge tool to resolve conflicts. |

### Example A: Managing conflict status
```bash
# Attempt merge that conflicts
git merge feature-dashboard

# Check active merge status
git status
```

Output:
```text
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")

Unmerged paths:
  both modified:   app.py
```

### Example B: Visual merge tools setup
```bash
# Configure VS Code as the default visual merge tool
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd "code --wait --merge \$LOCAL \$REMOTE \$BASE \$MERGED"

# Launch the visual tool during a conflict
git mergetool
```
*(Note: Enterprise developers often configure visual merge tools like VS Code, Beyond Compare, Meld, IntelliJ IDEA, Visual Studio, or KDiff3 to review local, remote, and baseline content concurrently).*

### Example C: Practical Team Resolution Workflow
```bash
# 1. Trigger merge
git switch main
git merge feature/login-page

# 2. Open app.py, resolve markers, then stage:
git add app.py

# 3. Finish merge using continue or commit
git merge --continue
```

Output:
```text
[main d8e7f6c] Merge branch 'feature/login-page'
```
*(Note: After resolving and staging all conflicted files, complete the merge using `git merge --continue` if prompted, or run `git commit` in workflows where Git expects a normal merge commit).*

---

### Advanced Tip: `git rerere`
Senior developers often enable Git's internal reuse of recorded resolutions (**rerere**) option. When enabled, Git remembers how you resolved a conflict hunk and automatically applies the same resolution when it encounters the exact same conflict again:
```bash
git config --global rerere.enabled true
```

---

## 4. Hands-on Workouts [id: workouts]

### MCQ
- Which command shows only the list of conflicted files during a merge conflict?
  - A) `git diff --conflicted`
  - B) `git diff --name-only --diff-filter=U` (Correct)
  - C) `git branch --unmerged`

### Coding Challenge: Resolving Worksheets
- You are resolving conflicts in `app.py`. Stage the resolved file and conclude the merge.
  - Answer:
    ```bash
    git add app.py
    git merge --continue
    ```

---

### Conflict Prevention Workflow Diagram
Minimizing merge conflicts is a matter of proactive team workflows:
```text
  Feature Branch ──► [Frequent Fetch] ──► [Small Commits] ──► Open PR ──► Easy Merge
```
- **Pull/Fetch Regularly**: Fetch and pull team changes frequently to keep your local branch in sync.
- **Short Branch Lifespans**: Avoid keeping feature branches active for weeks.
- **Atomic Commits**: Edit specific, scoped modules instead of editing multiple global files.
- **Communicate**: Discuss with teammates if you both need to modify the same structural files.

---

## 5. Workout Answers & Solutions [id: answers]

### Common Beginner Mistakes
- **Mistake**: Deleting conflict markers (`<<<<<<<` or `=======`) without actually reviewing the code differences.
  - *Result*: Compiles broken code or overwrites teammate's logic.
- **Mistake**: Forgetting to test the application after resolving conflicts.
  - *Fix*: **Always test your application** locally before running `git add` and completing the merge!
- **Mistake**: Committing files with raw unresolved conflict markers still inside.
  - *Fix*: Git will throw errors on compile/lint. Double-check `git status` before committing.

### Enterprise Best Practices
- **PR Conflicts**: Use Pull Requests (PRs) to detect conflicts on the server (GitHub/GitLab flags conflicts with a banner before merging) before attempting local merges.
- **Branch Strategy**: Resolve conflicts on feature branches whenever possible instead of directly on `main`, unless your team's workflow explicitly requires it.
- **Merge Tool Integration**: Integrate IDE merge editors (VS Code, IntelliJ IDEA, GitLab Merge Editors) to navigate overlaps safely.

### Key Takeaways
- Merge conflicts happen when Git cannot reconcile overlapping file modifications.
- Conflict markers separate competing changes from different histories so you can resolve them.
- The `HEAD` pointer represents the target during merges but represents the upstream during rebases.
- Good communication and frequent syncing minimize team merge conflicts.

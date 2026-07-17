# Advanced Git: Git Flow and Branching Strategies

---

```yaml
lesson_id: GIT-ADV-007
lesson_title: "Advanced Git: Git Flow & Branching Strategies"
subject: Git
course: "Git Fundamentals"
module: "Advanced Workflows"
difficulty: "⭐⭐⭐"
time_breakdown:
  reading: 15 min
  exercise: 15 min
  quiz: 10 min
  revision: 5 min
version: '1.0'
last_updated: '2026-07-17'
status: Published
author: Rajasekar
reviewed_by: Admin
prerequisites:
- GIT-ADV-006 (Advanced Git: Tags & Release Management)
tags:
- Git Flow
- Branching Strategies
- GitHub Flow
- Trunk-Based Development
```

---

## 1. Topics Covered [id: topics]
- Git Flow branching architecture
- GitHub Flow simplicity
- GitLab Flow environment tracking
- Trunk-Based Development pipelines

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - The differences between Git Flow, GitHub Flow, GitLab Flow, and Trunk-Based Development.
  - The roles of main, develop, feature, release, and hotfix branches.
  - When to select a branching strategy based on team size and deployment frequency.
- **Skills (What you can do)**:
  - Configure workspaces to follow feature branch lifecycle patterns.
- **Professional Outcome**:
  - Establish branch management guidelines to ensure team releases run smoothly.

---

## 2. Definitions & Core Concepts [id: definitions]

### Branching Strategies Comparison
| Strategy | Core Concept | Deployment Model | Ideal For |
|---|---|---|---|
| **Git Flow** | Strict branch roles (main, develop, feature, release, hotfix). | Scheduled release cycles. | Desktop applications, legacy enterprise software. |
| **GitHub Flow** | Lightweight feature branches merged directly into `main`. | Continuous Deployment (CD). | Web apps, SaaS products, small agile teams. |
| **GitLab Flow** | GitHub Flow + environmental branches (staging, production). | Gated environment deployments. | Enterprise SaaS with staging environments. |
| **Trunk-Based** | Developers merge small, frequent commits into `main`/trunk daily. | Continuous Integration (CI). | Fast-paced development, senior engineering teams. |

---

### Git Flow Branch Layout
Git Flow defines strict lifetime and temporary branch pathways:
```text
                         Git Flow Architecture
                         
    hotfix/v1.0.1 ─────► [Bugfix] ──────────┐
   (From tag release)                       ▼
                                       
    main ───────────────────────────────► [v1.0.0 Tag] ──────► [v1.0.1 Tag]
                                            ▲
    release/v1.0.0 ──► [Release Prep] ──────┤
                                            │
    develop ─────────► [Merge feature] ─────┴────────────────► [Merge hotfix]
                       ▲
    feature/login ─────┘
   (Created from develop)
```
- **`main`**: Stores official release history.
- **`develop`**: Integration branch for features.
- **`feature/`**: Temporary branches for specific feature developments.
- **`release/`**: Branches for release stabilization and bugfixes.
- **`hotfix/`**: Critical patches derived directly from tags to address live bugs.

---

### Trunk-Based Development (TBD)
In Trunk-Based Development, developers merge code into `main` (the trunk) multiple times a day:
```text
                     Trunk-Based Development
                     
    main/trunk  ─────[Commit]──────[Commit]──────[Merge]──────► (CD Deploy)
                        \            /            ▲
      short feature ─────[Edit]──────┘            │ (Quick Pull Request)
     (short-lived) ───────────────────────────────┘
```
- Features are kept behind **feature flags** (toggles in code) if they are not yet complete, allowing safe integrations into production without deploying unfinished work.

---

## 3. Practical Code Examples [id: examples]

### Example A: Git Flow feature release sequence
```bash
# 1. Start feature branch from develop
git switch develop
git switch -c feature/oauth-login

# 2. Develop, stage, and commit
echo "oauth = true" > oauth.py
git commit -am "feat: add oauth client config"

# 3. Merge feature back to develop
git switch develop
git merge --no-ff feature/oauth-login
git branch -d feature/oauth-login
```

Output:
```text
Merge made by the 'ort' strategy.
 oauth.py | 1 +
 1 file changed, 1 insertion(+)
```

### Example B: Git Flow hotfix release sequence
```bash
# 1. Branch from main at target release tag
git switch main
git switch -c hotfix/payment-error

# 2. Fix the bug, commit
echo "patch = true" > patch.py
git commit -am "fix: resolve payment rounding error"

# 3. Merge hotfix back into both main and develop
git switch main
git merge --no-ff hotfix/payment-error
git tag -a v1.0.1 -m "Hotfix patch 1.0.1"

git switch develop
git merge --no-ff hotfix/payment-error

# 4. Clean up hotfix branch
git branch -d hotfix/payment-error
```

---

## 4. Hands-on Workouts [id: workouts]

### MCQ
- Which branching strategy relies on continuous small merges to main multiple times a day?
  - A) Git Flow
  - B) GitLab Flow
  - C) Trunk-Based Development (Correct)

### Coding Challenge
- Start a feature branch named `feature/user-profile` from the `develop` branch.
  - Answer:
    ```bash
    git switch develop
    git switch -c feature/user-profile
    ```

### Scenario Question: Choosing a strategy
- A team of 3 developers builds a web application deployed to production multiple times a day.
  - Answer: GitHub Flow or Trunk-Based Development, as Git Flow's multiple branch gates would slow down their deployment speed.

---

## 5. Workout Answers & Solutions [id: answers]

### Common Beginner Mistakes
- **Long-lived Features**: Keeping feature branches active for weeks, causing significant merge conflict overhead when integrating back to develop or main.
- **Forgetting develop**: Merging feature branches directly into `main` instead of `develop` when following Git Flow guidelines.

### Enterprise Best Practices
1. **Match Team Workflow**: Choose the branching strategy that matches your deployment speed (e.g. Trunk-Based for SaaS, Git Flow for versioned releases).
2. **Automate Branch Cleanup**: Delete branch references locally and on the server immediately after successful merges.
3. **Use Feature Flags**: In Trunk-Based workflows, wrap half-finished features in feature flags to enable safe continuous integrations.

### Key Takeaways
- Branching strategies provide structure for team collaboration.
- Git Flow uses develop and main branches with release and hotfix gates.
- GitHub Flow is a simpler, feature-branch model designed for rapid releases.
- Trunk-Based Development prioritizes frequent, small integrations directly into main.

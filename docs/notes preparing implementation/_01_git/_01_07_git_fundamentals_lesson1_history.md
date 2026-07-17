# Lesson 1: Version Control History — Core Concepts and Evolution

---

```yaml
lesson_id: GIT-FND-001a
lesson_title: "Version Control History & Evolution"
subject: Git
course: Git Fundamentals
module: Introduction to VCS
difficulty: "\u2B50"
time_breakdown:
  reading: 10 min
  exercise: 10 min
  quiz: 5 min
  revision: 5 min
version: '1.0'
last_updated: '2026-07-17'
status: Published
author: Rajasekar
reviewed_by: Admin
prerequisites:
- Basic command line navigation
tags:
- VCS
- Git Origin
- Distributed
- Centralized
```

---

## 1. Topics Covered [id: topics]
This lesson explores the history and categories of Version Control Systems (VCS). We analyze why version tracking is necessary and trace the evolution from local files and centralized systems to modern distributed systems like Git.

### Learning Outcomes
- **Knowledge (What you will understand)**:
  - The historical progression of VCS (Local, Centralized, Distributed).
  - The key differences between centralized models (SVN) and distributed models (Git).
- **Skills (What you can do)**:
  - Compare system architectures and explain the origin and performance criteria of Git.
- **Outcome (Professional application)**:
  - Select appropriate collaboration models based on security, speed, and network availability.

## 2. Definitions & Core Concepts [id: definitions]
Version control is the practice of tracking and managing changes to software code.
- **Local VCS**: Simple database mapping files to version histories (e.g. RCS). Prone to human errors, like writing to the wrong directory.
- **Centralized VCS (CVCS)**: A single central database server hosting all versioned files. Clients check out files from this central source (e.g. SVN, Perforce). If the server goes down, collaboration halts.
- **Distributed VCS (DVCS)**: Clients fully clone the entire database repository history locally (e.g. Git, Mercurial). Every checkout is a complete backup of the data.

### Internals: Why Git is fast
Because every client has a complete local copy of the repository database, operations like diff, commit, and log run instantly without making network calls.

### Terminology & Glossary
- **VCS**: Version Control System.
- **CVCS**: Centralized Version Control System.
- **DVCS**: Distributed Version Control System.

## 3. Practical Code Examples [id: examples]
### Easy
Check installed version:
```bash
git --version
```

### Medium
Print help parameters for configuration:
```bash
git help config
```

### Advanced
Retrieve internal system parameters:
```bash
git var -l
```

## 4. Hands-on Workouts [id: workouts]
### MCQ
- Which system type clones the complete repository database to each client?
  - A) Centralized
  - B) Distributed (Correct)
  - C) Local

### Coding Challenge
- Run the command to check the installed version of Git.

### Predict the Output
- What does `git --version` output if Git is installed?
  - Output: `git version 2.x.x`

### Debugging Task
- Resolve the terminal error `git: command not found`.
  - Answer: Install Git via package manager or installer.

### Scenario Question
- A team works in an area with poor internet connectivity. Should they use SVN or Git?
  - Answer: Git, because all commits and history views run offline.

### Hands-on Lab
- Open terminal and check your git configuration credentials list using `git config --list`.

## 5. Workout Answers & Solutions [id: answers]
- **Standard Syntax**: `git --version`
- **Aliases**: None.
- **Shortcut**: None.
- **Warning**: Avoid working without VCS in any production repository.

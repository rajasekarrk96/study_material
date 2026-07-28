# 02 Current Syllabus Structure Report — Enterprise Learning OS

**Extraction Date**: July 28, 2026  
**Source Baseline**: Workspaces `_01_git` through `_07_cpp`  

---

## Course 1: Git Version Control (`_01_git`)

### Module 1: Fundamentals & Core Workflow
- **Lesson 1.1**: Version Control History & Evolution
  - *Topics*: VCS vs DVCS, Centralized vs Distributed, Linus Torvalds & Git origins.
- **Lesson 1.2**: Installing & Configuring Git
  - *Topics*: `git config --global`, user.name, user.email, core.editor, SSH vs HTTPS.
- **Lesson 1.3**: Inspecting History: Log & Diff
  - *Topics*: `git log`, `--oneline`, `--graph`, `git diff`, working tree vs staging.
- **Lesson 1.4**: Interactive Staging: Patch Mode & Partial Commits
  - *Topics*: `git add -p`, staging chunks, partial file staging.
- **Lesson 1.5**: Undoing Changes: Reset, Restore & Revert
  - *Topics*: `git restore`, `git reset` (soft, mixed, hard), `git revert`.
- **Lesson 1.6**: Branching Basics & Conflict Resolution
  - *Topics*: `git branch`, `git switch`, `git merge`, 3-way merge, merge conflicts.

### Module 2: Collaboration & Remote Repositories
- **Lesson 2.1**: Remote Repositories & Origin Config
  - *Topics*: `git remote add`, `git remote -v`, origin tracking.
- **Lesson 2.2**: Syncing Data: Fetch, Pull & Push
  - *Topics*: `git fetch`, `git pull --rebase`, `git push -u origin main`.
- **Lesson 2.3**: Merge Conflict Handling in Teams
  - *Topics*: Conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), resolving in IDE.
- **Lesson 2.4**: Forking & Upstream Workflows
  - *Topics*: Open-source PRs, `git remote add upstream`, sync fork.

### Module 3: Advanced Git Internals & Operations
- **Lesson 3.1**: Git Internals: Blobs, Trees & Commits
  - *Topics*: `.git` directory structure, SHA-1/SHA-256 hashes, object database.
- **Lesson 3.2**: Rewriting History: Amend, Rebase & Squash
  - *Topics*: `git commit --amend`, `git rebase -i` (interactive rebase), squashing.
- **Lesson 3.3**: Workspace Helpers: Stash, Bisect & Worktree
  - *Topics*: `git stash`, `git bisect` (binary search bug hunting), `git worktree`.
- **Lesson 3.4**: Git Hooks & Automation
  - *Topics*: Client-side hooks (`pre-commit`, `commit-msg`), husky integration.
- **Lesson 3.5**: Cherry-picking & Backporting
  - *Topics*: `git cherry-pick`, backporting bug fixes across branches.
- **Lesson 3.6**: Tags & Release Management
  - *Topics*: Lightweight vs Annotated tags, Semantic Versioning (SemVer).
- **Lesson 3.7**: Branching Strategies for Teams
  - *Topics*: GitFlow, GitHub Flow, Trunk-Based Development.
- **Lesson 3.8**: Credential Management & Security
  - *Topics*: SSH key generation, GPG commit signing, credential helpers.
- **Lesson 3.9**: Diagnostic & Troubleshooting Guide
  - *Topics*: Reflog recovery (`git reflog`), detached HEAD fix, `git fsck`.

---

## Course 2: Python Programming (`_02_python`)

### Module 1: Python Basics & Syntax
- **Lessons**: Python Overview, Interpreter, Variables, Data Types, Control Flow, Loops, Input/Output.

### Module 2: Data Structures & Built-in Types
- **Lessons**: Lists, Tuples, Sets, Dictionaries, Comprehensions (List/Dict/Set), Strings & Methods.

### Module 3: Functions & Modular Programming
- **Lessons**: Function Def, Positional & Keyword Arguments, `*args` and `**kwargs`, Scope (LEGB rule), Modules & Packages.

### Module 4: Object-Oriented Programming (OOP)
- **Lessons**: Classes & Objects, Constructors (`__init__`), Inheritance, Polymorphism, Encapsulation, Special Methods (`__str__`, `__repr__`).

### Module 5: Exception Handling & File I/O
- **Lessons**: `try...except...finally`, Custom Exceptions, Reading/Writing Files (`open()`, `with` context manager), JSON parsing.

---

## Course 3: Java Software Engineering (`_03_java`)

### Module 1: Java Foundations & Language Syntax
- **Lessons**: JVM, JRE, JDK Architecture, Primitive Types, Control Statements, Arrays, Methods.

### Module 2: Object-Oriented Java
- **Lessons**: Classes & Objects, Encapsulation (Access Modifiers), Inheritance (`extends`), Polymorphism (Overloading vs Overriding), Interfaces & Abstract Classes.

### Module 3: Java Collections Framework
- **Lessons**: `List` (ArrayList, LinkedList), `Set` (HashSet, TreeSet), `Map` (HashMap, TreeMap), Iterators.

### Module 4: Exception Handling & File I/O
- **Lessons**: Checked vs Unchecked Exceptions, `try-catch-finally`, `throws`, File I/O Streams (`BufferedReader`, `FileWriter`).

---

## Course 4: Automated Testing with Selenium (`_04_selenium`)

### Module 1: Selenium WebDriver Fundamentals
- **Lessons**: Architecture, Browser Drivers, Element Locators (ID, Name, Class, XPath, CSS Selectors).

### Module 2: Web Interaction & Synchronization
- **Lessons**: Clicking, Typing, Dropdowns (Select class), Implicit vs Explicit Waits (`WebDriverWait`).

### Module 3: Advanced WebDriver Controls
- **Lessons**: Alert Handling, Frames & Iframes, Multi-Window Switching, Actions Class (Drag and Drop, Mouse Hover).

### Module 4: Test Automation Framework Architecture
- **Lessons**: Page Object Model (POM), TestNG Assertions, Data-Driven Testing (Apache POI Excel), Report Generation.

---

## Course 5: Database Architecture with MySQL (`_05_mysql`)

### Module 1: Relational Database Design & DDL
- **Lessons**: RDBMS Concepts, `CREATE TABLE`, Primary Keys, Foreign Keys, Constraints (`NOT NULL`, `UNIQUE`, `CHECK`).

### Module 2: Data Manipulation & Querying (DML)
- **Lessons**: `INSERT`, `UPDATE`, `DELETE`, `SELECT`, `WHERE` filtering, `LIKE`, `IN`, `BETWEEN`.

### Module 3: Advanced SQL Joins & Aggregations
- **Lessons**: `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`, `GROUP BY`, `HAVING`, Aggregate Functions (`SUM`, `AVG`, `COUNT`, `MIN`, `MAX`).

### Module 4: Database Performance & Indexing
- **Lessons**: Index Types (B-Tree, Hash), Index Creation, Query Optimization basics, Transactions (`COMMIT`, `ROLLBACK`).

---

## Course 6: C Systems Programming (`_06_c`)

### Module 1: C Fundamentals & Compilation Pipeline
- **Lessons**: C History, Setup, `printf`/`scanf`, GCC Pipeline (Preprocessor, Compiler, Assembler, Linker).

### Module 2: Control Flow & Memory Concepts
- **Lessons**: Operators, Conditionals, Loops, Arrays, Strings (`char[]`, `string.h`).

### Module 3: Pointers & Dynamic Memory Allocation
- **Lessons**: Pointer Arithmetic, Pointers & Arrays, `malloc()`, `calloc()`, `realloc()`, `free()`, Memory Leaks.

### Module 4: Custom Types & File I/O
- **Lessons**: `struct`, `union`, `typedef`, File Operations (`fopen`, `fread`, `fwrite`, `fclose`).

---

## Course 7: C++ Object-Oriented Programming (`_07_cpp`)

### Module 1: Transition from C to C++
- **Lessons**: Namespaces, `std::cin` / `std::cout`, References vs Pointers, Function Overloading, Default Arguments.

### Module 2: Object-Oriented C++
- **Lessons**: Classes, Objects, Constructors & Destructors, Copy Constructors, Operator Overloading.

### Module 3: Inheritance & Polymorphism
- **Lessons**: Single & Multiple Inheritance, Virtual Functions, Abstract Classes (Pure Virtual Functions), VTables.

### Module 4: Templates & Standard Template Library (STL)
- **Lessons**: Function Templates, Class Templates, `std::vector`, `std::string`, `std::map`.

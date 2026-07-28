# 04 Updated Master Syllabus Report — Enterprise Learning OS

**Generation Date**: July 28, 2026  
**Status**: Unified Upgrade Target Specification  

This updated syllabus integrates existing lessons with modern technology deltas without duplicating any pre-authored content.

---

## Course 1: Git Version Control & Enterprise Workflows (`_01_git`)

### Module 1: Fundamentals & Core Workflow
- **Lesson 1.1**: Version Control History & Evolution `[Existing]`
- **Lesson 1.2**: Installing & Configuring Git `[Existing]`
- **Lesson 1.3**: Inspecting History: Log & Diff `[Existing]`
- **Lesson 1.4**: Interactive Staging: Patch Mode & Partial Commits `[Existing]`
- **Lesson 1.5**: Undoing Changes: Reset, Restore & Revert `[Existing]`
- **Lesson 1.6**: Branching Basics & Conflict Resolution `[Existing]`

### Module 2: Collaboration & Remote Repositories
- **Lesson 2.1**: Remote Repositories & Origin Config `[Existing]`
- **Lesson 2.2**: Syncing Data: Fetch, Pull & Push `[Existing]`
- **Lesson 2.3**: Merge Conflict Handling in Teams `[Existing]`
- **Lesson 2.4**: Forking & Upstream Workflows `[Existing]`

### Module 3: Advanced Git Internals & Enterprise Security
- **Lesson 3.1**: Git Internals: Blobs, Trees & Commits `[Existing]`
- **Lesson 3.2**: Rewriting History: Amend, Rebase & Squash `[Existing]`
- **Lesson 3.3**: Workspace Helpers: Stash, Bisect & Worktree `[Existing]`
- **Lesson 3.4**: Git Hooks & Automation `[Existing]`
- **Lesson 3.5**: Cherry-picking & Backporting `[Existing]`
- **Lesson 3.6**: Tags & Release Management `[Existing]`
- **Lesson 3.7**: Branching Strategies for Teams `[Existing]`
- **Lesson 3.8**: Credential Management & SSH/GPG Signing `[Expanded]`
- **Lesson 3.9**: Diagnostic & Troubleshooting Guide `[Existing]`
- **Lesson 3.10**: Monorepos & Large Repositories with Git Scalar & LFS `[New]`

---

## Course 2: Python 3.12+ Modern Programming (`_02_python`)

### Module 1: Core Fundamentals & Control Flow
- **Lesson 1.1**: Python Architecture & Setup `[Existing]`
- **Lesson 1.2**: Variables, Types, & Operators `[Existing]`
- **Lesson 1.3**: Strings & String Methods `[Existing]` (Upgrade to f-strings)
- **Lesson 1.4**: Conditionals & Control Flow `[Existing]`
- **Lesson 1.5**: Structural Pattern Matching (`match/case`) `[New]`
- **Lesson 1.6**: Loops & Iteration Constructs `[Existing]`

### Module 2: Advanced Data Structures & Comprehensions
- **Lesson 2.1**: Lists & Tuples Mechanics `[Existing]`
- **Lesson 2.2**: Dictionaries & Sets `[Existing]`
- **Lesson 2.3**: Comprehensions & Generator Expressions `[Existing]`

### Module 3: Functions, Modules, & Functional Tools
- **Lesson 3.1**: Function Declarations & Scope `[Existing]`
- **Lesson 3.2**: First-Class Functions, Lambda & Map/Filter `[Existing]`
- **Lesson 3.3**: Decorators & Higher-Order Functions `[Expanded]`
- **Lesson 3.4**: Generators & `yield` Keyword `[Expanded]`

### Module 4: Object-Oriented Programming & Design Patterns
- **Lesson 4.1**: Classes, Objects & Attributes `[Existing]`
- **Lesson 4.2**: Inheritance & Polymorphism `[Existing]`
- **Lesson 4.3**: Magic Methods (`__init__`, `__str__`, `__repr__`) `[Existing]`
- **Lesson 4.4**: Dataclasses & Pydantic Validation `[New]`

### Module 5: Async Concurrency & Type Hinting (Modern Delta)
- **Lesson 5.1**: Static Type Hinting & Mypy `[New]`
- **Lesson 5.2**: Asyncio Event Loop & `async`/`await` `[New]`
- **Lesson 5.3**: Modern Packaging with `pyproject.toml` & `uv` `[New]`

---

## Course 3: Java 21 LTS Enterprise Development (`_03_java`)

### Module 1: Java Core & Syntax
- **Lesson 1.1**: JVM Architecture & JDK 21 Setup `[Expanded]`
- **Lesson 1.2**: Variables, Data Types & Operators `[Existing]`
- **Lesson 1.3**: Control Statements & Pattern Matching Switch `[Expanded]`

### Module 2: Object-Oriented Programming & Modern Class Types
- **Lesson 2.1**: Classes, Objects & Encapsulation `[Existing]`
- **Lesson 2.2**: Inheritance, Polymorphism & Interfaces `[Existing]`
- **Lesson 2.3**: Immutable Data Records (`record`) `[New]`
- **Lesson 2.4**: Sealed Classes & Interfaces (`sealed`) `[New]`

### Module 3: Collections & Stream API
- **Lesson 3.1**: Java Collections Framework `[Existing]`
- **Lesson 3.2**: Sequenced Collections (`SequencedCollection`) `[New]`
- **Lesson 3.3**: Functional Interfaces & Lambda Expressions `[Existing]`
- **Lesson 3.4**: Java Streams API & Parallel Streams `[Expanded]`

### Module 4: High-Concurrency Virtual Threads (Project Loom)
- **Lesson 4.1**: Platform Threads vs Virtual Threads `[New]`
- **Lesson 4.2**: Structured Concurrency & Scoped Values `[New]`

---

## Course 4: Automated Testing with Selenium 4.x (`_04_selenium`)

### Module 1: Selenium WebDriver 4.x Architecture
- **Lesson 1.1**: W3C WebDriver Protocol & Selenium Manager `[Expanded]`
- **Lesson 1.2**: Element Locators & Relative Locators (`above`, `below`, `near`) `[Expanded]`

### Module 2: Synchronization & Page Object Model
- **Lesson 2.1**: Explicit Waits (`WebDriverWait`) & ExpectedConditions `[Existing]`
- **Lesson 2.2**: Page Object Model (POM) Architecture `[Existing]`

### Module 3: Advanced Browser Automation & CDP Integration
- **Lesson 3.1**: Chrome DevTools Protocol (CDP) Interception `[New]`
- **Lesson 3.2**: Network Interception & Geolocation Spoofing `[New]`
- **Lesson 3.3**: BiDi WebSocket Real-Time Automation `[New]`

---

## Course 5: Database Architecture with MySQL 8.4 (`_05_mysql`)

### Module 1: Relational Schema Design & DDL
- **Lesson 1.1**: RDBMS Architecture & Data Types `[Existing]`
- **Lesson 1.2**: Table Design, Primary & Foreign Keys `[Existing]`

### Module 2: DML & Relational Queries
- **Lesson 2.1**: SELECT, WHERE, GROUP BY, HAVING `[Existing]`
- **Lesson 2.2**: INNER, LEFT, RIGHT, FULL Joins `[Existing]`

### Module 3: Modern Analytical SQL (MySQL 8.0+ Delta)
- **Lesson 3.1**: Analytical Window Functions (`OVER`, `PARTITION BY`, `ROW_NUMBER`) `[New]`
- **Lesson 3.2**: Common Table Expressions (CTEs & Recursive CTEs) `[New]`
- **Lesson 3.3**: Native JSON Data Type & JSON Functions `[New]`

---

## Course 6: C23 Systems Programming (`_06_c`)

### Module 1: C Fundamentals & GCC Compilation
- **Lesson 1.1**: C History & Hello World `[Existing]`
- **Lesson 1.2**: GCC Compilation Lifecycle `[Existing]`
- **Lesson 1.3**: Modern C23 Features (`constexpr`, `typeof`, `auto`) `[New]`

### Module 2: Memory & Pointers
- **Lesson 2.1**: Pointer Arithmetic & Memory Addresses `[Existing]`
- **Lesson 2.2**: Dynamic Memory Allocation (`malloc`, `free`) `[Existing]`

---

## Course 7: C++23 Modern Programming (`_07_cpp`)

### Module 1: Transition to C++ & Modern OOP
- **Lesson 1.1**: Namespaces & I/O Streams `[Existing]`
- **Lesson 1.2**: Classes, Constructors & Destructors `[Existing]`
- **Lesson 1.3**: Virtual Functions & VTables `[Existing]`

### Module 2: Modern C++ Features & Memory Safety
- **Lesson 2.1**: Templates & Metaprogramming `[Existing]`
- **Lesson 2.2**: Smart Pointers (`unique_ptr`, `shared_ptr`) `[New]`
- **Lesson 2.3**: Concepts & Constraints (`requires`) `[New]`
- **Lesson 2.4**: Ranges & Views (`std::ranges`) `[New]`

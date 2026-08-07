# Bash Programming — Master Syllabus

---

# Course Information

**Course Name:** Bash Programming

**Category:** Foundation Course

**Learning Path(s):**
- Foundations
- DevOps & SRE Engineering
- Cloud Computing & Infrastructure
- Linux Administration
- Python Full Stack Engineering

**Difficulty:** Beginner → Intermediate

**Estimated Duration:** 60 Hours

**Prerequisites:**
- Computer Fundamentals
- Linux Fundamentals

**Course Status:** COMING_SOON

---

# Module 1 — Bash Fundamentals

## Lesson 1.1 — What is Bash
**Course Coverage:** 🟢 Covered in Class
### Topics
- History and Evolution of Bash
- The Shell Interface and Prompts
- Interactive vs. Non-Interactive Shells
- CLI Shell Execution Flow

---

## Lesson 1.2 — Writing Your First Script
**Course Coverage:** 🟢 Covered in Class
### Topics
- Shebang Directive (#!/bin/bash)
- Script File Permissions (chmod +x)
- Executing Scripts (Absolute vs. Relative Paths)
- Basic Output Echoing

---

# Module 2 — Variables & Input

## Lesson 2.1 — User Defined Variables
**Course Coverage:** 🟢 Covered in Class
### Topics
- Variable Declarations and Syntax
- Variable Scopes (Global vs. Local)
- Read-Only Constant Declarations
- Exporting Variables to Subshells

---

## Lesson 2.2 — Special Shell Variables
**Course Coverage:** 🟢 Covered in Class
### Topics
- Position Arguments ($0, $1 ... $9)
- Number of Arguments ($#)
- Process Identification PID ($$)
- Exit Status Code ($?)
- Capturing All Arguments ($@, $*)

---

## Lesson 2.3 — User Input
**Course Coverage:** 🟢 Covered in Class
### Topics
- Reading Inputs (read)
- Custom Input Prompts (-p)
- Reading Sensitive Data (-s)
- Input Read Timeouts (-t)

---

# Module 3 — Operators & Control Flow

## Lesson 3.1 — Bash Operators
**Course Coverage:** 🟢 Covered in Class
### Topics
- Arithmetic Operators
- String Comparison Operators
- Logical Evaluation Operators
- Relational Operators

---

## Lesson 3.2 — Conditional Statements
**Course Coverage:** 🟢 Covered in Class
### Topics
- conditional checks (if, else, elif)
- Nested If Structures
- File Type Checks (-f, -d, -e)
- The test Command Syntax

---

## Lesson 3.3 — Case Statements
**Course Coverage:** 🟢 Covered in Class
### Topics
- case Statement Structure
- Menu Programs and Pattern Matching
- Default Cases and Branch Options

---

## Lesson 3.4 — Loops
**Course Coverage:** 🟢 Covered in Class
### Topics
- for Loops
- while Loops
- until Loops
- Infinite Loop Structures

---

## Lesson 3.5 — Loop Control
**Course Coverage:** 🟢 Covered in Class
### Topics
- break Statement
- continue Statement
- exit Commands inside Loops

---

# Module 4 — Functions

## Lesson 4.1 — Bash Functions
**Course Coverage:** 🟢 Covered in Class
### Topics
- Function Declarations and Syntax
- Invoking Functions
- Passing Parameters to Functions

---

## Lesson 4.2 — Function Scope and Return
**Course Coverage:** 🟢 Covered in Class
### Topics
- Local Variables inside Functions (local)
- Return Status Codes (return)
- Capture Function Output (Stdout)
- Recursive Functions

---

## Lesson 4.3 — Modular Scripting
**Course Coverage:** 🟢 Covered in Class
### Topics
- Importing External Files (source, .)
- Structuring Bash Libraries
- Code Reuse and Structuring

---

# Module 5 — Files & Text Processing

## Lesson 5.1 — File Manipulation
**Course Coverage:** 🟢 Covered in Class
### Topics
- Checking File Existence and Types
- Parsing Files Line by Line
- Creating Temporary Files (mktemp)

---

## Lesson 5.2 — Text Search with Grep
**Course Coverage:** 🟢 Covered in Class
### Topics
- grep Command Syntax
- Search Matching Lines (-v, -i, -n)
- Recursive Directory Searches (-r)
- Extended Regular Expressions (-E)

---

## Lesson 5.3 — Text Modification with Sed
**Course Coverage:** 🟢 Covered in Class
### Topics
- sed Stream Editor Basics
- Global Find and Replace Syntax
- In-place File Modification (-i)
- Pattern Deletion and Parsing

---

## Lesson 5.4 — Text Manipulation with Awk
**Course Coverage:** 🟢 Covered in Class
### Topics
- awk Column-based Parsing
- Printing Specific Columns
- Basic Data Filtering and Arithmetic Reports

---

## Lesson 5.5 — File Utilities
**Course Coverage:** 🟢 Covered in Class
### Topics
- Text Formatting (cut, tr)
- Sorting and Uniqueness (sort, uniq)
- Counting Words and Lines (wc)
- Integrating Search Tools (find, xargs)

---

# Module 6 — Automation

## Lesson 6.1 — Command Substitution
**Course Coverage:** 🟢 Covered in Class
### Topics
- Capturing Command Output in Variables
- Legacy Backticks vs. Modern Syntax ($())
- Nesting Command Substitutions

---

## Lesson 6.2 — Pipes & Redirection
**Course Coverage:** 🟢 Covered in Class
### Topics
- Redirecting stdout and stderr (>, >>, 2>, 2>&1)
- Redirection input (<)
- Piping Command Outputs (|)
- Here Documents (<<EOF)

---

## Lesson 6.3 — Trapping Signals
**Course Coverage:** 🟢 Covered in Class
### Topics
- Introduction to Process Signals
- The trap Command
- Executing Script Cleanup Actions on Exit

---

# Module 7 — Cron & Scheduling

## Lesson 7.1 — Scheduled Executions
**Course Coverage:** 🟢 Covered in Class
### Topics
- Crontab Expression Fields
- Script Scheduling via cron
- Redirecting Outputs in cron Jobs
- Scheduling One-time Tasks (at)

---

# Module 8 — Debugging & Error Handling

## Lesson 8.1 — Script Debugging
**Course Coverage:** 🟢 Covered in Class
### Topics
- Running Script in Debug Mode (-x)
- Shell Options (set -e, set -u, set -o pipefail)
- Manual Trace Debugging

---

## Lesson 8.2 — Error Handling
**Course Coverage:** 🟢 Covered in Class
### Topics
- Validating Command Outcomes
- Graceful Failures and Custom Errors
- Printing Warnings to stderr

---

# Module 9 — Advanced Bash

## Lesson 9.1 — Arrays & Associative Arrays
**Course Coverage:** 🟢 Covered in Class
### Topics
- Indexed Arrays Declarations
- Accessing and Modifying Array Elements
- Associative Arrays (declare -A)
- Array Iteration Loops

---

## Lesson 9.2 — String Operations
**Course Coverage:** 🟢 Covered in Class
### Topics
- String Length Operations (${#var})
- String Slicing and Substrings
- Pattern Search and Replace (${var/search/replace})

---

## Lesson 9.3 — ShellCheck
**Course Coverage:** 🟢 Covered in Class
### Topics
- Linting Bash Scripts with ShellCheck
- Recognizing Common Shell Traps
- Code Cleanliness and Optimization

---

# Module 10 — Real World Projects

## Lesson 10.1 — System Health Monitor Project
**Course Coverage:** 🟢 Covered in Class
### Topics
- Scripting a Server Health Auditor (CPU, Memory, Disk)
- Logging Outputs and Checking Limits
- Sending Simulated Alerts

---

## Lesson 10.2 — Backup Automation System Project
**Course Coverage:** 🟢 Covered in Class
### Topics
- Designing an Automated Directory Packing Script
- Compressing Directories and Generating Names
- Implementing Automatic Cleanup Policies

---

## Lesson 10.3 — Log Monitoring Tool
**Course Coverage:** 🟢 Covered in Class
### Topics
- Reading Web Access Logs
- Extracting High-Traffic IPs and Error Statistics
- Printing Structured Console Reports

---

## Lesson 10.4 — Website Status Checker
**Course Coverage:** 🟢 Covered in Class
### Topics
- Scripting Website Reachability Verification (curl)
- Logging Response Codes and Tracking Server Downtime
- Generating Automated Text Status Reports

---

# Software & Tools
- Bash Shell
- VS Code / Vim
- ShellCheck
- Ubuntu Linux / WSL
- curl / mail (utilities)

---

# Hardware Requirements
- Terminal Access to Linux System (Physical or Virtual Machine)

---

# Course Completion Summary
**Estimated Hours:** 60 Hours
**Modules:** 10
**Lessons:** 32
**Topics:** 150+
**Difficulty:** Beginner → Intermediate
**Course Status:** COMING_SOON

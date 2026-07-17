# Lesson 1: Introduction to C — History, Setup, and Hello World

---

```yaml
lesson_id: "C-FND-001"
lesson_title: "Introduction to C: History, Setup & Hello World"
subject: "C"
course: "C Programming Fundamentals"
module: "Introduction & Basics"
difficulty: "⭐"
time_breakdown:
  reading: "10 min"
  exercise: "15 min"
  quiz: "5 min"
  revision: "5 min"
version: "1.0"
last_updated: "2026-07-17"
status: "Published"
author: "Rajasekar"
reviewed_by: "Admin"
prerequisites:
  - "None"
tags:
  - "C Basics"
  - "Hello World"
  - "Console Output"
  - "GCC"
```

---

## 1. Topics Covered [id: topics]
- History and Evolution of C
- Key Features of C Programming Language
- Local Development Toolchain Setup (GCC)
- Writing and Running your first "Hello World" Program
- Anatomy of a C Program

## 2. Definitions & Core Concepts [id: definitions]
- **C Language**: Created in 1972 by Dennis Ritchie at Bell Labs to write the UNIX operating system. It is a compiled, statically-typed, procedural, and mid-level programming language that provides raw access to system memory.
- **Compiler**: A system program that translates human-readable source code text (`.c` files) directly into machine-executable binary instructions.
- **Preprocessor directive (`#include`)**: A command beginning with `#` instructing the preprocessor to load the contents of standard libraries before compiling.
- **Standard Input-Output library (`stdio.h`)**: The core C header file providing function prototypes for handling console operations (like printing text and reading keystrokes).
- **Entrypoint (`main()`)**: The mandatory starting function in every C program where execution begins.
- **Statement Terminator (`;`)**: The semicolon symbol used in C to mark the end of an executable statement.

## 3. Practical Code Examples [id: examples]

### Example A: Basic Hello World C program
- **Code**:
  ```c
  #include <stdio.h>

  int main() {
      printf("Hello, World!\n");
      return 0;
  }
  ```
- **Input (i/p)**: None.
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ Hello, World!                                          │
  │                                                        │
  │ Process exited with status code 0                      │
  └────────────────────────────────────────────────────────┘
  ```

### Example B: Printing multiple lines with escape characters
- **Code**:
  ```c
  #include <stdio.h>

  int main() {
      printf("Welcome to BB Solutions!\n");
      printf("Line 1\n\tTab-indented Line 2\nLine 3\n");
      return 0;
  }
  ```
- **Input (i/p)**: None.
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ Welcome to BB Solutions!                               │
  │ Line 1                                                 │
  │         Tab-indented Line 2                            │
  │ Line 3                                                 │
  │                                                        │
  │ Process exited with status code 0                      │
  └────────────────────────────────────────────────────────┘
  ```

## 4. Hands-on Workouts [id: workouts]
- **Workout 1**: Write a C program that prints your name and company name ("Bytes and Boards Solutions") on two separate lines.
- **Workout 2**: Fix the compile syntax errors in the following code:
  ```c
  #include <stdio.h>
  void main {
      printf("Fix me")
      return 0
  }
  ```

## 5. Workout Answers & Solutions [id: answers]

### Solution to Workout 1:
- **Code**:
  ```c
  #include <stdio.h>

  int main() {
      printf("Rajasekar\n");
      printf("Bytes and Boards Solutions\n");
      return 0;
  }
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ Rajasekar                                              │
  │ Bytes and Boards Solutions                             │
  └────────────────────────────────────────────────────────┘
  ```

### Solution to Workout 2 (Corrected Code):
- **Code**:
  ```c
  #include <stdio.h>

  int main() {
      printf("Fix me\n");
      return 0;
  }
  ```

# Lesson 1: Transitioning to C++ — Namespaces and I/O Stream Buffers

---

```yaml
lesson_id: "CPP-OOP-001"
lesson_title: "Transition to C++: Namespaces & Streams"
subject: "C++"
course: "C++ Object-Oriented Programming"
module: "Transitioning from C"
difficulty: "⭐⭐"
time_breakdown:
  reading: "12 min"
  exercise: "15 min"
  quiz: "5 min"
  revision: "5 min"
version: "1.0"
last_updated: "2026-07-17"
status: "Published"
author: "Rajasekar"
reviewed_by: "Admin"
prerequisites:
  - "C-FND-001 (Introduction to C)"
tags:
  - "C++ Basics"
  - "Namespaces"
  - "Streams"
  - "OOP Intro"
```

---

## 1. Topics Covered [id: topics]
- Introduction to C++ namespaces
- Console I/O stream buffers (`std::cin` & `std::cout`)
- Stream insertion (`<<`) and extraction (`>>`) operators
- Standard namespace scoping (`std::` prefix)
- Fast I/O configuration tricks

## 2. Definitions & Core Concepts [id: definitions]
- **Namespace**: A scope mechanism in C++ used to organize classes and variables into named categories, preventing name collisions.
- **`std` namespace**: The Standard Library namespace in C++ where tools like `cout`, `cin`, and standard vectors reside.
- **I/O Streams**: Continuous flows of bytes between external devices (like consoles) and variables.
- **`std::cout`**: Output stream object representing standard system output buffer.
- **`std::cin`**: Input stream object representing standard system input buffer.
- **Buffer flushing (`std::endl`)**: Inserts a newline character *and* flushes the output stream buffer to the display, which is a slow hardware operation.

## 3. Practical Code Examples [id: examples]

### Example A: Standard Input & Output Streams
- **Code**:
  ```cpp
  #include <iostream>
  #include <string>

  int main() {
      std::string name;
      std::cout << "Enter your name: ";
      std::cin >> name;
      std::cout << "Hello, " << name << "!" << std::endl;
      return 0;
  }
  ```
- **Input (i/p)**: User types `Rajasekar` in the console prompt.
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ Enter your name: Rajasekar                             │
  │ Hello, Rajasekar!                                      │
  │                                                        │
  │ Process exited with status code 0                      │
  └────────────────────────────────────────────────────────┘
  ```

### Example B: Custom Namespaces Scoping
- **Code**:
  ```cpp
  #include <iostream>

  namespace Audio {
      void init() {
          std::cout << "Audio cards ready.\n";
      }
  }

  namespace Video {
      void init() {
          std::cout << "Video framework ready.\n";
      }
  }

  int main() {
      Audio::init();
      Video::init();
      return 0;
  }
  ```
- **Input (i/p)**: None.
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ Audio cards ready.                                     │
  │ Video framework ready.                                 │
  └────────────────────────────────────────────────────────┘
  ```

## 4. Hands-on Workouts [id: workouts]
- **Workout 1**: Create two namespaces: `BB` and `Solutions`. Add a variable `int speed` to both with values `50` and `100`. Print both speeds inside `main()`.
- **Workout 2**: Write a program to read two integers using `cin >> a >> b;` and output their sum using `cout`.

## 5. Workout Answers & Solutions [id: answers]

### Solution to Workout 1:
- **Code**:
  ```cpp
  #include <iostream>

  namespace BB {
      int speed = 50;
  }

  namespace Solutions {
      int speed = 100;
  }

  int main() {
      std::cout << "BB speed: " << BB::speed << "\n";
      std::cout << "Solutions speed: " << Solutions::speed << "\n";
      return 0;
  }
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ BB speed: 50                                           │
  │ Solutions speed: 100                                   │
  └────────────────────────────────────────────────────────┘
  ```

### Solution to Workout 2:
- **Code**:
  ```cpp
  #include <iostream>

  int main() {
      int a, b;
      std::cout << "Enter two numbers: ";
      std::cin >> a >> b;
      std::cout << "Sum: " << (a + b) << std::endl;
      return 0;
  }
  ```
- **Input (i/p)**: `12 8`
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ Enter two numbers: 12 8                                │
  │ Sum: 20                                                │
  └────────────────────────────────────────────────────────┘
  ```

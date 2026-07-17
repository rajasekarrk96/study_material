# Lesson 2: Classes, Objects, and Constructors — Constructor Overloading

---

```yaml
lesson_id: "CPP-OOP-002"
lesson_title: "Classes, Objects & Constructor Overloading"
subject: "C++"
course: "C++ Object-Oriented Programming"
module: "Object Oriented Basics"
difficulty: "⭐⭐"
time_breakdown:
  reading: "15 min"
  exercise: "20 min"
  quiz: "10 min"
  revision: "5 min"
version: "1.0"
last_updated: "2026-07-17"
status: "Published"
author: "Rajasekar"
reviewed_by: "Admin"
prerequisites:
  - "CPP-OOP-001 (Transitioning to C++)"
tags:
  - "Classes"
  - "Objects"
  - "Constructors"
  - "OOP"
```

---

## 1. Topics Covered [id: topics]
- Class declaration blueprints
- Object instantiation in memory
- Constructor functions (Default vs Parameterized)
- Constructor overloading rules
- Initializer list performance advantage

## 2. Definitions & Core Concepts [id: definitions]
- **Class**: A user-defined template or blueprint that packs data attributes and functional behavior together.
- **Object**: A physical runtime instance of a class allocated on the stack or heap memory.
- **Constructor**: A special class member function automatically triggered upon object birth, sharing the class name and having no return type.
- **Constructor Overloading**: Having multiple constructors with different parameter patterns to initialize objects differently.
- **Initializer List**: A colon-prefixed list running before the constructor body that initializes member variables directly.

## 3. Practical Code Examples [id: examples]

### Example A: Constructor Overloading with Initializer Lists
- **Code**:
  ```cpp
  #include <iostream>
  #include <string>

  class Account {
  public:
      std::string owner;
      double balance;

      // 1. Default Constructor
      Account() : owner("Guest"), balance(0.0) {
          std::cout << "Default Init\n";
      }

      // 2. Parameterized Constructor
      Account(std::string name, double bal) : owner(name), balance(bal) {
          std::cout << "Custom Init\n";
      }
  };

  int main() {
      Account acc1;
      Account acc2("Rajasekar", 5000.0);
      return 0;
  }
  ```
- **Input (i/p)**: None.
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ Default Init                                           │
  │ Custom Init                                            │
  └────────────────────────────────────────────────────────┘
  ```

### Example B: Copy Constructor Deep Copy
- **Code**:
  ```cpp
  #include <iostream>

  class Box {
  public:
      int* size;

      Box(int s) {
          size = new int(s);
      }

      // Copy Constructor (Deep Copy)
      Box(const Box& source) {
          size = new int(*source.size);
          std::cout << "Deep Copy executed\n";
      }

      ~Box() {
          delete size;
      }
  };

  int main() {
      Box box1(10);
      Box box2 = box1; // Triggers Copy Constructor
      return 0;
  }
  ```
- **Input (i/p)**: None.
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ Deep Copy executed                                     │
  └────────────────────────────────────────────────────────┘
  ```

## 4. Hands-on Workouts [id: workouts]
- **Workout 1**: Create a class `Car` with attributes `brand` and `year`. Implement a default constructor setting brand to "Toyota" and year to 2020. Overload it with a parameterized constructor.
- **Workout 2**: Fix this compiler error:
  ```cpp
  class Point {
      int x;
      Point(int val) : x(val) {}
  };
  int main() { Point p(10); }
  ```

## 5. Workout Answers & Solutions [id: answers]

### Solution to Workout 1:
- **Code**:
  ```cpp
  #include <iostream>
  #include <string>

  class Car {
  public:
      std::string brand;
      int year;

      Car() : brand("Toyota"), year(2020) {}
      Car(std::string b, int y) : brand(b), year(y) {}
  };

  int main() {
      Car c1;
      Car c2("Honda", 2025);
      std::cout << c1.brand << " (" << c1.year << ")\n";
      std::cout << c2.brand << " (" << c2.year << ")\n";
      return 0;
  }
  ```
- **Output (o/p)**:
  ```text
  ┌────────────────────────────────────────────────────────┐
  │                        CONSOLE                         │
  ├────────────────────────────────────────────────────────┤
  │ Toyota (2020)                                          │
  │ Honda (2025)                                           │
  └────────────────────────────────────────────────────────┘
  ```

### Solution to Workout 2 (Corrected Code):
- **Code**:
  ```cpp
  class Point {
  public: // Added public access specifier so constructor can be accessed externally
      int x;
      Point(int val) : x(val) {}
  };

  int main() {
      Point p(10);
      return 0;
  }
  ```

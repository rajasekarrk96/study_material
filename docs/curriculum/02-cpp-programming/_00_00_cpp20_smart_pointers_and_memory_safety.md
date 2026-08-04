# Cpp20 Smart Pointers And Memory Safety

> **Course**: Git Fundamentals | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐⭐ Advanced
- **Prerequisites**: C++ Pointers & Classes
- **XP Reward**: +70 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Implement the **RAII (Resource Acquisition Is Initialization)** design pattern.
2. Manage exclusive resource ownership using **`std::unique_ptr`** and `std::make_unique()`.
3. Manage shared reference-counted ownership using **`std::shared_ptr`** and `std::make_shared()`.
4. Prevent circular reference memory leaks using **`std::weak_ptr`**.
5. Ban raw `new` and `delete` operations in modern C++ codebases.

---

---

Ensure a C++20 standard compiler (GCC 11+, Clang 13+, MSVC) is active.

---

---

### 3.1 RAII & Smart Pointers
Raw pointers (`T* ptr = new T()`) require manual `delete ptr;` invocations, leading to memory leaks, double-free crashes, and dangling pointers.

Modern C++ enforces **RAII**: object lifetimes are tied to stack scope. When a **Smart Pointer** goes out of scope, its destructor automatically frees the heap memory:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          SMART POINTER TYPES MATRIX                         │
├─────────────────┬──────────────────────────────────┬────────────────────────┤
│ Smart Pointer   │ Ownership Semantics              │ Performance Overhead   │
├─────────────────┼──────────────────────────────────┼────────────────────────┤
│ `std::unique_ptr`│ Exclusive (Single owner)        │ ZERO (Same as raw pointer)│
│ `std::shared_ptr`│ Shared (Atomic Ref Counted)     │ Control Block + Atomic │
│ `std::weak_ptr`  │ Non-owning observer              │ Inspects shared_ptr    │
└─────────────────┴──────────────────────────────────┴────────────────────────┘
```

---

---

```mermaid
flowchart TD
    Ptr1[std::shared_ptr 1] --> ControlBlock["Control Block: Reference Count = 2"]
    Ptr2[std::shared_ptr 2] --> ControlBlock
    ControlBlock --> HeapObj[Heap Managed Object]
    WeakPtr[std::weak_ptr] -.->|Non-owning Observation| ControlBlock
```

---

---

```cpp
#include <iostream>
#include <memory>

class SensorNode {
public:
    std::string name;
    SensorNode(std::string n) : name(n) {
        std::cout << "[Constructor] Sensor initialized: " << name << "\n";
    }
    ~SensorNode() {
        std::cout << "[Destructor] Sensor auto-freed: " << name << "\n";
    }
    void readData() {
        std::cout << name << " reading telemetry...\n";
    }
};

int main() {
    // 1. Exclusive Ownership (std::unique_ptr)
    {
        auto u_sensor = std::make_unique<SensorNode>("ESP32-Exclusive");
        u_sensor->readData();
        // Move ownership (cannot copy!)
        std::unique_ptr<SensorNode> u_sensor2 = std::move(u_sensor);
    } // Destructor automatically called here as u_sensor2 goes out of scope!

    // 2. Shared Ownership (std::shared_ptr)
    std::shared_ptr<SensorNode> s_sensor1 = std::make_shared<SensorNode>("Gateway-Shared");
    {
        std::shared_ptr<SensorNode> s_sensor2 = s_sensor1;
        System.out.println("Use Count: " + s_sensor1.use_count()); // 2
    } // s_sensor2 scope ends, count drops back to 1
    
    std::cout << "Final Use Count: " << s_sensor1.use_count() << "\n";
    return 0; // Heap memory automatically freed!
}
```

---

---

- **Autonomous Vehicle Vision Engines**: High-frequency image buffer pipelines use `std::unique_ptr` to pass frame buffers between thread queues with zero copying and zero memory leak risks.

---

---

1. Save code as `smart_ptr_demo.cpp`.
2. Compile and run: `g++ -std=c++20 smart_ptr_demo.cpp -o smart_ptr_demo && ./smart_ptr_demo`.

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Circular Reference Memory Leak** | Two `shared_ptr` objects referencing each other (A $\leftrightarrow$ B), preventing count from reaching 0. | Replace one side of the circular reference with `std::weak_ptr`. |

---

---

- **Prefer `std::unique_ptr` by Default**: Use `unique_ptr` first; only switch to `shared_ptr` if shared ownership is explicitly required.

---

---

### Q1: What is the difference between `std::unique_ptr` and `std::shared_ptr`?
**Answer**: `std::unique_ptr` maintains strict exclusive ownership of a heap resource with zero runtime overhead; it cannot be copied, only moved. `std::shared_ptr` allows multiple owners to share a resource using atomic reference counting, freeing the resource when the reference count drops to zero.

---

---

```json
{
  "quiz_title": "Lesson 2.4 Smart Pointers Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which factory function is preferred for creating a `std::unique_ptr`?",
      "options": ["new unique_ptr()", "std::make_unique()", "std::create_unique()", "malloc()"],
      "correct_answer_index": 1,
      "explanation": "std::make_unique() is the safe factory function for unique_ptr."
    }
  ]
}
```

---

---

Build an exception-safe RAII File Handle wrapper using `std::unique_ptr` with custom deleter `fclose`.

---

---

**Front**: How do you transfer ownership of a `std::unique_ptr`?
**Back**: Using `std::move()` (e.g. `ptr2 = std::move(ptr1)`).
<!-- flashcard:end -->

---

---

```cpp
auto ptr = std::make_unique<Sensor>("Node1");
```

---

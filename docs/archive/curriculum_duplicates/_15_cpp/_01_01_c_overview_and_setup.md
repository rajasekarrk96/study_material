# C++ Overview and Setup

> **Course**: Cpp | **Module**: C++ Fundamentals | **Difficulty**: beginner

---

C++ is a **general-purpose, multi-paradigm** language (procedural, OOP, generic, functional) developed by Bjarne Stroustrup as a superset of C. Key features: **RAII**, zero-overhead abstractions, templates, STL.

---

| Standard | Key Features |
|---|---|
| C++11 | Move semantics, lambdas, auto, range-for, `nullptr`, smart pointers |
| C++14 | Generic lambdas, return type deduction |
| C++17 | Structured bindings, `if constexpr`, `std::optional`, `std::variant` |
| C++20 | Concepts, ranges, coroutines, modules, `std::span` |
| C++23 | `std::expected`, `std::flat_map`, stackful coroutines |

---

```bash
# Install GCC
sudo apt install g++ build-essential

# Compile
g++ -std=c++20 -Wall -Wextra -o hello hello.cpp
./hello

# CMakeLists.txt
cmake_minimum_required(VERSION 3.20)
project(MyApp CXX)
set(CMAKE_CXX_STANDARD 20)
add_executable(hello hello.cpp)
```

---

```cpp
#include <iostream>
#include <format>   // C++20

int main() {
    std::cout << "Hello, World!" << std::endl;
    std::cout << std::format("C++ is {} years old!\n", 2024 - 1979);
    return 0;
}
```

---

**Resource Acquisition Is Initialization** — resources (memory, files, locks) are acquired in constructors and released in destructors automatically.

```cpp
// Classic C — must remember to close!
FILE *f = fopen("file.txt", "r");
// ... use f ...
fclose(f);

// C++ RAII — auto-closed on scope exit
{
    std::ifstream f("file.txt");
    // ... use f ...
}   // f.~ifstream() called — file closed!
```

---

1. Write `hello.cpp` that uses `std::cout`, compile with `-std=c++20`
2. Create a `CMakeLists.txt` and build using `cmake .. && make`
3. Demonstrate RAII by creating a `TimedScope` class that measures execution time

---

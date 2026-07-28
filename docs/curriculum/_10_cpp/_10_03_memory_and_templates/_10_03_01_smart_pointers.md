---
id: "10_03_01"
title: "Smart Pointers"
course: "C++"
module: 3
module_title: "Modern C++ Memory"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["unique_ptr", "shared_ptr", "weak_ptr", "make_unique", "make_shared", "RAII", "ownership", "custom-deleter"]
prerequisites: []
lab_required: true
---

# Smart Pointers

## unique_ptr — Exclusive Ownership

```cpp
#include <memory>

// Create
auto p = std::make_unique<int>(42);         // preferred
auto arr = std::make_unique<int[]>(100);    // array

// Use
std::cout << *p << "\n";   // 42
*p = 100;

// Transfer ownership (move only — not copyable)
auto p2 = std::move(p);    // p is now nullptr
// p  = nullptr
// p2 = owns the int

// Custom deleter
auto file = std::unique_ptr<FILE, decltype(&fclose)>(
    fopen("file.txt", "r"), fclose
);
```

## shared_ptr — Shared Ownership

```cpp
auto sp1 = std::make_shared<std::string>("shared data");
auto sp2 = sp1;     // ref count = 2
auto sp3 = sp1;     // ref count = 3

sp1.use_count()     // 3
sp1.reset();        // ref count = 2
// sp2 and sp3 still valid
// Memory freed when last shared_ptr destroyed

// shared_ptr in container
std::vector<std::shared_ptr<Node>> nodes;
nodes.push_back(std::make_shared<Node>(1));
```

## weak_ptr — Non-Owning Reference

```cpp
// Breaks cycles! (parent-child cycle would leak with shared_ptr)
struct Node {
    int value;
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev;   // non-owning back-pointer
};

// Use weak_ptr
std::weak_ptr<Widget> weak = shared_ptr_widget;
if (auto locked = weak.lock()) {  // lock() returns shared_ptr or nullptr
    locked->doSomething();
} else {
    std::cout << "Object destroyed!\n";
}
```

## Ownership Guidelines

| Need | Tool |
|---|---|
| Single owner | `unique_ptr` |
| Shared ownership | `shared_ptr` |
| Non-owning reference to shared | `weak_ptr` |
| Stack object | Direct (no pointer) |
| Raw pointer | Observer/non-owning only |
| Raw `new` | Avoid! |

## Lab Exercise
1. Implement a linked list using `unique_ptr<Node>` for ownership
2. Show a `shared_ptr` cycle leak, fix it with `weak_ptr`
3. Build a tree structure with `shared_ptr` children and `weak_ptr` parent

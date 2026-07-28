---
id: "10_01_02"
title: "References and Value Types"
course: "C++"
module: 1
module_title: "C++ Fundamentals"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["reference", "lvalue", "rvalue", "move-semantics", "std::move", "perfect-forwarding", "auto", "decltype"]
prerequisites: []
lab_required: true
---

# References and Value Types

## References

```cpp
int x = 42;
int &ref = x;    // lvalue reference — must bind at declaration

ref = 100;       // modifies x!
std::cout << x;  // 100

// Const reference — does not allow modification
const int &cref = x;
// cref = 50;   // compile error

// Reference in function (avoids copy)
void double_value(int &n) { n *= 2; }
double_value(x);   // x is now 200

// Const reference parameter (safe, no copy)
void print(const std::string &s) { std::cout << s; }
```

## Value Categories: lvalue vs rvalue

```cpp
int x = 42;         // x is lvalue (has address)
42;                  // rvalue (temporary, no address)

// lvalue reference: int &r = x;   OK
// int &r = 42;    ERROR — can't bind lvalue-ref to rvalue

// rvalue reference (C++11)
int &&rref = 42;   // OK
int &&rref2 = std::move(x);  // move x as rvalue
```

## Move Semantics

```cpp
class Buffer {
    int *data;
    size_t size;
public:
    // Copy constructor — expensive!
    Buffer(const Buffer &other) : size(other.size) {
        data = new int[size];
        std::copy(other.data, other.data+size, data);
    }

    // Move constructor — cheap! (steal pointer)
    Buffer(Buffer &&other) noexcept
        : data(other.data), size(other.size) {
        other.data = nullptr;   // leave source empty
        other.size = 0;
    }

    ~Buffer() { delete[] data; }
};

Buffer a(1000);
Buffer b = std::move(a);   // move, not copy
// a.data is now nullptr — don't use a!
```

## auto and decltype

```cpp
auto x = 42;                // int
auto y = 3.14;              // double
auto z = std::string{"hi"}; // std::string

// auto in range-for
for (auto &item : container) { /* ... */ }
for (const auto &[key, value] : map) { /* C++17 structured binding */ }

// decltype — type of an expression without evaluating
decltype(x) copy = x;     // same type as x
auto result = compute();
decltype(result) backup;
```

## Lab Exercise
1. Show that passing `std::string` by value vs const-ref has different copy costs (with counter)
2. Implement a simple `UniqueResource<T>` with move constructor and deleted copy constructor
3. Use structured bindings to iterate a `std::map<std::string, int>`

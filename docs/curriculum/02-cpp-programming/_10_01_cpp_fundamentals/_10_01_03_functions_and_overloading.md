---
id: "10_01_03"
title: "Functions and Overloading"
course: "C++"
module: 1
module_title: "C++ Fundamentals"
lesson: 3
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["overloading", "default-arguments", "inline", "constexpr", "lambda", "std::function", "trailing-return"]
prerequisites: []
lab_required: true
---

# Functions and Overloading

## Function Overloading

```cpp
int    add(int a, int b)       { return a + b; }
double add(double a, double b) { return a + b; }
std::string add(const std::string &a, const std::string &b) { return a + b; }

add(1, 2)           // int version
add(1.5, 2.5)       // double version
add("Hello", " World")  // string version
```

## Default Arguments

```cpp
void connect(const std::string &host,
             int port = 8080,
             bool ssl = false) {
    std::cout << (ssl ? "https" : "http") << "://" << host << ":" << port;
}

connect("example.com");            // port=8080, ssl=false
connect("example.com", 443, true); // https://example.com:443
```

## constexpr Functions

```cpp
// Evaluated at compile-time when possible
constexpr int factorial(int n) {
    return n <= 1 ? 1 : n * factorial(n - 1);
}

constexpr int fact5 = factorial(5);  // computed at compile time
int arr[factorial(4)];               // OK: compile-time constant
```

## Lambda Expressions

```cpp
// [capture](params) -> return_type { body }
auto square = [](int x) { return x * x; };
square(5)   // 25

// Capture by value
int threshold = 10;
auto above = [threshold](int x) { return x > threshold; };

// Capture by reference
int count = 0;
auto counter = [&count]() { ++count; };

// Generic lambda (C++14)
auto add = [](auto a, auto b) { return a + b; };
add(1, 2)         // int
add(1.5, 2.5)     // double
add(std::string{"Hello"}, std::string{" World"})

// std::function
std::function<int(int, int)> op;
op = [](int a, int b) { return a + b; };
op = add_function;    // can hold any callable
```

## Lab Exercise
1. Overload `toString()` for int, double, bool, and vector
2. Write a `Timer` function using `std::function` that measures any callable
3. Implement `compose(f, g)` that returns a lambda `h(x) = f(g(x))`

---
id: "10_03_02"
title: "Templates"
course: "C++"
module: 3
module_title: "Modern C++ Memory"
lesson: 2
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["template", "class-template", "function-template", "specialization", "SFINAE", "concepts", "variadic-template", "type-traits"]
prerequisites: []
lab_required: true
---

# Templates

## Function Templates

```cpp
template <typename T>
T max_val(T a, T b) {
    return (a > b) ? a : b;
}

max_val(3, 7)            // int
max_val(3.14, 2.71)      // double
max_val<float>(1.5f, 2.5f)  // explicit instantiation

// Multiple type parameters
template <typename T, typename U>
auto add(T a, U b) -> decltype(a + b) {
    return a + b;
}
```

## Class Templates

```cpp
template <typename T, int Capacity = 10>
class FixedStack {
    T data_[Capacity];
    int top_ = 0;
public:
    void push(const T &val) {
        if (top_ >= Capacity) throw std::overflow_error("Stack full");
        data_[top_++] = val;
    }

    T pop() {
        if (top_ == 0) throw std::underflow_error("Stack empty");
        return data_[--top_];
    }

    int size() const { return top_; }
    bool empty() const { return top_ == 0; }
};

FixedStack<int, 5> istack;
FixedStack<std::string> sstack;   // uses default capacity 10
```

## Concepts (C++20)

```cpp
// Define concept
template <typename T>
concept Numeric = std::is_arithmetic_v<T>;

template <typename T>
concept Sortable = requires(T &container) {
    container.begin();
    container.end();
    { *container.begin() } -> std::totally_ordered;
};

// Use in function
template <Numeric T>
T square(T x) { return x * x; }

square(5)      // OK
square("hi")   // compile error — "string" does not satisfy Numeric
```

## Variadic Templates

```cpp
// Base case
void print() {}

// Recursive case
template <typename T, typename... Rest>
void print(T first, Rest... rest) {
    std::cout << first;
    if constexpr (sizeof...(rest) > 0) std::cout << ", ";
    print(rest...);
}

print(1, 3.14, "hello", true);   // 1, 3.14, hello, 1
```

## Lab Exercise
1. Implement a generic `Pair<T,U>` with `swap()`, `operator==`, and `make_pair`
2. Write a `TypeList<Types...>` that computes `size` and `get<N>` at compile time
3. Use Concepts to constrain a `BinaryTree<T>` to only accept `std::totally_ordered` types

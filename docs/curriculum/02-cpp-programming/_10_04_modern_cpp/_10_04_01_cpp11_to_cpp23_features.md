---
id: "10_04_01"
title: "C++11 to C++23 Features"
course: "C++"
module: 4
module_title: "Modern C++"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["auto", "constexpr", "nullptr", "range-for", "initializer_list", "optional", "variant", "any", "expected", "span"]
prerequisites: []
lab_required: true
---

# C++11 to C++23 Features

## C++11 Essentials

```cpp
// auto type deduction
auto x = 42;
auto it = container.begin();

// Range-based for
for (const auto &item : container) { /* ... */ }

// nullptr (replaces NULL)
int *p = nullptr;

// Initializer lists
std::vector<int> v = {1, 2, 3, 4, 5};

// Move semantics — std::move, std::forward
// Lambda expressions — [capture](params){ body }
// constexpr — compile-time evaluation
// Smart pointers — unique_ptr, shared_ptr, weak_ptr
```

## C++17 Features

```cpp
// std::optional — nullable value without pointer
std::optional<int> find_value(int key) {
    if (auto it = map.find(key); it != map.end())
        return it->second;
    return std::nullopt;
}

auto val = find_value(42);
if (val) std::cout << *val;
val.value_or(0);   // default if nullopt

// std::variant — type-safe union
std::variant<int, double, std::string> v;
v = 42;
v = 3.14;
v = "hello";
std::get<std::string>(v)       // "hello"
std::holds_alternative<int>(v) // false
std::visit([](auto &&val){ std::cout << val; }, v);

// Structured bindings
auto [key, value] = *map.begin();
auto [x, y, z] = std::tuple{1, 2.0, "three"};

// if/switch with initializer
if (auto it = m.find("key"); it != m.end()) {
    use(it->second);
}
```

## C++20 Features

```cpp
// Concepts
template <std::integral T>
T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

// std::span — non-owning view of contiguous data
void process(std::span<const int> data) {
    for (int x : data) { /* ... */ }
}
process(std::vector<int>{1,2,3});
process(std::array<int,3>{1,2,3});

// Ranges
auto evens = std::views::iota(1, 101)
           | std::views::filter([](int n){ return n%2==0; });
```

## C++23 Features

```cpp
// std::expected — error handling without exceptions
std::expected<int, std::string> parse_int(std::string_view s) {
    try { return std::stoi(std::string{s}); }
    catch (...) { return std::unexpected("Not a number: " + std::string{s}); }
}

auto result = parse_int("42");
if (result) std::cout << *result;    // 42
else std::cout << result.error();   // "Not a number: ..."
```

## Lab Exercise
1. Replace raw pointer with `optional<T>` in a find function, handle nullopt gracefully
2. Implement a `Result<T, E>` type using `std::variant` (before C++23)
3. Process a data pipeline using C++20 ranges: filter → transform → take → to vector

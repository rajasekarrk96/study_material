---
id: "10_03_03"
title: "STL Containers and Algorithms"
course: "C++"
module: 3
module_title: "Modern C++ Memory"
lesson: 3
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["vector", "map", "set", "unordered_map", "array", "deque", "list", "algorithm", "sort", "find", "transform", "ranges"]
prerequisites: []
lab_required: true
---

# STL Containers and Algorithms

## Key STL Containers

```cpp
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <array>
#include <deque>

std::vector<int> v = {3, 1, 4, 1, 5, 9};
v.push_back(2);
v.emplace_back(6);             // construct in-place
v.reserve(100);                // pre-allocate
v.size(); v.empty(); v.front(); v.back();

std::map<std::string, int> m;   // sorted by key O(log n)
m["Alice"] = 95;
m.find("Alice")               // iterator or end()
m.count("Bob")                // 0 or 1
m.emplace("Carol", 88);

std::unordered_map<std::string, int> um;  // O(1) average
um.reserve(100);

std::set<int> s = {3,1,4,1,5};  // sorted unique: {1,3,4,5}
s.insert(9);
s.count(1);   // 1 or 0

std::array<int, 5> arr = {1,2,3,4,5};   // fixed-size, no heap
```

## Algorithms

```cpp
#include <algorithm>
#include <numeric>

std::vector<int> v = {3,1,4,1,5,9,2,6};

std::sort(v.begin(), v.end());                 // ascending
std::sort(v.begin(), v.end(), std::greater{}); // descending

std::find(v.begin(), v.end(), 5);  // iterator to 5
std::count(v.begin(), v.end(), 1); // 2
std::binary_search(v.begin(), v.end(), 9); // true (must be sorted)

std::transform(v.begin(), v.end(), v.begin(), [](int x){ return x*x; });

std::accumulate(v.begin(), v.end(), 0);        // sum
std::reduce(v.begin(), v.end());               // faster, parallel-friendly

std::partition(v.begin(), v.end(), [](int x){ return x%2==0; });
std::remove_if(v.begin(), v.end(), [](int x){ return x<3; }); // + erase!
v.erase(std::remove_if(v.begin(), v.end(), pred), v.end());    // erase-remove
```

## Ranges (C++20)

```cpp
#include <ranges>
namespace rv = std::views;

std::vector<int> nums = {1,2,3,4,5,6,7,8,9,10};

// Lazy pipeline
auto result = nums
    | rv::filter([](int n){ return n % 2 == 0; })
    | rv::transform([](int n){ return n * n; })
    | rv::take(3);

for (int n : result) std::cout << n << " ";  // 4 16 36
```

## Lab Exercise
1. Find the top 5 most frequent words in a text using `unordered_map` + `partial_sort`
2. Implement a priority queue using `std::vector` + `std::make_heap`
3. Rewrite a series of loops as a ranges pipeline

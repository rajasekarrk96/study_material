---
id: "02_06_02"
title: "Generators and Iterators"
course: "Python"
module: 6
module_title: "Advanced Python"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["generator", "yield", "send", "throw", "close", "StopIteration", "iterator-protocol", "__iter__", "__next__", "itertools", "infinite-generator"]
prerequisites: []
lab_required: true
---

# Generators and Iterators


## The Iterator Protocol

Any object implementing `__iter__()` and `__next__()` is an iterator.

```python
class CountUp:
    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self   # iterator returns itself

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current

for n in CountUp(5):
    print(n)   # 1 2 3 4 5
```

## Generator Functions

A generator function uses `yield` to produce values **lazily**.

```python
def fibonacci():
    a, b = 0, 1
    while True:         # infinite generator
        yield a
        a, b = b, a + b

gen = fibonacci()
[next(gen) for _ in range(10)]   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Finite generator
def evens_up_to(n):
    for i in range(0, n+1, 2):
        yield i

list(evens_up_to(10))   # [0, 2, 4, 6, 8, 10]
```

## Generator Expressions

```python
# Lazy — memory efficient
gen = (x**2 for x in range(1_000_000))
sum(gen)    # computes without storing all squares

# Chaining generators (pipeline)
raw    = (line.strip() for line in open("data.txt"))
nonempty = (line for line in raw if line)
parsed = (line.split(",") for line in nonempty)
```

## yield with send() and throw()

```python
def accumulator():
    total = 0
    while True:
        value = yield total    # yield sends current, receives new
        if value is None:
            break
        total += value

gen = accumulator()
next(gen)       # 0  — prime the generator
gen.send(10)    # 10
gen.send(20)    # 30
gen.send(5)     # 35
```

## itertools — Powerful Combinators

```python
import itertools

# Infinite iterators
itertools.count(1, 2)                  # 1, 3, 5, 7, ...
itertools.cycle([1, 2, 3])            # 1, 2, 3, 1, 2, 3, ...
itertools.repeat("x", 3)              # "x", "x", "x"

# Combinatoric generators
list(itertools.permutations("ABC", 2))  # all 2-char permutations
list(itertools.combinations("ABC", 2))  # all 2-char combinations
list(itertools.product([1,2], [3,4]))   # cartesian product

# Slicing/chaining
itertools.islice(fibonacci(), 10)       # first 10 Fibonacci numbers
itertools.chain([1,2], [3,4], [5,6])   # [1,2,3,4,5,6]
itertools.takewhile(lambda x: x<5, count(1))  # 1,2,3,4
itertools.dropwhile(lambda x: x<5, count(1))  # 5,6,7,...

# Grouping
for key, group in itertools.groupby(sorted_data, key=lambda x: x.category):
    print(key, list(group))
```

## Memory Comparison

```python
import sys, tracemalloc

tracemalloc.start()
# List: all in memory at once
result = [x**2 for x in range(10**6)]
print(tracemalloc.get_peak())   # ~8MB

tracemalloc.clear_traces()
# Generator: O(1) memory
result = sum(x**2 for x in range(10**6))
print(tracemalloc.get_peak())   # ~1KB
```

## Lab Exercise
1. Build a `chunked(iterable, size)` generator that yields chunks
2. Implement a pipeline: read CSV lines → filter → parse → aggregate
3. Create a generator-based `tree_walk(node)` for a nested dict

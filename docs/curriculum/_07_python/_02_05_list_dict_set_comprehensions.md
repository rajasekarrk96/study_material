---
id: "02_05_03"
title: "List Dict Set Comprehensions"
course: "Python"
module: 5
module_title: "Functions"
lesson: 3
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["list-comprehension", "dict-comprehension", "set-comprehension", "generator-expression", "nested", "conditional", "walrus"]
prerequisites: []
lab_required: true
---

# List Dict Set Comprehensions


## Comprehension Syntax

```
[expression   for var in iterable if condition]   # list
{expression   for var in iterable if condition}   # set
{k: v         for var in iterable if condition}   # dict
(expression   for var in iterable if condition)   # generator
```

## List Comprehensions

```python
# Basic
squares = [x**2 for x in range(1, 11)]

# With condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]

# Multiple iterables
pairs = [(x, y) for x in [1,2,3] for y in ['a','b'] if x != 2]

# Flatten 2D matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [val for row in matrix for val in row]

# With walrus — compute once, use twice
results = [y for x in data if (y := transform(x)) > threshold]
```

## Dict Comprehensions

```python
# Invert a dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}

# Transform values
discounted = {name: price * 0.9 for name, price in prices.items()}

# Filter entries
active = {k: v for k, v in users.items() if v["active"]}

# Build from two lists
keys   = ["name", "age", "city"]
values = ["Raja",  28,   "Chennai"]
record = {k: v for k, v in zip(keys, values)}
```

## Set Comprehensions

```python
unique_lengths = {len(word) for word in words}
vowels_used = {c.lower() for c in text if c.lower() in "aeiou"}
```

## Generator Expressions

```python
# Lazy — compute on demand, don't store all in memory
gen = (x**2 for x in range(1_000_000))
next(gen)           # 0
next(gen)           # 1

# Pass directly to functions that accept iterables
total = sum(x**2 for x in range(100))
any(x > 90 for x in scores)
all(len(p) >= 8 for p in passwords)

# Memory comparison
import sys
list_mem = sys.getsizeof([x**2 for x in range(1000)])  # ~8072 bytes
gen_mem  = sys.getsizeof((x**2 for x in range(1000)))  # ~104 bytes
```

## Performance and Readability

```python
# Comprehension vs loop — usually 20-50% faster
import timeit

loop_time = timeit.timeit(
    "result = []\nfor x in range(100):\n    result.append(x**2)",
    number=10000
)
comp_time = timeit.timeit(
    "[x**2 for x in range(100)]",
    number=10000
)
```

## When NOT to Use Comprehensions

```python
# Avoid deeply nested or complex conditions — use a loop
# Bad:
result = [transform(x) for x in data if condition1(x)
          if condition2(x) if not condition3(x)]

# Good:
result = []
for x in data:
    if condition1(x) and condition2(x) and not condition3(x):
        result.append(transform(x))
```

## Lab Exercise
1. Build a word frequency dict from a sentence using dict comprehension
2. Find all Pythagorean triples up to n=20 using nested list comprehension
3. Compare memory usage of a generator vs list for 1M squares

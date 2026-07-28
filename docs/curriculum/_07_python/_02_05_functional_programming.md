---
id: "02_05_02"
title: "Functional Programming in Python"
course: "Python"
module: 5
module_title: "Functions"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["lambda", "map", "filter", "reduce", "sorted", "functools", "partial", "lru-cache", "operator", "pure-function", "immutability"]
prerequisites: []
lab_required: true
---

# Functional Programming in Python


## Lambda Functions

```python
# lambda arguments: expression
double = lambda x: x * 2
add    = lambda x, y: x + y

# Common uses
sorted(items, key=lambda x: x[1])
sorted(students, key=lambda s: (s.grade, s.name))

# Avoid complex lambdas — use def instead
```

## map, filter, reduce

```python
from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map — transform each element
doubles = list(map(lambda x: x*2, nums))        # [2, 4, 6, ...]
squares = list(map(lambda x: x**2, nums))

# filter — keep matching elements
evens   = list(filter(lambda x: x%2==0, nums))  # [2, 4, 6, 8, 10]
positives = list(filter(None, [-1, 0, 1, 2]))   # [1, 2] (filter falsy)

# reduce — aggregate
total   = reduce(lambda a, b: a + b, nums)       # 55
product = reduce(lambda a, b: a * b, nums)       # 3628800

# Prefer comprehensions over map/filter — more Pythonic
doubles  = [x*2 for x in nums]
evens    = [x for x in nums if x % 2 == 0]
```

## functools.partial

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube   = partial(power, exponent=3)

square(5)   # 25
cube(3)     # 27

# Practical: pre-configure print
import sys
eprint = partial(print, file=sys.stderr)
eprint("Error message")
```

## functools.lru_cache (Memoization)

```python
from functools import lru_cache

@lru_cache(maxsize=None)  # unlimited cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(50)   # instant — cached
fibonacci.cache_info()   # CacheInfo(hits=48, misses=51, ...)
fibonacci.cache_clear()  # clear the cache

# cache (3.9+) — simpler unbounded version
from functools import cache

@cache
def factorial(n):
    return n * factorial(n-1) if n else 1
```

## operator module

```python
import operator

# Replace lambdas with operator functions
from operator import itemgetter, attrgetter, methodcaller

# Sort by key (faster than lambda)
sorted(dicts, key=itemgetter("name"))
sorted(objects, key=attrgetter("age"))

# arithmetic operators as functions
operator.add(1, 2)      # 3
operator.mul(3, 4)      # 12
reduce(operator.add, [1,2,3,4,5])   # 15
```

## Immutability and Pure Functions

```python
# Pure function: same input → same output, no side effects
def add(a, b):
    return a + b   # pure

# Impure: depends on external state
total = 0
def add_to_total(n):
    global total
    total += n     # side effect — avoid in FP

# Use immutable data structures for safer code
from typing import FrozenSet
def process(data: tuple) -> tuple:  # tuple in, tuple out
    return tuple(x*2 for x in data)
```

## Lab Exercise
1. Implement `compose(*funcs)` that chains functions: `compose(f, g)(x)` = `f(g(x))`
2. Use `lru_cache` to speed up a recursive tree traversal
3. Rewrite a series of chained `map/filter` operations as comprehensions

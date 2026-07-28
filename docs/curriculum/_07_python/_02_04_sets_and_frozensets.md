---
id: "02_04_04"
title: "Sets and Frozensets"
course: "Python"
module: 4
module_title: "Collections"
lesson: 4
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["set", "frozenset", "union", "intersection", "difference", "symmetric-difference", "add", "discard", "set-comprehension", "hashing"]
prerequisites: []
lab_required: true
---

# Sets and Frozensets


## Sets

Sets are **unordered**, **unique** element collections with **O(1) membership** testing.

```python
# Creation
empty = set()            # NOT {} — that's an empty dict!
nums  = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3, 3])   # {1, 2, 3}
chars = set("hello")                    # {'h', 'e', 'l', 'o'}
```

## Set Operations

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union — all elements from both
a | b           # {1, 2, 3, 4, 5, 6, 7, 8}
a.union(b)

# Intersection — elements in both
a & b           # {4, 5}
a.intersection(b)

# Difference — in a but not b
a - b           # {1, 2, 3}
a.difference(b)

# Symmetric difference — in one but not both
a ^ b           # {1, 2, 3, 6, 7, 8}
a.symmetric_difference(b)

# Subset / superset
{1, 2} <= {1, 2, 3}     # True — is subset
{1, 2, 3} >= {1, 2}     # True — is superset
{1, 2}.isdisjoint({3,4}) # True — no common elements
```

## Modifying Sets

```python
s = {1, 2, 3}
s.add(4)              # {1, 2, 3, 4}
s.update([5, 6])      # add multiple
s.remove(1)           # KeyError if missing
s.discard(99)         # silent if missing (preferred)
s.pop()               # remove arbitrary element
s.clear()             # empty set
```

## Set Comprehensions

```python
squares = {x**2 for x in range(10)}
unique_lengths = {len(word) for word in words}
filtered = {x for x in data if x > 0}
```

## Frozenset (Immutable Set)

```python
fs = frozenset([1, 2, 3])
# Can be used as dict key or in another set
lookup = {frozenset([1,2]): "pair", frozenset([3,4]): "other_pair"}

# Set of frozensets
teams = {frozenset(["Alice","Bob"]), frozenset(["Charlie","Dave"])}
```

## Practical Use Cases

```python
# Deduplication (order-preserving with dict trick)
deduped = list(dict.fromkeys(items))

# Fast membership testing
VALID_EXTENSIONS = {'.py', '.js', '.ts', '.go', '.rs'}
if path.suffix in VALID_EXTENSIONS:
    process(path)

# Finding common/unique elements between lists
set1 = set(list1)
set2 = set(list2)
common  = set1 & set2
only_in_1 = set1 - set2
```

## Lab Exercise
1. Find duplicate elements in a list using sets
2. Compare two text files to find common and unique words
3. Implement a "seen" set to filter duplicates while streaming data

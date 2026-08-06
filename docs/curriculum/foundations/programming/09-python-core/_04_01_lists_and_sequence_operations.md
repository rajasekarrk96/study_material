# Lists and Sequence Operations

> **Course**: Core Python | **Module**: Collections | **Difficulty**: beginner

---

```python
# Creation
empty = []
nums = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, None, [1, 2]]
from_range = list(range(1, 11))

# Indexing and slicing
nums[0]        # 1  (first)
nums[-1]       # 5  (last)
nums[1:4]      # [2, 3, 4]
nums[::2]      # [1, 3, 5]  (every other)
nums[::-1]     # [5, 4, 3, 2, 1]  (reversed)
nums[1:4:2]    # [2, 4]  (slice with step)
```

---

```python
lst = [1, 2, 3]

lst.append(4)          # [1, 2, 3, 4] — O(1)
lst.extend([5, 6])     # [1, 2, 3, 4, 5, 6] — O(k)
lst.insert(1, 99)      # [1, 99, 2, ...] — O(n)

lst.remove(99)         # removes first occurrence — O(n)
val = lst.pop()        # removes and returns last — O(1)
val = lst.pop(0)       # removes and returns index 0 — O(n)

lst.clear()            # []
lst.index(3)           # first index of 3 — O(n)
lst.count(3)           # occurrences of 3 — O(n)
```

---

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]

nums.sort()                    # in-place, ascending
nums.sort(reverse=True)        # in-place, descending
sorted(nums)                   # new list, original unchanged

# Key function
words = ["banana", "apple", "cherry", "date"]
words.sort(key=len)            # sort by length
words.sort(key=str.lower)      # case-insensitive

# Sort complex objects
people = [{"name": "Bob", "age": 30}, {"name": "Alice", "age": 25}]
people.sort(key=lambda p: p["age"])
```

---

```python
# [expression for item in iterable if condition]
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
upper   = [s.upper() for s in words if len(s) > 3]

# Nested comprehension (matrix transpose)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
transposed = [[row[i] for row in matrix] for i in range(3)]

# Flatten nested list
flat = [x for row in matrix for x in row]
```

---

```python
original = [1, [2, 3], 4]

# Shallow copy (nested objects still shared)
shallow = original.copy()
shallow = original[:]
shallow = list(original)

# Deep copy (fully independent)
import copy
deep = copy.deepcopy(original)
```

---

1. Sort a list of tuples by the second element
2. Write a one-liner that flattens `[[1,[2,3]],4]` to `[1,2,3,4]`
3. Benchmark `list.append()` in a loop vs `list comprehension` using `timeit`

---

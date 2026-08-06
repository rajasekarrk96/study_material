---
id: "02_03_03"
title: "Iteration and Loop Structures"
course: "Python"
module: 3
module_title: "Control Flow"
lesson: 3
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["for", "while", "break", "continue", "else", "range", "enumerate", "zip", "iter", "next", "loop-patterns"]
prerequisites: []
lab_required: true
---

# Iteration and Loop Structures


## for Loops

```python
# Iterating sequences
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

# range()
for i in range(5):          # 0, 1, 2, 3, 4
for i in range(2, 10, 2):  # 2, 4, 6, 8
for i in range(10, 0, -1): # 10, 9, ..., 1

# enumerate — index + value
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# zip — parallel iteration
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# zip with strict (3.10+) — raises if unequal length
for a, b in zip(list1, list2, strict=True):
    ...
```

## while Loops

```python
# Classic while
count = 0
while count < 5:
    print(count)
    count += 1

# Do-while equivalent
while True:
    data = input("Enter (q to quit): ")
    if data == "q":
        break
    process(data)

# Sentinel pattern
total = 0
while (n := int(input("Number (-1 to stop): "))) != -1:
    total += n
```

## break, continue, else

```python
# break — exit loop immediately
for i in range(10):
    if i == 5:
        break   # stops at 5
    print(i)

# continue — skip to next iteration
for i in range(10):
    if i % 2 == 0:
        continue  # skip even
    print(i)

# else — runs only if loop completed without break
for item in items:
    if item.is_valid():
        break
else:
    print("No valid item found")  # runs if no break
```

## Advanced Iteration Patterns

```python
from itertools import product, combinations, permutations, chain

# Cartesian product
for x, y in product([1,2], ['a','b']):
    print(x, y)   # (1,a), (1,b), (2,a), (2,b)

# Combinations (no repetition)
for combo in combinations([1,2,3], 2):
    print(combo)  # (1,2), (1,3), (2,3)

# Flatten nested lists
nested = [[1,2],[3,4],[5,6]]
flat = list(chain.from_iterable(nested))  # [1,2,3,4,5,6]

# Manual iteration with iter/next
it = iter([1, 2, 3])
next(it)         # 1
next(it)         # 2
next(it, "done") # 3
next(it, "done") # "done" (default, no StopIteration)
```

## Lab Exercise
1. Find all prime numbers to 100 using nested loops + break
2. Flatten a 2D matrix using nested for loops and via `chain`
3. Implement a menu-driven CLI with `while True` + `match/case`

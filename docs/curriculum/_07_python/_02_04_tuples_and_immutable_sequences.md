---
id: "02_04_02"
title: "Tuples and Immutable Sequences"
course: "Python"
module: 4
module_title: "Collections"
lesson: 2
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["tuple", "namedtuple", "immutability", "packing", "unpacking", "single-element", "tuple-methods", "dataclass"]
prerequisites: []
lab_required: true
---

# Tuples and Immutable Sequences


## Tuples

Tuples are **immutable ordered sequences** — ideal for fixed data, function returns, dictionary keys.

```python
# Creation
empty  = ()
single = (42,)       # comma required! (42) is just parens
point  = (3, 4)
mixed  = (1, "two", 3.0)

# Packing (parens optional)
coords = 10, 20, 30

# Unpacking
x, y, z = coords
first, *rest = (1, 2, 3, 4, 5)   # first=1, rest=[2,3,4,5]
a, b = b, a                        # swap without temp variable

# Nested unpacking
(name, (x, y)) = ("point", (3, 4))
```

## Why Tuples?

```python
# 1. As dictionary keys (lists can't be)
grid = {(0,0): "A", (0,1): "B", (1,0): "C"}
grid[(0,1)]   # "B"

# 2. Multiple return values
def min_max(lst):
    return min(lst), max(lst)

lo, hi = min_max([3, 1, 4, 1, 5, 9])

# 3. Faster than lists
import timeit
timeit.timeit(lambda: (1,2,3,4,5))   # ~2x faster than list
```

## Named Tuples

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
p.x      # 3
p.y      # 4
p[0]     # 3 — still indexable
p._asdict()   # OrderedDict([('x', 3), ('y', 4)])

# With defaults
Config = namedtuple('Config', ['host', 'port', 'debug'], defaults=['localhost', 8000, False])
c = Config()          # Config(host='localhost', port=8000, debug=False)
c = Config('prod.server', 443)
```

## typing.NamedTuple (Modern)

```python
from typing import NamedTuple

class Employee(NamedTuple):
    name: str
    department: str
    salary: float = 50000.0

emp = Employee("Raja", "Engineering", 75000)
emp.name      # "Raja"
```

## Tuple vs List Decision

| Use | Tuple | List |
|---|---|---|
| Data will change | No | Yes |
| Dict key needed | Yes | No |
| Heterogeneous data | Yes | Usually no |
| Semantic record | Yes | Usually no |
| Large homogeneous data | No | Yes |

## Lab Exercise
1. Implement coordinate storage using namedtuples with distance method
2. Swap two variables using tuple packing/unpacking without a temp var
3. Profile memory usage of `(1,2,3)` vs `[1,2,3]` using `sys.getsizeof()`

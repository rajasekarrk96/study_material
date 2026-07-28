---
id: "02_07_03"
title: "Magic Dunder Methods"
course: "Python"
module: 7
module_title: "Object-Oriented Programming"
lesson: 3
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["__init__", "__repr__", "__str__", "__len__", "__getitem__", "__setitem__", "__contains__", "__eq__", "__hash__", "__call__", "__enter__", "__exit__", "__iter__"]
prerequisites: []
lab_required: true
---

# Magic Dunder Methods


## Essential Dunder Methods

```python
class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Representation
    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    # Arithmetic
    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> "Vector":
        return self.__mul__(scalar)   # 3 * v == v * 3

    def __neg__(self) -> "Vector":
        return Vector(-self.x, -self.y)

    def __abs__(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    # Comparison
    def __eq__(self, other) -> bool:
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))   # needed if __eq__ defined

    # Boolean
    def __bool__(self) -> bool:
        return self.x != 0 or self.y != 0

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v1 + v2     # Vector(4, 6)
3 * v1      # Vector(3, 6)
abs(v2)     # 5.0
{v1, v2}    # works because __hash__ defined
```

## Container Protocol

```python
class NumberList:
    def __init__(self, *numbers):
        self._data = list(numbers)

    def __len__(self):          return len(self._data)
    def __getitem__(self, idx): return self._data[idx]
    def __setitem__(self, idx, val): self._data[idx] = val
    def __delitem__(self, idx): del self._data[idx]
    def __contains__(self, item): return item in self._data
    def __iter__(self):         return iter(self._data)
    def __reversed__(self):     return reversed(self._data)

nl = NumberList(1, 2, 3, 4, 5)
len(nl)      # 5
nl[0]        # 1
3 in nl      # True
for n in nl: ...
```

## Context Manager Protocol

```python
class DatabaseConnection:
    def __init__(self, url: str):
        self.url = url
        self.conn = None

    def __enter__(self):
        self.conn = connect(self.url)
        return self.conn   # value assigned to `as` variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()
        return False   # don't suppress exceptions

with DatabaseConnection("sqlite:///mydb") as conn:
    conn.execute("INSERT INTO ...")
```

## Callable Objects `__call__`

```python
class Validator:
    def __init__(self, pattern: str):
        import re
        self.regex = re.compile(pattern)

    def __call__(self, value: str) -> bool:
        return bool(self.regex.match(value))

is_email = Validator(r"[^@]+@[^@]+\.[^@]+")
is_email("user@example.com")   # True
is_email("not-an-email")       # False
```

## Lab Exercise
1. Build a `Matrix` class supporting `+`, `*`, `@` (matmul), indexing
2. Create a `Roster` class with full container protocol (add/remove students)
3. Implement a reusable `Timer` context manager using `__enter__`/`__exit__`

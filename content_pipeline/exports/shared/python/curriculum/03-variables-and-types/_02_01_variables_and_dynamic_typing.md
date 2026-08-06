# Variables and Dynamic Typing

> **Course**: Core Python | **Module**: Variables and Types | **Difficulty**: beginner

---

Python variables are **names bound to objects**, not typed containers.

```python
x = 42          # x points to int object 42
x = "hello"     # x now points to str object (no error!)
x = [1, 2, 3]   # now a list

# Multiple assignment
a = b = c = 0
x, y, z = 1, 2, 3       # tuple unpacking
first, *rest = [1,2,3,4] # starred unpacking: first=1, rest=[2,3,4]

# Augmented assignment
count = 0
count += 1   # count = count + 1
count -= 1
count *= 2
count **= 3
```

---

```python
# Dynamic — type checked at runtime
def greet(name):
    return "Hello " + name   # works if name is str

greet("Raja")    # OK
greet(42)        # RuntimeError: can't concatenate str and int
```

---

```python
def add(a: int, b: int) -> int:
    return a + b

name: str = "Raja"
scores: list[int] = [90, 85, 92]
mapping: dict[str, int] = {"a": 1}
```
> Annotations are **not enforced** at runtime — use `mypy` for checking.

---

```python
# "If it walks like a duck and quacks like a duck, it's a duck"
def process(obj):
    obj.save()   # works for any object with .save() — no inheritance needed

class FileWriter:
    def save(self): ...

class DBWriter:
    def save(self): ...

process(FileWriter())  # OK
process(DBWriter())    # OK
```

---

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a == b    # True  — same value
a is b    # False — different objects
a is c    # True  — same object

# Use `is` only for None, True, False
if value is None: ...
if value is not None: ...
```

---

1. Demonstrate that `x = 5; y = x; y = 10` does NOT change `x`
2. Use `id()` to show two equal lists are different objects
3. Use starred unpacking to split a list into head and tail

---

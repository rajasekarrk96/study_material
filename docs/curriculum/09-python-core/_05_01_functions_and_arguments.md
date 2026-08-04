# Functions and Arguments

> **Course**: Core Python | **Module**: Functions | **Difficulty**: beginner

---

```python
def greet(name: str, greeting: str = "Hello") -> str:
    """Return a greeting string."""
    return f"{greeting}, {name}!"

greet("Raja")             # "Hello, Raja!"
greet("Raja", "Namaste")  # "Namaste, Raja!"
greet(greeting="Hi", name="Bob")  # keyword args — any order
```

---

```python
def func(pos_only, /, normal, *, kw_only):
    pass
    # pos_only — must be positional (before /)
    # normal   — can be positional or keyword
    # kw_only  — must be keyword (after *)

func(1, 2, kw_only=3)
func(1, normal=2, kw_only=3)
```

---

```python
def variadic(*args, **kwargs):
    print(args)    # tuple of positional extras
    print(kwargs)  # dict of keyword extras

variadic(1, 2, 3, name="Raja", age=28)
# (1, 2, 3)
# {'name': 'Raja', 'age': 28}

# Unpacking into function calls
nums = [1, 2, 3]
params = {"sep": ", ", "end": "!\n"}
print(*nums, **params)   # 1, 2, 3!
```

---

```python
# WRONG — mutable default is shared across calls
def append_to(element, lst=[]):
    lst.append(element)
    return lst

append_to(1)   # [1]
append_to(2)   # [1, 2] — NOT [2]!

# CORRECT — use None sentinel
def append_to(element, lst=None):
    if lst is None:
        lst = []
    lst.append(element)
    return lst
```

---

```python
def divide(a, b):
    if b == 0:
        return None, "Division by zero"
    return a / b, None

result, error = divide(10, 2)    # (5.0, None)
result, error = divide(10, 0)    # (None, "Division by zero")

# Functions without return → return None implicitly
```

---

```python
# Functions as arguments
def apply(func, value):
    return func(value)

apply(str.upper, "hello")   # "HELLO"
apply(abs, -5)              # 5

# Functions as return values
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
double(5)    # 10
triple = multiplier(3)
triple(5)    # 15
```

---

1. Write a function `stats(*numbers)` returning min, max, mean, median
2. Build a `retry(func, times=3)` decorator without using `@`
3. Implement `partial()` manually that pre-fills arguments

---

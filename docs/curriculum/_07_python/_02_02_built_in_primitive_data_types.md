---
id: "02_02_02"
title: "Built-in Primitive Data Types"
course: "Python"
module: 2
module_title: "Variables and Types"
lesson: 2
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["int", "float", "complex", "bool", "str", "bytes", "bytearray", "NoneType", "type-conversion", "isinstance"]
prerequisites: []
lab_required: true
---

# Built-in Primitive Data Types


## Numeric Types

```python
# Integer — arbitrary precision
x = 1_000_000          # underscore separator for readability
big = 2**100           # no overflow in Python!
hex_val = 0xFF         # 255
bin_val = 0b1010       # 10
oct_val = 0o17         # 15

# Float — IEEE 754 double precision
pi = 3.14159
sci = 1.5e-3           # 0.0015
from decimal import Decimal
d = Decimal("0.1") + Decimal("0.2")  # Exact: 0.3

# Complex
z = 3 + 4j
z.real  # 3.0
z.imag  # 4.0
abs(z)  # 5.0

# Boolean (subclass of int)
True + True   # 2
int(False)    # 0
bool(0)       # False
bool("")      # False
bool([])      # False
bool(None)    # False
```

## Strings

```python
s = 'single' or "double" or '''triple'''
raw = r"C:\Users\no\escape"      # raw string
byte = b"bytes literal"

# F-strings (3.6+)
name, score = "Raja", 95.5
f"Hello {name}, score: {score:.2f}"  # Hello Raja, score: 95.50
f"{2**10 = }"                         # "2**10 = 1024"  (3.8+ debug)

# Common methods
"  hello  ".strip()          # "hello"
"Hello World".lower()        # "hello world"
"hello".upper()              # "HELLO"
"a,b,c".split(",")           # ['a', 'b', 'c']
", ".join(["a","b","c"])     # "a, b, c"
"hello world".replace("world","Python")
"hello".startswith("hel")   # True
"hello".find("ll")           # 2
```

## NoneType

```python
result = None
type(result)          # <class 'NoneType'>
result is None        # True  (preferred check)
result == None        # True  (but use `is`)

# Functions return None implicitly
def no_return(): pass
print(no_return())   # None
```

## Type Conversion

```python
int("42")          # 42
int(3.9)           # 3  (truncates, not rounds)
float("3.14")      # 3.14
str(42)            # "42"
bool(0)            # False
list("abc")        # ['a', 'b', 'c']
tuple([1,2,3])     # (1, 2, 3)
```

## isinstance and type

```python
isinstance(42, int)          # True
isinstance(42, (int, float)) # True — check multiple types
type(42) is int              # True
type(42) == int              # True
# Prefer isinstance — handles inheritance
```

## Lab Exercise
1. Show integer overflow doesn't exist: compute `10**309`
2. Prove float imprecision: `0.1 + 0.2 == 0.3` and fix with `Decimal`
3. Benchmark f-string vs `%` formatting vs `.format()` using `timeit`

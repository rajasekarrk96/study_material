---
id: "02_02_03"
title: "Syntax Rules and Code Style"
course: "Python"
module: 2
module_title: "Variables and Types"
lesson: 3
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["indentation", "pep8", "comments", "docstrings", "naming-conventions", "semicolons", "line-continuation", "blank-lines"]
prerequisites: []
lab_required: true
---

# Syntax Rules and Code Style


## Python Syntax Fundamentals

### Indentation (Significant Whitespace)
```python
# Use 4 spaces (never tabs)
if True:
    print("indented block")
    if True:
        print("nested block")

# Bad — inconsistent indentation raises IndentationError
if True:
  print("2 spaces")  # will error if mixed with 4-space blocks
```

### Statements and Line Continuation
```python
# One statement per line (preferred)
x = 1
y = 2

# Multiple on one line (rarely used)
x = 1; y = 2

# Long lines — implicit continuation inside brackets
result = (value_one +
          value_two +
          value_three)

# Explicit continuation with backslash (avoid if possible)
total = first_number + \
        second_number
```

### Comments
```python
# Single-line comment
x = 5  # inline comment (2 spaces before #)

# Multi-line — use multiple # lines
# This is line 1
# This is line 2

# NOT: use triple-quotes for comments (they create string objects)
```

### Docstrings
```python
def calculate_bmi(weight: float, height: float) -> float:
    '''
    Calculate Body Mass Index.

    Args:
        weight: Weight in kilograms.
        height: Height in metres.

    Returns:
        BMI value as float.

    Raises:
        ValueError: If height is zero.

    Example:
        >>> calculate_bmi(70, 1.75)
        22.857142857142858
    '''
    if height == 0:
        raise ValueError("Height cannot be zero")
    return weight / (height ** 2)
```

## PEP 8 Style Guide

| Rule | Good | Bad |
|---|---|---|
| Variable names | `user_name` | `userName`, `Username` |
| Constants | `MAX_SIZE = 100` | `maxSize = 100` |
| Classes | `class UserAccount:` | `class user_account:` |
| Functions | `def get_user():` | `def GetUser():` |
| Private | `_internal`, `__dunder__` | |
| Max line length | 88–100 chars | 120+ |
| Imports | One per line, top of file | `import os, sys` |
| Spaces | `x = 1 + 2` | `x=1+2` |

## Naming Conventions Summary

```python
# snake_case for variables, functions, modules
user_name = "Raja"
def calculate_total(): ...
import my_module

# PascalCase for classes
class HttpRequest: ...
class UserProfile: ...

# UPPER_SNAKE_CASE for constants
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

# _single_leading for "private" (convention only)
_cache = {}

# __double_leading for name mangling in classes
class Foo:
    __private = "truly private"
```

## Lab Exercise
1. Run `ruff check` on a file with PEP 8 violations and fix them
2. Write a fully docstring-documented function with type hints
3. Configure VS Code to auto-format on save using `black` or `ruff`

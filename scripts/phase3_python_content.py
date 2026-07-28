"""
phase3_python_content.py
Fills all 39 Python stubs with full educational content.
"""
import os

BASE = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum'
PY = os.path.join(BASE, "_07_python")

written = 0

def write(fname, content):
    global written
    path = os.path.join(PY, fname)
    if os.path.exists(path):
        txt = open(path, encoding='utf-8', errors='ignore').read()
        if 'Status**: Stub' not in txt and 'Topics Covered' not in txt:
            print(f"  [SKIP-REAL] {fname}")
            return
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  [WRITE] {fname}")
    written += 1

def fm(lid, title, mod, mod_title, les, diff, tags):
    tag_str = ', '.join(f'"{t}"' for t in tags)
    return f'''---
id: "{lid}"
title: "{title}"
course: "Python"
module: {mod}
module_title: "{mod_title}"
lesson: {les}
version: "2.0"
difficulty: "{diff}"
duration_minutes: 60
tags: [{tag_str}]
prerequisites: []
lab_required: true
---

# {title}

'''

# ══════════════════════════════════════════════════════════════════
# MODULE 1: Setup & Overview
# ══════════════════════════════════════════════════════════════════

write("_02_01_python_overview_and_philosophy.md", fm(
    "02_01_01","Python Overview and Philosophy",1,"Setup and Overview",1,"beginner",
    ["python","guido","zen","pep8","cpython","interpreted","dynamic-typing","whitespace"]
) + """
## What is Python?

Python is a **high-level, interpreted, dynamically typed** programming language created by Guido van Rossum (1991). It emphasises **readability** and expressiveness over verbosity.

> "There should be one — and preferably only one — obvious way to do it." — The Zen of Python

## Python's Design Philosophy

```python
import this  # Prints The Zen of Python
```

Key principles:
- **Beautiful is better than ugly** — code should be readable
- **Explicit is better than implicit** — no magic unless necessary
- **Simple is better than complex** — prefer straightforward solutions
- **Readability counts** — code is read more often than written

## Python Versions

| Version | Key Features | Status |
|---|---|---|
| Python 2.x | Old syntax, `print` statement | EOL 2020 |
| Python 3.6 | f-strings, secrets module | EOL |
| Python 3.10 | Match/case (structural pattern matching) | EOL |
| Python 3.11 | 60% faster, better error messages | Supported |
| Python 3.12 | Type aliases, f-string improvements | Active LTS |
| Python 3.13 | Free-threaded mode (no GIL) | Latest |

## Where Python is Used

| Domain | Tools |
|---|---|
| Web Development | Flask, FastAPI, Django |
| Data Science | NumPy, Pandas, Matplotlib |
| Machine Learning | scikit-learn, TensorFlow, PyTorch |
| Automation / Scripting | subprocess, pathlib, os |
| Embedded / IoT | MicroPython, CircuitPython |
| DevOps | Ansible, Fabric, boto3 |

## Python Interpreter Types

| Interpreter | Language | Use Case |
|---|---|---|
| **CPython** | C | Default, most compatible |
| PyPy | Python + JIT | Speed-critical scripts |
| MicroPython | C | Microcontrollers |
| Jython | Java | JVM integration |
| GraalPy | GraalVM | Polyglot projects |

## Lab Exercise
1. Run `python --version` and `python -c "import this"`
2. Open the REPL and evaluate: `2**32`, `"hello"*3`, `type(3.14)`
3. Write a one-liner that prints the first 10 Fibonacci numbers
""")

write("_02_01_environment_setup_and_tooling.md", fm(
    "02_01_02","Environment Setup and Tooling",1,"Setup and Overview",2,"beginner",
    ["installation","venv","virtualenv","pip","pyproject.toml","uv","conda","VS-Code","pycharm","REPL"]
) + """
## Installing Python

```bash
# Windows — via official installer or winget
winget install Python.Python.3.12

# macOS
brew install python@3.12

# Ubuntu/Debian
sudo apt install python3.12 python3.12-venv python3.12-dev
```

## Virtual Environments

Always isolate project dependencies in a virtual environment.

```bash
# Create
python -m venv .venv

# Activate
source .venv/bin/activate        # Linux/macOS
.venv\\Scripts\\activate          # Windows PowerShell

# Deactivate
deactivate
```

## Package Management with pip

```bash
pip install requests flask       # install packages
pip install -r requirements.txt  # install from file
pip freeze > requirements.txt    # export current env
pip list --outdated              # check updates
pip uninstall requests           # remove package
pip show flask                   # package details
```

## Modern Tooling — uv (recommended 2024+)

```bash
# Install uv
pip install uv

# Create project
uv init myproject
cd myproject

# Add dependencies
uv add fastapi sqlalchemy

# Run script
uv run main.py

# Sync environment from pyproject.toml
uv sync
```

## pyproject.toml

```toml
[project]
name = "myapp"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["fastapi>=0.110", "sqlalchemy>=2.0"]

[project.optional-dependencies]
dev = ["pytest", "ruff", "mypy"]
```

## Code Quality Tools

| Tool | Purpose | Command |
|---|---|---|
| **ruff** | Linter + formatter (fast) | `ruff check .` / `ruff format .` |
| **black** | Formatter | `black .` |
| **mypy** | Type checker | `mypy src/` |
| **pytest** | Testing | `pytest tests/` |
| **pre-commit** | Git hooks | `pre-commit run --all-files` |

## REPL and Interactive Tools

```bash
python          # Standard REPL
ipython         # Enhanced REPL with magic commands
jupyter lab     # Browser-based notebooks
ptpython        # Pretty REPL with syntax highlighting
```

## Lab Exercise
1. Create a new project folder, set up `.venv`, activate it
2. Install `requests` and `rich`; freeze to `requirements.txt`
3. Configure VS Code with the Python extension and select the venv interpreter
""")

write("_02_01_cpython_architecture_and_execution.md", fm(
    "02_01_03","CPython Architecture and Execution Model",1,"Setup and Overview",3,"intermediate",
    ["CPython","bytecode","pyc","AST","tokenizer","GIL","memory-management","reference-counting","gc","dis"]
) + """
## How Python Code Executes

```
Source (.py)
    ↓ Tokenizer
Token Stream
    ↓ Parser
AST (Abstract Syntax Tree)
    ↓ Compiler
Bytecode (.pyc)
    ↓ CPython VM (eval loop)
Result
```

## Inspecting Bytecode

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
# LOAD_FAST    0 (a)
# LOAD_FAST    1 (b)
# BINARY_OP    0 (+)
# RETURN_VALUE
```

## The GIL (Global Interpreter Lock)

The GIL is a mutex that **allows only one thread to execute Python bytecode at a time**.

**Implications**:
- CPU-bound threads don't run truly in parallel
- I/O-bound threads work fine (GIL released during I/O)
- Use `multiprocessing` for CPU parallelism
- Python 3.13 introduces **free-threaded mode** (experimental, `--disable-gil`)

```python
# CPU-bound: use multiprocessing
from multiprocessing import Pool
with Pool(4) as p:
    results = p.map(heavy_compute, data_chunks)

# I/O-bound: threading or asyncio work fine
import asyncio
```

## Memory Management

### Reference Counting
```python
import sys
x = [1, 2, 3]
print(sys.getrefcount(x))   # 2 (x + getrefcount arg)
y = x                        # ref count goes to 3
del y                        # ref count back to 2
```

### Garbage Collector (for cycles)
```python
import gc
gc.collect()                 # force collection
gc.get_stats()               # collection statistics
```

### Object Interning
```python
a = "hello"
b = "hello"
print(a is b)    # True — interned (small strings/ints)

a = [1, 2]
b = [1, 2]
print(a is b)    # False — different objects
print(a == b)    # True — same value
```

## `__pycache__` and .pyc Files

Python caches compiled bytecode in `__pycache__/`:
```
mymodule.cpython-312.pyc
```
- Recompiled only when source changes (mtime check)
- Safe to delete — regenerated automatically

## Lab Exercise
1. Use `dis.dis()` to inspect a list comprehension vs. a `for` loop
2. Measure reference count changes with `sys.getrefcount()`
3. Create a circular reference and verify `gc.collect()` cleans it up
""")

# ══════════════════════════════════════════════════════════════════
# MODULE 2: Variables & Types
# ══════════════════════════════════════════════════════════════════

write("_02_02_variables_and_dynamic_typing.md", fm(
    "02_02_01","Variables and Dynamic Typing",2,"Variables and Types",1,"beginner",
    ["variable","assignment","dynamic-typing","duck-typing","type","id","is","del","multiple-assignment","augmented-assignment"]
) + """
## Variables in Python

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

## Dynamic vs Static Typing

```python
# Dynamic — type checked at runtime
def greet(name):
    return "Hello " + name   # works if name is str

greet("Raja")    # OK
greet(42)        # RuntimeError: can't concatenate str and int
```

## Type Annotations (Optional Static Hints)

```python
def add(a: int, b: int) -> int:
    return a + b

name: str = "Raja"
scores: list[int] = [90, 85, 92]
mapping: dict[str, int] = {"a": 1}
```
> Annotations are **not enforced** at runtime — use `mypy` for checking.

## Duck Typing

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

## Identity vs Equality

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

## Lab Exercise
1. Demonstrate that `x = 5; y = x; y = 10` does NOT change `x`
2. Use `id()` to show two equal lists are different objects
3. Use starred unpacking to split a list into head and tail
""")

write("_02_02_built_in_primitive_data_types.md", fm(
    "02_02_02","Built-in Primitive Data Types",2,"Variables and Types",2,"beginner",
    ["int","float","complex","bool","str","bytes","bytearray","NoneType","type-conversion","isinstance"]
) + """
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
raw = r"C:\\Users\\no\\escape"      # raw string
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
""")

write("_02_02_syntax_rules_and_style.md", fm(
    "02_02_03","Syntax Rules and Code Style",2,"Variables and Types",3,"beginner",
    ["indentation","pep8","comments","docstrings","naming-conventions","semicolons","line-continuation","blank-lines"]
) + """
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
total = first_number + \\
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
""")

# ══════════════════════════════════════════════════════════════════
# MODULE 3: Control Flow
# ══════════════════════════════════════════════════════════════════

write("_02_03_comprehensive_operator_systems.md", fm(
    "02_03_01","Comprehensive Operator Systems",3,"Control Flow",1,"beginner",
    ["arithmetic","comparison","logical","bitwise","assignment","identity","membership","operator-precedence","walrus"]
) + """
## Python Operators Reference

### Arithmetic Operators
```python
17 // 3    # 5  — floor division
17 %  3    # 2  — modulo (remainder)
2  ** 8    # 256 — exponentiation
-7 // 2    # -4  — floor towards negative infinity
-7 %  2    #  1  — always same sign as divisor
divmod(17, 3)   # (5, 2) — quotient and remainder
```

### Comparison Operators
```python
x = 5
1 < x < 10    # True  — Python allows chained comparisons
1 < x and x < 10  # equivalent (but more verbose)
x != 3        # True
x == 5.0      # True  — int and float compared by value
```

### Logical Operators (Short-Circuit)
```python
True  and False   # False
True  or  False   # True
not   True        # False

# Short-circuit — returns actual value, not bool
0 or "default"    # "default"
"value" or "other" # "value"
None and expensive()  # None (expensive() never called)
[] or {}              # {} (first falsy, returns last)

# Practical: default values
name = user_input or "Anonymous"
config = provided_config or load_defaults()
```

### Bitwise Operators
```python
0b1010 & 0b1100   # 0b1000 = 8  — AND
0b1010 | 0b1100   # 0b1110 = 14 — OR
0b1010 ^ 0b1100   # 0b0110 = 6  — XOR
~0b1010           # -11          — NOT (bitwise complement)
1 << 4            # 16           — left shift (multiply by 2^4)
256 >> 3          # 32           — right shift (divide by 2^3)
```

### Identity and Membership
```python
x is None         # identity check
x is not None
"key" in {"key": 1}   # True — dict membership checks keys
3 in [1, 2, 3]         # True
3 not in [1, 2]        # True
```

### Walrus Operator `:=` (Python 3.8+)
```python
# Assign and use in same expression
if (n := len(data)) > 10:
    print(f"Too long: {n}")

# In while loops
while chunk := file.read(8192):
    process(chunk)

# In comprehensions
results = [y for x in data if (y := process(x)) is not None]
```

### Operator Precedence (high → low)
```
()                 — parentheses
**                 — exponentiation
+x, -x, ~x        — unary
*, /, //, %        — multiplicative
+, -               — additive
<<, >>             — bit shift
&                  — bitwise AND
^                  — bitwise XOR
|                  — bitwise OR
==, !=, <, >, is, in  — comparisons
not                — logical NOT
and                — logical AND
or                 — logical OR
:=                 — walrus
```

## Lab Exercise
1. Explain why `-7 % 3 == 2` in Python (not -1 like C)
2. Use short-circuit evaluation to guard an expensive function call
3. Implement a simple bitmask-based permission system using `&` and `|`
""")

write("_02_03_conditional_execution.md", fm(
    "02_03_02","Conditional Execution",3,"Control Flow",2,"beginner",
    ["if","elif","else","ternary","match-case","structural-pattern-matching","guard","truthy","falsy"]
) + """
## if / elif / else

```python
score = 75

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")
```

## Ternary (Conditional Expression)

```python
# value_if_true if condition else value_if_false
status = "pass" if score >= 60 else "fail"
max_val = a if a > b else b

# Nested ternary (avoid — unreadable)
grade = "A" if s >= 90 else "B" if s >= 75 else "C"
```

## Truthy and Falsy Values

```python
# Falsy:
False, None, 0, 0.0, 0j, "", b"", [], (), {}, set()

# Truthy:
True, any non-zero number, any non-empty collection, any object

# Common patterns
if user:          # user is not None and not empty
if not errors:    # errors list is empty
if results:       # at least one result
```

## Structural Pattern Matching — match/case (3.10+)

```python
command = "quit"

match command:
    case "quit" | "exit":
        print("Goodbye")
    case "help":
        print("Help text")
    case _:
        print("Unknown command")
```

### Matching Sequences and Structures
```python
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"On X-axis at {x}")
    case (0, y):
        print(f"On Y-axis at {y}")
    case (x, y):
        print(f"Point at ({x}, {y})")
```

### Matching Data Classes
```python
from dataclasses import dataclass

@dataclass
class Response:
    status: int
    body: str

match response:
    case Response(status=200, body=body):
        handle_success(body)
    case Response(status=404):
        handle_not_found()
    case Response(status=s) if s >= 500:
        handle_server_error(s)
```

## Lab Exercise
1. Write a grade calculator using if/elif/else
2. Rewrite a complex if/elif chain using match/case
3. Use pattern matching to parse a command like `["move", 10, 20]`
""")

write("_02_03_iteration_and_loop_structures.md", fm(
    "02_03_03","Iteration and Loop Structures",3,"Control Flow",3,"beginner",
    ["for","while","break","continue","else","range","enumerate","zip","iter","next","loop-patterns"]
) + """
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
""")

# ══════════════════════════════════════════════════════════════════
# MODULE 4: Collections
# ══════════════════════════════════════════════════════════════════

write("_02_04_lists_and_sequence_operations.md", fm(
    "02_04_01","Lists and Sequence Operations",4,"Collections",1,"beginner",
    ["list","append","extend","insert","remove","pop","sort","sorted","reverse","slice","copy","list-comprehension"]
) + """
## Lists

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

## Modifying Lists

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

## Sorting

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

## List Comprehensions

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

## Copying Lists

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

## Lab Exercise
1. Sort a list of tuples by the second element
2. Write a one-liner that flattens `[[1,[2,3]],4]` to `[1,2,3,4]`
3. Benchmark `list.append()` in a loop vs `list comprehension` using `timeit`
""")

write("_02_04_tuples_and_immutable_sequences.md", fm(
    "02_04_02","Tuples and Immutable Sequences",4,"Collections",2,"beginner",
    ["tuple","namedtuple","immutability","packing","unpacking","single-element","tuple-methods","dataclass"]
) + """
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
""")

write("_02_04_dictionaries.md", fm(
    "02_04_03","Dictionaries",4,"Collections",3,"beginner",
    ["dict","keys","values","items","get","setdefault","update","pop","dict-comprehension","defaultdict","OrderedDict","ChainMap"]
) + """
## Dictionaries

Python dicts are **ordered** (3.7+), **mutable**, **O(1) average** key lookup.

```python
# Creation
empty = {}
person = {"name": "Raja", "age": 28, "city": "Chennai"}
from_pairs = dict([("a", 1), ("b", 2)])
from_keys = dict.fromkeys(["a","b","c"], 0)   # {"a":0,"b":0,"c":0}

# Access
person["name"]           # "Raja"
person.get("phone")      # None (no KeyError)
person.get("phone", "N/A")  # "N/A"
```

## CRUD Operations

```python
d = {"a": 1, "b": 2}

# Update / Add
d["c"] = 3
d.update({"d": 4, "e": 5})
d |= {"f": 6}             # merge operator (3.9+)

# Delete
del d["a"]
val = d.pop("b")          # removes and returns
val = d.pop("x", None)    # safe pop with default
d.popitem()               # removes last inserted (LIFO)
d.clear()

# Membership
"key" in d                # True/False — checks keys only
```

## Iterating Dictionaries

```python
for key in d:             # iterates keys
for key in d.keys():      # explicit keys
for val in d.values():    # values
for key, val in d.items():  # key-value pairs

# Get or set default
d.setdefault("count", 0)  # sets "count":0 only if not present
d["count"] = d.get("count", 0) + 1  # increment safely
```

## Dictionary Comprehensions

```python
squares = {x: x**2 for x in range(1, 6)}
# {1:1, 2:4, 3:9, 4:16, 5:25}

inverted = {v: k for k, v in original.items()}

filtered = {k: v for k, v in data.items() if v > 0}
```

## Advanced Dict Types

```python
from collections import defaultdict, OrderedDict, ChainMap

# defaultdict — auto-creates missing keys
word_count = defaultdict(int)
for word in text.split():
    word_count[word] += 1

# Group by category
groups = defaultdict(list)
for item in items:
    groups[item.category].append(item)

# ChainMap — layered lookup (later dicts override earlier)
defaults = {"color": "red", "size": "M"}
user_prefs = {"size": "L"}
config = ChainMap(user_prefs, defaults)
config["color"]  # "red" (from defaults)
config["size"]   # "L"  (from user_prefs)
```

## Merging Dicts (3.9+)

```python
a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}

merged = a | b          # {"x":1, "y":99, "z":3}
a |= b                  # update a in-place
```

## Lab Exercise
1. Build a word frequency counter using `defaultdict(int)`
2. Invert a dictionary (values become keys) using dict comprehension
3. Implement a simple cache (memoization dict) for a recursive function
""")

write("_02_04_sets_and_frozensets.md", fm(
    "02_04_04","Sets and Frozensets",4,"Collections",4,"beginner",
    ["set","frozenset","union","intersection","difference","symmetric-difference","add","discard","set-comprehension","hashing"]
) + """
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
""")

write("_02_04_strings_and_text_processing.md", fm(
    "02_04_05","Strings and Text Processing",4,"Collections",5,"beginner",
    ["str","f-string","format","encode","decode","template","textwrap","string-methods","re","split","join"]
) + """
## String Fundamentals

```python
# Strings are immutable sequences of Unicode code points
s = "Hello, World!"
len(s)           # 13
s[0]             # 'H'
s[-1]            # '!'
s[0:5]           # 'Hello'
"World" in s     # True

# Immutability — every "change" creates a new string
s.upper()        # returns new string "HELLO, WORLD!"
s                # still "Hello, World!"
```

## String Formatting

```python
name, price, qty = "Widget", 9.99, 42

# f-strings (recommended — fast, readable)
f"Product: {name}, Price: ${price:.2f}, Qty: {qty:,}"
f"{name!r}"         # repr: 'Widget'
f"{name!s}"         # str (default)
f"{name!a}"         # ascii: 'Widget'
f"{2**10 = }"       # debug: '2**10 = 1024'
f"{'hello':>10}"    # right-align in 10 chars: '     hello'
f"{3.14159:.2f}"    # '3.14'
f"{1000000:_}"      # '1_000_000'

# .format()
"{name} costs ${price:.2f}".format(name=name, price=price)
"{0} {1} {0}".format("aba", "c")   # "aba c aba"

# % formatting (legacy)
"%s costs $%.2f" % (name, price)
```

## Essential String Methods

```python
s = "  Hello, World!  "

s.strip()           # "Hello, World!"
s.lstrip()          # "Hello, World!  "
s.rstrip()          # "  Hello, World!"

s.lower()           # "  hello, world!  "
s.upper()           # "  HELLO, WORLD!  "
s.title()           # "  Hello, World!  "
s.swapcase()        # "  hELLO, wORLD!  "

s.split(",")        # ['  Hello', ' World!  ']
s.split()           # ['Hello,', 'World!']   (splits on whitespace)
", ".join(["a","b","c"])  # "a, b, c"

s.replace("World", "Python")
s.startswith("  Hello")   # True
s.endswith("!  ")         # True
s.find("World")    # 9  (-1 if not found)
s.count("l")       # 3
s.center(30, "-")  # "------  Hello, World!  ------"
```

## Multi-line and Raw Strings

```python
multi = '''Line 1
Line 2
Line 3'''

path = r"C:/Users/Raja/Documents"   # raw — no escape processing
regex = r"\d{3}-\d{4}"             # common for regex patterns
```

## String Encoding

```python
text = "Hello, 世界"
encoded = text.encode("utf-8")    # bytes
decoded = encoded.decode("utf-8") # str back

# Common encodings: utf-8, utf-16, ascii, latin-1, cp1252
```

## textwrap for Formatting

```python
import textwrap

long_text = "This is a very long string that needs to be wrapped..."
wrapped = textwrap.fill(long_text, width=40)
dedented = textwrap.dedent('''
    Line 1
    Line 2
''')
```

## Lab Exercise
1. Build a template engine that replaces `{{variable}}` in a string
2. Parse CSV data from a string without the `csv` module using `split()`
3. Write a function that converts snake_case to camelCase and PascalCase
""")

write("_02_04_advanced_collections_module.md", fm(
    "02_04_06","Advanced Collections Module",4,"Collections",6,"intermediate",
    ["Counter","deque","OrderedDict","defaultdict","ChainMap","namedtuple","UserDict","UserList","heapq"]
) + """
## collections.Counter

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
c = Counter(words)
# Counter({'apple': 3, 'banana': 2, 'cherry': 1})

c.most_common(2)   # [('apple', 3), ('banana', 2)]
c["apple"]         # 3
c["missing"]       # 0 (no KeyError)

# Arithmetic
c1 = Counter(a=3, b=2)
c2 = Counter(a=1, b=4)
c1 + c2    # Counter({'b': 6, 'a': 4})
c1 - c2    # Counter({'a': 2})  (negative dropped)
c1 & c2    # Counter({'a': 1, 'b': 2})  (min)
c1 | c2    # Counter({'b': 4, 'a': 3})  (max)

# Character frequency
Counter("hello world")
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

## collections.deque (Double-Ended Queue)

```python
from collections import deque

dq = deque([1, 2, 3], maxlen=5)   # fixed-size sliding window

dq.append(4)        # add to right — O(1)
dq.appendleft(0)    # add to left  — O(1)
dq.pop()            # remove from right — O(1)
dq.popleft()        # remove from left  — O(1)  ← list is O(n)!
dq.rotate(2)        # rotate right by 2
dq.rotate(-1)       # rotate left by 1

# Sliding window maximum
window = deque(maxlen=3)
for x in [1, 3, 5, 2, 4, 7]:
    window.append(x)
    print(max(window))   # max of last 3 elements
```

## heapq — Priority Queue

```python
import heapq

# Min-heap
heap = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(heap)
heapq.heappush(heap, 0)
smallest = heapq.heappop(heap)    # 0

# N largest / smallest
heapq.nlargest(3, data)           # [9, 6, 5]
heapq.nsmallest(3, data)          # [0, 1, 1]

# Priority queue with tuples (priority, item)
tasks = []
heapq.heappush(tasks, (2, "medium task"))
heapq.heappush(tasks, (1, "urgent task"))
heapq.heappush(tasks, (3, "low task"))
priority, task = heapq.heappop(tasks)   # (1, "urgent task")
```

## UserDict and UserList

```python
from collections import UserDict, UserList

class LowercaseDict(UserDict):
    '''Dict that normalises keys to lowercase'''
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)

    def __getitem__(self, key):
        return super().__getitem__(key.lower())

d = LowercaseDict()
d["Name"] = "Raja"
d["name"]    # "Raja"
```

## Lab Exercise
1. Count word frequencies in a paragraph using `Counter`, find top 5
2. Implement a browser history (back/forward) using `deque`
3. Build a task scheduler using `heapq` priority queue
""")

print(f"Module 4 collections written: {written}")
w_prev = written

# ══════════════════════════════════════════════════════════════════
# MODULE 5: Functions
# ══════════════════════════════════════════════════════════════════

write("_02_05_functions_and_arguments.md", fm(
    "02_05_01","Functions and Arguments",5,"Functions",1,"beginner",
    ["def","return","args","kwargs","positional","keyword","default","*args","**kwargs","keyword-only","positional-only","annotations"]
) + """
## Defining Functions

```python
def greet(name: str, greeting: str = "Hello") -> str:
    \"\"\"Return a greeting string.\"\"\"
    return f"{greeting}, {name}!"

greet("Raja")             # "Hello, Raja!"
greet("Raja", "Namaste")  # "Namaste, Raja!"
greet(greeting="Hi", name="Bob")  # keyword args — any order
```

## Parameter Types

```python
def func(pos_only, /, normal, *, kw_only):
    pass
    # pos_only — must be positional (before /)
    # normal   — can be positional or keyword
    # kw_only  — must be keyword (after *)

func(1, 2, kw_only=3)
func(1, normal=2, kw_only=3)
```

## *args and **kwargs

```python
def variadic(*args, **kwargs):
    print(args)    # tuple of positional extras
    print(kwargs)  # dict of keyword extras

variadic(1, 2, 3, name="Raja", age=28)
# (1, 2, 3)
# {'name': 'Raja', 'age': 28}

# Unpacking into function calls
nums = [1, 2, 3]
params = {"sep": ", ", "end": "!\\n"}
print(*nums, **params)   # 1, 2, 3!
```

## Default Argument Gotcha

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

## Return Values

```python
def divide(a, b):
    if b == 0:
        return None, "Division by zero"
    return a / b, None

result, error = divide(10, 2)    # (5.0, None)
result, error = divide(10, 0)    # (None, "Division by zero")

# Functions without return → return None implicitly
```

## Higher-Order Functions

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

## Lab Exercise
1. Write a function `stats(*numbers)` returning min, max, mean, median
2. Build a `retry(func, times=3)` decorator without using `@`
3. Implement `partial()` manually that pre-fills arguments
""")

write("_02_05_functional_programming.md", fm(
    "02_05_02","Functional Programming in Python",5,"Functions",2,"intermediate",
    ["lambda","map","filter","reduce","sorted","functools","partial","lru-cache","operator","pure-function","immutability"]
) + """
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
""")

write("_02_05_list_dict_set_comprehensions.md", fm(
    "02_05_03","List Dict Set Comprehensions",5,"Functions",3,"beginner",
    ["list-comprehension","dict-comprehension","set-comprehension","generator-expression","nested","conditional","walrus"]
) + """
## Comprehension Syntax

```
[expression   for var in iterable if condition]   # list
{expression   for var in iterable if condition}   # set
{k: v         for var in iterable if condition}   # dict
(expression   for var in iterable if condition)   # generator
```

## List Comprehensions

```python
# Basic
squares = [x**2 for x in range(1, 11)]

# With condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]

# Multiple iterables
pairs = [(x, y) for x in [1,2,3] for y in ['a','b'] if x != 2]

# Flatten 2D matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [val for row in matrix for val in row]

# With walrus — compute once, use twice
results = [y for x in data if (y := transform(x)) > threshold]
```

## Dict Comprehensions

```python
# Invert a dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}

# Transform values
discounted = {name: price * 0.9 for name, price in prices.items()}

# Filter entries
active = {k: v for k, v in users.items() if v["active"]}

# Build from two lists
keys   = ["name", "age", "city"]
values = ["Raja",  28,   "Chennai"]
record = {k: v for k, v in zip(keys, values)}
```

## Set Comprehensions

```python
unique_lengths = {len(word) for word in words}
vowels_used = {c.lower() for c in text if c.lower() in "aeiou"}
```

## Generator Expressions

```python
# Lazy — compute on demand, don't store all in memory
gen = (x**2 for x in range(1_000_000))
next(gen)           # 0
next(gen)           # 1

# Pass directly to functions that accept iterables
total = sum(x**2 for x in range(100))
any(x > 90 for x in scores)
all(len(p) >= 8 for p in passwords)

# Memory comparison
import sys
list_mem = sys.getsizeof([x**2 for x in range(1000)])  # ~8072 bytes
gen_mem  = sys.getsizeof((x**2 for x in range(1000)))  # ~104 bytes
```

## Performance and Readability

```python
# Comprehension vs loop — usually 20-50% faster
import timeit

loop_time = timeit.timeit(
    "result = []\\nfor x in range(100):\\n    result.append(x**2)",
    number=10000
)
comp_time = timeit.timeit(
    "[x**2 for x in range(100)]",
    number=10000
)
```

## When NOT to Use Comprehensions

```python
# Avoid deeply nested or complex conditions — use a loop
# Bad:
result = [transform(x) for x in data if condition1(x)
          if condition2(x) if not condition3(x)]

# Good:
result = []
for x in data:
    if condition1(x) and condition2(x) and not condition3(x):
        result.append(transform(x))
```

## Lab Exercise
1. Build a word frequency dict from a sentence using dict comprehension
2. Find all Pythagorean triples up to n=20 using nested list comprehension
3. Compare memory usage of a generator vs list for 1M squares
""")

# ══════════════════════════════════════════════════════════════════
# MODULE 6: Advanced Python
# ══════════════════════════════════════════════════════════════════

write("_02_06_closures_and_decorators.md", fm(
    "02_06_01","Closures and Decorators",6,"Advanced Python",1,"intermediate",
    ["closure","free-variable","nonlocal","decorator","functools-wraps","stacked","parametrized","class-decorator","property"]
) + """
## Closures

A closure is a function that **remembers the variables from its enclosing scope** even after that scope has finished executing.

```python
def make_counter(start=0):
    count = start                # free variable

    def counter():
        nonlocal count           # modify outer variable
        count += 1
        return count

    return counter               # returns the closure

c1 = make_counter()
c1()   # 1
c1()   # 2
c1()   # 3

c2 = make_counter(10)
c2()   # 11  (independent state)
```

## The `nonlocal` Keyword

```python
def outer():
    x = 10
    def inner():
        nonlocal x    # without this, assigning x creates local var
        x += 1
        return x
    return inner

inc = outer()
inc()   # 11
inc()   # 12
```

## Decorators

A decorator is a function that **wraps another function** to extend its behavior.

```python
import functools

def timer(func):
    @functools.wraps(func)   # preserves __name__, __doc__
    def wrapper(*args, **kwargs):
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end-start:.4f}s")
        return result
    return wrapper

@timer                    # equivalent to: greet = timer(greet)
def greet(name):
    return f"Hello, {name}!"

greet("Raja")   # prints timing, returns "Hello, Raja!"
```

## Parametrized Decorators

```python
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello!")

hello()   # prints "Hello!" 3 times
```

## Stacked Decorators

```python
@decorator_a
@decorator_b
@decorator_c
def func():
    pass
# Equivalent to: func = decorator_a(decorator_b(decorator_c(func)))
# Applied bottom-up, called top-down
```

## Practical Decorators

```python
# Retry on exception
def retry(max_attempts=3, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Retry {attempt+1}/{max_attempts}: {e}")
        return wrapper
    return decorator

@retry(max_attempts=3, exceptions=(ConnectionError,))
def fetch_data(url):
    ...
```

## Class-Based Decorators

```python
class Cache:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        functools.update_wrapper(self, func)

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@Cache
def expensive(n):
    return n ** 2
```

## Lab Exercise
1. Write a `@log_calls` decorator that logs function name + args
2. Build a `@rate_limit(calls_per_second)` decorator using time.sleep
3. Create a `@singleton` class decorator
""")

write("_02_06_generators_and_iterators.md", fm(
    "02_06_02","Generators and Iterators",6,"Advanced Python",2,"intermediate",
    ["generator","yield","send","throw","close","StopIteration","iterator-protocol","__iter__","__next__","itertools","infinite-generator"]
) + """
## The Iterator Protocol

Any object implementing `__iter__()` and `__next__()` is an iterator.

```python
class CountUp:
    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self   # iterator returns itself

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current

for n in CountUp(5):
    print(n)   # 1 2 3 4 5
```

## Generator Functions

A generator function uses `yield` to produce values **lazily**.

```python
def fibonacci():
    a, b = 0, 1
    while True:         # infinite generator
        yield a
        a, b = b, a + b

gen = fibonacci()
[next(gen) for _ in range(10)]   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Finite generator
def evens_up_to(n):
    for i in range(0, n+1, 2):
        yield i

list(evens_up_to(10))   # [0, 2, 4, 6, 8, 10]
```

## Generator Expressions

```python
# Lazy — memory efficient
gen = (x**2 for x in range(1_000_000))
sum(gen)    # computes without storing all squares

# Chaining generators (pipeline)
raw    = (line.strip() for line in open("data.txt"))
nonempty = (line for line in raw if line)
parsed = (line.split(",") for line in nonempty)
```

## yield with send() and throw()

```python
def accumulator():
    total = 0
    while True:
        value = yield total    # yield sends current, receives new
        if value is None:
            break
        total += value

gen = accumulator()
next(gen)       # 0  — prime the generator
gen.send(10)    # 10
gen.send(20)    # 30
gen.send(5)     # 35
```

## itertools — Powerful Combinators

```python
import itertools

# Infinite iterators
itertools.count(1, 2)                  # 1, 3, 5, 7, ...
itertools.cycle([1, 2, 3])            # 1, 2, 3, 1, 2, 3, ...
itertools.repeat("x", 3)              # "x", "x", "x"

# Combinatoric generators
list(itertools.permutations("ABC", 2))  # all 2-char permutations
list(itertools.combinations("ABC", 2))  # all 2-char combinations
list(itertools.product([1,2], [3,4]))   # cartesian product

# Slicing/chaining
itertools.islice(fibonacci(), 10)       # first 10 Fibonacci numbers
itertools.chain([1,2], [3,4], [5,6])   # [1,2,3,4,5,6]
itertools.takewhile(lambda x: x<5, count(1))  # 1,2,3,4
itertools.dropwhile(lambda x: x<5, count(1))  # 5,6,7,...

# Grouping
for key, group in itertools.groupby(sorted_data, key=lambda x: x.category):
    print(key, list(group))
```

## Memory Comparison

```python
import sys, tracemalloc

tracemalloc.start()
# List: all in memory at once
result = [x**2 for x in range(10**6)]
print(tracemalloc.get_peak())   # ~8MB

tracemalloc.clear_traces()
# Generator: O(1) memory
result = sum(x**2 for x in range(10**6))
print(tracemalloc.get_peak())   # ~1KB
```

## Lab Exercise
1. Build a `chunked(iterable, size)` generator that yields chunks
2. Implement a pipeline: read CSV lines → filter → parse → aggregate
3. Create a generator-based `tree_walk(node)` for a nested dict
""")

# ══════════════════════════════════════════════════════════════════
# MODULE 7: OOP
# ══════════════════════════════════════════════════════════════════

write("_02_07_classes_and_instance_mechanics.md", fm(
    "02_07_01","Classes and Instance Mechanics",7,"Object-Oriented Programming",1,"intermediate",
    ["class","self","__init__","instance-attributes","class-attributes","classmethod","staticmethod","__repr__","__str__","slots"]
) + """
## Defining a Class

```python
class BankAccount:
    # Class attribute (shared by all instances)
    interest_rate = 0.05
    _instances = 0

    def __init__(self, owner: str, balance: float = 0.0):
        # Instance attributes (unique per object)
        self.owner = owner
        self._balance = balance   # _ = convention: internal use
        BankAccount._instances += 1

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> float:
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return amount

    @property
    def balance(self) -> float:
        \"\"\"Read-only balance via property.\"\"\"
        return self._balance

    @classmethod
    def set_rate(cls, rate: float) -> None:
        \"\"\"Change rate for ALL accounts.\"\"\"
        cls.interest_rate = rate

    @staticmethod
    def validate_amount(amount: float) -> bool:
        \"\"\"Utility — doesn't need self or cls.\"\"\"
        return amount > 0

    def __repr__(self) -> str:
        \"\"\"Unambiguous — for developers.\"\"\"
        return f"BankAccount(owner={self.owner!r}, balance={self._balance})"

    def __str__(self) -> str:
        \"\"\"Readable — for end users.\"\"\"
        return f"Account[{self.owner}]: ${self._balance:.2f}"
```

## Properties

```python
class Temperature:
    def __init__(self, celsius: float = 0):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

    @celsius.deleter
    def celsius(self):
        del self._celsius

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32

t = Temperature(100)
t.celsius       # 100
t.fahrenheit    # 212.0
t.celsius = 200 # OK
t.celsius = -300  # ValueError
```

## `__slots__` — Memory Optimization

```python
class Point:
    __slots__ = ['x', 'y']   # disables __dict__, saves ~30% memory

    def __init__(self, x, y):
        self.x = x
        self.y = y

import sys
class PointDict:
    def __init__(self, x, y):
        self.x = x; self.y = y

p1 = Point(1, 2)
p2 = PointDict(1, 2)
sys.getsizeof(p1)   # ~48 bytes
sys.getsizeof(p2)   # ~152 bytes (dict overhead)
```

## Lab Exercise
1. Build a `Stack` class with push/pop/peek and `__len__`, `__repr__`
2. Create a `Circle` class with a radius property that auto-computes area and circumference
3. Compare memory of 1000 `__slots__` vs regular instances using `tracemalloc`
""")

write("_02_07_inheritance_and_polymorphism.md", fm(
    "02_07_02","Inheritance and Polymorphism",7,"Object-Oriented Programming",2,"intermediate",
    ["inheritance","super","MRO","multiple-inheritance","abstract-class","ABC","override","isinstance","issubclass","mixin"]
) + """
## Single Inheritance

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError("Subclass must implement speak()")

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name!r})"

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says: Woof!"

    def fetch(self, item: str) -> str:
        return f"{self.name} fetches the {item}!"

class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says: Meow!"

animals = [Dog("Rex"), Cat("Whiskers"), Dog("Buddy")]
for a in animals:
    print(a.speak())   # polymorphism — different speak per type
```

## `super()` and `__init__`

```python
class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_kwh: float):
        super().__init__(make, model, year)   # call parent __init__
        self.battery_kwh = battery_kwh

    def range_estimate(self) -> float:
        return self.battery_kwh * 5   # km per kWh

ev = ElectricVehicle("Tesla", "Model 3", 2024, 75)
ev.range_estimate()   # 375.0
```

## Abstract Base Classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:
        return f"{type(self).__name__}: area={self.area():.2f}"

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius

Shape()    # TypeError: Can't instantiate abstract class
Circle(5)  # OK — all abstract methods implemented
```

## Method Resolution Order (MRO)

```python
class A:
    def method(self): return "A"

class B(A):
    def method(self): return "B"

class C(A):
    def method(self): return "C"

class D(B, C):  # multiple inheritance
    pass

D.mro()   # [D, B, C, A, object]  — C3 linearisation
D().method()  # "B"  — follows MRO
```

## Mixins

```python
class JsonMixin:
    def to_json(self) -> str:
        import json
        return json.dumps(self.__dict__)

class LogMixin:
    def log(self, message: str) -> None:
        print(f"[{type(self).__name__}] {message}")

class User(JsonMixin, LogMixin):
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

u = User("Raja", "raja@example.com")
u.to_json()   # '{"name": "Raja", "email": "raja@example.com"}'
u.log("created")  # [User] created
```

## Lab Exercise
1. Build an animal hierarchy: Animal → Mammal → Dog/Cat; add `speak()`, `breathe()`
2. Use ABC to enforce an interface for payment gateways (Stripe, PayPal)
3. Create a `SerializableMixin` that adds `to_dict()` / `from_dict()` to any class
""")

write("_02_07_magic_dunder_methods.md", fm(
    "02_07_03","Magic Dunder Methods",7,"Object-Oriented Programming",3,"intermediate",
    ["__init__","__repr__","__str__","__len__","__getitem__","__setitem__","__contains__","__eq__","__hash__","__call__","__enter__","__exit__","__iter__"]
) + """
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

is_email = Validator(r"[^@]+@[^@]+\\.[^@]+")
is_email("user@example.com")   # True
is_email("not-an-email")       # False
```

## Lab Exercise
1. Build a `Matrix` class supporting `+`, `*`, `@` (matmul), indexing
2. Create a `Roster` class with full container protocol (add/remove students)
3. Implement a reusable `Timer` context manager using `__enter__`/`__exit__`
""")

write("_02_07_dataclasses_and_protocols.md", fm(
    "02_07_04","Dataclasses and Protocols",7,"Object-Oriented Programming",4,"intermediate",
    ["dataclass","field","frozen","post-init","__post_init__","Protocol","typing","NamedTuple","TypedDict","attrs"]
) + """
## @dataclass

```python
from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class Point:
    x: float
    y: float

    def distance(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

p = Point(3, 4)
p.x          # 3
repr(p)      # Point(x=3, y=4)  — auto-generated
p == Point(3, 4)   # True — auto __eq__
```

## Advanced dataclass Options

```python
@dataclass(frozen=True, order=True)  # immutable + sortable
class Config:
    host: str = "localhost"
    port: int = 8000
    debug: bool = False
    tags: list = field(default_factory=list)  # mutable default

    # Class variable (not a field)
    MAX_CONNECTIONS: ClassVar[int] = 100

    def __post_init__(self):
        # Validate after __init__
        if not 1 <= self.port <= 65535:
            raise ValueError(f"Invalid port: {self.port}")

c = Config(port=443)
c.host = "other"   # FrozenInstanceError (frozen=True)
```

## TypedDict

```python
from typing import TypedDict, Required, NotRequired

class UserRecord(TypedDict):
    id: int
    name: str
    email: str
    age: NotRequired[int]   # optional key

def create_user(data: UserRecord) -> None:
    print(data["name"])

create_user({"id": 1, "name": "Raja", "email": "r@x.com"})  # OK
```

## Protocol (Structural Subtyping)

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None: ...
    def resize(self, factor: float) -> None: ...

class Circle:   # No explicit inheritance!
    def draw(self): print("Drawing circle")
    def resize(self, factor): self.radius *= factor

class Square:
    def draw(self): print("Drawing square")
    def resize(self, factor): self.side *= factor

# Both satisfy the Protocol — duck typing with type safety
def render(shape: Drawable) -> None:
    shape.draw()

render(Circle())   # OK
render(Square())   # OK
isinstance(Circle(), Drawable)  # True (runtime_checkable)
```

## attrs Library

```python
import attrs

@attrs.define
class Product:
    name: str
    price: float = attrs.field(validator=attrs.validators.gt(0))
    category: str = "general"
    tags: list = attrs.Factory(list)

p = Product("Widget", 9.99)
p                    # Product(name='Widget', price=9.99, category='general', tags=[])
Product("Bad", -1)   # ValueError: price must be > 0
```

## Lab Exercise
1. Build a `@dataclass(frozen=True)` `Color` class with RGB validation
2. Create a `Serializable` Protocol requiring `to_json()` and `from_json()`
3. Compare boilerplate: regular class vs `@dataclass` vs `attrs.define` for same model
""")

# ══════════════════════════════════════════════════════════════════
# MODULE 8: Exceptions & Error Handling
# ══════════════════════════════════════════════════════════════════

write("_02_08_exception_handling.md", fm(
    "02_08_01","Exception Handling",8,"Exceptions and File I/O",1,"intermediate",
    ["try","except","else","finally","raise","raise-from","custom-exception","exception-hierarchy","ExceptionGroup","suppress"]
) + """
## Exception Hierarchy

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError (ZeroDivisionError, OverflowError)
    ├── LookupError (IndexError, KeyError)
    ├── ValueError
    ├── TypeError
    ├── IOError (FileNotFoundError, PermissionError)
    ├── RuntimeError
    ├── AttributeError
    └── ...
```

## try / except / else / finally

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError as e:
        print(f"Type error: {e}")
        return None
    else:
        # Runs only if no exception
        print(f"Result: {result}")
        return result
    finally:
        # ALWAYS runs (cleanup)
        print("Division attempted")
```

## Exception Information

```python
try:
    x = int("abc")
except ValueError as e:
    print(type(e).__name__)   # ValueError
    print(e.args)             # ('invalid literal...',)
    print(str(e))             # invalid literal for int()...
    import traceback
    traceback.print_exc()     # full traceback
```

## Raising Exceptions

```python
def set_age(age: int) -> None:
    if not isinstance(age, int):
        raise TypeError(f"Age must be int, got {type(age).__name__}")
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    return age

# raise from — chaining exceptions
try:
    data = json.loads(raw)
except json.JSONDecodeError as e:
    raise ValueError("Invalid configuration file") from e
    # Traceback shows both exceptions; `from e` sets __cause__
```

## Custom Exceptions

```python
class AppError(Exception):
    \"\"\"Base exception for this application.\"\"\"

class ValidationError(AppError):
    def __init__(self, field: str, message: str):
        self.field = field
        self.message = message
        super().__init__(f"Validation error on '{field}': {message}")

class NotFoundError(AppError):
    def __init__(self, resource: str, id: int):
        super().__init__(f"{resource} with id={id} not found")
        self.resource = resource
        self.id = id

try:
    raise ValidationError("email", "Invalid format")
except ValidationError as e:
    print(e.field)    # email
    print(e.message)  # Invalid format
```

## contextlib.suppress

```python
from contextlib import suppress

# Instead of try/except pass:
with suppress(FileNotFoundError):
    os.remove("temp_file.txt")
```

## ExceptionGroup (Python 3.11+)

```python
# For concurrent tasks that may raise multiple exceptions
try:
    raise ExceptionGroup("multiple errors", [
        ValueError("bad value"),
        TypeError("wrong type"),
    ])
except* ValueError as eg:
    print("Handled ValueError:", eg.exceptions)
except* TypeError as eg:
    print("Handled TypeError:", eg.exceptions)
```

## Lab Exercise
1. Build a `safe_open()` function with specific error messages for each IOError type
2. Create a custom exception hierarchy for an e-commerce app (OrderError, PaymentError, etc.)
3. Write a `retry_on_exception(func, exceptions, max_retries)` utility
""")

write("_02_08_context_managers.md", fm(
    "02_08_02","Context Managers",8,"Exceptions and File I/O",2,"intermediate",
    ["with","__enter__","__exit__","contextlib","contextmanager","suppress","closing","ExitStack","async-context-manager"]
) + """
## Context Manager Protocol

```python
# Any object with __enter__ and __exit__
class Timer:
    import time

    def __enter__(self):
        self.start = Timer.time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = Timer.time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.4f}s")
        return False   # False = propagate exceptions

with Timer() as t:
    total = sum(range(10**7))
print(f"Total: {total}, time: {t.elapsed:.4f}s")
```

## contextlib.contextmanager

```python
from contextlib import contextmanager

@contextmanager
def managed_resource(name: str):
    print(f"Acquiring {name}")
    resource = acquire(name)
    try:
        yield resource   # value bound to `as` variable
    finally:
        release(resource)
        print(f"Released {name}")

with managed_resource("database") as db:
    db.query("SELECT ...")
```

## Practical Examples

```python
# Database transaction
@contextmanager
def transaction(conn):
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise

# Temporary directory
from contextlib import contextmanager
import tempfile, shutil, os

@contextmanager
def temp_dir():
    path = tempfile.mkdtemp()
    try:
        yield path
    finally:
        shutil.rmtree(path)

with temp_dir() as d:
    # work in temporary directory
    pass  # auto-deleted on exit
```

## contextlib.ExitStack

```python
from contextlib import ExitStack

# Open dynamic number of files
with ExitStack() as stack:
    files = [
        stack.enter_context(open(f"file{i}.txt"))
        for i in range(5)
    ]
    # All 5 files auto-closed on exit
```

## Async Context Managers

```python
import aiofiles

async def read_file(path: str) -> str:
    async with aiofiles.open(path, "r") as f:
        return await f.read()

# Custom async context manager
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_timer():
    import time
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"Elapsed: {time.perf_counter()-start:.4f}s")
```

## Lab Exercise
1. Build a `locked_file(path)` context manager that creates a `.lock` file on entry
2. Write a `rollback_on_error(dict_)` context manager that restores dict on exception
3. Chain 3 context managers using `ExitStack`
""")

write("_02_08_logging_module.md", fm(
    "02_08_03","Logging Module",8,"Exceptions and File I/O",3,"intermediate",
    ["logging","Logger","Handler","Formatter","basicConfig","FileHandler","RotatingFileHandler","levels","structlog","rich-logging"]
) + """
## Python Logging Overview

```python
import logging

# Basic setup
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

logger.debug("Debug message — detailed diagnostic")
logger.info("Info message — general events")
logger.warning("Warning — unexpected but handled")
logger.error("Error — operation failed")
logger.critical("Critical — program may not recover")
```

## Log Levels

| Level | Value | When to Use |
|---|---|---|
| DEBUG | 10 | Detailed diagnostic information |
| INFO | 20 | Confirmation things are working |
| WARNING | 30 | Unexpected, but recoverable |
| ERROR | 40 | Serious problem, function failed |
| CRITICAL | 50 | Program may crash |

## Production Logger Setup

```python
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name: str, log_file: str, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Console handler
    console = logging.StreamHandler()
    console.setLevel(logging.WARNING)

    # File handler with rotation (5MB, keep 3 backups)
    file_handler = RotatingFileHandler(
        log_file, maxBytes=5*1024*1024, backupCount=3
    )
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(funcName)s:%(lineno)d | %(message)s"
    )
    console.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)
    return logger

logger = setup_logger("myapp", "app.log")
```

## Logging Exceptions

```python
try:
    result = 1 / 0
except ZeroDivisionError:
    logger.exception("Division failed")   # logs full traceback
    # OR
    logger.error("Division failed", exc_info=True)
```

## Structured Logging with structlog

```python
import structlog

log = structlog.get_logger()
log.info("user.login", user_id=42, ip="192.168.1.1")
# {"event": "user.login", "user_id": 42, "ip": "192.168.1.1", "timestamp": "..."}
```

## Lab Exercise
1. Configure separate DEBUG file log and WARNING console log for a module
2. Add request ID to all log messages in a FastAPI app using `logging.LoggerAdapter`
3. Set up JSON-formatted logs using `structlog` for production
""")

# ══════════════════════════════════════════════════════════════════
# MODULE 9: File I/O
# ══════════════════════════════════════════════════════════════════

write("_02_09_file_io_and_paths.md", fm(
    "02_09_01","File I/O and Paths",9,"File I/O and Serialisation",1,"beginner",
    ["open","read","write","readline","pathlib","Path","glob","shutil","os.path","context-manager","text-vs-binary"]
) + """
## File Operations

```python
# Reading
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()          # entire file as string
    lines   = f.readlines()     # list of lines (with \\n)
    line    = f.readline()      # one line

# Writing
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\\n")

# Appending
with open("log.txt", "a") as f:
    f.write(f"Entry: {entry}\\n")

# Binary mode
with open("image.png", "rb") as f:
    data = f.read()

with open("copy.png", "wb") as f:
    f.write(data)
```

## File Modes

| Mode | Description |
|---|---|
| `r` | Read (default) |
| `w` | Write (create/truncate) |
| `a` | Append |
| `x` | Exclusive create (fails if exists) |
| `b` | Binary (append to mode: `rb`, `wb`) |
| `+` | Read+Write (`r+`, `w+`) |

## pathlib — Modern Path Handling

```python
from pathlib import Path

# Build paths (cross-platform)
base = Path("/var/www/myapp")
config = base / "config" / "settings.json"

config.exists()        # True/False
config.is_file()       # True
config.is_dir()        # False
config.suffix          # ".json"
config.stem            # "settings"
config.name            # "settings.json"
config.parent          # Path('/var/www/myapp/config')

# Read/Write directly
config.read_text(encoding="utf-8")
config.write_text('{"debug": false}')
config.read_bytes()
config.write_bytes(data)

# Glob patterns
list(base.glob("**/*.py"))       # all Python files recursively
list(base.glob("*.json"))        # JSON files in base only

# Create directories
(base / "new_dir").mkdir(parents=True, exist_ok=True)

# Rename / move
old = Path("old.txt")
old.rename("new.txt")           # rename in-place

# Delete
config.unlink()                 # delete file
(base / "empty_dir").rmdir()   # delete empty dir
import shutil
shutil.rmtree(base / "full_dir")  # delete dir with contents
```

## CSV and JSON Files

```python
import csv, json

# CSV read
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])

# CSV write
with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows([{"name": "Raja", "age": 28}])

# JSON
data = {"users": [{"id": 1, "name": "Raja"}]}
text = json.dumps(data, indent=2, ensure_ascii=False)
parsed = json.loads(text)

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json") as f:
    data = json.load(f)
```

## Lab Exercise
1. Build a log parser that reads a log file and counts errors per hour
2. Recursively find all `.py` files in a directory using `pathlib.glob`
3. Write a config manager that reads/writes JSON and handles missing keys gracefully
""")

write("_02_09_data_serialization.md", fm(
    "02_09_02","Data Serialization",9,"File I/O and Serialisation",2,"intermediate",
    ["json","pickle","csv","yaml","tomllib","msgpack","pydantic","dataclass-json","orjson","serialization-patterns"]
) + """
## JSON

```python
import json

# Serialise Python → JSON string
data = {"name": "Raja", "scores": [90, 85, 92], "active": True}
text = json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False)

# Custom encoder for non-serialisable types
from datetime import datetime
from dataclasses import dataclass, asdict

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

json.dumps({"ts": datetime.now()}, cls=DateTimeEncoder)
```

## pickle — Python Object Serialization

```python
import pickle

# Serialize any Python object
data = {"model": trained_sklearn_model, "params": {...}}

with open("model.pkl", "wb") as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

with open("model.pkl", "rb") as f:
    loaded = pickle.load(f)

# ⚠️ NEVER unpickle untrusted data — arbitrary code execution risk!
```

## YAML (requires PyYAML)

```python
import yaml

config = yaml.safe_load('''
database:
  host: localhost
  port: 5432
  name: mydb
debug: false
''')

config["database"]["host"]   # "localhost"

with open("config.yaml") as f:
    config = yaml.safe_load(f)

yaml.dump(config, default_flow_style=False)
```

## TOML (Python 3.11+ built-in)

```python
import tomllib   # read only in 3.11+
# pip install tomli for older Python

with open("pyproject.toml", "rb") as f:
    config = tomllib.load(f)

# Write: use tomli-w
import tomli_w
with open("config.toml", "wb") as f:
    tomli_w.dump({"key": "value"}, f)
```

## Pydantic Serialization

```python
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    created_at: datetime = datetime.now()

# From dict / JSON
user = User(id=1, name="Raja")
user = User.model_validate({"id": 1, "name": "Raja"})
user = User.model_validate_json('{"id": 1, "name": "Raja"}')

# To dict / JSON
user.model_dump()              # dict
user.model_dump_json()         # JSON string
user.model_dump(exclude={"created_at"})
```

## orjson — Fast JSON

```python
import orjson

# 5-10x faster than stdlib json
data = {"name": "Raja", "scores": [1,2,3]}
encoded = orjson.dumps(data)          # bytes
decoded = orjson.loads(encoded)       # dict

# Handles datetime, UUID, numpy arrays natively
orjson.dumps(datetime.now())          # works!
```

## Lab Exercise
1. Serialize a list of dataclass objects to JSON and back
2. Build a config system supporting YAML, TOML, and JSON with unified API
3. Benchmark `json` vs `orjson` vs `ujson` for 10,000 serializations
""")

# ══════════════════════════════════════════════════════════════════
# MODULE 10: Regex
# ══════════════════════════════════════════════════════════════════

write("_02_10_regular_expressions.md", fm(
    "02_10_01","Regular Expressions",10,"Regular Expressions",1,"intermediate",
    ["re","match","search","findall","finditer","group","groups","compile","flags","lookahead","lookbehind","named-groups"]
) + """
## re Module Basics

```python
import re

pattern = r"\\d{3}-\\d{4}"   # phone number pattern
text = "Call 555-1234 or 800-5678"

# match — only at the beginning of string
re.match(r"\\d+", "123 abc")    # Match object
re.match(r"\\d+", "abc 123")    # None

# search — anywhere in string
re.search(r"\\d+", "abc 123")   # Match at pos 4

# findall — all non-overlapping matches
re.findall(r"\\d{3}-\\d{4}", text)    # ['555-1234', '800-5678']

# finditer — iterator of Match objects
for m in re.finditer(r"\\d{3}-\\d{4}", text):
    print(m.group(), m.start(), m.end())
```

## Regex Syntax Reference

```
.       Any character except newline
\\d      Digit [0-9]
\\D      Non-digit
\\w      Word char [a-zA-Z0-9_]
\\W      Non-word
\\s      Whitespace
\\S      Non-whitespace
\\b      Word boundary
^       Start of string
$       End of string

{n}     Exactly n repetitions
{n,m}   Between n and m
*       0 or more (greedy)
+       1 or more (greedy)
?       0 or 1 (greedy)
*?      0 or more (lazy/non-greedy)
+?      1 or more (lazy)

[abc]   Character class
[^abc]  Negated class
(abc)   Capturing group
(?:abc) Non-capturing group
|       Alternation
```

## Groups and Named Groups

```python
# Groups
m = re.search(r"(\\d{4})-(\\d{2})-(\\d{2})", "Date: 2024-07-28")
m.group(0)   # "2024-07-28" (full match)
m.group(1)   # "2024"
m.group(2)   # "07"
m.groups()   # ("2024", "07", "28")

# Named groups
pattern = r"(?P<year>\\d{4})-(?P<month>\\d{2})-(?P<day>\\d{2})"
m = re.search(pattern, "Date: 2024-07-28")
m.group("year")   # "2024"
m.groupdict()     # {"year": "2024", "month": "07", "day": "28"}
```

## sub and subn

```python
# Replace matches
re.sub(r"\\s+", " ", "  too   many   spaces  ")  # "  too many spaces  "
re.sub(r"^\\s+|\\s+$", "", "  stripped  ")         # "stripped"

# Replace with function
def double_digit(m):
    return str(int(m.group()) * 2)

re.sub(r"\\d+", double_digit, "a1 b22 c333")   # "a2 b44 c666"

# With backreferences
re.sub(r"(\\w+) (\\w+)", r"\\2 \\1", "hello world")   # "world hello"
```

## Compiled Patterns

```python
EMAIL_RE = re.compile(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}",
    re.IGNORECASE
)

# Reuse without recompiling
EMAIL_RE.findall(text)
EMAIL_RE.search(text)
```

## Lookahead and Lookbehind

```python
# Positive lookahead (?=...)
re.findall(r"\\d+(?= dollars)", "5 dollars and 10 euros")   # ["5"]

# Negative lookahead (?!...)
re.findall(r"\\d+(?! euros)", "5 dollars 10 euros")          # ["5"]

# Positive lookbehind (?<=...)
re.findall(r"(?<=\\$)\\d+", "Total: $50 and $30")            # ["50", "30"]
```

## Lab Exercise
1. Parse log lines: extract timestamp, level, message using named groups
2. Validate password complexity: min 8 chars, uppercase, digit, special char
3. Extract all URLs from HTML using `re.findall()` with a robust pattern
""")

# ══════════════════════════════════════════════════════════════════
# MODULE 11: Modules and Packages
# ══════════════════════════════════════════════════════════════════

write("_02_11_modules_and_packages.md", fm(
    "02_11_01","Modules and Packages",11,"Modules and Packages",1,"intermediate",
    ["import","from-import","as","__name__","__all__","package","__init__","relative-import","sys.path","importlib","namespace-package"]
) + """
## Importing Modules

```python
import os                        # import whole module
import os.path                   # import sub-module
from os import getcwd, listdir   # import specific names
from os import *                 # import all (avoid!)
import numpy as np               # alias
from pathlib import Path as P    # alias for name

# Conditional import
try:
    import ujson as json
except ImportError:
    import json
```

## Module Attributes

```python
# __name__ — string name of current module
if __name__ == "__main__":
    # Runs only when script is executed directly, not imported
    main()

# __file__ — absolute path of module file
print(__file__)   # /path/to/mymodule.py

# __all__ — controls what `from module import *` exports
__all__ = ["PublicClass", "public_function"]
```

## Package Structure

```
mypackage/
    __init__.py          # Makes folder a package
    core.py
    utils.py
    database/
        __init__.py
        models.py
        queries.py
```

```python
# mypackage/__init__.py
from .core import MainClass        # relative import
from .utils import helper_func
from .database.models import User

__version__ = "1.0.0"
__all__ = ["MainClass", "helper_func", "User"]
```

## Relative Imports

```python
# Inside mypackage/database/queries.py
from .models import User          # same package
from ..utils import helper_func   # parent package
from ..core import MainClass      # parent package
```

## sys.path and Import Resolution

```python
import sys

# Python searches for modules in:
# 1. Current directory
# 2. PYTHONPATH env variable
# 3. Standard library
# 4. site-packages (installed packages)

print(sys.path)

# Add custom path at runtime
sys.path.insert(0, "/path/to/my/libraries")
```

## importlib — Dynamic Imports

```python
import importlib

# Import by string name
module = importlib.import_module("os.path")
func = getattr(module, "join")

# Reload a changed module (useful in development)
import my_module
importlib.reload(my_module)

# Plugin system
def load_plugin(name: str):
    return importlib.import_module(f"plugins.{name}")
```

## Lab Exercise
1. Create a package `calculator` with `add`, `subtract`, `multiply` in separate modules
2. Implement a plugin system that loads modules by name from a `plugins/` directory
3. Write a `__init__.py` that lazy-imports submodules only on first attribute access
""")

# ══════════════════════════════════════════════════════════════════
# MODULE 12: Concurrency
# ══════════════════════════════════════════════════════════════════

write("_02_12_asyncio_and_async_await.md", fm(
    "02_12_01","Asyncio and Async/Await",12,"Concurrency",1,"advanced",
    ["asyncio","async","await","coroutine","event-loop","gather","create-task","aiohttp","asyncpg","async-context-manager","async-generator"]
) + """
## Async/Await Fundamentals

```python
import asyncio

# Coroutine — defined with async def
async def greet(name: str, delay: float) -> str:
    await asyncio.sleep(delay)   # non-blocking sleep
    return f"Hello, {name}!"

# Run coroutine
result = asyncio.run(greet("Raja", 1.0))

# Multiple coroutines concurrently
async def main():
    # gather — run concurrently, wait for all
    results = await asyncio.gather(
        greet("Alice", 1.0),
        greet("Bob",   0.5),
        greet("Charlie", 1.5),
    )
    # Total time ≈ 1.5s (not 3s!)
    print(results)

asyncio.run(main())
```

## Tasks — Fire and Forget

```python
async def main():
    # Create task — schedules coroutine, doesn't await yet
    task1 = asyncio.create_task(fetch_data("url1"))
    task2 = asyncio.create_task(fetch_data("url2"))

    # Do other work while tasks run
    print("Tasks started")

    # Now wait for results
    result1 = await task1
    result2 = await task2

    # Cancel a task
    task1.cancel()
    try:
        await task1
    except asyncio.CancelledError:
        print("Task cancelled")
```

## Async HTTP with aiohttp

```python
import aiohttp

async def fetch(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.json()

async def fetch_all(urls: list[str]) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)

results = asyncio.run(fetch_all(["https://api.example.com/1",
                                  "https://api.example.com/2"]))
```

## asyncio Primitives

```python
# Semaphore — limit concurrency
sem = asyncio.Semaphore(10)  # max 10 concurrent

async def limited_fetch(url):
    async with sem:
        return await fetch(url)

# Queue — async producer/consumer
queue = asyncio.Queue(maxsize=100)

async def producer():
    for item in data:
        await queue.put(item)
    await queue.put(None)  # sentinel

async def consumer():
    while True:
        item = await queue.get()
        if item is None:
            break
        await process(item)
        queue.task_done()
```

## Async Context Managers and Generators

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def db_connection():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()

async with db_connection() as conn:
    await conn.fetch("SELECT * FROM users")

# Async generator
async def paginate(url: str):
    page = 1
    while True:
        data = await fetch(f"{url}?page={page}")
        if not data:
            break
        for item in data:
            yield item
        page += 1

async for user in paginate("https://api.example.com/users"):
    process(user)
```

## Lab Exercise
1. Fetch 100 URLs concurrently with `aiohttp` and `gather`, limit to 10 at a time with `Semaphore`
2. Build a producer-consumer pipeline using `asyncio.Queue`
3. Port a synchronous recursive file scanner to async using `aiofiles`
""")

write("_02_12_threading_and_multiprocessing.md", fm(
    "02_12_02","Threading and Multiprocessing",12,"Concurrency",2,"advanced",
    ["threading","Thread","Lock","RLock","Semaphore","Queue","multiprocessing","Pool","Process","shared-memory","concurrent.futures","ProcessPoolExecutor","ThreadPoolExecutor"]
) + """
## Threading

```python
import threading

def download(url: str, results: list, lock: threading.Lock) -> None:
    data = fetch(url)
    with lock:   # protect shared resource
        results.append(data)

results = []
lock = threading.Lock()
threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url, results, lock))
    threads.append(t)
    t.start()

for t in threads:
    t.join()   # wait for all threads to finish
```

## Thread Synchronization

```python
# RLock — re-entrant lock (same thread can acquire multiple times)
rlock = threading.RLock()

# Semaphore — limit concurrent access
sem = threading.Semaphore(5)   # max 5 threads

# Event — signal between threads
event = threading.Event()

# Producer-Consumer with Queue
from queue import Queue

q = Queue(maxsize=100)

def producer():
    for item in data_source:
        q.put(item)   # blocks if full
    q.put(None)       # sentinel

def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        process(item)
        q.task_done()
```

## concurrent.futures — High-Level Interface

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Threading — best for I/O bound
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(fetch, url) for url in urls]
    results = [f.result() for f in futures]

# Map — simpler API
with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch, urls))

# ProcessPoolExecutor — best for CPU bound
def cpu_heavy(n: int) -> int:
    return sum(i**2 for i in range(n))

with ProcessPoolExecutor() as executor:
    results = list(executor.map(cpu_heavy, [10**6]*4))
```

## multiprocessing — True Parallelism

```python
from multiprocessing import Pool, Process, Queue, Value, Array

# Pool.map — parallel map
with Pool(processes=4) as pool:
    results = pool.map(cpu_heavy, data)

# Shared memory
counter = Value("i", 0)    # shared integer
arr = Array("d", range(10)) # shared float array

def increment(counter, lock):
    for _ in range(1000):
        with lock:
            counter.value += 1
```

## When to Use What

| Scenario | Tool |
|---|---|
| I/O bound (HTTP, files) | `asyncio` or `ThreadPoolExecutor` |
| CPU bound (compute, ML) | `ProcessPoolExecutor` or `multiprocessing` |
| Simple parallel map | `concurrent.futures.ProcessPoolExecutor` |
| Fine-grained sync | `threading` with `Lock/Event/Queue` |

## Lab Exercise
1. Download 50 images using `ThreadPoolExecutor(max_workers=10)`
2. Compute prime factors of 1000 numbers using `ProcessPoolExecutor`
3. Build a thread-safe rate limiter using `threading.Semaphore` and `time`
""")

# ══════════════════════════════════════════════════════════════════
# MODULE 13: Misc advanced topics
# ══════════════════════════════════════════════════════════════════

write("_02_13_numpy_fundamentals.md", fm(
    "02_13_01","NumPy Fundamentals",13,"Scientific Python",1,"intermediate",
    ["numpy","ndarray","dtype","shape","reshape","broadcasting","vectorization","indexing","slicing","ufunc","linspace","random"]
) + """
## NumPy Basics

```python
import numpy as np

# Creating arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6]])

a.shape    # (5,)
b.shape    # (2, 3)
a.dtype    # int64
b.ndim     # 2

# Common constructors
np.zeros((3, 4))           # 3x4 zeros
np.ones((2, 2))            # 2x2 ones
np.eye(3)                  # 3x3 identity
np.arange(0, 10, 2)        # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)       # [0, 0.25, 0.5, 0.75, 1.0]
np.random.randn(3, 3)      # 3x3 standard normal
```

## Indexing and Slicing

```python
a = np.arange(12).reshape(3, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

a[1, 2]      # 6
a[:, 1]      # [1, 5, 9]  — column 1
a[0, :]      # [0, 1, 2, 3]  — row 0
a[1:, 2:]    # [[6, 7], [10, 11]]

# Boolean indexing
a[a > 5]     # [6, 7, 8, 9, 10, 11]
a[a % 2 == 0]  # even elements
```

## Vectorized Operations (No Loops!)

```python
x = np.array([1, 2, 3, 4, 5])

x * 2          # [2, 4, 6, 8, 10]
x ** 2         # [1, 4, 9, 16, 25]
np.sqrt(x)     # [1, 1.41, 1.73, 2, 2.24]
np.sum(x)      # 15
np.mean(x)     # 3.0
np.std(x)      # 1.414...
```

## Broadcasting

```python
a = np.array([[1,2,3],[4,5,6]])  # (2,3)
b = np.array([10, 20, 30])       # (3,)
a + b   # [[11,22,33],[14,25,36]] — b broadcast to (2,3)

col = np.array([[10],[20]])       # (2,1)
a + col   # [[11,12,13],[24,25,26]] — col broadcast to (2,3)
```

## Matrix Operations

```python
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

A @ B             # matrix multiplication
np.dot(A, B)      # same as @
A.T               # transpose
np.linalg.inv(A)  # inverse
np.linalg.det(A)  # determinant
eigenvalues, eigenvectors = np.linalg.eig(A)
```

## Lab Exercise
1. Compute the running mean of a 1M-element array without Python loops
2. Implement linear regression using NumPy matrix operations only
3. Benchmark: Python loop vs NumPy vectorization for element-wise operations
""")

write("_02_13_pandas_fundamentals.md", fm(
    "02_13_02","Pandas Fundamentals",13,"Scientific Python",2,"intermediate",
    ["pandas","DataFrame","Series","read-csv","groupby","merge","pivot","apply","fillna","dropna","loc","iloc","datetime"]
) + """
## Pandas Basics

```python
import pandas as pd

# Series — 1D labeled array
s = pd.Series([1, 2, 3], index=["a", "b", "c"])

# DataFrame — 2D labeled table
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "score": [85.5, 92.0, 78.5]
})

# Loading data
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
df = pd.read_json("data.json")
```

## Selection and Filtering

```python
df["name"]           # column as Series
df[["name","age"]]   # multiple columns as DataFrame

# loc — label-based
df.loc[0]             # row by index label
df.loc[0:2, "name":"age"]   # rows 0-2, cols name to age

# iloc — integer position
df.iloc[0]            # first row
df.iloc[0:3, 0:2]     # first 3 rows, first 2 cols

# Boolean filtering
df[df["age"] > 28]
df[(df["age"] > 25) & (df["score"] >= 80)]
df.query("age > 25 and score >= 80")
```

## Essential Operations

```python
df.info()            # dtypes, null counts
df.describe()        # statistics
df.shape             # (rows, cols)
df.dtypes            # column types
df.head(5)           # first 5 rows
df.tail(5)           # last 5 rows

# Sorting
df.sort_values("score", ascending=False)
df.sort_values(["age", "score"])

# Missing values
df.isnull().sum()           # count nulls per column
df.dropna()                 # drop rows with any null
df.fillna(0)                # fill nulls with 0
df.fillna(df.mean())        # fill with column means

# Rename columns
df.rename(columns={"name": "full_name"})

# Apply function
df["score_grade"] = df["score"].apply(
    lambda x: "A" if x >= 90 else "B" if x >= 75 else "C"
)
```

## GroupBy

```python
# Split → Apply → Combine
grouped = df.groupby("department")
grouped["salary"].mean()      # mean salary per department
grouped["salary"].agg(["mean", "max", "count"])

grouped.apply(lambda g: g.nlargest(3, "salary"))  # top 3 per group
```

## Merge and Join

```python
# merge (SQL-style join)
merged = pd.merge(orders, customers,
                  left_on="customer_id", right_on="id",
                  how="left")

# concat (stack DataFrames)
all_data = pd.concat([df1, df2, df3], ignore_index=True)
```

## Lab Exercise
1. Load a sales CSV, compute monthly revenue grouped by product category
2. Merge two DataFrames (orders + products) and calculate average order value
3. Find and fill missing values: numerical with mean, categorical with mode
""")

write("_02_13_matplotlib_and_visualization.md", fm(
    "02_13_03","Matplotlib and Visualization",13,"Scientific Python",3,"intermediate",
    ["matplotlib","pyplot","figure","axes","plot","scatter","bar","hist","subplot","seaborn","plotly","savefig","style"]
) + """
## Matplotlib Basics

```python
import matplotlib.pyplot as plt
import numpy as np

# Line plot
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x, y, color="blue", linewidth=2, label="sin(x)")
ax.plot(x, np.cos(x), "r--", linewidth=1.5, label="cos(x)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Sine and Cosine")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("plot.png", dpi=150)
plt.show()
```

## Common Plot Types

```python
# Scatter
ax.scatter(x, y, c=colors, s=sizes, alpha=0.6)

# Bar
ax.bar(categories, values, color="steelblue")
ax.barh(categories, values)   # horizontal

# Histogram
ax.hist(data, bins=30, density=True, alpha=0.7)

# Box plot
ax.boxplot([group1, group2, group3], labels=["A","B","C"])

# Pie
ax.pie(sizes, labels=labels, autopct="%1.1f%%")
```

## Subplots

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0, 0].plot(x, y)
axes[0, 1].scatter(x, y)
axes[1, 0].bar(cats, vals)
axes[1, 1].hist(data)
plt.tight_layout()
```

## Seaborn — Statistical Plots

```python
import seaborn as sns

# Distribution
sns.histplot(df["score"], kde=True)
sns.boxplot(x="department", y="salary", data=df)
sns.violinplot(x="category", y="value", data=df)

# Relationships
sns.scatterplot(x="age", y="salary", hue="department", data=df)
sns.lineplot(x="date", y="revenue", data=df)

# Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", vmin=-1, vmax=1)

# Pair plot
sns.pairplot(df, hue="category")
```

## Lab Exercise
1. Plot monthly sales trends with dual y-axes (revenue + units sold)
2. Create a correlation heatmap for a financial dataset using Seaborn
3. Build an interactive scatter plot using `plotly.express.scatter()`
""")

write("_02_13_hardware_interfacing_python.md", fm(
    "02_13_04","Hardware Interfacing with Python",13,"Scientific Python",4,"intermediate",
    ["RPi.GPIO","gpiozero","serial","pyserial","I2C","SPI","smbus2","MicroPython","machine","Pin","ADC","PWM"]
) + """
## Raspberry Pi GPIO

```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)    # use BCM pin numbering
GPIO.setup(18, GPIO.OUT)  # pin 18 as output
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # pin 24 input

# Blink LED
try:
    while True:
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.5)
finally:
    GPIO.cleanup()   # always clean up!
```

## gpiozero — Higher Level

```python
from gpiozero import LED, Button, DistanceSensor
from time import sleep

led = LED(18)
button = Button(17)

# Event-driven
button.when_pressed = led.on
button.when_released = led.off

# Distance sensor (HC-SR04)
sensor = DistanceSensor(echo=24, trigger=23)
while True:
    print(f"Distance: {sensor.distance * 100:.1f} cm")
    sleep(0.1)
```

## PySerial — UART Communication

```python
import serial

# Connect to Arduino/ESP32
ser = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)

# Send command
ser.write(b"READ_TEMP\\n")

# Read response
line = ser.readline().decode("utf-8").strip()
print(f"Temperature: {line}")

ser.close()
```

## smbus2 — I2C Communication

```python
from smbus2 import SMBus

# Read from BME280 sensor at address 0x76
with SMBus(1) as bus:
    # Read 2 bytes from register 0xF3
    data = bus.read_i2c_block_data(0x76, 0xF3, 2)
    raw_temp = (data[0] << 8) | data[1]
```

## MicroPython

```python
# On ESP32/Pico
from machine import Pin, ADC, PWM
import time

# LED blink
led = Pin(2, Pin.OUT)
while True:
    led.value(1); time.sleep(0.5)
    led.value(0); time.sleep(0.5)

# ADC reading
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)   # 0-3.3V range
voltage = adc.read() * 3.3 / 4095

# PWM (servo control)
servo = PWM(Pin(5), freq=50)
servo.duty(77)   # ~0 degrees
```

## Lab Exercise
1. Read temperature from DHT11 using `gpiozero` and log to CSV every 10 seconds
2. Send commands over serial to an Arduino to blink an LED at variable frequencies
3. Read ADC values from a potentiometer on ESP32 via MicroPython and print the voltage
""")

# ══════════════════════════════════════════════════════════════════
# MODULE 14: Debugging and Testing
# ══════════════════════════════════════════════════════════════════

write("_02_14_debugging_and_profiling.md", fm(
    "02_14_01","Debugging and Profiling",14,"Debugging and Testing",1,"intermediate",
    ["pdb","breakpoint","ipdb","cProfile","timeit","line-profiler","memory-profiler","tracemalloc","py-spy","logging"]
) + """
## Python Debugger (pdb)

```python
# Method 1: breakpoint() built-in (3.7+)
def buggy_function(data):
    for item in data:
        breakpoint()   # drops into debugger here
        process(item)

# Method 2: explicit import
import pdb; pdb.set_trace()

# Method 3: post-mortem (debug after exception)
import pdb, traceback
try:
    buggy_code()
except Exception:
    traceback.print_exc()
    pdb.post_mortem()
```

### pdb Commands

| Command | Action |
|---|---|
| `n` (next) | Next line |
| `s` (step) | Step into function |
| `c` (continue) | Continue to next breakpoint |
| `l` (list) | Show current code |
| `p expr` | Print expression |
| `pp expr` | Pretty-print |
| `u`/`d` | Up/down stack frame |
| `w` (where) | Print stack trace |
| `q` (quit) | Exit debugger |
| `b 42` | Set breakpoint at line 42 |
| `cl` | Clear breakpoints |

## Profiling with cProfile

```python
import cProfile, pstats, io

profiler = cProfile.Profile()
profiler.enable()

# Code to profile
result = expensive_function()

profiler.disable()

# Print stats
stream = io.StringIO()
stats = pstats.Stats(profiler, stream=stream)
stats.sort_stats("cumulative")
stats.print_stats(20)   # top 20 functions
print(stream.getvalue())
```

## timeit — Micro-Benchmarking

```python
import timeit

# Statement timing
t = timeit.timeit("'-'.join(str(n) for n in range(100))", number=10000)
print(f"{t:.4f}s for 10000 runs")

# Compare two approaches
setup = "data = list(range(1000))"
t1 = timeit.timeit("[x**2 for x in data]", setup=setup, number=1000)
t2 = timeit.timeit("list(map(lambda x: x**2, data))", setup=setup, number=1000)
print(f"Comprehension: {t1:.4f}s, map: {t2:.4f}s")
```

## Memory Profiling

```python
import tracemalloc

tracemalloc.start()

# Code to measure
create_large_data()

current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current/1024:.1f} KB, Peak: {peak/1024:.1f} KB")
tracemalloc.stop()

# Top memory consumers
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
for stat in top_stats[:5]:
    print(stat)
```

## Line Profiler

```bash
pip install line-profiler

# Decorate function
@profile
def slow_function():
    ...

kernprof -l -v script.py
```

## Lab Exercise
1. Use `cProfile` to find the bottleneck in a slow data processing script
2. Profile memory usage of loading a 100MB CSV with pandas vs a generator
3. Set a conditional breakpoint in `pdb` that triggers only when `x > 100`
""")

write("_02_14_testing_with_pytest.md", fm(
    "02_14_02","Testing with Pytest",14,"Debugging and Testing",2,"intermediate",
    ["pytest","assert","fixture","parametrize","mock","monkeypatch","conftest","coverage","TDD","hypothesis"]
) + """
## Pytest Basics

```python
# test_calculator.py
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3

def test_add_negative():
    assert add(-1, -2) == -3

def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)
```

```bash
pytest                    # run all tests
pytest test_calculator.py # specific file
pytest -v                 # verbose
pytest -k "add"           # run tests matching pattern
pytest --tb=short         # shorter traceback
pytest -x                 # stop on first failure
```

## Fixtures

```python
import pytest

@pytest.fixture
def sample_user():
    return {"id": 1, "name": "Raja", "email": "raja@test.com"}

@pytest.fixture
def db_connection():
    conn = create_test_db()
    yield conn          # test runs here
    conn.close()        # teardown

def test_user_name(sample_user):
    assert sample_user["name"] == "Raja"

def test_user_in_db(db_connection, sample_user):
    db_connection.insert(sample_user)
    result = db_connection.find(1)
    assert result["email"] == sample_user["email"]
```

## Parametrize

```python
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (100, -50, 50),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
```

## Mocking

```python
from unittest.mock import Mock, patch, MagicMock

def test_send_email(monkeypatch):
    called_with = []

    def fake_send(to, subject, body):
        called_with.append((to, subject, body))
        return True

    monkeypatch.setattr("myapp.email.send", fake_send)
    result = register_user("user@test.com")

    assert result.success
    assert len(called_with) == 1
    assert called_with[0][0] == "user@test.com"

# patch as decorator
@patch("requests.get")
def test_api_call(mock_get):
    mock_get.return_value.json.return_value = {"data": [1, 2, 3]}
    result = my_api_client.fetch()
    assert result == [1, 2, 3]
    mock_get.assert_called_once_with("https://api.example.com/data")
```

## Coverage

```bash
pip install pytest-cov

pytest --cov=myapp --cov-report=html tests/
# Opens htmlcov/index.html with per-line coverage
```

## Property-Based Testing with Hypothesis

```python
from hypothesis import given, strategies as st

@given(st.integers(), st.integers())
def test_add_commutative(a, b):
    assert add(a, b) == add(b, a)   # tests 100 random pairs

@given(st.lists(st.integers(), min_size=1))
def test_max_in_list(lst):
    result = max(lst)
    assert result in lst
    assert all(result >= x for x in lst)
```

## Lab Exercise
1. Write unit tests for a `BankAccount` class with 100% coverage
2. Use `pytest.fixture` with database setup/teardown and test CRUD operations
3. Write property-based tests for a `sort()` function using Hypothesis
""")

print()
print("=" * 60)
print("PHASE 3: PYTHON CONTENT GENERATION COMPLETE")
print(f"  Total lessons written: {written}")
print("=" * 60)

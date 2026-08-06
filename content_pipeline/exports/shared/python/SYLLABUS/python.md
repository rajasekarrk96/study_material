# Python Programming — Master Syllabus

**Target Role:** Python Developer (Beginner to Advanced)  
**Difficulty Level:** Progressive — Beginner through Advanced  
**Estimated Duration:** 100 Hours  
**Prerequisites:** None for Part 1. Python Core for Part 2.

---

## Part 1 — Core Python

---

### Module 01 — Setup and Overview

1. **Python Overview and Philosophy**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is Python?
    2. Python's Design Philosophy (Zen of Python)
    3. Python Versions
    4. Where Python is Used
    5. Python Interpreter Types (CPython, PyPy, MicroPython)
    6. Lab Exercise

2. **Environment Setup and Tooling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Installing Python
    2. Virtual Environments (`venv`)
    3. Package Management with `pip`
    4. Modern Tooling — `uv` (recommended 2024+)
    5. `pyproject.toml`
    6. Code Quality Tools (ruff, black, mypy)
    7. REPL and Interactive Tools
    8. Lab Exercise

3. **CPython Architecture and Execution Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. How Python Code Executes
    2. Inspecting Bytecode (`dis` module)
    3. The GIL (Global Interpreter Lock)
    4. Memory Management
        - Reference Counting
        - Garbage Collector (for cycles)
        - Object Interning
    5. `__pycache__` and `.pyc` Files
    6. Lab Exercise

---

### Module 02 — Control Flow

1. **Comprehensive Operator Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Arithmetic Operators
    2. Comparison Operators
    3. Logical Operators (Short-Circuit)
    4. Bitwise Operators
    5. Identity and Membership (`is`, `in`)
    6. Walrus Operator `:=` (Python 3.8+)
    7. Operator Precedence
    8. Lab Exercise

2. **Conditional Execution**
    - **Course Coverage:** 🟢 Covered in Class
    1. `if` / `elif` / `else`
    2. Ternary (Conditional Expression)
    3. Truthy and Falsy Values
    4. Structural Pattern Matching — `match/case` (3.10+)
    5. Lab Exercise

3. **Iteration and Loop Structures**
    - **Course Coverage:** 🟢 Covered in Class
    1. `for` Loops
    2. `while` Loops
    3. `break`, `continue`, `else`
    4. Advanced Iteration Patterns (`enumerate`, `zip`, `reversed`)
    5. Lab Exercise

---

### Module 03 — Variables and Types

1. **Variables and Dynamic Typing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Variables in Python
    2. Dynamic vs Static Typing
    3. Type Annotations (Optional Static Hints)
    4. Duck Typing
    5. Identity vs Equality (`is` vs `==`)
    6. Lab Exercise

2. **Built-in Primitive Data Types**
    - **Course Coverage:** 🟢 Covered in Class
    1. Numeric Types (`int`, `float`, `complex`, `Decimal`)
    2. Strings
    3. `NoneType`
    4. Type Conversion
    5. `isinstance` and `type`
    6. Lab Exercise

3. **Syntax Rules and Code Style**
    - **Course Coverage:** 🟢 Covered in Class
    1. Indentation (Significant Whitespace)
    2. Statements and Line Continuation
    3. Comments and Docstrings
    4. PEP 8 Style Guide
    5. Naming Conventions
    6. Lab Exercise

---

### Module 04 — Collections

1. **Lists and Sequence Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Creating and Modifying Lists
    2. Sorting (`sort`, `sorted`, `key`)
    3. List Comprehensions
    4. Copying Lists (shallow vs deep)
    5. Lab Exercise

2. **Tuples and Immutable Sequences**
    - **Course Coverage:** 🟢 Covered in Class
    1. Tuples and Immutability
    2. Why Use Tuples?
    3. Named Tuples and `typing.NamedTuple`
    4. Tuple vs List Decision
    5. Lab Exercise

3. **Dictionaries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Dictionary Fundamentals
    2. CRUD Operations
    3. Iterating Dictionaries
    4. Dictionary Comprehensions
    5. Advanced Dict Types (`defaultdict`, `OrderedDict`, `ChainMap`)
    6. Merging Dicts (3.9+ `|` operator)
    7. Lab Exercise

4. **Sets and Frozensets**
    - **Course Coverage:** 🟢 Covered in Class
    1. Sets
    2. Set Operations (union, intersection, difference)
    3. Modifying Sets
    4. Set Comprehensions
    5. `frozenset` (Immutable Set)
    6. Practical Use Cases
    7. Lab Exercise

5. **Strings and Text Processing**
    - **Course Coverage:** 🟢 Covered in Class
    1. String Fundamentals and Immutability
    2. String Formatting (`f-strings`, `.format()`)
    3. Essential String Methods
    4. Multi-line and Raw Strings
    5. String Encoding (UTF-8, ASCII)
    6. `textwrap` for Formatting
    7. Lab Exercise

6. **Advanced Collections Module**
    - **Course Coverage:** 🟢 Covered in Class
    1. `collections.Counter`
    2. `collections.deque` (Double-Ended Queue)
    3. `heapq` — Priority Queue
    4. `UserDict` and `UserList`
    5. Lab Exercise

---

### Module 05 — Functions and Comprehensions

1. **Functions and Arguments**
    - **Course Coverage:** 🟢 Covered in Class
    1. Defining Functions (`def`)
    2. Parameter Types: positional, keyword, default
    3. `*args` and `**kwargs`
    4. Default Argument Gotcha (mutable defaults)
    5. Return Values
    6. Higher-Order Functions
    7. Lab Exercise

2. **Functional Programming in Python**
    - **Course Coverage:** 🟢 Covered in Class
    1. Lambda Functions
    2. `map`, `filter`, `reduce`
    3. `functools.partial`
    4. `functools.lru_cache` (Memoization)
    5. `operator` module
    6. Immutability and Pure Functions
    7. Lab Exercise

3. **List, Dict, Set Comprehensions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Comprehension Syntax
    2. List Comprehensions
    3. Dict Comprehensions
    4. Set Comprehensions
    5. Generator Expressions
    6. Performance and Readability
    7. When NOT to Use Comprehensions
    8. Lab Exercise

---

### Module 06 — Closures, Decorators & Generators

1. **Closures and Decorators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Closures
    2. The `nonlocal` Keyword
    3. Decorators (`@decorator` syntax)
    4. Parametrized Decorators
    5. Stacked Decorators
    6. Practical Decorators (`@timer`, `@retry`, `@cache`)
    7. Class-Based Decorators
    8. Lab Exercise

2. **Generators and Iterators**
    - **Course Coverage:** 🟢 Covered in Class
    1. The Iterator Protocol (`__iter__`, `__next__`)
    2. Generator Functions (`yield`)
    3. Generator Expressions
    4. `yield` with `send()` and `throw()`
    5. `itertools` — Powerful Combinators
    6. Memory Comparison: List vs Generator
    7. Lab Exercise

---

### Module 07 — Object-Oriented Programming

1. **Classes and Instance Mechanics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Defining a Class
    2. `__init__`, instance attributes, class attributes
    3. Properties (`@property`)
    4. `__slots__` — Memory Optimization
    5. Lab Exercise

2. **Inheritance and Polymorphism**
    - **Course Coverage:** 🟢 Covered in Class
    1. Single Inheritance
    2. `super()` and `__init__`
    3. Abstract Base Classes
    4. Method Resolution Order (MRO)
    5. Mixins
    6. Lab Exercise

3. **Magic Dunder Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Essential Dunder Methods (`__str__`, `__repr__`, `__eq__`, `__hash__`)
    2. Container Protocol (`__len__`, `__getitem__`, `__contains__`)
    3. Context Manager Protocol (`__enter__`, `__exit__`)
    4. Callable Objects `__call__`
    5. Lab Exercise

4. **Dataclasses and Protocols**
    - **Course Coverage:** 🟢 Covered in Class
    1. `@dataclass` decorator
    2. Advanced `dataclass` Options (`field`, `frozen`, `post_init`)
    3. `TypedDict`
    4. `Protocol` (Structural Subtyping)
    5. `attrs` Library
    6. Lab Exercise

---

### Module 08 — Exceptions and Context Managers

1. **Exception Handling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Exception Hierarchy
    2. `try` / `except` / `else` / `finally`
    3. Exception Information (`traceback`)
    4. Raising Exceptions
    5. Custom Exceptions
    6. `contextlib.suppress`
    7. `ExceptionGroup` (Python 3.11+)
    8. Lab Exercise

2. **Context Managers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Context Manager Protocol (`__enter__`, `__exit__`)
    2. `contextlib.contextmanager`
    3. Practical Examples (file, lock, timer)
    4. `contextlib.ExitStack`
    5. Async Context Managers
    6. Lab Exercise

3. **Logging Module**
    - **Course Coverage:** 🟢 Covered in Class
    1. Python Logging Overview
    2. Log Levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`)
    3. Production Logger Setup (handlers, formatters)
    4. Logging Exceptions
    5. Structured Logging with `structlog`
    6. Lab Exercise

---

### Module 09 — File I/O and Serialization

1. **File I/O and Paths**
    - **Course Coverage:** 🟢 Covered in Class
    1. File Operations (open, read, write, close)
    2. File Modes (`r`, `w`, `a`, `rb`, `wb`)
    3. `pathlib` — Modern Path Handling
    4. CSV and JSON Files
    5. Lab Exercise

2. **Data Serialization**
    - **Course Coverage:** 🟢 Covered in Class
    1. JSON (`json` module)
    2. `pickle` — Python Object Serialization
    3. YAML (requires `PyYAML`)
    4. TOML (Python 3.11+ built-in)
    5. Pydantic Serialization
    6. `orjson` — Fast JSON
    7. Lab Exercise

---

### Module 10 — Regular Expressions

1. **Regular Expressions**
    - **Course Coverage:** 🟢 Covered in Class
    1. `re` Module Basics
    2. Regex Syntax Reference (character classes, quantifiers, anchors)
    3. Groups and Named Groups
    4. `sub` and `subn`
    5. Compiled Patterns
    6. Lookahead and Lookbehind
    7. Lab Exercise

---

### Module 11 — Modules and Packages

1. **Modules and Packages**
    - **Course Coverage:** 🟢 Covered in Class
    1. Importing Modules
    2. Module Attributes (`__name__`, `__file__`, `__all__`)
    3. Package Structure (`__init__.py`)
    4. Relative Imports
    5. `sys.path` and Import Resolution
    6. `importlib` — Dynamic Imports
    7. Lab Exercise

---

### Module 12 — Concurrency

1. **Asyncio and Async/Await**
    - **Course Coverage:** 🟢 Covered in Class
    1. Async/Await Fundamentals
    2. Tasks — Fire and Forget
    3. Async HTTP with `aiohttp`
    4. `asyncio` Primitives (Lock, Semaphore, Queue)
    5. Async Context Managers and Generators
    6. Lab Exercise

2. **Threading and Multiprocessing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Threading (`threading.Thread`)
    2. Thread Synchronization (`Lock`, `RLock`, `Event`)
    3. `concurrent.futures` — High-Level Interface
    4. `multiprocessing` — True Parallelism
    5. When to Use What
    6. Lab Exercise

---

### Module 13 — Scientific Python

1. **NumPy Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. NumPy Arrays (`ndarray`)
    2. Indexing and Slicing
    3. Vectorized Operations (No Loops!)
    4. Broadcasting
    5. Matrix Operations
    6. Lab Exercise

2. **Pandas Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. `Series` and `DataFrame`
    2. Selection and Filtering
    3. Essential Operations (groupby, merge, join)
    4. Handling Missing Data
    5. Lab Exercise

3. **Matplotlib and Visualization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Matplotlib Basics
    2. Common Plot Types (line, bar, scatter, histogram)
    3. Subplots and Layouts
    4. Seaborn — Statistical Plots
    5. Lab Exercise

4. **Hardware Interfacing with Python**
    - **Course Coverage:** 🟢 Covered in Class
    1. Raspberry Pi GPIO
    2. `gpiozero` — Higher Level API
    3. `PySerial` — UART Communication
    4. `smbus2` — I2C Communication
    5. MicroPython
    6. Lab Exercise

---

### Module 14 — Debugging and Testing

1. **Debugging and Profiling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Python Debugger (`pdb`) — commands and usage
    2. Profiling with `cProfile`
    3. `timeit` — Micro-Benchmarking
    4. Memory Profiling (`tracemalloc`, `memory_profiler`)
    5. Line Profiler (`line_profiler`)
    6. Lab Exercise

2. **Testing with Pytest**
    - **Course Coverage:** 🟢 Covered in Class
    1. Pytest Basics
    2. Fixtures
    3. Parametrize (`@pytest.mark.parametrize`)
    4. Mocking (`unittest.mock`)
    5. Coverage (`pytest-cov`)
    6. Property-Based Testing with `Hypothesis`
    7. Lab Exercise

---

## Part 2 — Advanced Python & Professional Practices

---

### Module 15 — Python Internals

1. **Python Object Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Everything Is an Object
    2. Identity, Type, Value
    3. Object Lifecycle
    4. Lab Exercise

2. **Memory Management and GC**
    - **Course Coverage:** 🟢 Covered in Class
    1. Reference Counting
    2. Cyclic Garbage Collector
    3. `gc` Module
    4. Memory Profiling
    5. Lab Exercise

3. **Python Bytecode**
    - **Course Coverage:** 🟢 Covered in Class
    1. Compilation to Bytecode
    2. `dis` Module Deep Dive
    3. CPython Evaluation Loop
    4. Lab Exercise

4. **Global Interpreter Lock (GIL)**
    - **Course Coverage:** 🟢 Covered in Class
    1. What the GIL Is
    2. Why It Exists
    3. GIL Impact on Multithreading
    4. Free-Threaded Python 3.13+
    5. Lab Exercise

5. **Python Data Model (Deep Dive)**
    - **Course Coverage:** 🟢 Covered in Class
    1. The Data Model Protocol System
    2. Special Methods Reference
    3. Customizing Attribute Access
    4. Lab Exercise

---

### Module 16 — Advanced OOP

1. **Python Data Model & Special Dunder Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Full Dunder Method Reference
    2. Numeric Protocol
    3. Comparison Protocol
    4. Lab Exercise

2. **Multiple Inheritance & Method Resolution Order (MRO)**
    - **Course Coverage:** 🟢 Covered in Class
    1. MRO Algorithm (C3 Linearization)
    2. `__mro__` Inspection
    3. Cooperative Multiple Inheritance
    4. Lab Exercise

3. **Abstract Base Classes (abc module)**
    - **Course Coverage:** 🟢 Covered in Class
    1. `ABC` and `ABCMeta`
    2. `@abstractmethod`
    3. Virtual Subclasses
    4. Lab Exercise

4. **Properties, Getters, and Setters**
    - **Course Coverage:** 🟢 Covered in Class
    1. `@property` decorator
    2. Computed Properties
    3. `@cached_property`
    4. Lab Exercise

5. **Dataclasses & Pydantic Data Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Advanced `@dataclass` Patterns
    2. Pydantic `BaseModel`
    3. Validators and Field Constraints
    4. Lab Exercise

---

### Module 17 — Functional Programming & Metaprogramming

1. **First-Class Functions, Closures, and Higher-Order Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Functions as First-Class Objects
    2. Closure Variable Binding
    3. Higher-Order Function Patterns
    4. Lab Exercise

2. **Function & Class Decorators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Function Decorators (review + advanced)
    2. Class Decorators
    3. Lab Exercise

3. **Decorators with Arguments & `@wraps`**
    - **Course Coverage:** 🟢 Covered in Class
    1. Parametrized Decorators
    2. `functools.wraps`
    3. Lab Exercise

4. **Generators, `yield`, and Generator Expressions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Generator Protocol Deep Dive
    2. `send()`, `throw()`, `close()`
    3. Chaining Generators
    4. Lab Exercise

5. **Iterators, Iterables & Custom Iterators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Iterator Protocol (`__iter__` + `__next__`)
    2. Custom Iterator Classes
    3. Lab Exercise

6. **itertools and functools**
    - **Course Coverage:** 🟢 Covered in Class
    1. `itertools` Combinators
    2. `functools` Utilities (`cache`, `reduce`, `partial`)
    3. Lab Exercise

---

### Module 18 — Memory, Context Managers & Metaprogramming

1. **Python Memory Management & Garbage Collection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Reference Counting Details
    2. Cyclic References
    3. `weakref` Module
    4. Lab Exercise

2. **Context Managers & the `with` Statement**
    - **Course Coverage:** 🟢 Covered in Class
    1. Context Manager Protocol (review + advanced)
    2. Reusable Context Managers
    3. Lab Exercise

3. **Creating Context Managers via `contextlib`**
    - **Course Coverage:** 🟢 Covered in Class
    1. `@contextmanager`
    2. `contextlib.asynccontextmanager`
    3. `ExitStack`
    4. Lab Exercise

4. **Weak References & Memory Optimization**
    - **Course Coverage:** 🟢 Covered in Class
    1. `weakref.ref` and `WeakValueDictionary`
    2. Memory-Efficient Caching
    3. Lab Exercise

5. **Python Metaclasses & Dynamic Code Execution**
    - **Course Coverage:** 🟢 Covered in Class
    1. What Are Metaclasses?
    2. `type` as Metaclass
    3. Custom Metaclasses
    4. `exec()` and `eval()` (controlled use)
    5. Lab Exercise

---

### Module 19 — Advanced Concurrency

1. **Threading vs Multiprocessing in Python**
    - **Course Coverage:** 🟢 Covered in Class
    1. When to Use Threading vs Multiprocessing
    2. I/O-Bound vs CPU-Bound Work
    3. Lab Exercise

2. **GIL Deep Dive**
    - **Course Coverage:** 🟢 Covered in Class
    1. GIL Release Mechanisms
    2. C Extensions and the GIL
    3. Free-Threaded Python 3.13+
    4. Lab Exercise

3. **ThreadPoolExecutor & ProcessPoolExecutor**
    - **Course Coverage:** 🟢 Covered in Class
    1. `concurrent.futures.ThreadPoolExecutor`
    2. `concurrent.futures.ProcessPoolExecutor`
    3. Futures and `as_completed`
    4. Lab Exercise

4. **Asyncio Event Loop & async/await Syntax**
    - **Course Coverage:** 🟢 Covered in Class
    1. Event Loop Internals
    2. `asyncio.create_task`
    3. `asyncio.gather` and `TaskGroup`
    4. Lab Exercise

5. **Gathering Tasks & Async I/O Performance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Task Groups (Python 3.11+)
    2. Async I/O Performance Patterns
    3. Backpressure and Rate Limiting
    4. Lab Exercise

---

### Module 20 — Tooling, Packaging & Design Patterns

1. **Unit Testing with Pytest and Fixtures**
    - **Course Coverage:** 🟢 Covered in Class
    1. Advanced Fixtures (scope, autouse)
    2. Factory Fixtures
    3. Lab Exercise

2. **Mocking Dependencies with `unittest.mock`**
    - **Course Coverage:** 🟢 Covered in Class
    1. `Mock`, `MagicMock`, `patch`
    2. `spec`, `side_effect`, `return_value`
    3. Lab Exercise

3. **Code Coverage, Linting — ruff, black, flake8**
    - **Course Coverage:** 🟢 Covered in Class
    1. `pytest-cov` and Coverage Reports
    2. `ruff` — Fast Linter and Formatter
    3. CI Integration
    4. Lab Exercise

4. **Type Hinting and Static Analysis with mypy**
    - **Course Coverage:** 🟢 Covered in Class
    1. Advanced Type Annotations
    2. `mypy` Configuration
    3. Generics and `TypeVar`
    4. Lab Exercise

5. **Building and Publishing Python Packages to PyPI**
    - **Course Coverage:** 🟢 Covered in Class
    1. `pyproject.toml` Full Reference
    2. Building with `build`
    3. Publishing with `twine`
    4. Versioning with `bumpver`
    5. Lab Exercise

6. **Creational Patterns — Singleton, Factory, Builder**
    - **Course Coverage:** 🟢 Covered in Class
    1. Singleton Pattern in Python
    2. Factory Method
    3. Builder Pattern
    4. Lab Exercise

7. **Structural Patterns — Adapter, Decorator, Facade**
    - **Course Coverage:** 🟢 Covered in Class
    1. Adapter Pattern
    2. Decorator Pattern (GoF vs Python)
    3. Facade Pattern
    4. Lab Exercise

8. **Behavioral Patterns — Observer, Strategy, State**
    - **Course Coverage:** 🟢 Covered in Class
    1. Observer Pattern
    2. Strategy Pattern
    3. State Pattern
    4. Lab Exercise

9. **Clean Architecture and Dependency Injection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Hexagonal Architecture in Python
    2. Dependency Injection Containers
    3. Lab Exercise

10. **Refactoring Legacy Python Codebases**
    - **Course Coverage:** 🟢 Covered in Class
    1. Identifying Code Smells
    2. Refactoring Techniques
    3. Incremental Modernization
    4. Lab Exercise

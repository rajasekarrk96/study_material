# Python -- Syllabus

> Source: `_source_modular_courses.md`



#### 4.1. Module 1 — Setup and Overview

1. **Python Overview and Philosophy**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is Python?
    2. Python's Design Philosophy
    3. Python Versions
    4. Where Python is Used
    5. Python Interpreter Types
    6. Lab Exercise
2. **Environment Setup and Tooling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Installing Python
    2. Virtual Environments
    3. Package Management with pip
    4. Modern Tooling — uv (recommended 2024+)
    5. pyproject.toml
    6. Code Quality Tools
    7. REPL and Interactive Tools
    8. Lab Exercise
3. **CPython Architecture and Execution Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. How Python Code Executes
    2. Inspecting Bytecode
    3. The GIL (Global Interpreter Lock)
    4. Memory Management
        - Reference Counting
        - Garbage Collector (for cycles)
        - Object Interning
    5. `__pycache__` and .pyc Files
    6. Lab Exercise

#### 4.2. Module 2 — Core Fundamentals & Control Flow

1. **Lesson 1.5 Structural Pattern Matching (match/case)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `match/case` vs Legacy `if-elif-else`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What makes structural pattern matching different from C/Java `switch` statements?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Existing Jupyter Notebooks

#### 4.3. Module 3 — Variables and Types

1. **Variables and Dynamic Typing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Variables in Python
    2. Dynamic vs Static Typing
    3. Type Annotations (Optional Static Hints)
    4. Duck Typing
    5. Identity vs Equality
    6. Lab Exercise
2. **Built-in Primitive Data Types**
    - **Course Coverage:** 🟢 Covered in Class
    1. Numeric Types
    2. Strings
    3. NoneType
    4. Type Conversion
    5. isinstance and type
    6. Lab Exercise
3. **Syntax Rules and Code Style**
    - **Course Coverage:** 🟢 Covered in Class
    1. Python Syntax Fundamentals
        - Indentation (Significant Whitespace)
        - Statements and Line Continuation
        - Comments
        - Docstrings
    2. PEP 8 Style Guide
    3. Naming Conventions Summary
    4. Lab Exercise

#### 4.4. Module 4 — Control Flow

1. **Comprehensive Operator Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Python Operators Reference
        - Arithmetic Operators
        - Comparison Operators
        - Logical Operators (Short-Circuit)
        - Bitwise Operators
        - Identity and Membership
        - Walrus Operator `:=` (Python 3.8+)
        - Operator Precedence (high → low)
    2. Lab Exercise
2. **Conditional Execution**
    - **Course Coverage:** 🟢 Covered in Class
    1. if / elif / else
    2. Ternary (Conditional Expression)
    3. Truthy and Falsy Values
    4. Structural Pattern Matching — match/case (3.10+)
        - Matching Sequences and Structures
        - Matching Data Classes
    5. Lab Exercise
3. **Iteration and Loop Structures**
    - **Course Coverage:** 🟢 Covered in Class
    1. for Loops
    2. while Loops
    3. break, continue, else
    4. Advanced Iteration Patterns
    5. Lab Exercise

#### 4.5. Module 5 — Collections

1. **Lists and Sequence Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Lists
    2. Modifying Lists
    3. Sorting
    4. List Comprehensions
    5. Copying Lists
    6. Lab Exercise
2. **Tuples and Immutable Sequences**
    - **Course Coverage:** 🟢 Covered in Class
    1. Tuples
    2. Why Tuples?
    3. Named Tuples
    4. typing.NamedTuple (Modern)
    5. Tuple vs List Decision
    6. Lab Exercise
3. **Dictionaries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Dictionaries
    2. CRUD Operations
    3. Iterating Dictionaries
    4. Dictionary Comprehensions
    5. Advanced Dict Types
    6. Merging Dicts (3.9+)
    7. Lab Exercise
4. **Sets and Frozensets**
    - **Course Coverage:** 🟢 Covered in Class
    1. Sets
    2. Set Operations
    3. Modifying Sets
    4. Set Comprehensions
    5. Frozenset (Immutable Set)
    6. Practical Use Cases
    7. Lab Exercise
5. **Strings and Text Processing**
    - **Course Coverage:** 🟢 Covered in Class
    1. String Fundamentals
    2. String Formatting
    3. Essential String Methods
    4. Multi-line and Raw Strings
    5. String Encoding
    6. textwrap for Formatting
    7. Lab Exercise
6. **Advanced Collections Module**
    - **Course Coverage:** 🟢 Covered in Class
    1. collections.Counter
    2. collections.deque (Double-Ended Queue)
    3. heapq — Priority Queue
    4. UserDict and UserList
    5. Lab Exercise

#### 4.6. Module 6 — Async Concurrency & Type Hinting

1. **Lesson 5.1 Static Type Hinting & Mypy Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Gradual Typing in Python
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Do Python type hints affect runtime execution speed?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Existing Jupyter Notebooks
2. **Lesson 5.2 Asyncio Event Loop & async/await**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Synchronous vs Asynchronous Execution
        - Python 3.11+ `TaskGroup` Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Is Asyncio multi-threaded?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Existing Jupyter Notebooks
3. **Lesson 5.3 Modern Python Packaging (pyproject.toml & uv)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Legacy `setup.py` vs Modern `pyproject.toml`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Modern `pyproject.toml` Manifest Specification
        - High-Speed `uv` CLI Commands
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is `pyproject.toml` and why is it preferred over `requirements.txt`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Existing Jupyter Notebooks

#### 4.7. Module 7 — Functions

1. **Functions and Arguments**
    - **Course Coverage:** 🟢 Covered in Class
    1. Defining Functions
    2. Parameter Types
    3. *args and **kwargs
    4. Default Argument Gotcha
    5. Return Values
    6. Higher-Order Functions
    7. Lab Exercise
2. **Functional Programming in Python**
    - **Course Coverage:** 🟢 Covered in Class
    1. Lambda Functions
    2. map, filter, reduce
    3. functools.partial
    4. functools.lru_cache (Memoization)
    5. operator module
    6. Immutability and Pure Functions
    7. Lab Exercise
3. **List Dict Set Comprehensions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Comprehension Syntax
    2. List Comprehensions
    3. Dict Comprehensions
    4. Set Comprehensions
    5. Generator Expressions
    6. Performance and Readability
    7. When NOT to Use Comprehensions
    8. Lab Exercise

#### 4.8. Module 8 — Advanced Python

1. **Closures and Decorators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Closures
    2. The `nonlocal` Keyword
    3. Decorators
    4. Parametrized Decorators
    5. Stacked Decorators
    6. Practical Decorators
    7. Class-Based Decorators
    8. Lab Exercise
2. **Generators and Iterators**
    - **Course Coverage:** 🟢 Covered in Class
    1. The Iterator Protocol
    2. Generator Functions
    3. Generator Expressions
    4. yield with send() and throw()
    5. itertools — Powerful Combinators
    6. Memory Comparison
    7. Lab Exercise

#### 4.9. Module 9 — Object-Oriented Programming

1. **Classes and Instance Mechanics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Defining a Class
    2. Properties
    3. `__slots__` — Memory Optimization
    4. Lab Exercise
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
    1. Essential Dunder Methods
    2. Container Protocol
    3. Context Manager Protocol
    4. Callable Objects `__call__`
    5. Lab Exercise
4. **Dataclasses and Protocols**
    - **Course Coverage:** 🟢 Covered in Class
    1. @dataclass
    2. Advanced dataclass Options
    3. TypedDict
    4. Protocol (Structural Subtyping)
    5. attrs Library
    6. Lab Exercise

#### 4.10. Module 10 — Exceptions and File I/O

1. **Exception Handling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Exception Hierarchy
    2. try / except / else / finally
    3. Exception Information
    4. Raising Exceptions
    5. Custom Exceptions
    6. contextlib.suppress
    7. ExceptionGroup (Python 3.11+)
    8. Lab Exercise
2. **Context Managers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Context Manager Protocol
    2. contextlib.contextmanager
    3. Practical Examples
    4. contextlib.ExitStack
    5. Async Context Managers
    6. Lab Exercise
3. **Logging Module**
    - **Course Coverage:** 🟢 Covered in Class
    1. Python Logging Overview
    2. Log Levels
    3. Production Logger Setup
    4. Logging Exceptions
    5. Structured Logging with structlog
    6. Lab Exercise

#### 4.11. Module 11 — File I/O and Serialisation

1. **File I/O and Paths**
    - **Course Coverage:** 🟢 Covered in Class
    1. File Operations
    2. File Modes
    3. pathlib — Modern Path Handling
    4. CSV and JSON Files
    5. Lab Exercise
2. **Data Serialization**
    - **Course Coverage:** 🟢 Covered in Class
    1. JSON
    2. pickle — Python Object Serialization
    3. YAML (requires PyYAML)
    4. TOML (Python 3.11+ built-in)
    5. Pydantic Serialization
    6. orjson — Fast JSON
    7. Lab Exercise

#### 4.12. Module 12 — Regular Expressions

1. **Regular Expressions**
    - **Course Coverage:** 🟢 Covered in Class
    1. re Module Basics
    2. Regex Syntax Reference
    3. Groups and Named Groups
    4. sub and subn
    5. Compiled Patterns
    6. Lookahead and Lookbehind
    7. Lab Exercise

#### 4.13. Module 13 — s and Packages

1. **Modules and Packages**
    - **Course Coverage:** 🟢 Covered in Class
    1. Importing Modules
    2. Module Attributes
    3. Package Structure
    4. Relative Imports
    5. sys.path and Import Resolution
    6. importlib — Dynamic Imports
    7. Lab Exercise

#### 4.14. Module 14 — Concurrency

1. **Asyncio and Async/Await**
    - **Course Coverage:** 🟢 Covered in Class
    1. Async/Await Fundamentals
    2. Tasks — Fire and Forget
    3. Async HTTP with aiohttp
    4. asyncio Primitives
    5. Async Context Managers and Generators
    6. Lab Exercise
2. **Threading and Multiprocessing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Threading
    2. Thread Synchronization
    3. concurrent.futures — High-Level Interface
    4. multiprocessing — True Parallelism
    5. When to Use What
    6. Lab Exercise

#### 4.15. Module 15 — Scientific Python

1. **NumPy Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. NumPy Basics
    2. Indexing and Slicing
    3. Vectorized Operations (No Loops!)
    4. Broadcasting
    5. Matrix Operations
    6. Lab Exercise
2. **Pandas Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Pandas Basics
    2. Selection and Filtering
    3. Essential Operations
    4. GroupBy
    5. Merge and Join
    6. Lab Exercise
3. **Matplotlib and Visualization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Matplotlib Basics
    2. Common Plot Types
    3. Subplots
    4. Seaborn — Statistical Plots
    5. Lab Exercise
4. **Hardware Interfacing with Python**
    - **Course Coverage:** 🟢 Covered in Class
    1. Raspberry Pi GPIO
    2. gpiozero — Higher Level
    3. PySerial — UART Communication
    4. smbus2 — I2C Communication
    5. MicroPython
    6. Lab Exercise

#### 4.16. Module 16 — Debugging and Testing

1. **Debugging and Profiling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Python Debugger (pdb)
        - pdb Commands
    2. Profiling with cProfile
    3. timeit — Micro-Benchmarking
    4. Memory Profiling
    5. Line Profiler
    6. Lab Exercise
2. **Testing with Pytest**
    - **Course Coverage:** 🟢 Covered in Class
    1. Pytest Basics
    2. Fixtures
    3. Parametrize
    4. Mocking
    5. Coverage
    6. Property-Based Testing with Hypothesis
    7. Lab Exercise

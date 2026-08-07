# AI Engineering & Applied Machine Learning — Master Syllabus

**Target Role:** AI Engineer / LLM Application Developer / ML Engineer  
**Difficulty Level:** Advanced  
**Estimated Duration:** 250 Hours  
**Prerequisites:** engineering-math, core-python, python-dsa  
**Required Courses:** engineering-math, core-python  
**Optional Courses:** mlops-engineering, nlp-generative-ai  

---

## Study Flow

### 1. Python

#### 1.1. Module 1 — Setup and Overview

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

#### 1.2. Module 2 — Core Fundamentals & Control Flow

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

#### 1.3. Module 3 — Variables and Types

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

#### 1.4. Module 4 — Control Flow

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

#### 1.5. Module 5 — Collections

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

#### 1.6. Module 6 — Async Concurrency & Type Hinting

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

#### 1.7. Module 7 — Functions

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

#### 1.8. Module 8 — Advanced Python

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

#### 1.9. Module 9 — Object-Oriented Programming

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

#### 1.10. Module 10 — Exceptions and File I/O

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

#### 1.11. Module 11 — File I/O and Serialisation

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

#### 1.12. Module 12 — Regular Expressions

1. **Regular Expressions**
    - **Course Coverage:** 🟢 Covered in Class
    1. re Module Basics
    2. Regex Syntax Reference
    3. Groups and Named Groups
    4. sub and subn
    5. Compiled Patterns
    6. Lookahead and Lookbehind
    7. Lab Exercise

#### 1.13. Module 13 — s and Packages

1. **Modules and Packages**
    - **Course Coverage:** 🟢 Covered in Class
    1. Importing Modules
    2. Module Attributes
    3. Package Structure
    4. Relative Imports
    5. sys.path and Import Resolution
    6. importlib — Dynamic Imports
    7. Lab Exercise

#### 1.14. Module 14 — Concurrency

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

#### 1.15. Module 15 — Scientific Python

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

#### 1.16. Module 16 — Debugging and Testing

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

### 2. Advanced Python & Professional Practices

#### 2.1. Module 1 — Python Internals

1. **Python Object Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Memory Management and GC**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Python Bytecode**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Global Interpreter Lock**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Python Data Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.2. Module 2 — Advanced Object-Oriented Python

1. **Python Data Model & Special Dunder Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Python Data Model & Special Dunder Methods
    2. Core Concept
        - Core Concept: Python Data Model & Special Dunder Methods
    3. Syntax
        - Syntax: Python Data Model & Special Dunder Methods
    4. Example
        - Example: Python Data Model & Special Dunder Methods
    5. Pitfall
        - Pitfall: Python Data Model & Special Dunder Methods
    6. Q & A
        - Q & A: Python Data Model & Special Dunder Methods
2. **Multiple Inheritance & Method Resolution Order (MRO)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Multiple Inheritance & Method Resolution Order (MRO)
    2. Core Concept
        - Core Concept: Multiple Inheritance & Method Resolution Order (MRO)
    3. Syntax
        - Syntax: Multiple Inheritance & Method Resolution Order (MRO)
    4. Example
        - Example: Multiple Inheritance & Method Resolution Order (MRO)
    5. Pitfall
        - Pitfall: Multiple Inheritance & Method Resolution Order (MRO)
    6. Q & A
        - Q & A: Multiple Inheritance & Method Resolution Order (MRO)
3. **Abstract Base Classes (abc module)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Abstract Base Classes (abc module)
    2. Core Concept
        - Core Concept: Abstract Base Classes (abc module)
    3. Syntax
        - Syntax: Abstract Base Classes (abc module)
    4. Example
        - Example: Abstract Base Classes (abc module)
    5. Pitfall
        - Pitfall: Abstract Base Classes (abc module)
    6. Q & A
        - Q & A: Abstract Base Classes (abc module)
4. **Properties, Getters, and Setters**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Properties, Getters, and Setters
    2. Core Concept
        - Core Concept: Properties, Getters, and Setters
    3. Syntax
        - Syntax: Properties, Getters, and Setters
    4. Example
        - Example: Properties, Getters, and Setters
    5. Pitfall
        - Pitfall: Properties, Getters, and Setters
    6. Q & A
        - Q & A: Properties, Getters, and Setters
5. **Dataclasses & Pydantic Data Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Dataclasses & Pydantic Data Validation
    2. Core Concept
        - Core Concept: Dataclasses & Pydantic Data Validation
    3. Syntax
        - Syntax: Dataclasses & Pydantic Data Validation
    4. Example
        - Example: Dataclasses & Pydantic Data Validation
    5. Pitfall
        - Pitfall: Dataclasses & Pydantic Data Validation
    6. Q & A
        - Q & A: Dataclasses & Pydantic Data Validation

#### 2.3. Module 3 — Functional Programming & Metaprogramming

1. **First-Class Functions, Closures, and Higher-Order Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: First-Class Functions, Closures, and Higher-Order Functions
    2. Core Concept
        - Core Concept: First-Class Functions, Closures, and Higher-Order Functions
    3. Syntax
        - Syntax: First-Class Functions, Closures, and Higher-Order Functions
    4. Example
        - Example: First-Class Functions, Closures, and Higher-Order Functions
    5. Pitfall
        - Pitfall: First-Class Functions, Closures, and Higher-Order Functions
    6. Q & A
        - Q & A: First-Class Functions, Closures, and Higher-Order Functions
2. **Function & Class Decorators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Function & Class Decorators
    2. Core Concept
        - Core Concept: Function & Class Decorators
    3. Syntax
        - Syntax: Function & Class Decorators
    4. Example
        - Example: Function & Class Decorators
    5. Pitfall
        - Pitfall: Function & Class Decorators
    6. Q & A
        - Q & A: Function & Class Decorators
3. **Decorators with Arguments & Wraps**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Decorators with Arguments & Wraps
    2. Core Concept
        - Core Concept: Decorators with Arguments & Wraps
    3. Syntax
        - Syntax: Decorators with Arguments & Wraps
    4. Example
        - Example: Decorators with Arguments & Wraps
    5. Pitfall
        - Pitfall: Decorators with Arguments & Wraps
    6. Q & A
        - Q & A: Decorators with Arguments & Wraps
4. **Generators, Yield, and Generator Expressions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Generators, Yield, and Generator Expressions
    2. Core Concept
        - Core Concept: Generators, Yield, and Generator Expressions
    3. Syntax
        - Syntax: Generators, Yield, and Generator Expressions
    4. Example
        - Example: Generators, Yield, and Generator Expressions
    5. Pitfall
        - Pitfall: Generators, Yield, and Generator Expressions
    6. Q & A
        - Q & A: Generators, Yield, and Generator Expressions
5. **Iterators, Iterables, and Custom Iterators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Iterators, Iterables, and Custom Iterators
    2. Core Concept
        - Core Concept: Iterators, Iterables, and Custom Iterators
    3. Syntax
        - Syntax: Iterators, Iterables, and Custom Iterators
    4. Example
        - Example: Iterators, Iterables, and Custom Iterators
    5. Pitfall
        - Pitfall: Iterators, Iterables, and Custom Iterators
    6. Q & A
        - Q & A: Iterators, Iterables, and Custom Iterators

#### 2.4. Module 4 — Functional Programming

1. **First-Class Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Closures and Nonlocal**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Decorators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Generators and Yield**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Itertools and Functools**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.5. Module 5 — OOP Advanced

1. **Magic Methods Deep Dive**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Class Methods and Static Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Properties and Descriptors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Metaclasses**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Abstract Base Classes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.6. Module 6 — Memory Management & Context Managers

1. **Python Memory Management & Garbage Collection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Python Memory Management & Garbage Collection
    2. Core Concept
        - Core Concept: Python Memory Management & Garbage Collection
    3. Syntax
        - Syntax: Python Memory Management & Garbage Collection
    4. Example
        - Example: Python Memory Management & Garbage Collection
    5. Pitfall
        - Pitfall: Python Memory Management & Garbage Collection
    6. Q & A
        - Q & A: Python Memory Management & Garbage Collection
2. **Context Managers & the with Statement**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Context Managers & the with Statement
    2. Core Concept
        - Core Concept: Context Managers & the with Statement
    3. Syntax
        - Syntax: Context Managers & the with Statement
    4. Example
        - Example: Context Managers & the with Statement
    5. Pitfall
        - Pitfall: Context Managers & the with Statement
    6. Q & A
        - Q & A: Context Managers & the with Statement
3. **Creating Context Managers via contextlib**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Creating Context Managers via contextlib
    2. Core Concept
        - Core Concept: Creating Context Managers via contextlib
    3. Syntax
        - Syntax: Creating Context Managers via contextlib
    4. Example
        - Example: Creating Context Managers via contextlib
    5. Pitfall
        - Pitfall: Creating Context Managers via contextlib
    6. Q & A
        - Q & A: Creating Context Managers via contextlib
4. **Weak References & Memory Optimization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Weak References & Memory Optimization
    2. Core Concept
        - Core Concept: Weak References & Memory Optimization
    3. Syntax
        - Syntax: Weak References & Memory Optimization
    4. Example
        - Example: Weak References & Memory Optimization
    5. Pitfall
        - Pitfall: Weak References & Memory Optimization
    6. Q & A
        - Q & A: Weak References & Memory Optimization
5. **Python Metaclasses & Dynamic Code Execution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Python Metaclasses & Dynamic Code Execution
    2. Core Concept
        - Core Concept: Python Metaclasses & Dynamic Code Execution
    3. Syntax
        - Syntax: Python Metaclasses & Dynamic Code Execution
    4. Example
        - Example: Python Metaclasses & Dynamic Code Execution
    5. Pitfall
        - Pitfall: Python Metaclasses & Dynamic Code Execution
    6. Q & A
        - Q & A: Python Metaclasses & Dynamic Code Execution

#### 2.7. Module 7 — Concurrency & Async Programming

1. **Threading vs Multiprocessing in Python**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Threading vs Multiprocessing in Python
    2. Core Concept
        - Core Concept: Threading vs Multiprocessing in Python
    3. Syntax
        - Syntax: Threading vs Multiprocessing in Python
    4. Example
        - Example: Threading vs Multiprocessing in Python
    5. Pitfall
        - Pitfall: Threading vs Multiprocessing in Python
    6. Q & A
        - Q & A: Threading vs Multiprocessing in Python
2. **Global Interpreter Lock (GIL) Deep Dive**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Global Interpreter Lock (GIL) Deep Dive
    2. Core Concept
        - Core Concept: Global Interpreter Lock (GIL) Deep Dive
    3. Syntax
        - Syntax: Global Interpreter Lock (GIL) Deep Dive
    4. Example
        - Example: Global Interpreter Lock (GIL) Deep Dive
    5. Pitfall
        - Pitfall: Global Interpreter Lock (GIL) Deep Dive
    6. Q & A
        - Q & A: Global Interpreter Lock (GIL) Deep Dive
3. **ThreadPoolExecutor & ProcessPoolExecutor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: ThreadPoolExecutor & ProcessPoolExecutor
    2. Core Concept
        - Core Concept: ThreadPoolExecutor & ProcessPoolExecutor
    3. Syntax
        - Syntax: ThreadPoolExecutor & ProcessPoolExecutor
    4. Example
        - Example: ThreadPoolExecutor & ProcessPoolExecutor
    5. Pitfall
        - Pitfall: ThreadPoolExecutor & ProcessPoolExecutor
    6. Q & A
        - Q & A: ThreadPoolExecutor & ProcessPoolExecutor
4. **Asyncio Event Loop, Async/Await Syntax**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Asyncio Event Loop, Async/Await Syntax
    2. Core Concept
        - Core Concept: Asyncio Event Loop, Async/Await Syntax
    3. Syntax
        - Syntax: Asyncio Event Loop, Async/Await Syntax
    4. Example
        - Example: Asyncio Event Loop, Async/Await Syntax
    5. Pitfall
        - Pitfall: Asyncio Event Loop, Async/Await Syntax
    6. Q & A
        - Q & A: Asyncio Event Loop, Async/Await Syntax
5. **Gathering Tasks & Asynchronous I/O Performance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Gathering Tasks & Asynchronous I/O Performance
    2. Core Concept
        - Core Concept: Gathering Tasks & Asynchronous I/O Performance
    3. Syntax
        - Syntax: Gathering Tasks & Asynchronous I/O Performance
    4. Example
        - Example: Gathering Tasks & Asynchronous I/O Performance
    5. Pitfall
        - Pitfall: Gathering Tasks & Asynchronous I/O Performance
    6. Q & A
        - Q & A: Gathering Tasks & Asynchronous I/O Performance

#### 2.8. Module 8 — Concurrency

1. **Threading**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Multiprocessing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Asyncio**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Concurrent Futures**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Asyncio Advanced Patterns**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.9. Module 9 — Python Packaging and Tools

1. **Virtual Environments**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Writing Python Packages**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Publishing to PyPI**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Type Hints and Mypy**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Testing with Pytest**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.10. Module 10 — Packaging & Testing Frameworks

1. **Unit Testing with Pytest & Fixtures**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Unit Testing with Pytest & Fixtures
    2. Core Concept
        - Core Concept: Unit Testing with Pytest & Fixtures
    3. Syntax
        - Syntax: Unit Testing with Pytest & Fixtures
    4. Example
        - Example: Unit Testing with Pytest & Fixtures
    5. Pitfall
        - Pitfall: Unit Testing with Pytest & Fixtures
    6. Q & A
        - Q & A: Unit Testing with Pytest & Fixtures
2. **Mocking Dependencies with unittest.mock**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Mocking Dependencies with unittest.mock
    2. Core Concept
        - Core Concept: Mocking Dependencies with unittest.mock
    3. Syntax
        - Syntax: Mocking Dependencies with unittest.mock
    4. Example
        - Example: Mocking Dependencies with unittest.mock
    5. Pitfall
        - Pitfall: Mocking Dependencies with unittest.mock
    6. Q & A
        - Q & A: Mocking Dependencies with unittest.mock
3. **Code Coverage Analysis & Linting (Ruff, Black, Flake8)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Code Coverage Analysis & Linting (Ruff, Black, Flake8)
    2. Core Concept
        - Core Concept: Code Coverage Analysis & Linting (Ruff, Black, Flake8)
    3. Syntax
        - Syntax: Code Coverage Analysis & Linting (Ruff, Black, Flake8)
    4. Example
        - Example: Code Coverage Analysis & Linting (Ruff, Black, Flake8)
    5. Pitfall
        - Pitfall: Code Coverage Analysis & Linting (Ruff, Black, Flake8)
    6. Q & A
        - Q & A: Code Coverage Analysis & Linting (Ruff, Black, Flake8)
4. **Type Hinting & Static Analysis with Mypy**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Type Hinting & Static Analysis with Mypy
    2. Core Concept
        - Core Concept: Type Hinting & Static Analysis with Mypy
    3. Syntax
        - Syntax: Type Hinting & Static Analysis with Mypy
    4. Example
        - Example: Type Hinting & Static Analysis with Mypy
    5. Pitfall
        - Pitfall: Type Hinting & Static Analysis with Mypy
    6. Q & A
        - Q & A: Type Hinting & Static Analysis with Mypy
5. **Building & Publishing Python Packages to PyPI**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Building & Publishing Python Packages to PyPI
    2. Core Concept
        - Core Concept: Building & Publishing Python Packages to PyPI
    3. Syntax
        - Syntax: Building & Publishing Python Packages to PyPI
    4. Example
        - Example: Building & Publishing Python Packages to PyPI
    5. Pitfall
        - Pitfall: Building & Publishing Python Packages to PyPI
    6. Q & A
        - Q & A: Building & Publishing Python Packages to PyPI

#### 2.11. Module 11 — Advanced Patterns

1. **Context Managers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Design Patterns in Python**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Data Classes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Protocol and Structural Subtyping**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Python Performance Optimization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.12. Module 12 — Design Patterns in Python

1. **Creational Patterns (Singleton, Factory, Builder)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Creational Patterns (Singleton, Factory, Builder)
    2. Core Concept
        - Core Concept: Creational Patterns (Singleton, Factory, Builder)
    3. Syntax
        - Syntax: Creational Patterns (Singleton, Factory, Builder)
    4. Example
        - Example: Creational Patterns (Singleton, Factory, Builder)
    5. Pitfall
        - Pitfall: Creational Patterns (Singleton, Factory, Builder)
    6. Q & A
        - Q & A: Creational Patterns (Singleton, Factory, Builder)
2. **Structural Patterns (Adapter, Decorator, Facade)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Structural Patterns (Adapter, Decorator, Facade)
    2. Core Concept
        - Core Concept: Structural Patterns (Adapter, Decorator, Facade)
    3. Syntax
        - Syntax: Structural Patterns (Adapter, Decorator, Facade)
    4. Example
        - Example: Structural Patterns (Adapter, Decorator, Facade)
    5. Pitfall
        - Pitfall: Structural Patterns (Adapter, Decorator, Facade)
    6. Q & A
        - Q & A: Structural Patterns (Adapter, Decorator, Facade)
3. **Behavioral Patterns (Observer, Strategy, State)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Behavioral Patterns (Observer, Strategy, State)
    2. Core Concept
        - Core Concept: Behavioral Patterns (Observer, Strategy, State)
    3. Syntax
        - Syntax: Behavioral Patterns (Observer, Strategy, State)
    4. Example
        - Example: Behavioral Patterns (Observer, Strategy, State)
    5. Pitfall
        - Pitfall: Behavioral Patterns (Observer, Strategy, State)
    6. Q & A
        - Q & A: Behavioral Patterns (Observer, Strategy, State)
4. **Clean Architecture & Dependency Injection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Clean Architecture & Dependency Injection
    2. Core Concept
        - Core Concept: Clean Architecture & Dependency Injection
    3. Syntax
        - Syntax: Clean Architecture & Dependency Injection
    4. Example
        - Example: Clean Architecture & Dependency Injection
    5. Pitfall
        - Pitfall: Clean Architecture & Dependency Injection
    6. Q & A
        - Q & A: Clean Architecture & Dependency Injection
5. **Refactoring Legacy Python Codebases**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Refactoring Legacy Python Codebases
    2. Core Concept
        - Core Concept: Refactoring Legacy Python Codebases
    3. Syntax
        - Syntax: Refactoring Legacy Python Codebases
    4. Example
        - Example: Refactoring Legacy Python Codebases
    5. Pitfall
        - Pitfall: Refactoring Legacy Python Codebases
    6. Q & A
        - Q & A: Refactoring Legacy Python Codebases

### 3. Git Version Control

#### 3.1. Module 1 — Introduction

1. **Web Architecture And Protocols**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Client-Server Architecture
        - The Request-Response Cycle
        - HTTP vs HTTPS Protocols
        - HTTP Request Methods (Verbs)
        - HTTP Status Codes Classification
        - Web Servers vs Application Servers
        - Identifiers: URI, URL, and URN
        - Domain Name System (DNS) Resolution Tracing
    4. Architecture & Diagram Visualizations
        - DNS Resolution & HTTP Request Sequence
    5. Code & Hardware Implementation
        - Deconstructing Raw HTTP/1.1 Request and Response Payload
        - Command Line Inspection with cURL
    6. Enterprise Real-World Applications
        - Case Study: High-Throughput IoT Gateway Architecture
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspect Web Request Lifecycle using Chrome DevTools & Python
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens under the hood when you type `https://example.com` into a browser address bar and press Enter?
        - Q2: What is the technical difference between HTTP `POST`, `PUT`, and `PATCH` methods?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Starter Code
        - Success Criteria
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax & Command Cheat Sheet
        - Official References
2. **Browser Rendering Engine Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Anatomy of a Modern Web Browser
        - Major Browser Engines
        - The 5 Stages of the Rendering Pipeline
        - Reflow vs Repaint Trigger Comparison
    4. Architecture & Diagram Visualizations
        - Critical Rendering Path Architecture
    5. Code & Hardware Implementation
        - Script Execution Blocking Modes (`async` vs `defer`)
    6. Enterprise Real-World Applications
        - Critical CSS Inline Pattern for Enterprise E-Commerce
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Profile Reflow & Layout Thrashing in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Reflow and Repaint, and how do you minimize them?
        - Q2: How does the browser construct the Render Tree, and why are `display: none` elements excluded?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Requirements
        - Starter Code Snippet
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Cheat Sheet
        - Official References
3. **Html Standards And Document Structure**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Evolution of HTML Standards
        - The DOCTYPE Declaration & Rendering Modes
        - Root Element (`<html>`) & Language Attribute
        - Character Encodings (ASCII vs UTF-8)
        - Viewport Configuration for Mobile Responsiveness
        - Metadata & Social Media Protocol (Open Graph)
    4. Architecture & Diagram Visualizations
        - Complete HTML5 Document Architecture Tree
    5. Code & Hardware Implementation
        - Production-Ready HTML5 Boilerplate Template
    6. Enterprise Real-World Applications
        - Open Graph Debugging & Rich Social Cards
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Build & Validate an Enterprise Boilerplate
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Standards Mode and Quirks Mode in modern browsers?
        - Q2: Why is the WHATWG specification referred to as a "Living Standard"?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Starter Requirements
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
4. **Html Syntax Rules And Element Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Tag Syntax & Element Composition
        - Standard Elements vs Void (Self-Closing) Elements
        - Attribute Categories
        - Block-Level vs Inline-Level vs Inline-Block
        - Element Nesting Rules & DOM Tree Integrity
        - HTML Entity Encoding & Escaping
    4. Architecture & Diagram Visualizations
        - Block vs Inline Box Model Layout Geometry
    5. Code & Hardware Implementation
        - Demonstrating Block, Inline, and Data Attributes
    6. Enterprise Real-World Applications
        - Data Attributes in Modern Web Frameworks & IoT Dashboards
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspecting Box Geometry & Dataset Properties in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the exact visual difference between Block-level, Inline-level, and Inline-Block elements?
        - Q2: What are HTML Void Elements, and how do they differ from standard elements in DOM parsing?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Starter Requirements
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
5. **Text Content And Formatting Elements**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Heading Hierarchy (`<h1>` through `<h6>`)
        - Semantic vs Presentational Text Formatting
        - Computer Code & Technical Documentation Elements
        - Quotations, Citations, & Abbreviations
        - Bidirectional Text Formatting (`<bdo>` & `<bdi>`)
    4. Architecture & Diagram Visualizations
        - Accessible Heading Tree Outline
    5. Code & Hardware Implementation
        - Technical Documentation Markup Example
    6. Enterprise Real-World Applications
        - Accessible Developer Portals & CLI Documentation
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Build a Technical Quick Reference Sheet
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the semantic difference between `<strong>` and `<b>`, and `<em>` and `<i>`?
        - Q2: How do `<bdo>` and `<bdi>` differ when handling internationalized text?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
6. **Hyperlinks And Anchor Navigation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Anchor Element Architecture
        - URL Types & Path Resolution Rules
        - Fragment Identifiers & In-Page Jumping
        - Link Targets & Vulnerability Hardening (`tabnabbing`)
        - Non-HTML Protocols & Devices Integration
        - Download Attribute & Resource Hints
    4. Architecture & Diagram Visualizations
        - Reverse Tabnabbing Attack vs Hardened Fix
    5. Code & Hardware Implementation
        - Comprehensive Navigation Portal (`navigation_demo.html`)
    6. Enterprise Real-World Applications
        - Multi-Tenant SaaS & IoT Gateway Navigation
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Test Reverse Tabnabbing Security in Browser Console
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What security risk is introduced by `target="_blank"`, and how does `rel="noopener"` fix it?
        - Q2: What is the difference between `<link rel="prefetch">` and `<link rel="preload">`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
7. **Structural Semantic Elements**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Semantic Web Philosophy
        - Structural Landmark Elements
        - Content Sectioning Elements
        - Interactive Native Components
        - Figures, Captions & Machine-Readable Time
    4. Architecture & Diagram Visualizations
        - Complete Semantic HTML5 Web Page Layout
    5. Code & Hardware Implementation
        - Semantic Web Page Implementation (`semantic_layout.html`)
    6. Enterprise Real-World Applications
        - Native Dialog Modals vs Heavy JS Libraries
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Test Native Dialog & Details Accordion
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the exact semantic distinction between an `<article>` and a `<section>`?
        - Q2: How does the native HTML5 `<dialog>` element improve accessibility over custom `<div>` modals?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
8. **Document Outline And Accessibility Tree**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Accessibility Tree (AOM) Architecture
        - HTML5 Semantic Elements vs ARIA Landmark Roles
        - Core ARIA Attributes & Properties
        - Keyboard Focus Management & `tabindex` Rules
    4. Architecture & Diagram Visualizations
        - DOM Tree vs Accessibility Tree Mapping
    5. Code & Hardware Implementation
        - Fully Accessible Component Suite (`accessible_suite.html`)
    6. Enterprise Real-World Applications
        - Automated Accessibility Testing in CI/CD Pipelines
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Audit Accessibility Tree Properties in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `tabindex="0"`, `tabindex="-1"`, and `tabindex="1"`?
        - Q2: How does `aria-live="polite"` differ from `aria-live="assertive"`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
9. **List Elements And Structure**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unordered Lists (`<ul>`) & Ordered Lists (`<ol>`)
        - Description Lists (`<dl>`, `<dt>`, `<dd>`)
        - Nesting Rules for Lists
    4. Architecture & Diagram Visualizations
        - List Tree DOM Structure
    5. Code & Hardware Implementation
        - Semantic Navigation & Metadata Lists
    6. Enterprise Real-World Applications
        - Accessible Navigation Menus
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Build a Nested IoT Setup Procedure List
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: When should you use a Description List (`<dl>`) instead of an Unordered List (`<ul>`)?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
10. **Tabular Data And Advanced Table Markup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Semantic Table Architecture
        - Cell Spanning (`colspan` & `rowspan`)
        - Column Groups (`<colgroup>` & `<col>`)
        - Table Accessibility & Header Scoping
        - Responsive Mobile Table Patterns
    4. Architecture & Diagram Visualizations
        - Accessible Table DOM Hierarchy
    5. Code & Hardware Implementation
        - Complex Accessible Matrix Table (`matrix_table.html`)
    6. Enterprise Real-World Applications
        - Financial Reports & System Metrics Dashboards
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspect Accessible Headers in DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of the `scope` attribute on `<th>` elements?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
11. **Form Architecture And Submissions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Form Architecture
        - Key `<form>` Attributes
        - HTTP Submission Methods: GET vs POST
        - Encoding Types (`enctype`)
    4. Architecture & Diagram Visualizations
        - Form Submission Payload Pipeline
    5. Code & Hardware Implementation
        - File Upload & Search Form Examples
    6. Enterprise Real-World Applications
        - Firmware Uploads & Cloud API Integration
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspect Payload Formats in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens if a developer omits `enctype="multipart/form-data"` on a form containing a file input?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
12. **Form Controls And Input Types**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Label Association (`<label>`)
        - Form Controls Classification Matrix
        - Form Grouping & Visual Metering
    4. Architecture & Diagram Visualizations
        - Accessible Form Fieldset Hierarchy
    5. Code & Hardware Implementation
        - IoT Device Configuration Form (`iot_config_form.html`)
    6. Enterprise Real-World Applications
        - Soft-Keyboards & Mobile Optimization
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `<select>` dropdowns and `<datalist>` autocomplete inputs?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
13. **Native Client Side Form Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Native Validation Attributes
        - CSS Validation Pseudo-Classes
        - The Constraint Validation API (JavaScript)
    4. Architecture & Diagram Visualizations
        - Constraint Validation Flow
    5. Code & Hardware Implementation
        - Custom Validation & RegEx Portal (`validation_portal.html`)
    6. Enterprise Real-World Applications
        - Client-Side Validation is NOT Security
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is `ValidityState` in the HTML5 Constraint Validation API?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
14. **Media Elements Images Audio And Video**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Responsive Images (`srcset` & `sizes`)
        - Art Direction (`<picture>`)
        - Audio & Video Elements
    4. Architecture & Diagram Visualizations
        - Media Selection Pipeline
    5. Code & Hardware Implementation
        - Comprehensive Media Dashboard (`media_dashboard.html`)
    6. Enterprise Real-World Applications
        - AVIF & WebP Next-Gen Image Compression
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `<img srcset>` and the `<picture>` tag?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
15. **Embedded External Content**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Inline Frames (`<iframe>`)
        - Iframe Security Sandboxing (`sandbox` & `allow`)
    4. Architecture & Diagram Visualizations
        - Iframe Sandboxing Boundary
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
        - Embedded Grafana & OpenStreetMap Widgets
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does an empty `sandbox=""` attribute do on an iframe?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
16. **Vector Graphics And Html5 Canvas**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SVG vs Canvas Comparison Matrix
        - SVG Primitives (`<svg>`)
        - HTML5 Canvas 2D API (`<canvas>`)
    4. Architecture & Diagram Visualizations
        - SVG (DOM Retained) vs Canvas (Pixel Immediate)
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main architectural difference between SVG and Canvas?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
17. **Web Storage And Indexeddb**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Client Storage Matrix
        - LocalStorage & SessionStorage API
        - Storage Event Cross-Tab Sync
        - IndexedDB Architecture
    4. Architecture & Diagram Visualizations
        - IndexedDB Transaction Architecture
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is IndexedDB preferred over LocalStorage for offline-first web apps?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
18. **Geolocation And Device Apis**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Geolocation API
        - Position & Error Objects
    4. Architecture & Diagram Visualizations
        - Geolocation Permission Loop
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does Geolocation require HTTPS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
19. **Html5 Drag And Drop Api**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Drag and Drop Lifecycle
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `event.preventDefault()` required in the `dragover` handler?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
20. **Web Workers And Multithreading**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Single-Threaded JS & Web Workers Solution
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Main Application Thread (`app.js`)
        - Background Worker Script (`worker.js`)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Can a Web Worker access `localStorage` or DOM elements directly?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
21. **Shadow Dom And Custom Elements**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Web Components Suite
        - Custom Element Lifecycle Callbacks
        - Shadow DOM Encapsulation
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main purpose of the Shadow DOM in Web Components?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
22. **Web Content Accessibility Guidelines**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The POUR Principles (WCAG 2.1 / 2.2)
        - Conformance Levels
        - Color Contrast Requirements (Level AA)
        - Skip Navigation Links
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the four WCAG POUR principles?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
23. **Search Engine Optimization And Microdata**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - JSON-LD vs Microdata
        - JSON-LD Implementation Example
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is JSON-LD preferred over Microdata for SEO?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
24. **Performance Optimization And Best Practices**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Resource Hints Summary
        - Native Lazy Loading (`loading="lazy"`)
        - Obsolete & Deprecated HTML Tags
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `preload` and `prefetch`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
25. **Css Syntax And Inclusion Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Syntax Anatomy
        - Inclusion Methods Comparison
        - CSS At-Rules (`@`)
    4. Architecture & Diagram Visualizations
        - External CSS Loading vs `@import` Performance Waterfall
    5. Code & Hardware Implementation
        - External Stylesheet Architecture
    6. Enterprise Real-World Applications
        - Avoiding HTTP Request Waterfalls
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the performance disadvantages of using `@import` inside CSS files?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
26. **Comprehensive Selector Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Attribute Selectors
        - Combinator Systems
        - Pseudo-Classes & Modern `:has()` Parent Selector
        - Pseudo-Elements (`::before` & `::after`)
    4. Architecture & Diagram Visualizations
        - Combinator Target Matching Tree
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `:nth-child()` and `:nth-of-type()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
27. **Cascade Specificity And Inheritance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Cascade Algorithm
        - Specificity Calculation Vector Matrix `(A, B, C, D)`
        - Cascade Layers (`@layer`) Architecture
    4. Architecture & Diagram Visualizations
        - Cascade Layer Precedence Hierarchy
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do `@layer` declarations alter standard specificity calculations?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
28. **The Css Box Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 4 Box Model Layers
        - `content-box` vs `border-box`
        - Margin Collapsing Mechanics
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `box-sizing: border-box` preferred over `content-box`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
29. **Display Property And Visual Formatting Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Block Formatting Context (BFC) Triggers
        - `display: none` vs `visibility: hidden` vs `opacity: 0`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the modern standard property for creating a Block Formatting Context?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
30. **Positioning Systems And Stacking Contexts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Position Modes Matrix
        - Stacking Contexts & $Z$-Index Rules
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does a child with `z-index: 9999` fail to render above an element with `z-index: 2`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
31. **Sizing Units And Intrinsic Sizing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unit Categories Matrix
        - Intrinsic Sizing Keywords
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the technical difference between `1rem` and `1em`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
32. **Flexible Box Layout Flexbox**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Flexbox Axes System
        - Main Axis vs Cross Axis Alignment
        - Flex Item Sizing (`flex: grow shrink basis`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `flex: 1` expand to in CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
33. **Css Grid Layout System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - 2D Grid vs 1D Flexbox
        - Fractional Unit (`fr`) & `minmax()`
        - Named Grid Areas (`grid-template-areas`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `auto-fill` and `auto-fit` in CSS Grid?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
34. **Advanced Typography And Web Fonts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `@font-face` Syntax & WOFF2
        - Micro-Typography & Line Clamping
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `font-display: swap` in CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
35. **Modern Css Color Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Evolution of CSS Color Functions
        - The `color-mix()` Function
        - The `currentcolor` Keyword
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What makes `oklch()` superior to traditional `hsl()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
36. **Backgrounds Borders And Shadows**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Gradient Types
        - Box Shadow Layering (`box-shadow`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between blur-radius and spread-radius in a `box-shadow` property?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
37. **Visual Effects Filters And Blending**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Glassmorphism & `backdrop-filter`
        - Clipping Paths (`clip-path`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does `filter: blur()` differ from `backdrop-filter: blur()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
38. **Css Transitions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Transition Properties & Shorthand
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you avoid animating `height` or `margin` properties?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
39. **2D And 3D Transformations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - 2D vs 3D Transform Functions
        - 3D Card Flipping Setup
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `transform-style: preserve-3d` do?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
40. **Keyframe Animations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `@keyframes` Syntax & Shorthand
        - `animation-fill-mode`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `animation-fill-mode: forwards` do?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
41. **Responsive Architecture Principles**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Mobile-First vs Desktop-First
        - The Viewport Meta Tag
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is Mobile-First CSS architecture preferred over Desktop-First?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
42. **Media Queries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Modern Range Syntax (Level 4)
        - User Preference Media Features
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is `prefers-reduced-motion` and why is it important for accessibility?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
43. **Container Queries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Media Queries vs Container Queries
        - Setting Up Container Context
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main problem Container Queries solve that Media Queries could not?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
44. **Fluid Layout Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Math Functions (`calc`, `min`, `max`, `clamp`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the three parameters passed to `clamp()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
45. **Css Custom Properties Variables**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Syntax & Scoping
        - Typed Custom Properties (`@property`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do CSS Custom Properties differ from Sass/SCSS variables?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
46. **Modern Css Architecture And Methodologies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - BEM Naming Convention Syntax
        - ITCSS (Inverted Triangle CSS) Layers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does BEM stand for and what are its advantages?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
47. **Native Css Nesting And Logical Properties**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Native CSS Nesting (`&`)
        - Physical vs Logical Properties Matrix
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the benefit of Logical Properties over Physical Properties in modern CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
48. **Utility First Css And Tailwind Introduction**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Semantic CSS vs Utility-First CSS
        - Component Extraction (`@apply`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main benefit of Utility-First CSS over traditional semantic CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
49. **Component Frameworks And Component Styling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Modules Hashing Mechanism
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do CSS Modules prevent global CSS class name collisions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
50. **Production Css Performance Purging And Optimization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Critical CSS Extraction
        - GPU Layer Promotion (`will-change`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Critical CSS and why does inlining it improve performance?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
51. **History Evolution And Ecmascript Standards**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - TC39 Proposal Process
        - Transpilers vs Polyfills
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Babel Configuration Setup (`babel.config.json`)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the technical difference between a Babel transpiler and a polyfill?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
52. **Javascript Engine Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The V8 Engine Execution Pipeline
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are Ignition and TurboFan in the Google Chrome V8 engine?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
53. **Execution Context Call Stack And Memory Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Execution Context Lifecycle
        - Mark-and-Sweep Garbage Collection
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Mark-and-Sweep Garbage Collection in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
54. **Variable Declarations And Scoping**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `var` vs `let` vs `const`
        - The Temporal Dead Zone (TDZ)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the Temporal Dead Zone (TDZ) in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
55. **Primitive And Reference Data Types**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Primitives vs Reference Types
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the 7 primitive data types in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
56. **Type Coercion And Comparison Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 8 Falsy Values in JavaScript
        - Abstract (`==`) vs Strict (`===`) Equality
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the 8 falsy values in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
57. **Comprehensive Operator Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `||` vs `??` (Nullish Coalescing)
        - Optional Chaining (`?.`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the Nullish Coalescing Operator (`??`) differ from the Logical OR Operator (`||`)?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
58. **Vectors Matrices And Vector Spaces**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Vectors & The Dot Product
        - Matrix Multiplication Geometry
        - Linear Independence & Span
    4. Architecture & Diagram Visualizations
        - Matrix Multiplication Inner Dimension Match
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the geometric interpretation of the dot product between two normalized vectors?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
59. **Probability Fundamentals And Axioms**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Kolmogorov Probability Axioms
        - Bayes' Theorem
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Prior Probability and Posterior Probability in Bayes' Theorem?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
60. **Parametric Hypothesis Testing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Error Matrix & Statistical Power
        - Two-Sample Independent $t$-Test
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a $p$-value in hypothesis testing?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
61. **Non Parametric Statistical Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Parametric vs Non-Parametric Decision Matrix
        - Bootstrapping Resampling
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Bootstrapping and why is it useful in Data Science?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
62. **Python 312 Structural Pattern Matching**
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
63. **Static Type Hinting And Mypy Validation**
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
64. **Asyncio Event Loop And Async Await**
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
65. **Modern Python Packaging Pyproject And Uv**
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
66. **Java21 Record Classes And Dto Patterns**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Eliminating DTO Boilerplate
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Can a Java Record Class extend another class or be extended?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
67. **Java21 Sealed Classes And Interfaces**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Controlled Class Hierarchies
        - Subclass Modifiers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does exhaustive pattern matching on a sealed class eliminate the need for a `default` case in switch expressions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
68. **Java21 Virtual Threads Project Loom**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Platform Threads vs Virtual Threads
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Thread Pinning in Java 21 Virtual Threads and how do you avoid it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
69. **Java21 Sequenced Collections**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Missing Abstraction in Legacy Java Collections
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What problem do Sequenced Collections solve in Java 21?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
70. **Matrix Inversion Determinants And Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Determinants & Singular Matrices
        - Solving $A\mathbf{x} = \mathbf{b}$
        - Condition Number ($\kappa$)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you avoid explicitly computing $A^{-1}$ to solve $A\mathbf{x} = \mathbf{b}$?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
71. **Eigenvalues Eigenvectors And Decompositions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Eigenvalues & Eigenvectors
        - Singular Value Decomposition (SVD)
        - PCA & Covariance Matrix Connection
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the relationship between SVD and PCA?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
72. **Multivariable Calculus And Gradient Vectors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Gradient Vector ($\nabla f$)
        - The Hessian Matrix ($H$)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does the Gradient Vector $\nabla f$ represent geometrically?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
73. **Discrete And Continuous Probability Distributions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - PMF, PDF, & CDF
        - Gaussian (Normal) Distribution $\mathcal{N}(\mu, \sigma^2)$
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between a PMF and a PDF?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
74. **Joint Marginal And Conditional Distributions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Joint & Marginal Distributions
        - Covariance & Pearson Correlation
        - The Central Limit Theorem (CLT)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does the Central Limit Theorem state and why is it crucial for statistics?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
75. **Selenium4 Relative Locators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Spatial Locating in Selenium 4
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do Relative Locators in Selenium 4 calculate element positions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
76. **Estimation And Confidence Intervals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Point Estimation & MLE
        - Confidence Intervals (CI)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the correct interpretation of a 95% Confidence Interval?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
77. **Mysql8 Analytical Window Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `GROUP BY` vs Window Functions (`OVER`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `RANK()` and `DENSE_RANK()` in SQL?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
78. **Modern C23 Features Constexpr Typeof Auto**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The C23 Standard Evolution
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does `constexpr` in C23 improve performance over standard `const` variables?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
79. **Anova And Chi Square Tests**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - One-Way ANOVA ($F$-Statistic)
        - Chi-Square Test of Independence ($\chi^2$)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why use ANOVA instead of multiple individual $t$-tests when comparing 4 groups?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
80. **Cpp20 Smart Pointers And Memory Safety**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - RAII & Smart Pointers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `std::unique_ptr` and `std::shared_ptr`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
81. **Conditional Logic And Guard Clauses**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Guard Clauses vs Nested Arrow Code
        - Object Lookup Tables
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Guard Clause and why is it preferred over nested `if-else` blocks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
82. **Loops And Iteration Constructs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `for...in` vs `for...of`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the technical difference between `for...in` and `for...of` in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
83. **Iteration Protocols Iterators And Generators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Iterable & Iterator Protocols
        - Generator Functions (`function*`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does a Generator function differ from a regular function in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
84. **Function Declarations Expressions And Arrow Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Declarations vs Expressions vs Arrow Functions
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the `this` keyword behave differently in Arrow Functions compared to Regular Functions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
85. **Parameters Arguments And Return Values**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Rest Parameters (`...args`) vs `arguments` Object
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main advantage of Rest Parameters (`...args`) over the `arguments` object?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
86. **Scope Chain And Closures**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Lexical Scoping & Scope Chain
        - What is a Closure?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a JavaScript Closure and how does it retain memory?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
87. **Functional Concepts And Higher Order Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Pure Functions vs Side Effects
        - Currying
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Currying in Functional JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
88. **Object Literals Descriptors And Immutability**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Object Immutability Levels
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `Object.freeze()` and `Object.seal()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
89. **Dense Sparse Arrays And Higher Order Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Mutating vs Non-Mutating Methods
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does `.reduce()` work in JavaScript and what is the role of the initial value parameter?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
90. **Destructuring Assignment And Spread Rest Operators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unpacking Data Structures
        - Spread (`...`) for Immutable Merging
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do you rename a variable during Object Destructuring in ES6?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
91. **Keyed Collections Map Set Weakmap Weakset**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Plain Object vs `Map`
        - `WeakMap` & `WeakSet` Garbage Collection
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why can you not iterate over a `WeakMap` or check its size?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
92. **Asynchronous Execution Callbacks Event Queue**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Event Loop & Task Queue Priority
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between the Macrotask Queue and Microtask Queue in the JavaScript Event Loop?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
93. **Es6 Promises Architecture States And Chaining**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Promise States & Immutability
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens if a `.then()` callback returns a plain scalar value versus another Promise?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
94. **Async Await Syntactic Sugar And Async Iteration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Async/Await as Syntactic Sugar
        - Asynchronous Iteration (`for await...of`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens when the `await` keyword is executed in an `async` function?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
95. **Promise Combinators All Allsettled Race Any**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Promise Combinators Comparison Matrix
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main difference between `Promise.all()` and `Promise.allSettled()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
96. **Prototypes Prototype Chain And Inheritance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Prototypal Inheritance vs Class-Based Inheritance
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens when a property is accessed on a JavaScript object that does not exist on the instance itself?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
97. **Es6 Class Syntax And Constructors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Classes as Syntactic Sugar
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Are ES6 classes true classes like in Java or C++?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
98. **Inheritance Method Overriding And Super**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Subclassing & Mandatory `super()`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is calling `super()` mandatory in a subclass constructor before accessing `this`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
99. **Private Fields Getters Setters Static Members**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Hard Encapsulation (`#privateField`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do modern `#` private fields in JavaScript differ from the legacy `_` prefix convention?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
100. **Dom Tree Navigation And Selection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `querySelectorAll` (NodeList) vs `getElementsByClassName` (HTMLCollection)
        - Upward Traversal with `.closest()`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main difference between a live `HTMLCollection` and a static `NodeList`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
101. **Dynamic Element Creation And Modification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `appendChild()` vs `append()`
        - HTML5 `dataset` API
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the HTML5 `dataset` API in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
102. **Event Handling Propagation Bubbling Capturing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 3 Event Propagation Phases
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `event.target` and `event.currentTarget`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
103. **Event Delegation And Custom Events**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Event Delegation Architecture
        - Custom Events
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the primary benefits of using the Event Delegation Pattern?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
104. **Fetch Api And Http Network Requests**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The `fetch()` HTTP Status Code Trap
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does `fetch()` not reject when a server returns a 404 or 500 error code?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
105. **Web Storage Cookies Localstorage Sessionstorage**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Client Storage Comparison
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main security risk of storing authentication tokens in LocalStorage compared to HttpOnly Cookies?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
106. **Client Side Storage With Indexeddb**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why IndexedDB Over LocalStorage?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does IndexedDB differ from LocalStorage?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
107. **Websockets And Realtime Communication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - HTTP Polling vs WebSockets
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Exponential Backoff and why is it essential for WebSocket reconnection strategies?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
108. **Es6 Modules Export And Import Syntax**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CommonJS (`require`) vs ES Modules (`import`)
        - Named vs Default Exports
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `mathUtils.js` (Module)
        - File 2: `main.js` (Consumer)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main structural advantage of ES Modules over CommonJS `require()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
109. **Dynamic Imports And Toplevel Await**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Static Imports vs Dynamic `import()`
        - Top-Level Await
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Code Splitting and how do Dynamic Imports facilitate it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
110. **Modern Build Tooling Bundlers Tree Shaking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Legacy Bundlers (Webpack) vs Modern Native ESM (Vite)
        - Tree Shaking Mechanics
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Initializing a Lightning-Fast Vite Project
        - Production Build & Source Map Inspection
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Tree Shaking in modern JavaScript build tools and how does it work?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
111. **Critical Rendering Path And Dom Reflows**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Critical Rendering Path
        - Reflow vs Repaint vs Layout Thrashing
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Layout Thrashing in JavaScript and how do you prevent it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
112. **Core Web Vitals And Performance Monitoring**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Google Core Web Vitals Metrics
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Interaction to Next Paint (INP) and how does it differ from FID?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
113. **Memory Management And Leak Prevention**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Mark-and-Sweep Garbage Collection
        - The 4 Common Memory Leak Patterns
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Detached DOM Node memory leak in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
114. **Web Security Xss Csrf Csp Mitigation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - XSS vs CSRF Vulnerability Matrix
        - Content Security Policy (CSP)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Content Security Policy (CSP) and how does it prevent XSS attacks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
115. **Proxy And Reflect Api Metaprogramming**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is Meta-Programming?
        - Proxy Traps & Reflect API
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you use `Reflect` methods inside Proxy handler traps instead of accessing the target directly?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
116. **Web Workers And Multithreaded Javascript**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Single-Threaded Main Loop vs Worker Threads
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `worker.js` (Background Thread)
        - File 2: `main.js` (UI Thread)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What capabilities and Web APIs are accessible inside a Web Worker?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
117. **Service Workers And Offline Pwa Caching**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Service Worker Proxy Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `sw.js` (Service Worker Script)
        - File 2: `app.js` (Register Service Worker)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the Stale-While-Revalidate caching strategy work?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
118. **Javascript Unit Testing With Vitest**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The AAA Unit Testing Pattern
        - `toBe` vs `toEqual`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Target Module: `math.js`
        - Vitest Test Suite: `math.test.js`
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `toBe` and `toEqual` in Vitest/Jest?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
119. **E2E Testing With Playwright**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unit Testing vs End-to-End (E2E) Testing
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Playwright Test Suite: `dashboard.spec.js`
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is Playwright preferred over older Selenium or Puppeteer testing frameworks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
120. **Javascript Design Patterns**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Design Patterns Categories
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main difference between the Observer Pattern and the Publisher-Subscriber (PubSub) Pattern?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
121. **Internationalization Intl Api**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Native ECMAScript `Intl` API
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the performance advantages of using the native `Intl` API over external libraries like Moment.js?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
122. **Web Components And Shadow Dom**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 4 Web Components Technologies
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Usage in HTML:
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why must Custom Element tag names contain a hyphen (`-`)?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
123. **Webassembly Integration Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is WebAssembly (Wasm)?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Is WebAssembly intended to replace JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
124. **Advanced Debugging Chrome Devtools**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Advanced Breakpoint Types
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Logpoint in Chrome DevTools and how does it differ from a standard Breakpoint?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
125. **Capstone Realtime Iot Dashboard**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Capstone Enterprise Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Reactive State Store (`store.js`)
        - Capstone Dashboard Application (`app.js`)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does this Vanilla JavaScript Capstone architecture achieve high performance without a frontend framework like React?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
126. **Wsgi Architecture And Flask Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is WSGI (PEP 3333)?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is WSGI in Python web development and why is `Flask(__name__)` required?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
127. **Flask Application Factory Pattern**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why the Application Factory Pattern?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `config.py` (Environment Configurations)
        - File 2: `app/__init__.py` (Application Factory)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the Application Factory Pattern in Flask and why is it recommended for production applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
128. **Flask Routing And Url Converters**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Built-in URL Converters
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you use `url_for()` instead of hardcoding URL strings in Flask?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
129. **Flask Request Response Objects**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Flask `request` Context Local
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Context Local in Flask and how does the `request` object work behind the scenes?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
130. **Jinja2 Syntax Control Flow And Macros**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Jinja2 Delimiter Syntax
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `templates/macros/card.html` (Jinja2 Reusable Macro)
        - File 2: `templates/dashboard.html` (Main Page)
        - File 3: `app.py` (Python View Function)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does Jinja2 prevent Cross-Site Scripting (XSS) attacks when rendering dynamic variables?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
131. **Flask Contexts Application And Request**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Application Context vs Request Context
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between the Application Context and Request Context in Flask?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
132. **Flask G Object And Request Scoped State**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is the `g` Object?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `g` and `session` in Flask?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
133. **Flask Wtf Forms And Fields**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Processing Manual HTML Forms vs Flask-WTF
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `forms.py` (FlaskForm Class Definition)
        - File 2: `app.py` (Flask View Function)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `form.validate_on_submit()` do in Flask-WTF?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
134. **Form Validation And Csrf Protection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Custom In-Class Field Validation
        - CSRF Protection Mechanism
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `forms.py` (Form with Custom & Standard Validators)
        - File 2: `templates/register.html` (Rendering Inline Validation Errors)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do you write a custom field validator in Flask-WTF?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
135. **Flask Sqlalchemy Extension Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Object-Relational Mapping (ORM)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `extensions.py` (Unbound Extension Instance)
        - File 2: `config.py`
        - File 3: `app/__init__.py` (Application Factory Integration)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you initialize Flask-SQLAlchemy using `db = SQLAlchemy()` in an `extensions.py` module rather than `db = SQLAlchemy(app)`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
136. **Sqlalchemy Models Fields And Relationships**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SQLAlchemy Model Mapping
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `models.py` (SQLAlchemy Relational Schema)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `backref` and `back_populates` in SQLAlchemy relationships?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
137. **Sqlalchemy Crud Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unit of Work Transaction Management
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `db.session.rollback()` in Flask-SQLAlchemy?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
138. **Schema Migrations With Flask Migrate**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why `db.create_all()` Fails in Production
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `extensions.py`
        - File 2: `app/__init__.py` (Factory Integration)
        - File 3: Command Line Execution Sequence
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does Flask-Migrate detect changes made to SQLAlchemy models when generating migration scripts?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
139. **User Authentication With Flask Login**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Flask-Login Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `models.py` (User Model with UserMixin)
        - File 2: `app.py` (Flask-Login Initialization & Auth Routes)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `@login_manager.user_loader` in Flask-Login?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
140. **Password Hashing And Cookie Security**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - One-Way Password Hashing & Salting
        - Flask Session Cookie Security Configuration
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `security_demo.py` (Password Hashing & Cookie Security Config)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is storing plain MD5 or SHA-256 hashes of passwords insecure, and how does Werkzeug address this?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
141. **Flask Blueprint Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is a Flask Blueprint?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `app/api/routes.py` (Blueprint Module)
        - File 2: `app/__init__.py` (Registering Blueprints in Application Factory)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Flask Blueprint and how does it improve code architecture?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
142. **Restful Api Principles And Resource Routing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - REST Architectural Constraints
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is idempotency in RESTful APIs and which HTTP verbs are idempotent?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
143. **Api Serialization With Flask Marshmallow**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Serialization vs Deserialization
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `schemas.py` (Flask-Marshmallow Schemas)
        - File 2: `routes.py` (Using Schemas in API Views)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the primary role of Marshmallow schemas in a Flask REST API?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
144. **Jwt Authentication With Flask Jwt Extended**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - JSON Web Token (JWT) Structure
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main structural difference between session-based authentication and JWT authentication?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
145. **Application Caching With Flask Caching**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why Backend Caching?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `@cache.cached()` and `@cache.memoize()` in Flask-Caching?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
146. **Asynchronous Background Tasks With Celery**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why Asynchronous Background Tasks?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `celery_app.py` (Celery Integration Helper)
        - File 2: `tasks.py` (Celery Tasks)
        - File 3: `app.py` (Dispatching Tasks & Checking Status)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is Celery used with Flask instead of Python's built-in `threading` module?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
147. **Email Delivery With Flask Mail**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SMTP Protocol & Synchronous vs Async Delivery
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is it crucial to send emails asynchronously in web applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
148. **Custom Error Pages And Handlers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Exception Handling Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `@errorhandler` and `@app_errorhandler` on a Flask Blueprint?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
149. **Application Logging And Sentry**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Production Logging Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `RotatingFileHandler` critical for production Python applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
150. **Automated Testing With Pytest**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Flask `test_client()` Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `conftest.py` (Pytest Shared Fixtures)
        - File 2: `test_api.py` (Pytest Test Cases)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does Flask's `app.test_client()` work and why is it preferred over HTTP requests library like `requests` during unit testing?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
151. **Production Deployment Gunicorn Nginx Docker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Enterprise Production Deployment Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `wsgi.py` (Production Entrypoint)
        - File 2: `Dockerfile` (Production Multi-Stage Container)
        - File 3: `docker-compose.yml` (Multi-Container Orchestration)
        - File 4: `nginx.conf` (Nginx Reverse Proxy Configuration)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why must Flask's built-in development server never be used in production environments, and what roles do Gunicorn and Nginx play?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
152. **Asgi Architecture Uvicorn And Fastapi Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - WSGI vs ASGI Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Running with Uvicorn Server:
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens if you call a synchronous blocking function inside an `async def` endpoint in FastAPI?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
153. **Fastapi App Instantiation Routing And Openapi**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Zero-Configuration Automatic OpenAPI Generation
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does FastAPI generate Swagger UI documentation automatically without third-party plugins?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
154. **Path And Query Parameters**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Parameter Parsing & Automatic Type Conversion
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does FastAPI differentiate between a Path Parameter and a Query Parameter in a route function?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
155. **Pydantic V2 Models And Schema Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Pydantic v2 Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the key improvements of Pydantic v2 over Pydantic v1 in FastAPI?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
156. **Dependency Injection Architecture And Depends**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is Dependency Injection?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the main benefits of FastAPI's Dependency Injection system over traditional middleware?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
157. **Sub Dependencies Security And Yield Cleanups**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Yield Dependencies & Context Cleanup
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Mocking Dependencies in Unit Tests:
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do Yield Dependencies work in FastAPI and how do they prevent resource leaks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
158. **Sqlalchemy 20 Async Engine And Asyncpg**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Synchronous vs Asynchronous Database Drivers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `database.py` (SQLAlchemy 2.0 Async Engine & Dependency)
        - File 2: `main.py` (Using AsyncSession in Route)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `asyncpg` significantly faster than `psycopg2` when used with FastAPI?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
159. **Async Crud Operations And Asyncsession**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SQLAlchemy 2.0 Async Query Style
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `models.py` (Async SQLAlchemy Models)
        - File 2: `main.py` (Async CRUD Routes)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is lazy loading problematic in asynchronous SQLAlchemy and how does `selectinload()` solve it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
160. **Oauth2 Password Bearer And Hashing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - OAuth2 Password Bearer Flow
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `OAuth2PasswordBearer` do under the hood in FastAPI?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
161. **Jwt Authentication And Current User**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The `get_current_user` Dependency Pipeline
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does FastAPI implement Role-Based Access Control (RBAC) cleanly using Dependency Injection?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
162. **Apirouter Architecture And Prefixes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is an APIRouter?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `routers/devices.py` (APIRouter Module)
        - File 2: `main.py` (Main FastAPI App Registering Router)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does `APIRouter` in FastAPI differ from Flask's `Blueprint`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
163. **Modular Directory Structure And Big Applications**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Enterprise Production Directory Layout
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `src/app/core/config.py` (Pydantic-Settings Configuration)
        - File 2: `src/app/main.py` (Global Exception Handler & Main App)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `pydantic-settings` preferred over `os.environ.get()` in FastAPI production codebases?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
164. **Asynchronous Middleware And Cors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is FastAPI Middleware?
        - Cross-Origin Resource Sharing (CORS)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a CORS preflight request and how does FastAPI handle it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
165. **Request Timing Headers And Performance Logging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - High-Precision Latency Tracking
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `time.perf_counter()` preferred over `time.time()` for measuring code latency?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
166. **Fastapi Background Tasks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What are FastAPI BackgroundTasks?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: When should you use FastAPI `BackgroundTasks` versus an external task queue like Celery?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
167. **Lifespan Event Handlers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What are Lifespan Events?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why did FastAPI deprecate `@app.on_event("startup")` in favor of the `lifespan` context manager?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
168. **Websockets Protocol And Endpoint Handling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - HTTP Polling vs Full-Duplex WebSockets
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `await websocket.accept()` in a FastAPI WebSocket endpoint?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
169. **Realtime Connection Manager And Broadcasting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Connection Manager Pattern
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do you scale WebSocket broadcasting across multiple Uvicorn worker processes or servers?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
170. **Async Testing With Pytest And Httpx**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why `httpx.AsyncClient` over Starlette `TestClient`?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `conftest.py` (Pytest Async Fixtures)
        - File 2: `test_main.py` (Async Test Cases)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `httpx.AsyncClient` preferred over `TestClient` when testing async FastAPI applications with Pytest?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
171. **Production Deployment Gunicorn Uvicorn Docker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Production Process Management: Gunicorn + Uvicorn
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `gunicorn_conf.py` (Gunicorn Configuration)
        - File 2: `Dockerfile` (Production Container Definition)
        - File 3: `docker-compose.yml` (Multi-Container Deployment)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why do we use Gunicorn together with Uvicorn in production rather than running Uvicorn alone?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
172. **Esp32 Architecture And Pinout**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - ESP32 System-on-Chip (SoC) Architecture
        - Critical GPIO Pin Classification
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are ESP32 Strapping Pins and why must engineers exercise caution when connecting external hardware components to them?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
173. **Platformio Espidf Toolchain Setup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Embedded Development Frameworks
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `platformio.ini` (PlatformIO Configuration File)
        - File: `src/main.cpp` (Embedded Entrypoint)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is PlatformIO preferred over Arduino IDE for professional embedded engineering?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
174. **Gpio Digital Io And Interrupts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Polling vs Hardware Interrupts
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why must ESP32 Interrupt Service Routine (ISR) functions be declared with the `IRAM_ATTR` attribute?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
175. **Adc Dac And Pwm Timer Control**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - 12-Bit Analog-to-Digital Conversion (ADC)
        - Hardware PWM via LEDC Peripheral
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should embedded engineers avoid connecting analog sensors to ADC2 pins on the ESP32 in connected IoT applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
176. **I2C Spi And Uart Communication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Serial Protocol Comparison Matrix
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `main.cpp` (I2C Bus Address Scanner & Dual Hardware UART)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Compare I2C and SPI protocols. When would you choose SPI over I2C in an embedded system design?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
177. **Freertos Task Creation And Core Pinning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why FreeRTOS on ESP32?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `xTaskCreate()` and `xTaskCreatePinnedToCore()` in ESP32 FreeRTOS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
178. **Freertos Task Priorities Delays And Stack**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Pre-emptive Priority Scheduling
        - `vTaskDelay()` vs `vTaskDelayUntil()`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `vTaskDelay()` and `vTaskDelayUntil()` in FreeRTOS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
179. **Freertos Queues And Inter Task Messaging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why FreeRTOS Queues?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do FreeRTOS Queues achieve thread safety when sharing data between tasks running on different CPU cores?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
180. **Freertos Semaphores Mutexes And Locks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Binary Semaphores vs Mutexes
        - What is Priority Inversion?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Priority Inversion and how do FreeRTOS Mutexes resolve it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
181. **Wifi Station And Access Point Modes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - ESP32 Wi-Fi Operating Modes
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Station (STA) Mode and Access Point (AP) Mode on the ESP32?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
182. **Non Blocking Wifi Reconnect And Events**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Asynchronous System Wi-Fi Events
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Exponential Backoff and why is it essential for IoT Wi-Fi reconnect logic?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
183. **Http Rest Client Requests**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Embedded HTTP Client Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `http.end()` mandatory after executing an HTTP request with `HTTPClient` on the ESP32?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
184. **Mqtt Protocol And Pubsubclient**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is MQTT?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Compare MQTT and HTTP protocols for resource-constrained IoT devices.
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
185. **Esp32 Websocket Client Streaming**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why WebSockets for Microcontroller Telemetry?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: When should an embedded engineer choose WebSockets over MQTT for an IoT system architecture?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
186. **Deep Sleep Modes And Rtc Memory**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Power Consumption Modes Comparison
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens to standard C++ global variables versus `RTC_DATA_ATTR` variables when the ESP32 enters Deep Sleep?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
187. **Deep Sleep Wakeup Sources**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Deep Sleep Wake-Up Sources Matrix
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Ext0 and Ext1 wake-up sources on the ESP32?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
188. **Over The Air Ota Firmware Updates**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Dual-Bank OTA Partition Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the ESP32 dual-bank partition table prevent device bricking during Over-The-Air (OTA) updates?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
189. **Secure Boot Flash Encryption Partitions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Custom Partition Tables
        - Hardware Security Primitives
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `partitions_custom.csv` (Custom 4MB Dual-OTA Partition Table)
        - File: `platformio.ini` (Configuring Custom Partition Table)
        - File: `main.cpp` (Querying Partition & Security Status)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Explain how Secure Boot V2 and Flash Encryption combine to secure ESP32 hardware in the field.
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
190. **Spiffs Littlefs And Static File Serving**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SPIFFS vs LittleFS
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `data/index.html` (Static Web Asset in PlatformIO `data/` Directory)
        - File: `src/main.cpp` (Mounting LittleFS & File I/O)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is LittleFS preferred over SPIFFS for modern ESP32 embedded applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
191. **Espasyncwebserver And Rest Control**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Synchronous vs Asynchronous Web Servers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `ESPAsyncWebServer` superior to the standard synchronous `WebServer.h` library for ESP32 applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
192. **Fullstack Iot System Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - End-to-End Full-Stack IoT Data Pipeline
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `backend_bridge.py` (FastAPI + MQTT Ingestion Bridge)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is an MQTT message broker placed between embedded ESP32 devices and backend FastAPI microservices in full-stack IoT architectures?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
193. **Capstone Production Iot Gateway**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Capstone Architecture Blueprint
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - ESP32 Production FreeRTOS Firmware (`src/main.cpp`)
        - FastAPI Ingestion & WebSockets Backend (`server.py`)
    6. Guided Step-by-Step Hands-On Exercise
    7. Industry Interview Q&A
        - Q1: How does this capstone architecture ensure high reliability and zero telemetry loss across network drops?
    8. Self-Assessment Quiz
    9. Summary & Cheat Sheet
194. **Numpy Core Architecture And Ndarray**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Python Lists vs NumPy `ndarray`
        - Array Strides
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why are NumPy `ndarray` operations significantly faster than standard Python list comprehensions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
195. **Vectorization Slicing And Broadcasting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - NumPy Broadcasting Rules
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the two conditions under which two array dimensions are compatible for NumPy broadcasting?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
196. **Pandas Dataframes Series And Ingestion**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Pandas Data Structures Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does converting string columns with low cardinality to the `category` dtype in Pandas significantly reduce memory usage?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
197. **Pandas Indexing Filtering And Imputation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `loc` vs `iloc` Indexing Mechanics
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the crucial difference between `df.loc[0:2]` and `df.iloc[0:2]` in Pandas?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
198. **Pandas Groupby Pivoting And Merging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Split-Apply-Combine Pattern
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `transform()` and `agg()` when performing a `groupby()` in Pandas?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 3.2. Module 2 — Remote Collaboration

1. **Remote Repositories & Origin Config**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Visual Architecture Diagram
        - What is a Remote?
        - Git vs. Hosting Platforms
        - Clone vs. Fork
        - origin vs. upstream
        - Remote-Tracking Branches
        - HTTPS vs. SSH
    3. Practical Code Examples
        - Remote Command Cheat Sheet
        - Example A: Managing Multiple Remotes in Enterprise Environment
        - Example B: Renaming and Inspecting Remotes
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - E2E Remote Association Workflow
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
2. **Syncing Data: Fetch, Pull & Push**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Fetch vs. Pull Architecture Diagram
        - Fetch vs. Pull Comparison
        - git pull: Merge vs. Rebase
        - Ahead and Behind Tracking States
    3. Practical Code Examples
        - Syncing Commands Cheat Sheet
        - Example A: Pulling with Rebase
        - Example B: Pushing and linking branch
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Rejected Push
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
3. **Forking & Upstream Workflows**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - The Forking Workflow Diagram
        - Fork vs. Clone vs. Branch
        - origin vs. upstream
        - Pull Requests (PR) vs. Merge Requests (MR)
        - Merge vs. Rebase in Workflows
    3. Practical Code Examples
        - Remote Fork Commands Cheat Sheet
        - Example A: Full Open-Source Contribution Workflow
        - Example B: Syncing your Local Fork
        - Example C: Rebasing feature branches
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - GitHub Feature Lifecycle Flow
    5. Workout Answers & Solutions
        - Pull Request Best Practices
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

#### 3.3. Module 3 — Branching & Merging

1. **Branching Basics & Conflict Resolution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Branch Visualization Diagrams
        - Merging Strategies (FF vs. 3-Way)
        - Why Merge Conflicts Occur
        - Tagging Releases (Lightweight vs. Annotated)
    3. Practical Code Examples
        - Branch Command Cheat Sheet
        - Merge Command Cheat Sheet
        - Example A: Resolving Conflicts with git status Checks
        - Example B: Tagging and Remote Operations
        - Example C: Realistic Feature Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Standard Branch Naming Conventions
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
2. **Merge Conflict Handling in Teams**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Conflict Visualization Diagram
        - Conflict Resolution Workflow
        - Merge vs. Rebase Conflicts
        - Conflict Markers Decoded
        - HEAD vs. Theirs Pointer Reference Map
        - Conflict Types
    3. Practical Code Examples
        - Conflict Commands Cheat Sheet
        - Example A: Managing conflict status
        - Example B: Visual merge tools setup
        - Example C: Practical Team Resolution Workflow
        - Advanced Tip: `git rerere`
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge: Resolving Worksheets
        - Conflict Prevention Workflow Diagram
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

#### 3.4. Module 4 — Troubleshooting

1. **Diagnostic & Troubleshooting Guide**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Common Git Troubleshooting Scenarios
        - Scenario 1: Detached HEAD State
        - Scenario 2: Recovering Lost Commits (Reflog)
        - Scenario 3: Committed on the Wrong Branch
        - Scenario 4: Stuck Merge or Rebase
        - Scenario 5: Force Push Recovery
    3. Practical Code Examples
        - Diagnostic Commands Cheat Sheet
        - Example A: Finding lost commits using `git fsck`
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Wrong branch commit
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

#### 3.5. Module 5 — Automation & Security

1. **Git Customization: Hooks & Aliases**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Git Hook Lifecycle Diagrams
        - Client-side vs. Server-side Hooks
        - Why Hooks Exist
        - Git Hook Trigger Reference
        - Modern SaaS Hosting Realities
    3. Practical Code Examples
        - Hook & Alias Cheat Sheet
        - Common Git Aliases
        - Example A: Enterprise Pre-commit Pipeline
        - Example B: Portable pre-commit hook (POSIX sh)
        - Example C: Robust commit-msg message parsing (Bash)
    4. Hands-on Workouts
        - MCQ
        - Hook Distribution Strategies
    5. Workout Answers & Solutions
        - Common Mistakes
        - Enterprise Best Practices
        - Key Takeaways
2. **Credential Management & Security**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - HTTPS vs. SSH Authentication
        - Credential Helpers
        - SSH Key Setup Overview
    3. Practical Code Examples
        - Credential Config Cheat Sheet
        - Example A: Setting Up SSH Authentication
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Token Expiration
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

#### 3.6. Module 6 — Advanced Workflows

1. **Rewriting History: Amend, Rebase & Squash**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - History Rewriting Diagram
        - Decision Guide
        - History Rewriting Command Comparisons
        - Visualizing Interactive Rebase & Squashing
        - reflog Recovery Mechanics
    3. Practical Code Examples
        - Interactive Rebase Command Reference
        - Example A: Interactive Rebase Setup
        - Example B: Safe Force-Pushing
        - Example C: Complete Cleanup Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Undoing an amend
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
2. **Workspace Helpers: Stash, Bisect & Worktree**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
        - Workspace Helper Decision Guide
    2. Part 1: Git Stash
        - Stash Workflow
        - Stash Internals
        - Stash Commands Cheat Sheet
        - Enterprise Scenario: Stashing
    3. Part 2: Git Bisect
        - Bisect Visualization
        - Automated Bisect
        - Bisect Commands Cheat Sheet
        - Enterprise Scenario: Bisecting
    4. Part 3: Git Worktree
        - Worktree Visualization
        - Worktree vs. Clone
        - Worktree Commands Cheat Sheet
        - Enterprise Scenario: Worktrees
    5. Hands-on Workouts
        - MCQ
        - Coding Challenge
    6. Workout Answers & Solutions
        - Common Mistakes
        - Enterprise Best Practices
        - Key Takeaways
3. **Cherry-picking & Backporting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Cherry-picking Visual Diagram
        - What is Backporting?
        - Cherry-pick vs. Merge vs. Rebase
    3. Practical Code Examples
        - Cherry-pick Command Cheat Sheet
        - Example A: Cherry-picking a Hotfix
        - Example B: Handling Cherry-pick Conflicts
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Hotfixing
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
4. **Tags & Release Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Tag Types Comparison
        - Semantic Versioning (SemVer)
        - Tags vs. Releases
    3. Practical Code Examples
        - Tag Command Cheat Sheet
        - Example A: Creating and Pushing an Annotated Release Tag
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Security verification
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
5. **Branching Strategies for Teams**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Branching Strategies Comparison
        - Git Flow Branch Layout
        - Trunk-Based Development (TBD)
    3. Practical Code Examples
        - Example A: Git Flow feature release sequence
        - Example B: Git Flow hotfix release sequence
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Choosing a strategy
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

#### 3.7. Module 7 — Git Internals

1. **Git Internals: Blobs, Trees & Commits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Object Relationship Diagram
        - Object Hierarchy Flow
        - Inside the `.git` Directory
        - SHA-1 vs. SHA-256 Hashes
        - Content-Addressable Storage & Deduplication
        - Sample Commit Object Layout
        - Porcelain vs. Plumbing
    3. Practical Code Examples
        - Internal Investigation Command Reference
        - Example A: Inspecting Objects E2E
        - Example B: Tag objects vs References
        - Example C: Pack files optimization
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
    5. Workout Answers & Solutions
        - Common Mistakes
        - Enterprise Best Practices
        - Key Takeaways

#### 3.8. Module 8 — Git Foundations

1. **Git Architecture & Three States**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Git File States & Environments
        - The Lifecycle of a File
        - The State Transition Flow Connected to `git status`
        - Repository Creation Workflows
    3. Practical Code Examples
        - Step-by-Step Lab 1: First-Time Git Setup (Run Only Once)
        - Step-by-Step Lab 2: Initializing and First Staging
        - Step-by-Step Lab 3: Creating Your First Commit
    4. Hands-on Workouts
        - Checkpoint Questions
        - Try It Yourself Exercise: Selective Staging
    5. Workout Answers & Solutions
        - Checkpoint Answers
        - Solution to Try It Yourself Exercise
        - Common Beginner Mistakes
2. **Local Workflow: Init, Stage & Commit**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Git Configuration Scopes & Precedence
        - git init vs. git clone
        - Short Status Output (`git status -s`)
        - Git Ignore Filters (`.gitignore`)
    3. Practical Code Examples
        - Before You Start
        - Step-by-Step Lab 1: Configuration Scopes
        - Step-by-Step Lab 2: Cloning an Existing Repository
        - Step-by-Step Lab 3: Ignoring Cache & Temp Files
    4. Hands-on Workouts
        - Workout Exercises
    5. Workout Answers & Solutions
        - Checkpoint Questions
        - Workout Solutions
        - Summary of New Concepts
        - Next Lesson Preview
3. **Version Control History & Evolution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - The Problem: Coding Without Version Control
        - Version Control System (VCS) Evolution Timeline
        - VCS Comparison Chart
        - Why Git Was Created
        - Git vs. GitHub
        - Why Git is Fast
    3. Practical Code Examples
        - Example A: Basic Environment Checks
        - Example B: Help Document Lookup
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Collaboration without Git
    5. Workout Answers & Solutions
        - Common Problems Solved by Git
        - Why Git Won the Industry
        - Key Takeaways

#### 3.9. Module 9 — History Management

1. **Inspecting History: Log & Diff**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Visual History Diagram
        - git diff State Comparisons
        - git log Cheat Sheet
        - git diff Comparison Chart
        - Understanding Diff Output Markers
        - git show
        - Commit Hash Mechanics
    3. Practical Code Examples
        - Example A: Basic log filtering
        - Example B: Snoop searching with `git log -S`
        - Example C: Practical Investigation Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Who updated the file lines?
        - Common Investigation Commands
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
2. **Interactive Staging: Patch Mode & Partial Commits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - What is Interactive Staging?
        - Patch Mode Options Decoded
    3. Practical Code Examples
        - Interactive Staging Cheat Sheet
        - Example A: Running an Interactive Staging Session
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Unrelated modifications
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
3. **Undoing Changes: Reset, Restore & Revert**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
        - Undo Action Decision Flow
    2. Definitions & Core Concepts
        - Command Comparisons
        - Visual Explanation of `git reset` Modes
        - Detached HEAD
        - git log vs. git reflog
    3. Practical Code Examples
        - Example A: git restore Variations
        - Example B: Detached HEAD branch creation
        - Example C: Realistic Recovery Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - When Should I Use... Reference Box
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
### 4. Git

#### 4.1. Module 1 — Core Concepts and Workflows

1. **Git Architecture & Three States**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Git File States & Environments
        - The Lifecycle of a File
        - The State Transition Flow Connected to `git status`
        - Repository Creation Workflows
    3. Practical Code Examples
        - Step-by-Step Lab 1: First-Time Git Setup (Run Only Once)
        - Step-by-Step Lab 2: Initializing and First Staging
        - Step-by-Step Lab 3: Creating Your First Commit
    4. Hands-on Workouts
        - Checkpoint Questions
        - Try It Yourself Exercise: Selective Staging
    5. Workout Answers & Solutions
        - Checkpoint Answers
        - Solution to Try It Yourself Exercise
        - Common Beginner Mistakes
2. **Local Workflow: Init, Stage & Commit**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Git Configuration Scopes & Precedence
        - git init vs. git clone
        - Short Status Output (`git status -s`)
        - Git Ignore Filters (`.gitignore`)
    3. Practical Code Examples
        - Before You Start
        - Step-by-Step Lab 1: Configuration Scopes
        - Step-by-Step Lab 2: Cloning an Existing Repository
        - Step-by-Step Lab 3: Ignoring Cache & Temp Files
    4. Hands-on Workouts
        - Workout Exercises
    5. Workout Answers & Solutions
        - Checkpoint Questions
        - Workout Solutions
        - Summary of New Concepts
        - Next Lesson Preview
3. **Inspecting History: Log & Diff**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Visual History Diagram
        - git diff State Comparisons
        - git log Cheat Sheet
        - git diff Comparison Chart
        - Understanding Diff Output Markers
        - git show
        - Commit Hash Mechanics
    3. Practical Code Examples
        - Example A: Basic log filtering
        - Example B: Snoop searching with `git log -S`
        - Example C: Practical Investigation Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Who updated the file lines?
        - Common Investigation Commands
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
4. **Version Control History & Evolution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - The Problem: Coding Without Version Control
        - Version Control System (VCS) Evolution Timeline
        - VCS Comparison Chart
        - Why Git Was Created
        - Git vs. GitHub
        - Why Git is Fast
    3. Practical Code Examples
        - Example A: Basic Environment Checks
        - Example B: Help Document Lookup
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Collaboration without Git
    5. Workout Answers & Solutions
        - Common Problems Solved by Git
        - Why Git Won the Industry
        - Key Takeaways
5. **Interactive Staging: Patch Mode & Partial Commits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - What is Interactive Staging?
        - Patch Mode Options Decoded
    3. Practical Code Examples
        - Interactive Staging Cheat Sheet
        - Example A: Running an Interactive Staging Session
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Unrelated modifications
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
6. **Undoing Changes: Reset, Restore & Revert**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
        - Undo Action Decision Flow
    2. Definitions & Core Concepts
        - Command Comparisons
        - Visual Explanation of `git reset` Modes
        - Detached HEAD
        - git log vs. git reflog
    3. Practical Code Examples
        - Example A: git restore Variations
        - Example B: Detached HEAD branch creation
        - Example C: Realistic Recovery Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - When Should I Use... Reference Box
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
7. **Branching Basics & Conflict Resolution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Branch Visualization Diagrams
        - Merging Strategies (FF vs. 3-Way)
        - Why Merge Conflicts Occur
        - Tagging Releases (Lightweight vs. Annotated)
    3. Practical Code Examples
        - Branch Command Cheat Sheet
        - Merge Command Cheat Sheet
        - Example A: Resolving Conflicts with git status Checks
        - Example B: Tagging and Remote Operations
        - Example C: Realistic Feature Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Standard Branch Naming Conventions
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
8. **Remote Repositories & Origin Config**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Visual Architecture Diagram
        - What is a Remote?
        - Git vs. Hosting Platforms
        - Clone vs. Fork
        - origin vs. upstream
        - Remote-Tracking Branches
        - HTTPS vs. SSH
    3. Practical Code Examples
        - Remote Command Cheat Sheet
        - Example A: Managing Multiple Remotes in Enterprise Environment
        - Example B: Renaming and Inspecting Remotes
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - E2E Remote Association Workflow
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
9. **Syncing Data: Fetch, Pull & Push**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Fetch vs. Pull Architecture Diagram
        - Fetch vs. Pull Comparison
        - git pull: Merge vs. Rebase
        - Ahead and Behind Tracking States
    3. Practical Code Examples
        - Syncing Commands Cheat Sheet
        - Example A: Pulling with Rebase
        - Example B: Pushing and linking branch
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Rejected Push
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
10. **Merge Conflict Handling in Teams**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Conflict Visualization Diagram
        - Conflict Resolution Workflow
        - Merge vs. Rebase Conflicts
        - Conflict Markers Decoded
        - HEAD vs. Theirs Pointer Reference Map
        - Conflict Types
    3. Practical Code Examples
        - Conflict Commands Cheat Sheet
        - Example A: Managing conflict status
        - Example B: Visual merge tools setup
        - Example C: Practical Team Resolution Workflow
        - Advanced Tip: `git rerere`
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge: Resolving Worksheets
        - Conflict Prevention Workflow Diagram
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
11. **Forking & Upstream Workflows**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - The Forking Workflow Diagram
        - Fork vs. Clone vs. Branch
        - origin vs. upstream
        - Pull Requests (PR) vs. Merge Requests (MR)
        - Merge vs. Rebase in Workflows
    3. Practical Code Examples
        - Remote Fork Commands Cheat Sheet
        - Example A: Full Open-Source Contribution Workflow
        - Example B: Syncing your Local Fork
        - Example C: Rebasing feature branches
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - GitHub Feature Lifecycle Flow
    5. Workout Answers & Solutions
        - Pull Request Best Practices
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
12. **Git Internals: Blobs, Trees & Commits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Object Relationship Diagram
        - Object Hierarchy Flow
        - Inside the `.git` Directory
        - SHA-1 vs. SHA-256 Hashes
        - Content-Addressable Storage & Deduplication
        - Sample Commit Object Layout
        - Porcelain vs. Plumbing
    3. Practical Code Examples
        - Internal Investigation Command Reference
        - Example A: Inspecting Objects E2E
        - Example B: Tag objects vs References
        - Example C: Pack files optimization
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
    5. Workout Answers & Solutions
        - Common Mistakes
        - Enterprise Best Practices
        - Key Takeaways
13. **Rewriting History: Amend, Rebase & Squash**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - History Rewriting Diagram
        - Decision Guide
        - History Rewriting Command Comparisons
        - Visualizing Interactive Rebase & Squashing
        - reflog Recovery Mechanics
    3. Practical Code Examples
        - Interactive Rebase Command Reference
        - Example A: Interactive Rebase Setup
        - Example B: Safe Force-Pushing
        - Example C: Complete Cleanup Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Undoing an amend
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
14. **Workspace Helpers: Stash, Bisect & Worktree**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
        - Workspace Helper Decision Guide
    2. Part 1: Git Stash
        - Stash Workflow
        - Stash Internals
        - Stash Commands Cheat Sheet
        - Enterprise Scenario: Stashing
    3. Part 2: Git Bisect
        - Bisect Visualization
        - Automated Bisect
        - Bisect Commands Cheat Sheet
        - Enterprise Scenario: Bisecting
    4. Part 3: Git Worktree
        - Worktree Visualization
        - Worktree vs. Clone
        - Worktree Commands Cheat Sheet
        - Enterprise Scenario: Worktrees
    5. Hands-on Workouts
        - MCQ
        - Coding Challenge
    6. Workout Answers & Solutions
        - Common Mistakes
        - Enterprise Best Practices
        - Key Takeaways
15. **Git Customization: Hooks & Aliases**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Git Hook Lifecycle Diagrams
        - Client-side vs. Server-side Hooks
        - Why Hooks Exist
        - Git Hook Trigger Reference
        - Modern SaaS Hosting Realities
    3. Practical Code Examples
        - Hook & Alias Cheat Sheet
        - Common Git Aliases
        - Example A: Enterprise Pre-commit Pipeline
        - Example B: Portable pre-commit hook (POSIX sh)
        - Example C: Robust commit-msg message parsing (Bash)
    4. Hands-on Workouts
        - MCQ
        - Hook Distribution Strategies
    5. Workout Answers & Solutions
        - Common Mistakes
        - Enterprise Best Practices
        - Key Takeaways
16. **Cherry-picking & Backporting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Cherry-picking Visual Diagram
        - What is Backporting?
        - Cherry-pick vs. Merge vs. Rebase
    3. Practical Code Examples
        - Cherry-pick Command Cheat Sheet
        - Example A: Cherry-picking a Hotfix
        - Example B: Handling Cherry-pick Conflicts
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Hotfixing
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
17. **Tags & Release Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Tag Types Comparison
        - Semantic Versioning (SemVer)
        - Tags vs. Releases
    3. Practical Code Examples
        - Tag Command Cheat Sheet
        - Example A: Creating and Pushing an Annotated Release Tag
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Security verification
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
18. **Branching Strategies for Teams**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Branching Strategies Comparison
        - Git Flow Branch Layout
        - Trunk-Based Development (TBD)
    3. Practical Code Examples
        - Example A: Git Flow feature release sequence
        - Example B: Git Flow hotfix release sequence
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Choosing a strategy
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
19. **Credential Management & Security**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - HTTPS vs. SSH Authentication
        - Credential Helpers
        - SSH Key Setup Overview
    3. Practical Code Examples
        - Credential Config Cheat Sheet
        - Example A: Setting Up SSH Authentication
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Token Expiration
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
20. **Diagnostic & Troubleshooting Guide**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Common Git Troubleshooting Scenarios
        - Scenario 1: Detached HEAD State
        - Scenario 2: Recovering Lost Commits (Reflog)
        - Scenario 3: Committed on the Wrong Branch
        - Scenario 4: Stuck Merge or Rebase
        - Scenario 5: Force Push Recovery
    3. Practical Code Examples
        - Diagnostic Commands Cheat Sheet
        - Example A: Finding lost commits using `git fsck`
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Wrong branch commit
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

### 5. Machine Learning

#### 5.1. Module 1 — Foundations

1. **What is Machine Learning?**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **The Scikit-Learn Ecosystem**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Data Splitting and Leakage**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **The Bias-Variance Tradeoff**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **The No Free Lunch Theorem**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **ML Environment Setup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 5.2. Module 2 — Mathematics for ML

1. **Information Theory for ML**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Optimization Theory for ML**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Linear Algebra Applied in ML**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Probabilistic Foundations for ML**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 5.3. Module 3 — Data Preparation

1. **Exploratory Data Analysis**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Handling Missing Values**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Handling Outliers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Data Encoding**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Data Scaling and Normalization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Handling Class Imbalance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Data Splitting Strategies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 5.4. Module 4 — Feature Engineering

1. **Feature Creation and Transformation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Feature Selection: Filter Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Feature Selection: Wrapper Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Feature Selection: Embedded Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Dimensionality Reduction**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Feature Engineering for Time Series**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Sklearn Pipelines and ColumnTransformer**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 5.5. Module 5 — Model Evaluation

1. **Regression Metrics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Classification Metrics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Cross-Validation Strategies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Hyperparameter Tuning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Calibration and Threshold Tuning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Model Comparison and Statistical Testing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 5.6. Module 6 — Supervised - Regression

1. **Simple and Multiple Linear Regression**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Polynomial Regression**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Ridge, Lasso, and Elastic Net**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Decision Tree Regression**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Random Forest and Extra Trees Regression**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Gradient Boosting Regression**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **XGBoost Regression**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **LightGBM Regression**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
9. **CatBoost Regression**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
10. **Support Vector Regression (SVR)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
11. **Bayesian Regression**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
12. **SGD and Online Learning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 5.7. Module 7 — Supervised - Classification

1. **Logistic Regression**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **K-Nearest Neighbors (KNN)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Naive Bayes Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Decision Tree Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Random Forest Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Support Vector Machine (SVM)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Perceptron and MLP Classifier**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Gradient Boosting Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
9. **XGBoost Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
10. **LightGBM Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
11. **CatBoost Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
12. **AdaBoost Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
13. **SGD and Online Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
14. **Multi-Label and Multi-Output Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 5.8. Module 8 — Unsupervised Learning

1. **K-Means Clustering**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **DBSCAN and Density-Based Clustering**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Hierarchical Clustering**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Gaussian Mixture Models (GMM)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Spectral Clustering**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **PCA Applied**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **t-SNE and UMAP Applied**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Anomaly Detection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
9. **Association Rule Mining**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
10. **Topic Modeling Classical**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 5.9. Module 9 — Semi-Supervised Learning

1. **Semi-Supervised Learning Foundations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Self-Training**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Label Propagation and Spreading**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Generative Semi-Supervised Models**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 5.10. Module 10 — Reinforcement Learning

1. **RL Foundations and MDP**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Dynamic Programming Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Q-Learning and SARSA**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Multi-Armed Bandit**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Gymnasium and Stable-Baselines3**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 5.11. Module 11 — Ensemble Learning

1. **Bagging and Random Subspaces**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Boosting AdaBoost and Gradient Boosting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **XGBoost LightGBM CatBoost Deep Dive**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Stacking and Blending**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Voting Ensembles**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Cascade Ensembles**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Ensemble Competition Strategies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 5.12. Module 12 — Explainable AI

1. **Explainability Foundations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **SHAP Explainability**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **LIME Explainability**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Permutation and Partial Dependence**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Counterfactual Explanations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Model Cards and AI Transparency**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 5.13. Module 13 — AutoML

1. **AutoML Foundations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Auto-Sklearn**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **FLAML and AutoGluon**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Optuna Hyperparameter Optimization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Feature Engineering Automation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 5.14. Module 14 — MLOps for ML

1. **Experiment Tracking with MLflow**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Data Versioning with DVC**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Model Serialization and Persistence**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Sklearn Pipelines for Production**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Model Serving with FastAPI**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Model Monitoring and Drift Detection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **CI/CD for ML Models**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Feature Stores**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 5.15. Module 15 — Industry Projects

1. **Customer Churn Prediction**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Credit Risk Scoring System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Demand Forecasting Pipeline**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Fraud Detection System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Recommendation Engine**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **IoT Anomaly Detection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

### 6. Deep Learning

#### 6.1. Module 1 — DL Foundations

1. **The Artificial Neuron and Perceptron**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Feedforward Neural Networks MLP**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Activation Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Loss Functions for Deep Learning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Backpropagation and Computational Graphs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Weight Initialization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Regularization Techniques**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Neural Network Capacity and Generalization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 6.2. Module 2 — PyTorch Framework

1. **PyTorch Tensors and Autograd**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Building Models with nn.Module**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **PyTorch Optimizers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Learning Rate Scheduling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **PyTorch Data Pipeline**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Training Loop Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Debugging and Profiling PyTorch**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Distributed Training with PyTorch**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
9. **TorchScript and Model Export**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 6.3. Module 3 — TensorFlow and Keras

1. **TensorFlow 2.x Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Keras Sequential and Functional API**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Keras Training and Callbacks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **tf.data Pipeline**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Keras Tuner and AutoKeras**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **TensorFlow SavedModel and Serving**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **TensorBoard and Experiment Tracking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 6.4. Module 4 — Training Optimization

1. **Advanced Optimizers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Learning Rate Techniques**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Batch Size and Gradient Accumulation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Mixed Precision Training**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Gradient Clipping and Stability**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Normalization Layers Deep Dive**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Data Augmentation for Deep Learning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 6.5. Module 5 — CNNs

1. **Convolution Operation and Filters**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Pooling and Spatial Reduction**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Classic CNN Architectures**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **ResNet and Skip Connections**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Efficient CNN Architectures**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Image Classification Pipeline**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Object Detection YOLO**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Object Detection Faster RCNN SSD**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
9. **Image Segmentation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
10. **Pose Estimation and Face Recognition**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
11. **Video Understanding**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 6.6. Module 6 — RNNs

1. **Vanilla RNN Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **LSTM Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **GRU Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Sequence to Sequence Models**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Attention Mechanism RNN**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **RNNs for Time Series**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Temporal Convolutional Networks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Anomaly Detection with RNNs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 6.7. Module 7 — Attention and Transformers

1. **Scaled Dot-Product Attention**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Multi-Head Attention**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Positional Encoding**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Transformer Encoder Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Transformer Decoder Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Vision Transformer ViT**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Hierarchical Vision Transformers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Efficient Attention Mechanisms**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
9. **DETR and Detection Transformers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 6.8. Module 8 — Generative Models

1. **Autoencoders**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Variational Autoencoders VAE**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **GAN Foundations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Advanced GANs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Score-Based and Flow Models**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Diffusion Models**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Text to Image Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Evaluation of Generative Models**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
9. **Generative Models for Tabular and Audio**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 6.9. Module 9 — Self-Supervised Learning

1. **Self-Supervised Learning Foundations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Contrastive Learning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Masked Autoencoders MAE**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **DINO and Self-Distillation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Clustering-Based SSL**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Multi-Modal Self-Supervised Learning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 6.10. Module 10 — Transfer Learning and Fine-Tuning

1. **Transfer Learning Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Fine-Tuning ImageNet Pretrained CNNs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Few-Shot Learning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Domain Adaptation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Knowledge Distillation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **PEFT for Vision**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Multi-Task Learning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 6.11. Module 11 — Model Compression and Deployment

1. **Quantization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Pruning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Model Distillation Applied**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **ONNX and TensorRT Deployment**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **TensorFlow Lite Edge Deployment**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Serving with Triton and FastAPI**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Benchmarking and Profiling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 6.12. Module 12 — Industry Projects

1. **Image Classification System Production**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Object Detection System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Medical Image Segmentation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Generative Image Pipeline**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Time Series Forecasting Deep Learning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Anomaly Detection Industrial IoT**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

### 7. NLP

#### 7.1. Module 1 — NLP Foundations

1. **Text Preprocessing Pipeline**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Morphological Analysis**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Statistical NLP Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Regular Expressions for NLP**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Stopwords Vocabulary Corpus Statistics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Evaluation Metrics for NLP**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **NLP Libraries Overview**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 7.2. Module 2 — Text Representation

1. **BoW and TF-IDF Applied**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Word2Vec and GloVe**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **FastText and Subword Embeddings**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Sentence and Document Embeddings**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Contextual Embeddings ELMo**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Subword Tokenization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Knowledge Graph Embeddings**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Multilingual Cross-Lingual Embeddings**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 7.3. Module 3 — Pretrained Language Models

1. **BERT Architecture and Pretraining**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **BERT Variants and Improvements**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **GPT-Style Decoder Models**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Encoder-Decoder Models T5 BART**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Efficient Transformers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Tokenizer Deep Dive**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Fine-Tuning PLMs with HuggingFace**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **PEFT LoRA Adapters Prompt Tuning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
9. **Benchmarks and Model Evaluation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 7.4. Module 4 — NLP Classification

1. **Text Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Sentiment Analysis**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Natural Language Inference**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Topic Classification and Detection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Document Classification at Scale**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Hate Speech and Content Moderation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Language Identification and Detection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 7.5. Module 5 — Sequence Labeling

1. **Named Entity Recognition**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Relation Extraction**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Part-of-Speech Tagging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Chunking and Shallow Parsing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Coreference Resolution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Event Extraction**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Biomedical NLP**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 7.6. Module 6 — Text Generation

1. **Decoding Strategies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Machine Translation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Text Summarization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Question Generation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Controlled Text Generation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Text Data Augmentation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Code Generation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Grammatical Error Correction**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 7.7. Module 7 — Information Extraction

1. **Extractive Question Answering**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Open-Domain Question Answering**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Open Information Extraction**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Document-Level Information Extraction**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Knowledge Base Population**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Fact Verification and Claim Detection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 7.8. Module 8 — Text Retrieval

1. **Sparse Retrieval BM25 TF-IDF**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Dense Retrieval**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Hybrid Retrieval**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Neural Re-Ranking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Semantic Search Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Question Answering over Documents**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Passage and Paragraph Retrieval**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 7.9. Module 9 — Conversational AI

1. **Dialogue Systems Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Intent Classification and Slot Filling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Dialogue State Tracking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Response Generation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Task-Oriented Bot with Rasa**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Evaluation of Conversational Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Conversational AI with LLMs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 7.10. Module 10 — Industry Projects

1. **Multi-Class News Classification API**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **NER and RE Pipeline for Financial Docs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Multilingual Customer Support Bot**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Semantic Search Engine for Research Papers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Abstractive Summarization Service**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **End-to-End Document QA System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

### 8. Computer Vision

#### 8.1. Module 1 — CV Foundations

1. **Digital Image Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Image Transformations and Filtering**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Feature Detection and Descriptors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Image Segmentation Classical**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Optical Flow and Motion Analysis**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Camera Models and Calibration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Image Quality and Preprocessing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Video Processing and Streaming**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 8.2. Module 2 — Classification and Retrieval

1. **Fine-Grained Visual Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Image Retrieval and Metric Learning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Hash-Based Image Search**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Zero-Shot and Few-Shot Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Image Anomaly Detection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Scene Classification and Understanding**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Image Deduplication and Clustering**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 8.3. Module 3 — Advanced Detection

1. **Detection Metrics and Benchmarks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Anchor-Free Detection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **YOLO Deep Dive**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Transformer-Based Detection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Multi-Scale Feature Pyramid Networks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **3D Object Detection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Rotated and Oriented Object Detection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Real-Time Detection and Edge Deployment**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 8.4. Module 4 — Advanced Segmentation

1. **Semantic Segmentation Deep Dive**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Instance Segmentation Deep Dive**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Panoptic Segmentation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Segment Anything Model SAM**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Video Object Segmentation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Medical Image Segmentation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Satellite Remote Sensing Segmentation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Depth Estimation and Scene Reconstruction**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 8.5. Module 5 — OCR and Document

1. **Text Detection in Images**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Text Recognition OCR**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **End-to-End OCR Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Document Layout Analysis**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Table Extraction and Structured Data**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Handwriting Recognition**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Visual Document Intelligence**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 8.6. Module 6 — Face Recognition

1. **Face Detection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Face Alignment and Preprocessing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Face Recognition and Verification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Person Re-Identification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Facial Attribute Analysis**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Face Generation and Manipulation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Biometric Systems Engineering**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 8.7. Module 7 — 3D Vision

1. **Point Cloud Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Point Cloud Deep Learning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Neural Radiance Fields NeRF**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **3D Gaussian Splatting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Stereo Vision and Depth**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **SLAM and Localization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 8.8. Module 8 — Vision-Language Models

1. **CLIP and Zero-Shot Vision**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Image Captioning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Visual Question Answering**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Grounding and Referring Expression**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Large Vision-Language Models**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Vision-Language for Detection and Segmentation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Chart and Diagram Understanding**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Multimodal Embeddings and Search**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 8.9. Module 9 — Domain-Specific CV

1. **Medical Computer Vision**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Autonomous Driving Perception**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Industrial Quality Inspection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Retail and E-Commerce Vision**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Agricultural and Environmental CV**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Security and Surveillance Vision**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Geospatial and Remote Sensing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 8.10. Module 10 — Industry Projects

1. **Real-Time CCTV Analytics System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Document Intelligence Platform**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Face Recognition Attendance System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Medical Image Diagnosis System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Visual Search Engine**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Autonomous Inspection Robot Capstone**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

### 9. Generative AI & LLMs

#### 9.1. Module 1 — LLM Architecture

1. **Transformer Scaling Laws**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Advanced Positional Encodings**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Efficient Attention in LLMs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Mixture of Experts MoE**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **LLM Normalization and FFN Variants**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Tokenization in LLMs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **LLM Model Families**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **LLM Training Infrastructure**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 9.2. Module 2 — LLM Pretraining

1. **Pretraining Data Preparation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Causal Language Model Pretraining**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Continued Pretraining and Domain Adaptation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Training Small LLMs from Scratch**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Instruction Pretraining**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Evaluation During Pretraining**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Open Pretraining Datasets**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 9.3. Module 3 — Supervised Fine-Tuning

1. **Instruction Tuning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **SFT Data Preparation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Full Fine-Tuning with TRL**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **QLoRA Fine-Tuning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Chat Fine-Tuning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Math and Reasoning Fine-Tuning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Code Fine-Tuning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Continual and Multi-Task Fine-Tuning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 9.4. Module 4 — Alignment

1. **RLHF Overview and InstructGPT**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Reward Model Training**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **PPO Fine-Tuning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Direct Preference Optimization DPO**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **ORPO SimPO and DPO Variants**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Constitutional AI and RLAIF**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Process Reward Models**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Evaluation of Aligned Models**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 9.5. Module 5 — Prompt Engineering

1. **Prompt Engineering Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Chain-of-Thought Prompting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Structured Output and JSON Mode**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Advanced Prompting Techniques**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Prompt Optimization and AutoPrompt**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Context Window Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Prompt Security and Robustness**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 9.6. Module 6 — Multimodal LLMs

1. **Vision-Language Pretraining**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **LLaVA and Visual Instruction Tuning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Strong Open Multimodal LLMs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Multimodal Fine-Tuning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Video LLMs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Audio and Speech LLMs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Omni and Any-Modality Models**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 9.7. Module 7 — Evaluation and Safety

1. **LLM Benchmarks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **LLM-as-Judge Evaluation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Hallucination Detection and Mitigation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **LLM Safety and Red Teaming**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Bias and Fairness in LLMs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Responsible AI and Governance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **LLM Memorization and Privacy**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 9.8. Module 8 — Inference and Serving

1. **LLM Inference Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **vLLM**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Text Generation Inference TGI**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Ollama and Local Inference**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Speculative Decoding**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **LLM Batching and Scheduling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **LLM API Gateway**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 9.9. Module 9 — LLM Compression

1. **GPTQ Quantization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **AWQ Quantization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **GGUF and llama.cpp**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Knowledge Distillation for LLMs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Pruning and Sparsity in LLMs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Edge Deployment of LLMs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 9.10. Module 10 — Industry Projects

1. **Custom Chat Assistant QLoRA**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **DPO Aligned Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Code Generation Service**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Multimodal Document Analyst**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **On-Device LLM App**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **LLM Evaluation Pipeline Capstone**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

### 10. Prompt Engineering

#### 10.1. Module 1 — Foundations

1. **What is Prompt Engineering**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of What is Prompt Engineering
        - Core Concepts & Strategy
        - Example Prompt Template for What is Prompt Engineering
    2. Lab Exercise
2. **How Language Models Work**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of How Language Models Work
        - Core Concepts & Strategy
        - Example Prompt Template for How Language Models Work
    2. Lab Exercise
3. **Tokens Context and Completion**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Tokens Context and Completion
        - Core Concepts & Strategy
        - Example Prompt Template for Tokens Context and Completion
    2. Lab Exercise
4. **Prompt Components: Instruction, Context, Input, Output**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Prompt Components: Instruction, Context, Input, Output
        - Core Concepts & Strategy
        - Example Prompt Template for Prompt Components: Instruction, Context, Input, Output
    2. Lab Exercise
5. **Limits and Hallucinations in LLMs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Limits and Hallucinations in LLMs
        - Core Concepts & Strategy
        - Example Prompt Template for Limits and Hallucinations in LLMs
    2. Lab Exercise
6. **Multimodal Prompting (Vision + Audio + Text)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Multimodal Prompting (Vision + Audio + Text)
        - Core Concepts & Strategy
        - Example Prompt Template for Multimodal Prompting (Vision + Audio + Text)
    2. Lab Exercise

#### 10.2. Module 2 — Core Prompting Techniques

1. **Zero-Shot Prompting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Zero-Shot Prompting
        - Core Concepts & Strategy
        - Example Prompt Template for Zero-Shot Prompting
    2. Lab Exercise
2. **Few-Shot Prompting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Few-Shot Prompting
        - Core Concepts & Strategy
        - Example Prompt Template for Few-Shot Prompting
    2. Lab Exercise
3. **Chain-of-Thought (CoT) Prompting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Chain-of-Thought (CoT) Prompting
        - Core Concepts & Strategy
        - Example Prompt Template for Chain-of-Thought (CoT) Prompting
    2. Lab Exercise
4. **Self-Consistency Prompting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Self-Consistency Prompting
        - Core Concepts & Strategy
        - Example Prompt Template for Self-Consistency Prompting
    2. Lab Exercise
5. **Tree of Thoughts (ToT) Prompting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Tree of Thoughts (ToT) Prompting
        - Core Concepts & Strategy
        - Example Prompt Template for Tree of Thoughts (ToT) Prompting
    2. Lab Exercise
6. **Directional Stimulus Prompting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Directional Stimulus Prompting
        - Core Concepts & Strategy
        - Example Prompt Template for Directional Stimulus Prompting
    2. Lab Exercise
7. **Generated Knowledge Prompting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Generated Knowledge Prompting
        - Core Concepts & Strategy
        - Example Prompt Template for Generated Knowledge Prompting
    2. Lab Exercise
8. **Reconstructive and Refinement Prompting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Reconstructive and Refinement Prompting
        - Core Concepts & Strategy
        - Example Prompt Template for Reconstructive and Refinement Prompting
    2. Lab Exercise

#### 10.3. Module 3 — Advanced Prompt Structures

1. **Persona and Role Prompting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Persona and Role Prompting
        - Core Concepts & Strategy
        - Example Prompt Template for Persona and Role Prompting
    2. Lab Exercise
2. **System Prompts and Developer Messages**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of System Prompts and Developer Messages
        - Core Concepts & Strategy
        - Example Prompt Template for System Prompts and Developer Messages
    2. Lab Exercise
3. **Structured Outputs (JSON, XML, Markdown)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Structured Outputs (JSON, XML, Markdown)
        - Core Concepts & Strategy
        - Example Prompt Template for Structured Outputs (JSON, XML, Markdown)
    2. Lab Exercise
4. **Prompt Chaining and Sequential Workflows**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Prompt Chaining and Sequential Workflows
        - Core Concepts & Strategy
        - Example Prompt Template for Prompt Chaining and Sequential Workflows
    2. Lab Exercise
5. **Metaprompting and Auto-Prompting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Metaprompting and Auto-Prompting
        - Core Concepts & Strategy
        - Example Prompt Template for Metaprompting and Auto-Prompting
    2. Lab Exercise
6. **Constraining and Guardrailing Prompts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Constraining and Guardrailing Prompts
        - Core Concepts & Strategy
        - Example Prompt Template for Constraining and Guardrailing Prompts
    2. Lab Exercise
7. **Multilingual and Cross-Lingual Prompting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Multilingual and Cross-Lingual Prompting
        - Core Concepts & Strategy
        - Example Prompt Template for Multilingual and Cross-Lingual Prompting
    2. Lab Exercise

#### 10.4. Module 4 — Domain Specific Applications

1. **Code Generation and Debugging Prompts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Code Generation and Debugging Prompts
        - Core Concepts & Strategy
        - Example Prompt Template for Code Generation and Debugging Prompts
    2. Lab Exercise
2. **Data Extraction and Formatting Prompts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Data Extraction and Formatting Prompts
        - Core Concepts & Strategy
        - Example Prompt Template for Data Extraction and Formatting Prompts
    2. Lab Exercise
3. **Summarization and Synthesis Prompts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Summarization and Synthesis Prompts
        - Core Concepts & Strategy
        - Example Prompt Template for Summarization and Synthesis Prompts
    2. Lab Exercise
4. **Creative Writing and Brainstorming Prompts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Creative Writing and Brainstorming Prompts
        - Core Concepts & Strategy
        - Example Prompt Template for Creative Writing and Brainstorming Prompts
    2. Lab Exercise
5. **Question Answering and Search Prompts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Question Answering and Search Prompts
        - Core Concepts & Strategy
        - Example Prompt Template for Question Answering and Search Prompts
    2. Lab Exercise
6. **Synthetic Data Generation via Prompts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Synthetic Data Generation via Prompts
        - Core Concepts & Strategy
        - Example Prompt Template for Synthetic Data Generation via Prompts
    2. Lab Exercise

#### 10.5. Module 5 — Security and Vulnerabilities

1. **Prompt Security and Injection Attacks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Prompt Security and Injection Attacks
        - Core Concepts & Strategy
        - Example Prompt Template for Prompt Security and Injection Attacks
    2. Lab Exercise
2. **Jailbreaking Techniques and Defenses**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Jailbreaking Techniques and Defenses
        - Core Concepts & Strategy
        - Example Prompt Template for Jailbreaking Techniques and Defenses
    2. Lab Exercise
3. **Data Leakage and Privacy Protection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Data Leakage and Privacy Protection
        - Core Concepts & Strategy
        - Example Prompt Template for Data Leakage and Privacy Protection
    2. Lab Exercise
4. **Adversarial Prompting and Robustness**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Adversarial Prompting and Robustness
        - Core Concepts & Strategy
        - Example Prompt Template for Adversarial Prompting and Robustness
    2. Lab Exercise

#### 10.6. Module 6 — Evaluation and Optimization

1. **Evaluating Prompt Performance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Evaluating Prompt Performance
        - Core Concepts & Strategy
        - Example Prompt Template for Evaluating Prompt Performance
    2. Lab Exercise
2. **A/B Testing and Benchmark Prompts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of A/B Testing and Benchmark Prompts
        - Core Concepts & Strategy
        - Example Prompt Template for A/B Testing and Benchmark Prompts
    2. Lab Exercise
3. **Token Optimization and Cost Reduction**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Token Optimization and Cost Reduction
        - Core Concepts & Strategy
        - Example Prompt Template for Token Optimization and Cost Reduction
    2. Lab Exercise
4. **Automated Prompt Optimization (APO/DSPy)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Automated Prompt Optimization (APO/DSPy)
        - Core Concepts & Strategy
        - Example Prompt Template for Automated Prompt Optimization (APO/DSPy)
    2. Lab Exercise
5. **Hallucination Mitigation Techniques**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Hallucination Mitigation Techniques
        - Core Concepts & Strategy
        - Example Prompt Template for Hallucination Mitigation Techniques
    2. Lab Exercise

#### 10.7. Module 7 — Tool Integration and Frameworks

1. **OpenAI Function Calling and Tool Use**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of OpenAI Function Calling and Tool Use
        - Core Concepts & Strategy
        - Example Prompt Template for OpenAI Function Calling and Tool Use
    2. Lab Exercise
2. **Semantic Kernel and DSPy Frameworks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Semantic Kernel and DSPy Frameworks
        - Core Concepts & Strategy
        - Example Prompt Template for Semantic Kernel and DSPy Frameworks
    2. Lab Exercise
3. **Capstone Enterprise Prompt Suite**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Capstone Enterprise Prompt Suite
        - Core Concepts & Strategy
        - Example Prompt Template for Capstone Enterprise Prompt Suite
    2. Lab Exercise

### 11. RAG Engineering

#### 11.1. Module 1 — RAG Fundamentals

1. **What is RAG and Why It Matters**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Naive RAG Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **RAG Frameworks Overview**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **RAG Data Flow and Components**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **LangChain LCEL Pipeline**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 11.2. Module 2 — Document Processing

1. **Document Loaders**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Fixed-Size Chunking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Semantic and Sentence Chunking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Structure-Aware Chunking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Hierarchical Multi-Granularity Chunking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Multimodal Document Processing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Chunking Evaluation and Selection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 11.3. Module 3 — Embeddings for RAG

1. **Embedding Model Selection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Embedding APIs and Local Models**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Late Interaction Models ColBERT**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Fine-Tuning Embedding Models**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Sparse and Hybrid Embeddings**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Embedding Storage and Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 11.4. Module 4 — Vector Databases

1. **Vector Database Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **FAISS Deep Dive**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Chroma**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Qdrant**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Pinecone**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Weaviate**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Vector DB Selection and Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 11.5. Module 5 — Advanced Retrieval

1. **Hybrid Search**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **HyDE Hypothetical Document Embeddings**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Query Transformation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **RAG-Fusion**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Multi-Hop and Iterative Retrieval**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Metadata Filtering and Routing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Contextual Retrieval**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Re-Ranking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 11.6. Module 6 — Generation and Augmentation

1. **Response Synthesis Strategies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Streaming RAG**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Citations and Source Attribution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Conversational RAG with Memory**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Corrective RAG and Self-RAG**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 11.7. Module 7 — RAG Evaluation

1. **RAG Evaluation Dimensions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **RAGAS Framework**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **TruLens Evaluation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **DeepEval**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Building a RAG Test Dataset**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **RAG Experimentation and A/B Testing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 11.8. Module 8 — Production RAG

1. **Graph RAG**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Multimodal RAG**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Long Context RAG**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Agentic RAG**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **RAG Observability**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **RAG Security and Guardrails**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Scaling and Optimizing RAG**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 11.9. Module 9 — Industry Projects

1. **Enterprise Document Q&A System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Codebase Q&A Assistant**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Research Paper Assistant**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Customer Support RAG Bot**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Financial Report RAG**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **GraphRAG Knowledge Platform Capstone**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

### 12. AI Agents

#### 12.1. Module 1 — Agent Foundations

1. **What is an AI Agent**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **ReAct Agent Pattern**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Plan-and-Execute Agent**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **OpenAI Assistants API**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Agent Reasoning Strategies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Agent Prompt Engineering**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Agent Frameworks Comparison**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 12.2. Module 2 — Tool Use

1. **Function Calling Deep Dive**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Web Search Tools**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Code Execution Tools**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Database and SQL Tools**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **File System and Document Tools**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **API Integration Tools**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **RAG as a Tool**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **Tool Error Handling and Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 12.3. Module 3 — Agent Memory

1. **Memory Types in AI Agents**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Conversation Memory**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **External Long-Term Memory**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Knowledge Graph Memory**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Working Memory and Scratchpad**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Memory Evaluation and Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 12.4. Module 4 — LangGraph

1. **LangGraph Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Conditional Edges and Routing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Checkpointing and State Persistence**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Human-in-the-Loop**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **LangGraph ReAct Agent**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Subgraphs and Modular Agents**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **LangGraph Studio and Visualization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
8. **LangGraph Advanced Patterns**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 12.5. Module 5 — Multi-Agent

1. **Multi-Agent Architecture Patterns**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Supervisor Agent**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **AutoGen Multi-Agent Framework**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **CrewAI**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Agent Communication Protocols**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Collaborative and Adversarial Agents**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Multi-Agent Evaluation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 12.6. Module 6 — Specialized Agents

1. **Research Agent**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Coding Agent**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Data Analysis Agent**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Browser and Web Agent**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Computer Use Agent**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Voice and Multimodal Agents**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 12.7. Module 7 — Evaluation

1. **Agent Evaluation Framework**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Agent Benchmarks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **LangSmith Agent Evaluation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Agent Tracing and Debugging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Cost and Latency Optimization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 12.8. Module 8 — Production

1. **Deploying Agents as APIs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Agent Safety and Guardrails**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Agent Workflow Automation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Model Context Protocol MCP**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Agent Security**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 12.9. Module 9 — Industry Projects

1. **Autonomous Research Assistant**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Software Engineering Agent**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Multi-Agent Data Pipeline**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Customer Success Agent**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Agentic Content Creation Pipeline**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Enterprise AI Agent Platform Capstone**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

### 13. Docker & Containerization

#### 13.1. Module 1 — Docker Fundamentals

1. **What Is Docker and Why Containers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Installing Docker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Docker Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Running Your First Container**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Docker CLI Essentials**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 13.2. Module 2 — Docker Fundamentals

1. **Introduction to Containerization vs VMs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Introduction to Containerization vs VMs
    2. Core Concept
        - Core Concept: Introduction to Containerization vs VMs
    3. Syntax
        - Syntax: Introduction to Containerization vs VMs
    4. Example
        - Example: Introduction to Containerization vs VMs
    5. Pitfall
        - Pitfall: Introduction to Containerization vs VMs
    6. Q & A
        - Q & A: Introduction to Containerization vs VMs
2. **Installing Docker Engine & Desktop**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Installing Docker Engine & Desktop
    2. Core Concept
        - Core Concept: Installing Docker Engine & Desktop
    3. Syntax
        - Syntax: Installing Docker Engine & Desktop
    4. Example
        - Example: Installing Docker Engine & Desktop
    5. Pitfall
        - Pitfall: Installing Docker Engine & Desktop
    6. Q & A
        - Q & A: Installing Docker Engine & Desktop
3. **Docker Architecture & Daemon**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Docker Architecture & Daemon
    2. Core Concept
        - Core Concept: Docker Architecture & Daemon
    3. Syntax
        - Syntax: Docker Architecture & Daemon
    4. Example
        - Example: Docker Architecture & Daemon
    5. Pitfall
        - Pitfall: Docker Architecture & Daemon
    6. Q & A
        - Q & A: Docker Architecture & Daemon
4. **Working with Docker CLI Commands**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Working with Docker CLI Commands
    2. Core Concept
        - Core Concept: Working with Docker CLI Commands
    3. Syntax
        - Syntax: Working with Docker CLI Commands
    4. Example
        - Example: Working with Docker CLI Commands
    5. Pitfall
        - Pitfall: Working with Docker CLI Commands
    6. Q & A
        - Q & A: Working with Docker CLI Commands
5. **Understanding Docker Images & Registries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Understanding Docker Images & Registries
    2. Core Concept
        - Core Concept: Understanding Docker Images & Registries
    3. Syntax
        - Syntax: Understanding Docker Images & Registries
    4. Example
        - Example: Understanding Docker Images & Registries
    5. Pitfall
        - Pitfall: Understanding Docker Images & Registries
    6. Q & A
        - Q & A: Understanding Docker Images & Registries

#### 13.3. Module 3 — Docker Images

1. **Dockerfile Syntax**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Building Images**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Multi-Stage Builds**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Pushing to Docker Hub**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Image Best Practices**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 13.4. Module 4 — Dockerfiles & Custom Images

1. **Writing your First Dockerfile**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Writing your First Dockerfile
    2. Core Concept
        - Core Concept: Writing your First Dockerfile
    3. Syntax
        - Syntax: Writing your First Dockerfile
    4. Example
        - Example: Writing your First Dockerfile
    5. Pitfall
        - Pitfall: Writing your First Dockerfile
    6. Q & A
        - Q & A: Writing your First Dockerfile
2. **FROM, RUN, CMD, and ENTRYPOINT Directives**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: FROM, RUN, CMD, and ENTRYPOINT Directives
    2. Core Concept
        - Core Concept: FROM, RUN, CMD, and ENTRYPOINT Directives
    3. Syntax
        - Syntax: FROM, RUN, CMD, and ENTRYPOINT Directives
    4. Example
        - Example: FROM, RUN, CMD, and ENTRYPOINT Directives
    5. Pitfall
        - Pitfall: FROM, RUN, CMD, and ENTRYPOINT Directives
    6. Q & A
        - Q & A: FROM, RUN, CMD, and ENTRYPOINT Directives
3. **Managing Image Layers & Caching**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Managing Image Layers & Caching
    2. Core Concept
        - Core Concept: Managing Image Layers & Caching
    3. Syntax
        - Syntax: Managing Image Layers & Caching
    4. Example
        - Example: Managing Image Layers & Caching
    5. Pitfall
        - Pitfall: Managing Image Layers & Caching
    6. Q & A
        - Q & A: Managing Image Layers & Caching
4. **Multi-Stage Docker Builds**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Multi-Stage Docker Builds
    2. Core Concept
        - Core Concept: Multi-Stage Docker Builds
    3. Syntax
        - Syntax: Multi-Stage Docker Builds
    4. Example
        - Example: Multi-Stage Docker Builds
    5. Pitfall
        - Pitfall: Multi-Stage Docker Builds
    6. Q & A
        - Q & A: Multi-Stage Docker Builds
5. **Optimizing Dockerfile Size & Security**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Optimizing Dockerfile Size & Security
    2. Core Concept
        - Core Concept: Optimizing Dockerfile Size & Security
    3. Syntax
        - Syntax: Optimizing Dockerfile Size & Security
    4. Example
        - Example: Optimizing Dockerfile Size & Security
    5. Pitfall
        - Pitfall: Optimizing Dockerfile Size & Security
    6. Q & A
        - Q & A: Optimizing Dockerfile Size & Security

#### 13.5. Module 5 — Containers

1. **Container Lifecycle**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Port Mapping and Volumes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Environment Variables**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Container Networking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Logging and Debugging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 13.6. Module 6 — Docker Networking & Storage

1. **Docker Volumes & Bind Mounts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Docker Volumes & Bind Mounts
    2. Core Concept
        - Core Concept: Docker Volumes & Bind Mounts
    3. Syntax
        - Syntax: Docker Volumes & Bind Mounts
    4. Example
        - Example: Docker Volumes & Bind Mounts
    5. Pitfall
        - Pitfall: Docker Volumes & Bind Mounts
    6. Q & A
        - Q & A: Docker Volumes & Bind Mounts
2. **Persisting Database Data in Docker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Persisting Database Data in Docker
    2. Core Concept
        - Core Concept: Persisting Database Data in Docker
    3. Syntax
        - Syntax: Persisting Database Data in Docker
    4. Example
        - Example: Persisting Database Data in Docker
    5. Pitfall
        - Pitfall: Persisting Database Data in Docker
    6. Q & A
        - Q & A: Persisting Database Data in Docker
3. **Docker Bridge, Host, and Overlay Networks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Docker Bridge, Host, and Overlay Networks
    2. Core Concept
        - Core Concept: Docker Bridge, Host, and Overlay Networks
    3. Syntax
        - Syntax: Docker Bridge, Host, and Overlay Networks
    4. Example
        - Example: Docker Bridge, Host, and Overlay Networks
    5. Pitfall
        - Pitfall: Docker Bridge, Host, and Overlay Networks
    6. Q & A
        - Q & A: Docker Bridge, Host, and Overlay Networks
4. **Container Port Mapping & Communication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Container Port Mapping & Communication
    2. Core Concept
        - Core Concept: Container Port Mapping & Communication
    3. Syntax
        - Syntax: Container Port Mapping & Communication
    4. Example
        - Example: Container Port Mapping & Communication
    5. Pitfall
        - Pitfall: Container Port Mapping & Communication
    6. Q & A
        - Q & A: Container Port Mapping & Communication
5. **Container Inspection & Logging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Container Inspection & Logging
    2. Core Concept
        - Core Concept: Container Inspection & Logging
    3. Syntax
        - Syntax: Container Inspection & Logging
    4. Example
        - Example: Container Inspection & Logging
    5. Pitfall
        - Pitfall: Container Inspection & Logging
    6. Q & A
        - Q & A: Container Inspection & Logging

#### 13.7. Module 7 — Docker Compose

1. **Docker Compose Overview**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Writing docker-compose.yml**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Multi-Service Applications**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Compose Networking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Compose Commands**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 13.8. Module 8 — Multi-Container Apps with Docker Compose

1. **Introduction to docker-compose.yml**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Introduction to docker-compose.yml
    2. Core Concept
        - Core Concept: Introduction to docker-compose.yml
    3. Syntax
        - Syntax: Introduction to docker-compose.yml
    4. Example
        - Example: Introduction to docker-compose.yml
    5. Pitfall
        - Pitfall: Introduction to docker-compose.yml
    6. Q & A
        - Q & A: Introduction to docker-compose.yml
2. **Defining Services, Networks, and Volumes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Defining Services, Networks, and Volumes
    2. Core Concept
        - Core Concept: Defining Services, Networks, and Volumes
    3. Syntax
        - Syntax: Defining Services, Networks, and Volumes
    4. Example
        - Example: Defining Services, Networks, and Volumes
    5. Pitfall
        - Pitfall: Defining Services, Networks, and Volumes
    6. Q & A
        - Q & A: Defining Services, Networks, and Volumes
3. **Environment Variables & Configuration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Environment Variables & Configuration
    2. Core Concept
        - Core Concept: Environment Variables & Configuration
    3. Syntax
        - Syntax: Environment Variables & Configuration
    4. Example
        - Example: Environment Variables & Configuration
    5. Pitfall
        - Pitfall: Environment Variables & Configuration
    6. Q & A
        - Q & A: Environment Variables & Configuration
4. **Orchestrating Python Web App + Database**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Orchestrating Python Web App + Database
    2. Core Concept
        - Core Concept: Orchestrating Python Web App + Database
    3. Syntax
        - Syntax: Orchestrating Python Web App + Database
    4. Example
        - Example: Orchestrating Python Web App + Database
    5. Pitfall
        - Pitfall: Orchestrating Python Web App + Database
    6. Q & A
        - Q & A: Orchestrating Python Web App + Database
5. **Docker Compose Commands & Lifecycle**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Docker Compose Commands & Lifecycle
    2. Core Concept
        - Core Concept: Docker Compose Commands & Lifecycle
    3. Syntax
        - Syntax: Docker Compose Commands & Lifecycle
    4. Example
        - Example: Docker Compose Commands & Lifecycle
    5. Pitfall
        - Pitfall: Docker Compose Commands & Lifecycle
    6. Q & A
        - Q & A: Docker Compose Commands & Lifecycle

#### 13.9. Module 9 — Docker in Production

1. **Docker with CI/CD**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Docker Secrets and Configs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Health Checks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Resource Limits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Docker Registry Setup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 13.10. Module 10 — Production Deployment & Best Practices

1. **Docker Security & Non-Root Users**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Docker Security & Non-Root Users
    2. Core Concept
        - Core Concept: Docker Security & Non-Root Users
    3. Syntax
        - Syntax: Docker Security & Non-Root Users
    4. Example
        - Example: Docker Security & Non-Root Users
    5. Pitfall
        - Pitfall: Docker Security & Non-Root Users
    6. Q & A
        - Q & A: Docker Security & Non-Root Users
2. **Container Health Checks & Restart Policies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Container Health Checks & Restart Policies
    2. Core Concept
        - Core Concept: Container Health Checks & Restart Policies
    3. Syntax
        - Syntax: Container Health Checks & Restart Policies
    4. Example
        - Example: Container Health Checks & Restart Policies
    5. Pitfall
        - Pitfall: Container Health Checks & Restart Policies
    6. Q & A
        - Q & A: Container Health Checks & Restart Policies
3. **Pushing Images to Docker Hub & AWS ECR**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Pushing Images to Docker Hub & AWS ECR
    2. Core Concept
        - Core Concept: Pushing Images to Docker Hub & AWS ECR
    3. Syntax
        - Syntax: Pushing Images to Docker Hub & AWS ECR
    4. Example
        - Example: Pushing Images to Docker Hub & AWS ECR
    5. Pitfall
        - Pitfall: Pushing Images to Docker Hub & AWS ECR
    6. Q & A
        - Q & A: Pushing Images to Docker Hub & AWS ECR
4. **Docker Cleanup & Pruning System Resources**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Docker Cleanup & Pruning System Resources
    2. Core Concept
        - Core Concept: Docker Cleanup & Pruning System Resources
    3. Syntax
        - Syntax: Docker Cleanup & Pruning System Resources
    4. Example
        - Example: Docker Cleanup & Pruning System Resources
    5. Pitfall
        - Pitfall: Docker Cleanup & Pruning System Resources
    6. Q & A
        - Q & A: Docker Cleanup & Pruning System Resources
5. **Building a Complete Python Flask App Container Stack**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Building a Complete Python Flask App Container Stack
    2. Core Concept
        - Core Concept: Building a Complete Python Flask App Container Stack
    3. Syntax
        - Syntax: Building a Complete Python Flask App Container Stack
    4. Example
        - Example: Building a Complete Python Flask App Container Stack
    5. Pitfall
        - Pitfall: Building a Complete Python Flask App Container Stack
    6. Q & A
        - Q & A: Building a Complete Python Flask App Container Stack

### 14. Kubernetes

#### 14.1. Module 1 — Kubernetes Fundamentals

1. **What Is Kubernetes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Cluster Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **kubectl Setup and Commands**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Pods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Namespaces**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 14.2. Module 2 — Core Workloads

1. **Deployments**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Services**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **ConfigMaps and Secrets**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Persistent Volumes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **DaemonSets and StatefulSets**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 14.3. Module 3 — Networking and Ingress

1. **Kubernetes Networking Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Ingress Controller**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Network Policies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Helm Charts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Horizontal Pod Autoscaler**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 14.4. Module 4 — Production Kubernetes

1. **Resource Requests and Limits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Liveness and Readiness Probes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **RBAC**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Kubernetes on AWS EKS**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Monitoring with Prometheus and Grafana**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

### 15. MLOps & AI Deployment

#### 15.1. Module 1 — Experiment Tracking

1. **MLflow Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **MLflow Advanced Features**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Weights and Biases**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **DVC Data Version Control**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Experiment Design and Hyperparameter Tuning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Reproducibility and Experiment Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Comparing and Selecting Models**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 15.2. Module 2 — Model Packaging

1. **MLflow Model Logging and Flavors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **MLflow Model Registry**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **ONNX Model Export**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **TorchScript and TorchServe**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **BentoML**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Model Cards and Documentation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 15.3. Module 3 — ML CI/CD

1. **ML Pipeline Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **GitHub Actions for ML**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **ZenML**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Kubeflow Pipelines**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **MLflow Projects**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Continuous Training Pipelines**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Model Testing in CI**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 15.4. Module 4 — Model Serving

1. **FastAPI Model Serving**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Triton Inference Server**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Seldon Core**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **KServe**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Containerization for ML**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Kubernetes for ML Workloads**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **A/B Testing and Canary Deployments**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 15.5. Module 5 — LLM Deployment

1. **Production LLM Serving Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **vLLM Production Deployment**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Fine-Tuned Model Deployment**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Agent Deployment at Scale**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Embedding Service Deployment**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Model Versioning and Blue-Green**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Serverless ML Deployment**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 15.6. Module 6 — ML Monitoring

1. **ML Monitoring Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Data Drift Detection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Model Performance Monitoring**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **LLM Monitoring**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Evidently AI**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Prometheus and Grafana for ML**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Root Cause Analysis and Debugging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 15.7. Module 7 — Feature Stores

1. **Feature Store Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Feast Feature Store**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Apache Airflow for ML**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Prefect for ML Pipelines**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Data Validation with Great Expectations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Streaming Data Pipelines for ML**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
7. **Data Lake and Lakehouse for ML**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 15.8. Module 8 — MLOps Platforms

1. **SageMaker MLOps**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **Vertex AI MLOps**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **Azure ML**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Databricks ML**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Cost Optimization and Governance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

#### 15.9. Module 9 — Industry Projects

1. **End-to-End ML Pipeline Tabular**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
2. **LLM Fine-Tuning MLOps Pipeline**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
3. **RAG System MLOps**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
4. **Real-Time Prediction Service**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
5. **Multi-Model Serving Platform**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives
6. **Full-Stack AI System Grand Capstone**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
    2. Learning Objectives

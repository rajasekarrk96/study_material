# NLP & Generative AI Systems — Master Syllabus

**Target Role:** Generative AI Specialist / NLP Architect / LLM Engineer  
**Difficulty Level:** Advanced  
**Estimated Duration:** 110 Hours  
**Prerequisites:** deep-learning, core-python  
**Required Courses:** deep-learning, generative-ai-llms  
**Optional Courses:** rag-engineering, ai-agents  

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

### 2. NLP

#### 2.1. Module 1 — NLP Foundations

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

#### 2.2. Module 2 — Text Representation

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

#### 2.3. Module 3 — Pretrained Language Models

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

#### 2.4. Module 4 — NLP Classification

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

#### 2.5. Module 5 — Sequence Labeling

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

#### 2.6. Module 6 — Text Generation

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

#### 2.7. Module 7 — Information Extraction

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

#### 2.8. Module 8 — Text Retrieval

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

#### 2.9. Module 9 — Conversational AI

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

#### 2.10. Module 10 — Industry Projects

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

### 3. Generative AI & LLMs

#### 3.1. Module 1 — LLM Architecture

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

#### 3.2. Module 2 — LLM Pretraining

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

#### 3.3. Module 3 — Supervised Fine-Tuning

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

#### 3.4. Module 4 — Alignment

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

#### 3.5. Module 5 — Prompt Engineering

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

#### 3.6. Module 6 — Multimodal LLMs

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

#### 3.7. Module 7 — Evaluation and Safety

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

#### 3.8. Module 8 — Inference and Serving

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

#### 3.9. Module 9 — LLM Compression

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

#### 3.10. Module 10 — Industry Projects

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

### 4. Prompt Engineering

#### 4.1. Module 1 — Foundations

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

#### 4.2. Module 2 — Core Prompting Techniques

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

#### 4.3. Module 3 — Advanced Prompt Structures

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

#### 4.4. Module 4 — Domain Specific Applications

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

#### 4.5. Module 5 — Security and Vulnerabilities

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

#### 4.6. Module 6 — Evaluation and Optimization

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

#### 4.7. Module 7 — Tool Integration and Frameworks

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

### 5. RAG Engineering

#### 5.1. Module 1 — RAG Fundamentals

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

#### 5.2. Module 2 — Document Processing

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

#### 5.3. Module 3 — Embeddings for RAG

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

#### 5.4. Module 4 — Vector Databases

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

#### 5.5. Module 5 — Advanced Retrieval

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

#### 5.6. Module 6 — Generation and Augmentation

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

#### 5.7. Module 7 — RAG Evaluation

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

#### 5.8. Module 8 — Production RAG

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

#### 5.9. Module 9 — Industry Projects

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

### 6. AI Agents

#### 6.1. Module 1 — Agent Foundations

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

#### 6.2. Module 2 — Tool Use

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

#### 6.3. Module 3 — Agent Memory

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

#### 6.4. Module 4 — LangGraph

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

#### 6.5. Module 5 — Multi-Agent

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

#### 6.6. Module 6 — Specialized Agents

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

#### 6.7. Module 7 — Evaluation

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

#### 6.8. Module 8 — Production

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

#### 6.9. Module 9 — Industry Projects

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

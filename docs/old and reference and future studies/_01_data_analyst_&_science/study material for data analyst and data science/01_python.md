# Python Syllabus

This syllabus is based on the completed notes inside `_01_python`.

The Python folder uses this pattern:

- `_NN_00_*` = main teaching notebook
- `_NN_01_*` = questions notebook
- `_NN_02_*` = answers notebook

Note: `_11_` is now used for CSV, Excel, and encoding. Jupyter workflow is included at the end of `_00_`.

## 00. Environment Setup

This topic is important before starting Python practice seriously.

Topics:

- Install Python
- Check Python version
- Install VS Code
- Install Python extension in VS Code
- Install Jupyter extension in VS Code
- Install Jupyter Notebook
- Understand Jupyter Notebook workflow
- Understand code cells and Markdown cells
- Run, restart, clear, and save notebooks
- Know when to use notebooks and when to use `.py` scripts
- Understand Python interpreter
- Understand terminal and command prompt basics
- Use `pip`
- Install packages with `pip install`
- Check installed packages with `pip list`
- Upgrade packages with `pip install --upgrade`
- Create virtual environments
- Activate and deactivate virtual environments
- Understand why virtual environments are useful
- Create `requirements.txt`
- Install packages from `requirements.txt`
- Keep project dependencies organized
- Basic folder structure for Python projects

## 01. Basics, Data Types, Operators, ASCII, And Strings

Files:

- `_01_00_Basics_and_Data_Types_Operator_ASCII_String.ipynb`
- `_01_01_Basics_and_Data_Types_Operator_ASCII_String_Questions.ipynb`
- `_01_02_Basics_and_Data_Types_Operator_ASCII_String_Answers.ipynb`

Topics:

- Python introduction
- Variables and naming rules
- Dynamic typing
- `id()` and object identity basics
- Data types
- Implicit and explicit type conversion
- Operators
- Input and output
- ASCII basics
- `ord()` and `chr()`
- Strings
- Multi-line strings
- String comparison
- String iteration
- String case conversion

## 02. Control Flow

Files:

- `_02_00_Control_Flow.ipynb`
- `_02_01_Control_Flow_Questions.ipynb`
- `_02_02_Control_Flow_Answers.ipynb`

Topics:

- Boolean values
- Comparison operators
- Logical operators
- Membership operators
- Identity operators
- `if`, `elif`, and `else`
- Nested conditions
- Guard clauses
- Shorthand `if`
- `match` and `case`
- `for` loops
- `range()`
- `enumerate()`
- Dictionary iteration
- `while` loops
- `break`, `continue`, and `pass`
- Loop `else`
- Truthy and falsy values
- `any()` and `all()`
- Input validation
- Mini ATM-style examples

## 03. Data Structures

Files:

- `_03_00_Data_Structures.ipynb`
- `_03_01_Data_Structures_Questions.ipynb`
- `_03_02_Data_Structures_Answers.ipynb`

Topics:

- Choosing the correct data structure
- Lists
- Indexing and slicing
- List methods
- List comprehensions
- Tuples
- Dictionaries
- Safe dictionary access
- Dictionary iteration
- Dictionary comprehensions
- Sets
- Set operations
- Strings as sequences
- Mutability
- Aliasing and copying
- Nested data structures

## 04. Lists And Tuples

Files:

- `_04_00_Lists_and_Tuples.ipynb`
- `_04_01_Lists_and_Tuples_Questions.ipynb`
- `_04_02_Lists_and_Tuples_Answers.ipynb`

Topics:

- Creating lists
- Creating tuples
- Indexing and slicing
- List mutability
- Tuple immutability
- `append()` and `extend()`
- `insert()`, `remove()`, and `pop()`
- Sorting lists
- Tuple unpacking
- Star unpacking
- Nested lists
- List comprehensions
- Copying lists
- List and tuple operators
- Membership testing
- `enumerate()`
- `zip()`
- `min()`, `max()`, and `sum()`
- Sorting with keys
- Common mistakes and edge cases

## 05. Sets And Dictionaries

Files:

- `_05_00_Sets_and_Dictionaries.ipynb`
- `_05_01_Sets_and_Dictionaries_Questions.ipynb`
- `_05_02_Sets_and_Dictionaries_Answers.ipynb`

Topics:

- Set creation
- Set methods
- Set operators
- Union, intersection, difference, and symmetric difference
- Subset and superset checks
- Disjoint sets
- `frozenset`
- Set comprehensions
- Dictionary creation
- Dictionary access and update
- Dictionary methods
- Dictionary iteration
- Dictionary comprehensions
- Nested dictionaries
- Frequency counting
- Login-style dictionary examples
- Performance notes

## 06. Functions And Modules

Files:

- `_06_00_Functions_and_Modules.ipynb`
- `_06_01_Functions_and_Modules_Questions.ipynb`
- `_06_02_Functions_and_Modules_Answers.ipynb`

Topics:

- Defining functions
- Calling functions
- Parameters and arguments
- Return values
- `None`
- Local and global scope
- Default arguments
- Mutable default argument mistakes
- `*args`
- `**kwargs`
- Recursion
- Lambda functions
- Docstrings
- Type hints
- Higher-order functions
- Imports
- Selective imports
- Import aliases
- `__name__ == "__main__"`
- Packages
- Function mini practicals

## 07. Functional Programming

Files:

- `_07_00_Functional_Programming.ipynb`
- `_07_01_Functional_Programming_Questions.ipynb`
- `_07_02_Functional_Programming_Answers.ipynb`

Topics:

- First-class functions
- Pure functions
- Immutability mindset
- `map()`
- `filter()`
- `reduce()`
- Comprehensions vs functional tools
- `sorted()` with keys
- `zip()`
- `any()` and `all()`
- Higher-order functions
- Closures
- Data-cleaning pipelines
- Iterator pitfalls
- Generator expressions
- `sum()` with generator expressions
- Mini grading pipeline example

## 08. Classes And Objects

Files:

- `_08_00_Classes_and_Objects.ipynb`
- `_08_01_Classes_and_Objects_Questions.ipynb`
- `_08_02_Classes_and_Objects_Answers.ipynb`

Topics:

- Classes
- Objects
- `__init__`
- `self`
- Instance attributes
- Class attributes
- Instance methods
- `__str__`
- Default values
- Validation inside classes
- Common OOP mistakes
- Object-based practical examples

## 09. Advanced OOP

Files:

- `_09_00_Advanced_OOP.ipynb`
- `_09_01_Advanced_OOP_Questions.ipynb`
- `_09_02_Advanced_OOP_Answers.ipynb`

Topics:

- Inheritance
- `super()`
- Method overriding
- Polymorphism
- Dunder methods
- `__str__`
- `__add__`
- `__eq__`
- Encapsulation
- Name mangling
- `@classmethod`
- `@staticmethod`
- Abstract-style base classes
- Multiple inheritance awareness
- OOP best practices

## 10. Exceptions And File Handling

Files:

- `_10_00_Exceptions_and_File_Handling.ipynb`
- `_10_01_Exceptions_and_File_Handling_Questions.ipynb`
- `_10_02_Exceptions_and_File_Handling_Answers.ipynb`

Topics:

- Exceptions
- `try` and `except`
- Multiple exception handling
- `else`
- `finally`
- `raise`
- Custom exceptions
- File modes
- Reading files
- Writing files
- `with` statement
- File errors
- Safe parsing
- Spreadsheet and file workflow notes
- Real-world file-handling examples

## 11. CSV, Excel, And Encoding

Files:

- `_11_00_CSV_Excel_Encoding.ipynb`

Topics:

- CSV basics
- Reading CSV files with pure Python
- Writing CSV files with pure Python
- `csv.reader`
- `csv.DictReader`
- CSV headers
- `newline=""`
- Encoding basics
- `utf-8`
- `utf-8-sig`
- `latin-1`
- Encoding errors
- Excel basics
- CSV vs Excel
- Preparing for Pandas `read_csv()` and `read_excel()`

## 12. Advanced Concepts

Files:

- `_12_00_Advanced_Concepts.ipynb`
- `_12_01_Advanced_Concepts_Questions.ipynb`
- `_12_02_Advanced_Concepts_Answers.ipynb`

Topics:

- Nested functions
- Closures
- `nonlocal`
- LEGB rule
- Custom context managers
- `contextlib.contextmanager`
- Shallow copy
- Deep copy
- `@property`
- Property setters
- Descriptors
- Callable objects
- `__slots__`
- Dataclasses
- Decorator and closure practicals

## 13. Iterators And Generators

Files:

- `_13_00_Iterators_and_Generators.ipynb`
- `_13_01_Iterators_and_Generators_Questions.ipynb`
- `_13_02_Iterators_and_Generators_Answers.ipynb`

Topics:

- Iterable vs iterator
- `iter()`
- `next()`
- How `for` loops work internally
- Iterator exhaustion
- Custom iterator classes
- `yield`
- Generator functions
- Generator expressions
- Memory-efficient iteration
- `StopIteration`
- Infinite generators
- `yield from`
- `enumerate()` and `zip()`
- `send()`
- Generator return values
- Reverse iterator examples
- Batch processing
- Flattening data
- Running totals
- Streaming-style examples

## 14. Decorators

Files:

- `_14_00_Decorators.ipynb`
- `_14_01_Decorators_Questions.ipynb`
- `_14_02_Decorators_Answers.ipynb`

Topics:

- Why decorators are useful
- Functions as objects
- Manual decorator pattern
- `@` decorator syntax
- Wrappers
- `*args` and `**kwargs` in decorators
- Returning values from decorators
- `functools.wraps`
- Logging decorators
- Validation decorators
- Timing decorators
- Call-counting decorators
- Parameterized decorators
- Stacked decorators
- Access-control decorators
- Exception-handling decorators
- Caching decorators
- Built-in decorators
- Method decorators
- Decorator mistakes and edge cases

## 15. Modules And Standard Library

Files:

- `_15_00_Modules_and_Standard_Library.ipynb`
- `_15_01_Modules_and_Standard_Library_Questions.ipynb`
- `_15_02_Modules_and_Standard_Library_Answers.ipynb`

Topics:

- Modules
- Standard library
- Import styles
- `math`
- `random`
- `datetime`
- Date formatting and parsing
- `pathlib`
- `os`
- `sys`
- `json`
- `collections`
- `itertools`
- `statistics`
- `string`
- `re`
- `csv`
- `__name__ == "__main__"`
- JSON report mini example

## 16. New Python Features

Files:

- `_16_00_New_Python_Features.ipynb`
- `_16_01_New_Python_Features_Questions.ipynb`
- `_16_02_New_Python_Features_Answers.ipynb`

Topics:

- F-strings
- Expressions inside f-strings
- Numeric underscores
- Extended iterable unpacking
- Dictionary unpacking
- Dictionary merge operator `|`
- Walrus operator `:=`
- Type hints
- Modern union syntax
- Built-in generic types
- Dataclasses
- Modern `pathlib` style
- Positional-only parameters
- Keyword-only parameters
- Structural pattern matching
- Tuple patterns
- `zip(strict=True)`
- Better error messages
- Modern syntax mistakes and edge cases

## 17. Regular Expressions

Files:

- `_17_00_Regular_Expressions.ipynb`
- `_17_01_Regular_Expressions_Questions.ipynb`
- `_17_02_Regular_Expressions_Answers.ipynb`

Topics:

- `re` module
- `search()`
- `match()`
- `fullmatch()`
- `findall()`
- `finditer()`
- Character classes
- Predefined classes
- Quantifiers
- Anchors
- Alternation
- Capturing groups
- Named groups
- Greedy matching
- Lazy matching
- `sub()`
- `split()`
- Regex flags
- Escaping
- Email examples
- Phone number examples
- Regex mistakes and optimizations

## 18. Web APIs And Requests

Files:

- `_18_00_Web_APIs_and_Requests.ipynb`
- `_18_01_Web_APIs_and_Requests_Questions.ipynb`
- `_18_02_Web_APIs_and_Requests_Answers.ipynb`

Topics:

- APIs
- HTTP basics
- HTTP methods
- URLs
- Query parameters
- Headers
- JSON request bodies
- `requests`
- GET requests
- POST requests
- Status codes
- Parsing JSON responses
- Error handling
- Timeouts
- `raise_for_status()`
- Authentication basics
- Rate limits
- Pagination
- Structuring API data
- API mini practicals

## 19. Concurrency And Asyncio

Files:

- `_19_00_Concurrency_and_Asyncio.ipynb`
- `_19_01_Concurrency_and_Asyncio_Questions.ipynb`
- `_19_02_Concurrency_and_Asyncio_Answers.ipynb`

Topics:

- Concurrency vs parallelism
- Blocking vs non-blocking code
- Threading basics
- Race conditions
- Locks
- Queues
- `ThreadPoolExecutor`
- Process-based parallelism idea
- `ProcessPoolExecutor`
- `asyncio`
- Coroutines
- `await`
- `asyncio.run()`
- `asyncio.sleep()`
- `asyncio.gather()`
- Tasks
- Async queues
- Timeouts
- Cancellation
- Choosing threads vs asyncio
- Worker queue examples
- Async batch examples

## 20. Testing And Logging

Files:

- `_20_00_Testing_and_Logging.ipynb`
- `_20_01_Testing_and_Logging_Questions.ipynb`
- `_20_02_Testing_and_Logging_Answers.ipynb`

Topics:

- Why testing matters
- Manual testing vs automated testing
- Testable function design
- `assert`
- Assertion messages
- Edge-case testing
- `unittest`
- Test file organization
- Test naming
- `setUp()` and `tearDown()`
- Testing exceptions
- Testing collections
- Testing floating-point values
- Testing booleans
- `unittest.mock`
- `patch`
- `side_effect`
- Logging basics
- Logging levels
- Named loggers
- Logging exceptions
- Testing logs
- Retry-with-logging examples

## 21. SQLite3 Database Connectivity

Files:

- `_21_00_SQLite3_connectivity_python_Database.ipynb`
- `_21_01_SQLite3_connectivity_python_Database_Questions.ipynb`
- `_21_02_SQLite3_connectivity_python_Database_Answers.ipynb`

Topics:

- SQLite introduction
- `sqlite3`
- Database connections
- Cursor usage
- Creating tables
- Safe inserts
- `SELECT`
- `UPDATE`
- `DELETE`
- Transactions
- Error handling
- Constraints
- `sqlite3.Row`
- Joins
- Aggregation
- Filtering
- Helper functions
- Context manager style
- Upsert
- `LIMIT` and `OFFSET`
- Dictionary export
- SQLite best practices

## 22. MySQL Database Connectivity

Files:

- `_22_00_MySQL_connectivity_python_Database_.ipynb`
- `_22_01_MySQL_connectivity_python_Database_Questions.ipynb`
- `_22_02_MySQL_connectivity_python_Database_Answers.ipynb`

Topics:

- MySQL connector setup
- `mysql.connector`
- Connection parameters
- Connection and cursor objects
- Creating databases
- Creating tables
- Insert records
- Read records
- Update records
- Delete records
- Fetch modes
- Transactions
- Error handling
- `executemany()`
- Filtering
- Sorting
- Aggregation
- Joins
- Helper functions
- Student-management mini example

## 23. SQL Server Database Connectivity

Files:

- `_23_00_SQLServer_connectivity_python_Database_.ipynb`
- `_23_01_SQLServer_connectivity_python_Database_Questions.ipynb`
- `_23_02_SQLServer_connectivity_python_Database_Answers.ipynb`

Topics:

- SQL Server connectivity from Python
- `pyodbc`
- Connection strings
- SQL Server data types
- Cursor usage
- CRUD operations
- Transactions
- Error handling
- Stored procedure calls
- Filtering
- Sorting
- Aggregation
- Joins
- Student mini example

## 24. MongoDB Database Connectivity

Files:

- `_24_00_python_Database_MongoDB_connectivity.ipynb`
- `_24_01_Database_MongoDB_Questions.ipynb`
- `_24_02_Database_MongoDB_Answers.ipynb`

Topics:

- MongoDB model
- `pymongo`
- MongoDB URI
- `MongoClient`
- Database and collection
- Documents
- Flexible schema
- `_id`
- Insert one document
- Insert many documents
- `find_one()`
- `find()`
- Filters
- Projection
- Sorting
- Limiting
- `$set`
- `$inc`
- `$push`
- `$addToSet`
- Delete operations
- Replace operations
- Aggregation basics
- Safety practices
- Student-profile mini example
- Real-world MongoDB questions

## 25. PL/SQL And Python Database Concepts

Files:

- `_25_00_python_Database_PLSQL_connectivity.ipynb`
- `_25_01_Database_PLSQL_Questions.ipynb`
- `_25_02_Database_PLSQL_Answers.ipynb`

Topics:

- PL/SQL purpose
- Anonymous blocks
- `DECLARE`
- Variables
- Data types
- Constants
- `BEGIN` and `END`
- `DBMS_OUTPUT` concept
- Control flow
- Loops
- Procedures
- Functions
- `IN`, `OUT`, and `IN OUT`
- `SELECT INTO`
- Records
- Explicit cursors
- Cursor `FOR` loops
- Built-in exceptions
- User-defined exceptions
- `COMMIT`
- `ROLLBACK`
- Savepoints
- Triggers
- Packages
- `%TYPE`
- `%ROWTYPE`
- Bind-variable concept
- Payroll and validation examples

## Support Files

The Python folder also contains small support files used in examples:

- `numbers.txt`
- `sample_read.txt`
- `sample_output.txt`

## Final Python Learning Order

1. Environment setup
2. Basics, data types, operators, ASCII, and strings
3. Control flow
4. Data structures
5. Lists and tuples
6. Sets and dictionaries
7. Functions and modules
8. Functional programming
9. Classes and objects
10. Advanced OOP
11. Exceptions and file handling
12. CSV, Excel, and encoding
13. Advanced concepts
14. Iterators and generators
15. Decorators
16. Modules and standard library
17. New Python features
18. Regular expressions
19. Web APIs and requests
20. Concurrency and asyncio
21. Testing and logging
22. SQLite3 connectivity
23. MySQL connectivity
24. SQL Server connectivity
25. MongoDB connectivity
26. PL/SQL and database concepts

## Revision Checklist

Use this checklist after completing the Python syllabus.

Syntax:

- Can write variables, expressions, and comments correctly
- Can use strings, numbers, booleans, and type conversion
- Can use operators correctly
- Can write clean `if`, `for`, and `while` logic
- Can use `break`, `continue`, and `pass`

Data structures:

- Can use lists, tuples, sets, and dictionaries
- Can choose the correct data structure for a problem
- Can use indexing, slicing, and comprehensions
- Can handle nested structures
- Can avoid common mutability and copying mistakes

Functions and modules:

- Can write reusable functions
- Can use parameters, return values, `*args`, and `**kwargs`
- Can understand scope
- Can import modules and packages
- Can use standard library modules for real tasks

OOP:

- Can create classes and objects
- Can use `__init__`, `self`, instance attributes, and methods
- Can understand inheritance, overriding, and polymorphism
- Can use class methods and static methods
- Can understand basic dunder methods

Files and data handling:

- Can read and write text files
- Can handle file paths correctly
- Can read and write CSV files
- Can understand CSV vs Excel
- Can handle basic encoding issues
- Can use `with` for safe file handling

APIs:

- Can make GET and POST requests
- Can pass query parameters and headers
- Can read JSON responses
- Can handle status codes, timeouts, and errors
- Can understand authentication and pagination basics

Databases:

- Can connect Python with SQLite
- Can connect Python with MySQL
- Can connect Python with SQL Server
- Can understand MongoDB document operations
- Can understand PL/SQL basics
- Can perform basic CRUD operations safely
- Can use transactions where needed

Testing and logging:

- Can write basic tests with `unittest`
- Can test normal cases and edge cases
- Can test exceptions
- Can use mocks at a basic level
- Can use logging levels
- Can log errors and useful application information

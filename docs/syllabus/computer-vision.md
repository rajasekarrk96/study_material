# Computer Vision — Syllabus

## Study Flow

### 1. Python

#### 1.1. Module 1 — Setup and Overview

1. **Python Overview and Philosophy**
    1. What is Python?
    2. Python's Design Philosophy
    3. Python Versions
    4. Where Python is Used
    5. Python Interpreter Types
    6. Lab Exercise
2. **Environment Setup and Tooling**
    1. Installing Python
    2. Virtual Environments
    3. Package Management with pip
    4. Modern Tooling — uv (recommended 2024+)
    5. pyproject.toml
    6. Code Quality Tools
    7. REPL and Interactive Tools
    8. Lab Exercise
3. **CPython Architecture and Execution Model**
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
    1. Variables in Python
    2. Dynamic vs Static Typing
    3. Type Annotations (Optional Static Hints)
    4. Duck Typing
    5. Identity vs Equality
    6. Lab Exercise
2. **Built-in Primitive Data Types**
    1. Numeric Types
    2. Strings
    3. NoneType
    4. Type Conversion
    5. isinstance and type
    6. Lab Exercise
3. **Syntax Rules and Code Style**
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
    1. if / elif / else
    2. Ternary (Conditional Expression)
    3. Truthy and Falsy Values
    4. Structural Pattern Matching — match/case (3.10+)
        - Matching Sequences and Structures
        - Matching Data Classes
    5. Lab Exercise
3. **Iteration and Loop Structures**
    1. for Loops
    2. while Loops
    3. break, continue, else
    4. Advanced Iteration Patterns
    5. Lab Exercise

#### 1.5. Module 5 — Collections

1. **Lists and Sequence Operations**
    1. Lists
    2. Modifying Lists
    3. Sorting
    4. List Comprehensions
    5. Copying Lists
    6. Lab Exercise
2. **Tuples and Immutable Sequences**
    1. Tuples
    2. Why Tuples?
    3. Named Tuples
    4. typing.NamedTuple (Modern)
    5. Tuple vs List Decision
    6. Lab Exercise
3. **Dictionaries**
    1. Dictionaries
    2. CRUD Operations
    3. Iterating Dictionaries
    4. Dictionary Comprehensions
    5. Advanced Dict Types
    6. Merging Dicts (3.9+)
    7. Lab Exercise
4. **Sets and Frozensets**
    1. Sets
    2. Set Operations
    3. Modifying Sets
    4. Set Comprehensions
    5. Frozenset (Immutable Set)
    6. Practical Use Cases
    7. Lab Exercise
5. **Strings and Text Processing**
    1. String Fundamentals
    2. String Formatting
    3. Essential String Methods
    4. Multi-line and Raw Strings
    5. String Encoding
    6. textwrap for Formatting
    7. Lab Exercise
6. **Advanced Collections Module**
    1. collections.Counter
    2. collections.deque (Double-Ended Queue)
    3. heapq — Priority Queue
    4. UserDict and UserList
    5. Lab Exercise

#### 1.6. Module 6 — Async Concurrency & Type Hinting

1. **Lesson 5.1 Static Type Hinting & Mypy Validation**
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
    1. Defining Functions
    2. Parameter Types
    3. *args and **kwargs
    4. Default Argument Gotcha
    5. Return Values
    6. Higher-Order Functions
    7. Lab Exercise
2. **Functional Programming in Python**
    1. Lambda Functions
    2. map, filter, reduce
    3. functools.partial
    4. functools.lru_cache (Memoization)
    5. operator module
    6. Immutability and Pure Functions
    7. Lab Exercise
3. **List Dict Set Comprehensions**
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
    1. Closures
    2. The `nonlocal` Keyword
    3. Decorators
    4. Parametrized Decorators
    5. Stacked Decorators
    6. Practical Decorators
    7. Class-Based Decorators
    8. Lab Exercise
2. **Generators and Iterators**
    1. The Iterator Protocol
    2. Generator Functions
    3. Generator Expressions
    4. yield with send() and throw()
    5. itertools — Powerful Combinators
    6. Memory Comparison
    7. Lab Exercise

#### 1.9. Module 9 — Object-Oriented Programming

1. **Classes and Instance Mechanics**
    1. Defining a Class
    2. Properties
    3. `__slots__` — Memory Optimization
    4. Lab Exercise
2. **Inheritance and Polymorphism**
    1. Single Inheritance
    2. `super()` and `__init__`
    3. Abstract Base Classes
    4. Method Resolution Order (MRO)
    5. Mixins
    6. Lab Exercise
3. **Magic Dunder Methods**
    1. Essential Dunder Methods
    2. Container Protocol
    3. Context Manager Protocol
    4. Callable Objects `__call__`
    5. Lab Exercise
4. **Dataclasses and Protocols**
    1. @dataclass
    2. Advanced dataclass Options
    3. TypedDict
    4. Protocol (Structural Subtyping)
    5. attrs Library
    6. Lab Exercise

#### 1.10. Module 10 — Exceptions and File I/O

1. **Exception Handling**
    1. Exception Hierarchy
    2. try / except / else / finally
    3. Exception Information
    4. Raising Exceptions
    5. Custom Exceptions
    6. contextlib.suppress
    7. ExceptionGroup (Python 3.11+)
    8. Lab Exercise
2. **Context Managers**
    1. Context Manager Protocol
    2. contextlib.contextmanager
    3. Practical Examples
    4. contextlib.ExitStack
    5. Async Context Managers
    6. Lab Exercise
3. **Logging Module**
    1. Python Logging Overview
    2. Log Levels
    3. Production Logger Setup
    4. Logging Exceptions
    5. Structured Logging with structlog
    6. Lab Exercise

#### 1.11. Module 11 — File I/O and Serialisation

1. **File I/O and Paths**
    1. File Operations
    2. File Modes
    3. pathlib — Modern Path Handling
    4. CSV and JSON Files
    5. Lab Exercise
2. **Data Serialization**
    1. JSON
    2. pickle — Python Object Serialization
    3. YAML (requires PyYAML)
    4. TOML (Python 3.11+ built-in)
    5. Pydantic Serialization
    6. orjson — Fast JSON
    7. Lab Exercise

#### 1.12. Module 12 — Regular Expressions

1. **Regular Expressions**
    1. re Module Basics
    2. Regex Syntax Reference
    3. Groups and Named Groups
    4. sub and subn
    5. Compiled Patterns
    6. Lookahead and Lookbehind
    7. Lab Exercise

#### 1.13. Module 13 — s and Packages

1. **Modules and Packages**
    1. Importing Modules
    2. Module Attributes
    3. Package Structure
    4. Relative Imports
    5. sys.path and Import Resolution
    6. importlib — Dynamic Imports
    7. Lab Exercise

#### 1.14. Module 14 — Concurrency

1. **Asyncio and Async/Await**
    1. Async/Await Fundamentals
    2. Tasks — Fire and Forget
    3. Async HTTP with aiohttp
    4. asyncio Primitives
    5. Async Context Managers and Generators
    6. Lab Exercise
2. **Threading and Multiprocessing**
    1. Threading
    2. Thread Synchronization
    3. concurrent.futures — High-Level Interface
    4. multiprocessing — True Parallelism
    5. When to Use What
    6. Lab Exercise

#### 1.15. Module 15 — Scientific Python

1. **NumPy Fundamentals**
    1. NumPy Basics
    2. Indexing and Slicing
    3. Vectorized Operations (No Loops!)
    4. Broadcasting
    5. Matrix Operations
    6. Lab Exercise
2. **Pandas Fundamentals**
    1. Pandas Basics
    2. Selection and Filtering
    3. Essential Operations
    4. GroupBy
    5. Merge and Join
    6. Lab Exercise
3. **Matplotlib and Visualization**
    1. Matplotlib Basics
    2. Common Plot Types
    3. Subplots
    4. Seaborn — Statistical Plots
    5. Lab Exercise
4. **Hardware Interfacing with Python**
    1. Raspberry Pi GPIO
    2. gpiozero — Higher Level
    3. PySerial — UART Communication
    4. smbus2 — I2C Communication
    5. MicroPython
    6. Lab Exercise

#### 1.16. Module 16 — Debugging and Testing

1. **Debugging and Profiling**
    1. Python Debugger (pdb)
        - pdb Commands
    2. Profiling with cProfile
    3. timeit — Micro-Benchmarking
    4. Memory Profiling
    5. Line Profiler
    6. Lab Exercise
2. **Testing with Pytest**
    1. Pytest Basics
    2. Fixtures
    3. Parametrize
    4. Mocking
    5. Coverage
    6. Property-Based Testing with Hypothesis
    7. Lab Exercise

### 2. Machine Learning

#### 2.1. Module 1 — Foundations

1. **What is Machine Learning?**
    1. Topics Covered
    2. Learning Objectives
2. **The Scikit-Learn Ecosystem**
    1. Topics Covered
    2. Learning Objectives
3. **Data Splitting and Leakage**
    1. Topics Covered
    2. Learning Objectives
4. **The Bias-Variance Tradeoff**
    1. Topics Covered
    2. Learning Objectives
5. **The No Free Lunch Theorem**
    1. Topics Covered
    2. Learning Objectives
6. **ML Environment Setup**
    1. Topics Covered
    2. Learning Objectives

#### 2.2. Module 2 — Mathematics for ML

1. **Information Theory for ML**
    1. Topics Covered
    2. Learning Objectives
2. **Optimization Theory for ML**
    1. Topics Covered
    2. Learning Objectives
3. **Linear Algebra Applied in ML**
    1. Topics Covered
    2. Learning Objectives
4. **Probabilistic Foundations for ML**
    1. Topics Covered
    2. Learning Objectives

#### 2.3. Module 3 — Data Preparation

1. **Exploratory Data Analysis**
    1. Topics Covered
    2. Learning Objectives
2. **Handling Missing Values**
    1. Topics Covered
    2. Learning Objectives
3. **Handling Outliers**
    1. Topics Covered
    2. Learning Objectives
4. **Data Encoding**
    1. Topics Covered
    2. Learning Objectives
5. **Data Scaling and Normalization**
    1. Topics Covered
    2. Learning Objectives
6. **Handling Class Imbalance**
    1. Topics Covered
    2. Learning Objectives
7. **Data Splitting Strategies**
    1. Topics Covered
    2. Learning Objectives

#### 2.4. Module 4 — Feature Engineering

1. **Feature Creation and Transformation**
    1. Topics Covered
    2. Learning Objectives
2. **Feature Selection: Filter Methods**
    1. Topics Covered
    2. Learning Objectives
3. **Feature Selection: Wrapper Methods**
    1. Topics Covered
    2. Learning Objectives
4. **Feature Selection: Embedded Methods**
    1. Topics Covered
    2. Learning Objectives
5. **Dimensionality Reduction**
    1. Topics Covered
    2. Learning Objectives
6. **Feature Engineering for Time Series**
    1. Topics Covered
    2. Learning Objectives
7. **Sklearn Pipelines and ColumnTransformer**
    1. Topics Covered
    2. Learning Objectives

#### 2.5. Module 5 — Model Evaluation

1. **Regression Metrics**
    1. Topics Covered
    2. Learning Objectives
2. **Classification Metrics**
    1. Topics Covered
    2. Learning Objectives
3. **Cross-Validation Strategies**
    1. Topics Covered
    2. Learning Objectives
4. **Hyperparameter Tuning**
    1. Topics Covered
    2. Learning Objectives
5. **Calibration and Threshold Tuning**
    1. Topics Covered
    2. Learning Objectives
6. **Model Comparison and Statistical Testing**
    1. Topics Covered
    2. Learning Objectives

#### 2.6. Module 6 — Supervised - Regression

1. **Simple and Multiple Linear Regression**
    1. Topics Covered
    2. Learning Objectives
2. **Polynomial Regression**
    1. Topics Covered
    2. Learning Objectives
3. **Ridge, Lasso, and Elastic Net**
    1. Topics Covered
    2. Learning Objectives
4. **Decision Tree Regression**
    1. Topics Covered
    2. Learning Objectives
5. **Random Forest and Extra Trees Regression**
    1. Topics Covered
    2. Learning Objectives
6. **Gradient Boosting Regression**
    1. Topics Covered
    2. Learning Objectives
7. **XGBoost Regression**
    1. Topics Covered
    2. Learning Objectives
8. **LightGBM Regression**
    1. Topics Covered
    2. Learning Objectives
9. **CatBoost Regression**
    1. Topics Covered
    2. Learning Objectives
10. **Support Vector Regression (SVR)**
    1. Topics Covered
    2. Learning Objectives
11. **Bayesian Regression**
    1. Topics Covered
    2. Learning Objectives
12. **SGD and Online Learning**
    1. Topics Covered
    2. Learning Objectives

#### 2.7. Module 7 — Supervised - Classification

1. **Logistic Regression**
    1. Topics Covered
    2. Learning Objectives
2. **K-Nearest Neighbors (KNN)**
    1. Topics Covered
    2. Learning Objectives
3. **Naive Bayes Classification**
    1. Topics Covered
    2. Learning Objectives
4. **Decision Tree Classification**
    1. Topics Covered
    2. Learning Objectives
5. **Random Forest Classification**
    1. Topics Covered
    2. Learning Objectives
6. **Support Vector Machine (SVM)**
    1. Topics Covered
    2. Learning Objectives
7. **Perceptron and MLP Classifier**
    1. Topics Covered
    2. Learning Objectives
8. **Gradient Boosting Classification**
    1. Topics Covered
    2. Learning Objectives
9. **XGBoost Classification**
    1. Topics Covered
    2. Learning Objectives
10. **LightGBM Classification**
    1. Topics Covered
    2. Learning Objectives
11. **CatBoost Classification**
    1. Topics Covered
    2. Learning Objectives
12. **AdaBoost Classification**
    1. Topics Covered
    2. Learning Objectives
13. **SGD and Online Classification**
    1. Topics Covered
    2. Learning Objectives
14. **Multi-Label and Multi-Output Classification**
    1. Topics Covered
    2. Learning Objectives

#### 2.8. Module 8 — Unsupervised Learning

1. **K-Means Clustering**
    1. Topics Covered
    2. Learning Objectives
2. **DBSCAN and Density-Based Clustering**
    1. Topics Covered
    2. Learning Objectives
3. **Hierarchical Clustering**
    1. Topics Covered
    2. Learning Objectives
4. **Gaussian Mixture Models (GMM)**
    1. Topics Covered
    2. Learning Objectives
5. **Spectral Clustering**
    1. Topics Covered
    2. Learning Objectives
6. **PCA Applied**
    1. Topics Covered
    2. Learning Objectives
7. **t-SNE and UMAP Applied**
    1. Topics Covered
    2. Learning Objectives
8. **Anomaly Detection**
    1. Topics Covered
    2. Learning Objectives
9. **Association Rule Mining**
    1. Topics Covered
    2. Learning Objectives
10. **Topic Modeling Classical**
    1. Topics Covered
    2. Learning Objectives

#### 2.9. Module 9 — Semi-Supervised Learning

1. **Semi-Supervised Learning Foundations**
    1. Topics Covered
    2. Learning Objectives
2. **Self-Training**
    1. Topics Covered
    2. Learning Objectives
3. **Label Propagation and Spreading**
    1. Topics Covered
    2. Learning Objectives
4. **Generative Semi-Supervised Models**
    1. Topics Covered
    2. Learning Objectives

#### 2.10. Module 10 — Reinforcement Learning

1. **RL Foundations and MDP**
    1. Topics Covered
    2. Learning Objectives
2. **Dynamic Programming Methods**
    1. Topics Covered
    2. Learning Objectives
3. **Q-Learning and SARSA**
    1. Topics Covered
    2. Learning Objectives
4. **Multi-Armed Bandit**
    1. Topics Covered
    2. Learning Objectives
5. **Gymnasium and Stable-Baselines3**
    1. Topics Covered
    2. Learning Objectives

#### 2.11. Module 11 — Ensemble Learning

1. **Bagging and Random Subspaces**
    1. Topics Covered
    2. Learning Objectives
2. **Boosting AdaBoost and Gradient Boosting**
    1. Topics Covered
    2. Learning Objectives
3. **XGBoost LightGBM CatBoost Deep Dive**
    1. Topics Covered
    2. Learning Objectives
4. **Stacking and Blending**
    1. Topics Covered
    2. Learning Objectives
5. **Voting Ensembles**
    1. Topics Covered
    2. Learning Objectives
6. **Cascade Ensembles**
    1. Topics Covered
    2. Learning Objectives
7. **Ensemble Competition Strategies**
    1. Topics Covered
    2. Learning Objectives

#### 2.12. Module 12 — Explainable AI

1. **Explainability Foundations**
    1. Topics Covered
    2. Learning Objectives
2. **SHAP Explainability**
    1. Topics Covered
    2. Learning Objectives
3. **LIME Explainability**
    1. Topics Covered
    2. Learning Objectives
4. **Permutation and Partial Dependence**
    1. Topics Covered
    2. Learning Objectives
5. **Counterfactual Explanations**
    1. Topics Covered
    2. Learning Objectives
6. **Model Cards and AI Transparency**
    1. Topics Covered
    2. Learning Objectives

#### 2.13. Module 13 — AutoML

1. **AutoML Foundations**
    1. Topics Covered
    2. Learning Objectives
2. **Auto-Sklearn**
    1. Topics Covered
    2. Learning Objectives
3. **FLAML and AutoGluon**
    1. Topics Covered
    2. Learning Objectives
4. **Optuna Hyperparameter Optimization**
    1. Topics Covered
    2. Learning Objectives
5. **Feature Engineering Automation**
    1. Topics Covered
    2. Learning Objectives

#### 2.14. Module 14 — MLOps for ML

1. **Experiment Tracking with MLflow**
    1. Topics Covered
    2. Learning Objectives
2. **Data Versioning with DVC**
    1. Topics Covered
    2. Learning Objectives
3. **Model Serialization and Persistence**
    1. Topics Covered
    2. Learning Objectives
4. **Sklearn Pipelines for Production**
    1. Topics Covered
    2. Learning Objectives
5. **Model Serving with FastAPI**
    1. Topics Covered
    2. Learning Objectives
6. **Model Monitoring and Drift Detection**
    1. Topics Covered
    2. Learning Objectives
7. **CI/CD for ML Models**
    1. Topics Covered
    2. Learning Objectives
8. **Feature Stores**
    1. Topics Covered
    2. Learning Objectives

#### 2.15. Module 15 — Industry Projects

1. **Customer Churn Prediction**
    1. Topics Covered
    2. Learning Objectives
2. **Credit Risk Scoring System**
    1. Topics Covered
    2. Learning Objectives
3. **Demand Forecasting Pipeline**
    1. Topics Covered
    2. Learning Objectives
4. **Fraud Detection System**
    1. Topics Covered
    2. Learning Objectives
5. **Recommendation Engine**
    1. Topics Covered
    2. Learning Objectives
6. **IoT Anomaly Detection**
    1. Topics Covered
    2. Learning Objectives

### 3. Deep Learning

#### 3.1. Module 1 — DL Foundations

1. **The Artificial Neuron and Perceptron**
    1. Topics Covered
    2. Learning Objectives
2. **Feedforward Neural Networks MLP**
    1. Topics Covered
    2. Learning Objectives
3. **Activation Functions**
    1. Topics Covered
    2. Learning Objectives
4. **Loss Functions for Deep Learning**
    1. Topics Covered
    2. Learning Objectives
5. **Backpropagation and Computational Graphs**
    1. Topics Covered
    2. Learning Objectives
6. **Weight Initialization**
    1. Topics Covered
    2. Learning Objectives
7. **Regularization Techniques**
    1. Topics Covered
    2. Learning Objectives
8. **Neural Network Capacity and Generalization**
    1. Topics Covered
    2. Learning Objectives

#### 3.2. Module 2 — PyTorch Framework

1. **PyTorch Tensors and Autograd**
    1. Topics Covered
    2. Learning Objectives
2. **Building Models with nn.Module**
    1. Topics Covered
    2. Learning Objectives
3. **PyTorch Optimizers**
    1. Topics Covered
    2. Learning Objectives
4. **Learning Rate Scheduling**
    1. Topics Covered
    2. Learning Objectives
5. **PyTorch Data Pipeline**
    1. Topics Covered
    2. Learning Objectives
6. **Training Loop Architecture**
    1. Topics Covered
    2. Learning Objectives
7. **Debugging and Profiling PyTorch**
    1. Topics Covered
    2. Learning Objectives
8. **Distributed Training with PyTorch**
    1. Topics Covered
    2. Learning Objectives
9. **TorchScript and Model Export**
    1. Topics Covered
    2. Learning Objectives

#### 3.3. Module 3 — TensorFlow and Keras

1. **TensorFlow 2.x Architecture**
    1. Topics Covered
    2. Learning Objectives
2. **Keras Sequential and Functional API**
    1. Topics Covered
    2. Learning Objectives
3. **Keras Training and Callbacks**
    1. Topics Covered
    2. Learning Objectives
4. **tf.data Pipeline**
    1. Topics Covered
    2. Learning Objectives
5. **Keras Tuner and AutoKeras**
    1. Topics Covered
    2. Learning Objectives
6. **TensorFlow SavedModel and Serving**
    1. Topics Covered
    2. Learning Objectives
7. **TensorBoard and Experiment Tracking**
    1. Topics Covered
    2. Learning Objectives

#### 3.4. Module 4 — Training Optimization

1. **Advanced Optimizers**
    1. Topics Covered
    2. Learning Objectives
2. **Learning Rate Techniques**
    1. Topics Covered
    2. Learning Objectives
3. **Batch Size and Gradient Accumulation**
    1. Topics Covered
    2. Learning Objectives
4. **Mixed Precision Training**
    1. Topics Covered
    2. Learning Objectives
5. **Gradient Clipping and Stability**
    1. Topics Covered
    2. Learning Objectives
6. **Normalization Layers Deep Dive**
    1. Topics Covered
    2. Learning Objectives
7. **Data Augmentation for Deep Learning**
    1. Topics Covered
    2. Learning Objectives

#### 3.5. Module 5 — CNNs

1. **Convolution Operation and Filters**
    1. Topics Covered
    2. Learning Objectives
2. **Pooling and Spatial Reduction**
    1. Topics Covered
    2. Learning Objectives
3. **Classic CNN Architectures**
    1. Topics Covered
    2. Learning Objectives
4. **ResNet and Skip Connections**
    1. Topics Covered
    2. Learning Objectives
5. **Efficient CNN Architectures**
    1. Topics Covered
    2. Learning Objectives
6. **Image Classification Pipeline**
    1. Topics Covered
    2. Learning Objectives
7. **Object Detection YOLO**
    1. Topics Covered
    2. Learning Objectives
8. **Object Detection Faster RCNN SSD**
    1. Topics Covered
    2. Learning Objectives
9. **Image Segmentation**
    1. Topics Covered
    2. Learning Objectives
10. **Pose Estimation and Face Recognition**
    1. Topics Covered
    2. Learning Objectives
11. **Video Understanding**
    1. Topics Covered
    2. Learning Objectives

#### 3.6. Module 6 — RNNs

1. **Vanilla RNN Architecture**
    1. Topics Covered
    2. Learning Objectives
2. **LSTM Architecture**
    1. Topics Covered
    2. Learning Objectives
3. **GRU Architecture**
    1. Topics Covered
    2. Learning Objectives
4. **Sequence to Sequence Models**
    1. Topics Covered
    2. Learning Objectives
5. **Attention Mechanism RNN**
    1. Topics Covered
    2. Learning Objectives
6. **RNNs for Time Series**
    1. Topics Covered
    2. Learning Objectives
7. **Temporal Convolutional Networks**
    1. Topics Covered
    2. Learning Objectives
8. **Anomaly Detection with RNNs**
    1. Topics Covered
    2. Learning Objectives

#### 3.7. Module 7 — Attention and Transformers

1. **Scaled Dot-Product Attention**
    1. Topics Covered
    2. Learning Objectives
2. **Multi-Head Attention**
    1. Topics Covered
    2. Learning Objectives
3. **Positional Encoding**
    1. Topics Covered
    2. Learning Objectives
4. **Transformer Encoder Architecture**
    1. Topics Covered
    2. Learning Objectives
5. **Transformer Decoder Architecture**
    1. Topics Covered
    2. Learning Objectives
6. **Vision Transformer ViT**
    1. Topics Covered
    2. Learning Objectives
7. **Hierarchical Vision Transformers**
    1. Topics Covered
    2. Learning Objectives
8. **Efficient Attention Mechanisms**
    1. Topics Covered
    2. Learning Objectives
9. **DETR and Detection Transformers**
    1. Topics Covered
    2. Learning Objectives

#### 3.8. Module 8 — Generative Models

1. **Autoencoders**
    1. Topics Covered
    2. Learning Objectives
2. **Variational Autoencoders VAE**
    1. Topics Covered
    2. Learning Objectives
3. **GAN Foundations**
    1. Topics Covered
    2. Learning Objectives
4. **Advanced GANs**
    1. Topics Covered
    2. Learning Objectives
5. **Score-Based and Flow Models**
    1. Topics Covered
    2. Learning Objectives
6. **Diffusion Models**
    1. Topics Covered
    2. Learning Objectives
7. **Text to Image Systems**
    1. Topics Covered
    2. Learning Objectives
8. **Evaluation of Generative Models**
    1. Topics Covered
    2. Learning Objectives
9. **Generative Models for Tabular and Audio**
    1. Topics Covered
    2. Learning Objectives

#### 3.9. Module 9 — Self-Supervised Learning

1. **Self-Supervised Learning Foundations**
    1. Topics Covered
    2. Learning Objectives
2. **Contrastive Learning**
    1. Topics Covered
    2. Learning Objectives
3. **Masked Autoencoders MAE**
    1. Topics Covered
    2. Learning Objectives
4. **DINO and Self-Distillation**
    1. Topics Covered
    2. Learning Objectives
5. **Clustering-Based SSL**
    1. Topics Covered
    2. Learning Objectives
6. **Multi-Modal Self-Supervised Learning**
    1. Topics Covered
    2. Learning Objectives

#### 3.10. Module 10 — Transfer Learning and Fine-Tuning

1. **Transfer Learning Fundamentals**
    1. Topics Covered
    2. Learning Objectives
2. **Fine-Tuning ImageNet Pretrained CNNs**
    1. Topics Covered
    2. Learning Objectives
3. **Few-Shot Learning**
    1. Topics Covered
    2. Learning Objectives
4. **Domain Adaptation**
    1. Topics Covered
    2. Learning Objectives
5. **Knowledge Distillation**
    1. Topics Covered
    2. Learning Objectives
6. **PEFT for Vision**
    1. Topics Covered
    2. Learning Objectives
7. **Multi-Task Learning**
    1. Topics Covered
    2. Learning Objectives

#### 3.11. Module 11 — Model Compression and Deployment

1. **Quantization**
    1. Topics Covered
    2. Learning Objectives
2. **Pruning**
    1. Topics Covered
    2. Learning Objectives
3. **Model Distillation Applied**
    1. Topics Covered
    2. Learning Objectives
4. **ONNX and TensorRT Deployment**
    1. Topics Covered
    2. Learning Objectives
5. **TensorFlow Lite Edge Deployment**
    1. Topics Covered
    2. Learning Objectives
6. **Serving with Triton and FastAPI**
    1. Topics Covered
    2. Learning Objectives
7. **Benchmarking and Profiling**
    1. Topics Covered
    2. Learning Objectives

#### 3.12. Module 12 — Industry Projects

1. **Image Classification System Production**
    1. Topics Covered
    2. Learning Objectives
2. **Object Detection System**
    1. Topics Covered
    2. Learning Objectives
3. **Medical Image Segmentation**
    1. Topics Covered
    2. Learning Objectives
4. **Generative Image Pipeline**
    1. Topics Covered
    2. Learning Objectives
5. **Time Series Forecasting Deep Learning**
    1. Topics Covered
    2. Learning Objectives
6. **Anomaly Detection Industrial IoT**
    1. Topics Covered
    2. Learning Objectives

### 4. Computer Vision

#### 4.1. Module 1 — CV Foundations

1. **Digital Image Fundamentals**
    1. Topics Covered
    2. Learning Objectives
2. **Image Transformations and Filtering**
    1. Topics Covered
    2. Learning Objectives
3. **Feature Detection and Descriptors**
    1. Topics Covered
    2. Learning Objectives
4. **Image Segmentation Classical**
    1. Topics Covered
    2. Learning Objectives
5. **Optical Flow and Motion Analysis**
    1. Topics Covered
    2. Learning Objectives
6. **Camera Models and Calibration**
    1. Topics Covered
    2. Learning Objectives
7. **Image Quality and Preprocessing**
    1. Topics Covered
    2. Learning Objectives
8. **Video Processing and Streaming**
    1. Topics Covered
    2. Learning Objectives

#### 4.2. Module 2 — Classification and Retrieval

1. **Fine-Grained Visual Classification**
    1. Topics Covered
    2. Learning Objectives
2. **Image Retrieval and Metric Learning**
    1. Topics Covered
    2. Learning Objectives
3. **Hash-Based Image Search**
    1. Topics Covered
    2. Learning Objectives
4. **Zero-Shot and Few-Shot Classification**
    1. Topics Covered
    2. Learning Objectives
5. **Image Anomaly Detection**
    1. Topics Covered
    2. Learning Objectives
6. **Scene Classification and Understanding**
    1. Topics Covered
    2. Learning Objectives
7. **Image Deduplication and Clustering**
    1. Topics Covered
    2. Learning Objectives

#### 4.3. Module 3 — Advanced Detection

1. **Detection Metrics and Benchmarks**
    1. Topics Covered
    2. Learning Objectives
2. **Anchor-Free Detection**
    1. Topics Covered
    2. Learning Objectives
3. **YOLO Deep Dive**
    1. Topics Covered
    2. Learning Objectives
4. **Transformer-Based Detection**
    1. Topics Covered
    2. Learning Objectives
5. **Multi-Scale Feature Pyramid Networks**
    1. Topics Covered
    2. Learning Objectives
6. **3D Object Detection**
    1. Topics Covered
    2. Learning Objectives
7. **Rotated and Oriented Object Detection**
    1. Topics Covered
    2. Learning Objectives
8. **Real-Time Detection and Edge Deployment**
    1. Topics Covered
    2. Learning Objectives

#### 4.4. Module 4 — Advanced Segmentation

1. **Semantic Segmentation Deep Dive**
    1. Topics Covered
    2. Learning Objectives
2. **Instance Segmentation Deep Dive**
    1. Topics Covered
    2. Learning Objectives
3. **Panoptic Segmentation**
    1. Topics Covered
    2. Learning Objectives
4. **Segment Anything Model SAM**
    1. Topics Covered
    2. Learning Objectives
5. **Video Object Segmentation**
    1. Topics Covered
    2. Learning Objectives
6. **Medical Image Segmentation**
    1. Topics Covered
    2. Learning Objectives
7. **Satellite Remote Sensing Segmentation**
    1. Topics Covered
    2. Learning Objectives
8. **Depth Estimation and Scene Reconstruction**
    1. Topics Covered
    2. Learning Objectives

#### 4.5. Module 5 — OCR and Document

1. **Text Detection in Images**
    1. Topics Covered
    2. Learning Objectives
2. **Text Recognition OCR**
    1. Topics Covered
    2. Learning Objectives
3. **End-to-End OCR Systems**
    1. Topics Covered
    2. Learning Objectives
4. **Document Layout Analysis**
    1. Topics Covered
    2. Learning Objectives
5. **Table Extraction and Structured Data**
    1. Topics Covered
    2. Learning Objectives
6. **Handwriting Recognition**
    1. Topics Covered
    2. Learning Objectives
7. **Visual Document Intelligence**
    1. Topics Covered
    2. Learning Objectives

#### 4.6. Module 6 — Face Recognition

1. **Face Detection**
    1. Topics Covered
    2. Learning Objectives
2. **Face Alignment and Preprocessing**
    1. Topics Covered
    2. Learning Objectives
3. **Face Recognition and Verification**
    1. Topics Covered
    2. Learning Objectives
4. **Person Re-Identification**
    1. Topics Covered
    2. Learning Objectives
5. **Facial Attribute Analysis**
    1. Topics Covered
    2. Learning Objectives
6. **Face Generation and Manipulation**
    1. Topics Covered
    2. Learning Objectives
7. **Biometric Systems Engineering**
    1. Topics Covered
    2. Learning Objectives

#### 4.7. Module 7 — 3D Vision

1. **Point Cloud Fundamentals**
    1. Topics Covered
    2. Learning Objectives
2. **Point Cloud Deep Learning**
    1. Topics Covered
    2. Learning Objectives
3. **Neural Radiance Fields NeRF**
    1. Topics Covered
    2. Learning Objectives
4. **3D Gaussian Splatting**
    1. Topics Covered
    2. Learning Objectives
5. **Stereo Vision and Depth**
    1. Topics Covered
    2. Learning Objectives
6. **SLAM and Localization**
    1. Topics Covered
    2. Learning Objectives

#### 4.8. Module 8 — Vision-Language Models

1. **CLIP and Zero-Shot Vision**
    1. Topics Covered
    2. Learning Objectives
2. **Image Captioning**
    1. Topics Covered
    2. Learning Objectives
3. **Visual Question Answering**
    1. Topics Covered
    2. Learning Objectives
4. **Grounding and Referring Expression**
    1. Topics Covered
    2. Learning Objectives
5. **Large Vision-Language Models**
    1. Topics Covered
    2. Learning Objectives
6. **Vision-Language for Detection and Segmentation**
    1. Topics Covered
    2. Learning Objectives
7. **Chart and Diagram Understanding**
    1. Topics Covered
    2. Learning Objectives
8. **Multimodal Embeddings and Search**
    1. Topics Covered
    2. Learning Objectives

#### 4.9. Module 9 — Domain-Specific CV

1. **Medical Computer Vision**
    1. Topics Covered
    2. Learning Objectives
2. **Autonomous Driving Perception**
    1. Topics Covered
    2. Learning Objectives
3. **Industrial Quality Inspection**
    1. Topics Covered
    2. Learning Objectives
4. **Retail and E-Commerce Vision**
    1. Topics Covered
    2. Learning Objectives
5. **Agricultural and Environmental CV**
    1. Topics Covered
    2. Learning Objectives
6. **Security and Surveillance Vision**
    1. Topics Covered
    2. Learning Objectives
7. **Geospatial and Remote Sensing**
    1. Topics Covered
    2. Learning Objectives

#### 4.10. Module 10 — Industry Projects

1. **Real-Time CCTV Analytics System**
    1. Topics Covered
    2. Learning Objectives
2. **Document Intelligence Platform**
    1. Topics Covered
    2. Learning Objectives
3. **Face Recognition Attendance System**
    1. Topics Covered
    2. Learning Objectives
4. **Medical Image Diagnosis System**
    1. Topics Covered
    2. Learning Objectives
5. **Visual Search Engine**
    1. Topics Covered
    2. Learning Objectives
6. **Autonomous Inspection Robot Capstone**
    1. Topics Covered
    2. Learning Objectives

### 5. Computer Vision for IoT

#### 5.1. Module 1 — Edge Vision Foundations

1. **Image and Camera Fundamentals**
    1. Pixels, color spaces, resolution, frame rate, and dynamic range
    2. Lenses, focus, exposure, lighting, and field of view
    3. Camera interfaces and bandwidth constraints
2. **Edge Vision Architecture**
    1. Camera, processor, inference runtime, and communication path
    2. Edge, gateway, and cloud processing trade-offs
    3. Latency, privacy, power, memory, and thermal budgets
3. **Environment and First Capture**
    1. Python and OpenCV setup
    2. Capture images and video from a camera or file
    3. Lab: measure frame rate and image quality under varied lighting

#### 5.2. Module 2 — Image Processing and Data Pipelines

1. **Core Image Operations**
    1. Resize, crop, normalize, blur, threshold, and morphology
    2. Contours, edges, geometric transforms, and regions of interest
    3. Build a deterministic preprocessing pipeline
2. **Dataset Engineering**
    1. Image collection, annotation, and class definitions
    2. Augmentation and train-validation-test splits
    3. Prevent leakage, imbalance, and environmental bias
3. **Classical Vision**
    1. Motion detection and background subtraction
    2. Feature matching and simple tracking
    3. Lab: implement an event-triggered camera pipeline

#### 5.3. Module 3 — Vision Models for Constrained Devices

1. **Classification and Detection**
    1. CNN and transfer-learning concepts
    2. Object detection outputs, anchors, confidence, and NMS
    3. Select a model based on accuracy and resource limits
2. **Segmentation, Tracking, and OCR**
    1. Semantic segmentation and mask processing
    2. Multi-frame tracking and identity continuity
    3. OCR pipelines for labels, meters, and displays
3. **Optimization and Conversion**
    1. Quantization and input-shape trade-offs
    2. ONNX, TensorFlow Lite, and hardware-specific runtimes
    3. Lab: benchmark model size, latency, and accuracy

#### 5.4. Module 4 — Device Integration and Event Delivery

1. **Embedded and Gateway Deployment**
    1. Raspberry Pi and accelerator-assisted inference
    2. ESP32-class camera use cases and limitations
    3. Startup services, watchdogs, and offline buffering
2. **IoT Messaging and APIs**
    1. Publish detections through MQTT
    2. REST endpoints for configuration and snapshots
    3. Event schemas, timestamps, device identity, and deduplication
3. **Storage and Dashboards**
    1. Store metadata separately from image evidence
    2. Retention, compression, and upload policies
    3. Lab: build a live detection dashboard

#### 5.5. Module 5 — Security, Reliability, and Capstone

1. **Security and Privacy**
    1. Camera credentials, encryption, and signed updates
    2. Privacy masking, access control, and retention policy
    3. Adversarial inputs and tamper detection concepts
2. **Field Reliability**
    1. Lighting drift, lens obstruction, and camera movement
    2. Confidence calibration, health checks, and alert suppression
    3. Remote logs, metrics, rollback, and fleet updates
3. **Capstone: Smart Vision Node**
    1. Choose inspection, safety, occupancy, or agriculture use case
    2. Deploy real-time inference with MQTT/API integration
    3. Validate accuracy, latency, power, privacy, and failure recovery

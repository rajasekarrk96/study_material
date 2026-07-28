---
id: "02_13_01"
title: "NumPy Fundamentals"
course: "Python"
module: 13
module_title: "Scientific Python"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["numpy", "ndarray", "dtype", "shape", "reshape", "broadcasting", "vectorization", "indexing", "slicing", "ufunc", "linspace", "random"]
prerequisites: []
lab_required: true
---

# NumPy Fundamentals


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

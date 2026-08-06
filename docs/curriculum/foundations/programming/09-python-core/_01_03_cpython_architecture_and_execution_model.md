# CPython Architecture and Execution Model

> **Course**: Core Python | **Module**: Setup and Overview | **Difficulty**: intermediate

---

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

---

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

---

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

---

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

---

Python caches compiled bytecode in `__pycache__/`:
```
mymodule.cpython-312.pyc
```
- Recompiled only when source changes (mtime check)
- Safe to delete — regenerated automatically

---

1. Use `dis.dis()` to inspect a list comprehension vs. a `for` loop
2. Measure reference count changes with `sys.getrefcount()`
3. Create a circular reference and verify `gc.collect()` cleans it up

---

# Context Managers

> **Course**: Core Python | **Module**: Exceptions and File I/O | **Difficulty**: intermediate

---

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

---

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

---

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

---

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

---

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

---

1. Build a `locked_file(path)` context manager that creates a `.lock` file on entry
2. Write a `rollback_on_error(dict_)` context manager that restores dict on exception
3. Chain 3 context managers using `ExitStack`

---

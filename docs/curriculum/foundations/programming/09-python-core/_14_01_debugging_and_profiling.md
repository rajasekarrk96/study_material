# Debugging and Profiling

> **Course**: Core Python | **Module**: Debugging and Testing | **Difficulty**: intermediate

---

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

---

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

---

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

---

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

---

```bash
pip install line-profiler

# Decorate function
@profile
def slow_function():
    ...

kernprof -l -v script.py
```

---

1. Use `cProfile` to find the bottleneck in a slow data processing script
2. Profile memory usage of loading a 100MB CSV with pandas vs a generator
3. Set a conditional breakpoint in `pdb` that triggers only when `x > 100`

---

---
id: "02_12_02"
title: "Threading and Multiprocessing"
course: "Python"
module: 12
module_title: "Concurrency"
lesson: 2
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["threading", "Thread", "Lock", "RLock", "Semaphore", "Queue", "multiprocessing", "Pool", "Process", "shared-memory", "concurrent.futures", "ProcessPoolExecutor", "ThreadPoolExecutor"]
prerequisites: []
lab_required: true
---

# Threading and Multiprocessing


## Threading

```python
import threading

def download(url: str, results: list, lock: threading.Lock) -> None:
    data = fetch(url)
    with lock:   # protect shared resource
        results.append(data)

results = []
lock = threading.Lock()
threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url, results, lock))
    threads.append(t)
    t.start()

for t in threads:
    t.join()   # wait for all threads to finish
```

## Thread Synchronization

```python
# RLock — re-entrant lock (same thread can acquire multiple times)
rlock = threading.RLock()

# Semaphore — limit concurrent access
sem = threading.Semaphore(5)   # max 5 threads

# Event — signal between threads
event = threading.Event()

# Producer-Consumer with Queue
from queue import Queue

q = Queue(maxsize=100)

def producer():
    for item in data_source:
        q.put(item)   # blocks if full
    q.put(None)       # sentinel

def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        process(item)
        q.task_done()
```

## concurrent.futures — High-Level Interface

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Threading — best for I/O bound
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(fetch, url) for url in urls]
    results = [f.result() for f in futures]

# Map — simpler API
with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch, urls))

# ProcessPoolExecutor — best for CPU bound
def cpu_heavy(n: int) -> int:
    return sum(i**2 for i in range(n))

with ProcessPoolExecutor() as executor:
    results = list(executor.map(cpu_heavy, [10**6]*4))
```

## multiprocessing — True Parallelism

```python
from multiprocessing import Pool, Process, Queue, Value, Array

# Pool.map — parallel map
with Pool(processes=4) as pool:
    results = pool.map(cpu_heavy, data)

# Shared memory
counter = Value("i", 0)    # shared integer
arr = Array("d", range(10)) # shared float array

def increment(counter, lock):
    for _ in range(1000):
        with lock:
            counter.value += 1
```

## When to Use What

| Scenario | Tool |
|---|---|
| I/O bound (HTTP, files) | `asyncio` or `ThreadPoolExecutor` |
| CPU bound (compute, ML) | `ProcessPoolExecutor` or `multiprocessing` |
| Simple parallel map | `concurrent.futures.ProcessPoolExecutor` |
| Fine-grained sync | `threading` with `Lock/Event/Queue` |

## Lab Exercise
1. Download 50 images using `ThreadPoolExecutor(max_workers=10)`
2. Compute prime factors of 1000 numbers using `ProcessPoolExecutor`
3. Build a thread-safe rate limiter using `threading.Semaphore` and `time`

# Asyncio and Async/Await

> **Course**: Core Python | **Module**: Concurrency | **Difficulty**: advanced

---

```python
import asyncio

# Coroutine — defined with async def
async def greet(name: str, delay: float) -> str:
    await asyncio.sleep(delay)   # non-blocking sleep
    return f"Hello, {name}!"

# Run coroutine
result = asyncio.run(greet("Raja", 1.0))

# Multiple coroutines concurrently
async def main():
    # gather — run concurrently, wait for all
    results = await asyncio.gather(
        greet("Alice", 1.0),
        greet("Bob",   0.5),
        greet("Charlie", 1.5),
    )
    # Total time ≈ 1.5s (not 3s!)
    print(results)

asyncio.run(main())
```

---

```python
async def main():
    # Create task — schedules coroutine, doesn't await yet
    task1 = asyncio.create_task(fetch_data("url1"))
    task2 = asyncio.create_task(fetch_data("url2"))

    # Do other work while tasks run
    print("Tasks started")

    # Now wait for results
    result1 = await task1
    result2 = await task2

    # Cancel a task
    task1.cancel()
    try:
        await task1
    except asyncio.CancelledError:
        print("Task cancelled")
```

---

```python
import aiohttp

async def fetch(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.json()

async def fetch_all(urls: list[str]) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)

results = asyncio.run(fetch_all(["https://api.example.com/1",
                                  "https://api.example.com/2"]))
```

---

```python
# Semaphore — limit concurrency
sem = asyncio.Semaphore(10)  # max 10 concurrent

async def limited_fetch(url):
    async with sem:
        return await fetch(url)

# Queue — async producer/consumer
queue = asyncio.Queue(maxsize=100)

async def producer():
    for item in data:
        await queue.put(item)
    await queue.put(None)  # sentinel

async def consumer():
    while True:
        item = await queue.get()
        if item is None:
            break
        await process(item)
        queue.task_done()
```

---

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def db_connection():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()

async with db_connection() as conn:
    await conn.fetch("SELECT * FROM users")

# Async generator
async def paginate(url: str):
    page = 1
    while True:
        data = await fetch(f"{url}?page={page}")
        if not data:
            break
        for item in data:
            yield item
        page += 1

async for user in paginate("https://api.example.com/users"):
    process(user)
```

---

1. Fetch 100 URLs concurrently with `aiohttp` and `gather`, limit to 10 at a time with `Semaphore`
2. Build a producer-consumer pipeline using `asyncio.Queue`
3. Port a synchronous recursive file scanner to async using `aiofiles`

---

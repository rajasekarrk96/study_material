```yaml
schema_version: "2.0"
metadata:
  lesson_id: "PY-MOD05-LES02"
  course_slug: "course-02-python"
  course_title: "Course 2: Python 3.12+ Modern Programming"
  module_slug: "mod-05-modern-python-concurrency"
  module_title: "Module 5 - Async Concurrency & Type Hinting"
  lesson_slug: "asyncio-event-loop-and-async-await"
  lesson_title: "Lesson 5.2 Asyncio Event Loop & async/await"
  sort_order: 502

pedagogy:
  difficulty: "advanced"
  estimated_time:
    reading_minutes: 20
    practice_minutes: 25
    quiz_minutes: 10
    total_minutes: 55
  bloom_taxonomy_level: "Apply"
  xp_reward: 70

prerequisites:
  required_lesson_ids:
    - "PY-MOD05-LES01"
  required_skills:
    - "Python Functions & Static Type Hinting"

skills_acquired:
  - "Asyncio Single-Threaded Event Loop Mechanics"
  - "Coroutines Definition (`async def`) and Awaiting (`await`)"
  - "Concurrent Task Execution (`asyncio.gather` & `asyncio.TaskGroup`)"
  - "Asynchronous Context Managers (`async with`)"
  - "Non-blocking Network I/O Operations"

dependencies:
  software:
    - "VS Code"
    - "Python 3.11+"
  hardware: []

seo_and_social:
  meta_title: "Python Asyncio: Event Loop, Coroutines, TaskGroup & async/await"
  meta_description: "Master Python Asyncio: single-threaded event loop architecture, async def coroutines, await keywords, asyncio.TaskGroup, and async with."
  keywords: ["Python Asyncio", "async await", "Event Loop", "TaskGroup", "Async Coroutines", "Asynchronous I/O"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 5.2 Asyncio Event Loop & `async`/`await`

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐⭐ Advanced
- **Prerequisites**: Python Functions & Static Typing
- **XP Reward**: +70 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Explain how single-threaded cooperative multitasking operates via the **Asyncio Event Loop**.
2. Define Coroutines using `async def` and yield control using `await`.
3. Execute high-concurrency tasks in parallel using Python 3.11+ `asyncio.TaskGroup()`.
4. Implement asynchronous resource context managers (`async with`).

---

## 2. Environment & Prerequisites [id: prerequisites]

Open VS Code and write python async scripts.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 Synchronous vs Asynchronous Execution
In synchronous execution, I/O operations (network API calls, database queries) block the main execution thread. In **Asyncio**, the single-threaded **Event Loop** pauses a waiting coroutine and immediately switches to execute other ready coroutines:

```
Sync:  [Task 1 (I/O Wait...)] ──► [Task 2 (I/O Wait...)] ──► Total: 4 Seconds
Async: [Task 1 Start] ──┐
       [Task 2 Start] ──┼──► Event Loop processes both concurrently ──► Total: 2 Seconds
```

### 3.2 Python 3.11+ `TaskGroup` Architecture
`asyncio.TaskGroup()` provides exception-safe structured concurrency:

```python
async with asyncio.TaskGroup() as tg:
    task1 = tg.create_task(fetch_user(1))
    task2 = tg.create_task(fetch_user(2))
```

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    Loop[Asyncio Event Loop] --> Coro1[Coroutine 1: await fetch_api]
    Coro1 -->|Yields Control| Loop
    Loop --> Coro2[Coroutine 2: Processes DB Query]
    Coro2 -->|Yields Control| Loop
    Loop -->|API Response Ready| Coro1Resume[Resume Coroutine 1 Execution]
```

---

## 5. Code & Hardware Implementation [id: syntax]

```python
import asyncio
import time

async def fetch_telemetry_sensor(sensor_id: int, delay: float) -> dict[str, float]:
    print(f"[Sensor {sensor_id}] Fetching data...")
    await asyncio.sleep(delay)  # Non-blocking async sleep!
    print(f"[Sensor {sensor_id}] Received data.")
    return {"sensor_id": sensor_id, "reading": 24.5 + sensor_id}

async def main():
    start_time = time.perf_counter()
    
    # Python 3.11+ Structured Concurrency via TaskGroup
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(fetch_telemetry_sensor(1, 1.5))
        t2 = tg.create_task(fetch_telemetry_sensor(2, 1.0))
        t3 = tg.create_task(fetch_telemetry_sensor(3, 0.5))

    # All tasks inside TaskGroup complete here
    results = [t1.result(), t2.result(), t3.result()]
    elapsed = time.perf_counter() - start_time
    
    print("Telemetry Results:", results)
    print(f"Total Concurrency Time: {elapsed:.2f} seconds")

# Run Event Loop
asyncio.run(main())
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **FastAPI Async Web Servers**: High-throughput REST API servers utilize `async def` endpoints to handle thousands of concurrent client connections without worker thread starvation.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `async_demo.py`.
2. Run `python async_demo.py` $\to$ Verify all 3 tasks finish in ~1.5 seconds instead of 3.0 seconds!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Blocking the Event Loop** | Calling synchronous blocking I/O functions like `time.sleep()` or `requests.get()` inside coroutines. | Use non-blocking async libraries (`asyncio.sleep()`, `httpx`, `aiohttp`). |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Use `asyncio.TaskGroup()`**: Replaces legacy `asyncio.gather()` for clean exception propagation.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: Is Asyncio multi-threaded?
**Answer**: No. Asyncio runs on a single thread using cooperative multitasking. When a coroutine reaches an `await` expression, it yields control back to the central Event Loop, allowing other coroutines to execute while waiting for I/O.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 5.2 Asyncio Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "What keyword defines an asynchronous coroutine function in Python?",
      "options": ["async def", "def async", "coroutine def", "task def"],
      "correct_answer_index": 0,
      "explanation": "async def defines an asynchronous coroutine."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Build a high-performance async Web Scraper fetching 20 URLs concurrently using `httpx` and `asyncio.TaskGroup`.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What entry point starts the Asyncio Event Loop in Python 3.7+?
**Back**: `asyncio.run(main())`
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```python
asyncio.run(main())
```


---

## Existing Jupyter Notebooks

> **Note**: Comprehensive Jupyter notebooks exist for this topic in the Python study folder.
> Reference the notebooks when authoring full lesson content.
> Notebooks follow the pattern: `_NN_00_topic.ipynb` (notes), `_NN_01_topic_Questions.ipynb`, `_NN_02_topic_Answers.ipynb`

```yaml
schema_version: "2.0"
metadata:
  lesson_id: "JAVA-MOD04-LES01"
  course_slug: "course-03-java"
  course_title: "Course 3: Java 21 LTS Enterprise Development"
  module_slug: "mod-04-high-concurrency-virtual-threads"
  module_title: "Module 4 - High-Concurrency Virtual Threads & Project Loom"
  lesson_slug: "java21-virtual-threads-project-loom"
  lesson_title: "Lesson 4.1 Java 21 Virtual Threads (Project Loom)"
  sort_order: 401

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
    - "JAVA-MOD02-LES04"
  required_skills:
    - "Java Threading & Concurrency Basics"

skills_acquired:
  - "Platform Threads vs Virtual Threads Architecture"
  - "Carrier Threads & Unmounting Mechanics"
  - "High-Concurrency Execution (`Executors.newVirtualThreadPerTaskExecutor()`)"
  - "Virtual Thread Pinning Identification (`synchronized` vs `ReentrantLock`)"

dependencies:
  software:
    - "VS Code / IntelliJ IDEA"
    - "JDK 21 LTS"
  hardware: []

seo_and_social:
  meta_title: "Java 21 Virtual Threads: Project Loom, Carrier Threads & High Concurrency"
  meta_description: "Master Java 21 LTS Virtual Threads (Project Loom): lightweight threads, OS Platform Threads vs Virtual Threads, newVirtualThreadPerTaskExecutor, and avoiding pinning."
  keywords: ["Java 21 Virtual Threads", "Project Loom", "Platform Threads", "Carrier Threads", "Thread Pinning", "High Concurrency Java"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 4.1 Java 21 Virtual Threads (Project Loom)

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐⭐ Advanced
- **Prerequisites**: Java Threading Basics
- **XP Reward**: +70 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Contrast OS-managed **Platform Threads** with JVM-managed **Virtual Threads**.
2. Understand Carrier Threads, mounting, and unmounting mechanics during blocking I/O.
3. Spawn millions of concurrent virtual threads using `Executors.newVirtualThreadPerTaskExecutor()`.
4. Identify and fix **Thread Pinning** caused by legacy `synchronized` blocks.

---

## 2. Environment & Prerequisites [id: prerequisites]

Ensure JDK 21 LTS is active.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 Platform Threads vs Virtual Threads
Historically, every Java `Thread` was a 1:1 wrapper around an OS kernel thread. OS threads consume ~1MB of stack memory, limiting JVM capacity to ~5,000 concurrent threads before crashing with `OutOfMemoryError`.

**Virtual Threads (Project Loom)** are lightweight user-mode threads managed entirely by the JVM:
- **Stack Size**: Starts at bytes (grows dynamically).
- **Scale**: Millions of active virtual threads per JVM instance!
- **M:N Scheduling**: Millions of Virtual Threads are multiplexed over a small pool of OS **Carrier Threads**.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   PLATFORM THREADS VS VIRTUAL THREADS                       │
├─────────────────┬──────────────────────────────────┬────────────────────────┤
│ Metric          │ Platform Threads (OS 1:1)        │ Virtual Threads (M:N)  │
├─────────────────┼──────────────────────────────────┼────────────────────────┤
│ Memory Footprint│ ~1 MB per thread                 │ ~200 Bytes per thread  │
│ Creation Cost   │ Expensive (OS syscall)           │ Near Zero (JVM Heap)   │
│ Max Capacity    │ ~5,000 threads                   │ 1,000,000+ threads     │
│ Blocking I/O    │ Blocks OS thread                 │ Unmounts from Carrier! │
└─────────────────┴──────────────────────────────────┴────────────────────────┘
```

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    VT1[Virtual Thread 1: Blocking Database Query] -->|Unmounts from Carrier| Heap[JVM Heap Stack Storage]
    Carrier[OS Carrier Thread] -->|Executes| VT2[Virtual Thread 2: Processing REST Request]
    VT1 -->|DB Response Ready: Remounts| Carrier
```

---

## 5. Code & Hardware Implementation [id: syntax]

```java
import java.time.Duration;
import java.util.concurrent.Executors;
import java.util.stream.IntStream;

class VirtualThreadDemo {
    public static void main(String[] args) {
        long start = System.currentTimeMillis();

        // Spawn 100,000 Virtual Threads concurrently!
        try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
            IntStream.range(0, 100_000).forEach(i -> {
                executor.submit(() -> {
                    // Blocking I/O operation (does NOT block OS thread!)
                    Thread.sleep(Duration.ofSeconds(1));
                    return i;
                });
            });
        } // Executor automatically closes and waits for all 100,000 tasks to finish!

        long elapsed = System.currentTimeMillis() - start;
        System.out.println("Executed 100,000 Virtual Threads in: " + elapsed + " ms");
    }
}
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **High-Throughput Microservices (Tomcat / Jetty)**: Spring Boot 3.2+ running on Java 21 can handle 50,000+ requests per second by configuring `spring.threads.virtual.enabled=true`.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `VirtualThreadDemo.java`.
2. Compile and run: `javac VirtualThreadDemo.java` $\to$ `java VirtualThreadDemo` $\to$ Observe 100,000 threads complete in ~1.2 seconds!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Thread Pinning Slowness** | Calling blocking operations inside a `synchronized` block pins the virtual thread to its carrier thread. | Replace `synchronized` blocks with `ReentrantLock`. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Do NOT Pool Virtual Threads**: Never use thread pools for virtual threads; create them on demand using `Executors.newVirtualThreadPerTaskExecutor()`.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: What is Thread Pinning in Java 21 Virtual Threads and how do you avoid it?
**Answer**: Thread Pinning occurs when a virtual thread cannot unmount from its OS carrier thread during a blocking operation. This happens when blocking occurs inside a `synchronized` block/method or native code. To avoid pinning, replace `synchronized` locks with `java.util.concurrent.locks.ReentrantLock`.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 4.1 Virtual Threads Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which executor method creates an ExecutorService that spawns a new virtual thread for each task?",
      "options": ["Executors.newFixedThreadPool()", "Executors.newVirtualThreadPerTaskExecutor()", "Executors.newCachedThreadPool()", "Executors.newSingleThreadExecutor()"],
      "correct_answer_index": 1,
      "explanation": "Executors.newVirtualThreadPerTaskExecutor() spawns virtual threads."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Benchmark 10,000 concurrent HTTP GET requests using Platform Threads vs Virtual Threads.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: Should virtual threads be pooled like traditional platform threads?
**Back**: No. Virtual threads are cheap (~200 bytes) and should be created per task, never pooled.
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```java
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    executor.submit(() -> Thread.sleep(1000));
}
```

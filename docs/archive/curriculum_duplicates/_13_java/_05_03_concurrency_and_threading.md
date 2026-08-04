# Concurrency and Threading

> **Course**: Java | **Module**: Modern Java | **Difficulty**: advanced

---

```java
// Extend Thread
class PrintTask extends Thread {
    @Override
    public void run() { System.out.println("Running: " + getName()); }
}
new PrintTask().start();

// Implement Runnable (preferred)
Runnable task = () -> System.out.println("Task: " + Thread.currentThread().getName());
Thread t = new Thread(task, "my-thread");
t.start();
t.join();   // wait for completion
```

---

```java
ExecutorService exec = Executors.newFixedThreadPool(4);

// Submit tasks
Future<Integer> future = exec.submit(() -> expensiveCompute());
Integer result = future.get(5, TimeUnit.SECONDS);  // blocking get with timeout

// ScheduledExecutorService
ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(1);
scheduler.scheduleAtFixedRate(() -> pollDatabase(), 0, 30, TimeUnit.SECONDS);

exec.shutdown();        // no more tasks, let existing finish
exec.awaitTermination(60, TimeUnit.SECONDS);
exec.shutdownNow();     // interrupt running tasks
```

---

```java
CompletableFuture<String> future = CompletableFuture
    .supplyAsync(() -> fetchData("https://api.example.com"))
    .thenApply(data -> parseJson(data))
    .thenApply(obj -> obj.getName())
    .exceptionally(ex -> "default-name");

// Combine multiple
CompletableFuture<String> f1 = fetchAsync("url1");
CompletableFuture<String> f2 = fetchAsync("url2");

CompletableFuture.allOf(f1, f2).thenRun(() -> {
    System.out.println(f1.join() + f2.join());
});
```

---

```java
// synchronized method
public synchronized void increment() { count++; }

// synchronized block
public void process() {
    synchronized (this) { count++; }
}

// ReentrantLock
private final ReentrantLock lock = new ReentrantLock();
public void safeIncrement() {
    lock.lock();
    try { count++; }
    finally { lock.unlock(); }
}

// Atomic variables (lock-free)
private final AtomicInteger count = new AtomicInteger(0);
count.incrementAndGet();

// ConcurrentHashMap
ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();
map.merge("key", 1, Integer::sum);
```

---

1. Build a thread-safe counter with `AtomicInteger` and verify with 100 concurrent threads
2. Fetch 10 URLs concurrently using `CompletableFuture.allOf`, combine results
3. Implement a bounded blocking queue using `ReentrantLock` + `Condition`

---

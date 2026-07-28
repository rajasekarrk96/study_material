---
id: "10_04_02"
title: "Concurrency in C++"
course: "C++"
module: 4
module_title: "Modern C++"
lesson: 2
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["thread", "mutex", "lock_guard", "atomic", "future", "promise", "async", "condition_variable", "thread_pool"]
prerequisites: []
lab_required: true
---

# Concurrency in C++

## std::thread

```cpp
#include <thread>
#include <mutex>
#include <atomic>
#include <future>

void task(int id) {
    std::cout << "Thread " << id << "\n";
}

std::thread t1(task, 1);
std::thread t2(task, 2);
t1.join();   // wait for t1
t2.join();
```

## Mutex and Lock

```cpp
std::mutex mtx;
int shared = 0;

void increment() {
    std::lock_guard<std::mutex> lock(mtx);  // RAII — auto unlock
    shared++;
}

// unique_lock — flexible (can unlock manually)
std::unique_lock<std::mutex> lock(mtx);
lock.unlock();
// do other work...
lock.lock();
```

## Atomic Operations

```cpp
std::atomic<int> counter = 0;
counter.fetch_add(1, std::memory_order_relaxed);
counter++;    // operator++ is atomic
int val = counter.load();
counter.store(0);
counter.compare_exchange_strong(expected, desired);
```

## std::async and std::future

```cpp
// Launch async task (may run in new thread)
std::future<int> fut = std::async(std::launch::async, []() {
    return expensive_computation();
});

// Do other work...
int result = fut.get();   // blocks until done
```

## condition_variable

```cpp
std::mutex mtx;
std::condition_variable cv;
bool ready = false;

// Producer
{
    std::lock_guard<std::mutex> lock(mtx);
    ready = true;
}
cv.notify_one();

// Consumer
{
    std::unique_lock<std::mutex> lock(mtx);
    cv.wait(lock, [&]{ return ready; });
    // proceed
}
```

## Lab Exercise
1. Build a thread-safe queue using `mutex` + `condition_variable`
2. Parallelize a Monte Carlo π estimation with `std::async` across N threads
3. Implement a simple thread pool that executes `std::function<void()>` tasks

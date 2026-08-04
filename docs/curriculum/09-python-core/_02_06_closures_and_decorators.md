---
id: "02_06_01"
title: "Closures and Decorators"
course: "Python"
module: 6
module_title: "Advanced Python"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["closure", "free-variable", "nonlocal", "decorator", "functools-wraps", "stacked", "parametrized", "class-decorator", "property"]
prerequisites: []
lab_required: true
---

# Closures and Decorators


## Closures

A closure is a function that **remembers the variables from its enclosing scope** even after that scope has finished executing.

```python
def make_counter(start=0):
    count = start                # free variable

    def counter():
        nonlocal count           # modify outer variable
        count += 1
        return count

    return counter               # returns the closure

c1 = make_counter()
c1()   # 1
c1()   # 2
c1()   # 3

c2 = make_counter(10)
c2()   # 11  (independent state)
```

## The `nonlocal` Keyword

```python
def outer():
    x = 10
    def inner():
        nonlocal x    # without this, assigning x creates local var
        x += 1
        return x
    return inner

inc = outer()
inc()   # 11
inc()   # 12
```

## Decorators

A decorator is a function that **wraps another function** to extend its behavior.

```python
import functools

def timer(func):
    @functools.wraps(func)   # preserves __name__, __doc__
    def wrapper(*args, **kwargs):
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end-start:.4f}s")
        return result
    return wrapper

@timer                    # equivalent to: greet = timer(greet)
def greet(name):
    return f"Hello, {name}!"

greet("Raja")   # prints timing, returns "Hello, Raja!"
```

## Parametrized Decorators

```python
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello!")

hello()   # prints "Hello!" 3 times
```

## Stacked Decorators

```python
@decorator_a
@decorator_b
@decorator_c
def func():
    pass
# Equivalent to: func = decorator_a(decorator_b(decorator_c(func)))
# Applied bottom-up, called top-down
```

## Practical Decorators

```python
# Retry on exception
def retry(max_attempts=3, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Retry {attempt+1}/{max_attempts}: {e}")
        return wrapper
    return decorator

@retry(max_attempts=3, exceptions=(ConnectionError,))
def fetch_data(url):
    ...
```

## Class-Based Decorators

```python
class Cache:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        functools.update_wrapper(self, func)

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@Cache
def expensive(n):
    return n ** 2
```

## Lab Exercise
1. Write a `@log_calls` decorator that logs function name + args
2. Build a `@rate_limit(calls_per_second)` decorator using time.sleep
3. Create a `@singleton` class decorator

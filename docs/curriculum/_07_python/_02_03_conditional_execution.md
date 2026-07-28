---
id: "02_03_02"
title: "Conditional Execution"
course: "Python"
module: 3
module_title: "Control Flow"
lesson: 2
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["if", "elif", "else", "ternary", "match-case", "structural-pattern-matching", "guard", "truthy", "falsy"]
prerequisites: []
lab_required: true
---

# Conditional Execution


## if / elif / else

```python
score = 75

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")
```

## Ternary (Conditional Expression)

```python
# value_if_true if condition else value_if_false
status = "pass" if score >= 60 else "fail"
max_val = a if a > b else b

# Nested ternary (avoid — unreadable)
grade = "A" if s >= 90 else "B" if s >= 75 else "C"
```

## Truthy and Falsy Values

```python
# Falsy:
False, None, 0, 0.0, 0j, "", b"", [], (), {}, set()

# Truthy:
True, any non-zero number, any non-empty collection, any object

# Common patterns
if user:          # user is not None and not empty
if not errors:    # errors list is empty
if results:       # at least one result
```

## Structural Pattern Matching — match/case (3.10+)

```python
command = "quit"

match command:
    case "quit" | "exit":
        print("Goodbye")
    case "help":
        print("Help text")
    case _:
        print("Unknown command")
```

### Matching Sequences and Structures
```python
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"On X-axis at {x}")
    case (0, y):
        print(f"On Y-axis at {y}")
    case (x, y):
        print(f"Point at ({x}, {y})")
```

### Matching Data Classes
```python
from dataclasses import dataclass

@dataclass
class Response:
    status: int
    body: str

match response:
    case Response(status=200, body=body):
        handle_success(body)
    case Response(status=404):
        handle_not_found()
    case Response(status=s) if s >= 500:
        handle_server_error(s)
```

## Lab Exercise
1. Write a grade calculator using if/elif/else
2. Rewrite a complex if/elif chain using match/case
3. Use pattern matching to parse a command like `["move", 10, 20]`

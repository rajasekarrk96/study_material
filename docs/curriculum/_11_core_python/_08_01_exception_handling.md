# Exception Handling

> **Course**: Core Python | **Module**: Exceptions and File I/O | **Difficulty**: intermediate

---

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError (ZeroDivisionError, OverflowError)
    ├── LookupError (IndexError, KeyError)
    ├── ValueError
    ├── TypeError
    ├── IOError (FileNotFoundError, PermissionError)
    ├── RuntimeError
    ├── AttributeError
    └── ...
```

---

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError as e:
        print(f"Type error: {e}")
        return None
    else:
        # Runs only if no exception
        print(f"Result: {result}")
        return result
    finally:
        # ALWAYS runs (cleanup)
        print("Division attempted")
```

---

```python
try:
    x = int("abc")
except ValueError as e:
    print(type(e).__name__)   # ValueError
    print(e.args)             # ('invalid literal...',)
    print(str(e))             # invalid literal for int()...
    import traceback
    traceback.print_exc()     # full traceback
```

---

```python
def set_age(age: int) -> None:
    if not isinstance(age, int):
        raise TypeError(f"Age must be int, got {type(age).__name__}")
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    return age

# raise from — chaining exceptions
try:
    data = json.loads(raw)
except json.JSONDecodeError as e:
    raise ValueError("Invalid configuration file") from e
    # Traceback shows both exceptions; `from e` sets __cause__
```

---

```python
class AppError(Exception):
    """Base exception for this application."""

class ValidationError(AppError):
    def __init__(self, field: str, message: str):
        self.field = field
        self.message = message
        super().__init__(f"Validation error on '{field}': {message}")

class NotFoundError(AppError):
    def __init__(self, resource: str, id: int):
        super().__init__(f"{resource} with id={id} not found")
        self.resource = resource
        self.id = id

try:
    raise ValidationError("email", "Invalid format")
except ValidationError as e:
    print(e.field)    # email
    print(e.message)  # Invalid format
```

---

```python
from contextlib import suppress

# Instead of try/except pass:
with suppress(FileNotFoundError):
    os.remove("temp_file.txt")
```

---

```python
# For concurrent tasks that may raise multiple exceptions
try:
    raise ExceptionGroup("multiple errors", [
        ValueError("bad value"),
        TypeError("wrong type"),
    ])
except* ValueError as eg:
    print("Handled ValueError:", eg.exceptions)
except* TypeError as eg:
    print("Handled TypeError:", eg.exceptions)
```

---

1. Build a `safe_open()` function with specific error messages for each IOError type
2. Create a custom exception hierarchy for an e-commerce app (OrderError, PaymentError, etc.)
3. Write a `retry_on_exception(func, exceptions, max_retries)` utility

---

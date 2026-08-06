---
id: "02_07_01"
title: "Classes and Instance Mechanics"
course: "Python"
module: 7
module_title: "Object-Oriented Programming"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["class", "self", "__init__", "instance-attributes", "class-attributes", "classmethod", "staticmethod", "__repr__", "__str__", "slots"]
prerequisites: []
lab_required: true
---

# Classes and Instance Mechanics


## Defining a Class

```python
class BankAccount:
    # Class attribute (shared by all instances)
    interest_rate = 0.05
    _instances = 0

    def __init__(self, owner: str, balance: float = 0.0):
        # Instance attributes (unique per object)
        self.owner = owner
        self._balance = balance   # _ = convention: internal use
        BankAccount._instances += 1

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> float:
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return amount

    @property
    def balance(self) -> float:
        """Read-only balance via property."""
        return self._balance

    @classmethod
    def set_rate(cls, rate: float) -> None:
        """Change rate for ALL accounts."""
        cls.interest_rate = rate

    @staticmethod
    def validate_amount(amount: float) -> bool:
        """Utility — doesn't need self or cls."""
        return amount > 0

    def __repr__(self) -> str:
        """Unambiguous — for developers."""
        return f"BankAccount(owner={self.owner!r}, balance={self._balance})"

    def __str__(self) -> str:
        """Readable — for end users."""
        return f"Account[{self.owner}]: ${self._balance:.2f}"
```

## Properties

```python
class Temperature:
    def __init__(self, celsius: float = 0):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

    @celsius.deleter
    def celsius(self):
        del self._celsius

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32

t = Temperature(100)
t.celsius       # 100
t.fahrenheit    # 212.0
t.celsius = 200 # OK
t.celsius = -300  # ValueError
```

## `__slots__` — Memory Optimization

```python
class Point:
    __slots__ = ['x', 'y']   # disables __dict__, saves ~30% memory

    def __init__(self, x, y):
        self.x = x
        self.y = y

import sys
class PointDict:
    def __init__(self, x, y):
        self.x = x; self.y = y

p1 = Point(1, 2)
p2 = PointDict(1, 2)
sys.getsizeof(p1)   # ~48 bytes
sys.getsizeof(p2)   # ~152 bytes (dict overhead)
```

## Lab Exercise
1. Build a `Stack` class with push/pop/peek and `__len__`, `__repr__`
2. Create a `Circle` class with a radius property that auto-computes area and circumference
3. Compare memory of 1000 `__slots__` vs regular instances using `tracemalloc`

# Inheritance and Polymorphism

> **Course**: Core Python | **Module**: Object-Oriented Programming | **Difficulty**: intermediate

---

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError("Subclass must implement speak()")

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name!r})"

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says: Woof!"

    def fetch(self, item: str) -> str:
        return f"{self.name} fetches the {item}!"

class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says: Meow!"

animals = [Dog("Rex"), Cat("Whiskers"), Dog("Buddy")]
for a in animals:
    print(a.speak())   # polymorphism — different speak per type
```

---

```python
class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_kwh: float):
        super().__init__(make, model, year)   # call parent __init__
        self.battery_kwh = battery_kwh

    def range_estimate(self) -> float:
        return self.battery_kwh * 5   # km per kWh

ev = ElectricVehicle("Tesla", "Model 3", 2024, 75)
ev.range_estimate()   # 375.0
```

---

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:
        return f"{type(self).__name__}: area={self.area():.2f}"

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius

Shape()    # TypeError: Can't instantiate abstract class
Circle(5)  # OK — all abstract methods implemented
```

---

```python
class A:
    def method(self): return "A"

class B(A):
    def method(self): return "B"

class C(A):
    def method(self): return "C"

class D(B, C):  # multiple inheritance
    pass

D.mro()   # [D, B, C, A, object]  — C3 linearisation
D().method()  # "B"  — follows MRO
```

---

```python
class JsonMixin:
    def to_json(self) -> str:
        import json
        return json.dumps(self.__dict__)

class LogMixin:
    def log(self, message: str) -> None:
        print(f"[{type(self).__name__}] {message}")

class User(JsonMixin, LogMixin):
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

u = User("Raja", "raja@example.com")
u.to_json()   # '{"name": "Raja", "email": "raja@example.com"}'
u.log("created")  # [User] created
```

---

1. Build an animal hierarchy: Animal → Mammal → Dog/Cat; add `speak()`, `breathe()`
2. Use ABC to enforce an interface for payment gateways (Stripe, PayPal)
3. Create a `SerializableMixin` that adds `to_dict()` / `from_dict()` to any class

---

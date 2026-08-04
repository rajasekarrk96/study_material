---
id: "02_07_04"
title: "Dataclasses and Protocols"
course: "Python"
module: 7
module_title: "Object-Oriented Programming"
lesson: 4
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["dataclass", "field", "frozen", "post-init", "__post_init__", "Protocol", "typing", "NamedTuple", "TypedDict", "attrs"]
prerequisites: []
lab_required: true
---

# Dataclasses and Protocols


## @dataclass

```python
from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class Point:
    x: float
    y: float

    def distance(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

p = Point(3, 4)
p.x          # 3
repr(p)      # Point(x=3, y=4)  — auto-generated
p == Point(3, 4)   # True — auto __eq__
```

## Advanced dataclass Options

```python
@dataclass(frozen=True, order=True)  # immutable + sortable
class Config:
    host: str = "localhost"
    port: int = 8000
    debug: bool = False
    tags: list = field(default_factory=list)  # mutable default

    # Class variable (not a field)
    MAX_CONNECTIONS: ClassVar[int] = 100

    def __post_init__(self):
        # Validate after __init__
        if not 1 <= self.port <= 65535:
            raise ValueError(f"Invalid port: {self.port}")

c = Config(port=443)
c.host = "other"   # FrozenInstanceError (frozen=True)
```

## TypedDict

```python
from typing import TypedDict, Required, NotRequired

class UserRecord(TypedDict):
    id: int
    name: str
    email: str
    age: NotRequired[int]   # optional key

def create_user(data: UserRecord) -> None:
    print(data["name"])

create_user({"id": 1, "name": "Raja", "email": "r@x.com"})  # OK
```

## Protocol (Structural Subtyping)

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None: ...
    def resize(self, factor: float) -> None: ...

class Circle:   # No explicit inheritance!
    def draw(self): print("Drawing circle")
    def resize(self, factor): self.radius *= factor

class Square:
    def draw(self): print("Drawing square")
    def resize(self, factor): self.side *= factor

# Both satisfy the Protocol — duck typing with type safety
def render(shape: Drawable) -> None:
    shape.draw()

render(Circle())   # OK
render(Square())   # OK
isinstance(Circle(), Drawable)  # True (runtime_checkable)
```

## attrs Library

```python
import attrs

@attrs.define
class Product:
    name: str
    price: float = attrs.field(validator=attrs.validators.gt(0))
    category: str = "general"
    tags: list = attrs.Factory(list)

p = Product("Widget", 9.99)
p                    # Product(name='Widget', price=9.99, category='general', tags=[])
Product("Bad", -1)   # ValueError: price must be > 0
```

## Lab Exercise
1. Build a `@dataclass(frozen=True)` `Color` class with RGB validation
2. Create a `Serializable` Protocol requiring `to_json()` and `from_json()`
3. Compare boilerplate: regular class vs `@dataclass` vs `attrs.define` for same model

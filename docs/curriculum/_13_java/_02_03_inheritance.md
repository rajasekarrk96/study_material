# Inheritance

> **Course**: Java | **Module**: Object-Oriented Programming | **Difficulty**: intermediate

---

```java
// Base class
public class Vehicle {
    protected String make;
    protected int year;

    public Vehicle(String make, int year) {
        this.make = make;
        this.year = year;
    }

    public String getInfo() {
        return String.format("%d %s", year, make);
    }

    public void honk() { System.out.println("Beep!"); }
}

// Subclass
public class Car extends Vehicle {
    private int doors;

    public Car(String make, int year, int doors) {
        super(make, year);   // must be first statement
        this.doors = doors;
    }

    @Override
    public String getInfo() {
        return super.getInfo() + " (" + doors + " doors)";
    }

    @Override
    public void honk() { System.out.println("Honk!"); }
}

// Usage
Vehicle v = new Car("Toyota", 2024, 4);  // polymorphism
System.out.println(v.getInfo());          // "2024 Toyota (4 doors)"
v.honk();                                 // "Honk!"
```

---

```java
public abstract class Shape {
    protected String color;

    public Shape(String color) { this.color = color; }

    // Abstract — must be implemented by subclasses
    public abstract double area();
    public abstract double perimeter();

    // Concrete method (shared implementation)
    public void describe() {
        System.out.printf("%s %s: area=%.2f%n",
            color, getClass().getSimpleName(), area());
    }
}

public class Circle extends Shape {
    private double radius;

    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }

    @Override public double area()      { return Math.PI * radius * radius; }
    @Override public double perimeter() { return 2 * Math.PI * radius; }
}
```

---

```java
// final class — cannot be subclassed (e.g., String, Integer)
public final class ImmutableConfig { ... }

// final method — cannot be overridden
public final void validateInput() { ... }

// final field — cannot be reassigned
private final String id = UUID.randomUUID().toString();
```

---

1. Build Animal → Mammal → Dog/Cat hierarchy with abstract `makeSound()`
2. Override `toString()` at each level and verify the chain with `super.toString()`
3. Use `instanceof` with pattern matching to handle different Vehicle subtypes

---

---
id: "08_02_04"
title: "Polymorphism and Abstraction"
course: "Java"
module: 2
module_title: "Object-Oriented Programming"
lesson: 4
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["polymorphism", "dynamic-dispatch", "method-overriding", "abstract", "sealed", "interface", "duck-typing"]
prerequisites: []
lab_required: true
---

# Polymorphism and Abstraction

## Runtime Polymorphism

```java
// Method called depends on ACTUAL type, not declared type
Shape[] shapes = {
    new Circle("red", 5),
    new Rectangle("blue", 4, 6),
    new Triangle("green", 3, 4, 5)
};

double totalArea = 0;
for (Shape s : shapes) {
    totalArea += s.area();   // dynamic dispatch — correct area() called
    s.describe();
}
System.out.printf("Total: %.2f%n", totalArea);
```

## Sealed Classes (Java 17+)

```java
public sealed class Result<T>
    permits Result.Success, Result.Failure {

    public static final class Success<T> extends Result<T> {
        public final T value;
        public Success(T value) { this.value = value; }
    }

    public static final class Failure<T> extends Result<T> {
        public final String error;
        public Failure(String error) { this.error = error; }
    }
}

// Pattern matching switch
String message = switch (result) {
    case Result.Success<String> s -> "Got: " + s.value;
    case Result.Failure<String> f -> "Error: " + f.error;
};
```

## Abstract vs Interface

| | Abstract Class | Interface |
|---|---|---|
| Instantiate | No | No |
| Multiple inheritance | No | Yes |
| Constructor | Yes | No |
| Fields | Any | `public static final` only |
| Methods | Abstract + concrete | Default + abstract + static |
| Use when | Related classes share base | Unrelated classes share behaviour |

## Lab Exercise
1. Implement a `PaymentProcessor` hierarchy with `CreditCard`, `UPI`, `Wallet`
2. Use sealed `Result<T>` instead of checked exceptions in a file reader
3. Demonstrate how adding a new Shape subclass requires zero changes in the loop

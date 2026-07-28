---
id: "08_05_02"
title: "Java 8 to 21 Key Features"
course: "Java"
module: 5
module_title: "Modern Java"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["records", "sealed", "text-blocks", "switch-expression", "pattern-matching", "var", "instanceof", "virtual-threads"]
prerequisites: []
lab_required: true
---

# Java 8 to 21 Key Features

## Java Version Feature Map

| Version | Key Feature |
|---|---|
| 8 | Lambda, Stream, Optional, Date/Time API |
| 10 | `var` local type inference |
| 11 | `String.lines()`, `isBlank()`, `strip()` |
| 14 | Records (preview), Switch expressions |
| 15 | Text blocks |
| 16 | Records (final), `instanceof` pattern matching |
| 17 | Sealed classes, LTS |
| 21 | Virtual threads (Loom), Pattern matching switch, LTS |

## Records (Java 16)

```java
record Person(String name, int age) {
    // Compact constructor — validation
    Person {
        Objects.requireNonNull(name);
        if (age < 0) throw new IllegalArgumentException();
    }

    // Custom methods
    String greeting() { return "Hello, " + name + "!"; }
}

var p = new Person("Raja", 28);
p.name()      // "Raja" (auto-generated accessor)
p.age()       // 28
p.equals(new Person("Raja", 28))   // true (auto-generated)
```

## Sealed Classes (Java 17)

```java
sealed interface Shape permits Circle, Rectangle, Triangle {}

record Circle(double radius) implements Shape {}
record Rectangle(double w, double h) implements Shape {}
record Triangle(double a, double b, double c) implements Shape {}

double area(Shape s) {
    return switch (s) {
        case Circle c    -> Math.PI * c.radius() * c.radius();
        case Rectangle r -> r.w() * r.h();
        case Triangle t  -> {
            double sp = (t.a()+t.b()+t.c()) / 2;
            yield Math.sqrt(sp*(sp-t.a())*(sp-t.b())*(sp-t.c()));
        }
    };
}
```

## Virtual Threads (Java 21)

```java
// Classic: 1 OS thread per request — limited scalability
ExecutorService exec = Executors.newFixedThreadPool(200);

// Virtual threads: millions of lightweight threads
ExecutorService vExec = Executors.newVirtualThreadPerTaskExecutor();

// Per-request virtual thread
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    IntStream.range(0, 10_000).forEach(i ->
        executor.submit(() -> {
            Thread.sleep(Duration.ofMillis(100));  // non-blocking
            return i;
        })
    );
}
```

## Lab Exercise
1. Rewrite a `User` class as a record, add validation in compact constructor
2. Implement a `Shape` sealed interface with pattern-matching area computation
3. Compare throughput: 100 requests with thread pool vs virtual threads

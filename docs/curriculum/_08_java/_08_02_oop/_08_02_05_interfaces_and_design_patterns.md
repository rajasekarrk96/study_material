---
id: "08_02_05"
title: "Interfaces and Design Patterns"
course: "Java"
module: 2
module_title: "Object-Oriented Programming"
lesson: 5
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["interface", "default-method", "static-method", "functional-interface", "Comparable", "Comparator", "Singleton", "Factory", "Strategy"]
prerequisites: []
lab_required: true
---

# Interfaces and Design Patterns

## Interfaces

```java
public interface Drawable {
    void draw();                              // abstract
    default void drawWithBorder() {           // default (Java 8+)
        System.out.println("[border]");
        draw();
    }
    static Drawable circle(double r) {        // static factory
        return () -> System.out.printf("Circle r=%.1f%n", r);
    }
}

// Functional interface (single abstract method)
@FunctionalInterface
public interface Transformer<T> {
    T transform(T input);
}

Transformer<String> upper = s -> s.toUpperCase();
upper.transform("hello");   // "HELLO"
```

## Comparable and Comparator

```java
public class Product implements Comparable<Product> {
    private String name;
    private double price;

    @Override
    public int compareTo(Product other) {
        return Double.compare(this.price, other.price);
    }
}

// Sort by price ascending
Collections.sort(products);

// Sort by name (external comparator)
products.sort(Comparator.comparing(Product::getName));

// Multi-level sort
products.sort(
    Comparator.comparing(Product::getCategory)
              .thenComparing(Product::getPrice)
              .thenComparing(Comparator.comparing(Product::getName).reversed())
);
```

## Design Patterns

```java
// Singleton
public class DatabasePool {
    private static volatile DatabasePool instance;
    private DatabasePool() {}
    public static DatabasePool getInstance() {
        if (instance == null) {
            synchronized (DatabasePool.class) {
                if (instance == null) instance = new DatabasePool();
            }
        }
        return instance;
    }
}

// Strategy
public interface SortStrategy { void sort(int[] arr); }
public class BubbleSort implements SortStrategy {
    public void sort(int[] arr) { /* ... */ }
}
public class QuickSort implements SortStrategy {
    public void sort(int[] arr) { /* ... */ }
}
public class Sorter {
    private SortStrategy strategy;
    public Sorter(SortStrategy s) { this.strategy = s; }
    public void sort(int[] arr) { strategy.sort(arr); }
}
```

## Lab Exercise
1. Define a `Logger` interface with `log(String)`, `warn(String)`, `error(String)` — implement Console and File versions
2. Sort a list of employees by department then salary using chained `Comparator`
3. Implement Strategy pattern for discount calculation: flat, percentage, buy-2-get-1

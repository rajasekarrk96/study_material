---
id: "08_01_05"
title: "Methods and Varargs"
course: "Java"
module: 1
module_title: "Java Fundamentals"
lesson: 5
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["method", "return", "overloading", "varargs", "static", "recursion", "Math"]
prerequisites: []
lab_required: true
---

# Methods and Varargs

## Method Syntax

```java
// access-modifier return-type methodName(params) { body }
public static double calculateBMI(double weight, double height) {
    if (height == 0) throw new IllegalArgumentException("Height cannot be 0");
    return weight / (height * height);
}

// Calling
double bmi = calculateBMI(70.0, 1.75);
System.out.printf("BMI: %.2f%n", bmi);
```

## Method Overloading

```java
public static int add(int a, int b)          { return a + b; }
public static double add(double a, double b) { return a + b; }
public static int add(int a, int b, int c)   { return a + b + c; }

add(1, 2)        // int version
add(1.0, 2.5)    // double version
add(1, 2, 3)     // three-arg version
```

## Varargs

```java
public static int sum(int... numbers) {
    int total = 0;
    for (int n : numbers) total += n;
    return total;
}

sum()            // 0
sum(1, 2, 3)     // 6
sum(1, 2, 3, 4, 5) // 15

// Varargs + other params
public static String format(String template, Object... args) {
    return String.format(template, args);
}
```

## Recursion

```java
public static long factorial(int n) {
    if (n <= 1) return 1;       // base case
    return n * factorial(n - 1); // recursive case
}

public static int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n-1) + fibonacci(n-2);
}

// Tail-recursive with accumulator (optimised)
public static long factorial(int n, long acc) {
    if (n <= 1) return acc;
    return factorial(n - 1, n * acc);
}
```

## Math Class

```java
Math.abs(-5)          // 5
Math.pow(2, 10)       // 1024.0
Math.sqrt(144)        // 12.0
Math.cbrt(27)         // 3.0
Math.max(3, 7)        // 7
Math.min(3, 7)        // 3
Math.round(3.7)       // 4L
Math.floor(3.9)       // 3.0
Math.ceil(3.1)        // 4.0
Math.random()         // [0.0, 1.0)
Math.log(Math.E)      // 1.0
Math.PI               // 3.14159...
```

## Lab Exercise
1. Write overloaded `area()` methods for circle, rectangle, and triangle
2. Implement `quickSort(int[] arr, int low, int high)` recursively
3. Write a varargs `max(double... values)` that returns the maximum value

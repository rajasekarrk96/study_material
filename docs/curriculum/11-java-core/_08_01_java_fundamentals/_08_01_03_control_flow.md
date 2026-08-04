---
id: "08_01_03"
title: "Control Flow"
course: "Java"
module: 1
module_title: "Java Fundamentals"
lesson: 3
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["if", "switch", "for", "while", "do-while", "break", "continue", "enhanced-for", "switch-expression", "pattern-matching"]
prerequisites: []
lab_required: true
---

# Control Flow

## Conditional Statements

```java
// if / else if / else
int score = 82;
if (score >= 90) {
    System.out.println("A");
} else if (score >= 75) {
    System.out.println("B");
} else if (score >= 60) {
    System.out.println("C");
} else {
    System.out.println("F");
}

// Traditional switch
switch (day) {
    case "MON": case "TUE": case "WED": case "THU": case "FRI":
        System.out.println("Weekday");
        break;
    case "SAT": case "SUN":
        System.out.println("Weekend");
        break;
    default:
        System.out.println("Unknown");
}

// Switch expression (Java 14+)
String type = switch (day) {
    case "MON", "TUE", "WED", "THU", "FRI" -> "Weekday";
    case "SAT", "SUN" -> "Weekend";
    default -> throw new IllegalArgumentException("Unknown: " + day);
};
```

## Loops

```java
// for loop
for (int i = 0; i < 10; i++) {
    System.out.print(i + " ");
}

// while
int n = 1;
while (n <= 100) {
    n *= 2;
}

// do-while (runs at least once)
do {
    input = scanner.nextLine();
} while (input.isEmpty());

// Enhanced for (for-each)
int[] numbers = {1, 2, 3, 4, 5};
for (int num : numbers) {
    System.out.println(num);
}

// break and continue
for (int i = 0; i < 10; i++) {
    if (i == 5) break;      // exit loop
    if (i % 2 == 0) continue;  // skip even
    System.out.print(i);
}

// Labeled break (for nested loops)
outer:
for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 5; j++) {
        if (i == 2 && j == 2) break outer;
        System.out.print(i + "" + j + " ");
    }
}
```

## Pattern Matching (Java 16+)

```java
Object obj = "Hello";

// instanceof with pattern variable
if (obj instanceof String s) {
    System.out.println(s.toUpperCase());  // s is a String here
}

// Pattern matching in switch (Java 21)
String describe(Object o) {
    return switch (o) {
        case Integer i -> "int: " + i;
        case String s  -> "string: " + s;
        case Double d  -> "double: " + d;
        case null      -> "null";
        default        -> "other: " + o;
    };
}
```

## Lab Exercise
1. Print a multiplication table using nested for loops
2. Build a number guessing game using `while` loop and `Scanner`
3. Rewrite a 5-case switch statement using the switch expression arrow syntax

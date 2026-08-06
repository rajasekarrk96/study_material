---
id: "08_05_01"
title: "Lambda Expressions and Streams"
course: "Java"
module: 5
module_title: "Modern Java"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["lambda", "Stream", "filter", "map", "reduce", "collect", "Optional", "method-reference", "Collectors", "flatMap"]
prerequisites: []
lab_required: true
---

# Lambda Expressions and Streams

## Lambda Expressions

```java
// (params) -> expression  OR  (params) -> { body }
Runnable r = () -> System.out.println("Hello!");
Comparator<String> byLength = (a, b) -> Integer.compare(a.length(), b.length());
Predicate<Integer> isEven = n -> n % 2 == 0;
Function<String, Integer> strLen = String::length;  // method reference

// Common functional interfaces
Predicate<T>   test(T) → boolean
Function<T,R>  apply(T) → R
Consumer<T>    accept(T) → void
Supplier<T>    get() → T
BiFunction<T,U,R> apply(T,U) → R
UnaryOperator<T>  apply(T) → T
BinaryOperator<T> apply(T,T) → T
```

## Stream API

```java
import java.util.stream.*;

List<String> names = List.of("Alice","Bob","Charlie","Dave","Eve");

// filter, map, collect
List<String> result = names.stream()
    .filter(n -> n.length() > 3)      // filter: Charlie, Dave
    .map(String::toUpperCase)          // transform
    .sorted()                          // sort alphabetically
    .collect(Collectors.toList());     // collect to list

// Numeric operations
IntStream.range(1, 11).sum()       // 55
IntStream.of(1,2,3).average()      // OptionalDouble[2.0]

List<Integer> nums = List.of(1,2,3,4,5,6,7,8,9,10);
int sumOfSquaresOfEvens = nums.stream()
    .filter(n -> n % 2 == 0)
    .mapToInt(n -> n * n)
    .sum();   // 220
```

## Collectors

```java
// Grouping
Map<Integer, List<String>> byLength = names.stream()
    .collect(Collectors.groupingBy(String::length));

// Counting per group
Map<Integer, Long> counts = names.stream()
    .collect(Collectors.groupingBy(String::length, Collectors.counting()));

// Joining
String joined = names.stream()
    .collect(Collectors.joining(", ", "[", "]"));  // "[Alice, Bob, ...]"

// Partitioning
Map<Boolean, List<Integer>> partitioned = nums.stream()
    .collect(Collectors.partitioningBy(n -> n % 2 == 0));
```

## Optional

```java
Optional<String> opt = Optional.of("Hello");
Optional<String> empty = Optional.empty();

opt.isPresent()           // true
opt.get()                 // "Hello" (throws if empty)
opt.orElse("default")     // returns value or "default"
opt.orElseGet(() -> compute_default())
opt.map(String::toUpperCase)  // Optional["HELLO"]
opt.filter(s -> s.length() > 3)
opt.ifPresent(System.out::println)

// Safe chaining
Optional<String> result = Optional.ofNullable(user)
    .map(User::getAddress)
    .map(Address::getCity)
    .filter(city -> city.startsWith("C"));
```

## Lab Exercise
1. Count word frequencies in a paragraph using streams and `Collectors.groupingBy`
2. Find top 3 most expensive products per category using streams
3. Flatten a `List<List<Integer>>` to `List<Integer>` using `flatMap`

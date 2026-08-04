# Generics

> **Course**: Java | **Module**: Collections and Generics | **Difficulty**: intermediate

---

```java
public class Pair<A, B> {
    private final A first;
    private final B second;

    public Pair(A first, B second) {
        this.first = first;
        this.second = second;
    }

    public A getFirst()  { return first; }
    public B getSecond() { return second; }

    @Override public String toString() {
        return "(" + first + ", " + second + ")";
    }
}

Pair<String, Integer> p = new Pair<>("Raja", 28);
String name = p.getFirst();
```

---

```java
public static <T extends Comparable<T>> T max(T a, T b) {
    return a.compareTo(b) >= 0 ? a : b;
}

max(3, 7)            // 7
max("apple","mango") // "mango"
max(3.14, 2.71)      // 3.14
```

---

```java
// Unbounded — any type
public static void printList(List<?> list) {
    for (Object item : list) System.out.println(item);
}

// Upper bounded — T or subtype (producer)
public static double sumList(List<? extends Number> list) {
    return list.stream().mapToDouble(Number::doubleValue).sum();
}
sumList(List.of(1, 2, 3));    // List<Integer> — OK
sumList(List.of(1.5, 2.5));   // List<Double>  — OK

// Lower bounded — T or supertype (consumer)
public static void addNumbers(List<? super Integer> list) {
    list.add(1); list.add(2); list.add(3);
}
addNumbers(new ArrayList<Number>());  // OK
addNumbers(new ArrayList<Object>());  // OK

// PECS: Producer Extends, Consumer Super
```

---

```java
// At compile time: List<String> and List<Integer> are different
// At runtime: both become List (type erased!)
List<String> strings = new ArrayList<>();
List<Integer> ints = new ArrayList<>();
System.out.println(strings.getClass() == ints.getClass()); // true!
```

---

1. Build a generic `Stack<T>` with `push`, `pop`, `peek`, `isEmpty`
2. Write `filter(List<T> list, Predicate<T> pred)` — returns filtered list
3. Demonstrate PECS with a `copy(List<? super T> dest, List<? extends T> src)` method

---

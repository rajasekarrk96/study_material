---
id: "08_03_02"
title: "Iterators and Comparators"
course: "Java"
module: 3
module_title: "Collections and Generics"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["Iterator", "ListIterator", "Iterable", "Comparator", "Comparable", "Collections", "sort", "min", "max", "frequency"]
prerequisites: []
lab_required: true
---

# Iterators and Comparators

## Iterator Pattern

```java
List<String> items = new ArrayList<>(List.of("a","b","c","d"));

// External iterator
Iterator<String> it = items.iterator();
while (it.hasNext()) {
    String item = it.next();
    if (item.equals("b")) it.remove();  // safe removal during iteration
}

// ListIterator (bidirectional)
ListIterator<String> lit = items.listIterator();
while (lit.hasNext()) {
    String item = lit.next();
    lit.set(item.toUpperCase());  // replace current element
}

// ConcurrentModificationException — WRONG
for (String s : items) {
    if (s.equals("a")) items.remove(s);  // throws!
}
```

## Implementing Iterable

```java
public class NumberRange implements Iterable<Integer> {
    private final int start, end;
    public NumberRange(int start, int end) {
        this.start = start; this.end = end;
    }

    @Override
    public Iterator<Integer> iterator() {
        return new Iterator<>() {
            int current = start;
            public boolean hasNext() { return current <= end; }
            public Integer next()    { return current++; }
        };
    }
}

for (int n : new NumberRange(1, 5)) {
    System.out.print(n + " ");   // 1 2 3 4 5
}
```

## Collections Utility Class

```java
List<Integer> nums = new ArrayList<>(List.of(3,1,4,1,5,9,2,6));

Collections.sort(nums);
Collections.sort(nums, Comparator.reverseOrder());
Collections.shuffle(nums);
Collections.reverse(nums);
Collections.min(nums);
Collections.max(nums);
Collections.frequency(nums, 1);         // count of 1s
Collections.nCopies(3, "x");           // ["x","x","x"]
Collections.unmodifiableList(nums);     // read-only view
Collections.synchronizedList(nums);     // thread-safe wrapper
```

## Lab Exercise
1. Build a custom `CircularIterator<T>` that wraps around at the end
2. Sort a `List<Employee>` by multiple criteria: department → salary desc → name asc
3. Use `Collections.rotate(list, n)` to implement a round-robin scheduler

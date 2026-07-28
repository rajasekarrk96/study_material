---
id: "08_03_01"
title: "Collections Framework"
course: "Java"
module: 3
module_title: "Collections and Generics"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["Collection", "List", "ArrayList", "LinkedList", "Set", "HashSet", "TreeSet", "Map", "HashMap", "TreeMap", "LinkedHashMap"]
prerequisites: []
lab_required: true
---

# Collections Framework

## Collection Hierarchy

```
Collection
├── List      — ordered, duplicates allowed
│   ├── ArrayList
│   ├── LinkedList
│   └── Vector (legacy)
├── Set       — unique elements
│   ├── HashSet (unordered, O(1))
│   ├── LinkedHashSet (insertion order)
│   └── TreeSet (sorted, O(log n))
└── Queue
    ├── LinkedList
    ├── PriorityQueue
    └── ArrayDeque

Map (not Collection)
├── HashMap (unordered, O(1))
├── LinkedHashMap (insertion order)
├── TreeMap (sorted, O(log n))
└── Hashtable (legacy, synchronised)
```

## List — ArrayList vs LinkedList

```java
// ArrayList — fast random access, slow insert/delete in middle
List<String> list = new ArrayList<>();
list.add("Alice");
list.add(0, "Bob");        // insert at index
list.remove("Alice");
list.remove(0);            // remove by index
list.get(0);               // O(1)
list.size();

// LinkedList — fast insert/delete, slow random access
LinkedList<Integer> ll = new LinkedList<>();
ll.addFirst(1);   ll.addLast(3);   ll.add(1, 2);
ll.peekFirst();   ll.pollLast();

// Factory methods (immutable)
List<String> names = List.of("Alice", "Bob", "Charlie");
Set<Integer>  nums = Set.of(1, 2, 3);
Map<String,Integer> ages = Map.of("Alice", 25, "Bob", 30);
```

## Map Operations

```java
Map<String, Integer> scores = new HashMap<>();
scores.put("Alice", 95);
scores.put("Bob", 87);
scores.putIfAbsent("Carol", 0);          // only if not present
scores.merge("Alice", 5, Integer::sum);   // 95 + 5 = 100

// Get with default
int score = scores.getOrDefault("Dave", 0);

// Compute
scores.compute("Bob", (k, v) -> v == null ? 1 : v + 1);

// Iterate
for (Map.Entry<String, Integer> e : scores.entrySet()) {
    System.out.println(e.getKey() + ": " + e.getValue());
}
scores.forEach((k, v) -> System.out.printf("%s=%d%n", k, v));
```

## Lab Exercise
1. Count word frequency from a text using `HashMap` then sort by frequency using `TreeMap`
2. Demonstrate why `equals()`/`hashCode()` must be correct for `HashSet` to work
3. Implement a LRU Cache using `LinkedHashMap` with `removeEldestEntry()`

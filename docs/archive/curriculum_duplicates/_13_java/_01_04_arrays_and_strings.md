# Arrays and Strings

> **Course**: Java | **Module**: Java Fundamentals | **Difficulty**: beginner

---

```java
// Declaration and initialization
int[] nums = {1, 2, 3, 4, 5};
String[] names = new String[3];
names[0] = "Alice"; names[1] = "Bob"; names[2] = "Charlie";

// Accessing
System.out.println(nums.length);   // 5
System.out.println(nums[0]);       // 1
System.out.println(nums[nums.length - 1]);  // 5

// 2D array
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};
System.out.println(matrix[1][2]);  // 6

// java.util.Arrays utility
import java.util.Arrays;

Arrays.sort(nums);
int idx = Arrays.binarySearch(nums, 3);
int[] copy = Arrays.copyOf(nums, 10);       // pad with 0s
int[] range = Arrays.copyOfRange(nums, 1, 4); // [2,3,4]
System.out.println(Arrays.toString(nums));   // [1, 2, 3, 4, 5]
Arrays.fill(nums, 0);
```

---

```java
String s = "  Hello, World!  ";

s.length()                   // 17
s.trim()                     // "Hello, World!"
s.strip()                    // same (Unicode-aware)
s.toLowerCase()
s.toUpperCase()
s.charAt(7)                  // 'W'
s.indexOf("World")           // 9
s.lastIndexOf('l')           // 12
s.substring(2, 7)            // "Hello"
s.replace("World", "Java")
s.contains("Hello")          // true
s.startsWith("  H")         // true
s.endsWith("  ")             // true
s.split(", ")                // ["  Hello", "World!  "]
s.isEmpty()                  // false
s.isBlank()                  // false
String.join(", ", "a","b","c")  // "a, b, c"
```

---

```java
// String concatenation in loop = O(n²) — use StringBuilder instead
StringBuilder sb = new StringBuilder();
for (int i = 1; i <= 5; i++) {
    sb.append(i).append(", ");  // chaining
}
sb.deleteCharAt(sb.length() - 1);  // remove last comma
sb.insert(0, "[").append("]");
String result = sb.toString();    // "[1, 2, 3, 4, 5]"

// Common methods
sb.reverse()
sb.replace(start, end, str)
sb.delete(start, end)
sb.length()
```

---

```java
import java.util.StringJoiner;

StringJoiner sj = new StringJoiner(", ", "[", "]");
for (String name : names) sj.add(name);
System.out.println(sj);  // [Alice, Bob, Charlie]

// Formatted strings
String.format("Name: %-15s Age: %3d", "Raja", 28)
// "Name: Raja            Age:  28"
```

---

1. Implement bubble sort on an integer array, verify with `Arrays.sort`
2. Count character frequencies in a string using an array of 26 ints
3. Reverse words in a sentence using `split()` and `StringBuilder`

---

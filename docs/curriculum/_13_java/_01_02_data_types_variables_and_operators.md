# Data Types Variables and Operators

> **Course**: Java | **Module**: Java Fundamentals | **Difficulty**: beginner

---

```java
// Integer types
byte   b = 127;              // 8-bit  (-128 to 127)
short  s = 32767;            // 16-bit
int    i = 2_147_483_647;    // 32-bit (default integer)
long   l = 9_223_372_036_854_775_807L;  // 64-bit (suffix L)

// Floating point
float  f = 3.14f;            // 32-bit (suffix f)
double d = 3.141592653589793; // 64-bit (default decimal)

// Other
boolean flag = true;
char    c    = 'A';          // 16-bit Unicode character (UTF-16)

// Literals
int hex = 0xFF;              // 255
int bin = 0b1010;            // 10
long big = 1_000_000L;       // underscore for readability
```

---

```java
// String — immutable, interned
String name = "Raja";
String greeting = "Hello, " + name + "!";
String multiline = """
        Line 1
        Line 2
        """;  // Text block (Java 15+)

// String methods
name.length()           // 4
name.toUpperCase()      // "RAJA"
name.charAt(0)          // 'R'
name.substring(1, 3)    // "aj"
name.contains("aj")     // true
name.replace("a", "A")  // "RAjA"
name.strip()            // trim (Unicode-aware)
String.format("Name: %s, Age: %d", name, 28)
```

---

```java
var message = "Hello";       // String
var count   = 42;            // int
var prices  = new ArrayList<Double>();

// Works in for-each
for (var item : prices) {
    System.out.println(item);
}
```

---

```java
final int MAX_SIZE = 100;
final double PI = 3.141592653589793;
// MAX_SIZE = 200; // CompileError: cannot assign final
```

---

```java
// Widening (implicit — safe)
int i = 100;
long l = i;       // int → long
double d = l;     // long → double

// Narrowing (explicit — may lose data)
double price = 9.99;
int truncated = (int) price;   // 9

// String conversions
int n = Integer.parseInt("42");
double pi = Double.parseDouble("3.14");
String s = String.valueOf(42);    // "42"
String.valueOf(true)              // "true"
```

---

```java
// Arithmetic: + - * / % (integer division truncates)
10 / 3      // 3 (not 3.33!)
10.0 / 3    // 3.333...
10 % 3      // 1

// Comparison: == != < > <= >=
// Logical: && || !
// Bitwise: & | ^ ~ << >> >>>
// Ternary
String result = score >= 60 ? "Pass" : "Fail";

// String concatenation
"Hello" + 42       // "Hello42"
"Sum: " + (1 + 2)  // "Sum: 3"
```

---

1. Calculate the area and circumference of a circle using `Math.PI`
2. Demonstrate widening and narrowing casts with a temperature converter (Celsius ↔ Fahrenheit)
3. Use a text block to format a multi-line JSON string without escape characters

---

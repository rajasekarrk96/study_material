---
id: "02_03_01"
title: "Comprehensive Operator Systems"
course: "Python"
module: 3
module_title: "Control Flow"
lesson: 1
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["arithmetic", "comparison", "logical", "bitwise", "assignment", "identity", "membership", "operator-precedence", "walrus"]
prerequisites: []
lab_required: true
---

# Comprehensive Operator Systems


## Python Operators Reference

### Arithmetic Operators
```python
17 // 3    # 5  — floor division
17 %  3    # 2  — modulo (remainder)
2  ** 8    # 256 — exponentiation
-7 // 2    # -4  — floor towards negative infinity
-7 %  2    #  1  — always same sign as divisor
divmod(17, 3)   # (5, 2) — quotient and remainder
```

### Comparison Operators
```python
x = 5
1 < x < 10    # True  — Python allows chained comparisons
1 < x and x < 10  # equivalent (but more verbose)
x != 3        # True
x == 5.0      # True  — int and float compared by value
```

### Logical Operators (Short-Circuit)
```python
True  and False   # False
True  or  False   # True
not   True        # False

# Short-circuit — returns actual value, not bool
0 or "default"    # "default"
"value" or "other" # "value"
None and expensive()  # None (expensive() never called)
[] or {}              # {} (first falsy, returns last)

# Practical: default values
name = user_input or "Anonymous"
config = provided_config or load_defaults()
```

### Bitwise Operators
```python
0b1010 & 0b1100   # 0b1000 = 8  — AND
0b1010 | 0b1100   # 0b1110 = 14 — OR
0b1010 ^ 0b1100   # 0b0110 = 6  — XOR
~0b1010           # -11          — NOT (bitwise complement)
1 << 4            # 16           — left shift (multiply by 2^4)
256 >> 3          # 32           — right shift (divide by 2^3)
```

### Identity and Membership
```python
x is None         # identity check
x is not None
"key" in {"key": 1}   # True — dict membership checks keys
3 in [1, 2, 3]         # True
3 not in [1, 2]        # True
```

### Walrus Operator `:=` (Python 3.8+)
```python
# Assign and use in same expression
if (n := len(data)) > 10:
    print(f"Too long: {n}")

# In while loops
while chunk := file.read(8192):
    process(chunk)

# In comprehensions
results = [y for x in data if (y := process(x)) is not None]
```

### Operator Precedence (high → low)
```
()                 — parentheses
**                 — exponentiation
+x, -x, ~x        — unary
*, /, //, %        — multiplicative
+, -               — additive
<<, >>             — bit shift
&                  — bitwise AND
^                  — bitwise XOR
|                  — bitwise OR
==, !=, <, >, is, in  — comparisons
not                — logical NOT
and                — logical AND
or                 — logical OR
:=                 — walrus
```

## Lab Exercise
1. Explain why `-7 % 3 == 2` in Python (not -1 like C)
2. Use short-circuit evaluation to guard an expensive function call
3. Implement a simple bitmask-based permission system using `&` and `|`

---
id: "02_04_05"
title: "Strings and Text Processing"
course: "Python"
module: 4
module_title: "Collections"
lesson: 5
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["str", "f-string", "format", "encode", "decode", "template", "textwrap", "string-methods", "re", "split", "join"]
prerequisites: []
lab_required: true
---

# Strings and Text Processing


## String Fundamentals

```python
# Strings are immutable sequences of Unicode code points
s = "Hello, World!"
len(s)           # 13
s[0]             # 'H'
s[-1]            # '!'
s[0:5]           # 'Hello'
"World" in s     # True

# Immutability — every "change" creates a new string
s.upper()        # returns new string "HELLO, WORLD!"
s                # still "Hello, World!"
```

## String Formatting

```python
name, price, qty = "Widget", 9.99, 42

# f-strings (recommended — fast, readable)
f"Product: {name}, Price: ${price:.2f}, Qty: {qty:,}"
f"{name!r}"         # repr: 'Widget'
f"{name!s}"         # str (default)
f"{name!a}"         # ascii: 'Widget'
f"{2**10 = }"       # debug: '2**10 = 1024'
f"{'hello':>10}"    # right-align in 10 chars: '     hello'
f"{3.14159:.2f}"    # '3.14'
f"{1000000:_}"      # '1_000_000'

# .format()
"{name} costs ${price:.2f}".format(name=name, price=price)
"{0} {1} {0}".format("aba", "c")   # "aba c aba"

# % formatting (legacy)
"%s costs $%.2f" % (name, price)
```

## Essential String Methods

```python
s = "  Hello, World!  "

s.strip()           # "Hello, World!"
s.lstrip()          # "Hello, World!  "
s.rstrip()          # "  Hello, World!"

s.lower()           # "  hello, world!  "
s.upper()           # "  HELLO, WORLD!  "
s.title()           # "  Hello, World!  "
s.swapcase()        # "  hELLO, wORLD!  "

s.split(",")        # ['  Hello', ' World!  ']
s.split()           # ['Hello,', 'World!']   (splits on whitespace)
", ".join(["a","b","c"])  # "a, b, c"

s.replace("World", "Python")
s.startswith("  Hello")   # True
s.endswith("!  ")         # True
s.find("World")    # 9  (-1 if not found)
s.count("l")       # 3
s.center(30, "-")  # "------  Hello, World!  ------"
```

## Multi-line and Raw Strings

```python
multi = '''Line 1
Line 2
Line 3'''

path = r"C:/Users/Raja/Documents"   # raw — no escape processing
regex = r"\d{3}-\d{4}"             # common for regex patterns
```

## String Encoding

```python
text = "Hello, 世界"
encoded = text.encode("utf-8")    # bytes
decoded = encoded.decode("utf-8") # str back

# Common encodings: utf-8, utf-16, ascii, latin-1, cp1252
```

## textwrap for Formatting

```python
import textwrap

long_text = "This is a very long string that needs to be wrapped..."
wrapped = textwrap.fill(long_text, width=40)
dedented = textwrap.dedent('''
    Line 1
    Line 2
''')
```

## Lab Exercise
1. Build a template engine that replaces `{{variable}}` in a string
2. Parse CSV data from a string without the `csv` module using `split()`
3. Write a function that converts snake_case to camelCase and PascalCase

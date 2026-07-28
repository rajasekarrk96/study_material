---
id: "02_10_01"
title: "Regular Expressions"
course: "Python"
module: 10
module_title: "Regular Expressions"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["re", "match", "search", "findall", "finditer", "group", "groups", "compile", "flags", "lookahead", "lookbehind", "named-groups"]
prerequisites: []
lab_required: true
---

# Regular Expressions


## re Module Basics

```python
import re

pattern = r"\d{3}-\d{4}"   # phone number pattern
text = "Call 555-1234 or 800-5678"

# match — only at the beginning of string
re.match(r"\d+", "123 abc")    # Match object
re.match(r"\d+", "abc 123")    # None

# search — anywhere in string
re.search(r"\d+", "abc 123")   # Match at pos 4

# findall — all non-overlapping matches
re.findall(r"\d{3}-\d{4}", text)    # ['555-1234', '800-5678']

# finditer — iterator of Match objects
for m in re.finditer(r"\d{3}-\d{4}", text):
    print(m.group(), m.start(), m.end())
```

## Regex Syntax Reference

```
.       Any character except newline
\d      Digit [0-9]
\D      Non-digit
\w      Word char [a-zA-Z0-9_]
\W      Non-word
\s      Whitespace
\S      Non-whitespace
\b      Word boundary
^       Start of string
$       End of string

{n}     Exactly n repetitions
{n,m}   Between n and m
*       0 or more (greedy)
+       1 or more (greedy)
?       0 or 1 (greedy)
*?      0 or more (lazy/non-greedy)
+?      1 or more (lazy)

[abc]   Character class
[^abc]  Negated class
(abc)   Capturing group
(?:abc) Non-capturing group
|       Alternation
```

## Groups and Named Groups

```python
# Groups
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "Date: 2024-07-28")
m.group(0)   # "2024-07-28" (full match)
m.group(1)   # "2024"
m.group(2)   # "07"
m.groups()   # ("2024", "07", "28")

# Named groups
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
m = re.search(pattern, "Date: 2024-07-28")
m.group("year")   # "2024"
m.groupdict()     # {"year": "2024", "month": "07", "day": "28"}
```

## sub and subn

```python
# Replace matches
re.sub(r"\s+", " ", "  too   many   spaces  ")  # "  too many spaces  "
re.sub(r"^\s+|\s+$", "", "  stripped  ")         # "stripped"

# Replace with function
def double_digit(m):
    return str(int(m.group()) * 2)

re.sub(r"\d+", double_digit, "a1 b22 c333")   # "a2 b44 c666"

# With backreferences
re.sub(r"(\w+) (\w+)", r"\2 \1", "hello world")   # "world hello"
```

## Compiled Patterns

```python
EMAIL_RE = re.compile(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    re.IGNORECASE
)

# Reuse without recompiling
EMAIL_RE.findall(text)
EMAIL_RE.search(text)
```

## Lookahead and Lookbehind

```python
# Positive lookahead (?=...)
re.findall(r"\d+(?= dollars)", "5 dollars and 10 euros")   # ["5"]

# Negative lookahead (?!...)
re.findall(r"\d+(?! euros)", "5 dollars 10 euros")          # ["5"]

# Positive lookbehind (?<=...)
re.findall(r"(?<=\$)\d+", "Total: $50 and $30")            # ["50", "30"]
```

## Lab Exercise
1. Parse log lines: extract timestamp, level, message using named groups
2. Validate password complexity: min 8 chars, uppercase, digit, special char
3. Extract all URLs from HTML using `re.findall()` with a robust pattern

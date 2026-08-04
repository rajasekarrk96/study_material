# Dictionaries

> **Course**: Core Python | **Module**: Collections | **Difficulty**: beginner

---

Python dicts are **ordered** (3.7+), **mutable**, **O(1) average** key lookup.

```python
# Creation
empty = {}
person = {"name": "Raja", "age": 28, "city": "Chennai"}
from_pairs = dict([("a", 1), ("b", 2)])
from_keys = dict.fromkeys(["a","b","c"], 0)   # {"a":0,"b":0,"c":0}

# Access
person["name"]           # "Raja"
person.get("phone")      # None (no KeyError)
person.get("phone", "N/A")  # "N/A"
```

---

```python
d = {"a": 1, "b": 2}

# Update / Add
d["c"] = 3
d.update({"d": 4, "e": 5})
d |= {"f": 6}             # merge operator (3.9+)

# Delete
del d["a"]
val = d.pop("b")          # removes and returns
val = d.pop("x", None)    # safe pop with default
d.popitem()               # removes last inserted (LIFO)
d.clear()

# Membership
"key" in d                # True/False — checks keys only
```

---

```python
for key in d:             # iterates keys
for key in d.keys():      # explicit keys
for val in d.values():    # values
for key, val in d.items():  # key-value pairs

# Get or set default
d.setdefault("count", 0)  # sets "count":0 only if not present
d["count"] = d.get("count", 0) + 1  # increment safely
```

---

```python
squares = {x: x**2 for x in range(1, 6)}
# {1:1, 2:4, 3:9, 4:16, 5:25}

inverted = {v: k for k, v in original.items()}

filtered = {k: v for k, v in data.items() if v > 0}
```

---

```python
from collections import defaultdict, OrderedDict, ChainMap

# defaultdict — auto-creates missing keys
word_count = defaultdict(int)
for word in text.split():
    word_count[word] += 1

# Group by category
groups = defaultdict(list)
for item in items:
    groups[item.category].append(item)

# ChainMap — layered lookup (later dicts override earlier)
defaults = {"color": "red", "size": "M"}
user_prefs = {"size": "L"}
config = ChainMap(user_prefs, defaults)
config["color"]  # "red" (from defaults)
config["size"]   # "L"  (from user_prefs)
```

---

```python
a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}

merged = a | b          # {"x":1, "y":99, "z":3}
a |= b                  # update a in-place
```

---

1. Build a word frequency counter using `defaultdict(int)`
2. Invert a dictionary (values become keys) using dict comprehension
3. Implement a simple cache (memoization dict) for a recursive function

---

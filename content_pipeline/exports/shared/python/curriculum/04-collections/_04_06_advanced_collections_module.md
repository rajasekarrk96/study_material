# Advanced Collections Module

> **Course**: Core Python | **Module**: Collections | **Difficulty**: intermediate

---

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
c = Counter(words)
# Counter({'apple': 3, 'banana': 2, 'cherry': 1})

c.most_common(2)   # [('apple', 3), ('banana', 2)]
c["apple"]         # 3
c["missing"]       # 0 (no KeyError)

# Arithmetic
c1 = Counter(a=3, b=2)
c2 = Counter(a=1, b=4)
c1 + c2    # Counter({'b': 6, 'a': 4})
c1 - c2    # Counter({'a': 2})  (negative dropped)
c1 & c2    # Counter({'a': 1, 'b': 2})  (min)
c1 | c2    # Counter({'b': 4, 'a': 3})  (max)

# Character frequency
Counter("hello world")
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

---

```python
from collections import deque

dq = deque([1, 2, 3], maxlen=5)   # fixed-size sliding window

dq.append(4)        # add to right — O(1)
dq.appendleft(0)    # add to left  — O(1)
dq.pop()            # remove from right — O(1)
dq.popleft()        # remove from left  — O(1)  ← list is O(n)!
dq.rotate(2)        # rotate right by 2
dq.rotate(-1)       # rotate left by 1

# Sliding window maximum
window = deque(maxlen=3)
for x in [1, 3, 5, 2, 4, 7]:
    window.append(x)
    print(max(window))   # max of last 3 elements
```

---

```python
import heapq

# Min-heap
heap = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(heap)
heapq.heappush(heap, 0)
smallest = heapq.heappop(heap)    # 0

# N largest / smallest
heapq.nlargest(3, data)           # [9, 6, 5]
heapq.nsmallest(3, data)          # [0, 1, 1]

# Priority queue with tuples (priority, item)
tasks = []
heapq.heappush(tasks, (2, "medium task"))
heapq.heappush(tasks, (1, "urgent task"))
heapq.heappush(tasks, (3, "low task"))
priority, task = heapq.heappop(tasks)   # (1, "urgent task")
```

---

```python
from collections import UserDict, UserList

class LowercaseDict(UserDict):
    '''Dict that normalises keys to lowercase'''
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)

    def __getitem__(self, key):
        return super().__getitem__(key.lower())

d = LowercaseDict()
d["Name"] = "Raja"
d["name"]    # "Raja"
```

---

1. Count word frequencies in a paragraph using `Counter`, find top 5
2. Implement a browser history (back/forward) using `deque`
3. Build a task scheduler using `heapq` priority queue

---

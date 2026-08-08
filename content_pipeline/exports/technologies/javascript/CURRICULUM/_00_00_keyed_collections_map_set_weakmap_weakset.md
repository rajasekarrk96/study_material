# Keyed Collections Map Set Weakmap Weakset

> **Course**: Git Version Control | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 5.3 Destructuring](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_17_destructuring_assignment_and_spread_rest_operators.md)
- **XP Reward**: +60 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Construct **`Map`** collections supporting objects/functions as keys.
2. Deduplicate array values using **`Set`** collections.
3. Compare **`Map`** vs plain JavaScript `Object`.
4. Prevent memory leaks using **`WeakMap`** and **`WeakSet`** (Weak Reference Garbage Collection).

---

---

Open Node.js REPL to execute Map and Set operations.

---

---

### 3.1 Plain Object vs `Map`

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          PLAIN OBJECT VS MAP MATRIX                         │
├─────────────────┬──────────────────────────────────┬────────────────────────┤
│ Feature         │ Plain Object                     │ ES6 `Map`              │
├─────────────────┼──────────────────────────────────┼────────────────────────┤
│ Key Types       │ Strings & Symbols ONLY           │ ANY Data Type (Objects)│
│ Direct Size     │ Manual (`Object.keys().length`)  │ `map.size` property    │
│ Order           │ Complex insertion ordering       │ Guaranteed Insertion   │
│ Performance     │ Un-optimized for frequent add/del│ Optimized Key/Val Map  │
└─────────────────┴──────────────────────────────────┴────────────────────────┘
```

### 3.2 `WeakMap` & `WeakSet` Garbage Collection
Standard `Map` holds **Strong References** to key objects, preventing V8 garbage collection even if the object is deleted elsewhere. **`WeakMap`** holds **Weak References**—if no other reference to the key object exists, V8 automatically garbage collects both the key AND its associated value!

---

---

```mermaid
flowchart TD
    DomNode[DOM Element Reference] -->|Key in WeakMap| WM[WeakMap Metadata Storage]
    DomNode -->|Removed from DOM| GC[V8 Garbage Collector Sweeps WeakMap Entry Automatically!]
```

---

---

```javascript
// Map, Set, & WeakMap Demonstration

// 1. Map with Object Keys
const sensorMap = new Map();
const node1 = { id: "ESP32-A" };
const node2 = { id: "ESP32-B" };

sensorMap.set(node1, { temp: 24.5, active: true });
sensorMap.set(node2, { temp: 19.8, active: false });

console.log("Sensor 1 Reading:", sensorMap.get(node1));
console.log("Total Monitored Nodes:", sensorMap.size);

// 2. Set Deduplication
const rawCategories = ["Sensor", "Gateway", "Sensor", "Actuator", "Gateway"];
const uniqueCategories = [...new Set(rawCategories)];
console.log("Deduplicated Categories:", uniqueCategories); // ['Sensor', 'Gateway', 'Actuator']

// 3. WeakMap for Private Metadata (No Memory Leaks!)
const privateState = new WeakMap();

class SecureNode {
  constructor(secretKey) {
    // Store private state mapped to 'this' instance in WeakMap!
    privateState.set(this, { secretKey });
  }

  getSecret() {
    return privateState.get(this).secretKey;
  }
}

const nodeInstance = new SecureNode("RSA-90210");
console.log("Secret:", nodeInstance.getSecret());
```

---

---

- **DOM Node Metadata & Event Listeners**: Modern UI frameworks use `WeakMap` to associate private metadata and event listeners with DOM elements without creating memory leaks when elements are removed from the document tree.

---

---

1. Save code as `collections_demo.js`.
2. Run `node collections_demo.js` $\to$ Inspect Map object key retrieval and Set deduplication!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`TypeError: Invalid value used as weak map key`** | Passing a primitive (`number`, `string`) as a `WeakMap` key. | `WeakMap` keys MUST be Objects or Symbols. |

---

---

- **Use `Set` for Array Deduplication**: `[...new Set(array)]` is the single fastest way to deduplicate values.

---

---

### Q1: Why can you not iterate over a `WeakMap` or check its size?
**Answer**: Because `WeakMap` keys are weakly referenced, their presence depends on the current state of V8 Garbage Collection, making the collection non-deterministic. Therefore, `WeakMap` does not support iteration (`for...of`), `.keys()`, `.values()`, or a `.size` property.

---

---

```json
{
  "quiz_title": "Lesson 5.4 Keyed Collections Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which collection guarantees that all contained values are unique?",
      "options": ["Map", "Set", "WeakMap", "Array"],
      "correct_answer_index": 1,
      "explanation": "Set enforces unique value constraints."
    }
  ]
}
```

---

---

Build a private class property store using `WeakMap`.

---

---

**Front**: Can primitive values (numbers/strings) be used as keys in a `WeakMap`?
**Back**: No. `WeakMap` keys MUST be non-primitive Objects (or Symbols).
<!-- flashcard:end -->

---

---

```javascript
const map = new Map([[key, val]]);
const unique = [...new Set(arr)];
```

---

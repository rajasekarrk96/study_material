# Prototypes Prototype Chain And Inheritance

> **Course**: Git Version Control | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 6.4 Promise Combinators](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_22_promise_combinators_all_allsettled_race_any.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Explain JavaScript's **Prototypal Inheritance** paradigm.
2. Trace property and method resolution up the **Prototype Chain**.
3. Create objects using Constructor Functions and link methods to `.prototype`.
4. Inspect and set prototype links using `Object.getPrototypeOf()` and `Object.create()`.

---

---

Open Node.js REPL to execute prototype inspections.

---

---

### 3.1 Prototypal Inheritance vs Class-Based Inheritance
Unlike classical OOP languages (Java, C++) where classes serve as blueprints for instantiating objects, JavaScript objects inherit directly from other objects via a prototype link (`[[Prototype]]` / `__proto__`).

When a property is accessed on an object, V8 searches:
1. Direct own properties on the object instance.
2. The object's prototype (`obj.__proto__`).
3. The prototype's prototype, up until reaching `Object.prototype.__proto__ === null`.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          PROTOTYPE CHAIN RESOLUTION                         │
├─────────────────────────────────────────────────────────────────────────────┤
│ Instance (`sensor`) ──► Sensor.prototype ──► Object.prototype ──► null      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

---

```mermaid
flowchart TD
    Inst[Sensor Instance: own property 'id'] -->|__proto__| Proto[Sensor.prototype: shared method 'read()']
    Proto -->|__proto__| ObjProto[Object.prototype: toString(), valueOf()]
    ObjProto -->|__proto__| Null[null: End of Chain]
```

---

---

```javascript
// Constructor Function & Prototypal Inheritance

function TelemetrySensor(sensorId, location) {
  this.sensorId = sensorId;
  this.location = location;
}

// Attach shared methods to the prototype (Memory Efficient!)
TelemetrySensor.prototype.getReading = function() {
  return { sensorId: this.sensorId, status: "OK", timestamp: Date.now() };
};

const nodeA = new TelemetrySensor("ESP32-01", "Lab-1");
const nodeB = new TelemetrySensor("ESP32-02", "Lab-2");

console.log(nodeA.getReading());

// Prototype Link Verification
console.log(Object.getPrototypeOf(nodeA) === TelemetrySensor.prototype); // true
console.log(nodeA.getReading === nodeB.getReading);                       // true (Shares exact same function memory!)
```

---

---

- **V8 Memory Optimization**: Attaching methods to `.prototype` instead of assigning them inside constructor functions ensures 100,000 object instances share a single method memory address in the V8 heap.

---

---

1. Save code as `prototypes_demo.js`.
2. Run `node prototypes_demo.js` $\to$ Verify shared method memory equality!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **High Memory Heap Bloat** | Defining methods directly inside constructor functions using `this.method = function() {}`. | Move shared methods onto the constructor's `.prototype`. |

---

---

- **Use `Object.getPrototypeOf()`**: Avoid using the legacy deprecated `__proto__` accessor.

---

---

### Q1: What happens when a property is accessed on a JavaScript object that does not exist on the instance itself?
**Answer**: JavaScript searches the object's `[[Prototype]]` link. If not found, it recursively traverses up the Prototype Chain until the property is found or until it reaches `Object.prototype.__proto__` (which is `null`), returning `undefined`.

---

---

```json
{
  "quiz_title": "Lesson 7.1 Prototypes Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "What is the end of the JavaScript Prototype Chain?",
      "options": ["Object.prototype", "null", "undefined", "Function.prototype"],
      "correct_answer_index": 1,
      "explanation": "Object.prototype.__proto__ evaluates to null, ending the chain."
    }
  ]
}
```

---

---

Re-implement inheritance using `Object.create()` without ES6 class keywords.

---

---

**Front**: What function safely retrieves an object's prototype in modern JS?
**Back**: `Object.getPrototypeOf(obj)`.
<!-- flashcard:end -->

---

---

```javascript
Constructor.prototype.method = function() {};
```

---

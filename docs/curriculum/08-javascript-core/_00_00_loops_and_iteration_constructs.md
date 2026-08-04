# Loops And Iteration Constructs

> **Course**: Git Fundamentals | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐ Beginner
- **Prerequisites**: [Lesson 3.1 Conditionals](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_08_conditional_logic_and_guard_clauses.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Construct standard `for`, `while`, and `do...while` loops.
2. Control loop execution flow using `break`, `continue`, and Labeled Statements.
3. Use `for...in` to enumerate Object keys.
4. Use `for...of` to iterate over Array values and Iterable collections.

---

---

Open Node.js REPL to execute loop iterations.

---

---

### 3.1 `for...in` vs `for...of`

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          FOR...IN VS FOR...OF MATRIX                        │
├─────────────────┬──────────────────────────────────┬────────────────────────┤
│ Construct       │ Target Domain                    │ Iterates Over          │
├─────────────────┼──────────────────────────────────┼────────────────────────┤
│ `for...in`      │ Objects (Enumerable Properties)  │ Keys / Property Names  │
│ `for...of`      │ Iterables (Arrays, Strings, Maps)│ Values                 │
└─────────────────┴──────────────────────────────────┴────────────────────────┘
```

> [!CAUTION]
> **Never use `for...in` for Arrays**: `for...in` iterates over string property keys and custom prototype properties, which can cause out-of-order execution on arrays. Always use `for...of` or `.forEach()` for arrays!

---

---

```mermaid
flowchart TD
    Input[Array: ['A', 'B', 'C']] --> ForIn["for...in -> Returns Keys: '0', '1', '2'"]
    Input --> ForOf["for...of -> Returns Values: 'A', 'B', 'C'"]
```

---

---

```javascript
// Loop Mechanics Demonstration

// 1. for...of (Iterable Values)
const telemetryReadings = [22.4, 25.1, 28.9];
for (const temp of telemetryReadings) {
  console.log(`Reading: ${temp}°C`);
}

// 2. for...in (Object Keys)
const deviceConfig = { id: "ESP32", baudRate: 115200, status: "ACTIVE" };
for (const key in deviceConfig) {
  if (Object.hasOwn(deviceConfig, key)) {
    console.log(`Config Key: ${key} -> ${deviceConfig[key]}`);
  }
}

// 3. Labeled Statement Break
outerLoop: for (let r = 0; r < 3; r++) {
  for (let c = 0; c < 3; c++) {
    if (r === 1 && c === 1) {
      break outerLoop; // Breaks directly out of outerLoop!
    }
  }
}
```

---

---

- **Batch Telemetry Packet Processing**: Iterating over multi-frame WebSocket payload buffers using `for...of` to extract binary readings.

---

---

1. Save code as `loops_demo.js`.
2. Run `node loops_demo.js` $\to$ Inspect property enumeration vs array value iteration output!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`TypeError: X is not iterable`** | Attempting to run `for...of` on a plain JS Object. | Use `for...in` or `Object.entries(obj)` with `for...of`. |

---

---

- **Use `for...of` for Arrays**: Guarantees sequential value iteration.

---

---

### Q1: What is the technical difference between `for...in` and `for...of` in JavaScript?
**Answer**: `for...in` iterates over the enumerable *property keys* (strings) of an object, including inherited prototype properties. `for...of` iterates over the data *values* of an iterable object (Arrays, Strings, Maps, Sets) implementing `[Symbol.iterator]`.

---

---

```json
{
  "quiz_title": "Lesson 3.2 Loops Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which loop construct is designed specifically to iterate over the values of an Array?",
      "options": ["for...in", "for...of", "while", "do...while"],
      "correct_answer_index": 1,
      "explanation": "for...of iterates over values of iterable objects like Arrays."
    }
  ]
}
```

---

---

Build an object flattener using recursive iteration over nested structures.

---

---

**Front**: How do you break out of a nested outer loop from inside an inner loop?
**Back**: Using a Labeled Statement: `break labelName;`.
<!-- flashcard:end -->

---

---

```javascript
for (const val of array) {} // Values
for (const key in object) {} // Keys
```

---

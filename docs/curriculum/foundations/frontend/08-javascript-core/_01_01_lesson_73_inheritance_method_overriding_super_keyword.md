# Lesson 7.3 Inheritance, Method Overriding, & Super Keyword

> **Course**: Javascript | **Module**: Module 1 | **Difficulty**: beginner

---

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 7.2 ES6 Classes](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_24_es6_class_syntax_and_constructors.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Create subclass hierarchies using the **`extends`** keyword.
2. Invoke parent constructors correctly using **`super()`**.
3. Override parent methods to customize subclass functionality.
4. Call superclass methods from overridden child methods using `super.methodName()`.

---

---

Open Node.js REPL to execute subclassing scripts.

---

---

### 3.1 Subclassing & Mandatory `super()`
When a class extends a parent class using `extends`, its constructor MUST call **`super()`** *before* accessing `this`. Calling `super()` executes the parent class constructor and initializes the `this` binding:

```javascript
class Parent {
  constructor(name) {
    this.name = name;
  }
}

class Child extends Parent {
  constructor(name, age) {
    super(name); // MUST be called before using 'this'!
    this.age = age;
  }
}
```

---

---

```mermaid
flowchart TD
    Parent[Base Class: Sensor] -->|extends| Child[Subclass: TemperatureSensor]
    Child -->|super()| InitParent[Executes Base Constructor]
    Child -->|super.read()| ParentRead[Delegates to Parent Method]
```

---

---

```javascript
// Class Inheritance & Method Overriding Demonstration

class BaseSensor {
  constructor(sensorId) {
    this.sensorId = sensorId;
  }

  getReading() {
    return { sensorId: this.sensorId, timestamp: Date.now() };
  }
}

// Subclass extending BaseSensor
class HumiditySensor extends BaseSensor {
  constructor(sensorId, humidityLevel) {
    super(sensorId); // Call parent constructor!
    this.humidityLevel = humidityLevel;
  }

  // Method Overriding
  getReading() {
    // Call parent method via super.getReading()
    const baseData = super.getReading();
    return { ...baseData, humidity: `${this.humidityLevel}%` };
  }
}

const humidityNode = new HumiditySensor("HUM-01", 65.4);
console.log(humidityNode.getReading());
```

---

---

- **Custom Error Hierarchies**: Enterprise applications extend standard `Error` (`class DatabaseConnectionError extends Error`) to attach HTTP status codes and diagnostic metadata.

---

---

1. Save code as `inheritance_demo.js`.
2. Run `node inheritance_demo.js` $\to$ Inspect inherited and overridden method output!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`ReferenceError: Must call super constructor in derived class before accessing 'this'`** | Accessing `this.prop` inside a subclass constructor before calling `super()`. | Move `super()` to the first line of the subclass constructor. |

---

---

- **Call `super()` First**: Always invoke `super()` on the very first line of a subclass constructor.

---

---

### Q1: Why is calling `super()` mandatory in a subclass constructor before accessing `this`?
**Answer**: In ES6 subclassing, the `this` object is initialized by the parent class constructor when `super()` is executed. Until `super()` runs, `this` is uninitialized, and accessing it throws a `ReferenceError`.

---

---

```json
{
  "quiz_title": "Lesson 7.3 Inheritance Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which keyword is used by a subclass constructor to invoke the parent class constructor?",
      "options": ["parent()", "super()", "base()", "this()"],
      "correct_answer_index": 1,
      "explanation": "super() invokes the parent class constructor."
    }
  ]
}
```

---

---

Build a custom Error class hierarchy (`ValidationError`, `AuthError`, `NotFoundError`) extending `Error`.

---

---

**Front**: How do you call a parent method `read()` from an overridden subclass method?
**Back**: Using `super.read()`.
<!-- flashcard:end -->

---

---

```javascript
class Child extends Parent {
  constructor(a, b) { super(a); this.b = b; }
}
```

---

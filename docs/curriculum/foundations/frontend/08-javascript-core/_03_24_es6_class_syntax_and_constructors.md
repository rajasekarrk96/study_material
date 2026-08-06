```yaml
schema_version: "2.0"
metadata:
  lesson_id: "JS-MOD07-LES02"
  course_slug: "course-03-javascript"
  course_title: "Course 3: JavaScript & ES6+"
  module_slug: "mod-07-oop-classes-prototypes"
  module_title: "Module 7 - Object-Oriented Programming, Classes, & Prototypes"
  lesson_slug: "es6-class-syntax-and-constructors"
  lesson_title: "Lesson 7.2 ES6 Class Syntax & Constructor Mechanics"
  sort_order: 702

pedagogy:
  difficulty: "beginner"
  estimated_time:
    reading_minutes: 15
    practice_minutes: 20
    quiz_minutes: 10
    total_minutes: 45
  bloom_taxonomy_level: "Apply"
  xp_reward: 50

prerequisites:
  required_lesson_ids:
    - "JS-MOD07-LES01"
  required_skills:
    - "JavaScript Prototypes & Constructor Functions"

skills_acquired:
  - "ES6 Class Syntax (`class ClassName {}`)"
  - "Constructor Initialization (`constructor()`) Mechanics"
  - "Public Instance Fields & Methods"
  - "Understanding Classes as Prototypal Syntactic Sugar"

dependencies:
  software:
    - "VS Code"
    - "Node.js REPL"
  hardware: []

seo_and_social:
  meta_title: "ES6 Classes: class Syntax, constructor, Instance Methods & Prototype Sugar"
  meta_description: "Master ES6 Classes in JavaScript: class declarations, constructor initialization, instance methods, and how classes act as syntactic sugar over prototypes."
  keywords: ["ES6 Classes", "JavaScript class", "constructor method", "Instance Methods", "OOP JavaScript", "Syntactic Sugar"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 7.2 ES6 Class Syntax & Constructor Mechanics

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐ Beginner
- **Prerequisites**: [Lesson 7.1 Prototypes](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_23_prototypes_prototype_chain_and_inheritance.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Write object blueprints using ES6 **`class`** syntax.
2. Initialize instance properties inside the **`constructor()`** method.
3. Define instance methods and understand how V8 automatically attaches them to the underlying prototype.
4. Contrast ES6 classes with legacy constructor functions.

---

## 2. Environment & Prerequisites [id: prerequisites]

Open Node.js REPL to execute class definitions.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 Classes as Syntactic Sugar
ES6 introduced the `class` keyword to provide a clean, declarative syntax familiar to developers coming from Java or C++. Under the hood, ES6 classes are **syntactic sugar** over JavaScript's existing prototype chain:

```javascript
// ES6 Class Definition
class Sensor {
  constructor(id) {
    this.id = id;
  }

  read() {
    return `Reading from ${this.id}`;
  }
}

// Exactly Equivalent to Legacy Prototype Code:
// typeof Sensor === "function"
// Sensor.prototype.read = function() { ... }
```

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    Class[class Sensor] -->|Instantiated via new| Inst[new Sensor('A')]
    Class -->|Auto Method Mapping| Proto[Sensor.prototype.read]
    Inst -->|Inherits| Proto
```

---

## 5. Code & Hardware Implementation [id: syntax]

```javascript
// ES6 Class Declaration Demonstration

class IotDevice {
  // Public Instance Fields
  status = "INITIALIZING";

  constructor(deviceId, firmwareVersion) {
    this.deviceId = deviceId;
    this.firmwareVersion = firmwareVersion;
  }

  // Instance Method (Attached to IotDevice.prototype!)
  connect() {
    this.status = "CONNECTED";
    return `[Device ${this.deviceId}] Connected (FW: v${this.firmwareVersion})`;
  }

  getStatus() {
    return { id: this.deviceId, status: this.status };
  }
}

const gateway = new IotDevice("GW-101", "2.4.1");
console.log(gateway.connect());
console.log(gateway.getStatus());
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Full-Stack Application Services**: Node.js microservices use ES6 classes to encapsulate database repositories, API controllers, and WebSocket stream handlers.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `class_demo.js`.
2. Run `node class_demo.js` $\to$ Inspect class initialization and method invocation!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`TypeError: Class constructor cannot be invoked without 'new'`** | Attempting to call a class as a regular function (`IotDevice()`). | Always instantiate classes using `new IotDevice()`. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Always Use `new`**: ES6 classes strictly require the `new` keyword for instantiation.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: Are ES6 classes true classes like in Java or C++?
**Answer**: No. ES6 classes are syntactic sugar over JavaScript's existing prototypal inheritance model. `typeof MyClass` evaluates to `"function"`, and methods defined inside the class body are automatically bound to `MyClass.prototype`.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 7.2 ES6 Classes Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "What does `typeof MyClass` evaluate to in JavaScript?",
      "options": ["class", "object", "function", "undefined"],
      "correct_answer_index": 2,
      "explanation": "Classes are special functions under the hood."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Build an e-commerce Product class with methods for price calculation and stock updates.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What special method initializes instance properties in an ES6 class?
**Back**: `constructor()`.
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```javascript
class Device {
  constructor(id) { this.id = id; }
  read() { return this.id; }
}
```

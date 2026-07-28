```yaml
schema_version: "2.0"
metadata:
  lesson_id: "JS-MOD07-LES03"
  course_slug: "course-03-javascript"
  course_title: "Course 3: JavaScript & ES6+"
  module_slug: "mod-07-oop-classes-prototypes"
  module_title: "Module 7 - Object-Oriented Programming, Classes, & Prototypes"
  lesson_slug: "inheritance-method-overriding-and-super"
  lesson_title: "Lesson 7.3 Inheritance, Method Overriding, & Super Keyword"
  sort_order: 703

pedagogy:
  difficulty: "intermediate"
  estimated_time:
    reading_minutes: 15
    practice_minutes: 20
    quiz_minutes: 10
    total_minutes: 45
  bloom_taxonomy_level: "Apply"
  xp_reward: 50

prerequisites:
  required_lesson_ids:
    - "JS-MOD07-LES02"
  required_skills:
    - "ES6 Class Syntax & Constructor Mechanics"

skills_acquired:
  - "Subclass Inheritance using `extends`"
  - "Mandatory Parent Constructor Invocation (`super()`) Rules"
  - "Method Overriding in Subclasses"
  - "Accessing Parent Class Methods via `super.methodName()`"

dependencies:
  software:
    - "VS Code"
    - "Node.js REPL"
  hardware: []

seo_and_social:
  meta_title: "ES6 Class Inheritance: extends, super(), Method Overriding & Polymorphism"
  meta_description: "Master ES6 Class Inheritance: subclassing with extends, mandatory super() constructor calls, method overriding, and super.method() invocation."
  keywords: ["ES6 Class Inheritance", "extends keyword", "super constructor", "Method Overriding", "Polymorphism JavaScript"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 7.3 Inheritance, Method Overriding, & Super Keyword

## 1. Overview & Learning Objectives [id: overview]

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

## 2. Environment & Prerequisites [id: prerequisites]

Open Node.js REPL to execute subclassing scripts.

---

## 3. Theoretical Foundations [id: theory]

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

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    Parent[Base Class: Sensor] -->|extends| Child[Subclass: TemperatureSensor]
    Child -->|super()| InitParent[Executes Base Constructor]
    Child -->|super.read()| ParentRead[Delegates to Parent Method]
```

---

## 5. Code & Hardware Implementation [id: syntax]

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

## 6. Enterprise Real-World Applications [id: examples]

- **Custom Error Hierarchies**: Enterprise applications extend standard `Error` (`class DatabaseConnectionError extends Error`) to attach HTTP status codes and diagnostic metadata.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `inheritance_demo.js`.
2. Run `node inheritance_demo.js` $\to$ Inspect inherited and overridden method output!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`ReferenceError: Must call super constructor in derived class before accessing 'this'`** | Accessing `this.prop` inside a subclass constructor before calling `super()`. | Move `super()` to the first line of the subclass constructor. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Call `super()` First**: Always invoke `super()` on the very first line of a subclass constructor.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: Why is calling `super()` mandatory in a subclass constructor before accessing `this`?
**Answer**: In ES6 subclassing, the `this` object is initialized by the parent class constructor when `super()` is executed. Until `super()` runs, `this` is uninitialized, and accessing it throws a `ReferenceError`.

---

## 11. Self-Assessment Quiz [id: quiz]

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

## 12. Portfolio Assignment & Challenge [id: lab]

Build a custom Error class hierarchy (`ValidationError`, `AuthError`, `NotFoundError`) extending `Error`.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: How do you call a parent method `read()` from an overridden subclass method?
**Back**: Using `super.read()`.
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```javascript
class Child extends Parent {
  constructor(a, b) { super(a); this.b = b; }
}
```

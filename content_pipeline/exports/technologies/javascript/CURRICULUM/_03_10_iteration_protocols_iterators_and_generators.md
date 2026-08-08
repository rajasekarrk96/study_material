```yaml
schema_version: "2.0"
metadata:
  lesson_id: "JS-MOD03-LES03"
  course_slug: "course-03-javascript"
  course_title: "Course 3: JavaScript & ES6+"
  module_slug: "mod-03-control-flow-loops"
  module_title: "Module 3 - Control Flow, Loops, & Iteration Protocols"
  lesson_slug: "iteration-protocols-iterators-and-generators"
  lesson_title: "Lesson 3.3 Iteration Protocols, Iterators, & Generators"
  sort_order: 303

pedagogy:
  difficulty: "advanced"
  estimated_time:
    reading_minutes: 20
    practice_minutes: 25
    quiz_minutes: 10
    total_minutes: 55
  bloom_taxonomy_level: "Apply"
  xp_reward: 70

prerequisites:
  required_lesson_ids:
    - "JS-MOD03-LES02"
  required_skills:
    - "JavaScript Loops & Symbol Primitive Data Type"

skills_acquired:
  - "Iterable Protocol (`[Symbol.iterator]`)"
  - "Iterator Protocol (`next()` method returning `{ value, done }`)"
  - "Custom Iterable Data Structure Construction"
  - "Generator Functions (`function*` & `yield` Keyword)"
  - "Lazy Infinite Sequence Generation"

dependencies:
  software:
    - "VS Code"
    - "Node.js REPL"
  hardware: []

seo_and_social:
  meta_title: "JavaScript Iteration Protocols: Iterators, Symbol.iterator & Generators"
  meta_description: "Master JavaScript iteration protocols: Iterable protocol, Iterator next() method, custom Symbol.iterator objects, generator function* and yield."
  keywords: ["JavaScript Iterators", "Symbol.iterator", "Generator Functions", "yield keyword", "Iterable Protocol", "Lazy Evaluation"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 3.3 Iteration Protocols, Iterators, & Generators

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐⭐ Advanced
- **Prerequisites**: [Lesson 3.2 Loops](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_03_javascript/_03_09_loops_and_iteration_constructs.md)
- **XP Reward**: +70 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Deconstruct the **Iterable Protocol** (`[Symbol.iterator]`).
2. Implement the **Iterator Protocol** (`next()` method returning `{ value, done }`).
3. Build custom iterable objects compatible with `for...of` and spread syntax (`...`).
4. Write Generator Functions (`function*`) using the **`yield`** keyword for lazy infinite sequence evaluation.

---

## 2. Environment & Prerequisites [id: prerequisites]

Open Node.js REPL to execute iterator and generator code.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 The Iterable & Iterator Protocols
- **Iterable**: An object that defines a method with key `[Symbol.iterator]`, which returns an Iterator.
- **Iterator**: An object implementing a `next()` method returning an result object with structure: `{ value: any, done: boolean }`.

```javascript
// Manual Iterator Traversal
const str = "HI";
const iterator = str[Symbol.iterator]();

console.log(iterator.next()); // { value: 'H', done: false }
console.log(iterator.next()); // { value: 'I', done: false }
console.log(iterator.next()); // { value: undefined, done: true }
```

### 3.2 Generator Functions (`function*`)
Generators provide factory functions for producing iterators cleanly using `yield`. Execution pauses at each `yield` and resumes on subsequent `.next()` calls:

```python
function* fibonacci() {
  let [prev, curr] = [0, 1];
  while (true) {
    yield curr;
    [prev, curr] = [curr, prev + curr];
  }
}
```

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    Gen[Generator Function*] -->|Invocated| GenObj[Generator Object]
    GenObj -->|Call .next()| Exec[Executes until yield keyword]
    Exec -->|Yield Value| Pause[Pauses Execution State]
    Pause -->|Call .next() again| Exec
```

---

## 5. Code & Hardware Implementation [id: syntax]

```javascript
// Custom Iterable & Generator Demonstration

// 1. Custom Iterable Object
const customRange = {
  start: 1,
  end: 3,
  [Symbol.iterator]() {
    let current = this.start;
    const last = this.end;
    return {
      next() {
        if (current <= last) {
          return { value: current++, done: false };
        }
        return { value: undefined, done: true };
      }
    };
  }
};

for (const num of customRange) {
  console.log("Custom Iterable Num:", num);
}

// 2. Generator Function (Lazy Sequence)
function* idGenerator() {
  let id = 100;
  while (id < 103) {
    yield `SENSOR-NODE-${id++}`;
  }
}

const gen = idGenerator();
console.log(gen.next().value); // "SENSOR-NODE-100"
console.log(gen.next().value); // "SENSOR-NODE-101"
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Paginated API Stream Processors**: Large enterprise datasets (fetching 1,000,000 records from a database) use Generator functions to stream and process chunks lazy-loaded into memory one page at a time.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `iterators_demo.js`.
2. Run `node iterators_demo.js` $\to$ Observe custom iterable and generator execution!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`TypeError: X is not iterable`** | Passing a custom object into `for...of` or `[...]` spread without defining `[Symbol.iterator]`. | Implement `[Symbol.iterator]()` or use a Generator function. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Use Generators for Custom Iterators**: `function*` eliminates manual state tracking in iterator `next()` methods.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: How does a Generator function differ from a regular function in JavaScript?
**Answer**: A regular function executes to completion and returns a single value. A Generator function (`function*`) returns a Generator object, pauses execution at each `yield` keyword, preserves its execution state (local variables and stack frame), and resumes when `.next()` is called.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 3.3 Iterators Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which Symbol key must an object define to conform to the Iterable Protocol?",
      "options": ["Symbol.iterator", "Symbol.iterable", "Symbol.async", "Symbol.toPrimitive"],
      "correct_answer_index": 0,
      "explanation": "Symbol.iterator is the well-known symbol defining the iterable protocol."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Build a lazy memory-efficient CSV row parser generator.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What structure does an Iterator `next()` method return?
**Back**: An object containing `{ value: any, done: boolean }`.
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```javascript
function* gen() { yield 1; }
```

# Python 312 Structural Pattern Matching

> **Course**: Git Version Control | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: Python Conditionals & Control Flow
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Implement Structural Pattern Matching using Python 3.10+ `match` and `case` statements.
2. Destructure sequences (lists/tuples) and mappings (dictionaries) directly inside patterns.
3. Apply **Guard Clauses** (`if` conditions) within `case` blocks.
4. Match custom Class Instances (`case Point(x, y)`).

---

---

Ensure Python 3.10+ is installed:
- Run `python --version` $\to$ Must output `Python 3.10.x` or higher.

---

---

### 3.1 `match/case` vs Legacy `if-elif-else`
Traditional `if-elif-else` chains test booleans sequentially. **Structural Pattern Matching** evaluates data structure *shapes* and values simultaneously, destructuring components into local variables:

```python
# Modern Structural Pattern Matching
match command.split():
    case ["quit"]:
        exit()
    case ["move", ("left" | "right" | "up" | "down") as direction]:
        move(direction)
    case ["teleport", int(x), int(y)]:
        teleport(x, y)
    case _:
        print("Unknown command")
```

---

---

```mermaid
flowchart TD
    Input[Incoming Command List] --> Match[match command]
    Match --> Case1{"case ['quit']"}
    Match --> Case2{"case ['move', direction]"}
    Match --> Case3{"case ['teleport', x, y]"}
    Match --> Default{"case _ (Wildcard Catch-all)"}
```

---

---

```python
from dataclasses import dataclass

@dataclass
class Command:
    action: str
    amount: float

def process_event(event: tuple | dict | Command):
    match event:
        # 1. Sequence Pattern with Guard Clause
        case ("TEMP_SENSOR", temp) if temp > 50.0:
            print(f"CRITICAL ALARM: Temperature {temp}°C exceeds safety threshold!")

        # 2. Mapping Pattern (Dictionary)
        case {"type": "PAYMENT", "amount": val, "status": "SUCCESS"}:
            print(f"Processed payment of ${val:.2f}")

        # 3. Class Instance Pattern
        case Command(action="REBOOT", amount=_):
            print("Executing system reboot...")

        # 4. Wildcard Catch-all
        case _:
            print("Unhandled event payload format.")

# Test Execution
process_event(("TEMP_SENSOR", 62.5))
process_event({"type": "PAYMENT", "amount": 150.00, "status": "SUCCESS"})
```

---

---

- **API Event Dispatchers**: Microservices processing heterogeneous Kafka JSON events use `match/case` to cleanly route payloads based on internal schema shapes.

---

---

1. Save code as `pattern_demo.py`.
2. Run `python pattern_demo.py` $\to$ Inspect clean pattern matching output!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`SyntaxError: invalid syntax`** | Running `match/case` code on Python 3.9 or older. | Upgrade to Python 3.10+ runtime environment. |

---

---

- **Use Wildcard `case _` Last**: Always include a catch-all `case _` at the end of a match block.

---

---

### Q1: What makes structural pattern matching different from C/Java `switch` statements?
**Answer**: C/Java `switch` statements match simple scalar values (integers, strings). Python's `match/case` performs structural destructuring—matching sequence lengths, dictionary keys, class shapes, type constraints, and applying conditional guards simultaneously.

---

---

```json
{
  "quiz_title": "Lesson 1.5 Pattern Matching Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which symbol represents the wildcard catch-all case in Python structural pattern matching?",
      "options": ["*", "case default", "case _", "else"],
      "correct_answer_index": 2,
      "explanation": "case _ is the wildcard catch-all pattern."
    }
  ]
}
```

---

---

Build a CLI command parser handling 5 complex command structures using `match/case`.

---

---

**Front**: How do you add an if condition inside a `case` pattern?
**Back**: Using a Guard Clause: `case pattern if condition:`.
<!-- flashcard:end -->

---

---

```python
match payload:
    case {"status": 200, "data": body}:
        process(body)
    case _:
        handle_error()
```

---

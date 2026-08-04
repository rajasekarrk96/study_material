```yaml
schema_version: "2.0"
metadata:
  lesson_id: "JAVA-MOD02-LES03"
  course_slug: "course-03-java"
  course_title: "Course 3: Java 21 LTS Enterprise Development"
  module_slug: "mod-02-modern-class-types"
  module_title: "Module 2 - Modern Class Types & Object-Oriented Java"
  lesson_slug: "java21-record-classes-and-dto-patterns"
  lesson_title: "Lesson 2.3 Java 21 Record Classes & DTO Patterns"
  sort_order: 203

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
    - "JAVA-MOD02-LES01"
  required_skills:
    - "Java OOP & Encapsulation Principles"

skills_acquired:
  - "Immutable Data Record Definition (`record Point(int x, int y)`)"
  - "Compact Constructor Validation Mechanics"
  - "Custom Record Methods & Static Fields"
  - "Data Transfer Object (DTO) Pattern Implementation"

dependencies:
  software:
    - "VS Code / IntelliJ IDEA"
    - "JDK 21 LTS"
  hardware: []

seo_and_social:
  meta_title: "Java 21 Record Classes: Immutable Records, Compact Constructors & DTOs"
  meta_description: "Master Java 21 LTS Record Classes: concise immutable data carriers, compact constructors, accessor methods, equals/hashCode/toString generation, and DTOs."
  keywords: ["Java 21", "Java Record Class", "Immutable Data Carrier", "Compact Constructor", "Java DTO Pattern", "Lombok alternative"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 2.3 Java 21 Record Classes & DTO Patterns

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: Java Classes & Encapsulation
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Define concise immutable data carriers using Java 21 **Record Classes**.
2. Understand auto-generated record components (`private final` fields, accessors, `equals()`, `hashCode()`, `toString()`).
3. Implement validation inside **Compact Constructors**.
4. Replace verbose boilerplate DTO classes (and Lombok `@Value`) with native Java records.

---

## 2. Environment & Prerequisites [id: prerequisites]

Ensure JDK 21 LTS is installed:
- Run `java -version` $\to$ Must output `openjdk 21` or higher.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 Eliminating DTO Boilerplate
Before Java 16/21, creating a simple immutable Data Transfer Object (DTO) required 50+ lines of verbose Java boilerplate (private final fields, constructor, getters, `equals`, `hashCode`, `toString`).

**Java Record Classes** reduce this entire declaration to a single line:

```java
// Modern Java 21 Record Class Declaration (1 Line!)
public record UserDTO(Long id, String username, String email) {}
```

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       JAVA 21 RECORD AUTO-GENERATION MATRIX                 │
├─────────────────┬───────────────────────────────────────────────────────────┤
│ Component       │ Automatically Generated Behavior                           │
├─────────────────┼───────────────────────────────────────────────────────────┤
│ Fields          │ `private final` instance fields for each header component │
│ Accessors       │ `id()`, `username()`, `email()` (No 'get' prefix!)       │
│ Methods         │ Value-based `equals()`, `hashCode()`, and `toString()`    │
│ Class           │ Implicitly `final` (Cannot be extended)                  │
└─────────────────┴───────────────────────────────────────────────────────────┘
```

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    Header["public record UserDTO(Long id, String name)"] --> Fields["Auto: private final Long id; private final String name;"]
    Header --> Methods["Auto: id(), name(), equals(), hashCode(), toString()"]
    Header --> Compact["Compact Constructor: Validation rules enforced before instantiation"]
```

---

## 5. Code & Hardware Implementation [id: syntax]

```java
// Java 21 Record with Compact Constructor Validation

public record SensorTelemetry(String nodeId, double temperature, long timestamp) {
    
    // Compact Constructor (No parameters listed!)
    public SensorTelemetry {
        if (temperature < -273.15) {
            throw new IllegalArgumentException("Temperature below Absolute Zero!");
        }
        if (nodeId == null || nodeId.isBlank()) {
            throw new IllegalArgumentException("Node ID cannot be blank.");
        }
        // Components are automatically assigned at the end of compact constructor!
    }

    // Custom Instance Method
    public boolean isFeverish() {
        return temperature > 38.0;
    }
}

class RecordDemo {
    public static void main(String[] args) {
        SensorTelemetry reading = new SensorTelemetry("ESP32-NODE-1", 39.2, System.currentTimeMillis());
        
        // Record Accessors (No 'get' prefix!)
        System.out.println("Node ID: " + reading.nodeId());
        System.out.println("Temperature: " + reading.temperature() + "°C");
        System.out.println("Is Feverish? " + reading.isFeverish());
        System.out.println("Auto toString: " + reading);
    }
}
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Spring Boot REST DTOs**: Modern Spring Boot 3+ REST controllers use Java Records to map incoming JSON request payloads directly into strongly-typed immutable records with Jackson JSON deserialization.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `RecordDemo.java`.
2. Compile and run: `javac RecordDemo.java` $\to$ `java RecordDemo`.

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`Cannot assign a value to final variable`** | Attempting to mutate a record component value after construction. | Records are strictly immutable; create a new record instance with modified values instead. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Use Compact Constructors for Validation**: Omit parameter lists in validation constructors.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: Can a Java Record Class extend another class or be extended?
**Answer**: No. All Java records implicitly extend `java.lang.Record` and are implicitly `final`. Therefore, a record cannot extend any other class, nor can another class extend a record. However, records CAN implement interfaces.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 2.3 Java Records Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "What is the method name used to read the 'email' component from `record User(String email)`?",
      "options": ["getEmail()", "email()", "get_email()", "readEmail()"],
      "correct_answer_index": 1,
      "explanation": "Record accessor methods share the exact name of the component (email())."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Build an immutable REST API response envelope using Java 21 Records and custom validation.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: How do accessors in Java Records differ from standard JavaBeans getters?
**Back**: Record accessors match the component name directly (`id()`), whereas JavaBeans use `getId()`.
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```java
public record User(Long id, String name) {}
```

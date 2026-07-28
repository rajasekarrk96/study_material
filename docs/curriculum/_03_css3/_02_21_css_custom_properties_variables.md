```yaml
schema_version: "2.0"
metadata:
  lesson_id: "CSS3-MOD07-LES01"
  course_slug: "course-02-css3"
  course_title: "Course 2: CSS3"
  module_slug: "mod-07-advanced-css-architecture"
  module_title: "Module 7 - Advanced CSS Architecture & Modern Specifications"
  lesson_slug: "css-custom-properties-variables"
  lesson_title: "Lesson 7.1 CSS Custom Properties (Variables)"
  sort_order: 701

pedagogy:
  difficulty: "intermediate"
  estimated_time:
    reading_minutes: 20
    practice_minutes: 25
    quiz_minutes: 10
    total_minutes: 55
  bloom_taxonomy_level: "Apply"
  xp_reward: 60

prerequisites:
  required_lesson_ids:
    - "CSS3-MOD01-LES03"
  required_skills:
    - "CSS Cascade & Inheritance"

skills_acquired:
  - "Custom Property Syntax (`--variable-name` & `var()`)"
  - "Global `:root` Scope vs Local Scope Declarations"
  - "Fallback Property Values (`var(--primary, #3b82f6)`)"
  - "Typed Custom Properties (`@property` Rule)"
  - "JavaScript Interaction (`setProperty`, `getPropertyValue`)"

dependencies:
  software:
    - "VS Code"
  hardware: []

seo_and_social:
  meta_title: "CSS3 Custom Properties (Variables): :root Scope, Fallbacks & @property"
  meta_description: "Master CSS Custom Properties (CSS Variables): --var syntax, var() fallback values, global :root scope, JavaScript setProperty, and typed @property."
  keywords: ["CSS Variables", "Custom Properties", "--var", "var()", ":root", "@property", "JS setProperty"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 7.1 CSS Custom Properties (Variables)

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 1.3 Cascade, Specificity, & Inheritance](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_02_css3/_02_03_cascade_specificity_and_inheritance.md)
- **XP Reward**: +60 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Declare and consume CSS Custom Properties (`--variable-name` & `var()`).
2. Scope variables globally on `:root` or locally within component blocks.
3. Provide fallback values inside `var(--name, fallback)`.
4. Register typed custom properties using the **`@property`** API.
5. Manipulate CSS variables dynamically via JavaScript (`element.style.setProperty()`).

---

## 2. Environment & Prerequisites [id: prerequisites]

Inspect custom properties in Chrome DevTools Styles panel.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 Syntax & Scoping
CSS variables begin with `--` and are inherited through the DOM tree:

```css
/* Global Scope */
:root {
  --primary-color: #3b82f6;
  --card-padding: 1.5rem;
}

/* Consumption with Fallback */
.card {
  background-color: var(--primary-color, #0f172a);
  padding: var(--card-padding);
}
```

### 3.2 Typed Custom Properties (`@property`)
Allows animating CSS variables by explicitly registering syntax types (`<color>`, `<length>`, `<angle>`):

```css
@property --gradient-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}
```

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    JS[JavaScript: setProperty('--theme-color', '#22c55e')] --> Root[:root Scope CSS Variables]
    Root --> Component1[Card Component A]
    Root --> Component2[Card Component B]
    Component1 --> UI[UI Theme Updates Instantly Across All Components!]
```

---

## 5. Code & Hardware Implementation [id: syntax]

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CSS Variables Demo</title>
  <style>
    :root {
      --bg-color: #0f172a;
      --text-color: #f8fafc;
      --accent-color: #38bdf8;
    }
    
    body { background: var(--bg-color); color: var(--text-color); font-family: system-ui; padding: 2rem; }
    button { background: var(--accent-color); color: #000; border: none; padding: 10px 20px; cursor: pointer; }
  </style>
</head>
<body>
  <h1>Dynamic Theme Engine</h1>
  <button onclick="toggleTheme()">Toggle Theme</button>

  <script>
    function toggleTheme() {
      const root = document.documentElement;
      const isDark = root.style.getPropertyValue('--bg-color') === '#ffffff';
      root.style.setProperty('--bg-color', isDark ? '#0f172a' : '#ffffff');
      root.style.setProperty('--text-color', isDark ? '#f8fafc' : '#0f172a');
    }
  </script>
</body>
</html>
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Design Tokens & Dark Mode**: Modern design systems export design tokens (colors, spacing) as CSS Custom Properties on `:root`, allowing instant theme switching.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `variables_demo.html`.
2. Click **Toggle Theme** button $\rightarrow$ Observe CSS variables update dynamically in real time via JavaScript!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Variable Fails to Render** | Misspelling `--var-name` or omitting double hyphens `--`. | Custom property names MUST begin with `--`. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Declare Design Tokens on `:root`**: Centralize colors, typography, and spacing variables.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: How do CSS Custom Properties differ from Sass/SCSS variables?
**Answer**: Sass variables are compiled away at build time into static CSS values. CSS Custom Properties exist dynamically in the browser DOM at runtime, participating in the Cascade and reacting instantly to JavaScript modifications.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 7.1 Variables Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "What prefix is required for all CSS Custom Property names?",
      "options": ["$", "@", "--", "var-"],
      "correct_answer_index": 2,
      "explanation": "All custom property names must begin with double hyphens (--)."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Build a multi-theme UI switcher (Light, Dark, Cyberpunk) using CSS Custom Properties.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What JS method updates a CSS variable on `:root` dynamically?
**Back**: `document.documentElement.style.setProperty('--var-name', 'value')`
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```css
:root { --primary: #3b82f6; }
.btn { background: var(--primary); }
```

```yaml
schema_version: "2.0"
metadata:
  lesson_id: "CSS3-MOD06-LES01"
  course_slug: "course-02-css3"
  course_title: "Course 2: CSS3"
  module_slug: "mod-06-responsive-design-queries"
  module_title: "Module 6 - Responsive Web Design, Media Queries, & Container Queries"
  lesson_slug: "responsive-architecture-principles"
  lesson_title: "Lesson 6.1 Responsive Architecture Principles"
  sort_order: 601

pedagogy:
  difficulty: "beginner"
  estimated_time:
    reading_minutes: 15
    practice_minutes: 20
    quiz_minutes: 10
    total_minutes: 45
  bloom_taxonomy_level: "Understand"
  xp_reward: 50

prerequisites:
  required_lesson_ids:
    - "CSS3-MOD02-LES04"
  required_skills:
    - "CSS Box Model & Viewport Sizing Units"

skills_acquired:
  - "Mobile-First vs Desktop-First Architectural Paradigms"
  - "Viewport Meta Tag Configuration (`width=device-width, initial-scale=1.0`)"
  - "Fluid Grids & Flexible Layout Geometry"
  - "Device Breakpoint Selection Strategies"

dependencies:
  software:
    - "VS Code"
    - "Chrome DevTools Device Mode"
  hardware: []

seo_and_social:
  meta_title: "Responsive Web Design (RWD) Architecture: Mobile-First Strategy"
  meta_description: "Master Responsive Web Design (RWD) principles: Mobile-First vs Desktop-First, Viewport meta tag configuration, fluid layouts, and breakpoint selection."
  keywords: ["Responsive Web Design", "RWD", "Mobile First", "Viewport Meta Tag", "Breakpoints", "Fluid Layouts"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 6.1 Responsive Architecture Principles

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 45 Minutes (15m Reading | 20m Practice | 10m Quiz)
- **Difficulty Level**: ⭐ Beginner
- **Prerequisites**: [Lesson 2.4 Sizing Units](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_02_css3/_02_07_sizing_units_and_intrinsic_sizing.md)
- **XP Reward**: +50 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Contrast **Mobile-First** vs Desktop-First architectural paradigms.
2. Configure the mandatory HTML `<meta name="viewport">` tag.
3. Establish fluid layout geometry using percentage and relative units.
4. Select content-driven device breakpoints rather than hardcoded device widths.

---

## 2. Environment & Prerequisites [id: prerequisites]

Inspect pages across simulated mobile viewports in Chrome DevTools:
- Open DevTools (`F12`) $\rightarrow$ Click **Toggle device toolbar** (`Ctrl+Shift+M` or `Cmd+Shift+M`).

---

## 3. Theoretical Foundations [id: theory]

### 3.1 Mobile-First vs Desktop-First
- **Mobile-First (Industry Standard)**: Base CSS rules target small mobile screens without media queries. Overrides for larger screens are added progressively using `min-width` media queries.
- **Desktop-First (Legacy)**: Base CSS rules target 1920px desktops, adding `max-width` overrides to shrink components for mobile.

```
Mobile-First Progression:   Base Styles (Mobile) ──► min-width: 640px (Tablet) ──► min-width: 1024px (Desktop)
```

### 3.2 The Viewport Meta Tag

> [!IMPORTANT]
> Without the Viewport meta tag, mobile browsers render pages at a fake 980px desktop resolution, shrinking text to unreadable microscopic sizes!

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
graph LR
    Mobile["Base CSS (Mobile Default)"] -->|@media (min-width: 640px)| Tablet["Tablet Overrides"]
    Tablet -->|@media (min-width: 1024px)| Desktop["Desktop Overrides"]
```

---

## 5. Code & Hardware Implementation [id: syntax]

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mobile-First Architecture</title>
  <style>
    /* 1. Base Mobile Styles (Default) */
    body { font-family: system-ui; padding: 1rem; background: #0f172a; color: #fff; }
    .layout { display: flex; flex-direction: column; gap: 1rem; }
    .card { background: #1e293b; padding: 1rem; border-radius: 8px; }

    /* 2. Tablet Breakpoint Progressive Enhancement */
    @media (min-width: 640px) {
      .layout { flex-direction: row; }
      .card { flex: 1; }
    }
  </style>
</head>
<body>
  <div class="layout">
    <div class="card">Telemetry Node A</div>
    <div class="card">Telemetry Node B</div>
  </div>
</body>
</html>
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Google Mobile-First Indexing**: Google ranks websites based on their mobile rendering experience. Mobile-First CSS architecture ensures fast mobile load times.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `rwd_demo.html`.
2. Toggle Device Toolbar in Chrome DevTools $\rightarrow$ Drag viewport width below 640px (column stack) and above 640px (horizontal row)!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Mobile Site Microscopic / Unreadable** | Missing `<meta name="viewport">` tag in HTML `<head>`. | Add `<meta name="viewport" content="width=device-width, initial-scale=1.0">`. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Adopt Mobile-First Strategy**: Write base CSS for mobile viewports using `min-width` media queries.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: Why is Mobile-First CSS architecture preferred over Desktop-First?
**Answer**: Mobile-First progressively enhances layouts as viewport size increases. Mobile devices parse less CSS payload, reducing network overhead on slow cellular connections.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 6.1 RWD Principles Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which media query type is used in Mobile-First CSS architecture?",
      "options": ["min-width", "max-width", "orientation: landscape", "max-device-width"],
      "correct_answer_index": 0,
      "explanation": "min-width queries progressively add styles as viewport width grows wider."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Convert a legacy desktop-first layout into a clean mobile-first responsive architecture.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What tag tells mobile browsers to match page width to physical device screen width?
**Back**: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```css
/* Base Mobile Rules First */
@media (min-width: 768px) { /* Tablet Overrides */ }
```

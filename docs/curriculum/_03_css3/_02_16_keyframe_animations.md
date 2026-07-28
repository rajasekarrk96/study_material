```yaml
schema_version: "2.0"
metadata:
  lesson_id: "CSS3-MOD05-LES03"
  course_slug: "course-02-css3"
  course_title: "Course 2: CSS3"
  module_slug: "mod-05-transitions-transforms-animations"
  module_title: "Module 5 - Transitions, 2D/3D Transforms, & Animations"
  lesson_slug: "keyframe-animations"
  lesson_title: "Lesson 5.3 Keyframe Animations"
  sort_order: 503

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
    - "CSS3-MOD05-LES02"
  required_skills:
    - "CSS 2D/3D Transforms"

skills_acquired:
  - "Keyframe Declaration Syntax (`@keyframes name { 0% {}, 100% {} }`)"
  - "Animation Control (`animation-iteration-count`, `animation-direction`, `animation-play-state`)"
  - "Animation Persistence (`animation-fill-mode: forwards | backwards | both`)"
  - "Scroll-Driven Animations Overview (`animation-timeline: scroll()`)"
  - "Animation Shorthand Syntax"

dependencies:
  software:
    - "VS Code"
  hardware: []

seo_and_social:
  meta_title: "CSS3 Keyframe Animations: @keyframes, fill-mode & Scroll-Driven Animations"
  meta_description: "Master CSS3 animations: @keyframes rule, animation shorthand, animation-fill-mode, iteration counts, paused state, and scroll-driven animation-timeline."
  keywords: ["CSS Animations", "@keyframes", "animation shorthand", "animation-fill-mode", "animation-iteration-count", "scroll-driven animation"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 5.3 Keyframe Animations

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐⭐ Advanced
- **Prerequisites**: [Lesson 5.2 2D & 3D Transformations](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_02_css3/_02_15_2d_and_3d_transformations.md)
- **XP Reward**: +70 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Define complex multi-step animation sequences using `@keyframes`.
2. Configure animation properties (`animation-name`, `duration`, `timing-function`, `delay`, `iteration-count`, `direction`, `fill-mode`, `play-state`).
3. Lock end states after animation completion using `animation-fill-mode: forwards`.
4. Pause and resume animations dynamically using `animation-play-state: paused`.
5. Implement modern **Scroll-Driven Animations** using `animation-timeline: scroll()`.

---

## 2. Environment & Prerequisites [id: prerequisites]

Open VS Code and create `keyframes_demo.html` to write keyframe animations.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 `@keyframes` Syntax & Shorthand
Unlike Transitions (which require state triggers like `:hover`), Keyframe Animations run automatically on page load or class addition:

```css
@keyframes pulse-ring {
  0%   { transform: scale(0.95); opacity: 0.8; }
  50%  { transform: scale(1.05); opacity: 1; }
  100% { transform: scale(0.95); opacity: 0.8; }
}

/* Shorthand: name | duration | timing | delay | iterations | direction | fill-mode */
.status-indicator {
  animation: pulse-ring 2s infinite ease-in-out;
}
```

### 3.2 `animation-fill-mode`
- `none`: Element resets to original un-animated state after animation ends.
- `forwards`: Element retains final keyframe state (`100%`) after completion.
- `backwards`: Element applies initial keyframe state (`0%`) during `animation-delay`.
- `both`: Applies both `backwards` delay styles and `forwards` end styles!

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart LR
    Key0["0%: scale(0.95)"] --> Key50["50%: scale(1.05)"]
    Key50 --> Key100["100%: scale(0.95)"]
    Key100 -->|animation-iteration-count: infinite| Key0
```

---

## 5. Code & Hardware Implementation [id: syntax]

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Keyframe Animations</title>
  <style>
    body { font-family: system-ui; padding: 4rem; background: #0f172a; color: #fff; }
    
    @keyframes pulse {
      0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); }
      70% { transform: scale(1.05); box-shadow: 0 0 0 10px rgba(34, 197, 94, 0); }
      100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }
    }
    
    .status-badge {
      display: inline-block; padding: 8px 16px; background: #22c55e;
      color: #000; font-weight: bold; border-radius: 999px;
      animation: pulse 2s infinite ease-in-out;
    }
  </style>
</head>
<body>
  <div class="status-badge">ESP32 GATEWAY ONLINE</div>
</body>
</html>
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Live Status Radar Bullets & Loading Spinners**: Telemetry dashboards use infinite keyframe animations for real-time connection status indicators and loading skeletons.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `keyframes_demo.html`.
2. Open in Chrome $\rightarrow$ Observe continuous live green pulsing radar status badge!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Animation Resets to Initial State** | Missing `animation-fill-mode: forwards`. | Add `animation-fill-mode: forwards;` to retain end state. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Use `animation-fill-mode: forwards`**: Retains final animation state cleanly.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: What does `animation-fill-mode: forwards` do?
**Answer**: It forces the element to retain the computed property values established by the final keyframe (`100%` or `to`) after the animation completes.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 5.3 Keyframes Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which property value keeps an element locked at its final 100% keyframe state when an animation ends?",
      "options": ["animation-fill-mode: forwards", "animation-fill-mode: backwards", "animation-iteration-count: 1", "animation-play-state: paused"],
      "correct_answer_index": 0,
      "explanation": "forwards causes the element to retain final keyframe properties."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Build a multi-stage radar sweep animation for IoT device discovery.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What property pauses a running CSS keyframe animation?
**Back**: `animation-play-state: paused;`
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```css
@keyframes pulse { 0% { opacity: 0; } 100% { opacity: 1; } }
.badge { animation: pulse 1s forwards; }
```

# Backgrounds Borders And Shadows

> **Course**: Git Version Control | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 4.2 Modern CSS Color Systems](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_02_css3/_02_11_modern_css_color_systems.md)
- **XP Reward**: +60 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Configure background fitting and positioning (`background-size: cover`, `background-attachment`).
2. Construct Linear, Radial, and Conic CSS Gradients.
3. Apply advanced border radius curves and accessibility `outline-offset`.
4. Layer realistic elevation `box-shadow` values (offset-x, offset-y, blur, spread, inset).

---

---

Open VS Code and create `shadow_demo.html` to write background and shadow code.

---

---

### 3.1 CSS Gradient Types
- **Linear Gradient**: Transitions color along a directional angle (`linear-gradient(135deg, #0f172a, #3b82f6)`).
- **Radial Gradient**: Transitions color outward from an origin point (`radial-gradient(circle, #38bdf8, #0f172a)`).
- **Conic Gradient**: Transitions color around a center pivot point (`conic-gradient(#ef4444, #22c55e, #3b82f6)`).

### 3.2 Box Shadow Layering (`box-shadow`)

```css
/* box-shadow: offset-x | offset-y | blur-radius | spread-radius | color */
.card {
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
}
```

---

---

```mermaid
graph LR
    Shadow["box-shadow: 0px 10px 15px -3px rgba(0,0,0,0.3)"] --> X[Offset-X: 0px]
    Shadow --> Y[Offset-Y: 10px]
    Shadow --> Blur[Blur Radius: 15px]
    Shadow --> Spread[Spread: -3px]
    Shadow --> Color[Color: rgba]
```

---

---

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Gradients and Shadows</title>
  <style>
    body { font-family: system-ui; padding: 2rem; background: #0f172a; }
    .hero-card {
      background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
      border: 1px solid #38bdf8;
      border-radius: 12px;
      padding: 2rem;
      color: #fff;
      box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
    }
  </style>
</head>
<body>
  <div class="hero-card">
    <h2>Linear Gradient Card</h2>
    <p>Layered shadows create realistic visual elevation.</p>
  </div>
</body>
</html>
```

---

---

- **Elevation Systems**: Modern UI kits (Material Design, Tailwind) define elevation shadow tiers (`shadow-sm`, `shadow-md`, `shadow-lg`, `shadow-xl`) using multi-layered `box-shadow` rules.

---

---

1. Save code as `shadow_demo.html`.
2. Inspect `.hero-card` in Chrome DevTools $\rightarrow$ Toggle `box-shadow` on/off to observe depth removal!

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Harsh Unnatural Shadows** | Using pure black `box-shadow: 0 5px 10px #000000;`. | Use soft semi-transparent black (`rgba(0, 0, 0, 0.15)`) or colored shadows. |

---

---

- **Layer Shadows**: Combine two subtle `box-shadow` layers for smooth elevation.

---

---

### Q1: What is the difference between blur-radius and spread-radius in a `box-shadow` property?
**Answer**: Blur-radius controls the softness and spread of the shadow blur. Spread-radius expands or contracts the physical footprint size of the shadow before blur is applied.

---

---

```json
{
  "quiz_title": "Lesson 4.3 Shadows Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which gradient type rotates colors around a central 360 degree pivot point?",
      "options": ["linear-gradient", "radial-gradient", "conic-gradient", "repeating-gradient"],
      "correct_answer_index": 2,
      "explanation": "conic-gradient transitions colors around a center pivot point."
    }
  ]
}
```

---

---

Build a 3D elevated card set with linear gradients and hover elevation state transitions.

---

---

**Front**: How do you create an inner inset box shadow in CSS?
**Back**: Add the `inset` keyword to the `box-shadow` property (`box-shadow: inset 0 2px 4px #000;`).
<!-- flashcard:end -->

---

---

```css
.card { background: linear-gradient(135deg, #1e293b, #0f172a); box-shadow: 0 10px 15px rgba(0,0,0,0.3); }
```

---

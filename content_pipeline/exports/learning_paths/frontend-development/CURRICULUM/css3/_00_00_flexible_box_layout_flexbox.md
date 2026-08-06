# Flexible Box Layout Flexbox

> **Course**: Git Fundamentals | **Module**: Introduction | **Difficulty**: beginner

---

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 2.2 Display Property](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_02_css3/_02_05_display_property_and_visual_formatting_model.md)
- **XP Reward**: +60 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Deconstruct Flexbox layouts into Flex Container and Flex Item relationships.
2. Align items along Main Axis (`justify-content`) and Cross Axis (`align-items`, `align-content`).
3. Control item sizing dynamics using `flex-grow`, `flex-shrink`, `flex-basis`, and `flex` shorthand.
4. Reorder flex items using `order` and `align-self`.
5. Apply modern gap spacing (`gap: 1rem`).

---

---

Inspect Flexbox layouts in Chrome DevTools:
- Open DevTools (`F12`) $\rightarrow$ Click **Elements** tab $\rightarrow$ Click the **flex** badge on DOM nodes to reveal interactive grid overlay guides.

---

---

### 3.1 Flexbox Axes System
Flexbox is a 1-dimensional layout model operating on two orthogonal axes:
- **Main Axis**: Defined by `flex-direction` (`row` [horizontal] or `column` [vertical]).
- **Cross Axis**: Runs perpendicular to the Main Axis.

```
flex-direction: row ────►  Main Axis (Horizontal)
                              │
                              ▼  Cross Axis (Vertical)

flex-direction: column ──► Main Axis (Vertical)
                              │
                              ▼  Cross Axis (Horizontal)
```

### 3.2 Main Axis vs Cross Axis Alignment

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       FLEXBOX ALIGNMENT PROPERTIES                          │
├───────────────────┬───────────────────┬─────────────────────────────────────┤
│ Property          │ Axis Target       │ Values                              │
├───────────────────┼───────────────────┼─────────────────────────────────────┤
│ `justify-content` │ Main Axis         │ `flex-start`, `flex-end`, `center`, │
│                   │                   │ `space-between`, `space-around`,    │
│                   │                   │ `space-evenly`                      │
├───────────────────┼───────────────────┼─────────────────────────────────────┤
│ `align-items`     │ Cross Axis        │ `stretch`, `flex-start`, `flex-end`,│
│                   │                   │ `center`, `baseline`                │
├───────────────────┼───────────────────┼─────────────────────────────────────┤
│ `gap`             │ Main & Cross Gap  │ `1rem`, `16px 24px`                 │
└───────────────────┴───────────────────┴─────────────────────────────────────┘
```

### 3.3 Flex Item Sizing (`flex: grow shrink basis`)
- `flex-grow`: Ratio of extra available space item absorbs (default `0`).
- `flex-shrink`: Ratio item shrinks when container overflows (default `1`).
- `flex-basis`: Initial size before space distribution (default `auto`).

```css
/* Production Shorthand: flex: grow shrink basis */
.flex-item {
  flex: 1 1 0%; /* Fills equal width in flex row */
}
```

---

---

```mermaid
graph TD
    Container["Flex Container (display: flex)"] --> MainAxis["Main Axis: justify-content (space-between)"]
    Container --> CrossAxis["Cross Axis: align-items (center)"]
    
    MainAxis --> Item1["Item 1 (flex: 1)"]
    MainAxis --> Item2["Item 2 (flex: 2)"]
```

---

---

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Flexbox Card Grid</title>
  <style>
    body { font-family: system-ui; padding: 2rem; background: #0f172a; color: #fff; }
    
    /* Flex Container */
    .card-grid {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: stretch;
      gap: 1.5rem;
    }

    /* Flex Items */
    .card {
      flex: 1 1 280px; /* Grow=1, Shrink=1, Basis=280px */
      background: #1e293b;
      padding: 1.5rem;
      border-radius: 8px;
      border: 1px solid #3b82f6;
    }
  </style>
</head>
<body>
  <div class="card-grid">
    <div class="card"><h3>ESP32 Node 1</h3><p>Status: Active</p></div>
    <div class="card"><h3>ESP32 Node 2</h3><p>Status: Active</p></div>
    <div class="card"><h3>ESP32 Node 3</h3><p>Status: Offline</p></div>
  </div>
</body>
</html>
```

---

---

- **Equal-Height Responsive Cards**: `align-items: stretch` ensures cards in a row expand to matching vertical heights regardless of content length.

---

---

1. Save code as `flex_demo.html`.
2. Resize browser window $\rightarrow$ Observe cards wrapping gracefully via `flex-wrap: wrap` and `flex: 1 1 280px`.

---

---

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Flex Items Squished / Compressed** | `flex-shrink` defaulted to `1`. | Add `flex-shrink: 0` or set `min-width` to prevent unwanted compression. |

---

---

- **Use Shorthand `flex: 1 1 auto`**: Avoid writing `flex-grow`, `flex-shrink`, and `flex-basis` separately.

---

---

### Q1: What does `flex: 1` expand to in CSS?
**Answer**: `flex: 1` expands to `flex-grow: 1`, `flex-shrink: 1`, and `flex-basis: 0%`. It forces items to absorb equal shares of available container width.

---

---

```json
{
  "quiz_title": "Lesson 3.1 Flexbox Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which property aligns items along the Main Axis in Flexbox?",
      "options": ["align-items", "justify-content", "align-content", "flex-flow"],
      "correct_answer_index": 1,
      "explanation": "justify-content controls alignment along the Main Axis."
    }
  ]
}
```

---

---

Build a responsive navigation header with left logo, centered links, and right call-to-action button using Flexbox.

---

---

**Front**: What Flexbox property changes the main axis from horizontal to vertical?
**Back**: `flex-direction: column;`
<!-- flashcard:end -->

---

---

```css
.flex-container { display: flex; justify-content: space-between; gap: 1rem; }
```

---

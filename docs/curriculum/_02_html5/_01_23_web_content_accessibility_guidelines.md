```yaml
schema_version: "2.0"
metadata:
  lesson_id: "HTML5-MOD09-LES01"
  course_slug: "course-01-html5"
  course_title: "Course 1: HTML5"
  module_slug: "mod-09-a11y-seo-performance"
  module_title: "Module 9 - Accessibility (a11y), SEO, & Performance Optimization"
  lesson_slug: "web-content-accessibility-guidelines"
  lesson_title: "Lesson 9.1 Web Content Accessibility Guidelines (WCAG)"
  sort_order: 901

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
    - "HTML5-MOD03-LES02"
  required_skills:
    - "Accessibility Tree & ARIA Roles"

skills_acquired:
  - "WCAG 2.1 / 2.2 Principles (POUR: Perceivable, Operable, Understandable, Robust)"
  - "Conformance Levels (A, AA, AAA)"
  - "Color Contrast Requirements (4.5:1 Normal Text, 3:1 Large Text)"
  - "Keyboard Focus Trapping & Skip Links (`href='#main-content'`)"
  - "Accessible Form Control Labeling & Error Recovery"

dependencies:
  software:
    - "VS Code"
    - "Chrome Lighthouse Accessibility Auditor"
  hardware: []

seo_and_social:
  meta_title: "WCAG 2.1 / 2.2 Guidelines: POUR Principles, Contrast & Skip Links"
  meta_description: "Master WCAG 2.1/2.2 accessibility guidelines: POUR principles (Perceivable, Operable, Understandable, Robust), AA contrast rules, and skip links."
  keywords: ["WCAG 2.1", "WCAG 2.2", "POUR Principles", "a11y", "Color Contrast", "Skip Links", "Accessibility Conformance"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 9.1 Web Content Accessibility Guidelines (WCAG)

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 3.2 Document Outline & Accessibility Tree](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_01_html5/_01_08_document_outline_and_accessibility_tree.md)
- **XP Reward**: +60 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Apply the four core **POUR** principles of WCAG 2.1 / 2.2 (Perceivable, Operable, Understandable, Robust).
2. Evaluate WCAG conformance levels (Level A, Level AA, Level AAA).
3. Enforce color contrast minimum ratios (4.5:1 for normal text, 3:1 for large text).
4. Implement "Skip to Main Content" links to assist keyboard navigation.
5. Audit web applications for accessible form error messages and focus management.

---

## 2. Environment & Prerequisites [id: prerequisites]

Run WCAG audits in Chrome DevTools:
- Open DevTools (`F12`) $\rightarrow$ Click **Lighthouse** tab $\rightarrow$ Check **Accessibility** $\rightarrow$ Click **Analyze page load**.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 The POUR Principles (WCAG 2.1 / 2.2)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       THE 4 POUR ACCESSIBILITY PRINCIPLES                   │
├─────────────────┬───────────────────────────────────────────────────────────┤
│ 1. Perceivable  │ Information must be presented in ways users can perceive  │
│                 │ (e.g. text alternatives for images, captions for video).   │
├─────────────────┼───────────────────────────────────────────────────────────┤
│ 2. Operable     │ Interface components must be operable via keyboard        │
│                 │ without trapping focus.                                   │
├─────────────────┼───────────────────────────────────────────────────────────┤
│ 3. Understandable│ Text content and UI controls must be clear and predictable.│
├─────────────────┼───────────────────────────────────────────────────────────┤
│ 4. Robust       │ Content must be compatible with assistive technologies.   │
└─────────────────┴───────────────────────────────────────────────────────────┘
```

### 3.2 Conformance Levels
- **Level A**: Minimum baseline requirements (e.g., non-text alt text).
- **Level AA (Industry Standard)**: Legal requirement for enterprise websites (4.5:1 contrast, keyboard navigation, visible focus indicators).
- **Level AAA**: Highest accessibility standards (7:1 contrast, sign language translation).

### 3.3 Color Contrast Requirements (Level AA)
- **Normal Text (< 24px or < 18.66px bold)**: Minimum **4.5:1** contrast ratio against background.
- **Large Text ($\ge$ 24px or $\ge$ 18.66px bold)**: Minimum **3.0:1** contrast ratio against background.

### 3.4 Skip Navigation Links
Allows screen reader and keyboard users to bypass top navigation bars and jump directly to the primary page content:

```html
<!-- Visible on keyboard focus only -->
<a href="#main-content" class="skip-link">Skip to Main Content</a>
```

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    Key[User Presses Tab Key] --> Skip[Focus 'Skip to Main Content' Link]
    Skip -->|Press Enter| Main[Focus Instantly Moves to <main id='main-content'>]
    Skip -->|Press Tab Again| Nav[Focus Enters Main Navigation Links]
```

---

## 5. Code & Hardware Implementation [id: syntax]

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>WCAG AA Compliant Page</title>
  <style>
    /* Visually hidden until keyboard focus */
    .skip-link {
      position: absolute; top: -40px; left: 0; background: #0f172a; color: #fff;
      padding: 8px; z-index: 100; transition: top 0.2s;
    }
    .skip-link:focus { top: 0; }
    body { font-family: system-ui; color: #0f172a; background: #ffffff; } /* 16:1 Contrast Ratio */
  </style>
</head>
<body>

  <!-- Skip Navigation Link -->
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <header><h1>Enterprise Portal</h1></header>

  <main id="main-content" tabindex="-1">
    <h2>Accessible Form Section</h2>
    <p>High contrast content matching WCAG Level AA standards.</p>
  </main>

</body>
</html>
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Legal Compliance**: Section 508 and the European Accessibility Act require enterprise websites to meet WCAG 2.1 Level AA conformance.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `wcag_demo.html`.
2. Open in Chrome $\rightarrow$ Press <kbd>Tab</kbd> key $\rightarrow$ Verify **Skip to main content** link appears at the top left of screen!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Outline Reset Anti-Pattern** | Adding `* { outline: none; }` in CSS, removing keyboard focus rings. | Use `:focus-visible { outline: 3px solid #3b82f6; }`. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Never Remove Focus Outlines**: Retain visible focus rings.
- **Maintain 4.5:1 Contrast Ratio**: Ensure text is legible.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: What are the four WCAG POUR principles?
**Answer**: Perceivable, Operable, Understandable, and Robust.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 9.1 WCAG Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "What is the minimum WCAG 2.1 Level AA color contrast ratio required for normal body text?",
      "options": ["2:1", "3:1", "4.5:1", "7:1"],
      "correct_answer_index": 2,
      "explanation": "WCAG Level AA mandates a minimum 4.5:1 contrast ratio for normal text."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Perform a WCAG Level AA audit on an existing web page using Chrome Lighthouse.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What is the target conformance level for most enterprise web applications?
**Back**: WCAG 2.1 / 2.2 Level AA.
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```html
<a href="#main-content" class="skip-link">Skip to content</a>
```

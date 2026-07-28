```yaml
schema_version: "2.0"
metadata:
  lesson_id: "HTML5-MOD09-LES03"
  course_slug: "course-01-html5"
  course_title: "Course 1: HTML5"
  module_slug: "mod-09-a11y-seo-performance"
  module_title: "Module 9 - Accessibility (a11y), SEO, & Performance Optimization"
  lesson_slug: "performance-optimization-and-best-practices"
  lesson_title: "Lesson 9.3 Performance Optimization & Best Practices"
  sort_order: 903

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
    - "HTML5-MOD01-LES02"
  required_skills:
    - "Critical Rendering Path & Resource Loading"

skills_acquired:
  - "Resource Hint Implementation (`dns-prefetch`, `preconnect`, `prefetch`, `preload`)"
  - "Module Preloading (`modulepreload`)"
  - "Native Lazy Loading (`loading='lazy'` on images & iframes)"
  - "Audit & Deprecation of Obsolete HTML Elements (`<font>`, `<center>`, `<marquee>`)"
  - "W3C Markup Validation Testing Workflow"

dependencies:
  software:
    - "VS Code"
    - "Chrome Lighthouse Performance Auditor"
    - "W3C Markup Validation Service"
  hardware: []

seo_and_social:
  meta_title: "HTML5 Performance Optimization, Resource Hints & W3C Validation"
  meta_description: "Master HTML5 performance optimization: resource hints (preload, preconnect), native lazy loading, eliminating deprecated HTML tags, and W3C validation."
  keywords: ["HTML5 Performance", "Resource Hints", "preload", "preconnect", "lazy loading", "Deprecated HTML Elements", "W3C Validation"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 9.3 Performance Optimization & Best Practices

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 1.2 Browser Rendering Engine](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_01_html5/_01_02_browser_rendering_engine_architecture.md)
- **XP Reward**: +60 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Configure browser resource hints (`dns-prefetch`, `preconnect`, `prefetch`, `preload`, `modulepreload`).
2. Apply native lazy loading (`loading="lazy"`) to images and `<iframe>` elements to defer offscreen network downloads.
3. Identify and purge obsolete, deprecated HTML elements (`<font>`, `<center>`, `<marquee>`, `<strike>`, `<big>`).
4. Validate HTML documents using W3C Validation Services to achieve 100% syntax compliance.

---

## 2. Environment & Prerequisites [id: prerequisites]

Run performance profiling in Chrome DevTools:
- Open DevTools (`F12`) $\rightarrow$ Click **Lighthouse** tab $\rightarrow$ Check **Performance** $\rightarrow$ Analyze page load.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 Resource Hints Summary

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          HTML5 RESOURCE HINTS SUMMARY                       │
├─────────────────┬───────────────────────────────────────────────────────────┤
│ `dns-prefetch`  │ Performs early DNS lookup for external domain origin.     │
├─────────────────┼───────────────────────────────────────────────────────────┤
│ `preconnect`    │ Performs DNS lookup + TCP handshake + TLS negotiation.     │
├─────────────────┼───────────────────────────────────────────────────────────┤
│ `preload`       │ Mandatory high-priority fetch for current page assets     │
│                 │ (fonts, critical CSS, key JS).                            │
├─────────────────┼───────────────────────────────────────────────────────────┤
│ `prefetch`      │ Low-priority background fetch for FUTURE page assets.     │
├─────────────────┼───────────────────────────────────────────────────────────┤
│ `modulepreload` │ Preloads and compiles ES6 JavaScript modules.             │
└─────────────────┴───────────────────────────────────────────────────────────┘
```

### 3.2 Native Lazy Loading (`loading="lazy"`)
Native lazy loading delays network requests for images and iframes until they scroll near the visible viewport:

```html
<!-- Offscreen Image Lazy Loading -->
<img src="large-photo.jpg" alt="Gallery Image" loading="lazy" width="800" height="600">

<!-- Offscreen Iframe Lazy Loading -->
<iframe src="dashboard.html" loading="lazy" title="Widget"></iframe>
```

### 3.3 Obsolete & Deprecated HTML Tags
Modern HTML5 separates styling (CSS) from structure. The following legacy presentational tags are **deprecated** and forbidden in production HTML5:

- `<font>`, `<center>`, `<marquee>`, `<strike>`, `<big>`, `<tt>`, `<frame>`, `<frameset>`.

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    HTML[Page Loading Begins] --> Hints[Process Resource Hints in <head>]
    Hints -->|preconnect| TCP[Open TCP/TLS Connection Early]
    Hints -->|preload| Font[High Priority Critical Font Fetch]
    HTML -->|loading='lazy'| Defer[Defer Offscreen Images Until Scroll]
```

---

## 5. Code & Hardware Implementation [id: syntax]

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>High Performance HTML5 Portal</title>

  <!-- 1. Resource Hints -->
  <link rel="dns-prefetch" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" href="/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>

  <style>
    body { font-family: system-ui; margin: 0; padding: 20px; }
  </style>
</head>
<body>

  <h1>High Performance HTML5 Page</h1>

  <!-- Native Lazy Loaded Image -->
  <img src="/assets/hero.jpg" alt="Hero Banner" width="1200" height="600" loading="lazy">

</body>
</html>
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **Core Web Vitals**: Utilizing `preload` and `loading="lazy"` improves Largest Contentful Paint (LCP) and Cumulative Layout Shift (CLS) scores on Google PageSpeed Insights.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `perf_demo.html`.
2. Run Lighthouse in Chrome DevTools $\rightarrow$ Verify **Performance Score** is 95+!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **`Preload trigger warning`** | Preloading an asset that is not used within 3 seconds of page load. | Only use `<link rel="preload">` for critical above-the-fold assets. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Lazy Load Below-the-Fold Images**: Add `loading="lazy"`.
- **Preconnect Third-Party Domains**: Preconnect to font or API origins.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: What is the difference between `preload` and `prefetch`?
**Answer**: `preload` is a high-priority directive for critical assets needed on the *current* page. `prefetch` is a low-priority directive for assets likely needed on *future* pages during navigation.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 9.3 Performance Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which attribute defers loading of offscreen images until they approach the viewport?",
      "options": ["defer", "async", "loading='lazy'", "preload"],
      "correct_answer_index": 2,
      "explanation": "loading='lazy' enables native browser lazy loading."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Optimize an un-optimized HTML page to achieve a 100 Performance Score on Chrome Lighthouse.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What resource hint opens early DNS, TCP, and TLS connections to an external domain?
**Back**: `<link rel="preconnect" href="...">`
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```html
<img src="photo.jpg" loading="lazy" width="800" height="600" alt="Lazy Photo">
```

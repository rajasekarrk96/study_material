```yaml
schema_version: "2.0"
metadata:
  lesson_id: "HTML5-MOD09-LES02"
  course_slug: "course-01-html5"
  course_title: "Course 1: HTML5"
  module_slug: "mod-09-a11y-seo-performance"
  module_title: "Module 9 - Accessibility (a11y), SEO, & Performance Optimization"
  lesson_slug: "search-engine-optimization-and-microdata"
  lesson_title: "Lesson 9.2 Search Engine Optimization (SEO) & Microdata"
  sort_order: 902

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
    - "HTML5-MOD01-LES03"
  required_skills:
    - "HTML Metadata & Document Head Architecture"

skills_acquired:
  - "On-Page SEO Optimization Strategies"
  - "Canonical URL Implementation (`<link rel='canonical'>`)"
  - "Schema.org Microdata & Itemprop Syntax"
  - "JSON-LD Structured Data Implementation"
  - "Robots Meta Tags & `robots.txt` Integration"

dependencies:
  software:
    - "VS Code"
    - "Google Rich Results Test Tool"
  hardware: []

seo_and_social:
  meta_title: "HTML5 SEO Strategy, Schema.org Microdata & JSON-LD Structured Data"
  meta_description: "Master HTML5 SEO best practices: title/meta tags, canonical links, Schema.org Microdata, JSON-LD structured data, and robots.txt rules."
  keywords: ["SEO HTML5", "JSON-LD", "Schema.org", "Microdata", "Canonical URL", "Robots.txt", "Structured Data"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 9.2 Search Engine Optimization (SEO) & Microdata

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 1.3 HTML Standards](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_01_html5/_01_03_html_standards_and_document_structure.md)
- **XP Reward**: +60 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Implement essential On-Page SEO elements (title, meta description, heading structure, canonical URLs).
2. Contrast Microdata (`itemscope`, `itemtype`, `itemprop`) with **JSON-LD** structured data.
3. Construct Schema.org JSON-LD scripts for Tech Articles, Courses, and Products.
4. Configure crawler instructions using `<meta name="robots">` and `robots.txt`.

---

## 2. Environment & Prerequisites [id: prerequisites]

Validate structured data using [Google Rich Results Test](https://search.google.com/test/rich-results).

---

## 3. Theoretical Foundations [id: theory]

### 3.1 JSON-LD vs Microdata
Structured data enables search engines to display rich snippets (star ratings, course details, prices) in search results.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       JSON-LD VS MICRODATA COMPARISON                       │
├─────────────────┬──────────────────────────────────┬────────────────────────┤
│ Feature         │ JSON-LD (Recommended by Google)  │ Microdata              │
├─────────────────┼──────────────────────────────────┼────────────────────────┤
│ Syntax          │ Script tag containing JSON       │ Inline HTML attributes │
│ Maintenance     │ High (Clean, decoupled from DOM) │ Low (Clutters markup)  │
│ Position        │ Placed inside `<head>` or `<body>│ Attached to HTML tags  │
└─────────────────┴──────────────────────────────────┴────────────────────────┘
```

### 3.2 JSON-LD Implementation Example
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "Course 1: HTML5 Masterclass",
  "description": "Comprehensive HTML5 web architecture and IoT full stack engineering.",
  "provider": {
    "@type": "Organization",
    "name": "Bytes and Boards Solutions"
  }
}
</script>
```

---

## 4. Architecture & Diagram Visualizations [id: diagram]

```mermaid
flowchart TD
    Crawler[Search Engine Crawler] --> ReadsHead[Reads HTML Head Metadata]
    ReadsHead --> JSONLD[Parses JSON-LD Structured Data]
    JSONLD --> RichSnippet[Displays Rich Search Card Snippet in SERP]
```

---

## 5. Code & Hardware Implementation [id: syntax]

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>SEO & JSON-LD Portal</title>
  <link rel="canonical" href="https://example.com/course-html5">
  <meta name="robots" content="index, follow">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "HTML5 Web Architecture & Protocols",
    "author": "Bytes and Boards Solutions",
    "datePublished": "2026-07-28"
  }
  </script>
</head>
<body>
  <h1>HTML5 Web Architecture</h1>
</body>
</html>
```

---

## 6. Enterprise Real-World Applications [id: examples]

- **E-Commerce & Learning Portals**: Uses JSON-LD to display price ranges, course duration, and review stars in Google search results.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save code as `seo_demo.html`.
2. Copy code into Google Rich Results Test $\rightarrow$ Verify zero syntax errors!

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Duplicate Content Penalty** | Missing `<link rel="canonical">` tag across HTTP/HTTPS or trailing slash variations. | Always specify a canonical URL. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Use JSON-LD**: Google's preferred structured data format.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: Why is JSON-LD preferred over Microdata for SEO?
**Answer**: JSON-LD is decoupled from HTML presentation markup inside a single `<script type="application/ld+json">` block, making it cleaner to maintain and generate programmatically.

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 9.2 SEO Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which script type is used to insert JSON-LD structured data?",
      "options": ["text/json", "application/ld+json", "application/schema", "text/javascript"],
      "correct_answer_index": 1,
      "explanation": "application/ld+json specifies JSON-LD structured data."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Add JSON-LD Course metadata to an educational portal landing page.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What is the purpose of `<link rel="canonical">`?
**Back**: Prevents duplicate content penalties by specifying the primary authoritative URL for a page.
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```html
<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage"}</script>
```

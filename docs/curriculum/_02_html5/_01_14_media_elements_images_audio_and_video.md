```yaml
schema_version: "2.0"
metadata:
  lesson_id: "HTML5-MOD06-LES01"
  course_slug: "course-01-html5"
  course_title: "Course 1: HTML5"
  module_slug: "mod-06-multimedia-and-canvas"
  module_title: "Module 6 - Multimedia, Embedded Content, & Graphics"
  lesson_slug: "media-elements-images-audio-and-video"
  lesson_title: "Lesson 6.1 Media Elements: Images, Audio, & Video"
  sort_order: 601

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
    - "HTML5-MOD03-LES01"
  required_skills:
    - "HTML Document Structure & Asset Referencing"

skills_acquired:
  - "Image Element (`<img>`) Core & Responsive Attributes (`srcset`, `sizes`)"
  - "Art Direction with `<picture>` & Media Queries"
  - "Modern Image Formats (WebP, AVIF, SVG vs JPEG/PNG)"
  - "Native Audio (`<audio>`) & Video (`<video>`) Embeds"
  - "Media Controls (`controls`, `autoplay`, `loop`, `muted`, `preload`)"
  - "Subtitles & Captions Track Integration (`<track>`, WebVTT)"

dependencies:
  software:
    - "VS Code"
  hardware: []

seo_and_social:
  meta_title: "HTML5 Media Elements: Images, Audio, Video & WebVTT Captions"
  meta_description: "Master HTML5 multimedia: responsive srcset, picture art direction, AVIF/WebP formats, audio/video elements, and WebVTT subtitle tracks."
  keywords: ["HTML5 Media", "img srcset sizes", "picture tag", "WebP AVIF", "audio video tags", "track WebVTT", "media controls"]

assessment_config:
  has_quiz: true
  has_lab: true
  has_flashcards: true
  pass_score_percentage: 80
```

# Lesson 6.1 Media Elements: Images, Audio, & Video

## 1. Overview & Learning Objectives [id: overview]

- **Estimated Time**: 55 Minutes (20m Reading | 25m Practice | 10m Quiz)
- **Difficulty Level**: ⭐⭐ Intermediate
- **Prerequisites**: [Lesson 3.1 Structural Semantic Elements](file:///d:/My%20Drive/all%20files/PROJECT%20FILES/notes/docs/curriculum/_01_html5/_01_07_structural_semantic_elements.md)
- **XP Reward**: +60 XP

### Learning Objectives
By the end of this lesson, you will be able to:
1. Implement responsive image loading using `srcset` and `sizes` attributes.
2. Execute art direction for different screen sizes using `<picture>` and `<source>` elements.
3. Compare modern image formats (AVIF, WebP, SVG) vs legacy formats (JPEG, PNG).
4. Embed native HTML5 audio (`<audio>`) and video (`<video>`) media streams.
5. Add accessible subtitles and captions using `<track>` and WebVTT files.

---

## 2. Environment & Prerequisites [id: prerequisites]

Open VS Code and create `media_demo.html` to write interactive media embeds.

---

## 3. Theoretical Foundations [id: theory]

### 3.1 Responsive Images (`srcset` & `sizes`)
`srcset` allows browsers to select the optimal image resolution based on device screen density (DPI) and viewport width:

```html
<img src="small.jpg"
     srcset="small.jpg 400w, medium.jpg 800w, large.jpg 1200w"
     sizes="(max-width: 600px) 100vw, 50vw"
     alt="IoT Hardware Dashboard"
     loading="lazy">
```

### 3.2 Art Direction (`<picture>`)
`<picture>` allows serving completely different cropped images or modern formats (AVIF/WebP) based on media queries:

```html
<picture>
  <source srcset="hero-mobile.webp" media="(max-width: 600px)" type="image/webp">
  <source srcset="hero-desktop.avif" type="image/avif">
  <img src="hero-fallback.jpg" alt="Hero Banner" loading="lazy">
</picture>
```

### 3.3 Audio & Video Elements
HTML5 provides native hardware-accelerated playback without plugins:

```html
<video controls width="640" poster="cover.jpg" preload="metadata">
  <source src="stream.webm" type="video/webm">
  <source src="stream.mp4" type="video/mp4">
  <track src="subtitles-en.vtt" kind="subtitles" srclang="en" label="English" default>
  Your browser does not support video playback.
</video>
```

---

## 4. Architecture & Diagram Visualizations [id: diagram]

### Media Selection Pipeline
```mermaid
flowchart TD
    Browser[Browser Requests Page Asset] --> Check{Picture or srcset Tag?}
    Check -->|Picture| MatchMedia[Match Media Query & MIME Type]
    Check -->|Srcset| ComputeDensity[Compute DPI & Viewport Width]
    MatchMedia --> FetchAsset[Fetch Target Image Stream]
    ComputeDensity --> FetchAsset
```

---

## 5. Code & Hardware Implementation [id: syntax]

### 5.1 Comprehensive Media Dashboard (`media_dashboard.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Media & WebVTT Portal</title>
  <style>
    body { font-family: system-ui; padding: 20px; }
    video, img { max-width: 100%; height: auto; border-radius: 8px; }
  </style>
</head>
<body>

  <h1>IoT Video Telemetry Feed</h1>

  <video controls width="720" poster="/assets/poster.jpg">
    <source src="/assets/stream.mp4" type="video/mp4">
    <track src="/assets/subtitles.vtt" kind="subtitles" srclang="en" label="English" default>
  </video>

</body>
</html>
```

---

## 6. Enterprise Real-World Applications [id: examples]

### AVIF & WebP Next-Gen Image Compression
Enterprise platforms (YouTube, Netflix) use AVIF/WebP image formats to reduce page payload size by up to 50% compared to legacy JPEG/PNG formats.

---

## 7. Guided Step-by-Step Hands-On Exercise [id: exercises]

1. Save Section 5.1 as `media_dashboard.html`.
2. Inspect the video element in DevTools to verify subtitle track rendering.

---

## 8. Common Pitfalls & Troubleshooting [id: common_mistakes]

| Bug / Error | Root Cause | Engineering Solution |
| :--- | :--- | :--- |
| **Autoplay Fails** | Browsers block unmuted video autoplay. | Always include the `muted` attribute alongside `autoplay`: `<video autoplay muted>`. |

---

## 9. Best Practices & Optimization [id: best_practices]

- **Use `loading="lazy"`**: Defer offscreen image loading.
- **Mute Autoplay Videos**: Always add `muted` when using `autoplay`.

---

## 10. Industry Interview Q&A [id: interview_qa]

### Q1: What is the difference between `<img srcset>` and the `<picture>` tag?
**Answer**: `srcset` lets the browser automatically select the best resolution of the *same* image. `<picture>` gives the developer explicit control over *art direction* (switching images or format types based on CSS media queries).

---

## 11. Self-Assessment Quiz [id: quiz]

```json
{
  "quiz_title": "Lesson 6.1 Media Elements Assessment",
  "questions": [
    {
      "question_id": "Q1",
      "type": "multiple_choice",
      "question_text": "Which tag defines text subtitles for a `<video>` element?",
      "options": ["<caption>", "<track>", "<text>", "<subtitle>"],
      "correct_answer_index": 1,
      "explanation": "<track> defines subtitles and captions in WebVTT format."
    }
  ]
}
```

---

## 12. Portfolio Assignment & Challenge [id: lab]

Build a responsive media gallery using `<picture>`, WebP formats, and lazy loading.

---

## 13. Spaced Repetition Flashcards [id: flashcards]

**Front**: What attribute is required for video `autoplay` to function in modern browsers?
**Back**: `muted`
<!-- flashcard:end -->

---

## 14. Summary & Cheat Sheet [id: summary]

```html
<img src="hero.jpg" loading="lazy" alt="Hero Image">
```

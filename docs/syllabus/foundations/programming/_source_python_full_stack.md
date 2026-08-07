# Python Full Stack Web Engineering — Master Syllabus

**Target Role:** Python Full Stack Developer / Web Solutions Architect  
**Difficulty Level:** Advanced  
**Estimated Duration:** 330 Hours  
**Prerequisites:** core-python, html5, css3, javascript  
**Required Courses:** core-python, fast-api, react, mysql  
**Optional Courses:** docker, aws  

---

## 1. Term 1

### 1.1. HTML5

#### 1.1.1. Module 1 — Web & Browser Architecture Fundamentals

1. **Lesson 1.1 Web Architecture & Protocols**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Client-Server Architecture
        - The Request-Response Cycle
        - HTTP vs HTTPS Protocols
        - HTTP Request Methods (Verbs)
        - HTTP Status Codes Classification
        - Web Servers vs Application Servers
        - Identifiers: URI, URL, and URN
        - Domain Name System (DNS) Resolution Tracing
    4. Architecture & Diagram Visualizations
        - DNS Resolution & HTTP Request Sequence
    5. Code & Hardware Implementation
        - Deconstructing Raw HTTP/1.1 Request and Response Payload
        - Command Line Inspection with cURL
    6. Enterprise Real-World Applications
        - Case Study: High-Throughput IoT Gateway Architecture
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspect Web Request Lifecycle using Chrome DevTools & Python
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens under the hood when you type `https://example.com` into a browser address bar and press Enter?
        - Q2: What is the technical difference between HTTP `POST`, `PUT`, and `PATCH` methods?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Starter Code
        - Success Criteria
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax & Command Cheat Sheet
        - Official References
2. **Lesson 1.2 Browser Rendering Engine Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Anatomy of a Modern Web Browser
        - Major Browser Engines
        - The 5 Stages of the Rendering Pipeline
        - Reflow vs Repaint Trigger Comparison
    4. Architecture & Diagram Visualizations
        - Critical Rendering Path Architecture
    5. Code & Hardware Implementation
        - Script Execution Blocking Modes (`async` vs `defer`)
    6. Enterprise Real-World Applications
        - Critical CSS Inline Pattern for Enterprise E-Commerce
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Profile Reflow & Layout Thrashing in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Reflow and Repaint, and how do you minimize them?
        - Q2: How does the browser construct the Render Tree, and why are `display: none` elements excluded?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Requirements
        - Starter Code Snippet
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Cheat Sheet
        - Official References
3. **Lesson 1.3 HTML Standards & Document Structure**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Evolution of HTML Standards
        - The DOCTYPE Declaration & Rendering Modes
        - Root Element (`<html>`) & Language Attribute
        - Character Encodings (ASCII vs UTF-8)
        - Viewport Configuration for Mobile Responsiveness
        - Metadata & Social Media Protocol (Open Graph)
    4. Architecture & Diagram Visualizations
        - Complete HTML5 Document Architecture Tree
    5. Code & Hardware Implementation
        - Production-Ready HTML5 Boilerplate Template
    6. Enterprise Real-World Applications
        - Open Graph Debugging & Rich Social Cards
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Build & Validate an Enterprise Boilerplate
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Standards Mode and Quirks Mode in modern browsers?
        - Q2: Why is the WHATWG specification referred to as a "Living Standard"?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Starter Requirements
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References

#### 1.1.2. Module 2 — HTML Syntax, Text Formatting, & Hyperlinks

1. **Lesson 2.1 Syntax Rules & Element Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Tag Syntax & Element Composition
        - Standard Elements vs Void (Self-Closing) Elements
        - Attribute Categories
        - Block-Level vs Inline-Level vs Inline-Block
        - Element Nesting Rules & DOM Tree Integrity
        - HTML Entity Encoding & Escaping
    4. Architecture & Diagram Visualizations
        - Block vs Inline Box Model Layout Geometry
    5. Code & Hardware Implementation
        - Demonstrating Block, Inline, and Data Attributes
    6. Enterprise Real-World Applications
        - Data Attributes in Modern Web Frameworks & IoT Dashboards
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspecting Box Geometry & Dataset Properties in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the exact visual difference between Block-level, Inline-level, and Inline-Block elements?
        - Q2: What are HTML Void Elements, and how do they differ from standard elements in DOM parsing?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Starter Requirements
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
2. **Lesson 2.2 Text Content & Formatting Elements**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Heading Hierarchy (`<h1>` through `<h6>`)
        - Semantic vs Presentational Text Formatting
        - Computer Code & Technical Documentation Elements
        - Quotations, Citations, & Abbreviations
        - Bidirectional Text Formatting (`<bdo>` & `<bdi>`)
    4. Architecture & Diagram Visualizations
        - Accessible Heading Tree Outline
    5. Code & Hardware Implementation
        - Technical Documentation Markup Example
    6. Enterprise Real-World Applications
        - Accessible Developer Portals & CLI Documentation
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Build a Technical Quick Reference Sheet
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the semantic difference between `<strong>` and `<b>`, and `<em>` and `<i>`?
        - Q2: How do `<bdo>` and `<bdi>` differ when handling internationalized text?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
3. **Lesson 2.3 Hyperlinks & Anchor Navigation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Anchor Element Architecture
        - URL Types & Path Resolution Rules
        - Fragment Identifiers & In-Page Jumping
        - Link Targets & Vulnerability Hardening (`tabnabbing`)
        - Non-HTML Protocols & Devices Integration
        - Download Attribute & Resource Hints
    4. Architecture & Diagram Visualizations
        - Reverse Tabnabbing Attack vs Hardened Fix
    5. Code & Hardware Implementation
        - Comprehensive Navigation Portal (`navigation_demo.html`)
    6. Enterprise Real-World Applications
        - Multi-Tenant SaaS & IoT Gateway Navigation
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Test Reverse Tabnabbing Security in Browser Console
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What security risk is introduced by `target="_blank"`, and how does `rel="noopener"` fix it?
        - Q2: What is the difference between `<link rel="prefetch">` and `<link rel="preload">`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References

#### 1.1.3. Module 3 — Semantic HTML5 & Document Layout Architecture

1. **Lesson 3.1 Structural Semantic Elements**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Semantic Web Philosophy
        - Structural Landmark Elements
        - Content Sectioning Elements
        - Interactive Native Components
        - Figures, Captions & Machine-Readable Time
    4. Architecture & Diagram Visualizations
        - Complete Semantic HTML5 Web Page Layout
    5. Code & Hardware Implementation
        - Semantic Web Page Implementation (`semantic_layout.html`)
    6. Enterprise Real-World Applications
        - Native Dialog Modals vs Heavy JS Libraries
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Test Native Dialog & Details Accordion
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the exact semantic distinction between an `<article>` and a `<section>`?
        - Q2: How does the native HTML5 `<dialog>` element improve accessibility over custom `<div>` modals?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
2. **Lesson 3.2 Document Outline & Accessibility Tree**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Accessibility Tree (AOM) Architecture
        - HTML5 Semantic Elements vs ARIA Landmark Roles
        - Core ARIA Attributes & Properties
        - Keyboard Focus Management & `tabindex` Rules
    4. Architecture & Diagram Visualizations
        - DOM Tree vs Accessibility Tree Mapping
    5. Code & Hardware Implementation
        - Fully Accessible Component Suite (`accessible_suite.html`)
    6. Enterprise Real-World Applications
        - Automated Accessibility Testing in CI/CD Pipelines
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Audit Accessibility Tree Properties in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `tabindex="0"`, `tabindex="-1"`, and `tabindex="1"`?
        - Q2: How does `aria-live="polite"` differ from `aria-live="assertive"`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References

#### 1.1.4. Module 4 — Data Organization: Lists & Tables

1. **Lesson 4.1 List Elements & Structure**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unordered Lists (`<ul>`) & Ordered Lists (`<ol>`)
        - Description Lists (`<dl>`, `<dt>`, `<dd>`)
        - Nesting Rules for Lists
    4. Architecture & Diagram Visualizations
        - List Tree DOM Structure
    5. Code & Hardware Implementation
        - Semantic Navigation & Metadata Lists
    6. Enterprise Real-World Applications
        - Accessible Navigation Menus
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Build a Nested IoT Setup Procedure List
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: When should you use a Description List (`<dl>`) instead of an Unordered List (`<ul>`)?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 4.2 Tabular Data & Advanced Table Markup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Semantic Table Architecture
        - Cell Spanning (`colspan` & `rowspan`)
        - Column Groups (`<colgroup>` & `<col>`)
        - Table Accessibility & Header Scoping
        - Responsive Mobile Table Patterns
    4. Architecture & Diagram Visualizations
        - Accessible Table DOM Hierarchy
    5. Code & Hardware Implementation
        - Complex Accessible Matrix Table (`matrix_table.html`)
    6. Enterprise Real-World Applications
        - Financial Reports & System Metrics Dashboards
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspect Accessible Headers in DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of the `scope` attribute on `<th>` elements?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.1.5. Module 5 — Forms, Inputs, & Client-Side Validation

1. **Lesson 5.1 Form Architecture & Submissions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Form Architecture
        - Key `<form>` Attributes
        - HTTP Submission Methods: GET vs POST
        - Encoding Types (`enctype`)
    4. Architecture & Diagram Visualizations
        - Form Submission Payload Pipeline
    5. Code & Hardware Implementation
        - File Upload & Search Form Examples
    6. Enterprise Real-World Applications
        - Firmware Uploads & Cloud API Integration
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspect Payload Formats in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens if a developer omits `enctype="multipart/form-data"` on a form containing a file input?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 5.2 Form Controls & Input Types**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Label Association (`<label>`)
        - Form Controls Classification Matrix
        - Form Grouping & Visual Metering
    4. Architecture & Diagram Visualizations
        - Accessible Form Fieldset Hierarchy
    5. Code & Hardware Implementation
        - IoT Device Configuration Form (`iot_config_form.html`)
    6. Enterprise Real-World Applications
        - Soft-Keyboards & Mobile Optimization
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `<select>` dropdowns and `<datalist>` autocomplete inputs?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 5.3 Native Client-Side Form Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Native Validation Attributes
        - CSS Validation Pseudo-Classes
        - The Constraint Validation API (JavaScript)
    4. Architecture & Diagram Visualizations
        - Constraint Validation Flow
    5. Code & Hardware Implementation
        - Custom Validation & RegEx Portal (`validation_portal.html`)
    6. Enterprise Real-World Applications
        - Client-Side Validation is NOT Security
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is `ValidityState` in the HTML5 Constraint Validation API?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.1.6. Module 6 — Multimedia, Embedded Content, & Graphics

1. **Lesson 6.1 Media Elements: Images, Audio, & Video**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Responsive Images (`srcset` & `sizes`)
        - Art Direction (`<picture>`)
        - Audio & Video Elements
    4. Architecture & Diagram Visualizations
        - Media Selection Pipeline
    5. Code & Hardware Implementation
        - Comprehensive Media Dashboard (`media_dashboard.html`)
    6. Enterprise Real-World Applications
        - AVIF & WebP Next-Gen Image Compression
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `<img srcset>` and the `<picture>` tag?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 6.2 Embedded External Content**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Inline Frames (`<iframe>`)
        - Iframe Security Sandboxing (`sandbox` & `allow`)
    4. Architecture & Diagram Visualizations
        - Iframe Sandboxing Boundary
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
        - Embedded Grafana & OpenStreetMap Widgets
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does an empty `sandbox=""` attribute do on an iframe?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 6.3 Vector Graphics & HTML5 Canvas**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SVG vs Canvas Comparison Matrix
        - SVG Primitives (`<svg>`)
        - HTML5 Canvas 2D API (`<canvas>`)
    4. Architecture & Diagram Visualizations
        - SVG (DOM Retained) vs Canvas (Pixel Immediate)
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main architectural difference between SVG and Canvas?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.1.7. Module 7 — HTML5 Advanced APIs & Storage Mechanisms

1. **Lesson 7.2 Geolocation & Device APIs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Geolocation API
        - Position & Error Objects
    4. Architecture & Diagram Visualizations
        - Geolocation Permission Loop
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does Geolocation require HTTPS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 7.3 HTML5 Drag and Drop API**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Drag and Drop Lifecycle
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `event.preventDefault()` required in the `dragover` handler?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 7.4 Web Workers & Multithreading**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Single-Threaded JS & Web Workers Solution
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Main Application Thread (`app.js`)
        - Background Worker Script (`worker.js`)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Can a Web Worker access `localStorage` or DOM elements directly?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.1.8. Module 8 — Web Components & Modern HTML Specifications

1. **Lesson 8.1 Shadow DOM & Custom Elements**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Web Components Suite
        - Custom Element Lifecycle Callbacks
        - Shadow DOM Encapsulation
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main purpose of the Shadow DOM in Web Components?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.1.9. Module 9 — Accessibility (a11y), SEO, & Performance Optimization

1. **Lesson 9.1 Web Content Accessibility Guidelines (WCAG)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The POUR Principles (WCAG 2.1 / 2.2)
        - Conformance Levels
        - Color Contrast Requirements (Level AA)
        - Skip Navigation Links
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the four WCAG POUR principles?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 9.2 Search Engine Optimization (SEO) & Microdata**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - JSON-LD vs Microdata
        - JSON-LD Implementation Example
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is JSON-LD preferred over Microdata for SEO?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 9.3 Performance Optimization & Best Practices**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Resource Hints Summary
        - Native Lazy Loading (`loading="lazy"`)
        - Obsolete & Deprecated HTML Tags
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `preload` and `prefetch`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

### 1.2. CSS3

#### 1.2.1. Module 1 — Core Fundamentals, Syntax, & Specificity Architecture

1. **Lesson 1.1 CSS Syntax & Inclusion Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Syntax Anatomy
        - Inclusion Methods Comparison
        - CSS At-Rules (`@`)
    4. Architecture & Diagram Visualizations
        - External CSS Loading vs `@import` Performance Waterfall
    5. Code & Hardware Implementation
        - External Stylesheet Architecture
    6. Enterprise Real-World Applications
        - Avoiding HTTP Request Waterfalls
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the performance disadvantages of using `@import` inside CSS files?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 1.2 Comprehensive Selector Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Attribute Selectors
        - Combinator Systems
        - Pseudo-Classes & Modern `:has()` Parent Selector
        - Pseudo-Elements (`::before` & `::after`)
    4. Architecture & Diagram Visualizations
        - Combinator Target Matching Tree
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `:nth-child()` and `:nth-of-type()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 1.3 Cascade, Specificity, & Inheritance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Cascade Algorithm
        - Specificity Calculation Vector Matrix `(A, B, C, D)`
        - Cascade Layers (`@layer`) Architecture
    4. Architecture & Diagram Visualizations
        - Cascade Layer Precedence Hierarchy
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do `@layer` declarations alter standard specificity calculations?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.2.2. Module 2 — The Box Model, Sizing, & Layout Fundamentals

1. **Lesson 2.1 The CSS Box Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 4 Box Model Layers
        - `content-box` vs `border-box`
        - Margin Collapsing Mechanics
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `box-sizing: border-box` preferred over `content-box`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 2.2 Display Property & Visual Formatting Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Block Formatting Context (BFC) Triggers
        - `display: none` vs `visibility: hidden` vs `opacity: 0`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the modern standard property for creating a Block Formatting Context?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 2.3 Positioning Systems & Stacking Contexts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Position Modes Matrix
        - Stacking Contexts & $Z$-Index Rules
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does a child with `z-index: 9999` fail to render above an element with `z-index: 2`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 2.4 Sizing Units & Intrinsic Sizing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unit Categories Matrix
        - Intrinsic Sizing Keywords
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the technical difference between `1rem` and `1em`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.2.3. Module 3 — Modern Layout Engine: Flexbox & CSS Grid

1. **Lesson 3.1 Flexible Box Layout (Flexbox)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Flexbox Axes System
        - Main Axis vs Cross Axis Alignment
        - Flex Item Sizing (`flex: grow shrink basis`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `flex: 1` expand to in CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 3.2 CSS Grid Layout System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - 2D Grid vs 1D Flexbox
        - Fractional Unit (`fr`) & `minmax()`
        - Named Grid Areas (`grid-template-areas`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `auto-fill` and `auto-fit` in CSS Grid?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.2.4. Module 4 — Typography, Colors, Backgrounds, & Visual Effects

1. **Lesson 4.1 Advanced Typography & Web Fonts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `@font-face` Syntax & WOFF2
        - Micro-Typography & Line Clamping
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `font-display: swap` in CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 4.2 Modern CSS Color Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Evolution of CSS Color Functions
        - The `color-mix()` Function
        - The `currentcolor` Keyword
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What makes `oklch()` superior to traditional `hsl()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 4.3 Backgrounds, Borders, & Shadows**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Gradient Types
        - Box Shadow Layering (`box-shadow`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between blur-radius and spread-radius in a `box-shadow` property?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 4.4 Visual Effects, Filters, & Blending**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Glassmorphism & `backdrop-filter`
        - Clipping Paths (`clip-path`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does `filter: blur()` differ from `backdrop-filter: blur()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.2.5. Module 5 — Transitions, 2D/3D Transforms, & Animations

1. **Lesson 5.1 CSS Transitions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Transition Properties & Shorthand
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you avoid animating `height` or `margin` properties?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 5.2 2D and 3D Transformations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - 2D vs 3D Transform Functions
        - 3D Card Flipping Setup
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `transform-style: preserve-3d` do?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 5.3 Keyframe Animations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `@keyframes` Syntax & Shorthand
        - `animation-fill-mode`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `animation-fill-mode: forwards` do?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.2.6. Module 6 — Responsive Web Design, Media Queries, & Container Queries

1. **Lesson 6.1 Responsive Architecture Principles**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Mobile-First vs Desktop-First
        - The Viewport Meta Tag
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is Mobile-First CSS architecture preferred over Desktop-First?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 6.2 Media Queries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Modern Range Syntax (Level 4)
        - User Preference Media Features
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is `prefers-reduced-motion` and why is it important for accessibility?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 6.3 Container Queries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Media Queries vs Container Queries
        - Setting Up Container Context
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main problem Container Queries solve that Media Queries could not?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 6.4 Fluid Layout Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Math Functions (`calc`, `min`, `max`, `clamp`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the three parameters passed to `clamp()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.2.7. Module 7 — Advanced CSS Architecture & Modern Specifications

1. **Lesson 7.1 CSS Custom Properties (Variables)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Syntax & Scoping
        - Typed Custom Properties (`@property`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do CSS Custom Properties differ from Sass/SCSS variables?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 7.2 Modern CSS Architecture & Methodologies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - BEM Naming Convention Syntax
        - ITCSS (Inverted Triangle CSS) Layers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does BEM stand for and what are its advantages?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 7.3 Native CSS Nesting & Logical Properties**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Native CSS Nesting (`&`)
        - Physical vs Logical Properties Matrix
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the benefit of Logical Properties over Physical Properties in modern CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.2.8. Module 8 — CSS Frameworks Intro & Production Performance

1. **Lesson 8.1 Utility-First CSS & Tailwind Introduction**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Semantic CSS vs Utility-First CSS
        - Component Extraction (`@apply`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main benefit of Utility-First CSS over traditional semantic CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 8.2 Component Frameworks & Component Styling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Modules Hashing Mechanism
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do CSS Modules prevent global CSS class name collisions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 8.3 Production CSS Performance, Purging, & Optimization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Critical CSS Extraction
        - GPU Layer Promotion (`will-change`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Critical CSS and why does inlining it improve performance?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

### 1.3. Bootstrap

#### 1.3.1. Module 1 — Grid System and Layout

1. **Bootstrap Grid System**
    - **Course Coverage:** 🟢 Covered in Class
    1. The Bootstrap 12-Column Grid
        - Breakpoints
    2. Grid HTML Structure
    3. Equal Width vs Specific Widths
    4. Lab Exercise
2. **Responsive Utilities and Display**
    - **Course Coverage:** 🟢 Covered in Class
    1. Display Property Utilities
        - Classes Format
        - Common Display Values
    2. Responsive Hiding & Showing
    3. Lab Exercise
3. **Flexbox and Alignment Utilities**
    - **Course Coverage:** 🟢 Covered in Class
    1. Flexbox Utility Classes
    2. Lab Exercise
4. **Bootstrap Layout Patterns**
    - **Course Coverage:** 🟢 Covered in Class
    1. Common Bootstrap Layout Patterns
        - Holy Grail / Dashboard Layout
    2. Lab Exercise

#### 1.3.2. Module 2 — Typography and Utilities

1. **Typography System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Typography Helpers & Text Styling
    2. Lab Exercise
2. **Color Palette and Themes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Theme Colors
    2. Lab Exercise
3. **Spacing Utilities**
    - **Course Coverage:** 🟢 Covered in Class
    1. Spacing Notation
    2. Lab Exercise
4. **Borders Shadows and Sizing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Borders, Radius, Shadows, and Sizing
    2. Lab Exercise

#### 1.3.3. Module 3 — Core Components

1. **Buttons and Button Groups**
    - **Course Coverage:** 🟢 Covered in Class
    1. Buttons & Grouping
    2. Lab Exercise
2. **Cards and Accordions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Cards and Accordions
    2. Lab Exercise
3. **Navbars and Navigation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Navbar Component
    2. Lab Exercise
4. **Forms and Input Groups**
    - **Course Coverage:** 🟢 Covered in Class
    1. Form Controls and Input Groups
    2. Lab Exercise
5. **Modals and Tooltips**
    - **Course Coverage:** 🟢 Covered in Class
    1. Modals and Tooltips
    2. Lab Exercise

#### 1.3.4. Module 4 — Advanced Layout and Customization

1. **Flexbox Layout Deep Dive**
    - **Course Coverage:** 🟢 Covered in Class
    1. Deep Dive into Flexbox Helpers
    2. Lab Exercise
2. **CSS Grid in Bootstrap**
    - **Course Coverage:** 🟢 Covered in Class
    1. Opt-in CSS Grid System
    2. Lab Exercise
3. **Customizing Sass Variables**
    - **Course Coverage:** 🟢 Covered in Class
    1. Customizing Bootstrap with SCSS
    2. Lab Exercise
4. **Utility API**
    - **Course Coverage:** 🟢 Covered in Class
    1. Bootstrap Utility API
    2. Lab Exercise
5. **Capstone Portfolio Landing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Capstone Project: Developer Portfolio Landing Page
    2. Lab Exercise

### 1.4. JavaScript

#### 1.4.1. Module 1 — Language Architecture, Engine, & Execution Mechanics

1. **Lesson 1.1 History, Evolution, & ECMAScript Standards**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - TC39 Proposal Process
        - Transpilers vs Polyfills
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Babel Configuration Setup (`babel.config.json`)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the technical difference between a Babel transpiler and a polyfill?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 1.2 JavaScript Engine Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The V8 Engine Execution Pipeline
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are Ignition and TurboFan in the Google Chrome V8 engine?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 1.3 Execution Context, Call Stack, & Memory Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Execution Context Lifecycle
        - Mark-and-Sweep Garbage Collection
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Mark-and-Sweep Garbage Collection in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.4.2. Module 2 — Variables, Data Types, & Operators

1. **Lesson 2.1 Variable Declarations & Scoping**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `var` vs `let` vs `const`
        - The Temporal Dead Zone (TDZ)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the Temporal Dead Zone (TDZ) in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 2.2 Primitive & Reference Data Types**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Primitives vs Reference Types
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the 7 primitive data types in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 2.3 Type Coercion & Comparison Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 8 Falsy Values in JavaScript
        - Abstract (`==`) vs Strict (`===`) Equality
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the 8 falsy values in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 2.4 Comprehensive Operator Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `||` vs `??` (Nullish Coalescing)
        - Optional Chaining (`?.`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the Nullish Coalescing Operator (`??`) differ from the Logical OR Operator (`||`)?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.4.3. Module 3 — Control Flow, Loops, & Iteration Protocols

1. **Lesson 3.1 Conditional Logic & Guard Clauses**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Guard Clauses vs Nested Arrow Code
        - Object Lookup Tables
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Guard Clause and why is it preferred over nested `if-else` blocks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 3.2 Loops & Iteration Constructs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `for...in` vs `for...of`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the technical difference between `for...in` and `for...of` in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 3.3 Iteration Protocols, Iterators, & Generators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Iterable & Iterator Protocols
        - Generator Functions (`function*`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does a Generator function differ from a regular function in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.4.4. Module 4 — Functions, Scope, & Closures

1. **Lesson 4.1 Function Declarations, Expressions, & Arrow Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Declarations vs Expressions vs Arrow Functions
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the `this` keyword behave differently in Arrow Functions compared to Regular Functions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 4.2 Parameters, Arguments, & Return Values**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Rest Parameters (`...args`) vs `arguments` Object
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main advantage of Rest Parameters (`...args`) over the `arguments` object?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 4.3 Scope Chain & Closures**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Lexical Scoping & Scope Chain
        - What is a Closure?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a JavaScript Closure and how does it retain memory?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 4.4 Functional Concepts & Higher-Order Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Pure Functions vs Side Effects
        - Currying
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Currying in Functional JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.4.5. Module 5 — Objects, Arrays, & Data Structures

1. **Lesson 5.1 Object Literals, Descriptors, & Immutability**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Object Immutability Levels
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `Object.freeze()` and `Object.seal()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 5.2 Arrays & Array Higher-Order Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Mutating vs Non-Mutating Methods
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does `.reduce()` work in JavaScript and what is the role of the initial value parameter?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 5.3 Destructuring Assignment & Spread/Rest Operators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unpacking Data Structures
        - Spread (`...`) for Immutable Merging
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do you rename a variable during Object Destructuring in ES6?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 5.4 Keyed Collections: Map, Set, WeakMap, & WeakSet**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Plain Object vs `Map`
        - `WeakMap` & `WeakSet` Garbage Collection
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why can you not iterate over a `WeakMap` or check its size?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.4.6. Module 6 — Asynchronous JavaScript, Promises, & Async/Await

1. **Lesson 6.1 Asynchronous Execution, Callbacks, & Event Queue**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Event Loop & Task Queue Priority
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between the Macrotask Queue and Microtask Queue in the JavaScript Event Loop?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 6.2 ES6 Promises Architecture, States, & Chaining**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Promise States & Immutability
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens if a `.then()` callback returns a plain scalar value versus another Promise?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 6.3 Async/Await & Asynchronous Iteration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Async/Await as Syntactic Sugar
        - Asynchronous Iteration (`for await...of`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens when the `await` keyword is executed in an `async` function?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 6.4 Promise Combinators (all, allSettled, race, any)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Promise Combinators Comparison Matrix
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main difference between `Promise.all()` and `Promise.allSettled()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.4.7. Module 7 — Object-Oriented Programming, Classes, & Prototypes

1. **Lesson 7.1 Prototypes, Prototype Chain, & Prototypal Inheritance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Prototypal Inheritance vs Class-Based Inheritance
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens when a property is accessed on a JavaScript object that does not exist on the instance itself?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 7.2 ES6 Class Syntax & Constructor Mechanics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Classes as Syntactic Sugar
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Are ES6 classes true classes like in Java or C++?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 7.3 Inheritance, Method Overriding, & Super Keyword**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Subclassing & Mandatory `super()`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is calling `super()` mandatory in a subclass constructor before accessing `this`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 7.4 Private Fields, Getters/Setters, & Static Members**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Hard Encapsulation (`#privateField`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do modern `#` private fields in JavaScript differ from the legacy `_` prefix convention?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.4.8. Module 8 — Document Object Model (DOM) Manipulation & Events

1. **Lesson 8.1 DOM Tree Navigation & Selection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `querySelectorAll` (NodeList) vs `getElementsByClassName` (HTMLCollection)
        - Upward Traversal with `.closest()`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main difference between a live `HTMLCollection` and a static `NodeList`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 8.2 Dynamic Element Creation, Modification, & Attributes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `appendChild()` vs `append()`
        - HTML5 `dataset` API
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the HTML5 `dataset` API in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 8.3 Event Handling, Propagation, Bubbling, & Capturing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 3 Event Propagation Phases
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `event.target` and `event.currentTarget`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 8.4 Event Delegation & Custom Event Dispatching**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Event Delegation Architecture
        - Custom Events
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the primary benefits of using the Event Delegation Pattern?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.4.9. Module 9 — Web APIs, Client-Side Storage, & Network Requests

1. **Lesson 9.1 Fetch API & HTTP Network Requests**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The `fetch()` HTTP Status Code Trap
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does `fetch()` not reject when a server returns a 404 or 500 error code?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 9.2 Web Storage: Cookies, LocalStorage, & SessionStorage**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Client Storage Comparison
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main security risk of storing authentication tokens in LocalStorage compared to HttpOnly Cookies?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 9.4 WebSockets & Real-Time Communication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - HTTP Polling vs WebSockets
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Exponential Backoff and why is it essential for WebSocket reconnection strategies?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.4.10. Module 10 — ES6+ Modules, Tooling, & Bundlers

1. **Lesson 10.1 ES6 Modules: Export & Import Syntax**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CommonJS (`require`) vs ES Modules (`import`)
        - Named vs Default Exports
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `mathUtils.js` (Module)
        - File 2: `main.js` (Consumer)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main structural advantage of ES Modules over CommonJS `require()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 10.2 Dynamic Imports & Top-Level Await**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Static Imports vs Dynamic `import()`
        - Top-Level Await
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Code Splitting and how do Dynamic Imports facilitate it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 10.3 Modern Build Tooling, Bundlers, & Tree Shaking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Legacy Bundlers (Webpack) vs Modern Native ESM (Vite)
        - Tree Shaking Mechanics
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Initializing a Lightning-Fast Vite Project
        - Production Build & Source Map Inspection
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Tree Shaking in modern JavaScript build tools and how does it work?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.4.11. Module 11 — Browser Performance, Security, & Optimization

1. **Lesson 11.1 Critical Rendering Path & DOM Reflows**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Critical Rendering Path
        - Reflow vs Repaint vs Layout Thrashing
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Layout Thrashing in JavaScript and how do you prevent it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 11.2 Core Web Vitals & Performance Monitoring**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Google Core Web Vitals Metrics
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Interaction to Next Paint (INP) and how does it differ from FID?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 11.3 Memory Management & Leak Prevention**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Mark-and-Sweep Garbage Collection
        - The 4 Common Memory Leak Patterns
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Detached DOM Node memory leak in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 11.4 Web Security: XSS, CSRF, & CSP Mitigation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - XSS vs CSRF Vulnerability Matrix
        - Content Security Policy (CSP)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Content Security Policy (CSP) and how does it prevent XSS attacks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 1.4.12. Module 12 — Advanced Patterns, Meta-Programming, & Testing

1. **Lesson 12.1 Proxy & Reflect API Meta-Programming**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is Meta-Programming?
        - Proxy Traps & Reflect API
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you use `Reflect` methods inside Proxy handler traps instead of accessing the target directly?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 12.2 Web Workers & Multithreaded JavaScript**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Single-Threaded Main Loop vs Worker Threads
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `worker.js` (Background Thread)
        - File 2: `main.js` (UI Thread)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What capabilities and Web APIs are accessible inside a Web Worker?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 12.3 Service Workers & Offline PWA Caching**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Service Worker Proxy Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `sw.js` (Service Worker Script)
        - File 2: `app.js` (Register Service Worker)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the Stale-While-Revalidate caching strategy work?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 12.4 JavaScript Unit Testing with Vitest**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The AAA Unit Testing Pattern
        - `toBe` vs `toEqual`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Target Module: `math.js`
        - Vitest Test Suite: `math.test.js`
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `toBe` and `toEqual` in Vitest/Jest?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
5. **Lesson 12.5 Integration & E2E Testing with Playwright**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unit Testing vs End-to-End (E2E) Testing
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Playwright Test Suite: `dashboard.spec.js`
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is Playwright preferred over older Selenium or Puppeteer testing frameworks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
6. **Lesson 12.6 Design Patterns: Singleton, Factory, & Observer**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Design Patterns Categories
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main difference between the Observer Pattern and the Publisher-Subscriber (PubSub) Pattern?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
7. **Lesson 12.7 Internationalization (Intl API)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Native ECMAScript `Intl` API
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the performance advantages of using the native `Intl` API over external libraries like Moment.js?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
8. **Lesson 12.8 Web Components & Shadow DOM**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 4 Web Components Technologies
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Usage in HTML:
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why must Custom Element tag names contain a hyphen (`-`)?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
9. **Lesson 12.9 WebAssembly (Wasm) Integration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is WebAssembly (Wasm)?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Is WebAssembly intended to replace JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
10. **Lesson 12.10 Debugging Techniques & Chrome DevTools**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Advanced Breakpoint Types
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Logpoint in Chrome DevTools and how does it differ from a standard Breakpoint?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
11. **Lesson 12.11 Capstone: Real-Time IoT Telemetry Dashboard**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Capstone Enterprise Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Reactive State Store (`store.js`)
        - Capstone Dashboard Application (`app.js`)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does this Vanilla JavaScript Capstone architecture achieve high performance without a frontend framework like React?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

### 1.5. jQuery

#### 1.5.1. Module 1 — Core and DOM Selection

1. **jQuery Setup and Core**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is jQuery?
    2. Lab Exercise
2. **jQuery Selectors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Selecting DOM Elements
    2. Lab Exercise
3. **DOM Traversal and Manipulation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Traversal & Content Manipulation
    2. Lab Exercise

#### 1.5.2. Module 2 — Events and Effects

1. **Event Handling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Event Listeners in jQuery
    2. Lab Exercise
2. **Effects and Animations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Built-in Animation Effects
    2. Lab Exercise
3. **Custom Animation Queues**
    - **Course Coverage:** 🟢 Covered in Class
    1. Animation Queue Control
    2. Lab Exercise

#### 1.5.3. Module 3 — Ajax and Data Exchange

1. **Ajax Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Asynchronous Requests with $.ajax
    2. Lab Exercise
2. **Ajax Shorthand Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Shorthand AJAX Helper Functions
    2. Lab Exercise
3. **Deferreds and Promises**
    - **Course Coverage:** 🟢 Covered in Class
    1. Deferreds & Promises
    2. Lab Exercise

#### 1.5.4. Module 4 — Plugins and Modern Usage

1. **Plugin Development Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Writing Custom jQuery Plugins
    2. Lab Exercise
2. **Popular jQuery Plugins**
    - **Course Coverage:** 🟢 Covered in Class
    1. Integrating Third-Party jQuery Plugins
    2. Lab Exercise
3. **Migrating from jQuery to Vanilla JS**
    - **Course Coverage:** 🟢 Covered in Class
    1. Modern Alternatives to jQuery
    2. Lab Exercise

### 1.6. Python

#### 1.6.1. Module 1 — Setup and Overview

1. **Python Overview and Philosophy**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is Python?
    2. Python's Design Philosophy
    3. Python Versions
    4. Where Python is Used
    5. Python Interpreter Types
    6. Lab Exercise
2. **Environment Setup and Tooling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Installing Python
    2. Virtual Environments
    3. Package Management with pip
    4. Modern Tooling — uv (recommended 2024+)
    5. pyproject.toml
    6. Code Quality Tools
    7. REPL and Interactive Tools
    8. Lab Exercise
3. **CPython Architecture and Execution Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. How Python Code Executes
    2. Inspecting Bytecode
    3. The GIL (Global Interpreter Lock)
    4. Memory Management
        - Reference Counting
        - Garbage Collector (for cycles)
        - Object Interning
    5. `__pycache__` and .pyc Files
    6. Lab Exercise

#### 1.6.2. Module 2 — Core Fundamentals & Control Flow

1. **Lesson 1.5 Structural Pattern Matching (match/case)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `match/case` vs Legacy `if-elif-else`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What makes structural pattern matching different from C/Java `switch` statements?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Existing Jupyter Notebooks

#### 1.6.3. Module 3 — Variables and Types

1. **Variables and Dynamic Typing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Variables in Python
    2. Dynamic vs Static Typing
    3. Type Annotations (Optional Static Hints)
    4. Duck Typing
    5. Identity vs Equality
    6. Lab Exercise
2. **Built-in Primitive Data Types**
    - **Course Coverage:** 🟢 Covered in Class
    1. Numeric Types
    2. Strings
    3. NoneType
    4. Type Conversion
    5. isinstance and type
    6. Lab Exercise
3. **Syntax Rules and Code Style**
    - **Course Coverage:** 🟢 Covered in Class
    1. Python Syntax Fundamentals
        - Indentation (Significant Whitespace)
        - Statements and Line Continuation
        - Comments
        - Docstrings
    2. PEP 8 Style Guide
    3. Naming Conventions Summary
    4. Lab Exercise

#### 1.6.4. Module 4 — Control Flow

1. **Comprehensive Operator Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Python Operators Reference
        - Arithmetic Operators
        - Comparison Operators
        - Logical Operators (Short-Circuit)
        - Bitwise Operators
        - Identity and Membership
        - Walrus Operator `:=` (Python 3.8+)
        - Operator Precedence (high → low)
    2. Lab Exercise
2. **Conditional Execution**
    - **Course Coverage:** 🟢 Covered in Class
    1. if / elif / else
    2. Ternary (Conditional Expression)
    3. Truthy and Falsy Values
    4. Structural Pattern Matching — match/case (3.10+)
        - Matching Sequences and Structures
        - Matching Data Classes
    5. Lab Exercise
3. **Iteration and Loop Structures**
    - **Course Coverage:** 🟢 Covered in Class
    1. for Loops
    2. while Loops
    3. break, continue, else
    4. Advanced Iteration Patterns
    5. Lab Exercise

#### 1.6.5. Module 5 — Collections

1. **Lists and Sequence Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Lists
    2. Modifying Lists
    3. Sorting
    4. List Comprehensions
    5. Copying Lists
    6. Lab Exercise
2. **Tuples and Immutable Sequences**
    - **Course Coverage:** 🟢 Covered in Class
    1. Tuples
    2. Why Tuples?
    3. Named Tuples
    4. typing.NamedTuple (Modern)
    5. Tuple vs List Decision
    6. Lab Exercise
3. **Dictionaries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Dictionaries
    2. CRUD Operations
    3. Iterating Dictionaries
    4. Dictionary Comprehensions
    5. Advanced Dict Types
    6. Merging Dicts (3.9+)
    7. Lab Exercise
4. **Sets and Frozensets**
    - **Course Coverage:** 🟢 Covered in Class
    1. Sets
    2. Set Operations
    3. Modifying Sets
    4. Set Comprehensions
    5. Frozenset (Immutable Set)
    6. Practical Use Cases
    7. Lab Exercise
5. **Strings and Text Processing**
    - **Course Coverage:** 🟢 Covered in Class
    1. String Fundamentals
    2. String Formatting
    3. Essential String Methods
    4. Multi-line and Raw Strings
    5. String Encoding
    6. textwrap for Formatting
    7. Lab Exercise
6. **Advanced Collections Module**
    - **Course Coverage:** 🟢 Covered in Class
    1. collections.Counter
    2. collections.deque (Double-Ended Queue)
    3. heapq — Priority Queue
    4. UserDict and UserList
    5. Lab Exercise

#### 1.6.6. Module 6 — Async Concurrency & Type Hinting

1. **Lesson 5.1 Static Type Hinting & Mypy Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Gradual Typing in Python
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Do Python type hints affect runtime execution speed?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Existing Jupyter Notebooks
2. **Lesson 5.2 Asyncio Event Loop & async/await**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Synchronous vs Asynchronous Execution
        - Python 3.11+ `TaskGroup` Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Is Asyncio multi-threaded?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Existing Jupyter Notebooks
3. **Lesson 5.3 Modern Python Packaging (pyproject.toml & uv)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Legacy `setup.py` vs Modern `pyproject.toml`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Modern `pyproject.toml` Manifest Specification
        - High-Speed `uv` CLI Commands
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is `pyproject.toml` and why is it preferred over `requirements.txt`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Existing Jupyter Notebooks

#### 1.6.7. Module 7 — Functions

1. **Functions and Arguments**
    - **Course Coverage:** 🟢 Covered in Class
    1. Defining Functions
    2. Parameter Types
    3. *args and **kwargs
    4. Default Argument Gotcha
    5. Return Values
    6. Higher-Order Functions
    7. Lab Exercise
2. **Functional Programming in Python**
    - **Course Coverage:** 🟢 Covered in Class
    1. Lambda Functions
    2. map, filter, reduce
    3. functools.partial
    4. functools.lru_cache (Memoization)
    5. operator module
    6. Immutability and Pure Functions
    7. Lab Exercise
3. **List Dict Set Comprehensions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Comprehension Syntax
    2. List Comprehensions
    3. Dict Comprehensions
    4. Set Comprehensions
    5. Generator Expressions
    6. Performance and Readability
    7. When NOT to Use Comprehensions
    8. Lab Exercise

#### 1.6.8. Module 8 — Advanced Python

1. **Closures and Decorators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Closures
    2. The `nonlocal` Keyword
    3. Decorators
    4. Parametrized Decorators
    5. Stacked Decorators
    6. Practical Decorators
    7. Class-Based Decorators
    8. Lab Exercise
2. **Generators and Iterators**
    - **Course Coverage:** 🟢 Covered in Class
    1. The Iterator Protocol
    2. Generator Functions
    3. Generator Expressions
    4. yield with send() and throw()
    5. itertools — Powerful Combinators
    6. Memory Comparison
    7. Lab Exercise

#### 1.6.9. Module 9 — Object-Oriented Programming

1. **Classes and Instance Mechanics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Defining a Class
    2. Properties
    3. `__slots__` — Memory Optimization
    4. Lab Exercise
2. **Inheritance and Polymorphism**
    - **Course Coverage:** 🟢 Covered in Class
    1. Single Inheritance
    2. `super()` and `__init__`
    3. Abstract Base Classes
    4. Method Resolution Order (MRO)
    5. Mixins
    6. Lab Exercise
3. **Magic Dunder Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Essential Dunder Methods
    2. Container Protocol
    3. Context Manager Protocol
    4. Callable Objects `__call__`
    5. Lab Exercise
4. **Dataclasses and Protocols**
    - **Course Coverage:** 🟢 Covered in Class
    1. @dataclass
    2. Advanced dataclass Options
    3. TypedDict
    4. Protocol (Structural Subtyping)
    5. attrs Library
    6. Lab Exercise

#### 1.6.10. Module 10 — Exceptions and File I/O

1. **Exception Handling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Exception Hierarchy
    2. try / except / else / finally
    3. Exception Information
    4. Raising Exceptions
    5. Custom Exceptions
    6. contextlib.suppress
    7. ExceptionGroup (Python 3.11+)
    8. Lab Exercise
2. **Context Managers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Context Manager Protocol
    2. contextlib.contextmanager
    3. Practical Examples
    4. contextlib.ExitStack
    5. Async Context Managers
    6. Lab Exercise
3. **Logging Module**
    - **Course Coverage:** 🟢 Covered in Class
    1. Python Logging Overview
    2. Log Levels
    3. Production Logger Setup
    4. Logging Exceptions
    5. Structured Logging with structlog
    6. Lab Exercise

#### 1.6.11. Module 11 — File I/O and Serialisation

1. **File I/O and Paths**
    - **Course Coverage:** 🟢 Covered in Class
    1. File Operations
    2. File Modes
    3. pathlib — Modern Path Handling
    4. CSV and JSON Files
    5. Lab Exercise
2. **Data Serialization**
    - **Course Coverage:** 🟢 Covered in Class
    1. JSON
    2. pickle — Python Object Serialization
    3. YAML (requires PyYAML)
    4. TOML (Python 3.11+ built-in)
    5. Pydantic Serialization
    6. orjson — Fast JSON
    7. Lab Exercise

#### 1.6.12. Module 12 — Regular Expressions

1. **Regular Expressions**
    - **Course Coverage:** 🟢 Covered in Class
    1. re Module Basics
    2. Regex Syntax Reference
    3. Groups and Named Groups
    4. sub and subn
    5. Compiled Patterns
    6. Lookahead and Lookbehind
    7. Lab Exercise

#### 1.6.13. Module 13 — s and Packages

1. **Modules and Packages**
    - **Course Coverage:** 🟢 Covered in Class
    1. Importing Modules
    2. Module Attributes
    3. Package Structure
    4. Relative Imports
    5. sys.path and Import Resolution
    6. importlib — Dynamic Imports
    7. Lab Exercise

#### 1.6.14. Module 14 — Concurrency

1. **Asyncio and Async/Await**
    - **Course Coverage:** 🟢 Covered in Class
    1. Async/Await Fundamentals
    2. Tasks — Fire and Forget
    3. Async HTTP with aiohttp
    4. asyncio Primitives
    5. Async Context Managers and Generators
    6. Lab Exercise
2. **Threading and Multiprocessing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Threading
    2. Thread Synchronization
    3. concurrent.futures — High-Level Interface
    4. multiprocessing — True Parallelism
    5. When to Use What
    6. Lab Exercise

#### 1.6.15. Module 15 — Scientific Python

1. **NumPy Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. NumPy Basics
    2. Indexing and Slicing
    3. Vectorized Operations (No Loops!)
    4. Broadcasting
    5. Matrix Operations
    6. Lab Exercise
2. **Pandas Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Pandas Basics
    2. Selection and Filtering
    3. Essential Operations
    4. GroupBy
    5. Merge and Join
    6. Lab Exercise
3. **Matplotlib and Visualization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Matplotlib Basics
    2. Common Plot Types
    3. Subplots
    4. Seaborn — Statistical Plots
    5. Lab Exercise
4. **Hardware Interfacing with Python**
    - **Course Coverage:** 🟢 Covered in Class
    1. Raspberry Pi GPIO
    2. gpiozero — Higher Level
    3. PySerial — UART Communication
    4. smbus2 — I2C Communication
    5. MicroPython
    6. Lab Exercise

#### 1.6.16. Module 16 — Debugging and Testing

1. **Debugging and Profiling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Python Debugger (pdb)
        - pdb Commands
    2. Profiling with cProfile
    3. timeit — Micro-Benchmarking
    4. Memory Profiling
    5. Line Profiler
    6. Lab Exercise
2. **Testing with Pytest**
    - **Course Coverage:** 🟢 Covered in Class
    1. Pytest Basics
    2. Fixtures
    3. Parametrize
    4. Mocking
    5. Coverage
    6. Property-Based Testing with Hypothesis
    7. Lab Exercise

### 1.7. Advanced Python & Professional Practices

#### 1.7.1. Module 1 — Python Internals

1. **Python Object Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Memory Management and GC**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Python Bytecode**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Global Interpreter Lock**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Python Data Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 1.7.2. Module 2 — Advanced Object-Oriented Python

1. **Python Data Model & Special Dunder Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Python Data Model & Special Dunder Methods
    2. Core Concept
        - Core Concept: Python Data Model & Special Dunder Methods
    3. Syntax
        - Syntax: Python Data Model & Special Dunder Methods
    4. Example
        - Example: Python Data Model & Special Dunder Methods
    5. Pitfall
        - Pitfall: Python Data Model & Special Dunder Methods
    6. Q & A
        - Q & A: Python Data Model & Special Dunder Methods
2. **Multiple Inheritance & Method Resolution Order (MRO)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Multiple Inheritance & Method Resolution Order (MRO)
    2. Core Concept
        - Core Concept: Multiple Inheritance & Method Resolution Order (MRO)
    3. Syntax
        - Syntax: Multiple Inheritance & Method Resolution Order (MRO)
    4. Example
        - Example: Multiple Inheritance & Method Resolution Order (MRO)
    5. Pitfall
        - Pitfall: Multiple Inheritance & Method Resolution Order (MRO)
    6. Q & A
        - Q & A: Multiple Inheritance & Method Resolution Order (MRO)
3. **Abstract Base Classes (abc module)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Abstract Base Classes (abc module)
    2. Core Concept
        - Core Concept: Abstract Base Classes (abc module)
    3. Syntax
        - Syntax: Abstract Base Classes (abc module)
    4. Example
        - Example: Abstract Base Classes (abc module)
    5. Pitfall
        - Pitfall: Abstract Base Classes (abc module)
    6. Q & A
        - Q & A: Abstract Base Classes (abc module)
4. **Properties, Getters, and Setters**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Properties, Getters, and Setters
    2. Core Concept
        - Core Concept: Properties, Getters, and Setters
    3. Syntax
        - Syntax: Properties, Getters, and Setters
    4. Example
        - Example: Properties, Getters, and Setters
    5. Pitfall
        - Pitfall: Properties, Getters, and Setters
    6. Q & A
        - Q & A: Properties, Getters, and Setters
5. **Dataclasses & Pydantic Data Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Dataclasses & Pydantic Data Validation
    2. Core Concept
        - Core Concept: Dataclasses & Pydantic Data Validation
    3. Syntax
        - Syntax: Dataclasses & Pydantic Data Validation
    4. Example
        - Example: Dataclasses & Pydantic Data Validation
    5. Pitfall
        - Pitfall: Dataclasses & Pydantic Data Validation
    6. Q & A
        - Q & A: Dataclasses & Pydantic Data Validation

#### 1.7.3. Module 3 — Functional Programming & Metaprogramming

1. **First-Class Functions, Closures, and Higher-Order Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: First-Class Functions, Closures, and Higher-Order Functions
    2. Core Concept
        - Core Concept: First-Class Functions, Closures, and Higher-Order Functions
    3. Syntax
        - Syntax: First-Class Functions, Closures, and Higher-Order Functions
    4. Example
        - Example: First-Class Functions, Closures, and Higher-Order Functions
    5. Pitfall
        - Pitfall: First-Class Functions, Closures, and Higher-Order Functions
    6. Q & A
        - Q & A: First-Class Functions, Closures, and Higher-Order Functions
2. **Function & Class Decorators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Function & Class Decorators
    2. Core Concept
        - Core Concept: Function & Class Decorators
    3. Syntax
        - Syntax: Function & Class Decorators
    4. Example
        - Example: Function & Class Decorators
    5. Pitfall
        - Pitfall: Function & Class Decorators
    6. Q & A
        - Q & A: Function & Class Decorators
3. **Decorators with Arguments & Wraps**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Decorators with Arguments & Wraps
    2. Core Concept
        - Core Concept: Decorators with Arguments & Wraps
    3. Syntax
        - Syntax: Decorators with Arguments & Wraps
    4. Example
        - Example: Decorators with Arguments & Wraps
    5. Pitfall
        - Pitfall: Decorators with Arguments & Wraps
    6. Q & A
        - Q & A: Decorators with Arguments & Wraps
4. **Generators, Yield, and Generator Expressions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Generators, Yield, and Generator Expressions
    2. Core Concept
        - Core Concept: Generators, Yield, and Generator Expressions
    3. Syntax
        - Syntax: Generators, Yield, and Generator Expressions
    4. Example
        - Example: Generators, Yield, and Generator Expressions
    5. Pitfall
        - Pitfall: Generators, Yield, and Generator Expressions
    6. Q & A
        - Q & A: Generators, Yield, and Generator Expressions
5. **Iterators, Iterables, and Custom Iterators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Iterators, Iterables, and Custom Iterators
    2. Core Concept
        - Core Concept: Iterators, Iterables, and Custom Iterators
    3. Syntax
        - Syntax: Iterators, Iterables, and Custom Iterators
    4. Example
        - Example: Iterators, Iterables, and Custom Iterators
    5. Pitfall
        - Pitfall: Iterators, Iterables, and Custom Iterators
    6. Q & A
        - Q & A: Iterators, Iterables, and Custom Iterators

#### 1.7.4. Module 4 — Functional Programming

1. **First-Class Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Closures and Nonlocal**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Decorators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Generators and Yield**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Itertools and Functools**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 1.7.5. Module 5 — OOP Advanced

1. **Magic Methods Deep Dive**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Class Methods and Static Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Properties and Descriptors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Metaclasses**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Abstract Base Classes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 1.7.6. Module 6 — Memory Management & Context Managers

1. **Python Memory Management & Garbage Collection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Python Memory Management & Garbage Collection
    2. Core Concept
        - Core Concept: Python Memory Management & Garbage Collection
    3. Syntax
        - Syntax: Python Memory Management & Garbage Collection
    4. Example
        - Example: Python Memory Management & Garbage Collection
    5. Pitfall
        - Pitfall: Python Memory Management & Garbage Collection
    6. Q & A
        - Q & A: Python Memory Management & Garbage Collection
2. **Context Managers & the with Statement**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Context Managers & the with Statement
    2. Core Concept
        - Core Concept: Context Managers & the with Statement
    3. Syntax
        - Syntax: Context Managers & the with Statement
    4. Example
        - Example: Context Managers & the with Statement
    5. Pitfall
        - Pitfall: Context Managers & the with Statement
    6. Q & A
        - Q & A: Context Managers & the with Statement
3. **Creating Context Managers via contextlib**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Creating Context Managers via contextlib
    2. Core Concept
        - Core Concept: Creating Context Managers via contextlib
    3. Syntax
        - Syntax: Creating Context Managers via contextlib
    4. Example
        - Example: Creating Context Managers via contextlib
    5. Pitfall
        - Pitfall: Creating Context Managers via contextlib
    6. Q & A
        - Q & A: Creating Context Managers via contextlib
4. **Weak References & Memory Optimization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Weak References & Memory Optimization
    2. Core Concept
        - Core Concept: Weak References & Memory Optimization
    3. Syntax
        - Syntax: Weak References & Memory Optimization
    4. Example
        - Example: Weak References & Memory Optimization
    5. Pitfall
        - Pitfall: Weak References & Memory Optimization
    6. Q & A
        - Q & A: Weak References & Memory Optimization
5. **Python Metaclasses & Dynamic Code Execution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Python Metaclasses & Dynamic Code Execution
    2. Core Concept
        - Core Concept: Python Metaclasses & Dynamic Code Execution
    3. Syntax
        - Syntax: Python Metaclasses & Dynamic Code Execution
    4. Example
        - Example: Python Metaclasses & Dynamic Code Execution
    5. Pitfall
        - Pitfall: Python Metaclasses & Dynamic Code Execution
    6. Q & A
        - Q & A: Python Metaclasses & Dynamic Code Execution

#### 1.7.7. Module 7 — Concurrency & Async Programming

1. **Threading vs Multiprocessing in Python**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Threading vs Multiprocessing in Python
    2. Core Concept
        - Core Concept: Threading vs Multiprocessing in Python
    3. Syntax
        - Syntax: Threading vs Multiprocessing in Python
    4. Example
        - Example: Threading vs Multiprocessing in Python
    5. Pitfall
        - Pitfall: Threading vs Multiprocessing in Python
    6. Q & A
        - Q & A: Threading vs Multiprocessing in Python
2. **Global Interpreter Lock (GIL) Deep Dive**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Global Interpreter Lock (GIL) Deep Dive
    2. Core Concept
        - Core Concept: Global Interpreter Lock (GIL) Deep Dive
    3. Syntax
        - Syntax: Global Interpreter Lock (GIL) Deep Dive
    4. Example
        - Example: Global Interpreter Lock (GIL) Deep Dive
    5. Pitfall
        - Pitfall: Global Interpreter Lock (GIL) Deep Dive
    6. Q & A
        - Q & A: Global Interpreter Lock (GIL) Deep Dive
3. **ThreadPoolExecutor & ProcessPoolExecutor**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: ThreadPoolExecutor & ProcessPoolExecutor
    2. Core Concept
        - Core Concept: ThreadPoolExecutor & ProcessPoolExecutor
    3. Syntax
        - Syntax: ThreadPoolExecutor & ProcessPoolExecutor
    4. Example
        - Example: ThreadPoolExecutor & ProcessPoolExecutor
    5. Pitfall
        - Pitfall: ThreadPoolExecutor & ProcessPoolExecutor
    6. Q & A
        - Q & A: ThreadPoolExecutor & ProcessPoolExecutor
4. **Asyncio Event Loop, Async/Await Syntax**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Asyncio Event Loop, Async/Await Syntax
    2. Core Concept
        - Core Concept: Asyncio Event Loop, Async/Await Syntax
    3. Syntax
        - Syntax: Asyncio Event Loop, Async/Await Syntax
    4. Example
        - Example: Asyncio Event Loop, Async/Await Syntax
    5. Pitfall
        - Pitfall: Asyncio Event Loop, Async/Await Syntax
    6. Q & A
        - Q & A: Asyncio Event Loop, Async/Await Syntax
5. **Gathering Tasks & Asynchronous I/O Performance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Gathering Tasks & Asynchronous I/O Performance
    2. Core Concept
        - Core Concept: Gathering Tasks & Asynchronous I/O Performance
    3. Syntax
        - Syntax: Gathering Tasks & Asynchronous I/O Performance
    4. Example
        - Example: Gathering Tasks & Asynchronous I/O Performance
    5. Pitfall
        - Pitfall: Gathering Tasks & Asynchronous I/O Performance
    6. Q & A
        - Q & A: Gathering Tasks & Asynchronous I/O Performance

#### 1.7.8. Module 8 — Concurrency

1. **Threading**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Multiprocessing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Asyncio**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Concurrent Futures**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Asyncio Advanced Patterns**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 1.7.9. Module 9 — Python Packaging and Tools

1. **Virtual Environments**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Writing Python Packages**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Publishing to PyPI**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Type Hints and Mypy**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Testing with Pytest**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 1.7.10. Module 10 — Packaging & Testing Frameworks

1. **Unit Testing with Pytest & Fixtures**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Unit Testing with Pytest & Fixtures
    2. Core Concept
        - Core Concept: Unit Testing with Pytest & Fixtures
    3. Syntax
        - Syntax: Unit Testing with Pytest & Fixtures
    4. Example
        - Example: Unit Testing with Pytest & Fixtures
    5. Pitfall
        - Pitfall: Unit Testing with Pytest & Fixtures
    6. Q & A
        - Q & A: Unit Testing with Pytest & Fixtures
2. **Mocking Dependencies with unittest.mock**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Mocking Dependencies with unittest.mock
    2. Core Concept
        - Core Concept: Mocking Dependencies with unittest.mock
    3. Syntax
        - Syntax: Mocking Dependencies with unittest.mock
    4. Example
        - Example: Mocking Dependencies with unittest.mock
    5. Pitfall
        - Pitfall: Mocking Dependencies with unittest.mock
    6. Q & A
        - Q & A: Mocking Dependencies with unittest.mock
3. **Code Coverage Analysis & Linting (Ruff, Black, Flake8)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Code Coverage Analysis & Linting (Ruff, Black, Flake8)
    2. Core Concept
        - Core Concept: Code Coverage Analysis & Linting (Ruff, Black, Flake8)
    3. Syntax
        - Syntax: Code Coverage Analysis & Linting (Ruff, Black, Flake8)
    4. Example
        - Example: Code Coverage Analysis & Linting (Ruff, Black, Flake8)
    5. Pitfall
        - Pitfall: Code Coverage Analysis & Linting (Ruff, Black, Flake8)
    6. Q & A
        - Q & A: Code Coverage Analysis & Linting (Ruff, Black, Flake8)
4. **Type Hinting & Static Analysis with Mypy**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Type Hinting & Static Analysis with Mypy
    2. Core Concept
        - Core Concept: Type Hinting & Static Analysis with Mypy
    3. Syntax
        - Syntax: Type Hinting & Static Analysis with Mypy
    4. Example
        - Example: Type Hinting & Static Analysis with Mypy
    5. Pitfall
        - Pitfall: Type Hinting & Static Analysis with Mypy
    6. Q & A
        - Q & A: Type Hinting & Static Analysis with Mypy
5. **Building & Publishing Python Packages to PyPI**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Building & Publishing Python Packages to PyPI
    2. Core Concept
        - Core Concept: Building & Publishing Python Packages to PyPI
    3. Syntax
        - Syntax: Building & Publishing Python Packages to PyPI
    4. Example
        - Example: Building & Publishing Python Packages to PyPI
    5. Pitfall
        - Pitfall: Building & Publishing Python Packages to PyPI
    6. Q & A
        - Q & A: Building & Publishing Python Packages to PyPI

#### 1.7.11. Module 11 — Advanced Patterns

1. **Context Managers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Design Patterns in Python**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Data Classes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Protocol and Structural Subtyping**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Python Performance Optimization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 1.7.12. Module 12 — Design Patterns in Python

1. **Creational Patterns (Singleton, Factory, Builder)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Creational Patterns (Singleton, Factory, Builder)
    2. Core Concept
        - Core Concept: Creational Patterns (Singleton, Factory, Builder)
    3. Syntax
        - Syntax: Creational Patterns (Singleton, Factory, Builder)
    4. Example
        - Example: Creational Patterns (Singleton, Factory, Builder)
    5. Pitfall
        - Pitfall: Creational Patterns (Singleton, Factory, Builder)
    6. Q & A
        - Q & A: Creational Patterns (Singleton, Factory, Builder)
2. **Structural Patterns (Adapter, Decorator, Facade)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Structural Patterns (Adapter, Decorator, Facade)
    2. Core Concept
        - Core Concept: Structural Patterns (Adapter, Decorator, Facade)
    3. Syntax
        - Syntax: Structural Patterns (Adapter, Decorator, Facade)
    4. Example
        - Example: Structural Patterns (Adapter, Decorator, Facade)
    5. Pitfall
        - Pitfall: Structural Patterns (Adapter, Decorator, Facade)
    6. Q & A
        - Q & A: Structural Patterns (Adapter, Decorator, Facade)
3. **Behavioral Patterns (Observer, Strategy, State)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Behavioral Patterns (Observer, Strategy, State)
    2. Core Concept
        - Core Concept: Behavioral Patterns (Observer, Strategy, State)
    3. Syntax
        - Syntax: Behavioral Patterns (Observer, Strategy, State)
    4. Example
        - Example: Behavioral Patterns (Observer, Strategy, State)
    5. Pitfall
        - Pitfall: Behavioral Patterns (Observer, Strategy, State)
    6. Q & A
        - Q & A: Behavioral Patterns (Observer, Strategy, State)
4. **Clean Architecture & Dependency Injection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Clean Architecture & Dependency Injection
    2. Core Concept
        - Core Concept: Clean Architecture & Dependency Injection
    3. Syntax
        - Syntax: Clean Architecture & Dependency Injection
    4. Example
        - Example: Clean Architecture & Dependency Injection
    5. Pitfall
        - Pitfall: Clean Architecture & Dependency Injection
    6. Q & A
        - Q & A: Clean Architecture & Dependency Injection
5. **Refactoring Legacy Python Codebases**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Refactoring Legacy Python Codebases
    2. Core Concept
        - Core Concept: Refactoring Legacy Python Codebases
    3. Syntax
        - Syntax: Refactoring Legacy Python Codebases
    4. Example
        - Example: Refactoring Legacy Python Codebases
    5. Pitfall
        - Pitfall: Refactoring Legacy Python Codebases
    6. Q & A
        - Q & A: Refactoring Legacy Python Codebases

### 1.8. MySQL

#### 1.8.1. Module 1 — MySQL Foundations

1. **Database Architecture and Relational Concepts**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is a Relational Database?
        - Key Concepts
    2. MySQL Architecture
        - Storage Engines Comparison
    3. ACID Properties
    4. SQL Categories
    5. Connecting to MySQL
    6. Lab Exercise
2. **Database Design ER Modeling and Normalization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Entity-Relationship Modeling
        - ER to Schema Mapping
        - Normal Forms
        - Normalization Example
    2. Lab

#### 1.8.2. Module 2 — SQL Fundamentals

1. **DDL and Integrity Constraints**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - CREATE TABLE
        - ALTER TABLE
        - ON DELETE / ON UPDATE Actions
        - Indexes Created Automatically
    2. Lab
2. **DML and Basic Retrieval**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - INSERT
        - UPDATE
        - DELETE
        - SELECT with Filtering
    2. Lab
3. **Aggregation Grouping and Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Aggregate Functions
        - WITH ROLLUP
        - String Functions
        - Date Functions
        - CASE Expression
    2. Lab
4. **Relational Joins and Set Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - JOIN Types
        - Multi-Table Join
        - Set Operations
    2. Lab

#### 1.8.3. Module 3 — Modern Analytical SQL & Window Functions

1. **Lesson 3.1 MySQL 8.4 Analytical Window Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `GROUP BY` vs Window Functions (`OVER`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `RANK()` and `DENSE_RANK()` in SQL?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Existing SQL Reference Files

#### 1.8.4. Module 4 — Advanced SQL

1. **Subqueries CTEs and Window Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Subqueries
        - Common Table Expressions (CTEs)
        - Recursive CTE — Org Chart
        - Window Functions
    2. Lab

#### 1.8.5. Module 5 — Programmability

1. **Stored Procedures Functions Triggers and Events**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Stored Procedures
        - User-Defined Functions
        - Triggers
        - Events (Scheduled Jobs)
    2. Lab
2. **Transactions Concurrency and Locking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Transactions
        - ACID Properties
        - Isolation Levels
        - Lock Types
    2. Lab

#### 1.8.6. Module 6 — Administration

1. **Database Security Administration and Replication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - User Management
        - MySQL Roles (8.0+)
        - Backup and Restore
        - Replication Overview
    2. Lab
2. **MySQL Integration with Python**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - mysql-connector-python
        - Connection Pooling
        - SQLAlchemy ORM (MySQL)
        - Async MySQL (aiomysql)
    2. Lab

### 1.9. SQL Server

#### 1.9.1. Module 1 — Setup and TSQL Fundamentals

1. **SQL Server Setup and SSMS**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of SQL Server Setup and SSMS
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
2. **DDL Fundamentals: CREATE, ALTER, DROP**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of DDL Fundamentals: CREATE, ALTER, DROP
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
3. **DML: INSERT, UPDATE, DELETE, MERGE**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of DML: INSERT, UPDATE, DELETE, MERGE
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
4. **SQL Server Data Types and NULL Handling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of SQL Server Data Types and NULL Handling
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
5. **Built-in System Functions (Date, String, Math)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Built-in System Functions (Date, String, Math)
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise

#### 1.9.2. Module 2 — Retrieval and Filtering

1. **SELECT and Filtering with WHERE**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of SELECT and Filtering with WHERE
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
2. **Sorting and Paging (OFFSET-FETCH)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Sorting and Paging (OFFSET-FETCH)
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
3. **JOINS: INNER, LEFT, RIGHT, FULL, CROSS**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of JOINS: INNER, LEFT, RIGHT, FULL, CROSS
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
4. **Subqueries: Correlated and Uncorrelated**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Subqueries: Correlated and Uncorrelated
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
5. **Common Table Expressions (CTEs)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Common Table Expressions (CTEs)
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
6. **Set Operators: UNION, UNION ALL, INTERSECT, EXCEPT**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Set Operators: UNION, UNION ALL, INTERSECT, EXCEPT
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise

#### 1.9.3. Module 3 — Aggregations and Window Functions

1. **GROUP BY and HAVING Clause**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of GROUP BY and HAVING Clause
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
2. **Window Functions: ROW_NUMBER, RANK, DENSE_RANK**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Window Functions: ROW_NUMBER, RANK, DENSE_RANK
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
3. **Analytic Functions: LEAD, LAG, FIRST_VALUE**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Analytic Functions: LEAD, LAG, FIRST_VALUE
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
4. **GROUPING SETS, ROLLUP, and CUBE**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of GROUPING SETS, ROLLUP, and CUBE
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
5. **PIVOT and UNPIVOT Operators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of PIVOT and UNPIVOT Operators
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise

#### 1.9.4. Module 4 — Indexes and Optimization

1. **Execution Plans and Query Tuning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Execution Plans and Query Tuning
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise

#### 1.9.5. Module 5 — Programmability and Transactions

1. **Stored Procedures and Parameters**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Stored Procedures and Parameters
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
2. **User-Defined Functions (Scalar and Table-Valued)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of User-Defined Functions (Scalar and Table-Valued)
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
3. **Triggers: AFTER and INSTEAD OF**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Triggers: AFTER and INSTEAD OF
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
4. **Transactions and Isolation Levels**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Transactions and Isolation Levels
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
5. **Error Handling with TRY...CATCH**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Error Handling with TRY...CATCH
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
6. **Dynamic SQL and sp_executesql**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Dynamic SQL and sp_executesql
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
7. **Cursors vs Set-Based Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Cursors vs Set-Based Operations
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise

#### 1.9.6. Module 6 — Administration and Security

1. **Backup and Restore Strategies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Backup and Restore Strategies
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
2. **Logins, Users, Roles, and Permissions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Logins, Users, Roles, and Permissions
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
3. **SQL Server Agent and Job Scheduling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of SQL Server Agent and Job Scheduling
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
4. **TempDB Management and Concurrency**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of TempDB Management and Concurrency
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
5. **Always On Availability Groups Overview**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Always On Availability Groups Overview
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
6. **Auditing and Compliance Features**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Auditing and Compliance Features
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise

#### 1.9.7. Module 7 — Enterprise Architecture

1. **Capstone Enterprise Database Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Capstone Enterprise Database Architecture
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
2. **Introduction to SSIS (SQL Server Integration Services)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Introduction to SSIS (SQL Server Integration Services)
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise
3. **Introduction to SSRS (SQL Server Reporting Services)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview of Introduction to SSRS (SQL Server Reporting Services)
        - T-SQL Syntax & Technical Mechanics
    2. Lab Exercise

## 2. Term 2

### 2.1. Git Version Control

#### 2.1.1. Module 1 — Introduction

1. **Web Architecture And Protocols**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Client-Server Architecture
        - The Request-Response Cycle
        - HTTP vs HTTPS Protocols
        - HTTP Request Methods (Verbs)
        - HTTP Status Codes Classification
        - Web Servers vs Application Servers
        - Identifiers: URI, URL, and URN
        - Domain Name System (DNS) Resolution Tracing
    4. Architecture & Diagram Visualizations
        - DNS Resolution & HTTP Request Sequence
    5. Code & Hardware Implementation
        - Deconstructing Raw HTTP/1.1 Request and Response Payload
        - Command Line Inspection with cURL
    6. Enterprise Real-World Applications
        - Case Study: High-Throughput IoT Gateway Architecture
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspect Web Request Lifecycle using Chrome DevTools & Python
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens under the hood when you type `https://example.com` into a browser address bar and press Enter?
        - Q2: What is the technical difference between HTTP `POST`, `PUT`, and `PATCH` methods?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Starter Code
        - Success Criteria
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax & Command Cheat Sheet
        - Official References
2. **Browser Rendering Engine Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Anatomy of a Modern Web Browser
        - Major Browser Engines
        - The 5 Stages of the Rendering Pipeline
        - Reflow vs Repaint Trigger Comparison
    4. Architecture & Diagram Visualizations
        - Critical Rendering Path Architecture
    5. Code & Hardware Implementation
        - Script Execution Blocking Modes (`async` vs `defer`)
    6. Enterprise Real-World Applications
        - Critical CSS Inline Pattern for Enterprise E-Commerce
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Profile Reflow & Layout Thrashing in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Reflow and Repaint, and how do you minimize them?
        - Q2: How does the browser construct the Render Tree, and why are `display: none` elements excluded?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Requirements
        - Starter Code Snippet
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Cheat Sheet
        - Official References
3. **Html Standards And Document Structure**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Evolution of HTML Standards
        - The DOCTYPE Declaration & Rendering Modes
        - Root Element (`<html>`) & Language Attribute
        - Character Encodings (ASCII vs UTF-8)
        - Viewport Configuration for Mobile Responsiveness
        - Metadata & Social Media Protocol (Open Graph)
    4. Architecture & Diagram Visualizations
        - Complete HTML5 Document Architecture Tree
    5. Code & Hardware Implementation
        - Production-Ready HTML5 Boilerplate Template
    6. Enterprise Real-World Applications
        - Open Graph Debugging & Rich Social Cards
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Build & Validate an Enterprise Boilerplate
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Standards Mode and Quirks Mode in modern browsers?
        - Q2: Why is the WHATWG specification referred to as a "Living Standard"?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Starter Requirements
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
4. **Html Syntax Rules And Element Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Tag Syntax & Element Composition
        - Standard Elements vs Void (Self-Closing) Elements
        - Attribute Categories
        - Block-Level vs Inline-Level vs Inline-Block
        - Element Nesting Rules & DOM Tree Integrity
        - HTML Entity Encoding & Escaping
    4. Architecture & Diagram Visualizations
        - Block vs Inline Box Model Layout Geometry
    5. Code & Hardware Implementation
        - Demonstrating Block, Inline, and Data Attributes
    6. Enterprise Real-World Applications
        - Data Attributes in Modern Web Frameworks & IoT Dashboards
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspecting Box Geometry & Dataset Properties in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the exact visual difference between Block-level, Inline-level, and Inline-Block elements?
        - Q2: What are HTML Void Elements, and how do they differ from standard elements in DOM parsing?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
        - Starter Requirements
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
5. **Text Content And Formatting Elements**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Heading Hierarchy (`<h1>` through `<h6>`)
        - Semantic vs Presentational Text Formatting
        - Computer Code & Technical Documentation Elements
        - Quotations, Citations, & Abbreviations
        - Bidirectional Text Formatting (`<bdo>` & `<bdi>`)
    4. Architecture & Diagram Visualizations
        - Accessible Heading Tree Outline
    5. Code & Hardware Implementation
        - Technical Documentation Markup Example
    6. Enterprise Real-World Applications
        - Accessible Developer Portals & CLI Documentation
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Build a Technical Quick Reference Sheet
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the semantic difference between `<strong>` and `<b>`, and `<em>` and `<i>`?
        - Q2: How do `<bdo>` and `<bdi>` differ when handling internationalized text?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
6. **Hyperlinks And Anchor Navigation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Anchor Element Architecture
        - URL Types & Path Resolution Rules
        - Fragment Identifiers & In-Page Jumping
        - Link Targets & Vulnerability Hardening (`tabnabbing`)
        - Non-HTML Protocols & Devices Integration
        - Download Attribute & Resource Hints
    4. Architecture & Diagram Visualizations
        - Reverse Tabnabbing Attack vs Hardened Fix
    5. Code & Hardware Implementation
        - Comprehensive Navigation Portal (`navigation_demo.html`)
    6. Enterprise Real-World Applications
        - Multi-Tenant SaaS & IoT Gateway Navigation
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Test Reverse Tabnabbing Security in Browser Console
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What security risk is introduced by `target="_blank"`, and how does `rel="noopener"` fix it?
        - Q2: What is the difference between `<link rel="prefetch">` and `<link rel="preload">`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
7. **Structural Semantic Elements**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Semantic Web Philosophy
        - Structural Landmark Elements
        - Content Sectioning Elements
        - Interactive Native Components
        - Figures, Captions & Machine-Readable Time
    4. Architecture & Diagram Visualizations
        - Complete Semantic HTML5 Web Page Layout
    5. Code & Hardware Implementation
        - Semantic Web Page Implementation (`semantic_layout.html`)
    6. Enterprise Real-World Applications
        - Native Dialog Modals vs Heavy JS Libraries
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Test Native Dialog & Details Accordion
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the exact semantic distinction between an `<article>` and a `<section>`?
        - Q2: How does the native HTML5 `<dialog>` element improve accessibility over custom `<div>` modals?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
8. **Document Outline And Accessibility Tree**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Accessibility Tree (AOM) Architecture
        - HTML5 Semantic Elements vs ARIA Landmark Roles
        - Core ARIA Attributes & Properties
        - Keyboard Focus Management & `tabindex` Rules
    4. Architecture & Diagram Visualizations
        - DOM Tree vs Accessibility Tree Mapping
    5. Code & Hardware Implementation
        - Fully Accessible Component Suite (`accessible_suite.html`)
    6. Enterprise Real-World Applications
        - Automated Accessibility Testing in CI/CD Pipelines
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Audit Accessibility Tree Properties in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `tabindex="0"`, `tabindex="-1"`, and `tabindex="1"`?
        - Q2: How does `aria-live="polite"` differ from `aria-live="assertive"`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
        - Objective
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
        - Key Takeaways
        - Quick Syntax Reference
        - Official References
9. **List Elements And Structure**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unordered Lists (`<ul>`) & Ordered Lists (`<ol>`)
        - Description Lists (`<dl>`, `<dt>`, `<dd>`)
        - Nesting Rules for Lists
    4. Architecture & Diagram Visualizations
        - List Tree DOM Structure
    5. Code & Hardware Implementation
        - Semantic Navigation & Metadata Lists
    6. Enterprise Real-World Applications
        - Accessible Navigation Menus
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Build a Nested IoT Setup Procedure List
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: When should you use a Description List (`<dl>`) instead of an Unordered List (`<ul>`)?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
10. **Tabular Data And Advanced Table Markup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Semantic Table Architecture
        - Cell Spanning (`colspan` & `rowspan`)
        - Column Groups (`<colgroup>` & `<col>`)
        - Table Accessibility & Header Scoping
        - Responsive Mobile Table Patterns
    4. Architecture & Diagram Visualizations
        - Accessible Table DOM Hierarchy
    5. Code & Hardware Implementation
        - Complex Accessible Matrix Table (`matrix_table.html`)
    6. Enterprise Real-World Applications
        - Financial Reports & System Metrics Dashboards
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspect Accessible Headers in DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of the `scope` attribute on `<th>` elements?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
11. **Form Architecture And Submissions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Form Architecture
        - Key `<form>` Attributes
        - HTTP Submission Methods: GET vs POST
        - Encoding Types (`enctype`)
    4. Architecture & Diagram Visualizations
        - Form Submission Payload Pipeline
    5. Code & Hardware Implementation
        - File Upload & Search Form Examples
    6. Enterprise Real-World Applications
        - Firmware Uploads & Cloud API Integration
    7. Guided Step-by-Step Hands-On Exercise
        - Task: Inspect Payload Formats in Chrome DevTools
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens if a developer omits `enctype="multipart/form-data"` on a form containing a file input?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
12. **Form Controls And Input Types**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Label Association (`<label>`)
        - Form Controls Classification Matrix
        - Form Grouping & Visual Metering
    4. Architecture & Diagram Visualizations
        - Accessible Form Fieldset Hierarchy
    5. Code & Hardware Implementation
        - IoT Device Configuration Form (`iot_config_form.html`)
    6. Enterprise Real-World Applications
        - Soft-Keyboards & Mobile Optimization
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `<select>` dropdowns and `<datalist>` autocomplete inputs?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
13. **Native Client Side Form Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Native Validation Attributes
        - CSS Validation Pseudo-Classes
        - The Constraint Validation API (JavaScript)
    4. Architecture & Diagram Visualizations
        - Constraint Validation Flow
    5. Code & Hardware Implementation
        - Custom Validation & RegEx Portal (`validation_portal.html`)
    6. Enterprise Real-World Applications
        - Client-Side Validation is NOT Security
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is `ValidityState` in the HTML5 Constraint Validation API?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
14. **Media Elements Images Audio And Video**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Responsive Images (`srcset` & `sizes`)
        - Art Direction (`<picture>`)
        - Audio & Video Elements
    4. Architecture & Diagram Visualizations
        - Media Selection Pipeline
    5. Code & Hardware Implementation
        - Comprehensive Media Dashboard (`media_dashboard.html`)
    6. Enterprise Real-World Applications
        - AVIF & WebP Next-Gen Image Compression
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `<img srcset>` and the `<picture>` tag?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
15. **Embedded External Content**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Inline Frames (`<iframe>`)
        - Iframe Security Sandboxing (`sandbox` & `allow`)
    4. Architecture & Diagram Visualizations
        - Iframe Sandboxing Boundary
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
        - Embedded Grafana & OpenStreetMap Widgets
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does an empty `sandbox=""` attribute do on an iframe?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
16. **Vector Graphics And Html5 Canvas**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SVG vs Canvas Comparison Matrix
        - SVG Primitives (`<svg>`)
        - HTML5 Canvas 2D API (`<canvas>`)
    4. Architecture & Diagram Visualizations
        - SVG (DOM Retained) vs Canvas (Pixel Immediate)
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main architectural difference between SVG and Canvas?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
17. **Web Storage And Indexeddb**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Client Storage Matrix
        - LocalStorage & SessionStorage API
        - Storage Event Cross-Tab Sync
        - IndexedDB Architecture
    4. Architecture & Diagram Visualizations
        - IndexedDB Transaction Architecture
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is IndexedDB preferred over LocalStorage for offline-first web apps?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
18. **Geolocation And Device Apis**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Geolocation API
        - Position & Error Objects
    4. Architecture & Diagram Visualizations
        - Geolocation Permission Loop
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does Geolocation require HTTPS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
19. **Html5 Drag And Drop Api**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Drag and Drop Lifecycle
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `event.preventDefault()` required in the `dragover` handler?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
20. **Web Workers And Multithreading**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Single-Threaded JS & Web Workers Solution
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Main Application Thread (`app.js`)
        - Background Worker Script (`worker.js`)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Can a Web Worker access `localStorage` or DOM elements directly?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
21. **Shadow Dom And Custom Elements**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Web Components Suite
        - Custom Element Lifecycle Callbacks
        - Shadow DOM Encapsulation
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main purpose of the Shadow DOM in Web Components?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
22. **Web Content Accessibility Guidelines**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The POUR Principles (WCAG 2.1 / 2.2)
        - Conformance Levels
        - Color Contrast Requirements (Level AA)
        - Skip Navigation Links
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the four WCAG POUR principles?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
23. **Search Engine Optimization And Microdata**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - JSON-LD vs Microdata
        - JSON-LD Implementation Example
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is JSON-LD preferred over Microdata for SEO?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
24. **Performance Optimization And Best Practices**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Resource Hints Summary
        - Native Lazy Loading (`loading="lazy"`)
        - Obsolete & Deprecated HTML Tags
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `preload` and `prefetch`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
25. **Css Syntax And Inclusion Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Syntax Anatomy
        - Inclusion Methods Comparison
        - CSS At-Rules (`@`)
    4. Architecture & Diagram Visualizations
        - External CSS Loading vs `@import` Performance Waterfall
    5. Code & Hardware Implementation
        - External Stylesheet Architecture
    6. Enterprise Real-World Applications
        - Avoiding HTTP Request Waterfalls
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the performance disadvantages of using `@import` inside CSS files?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
26. **Comprehensive Selector Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Attribute Selectors
        - Combinator Systems
        - Pseudo-Classes & Modern `:has()` Parent Selector
        - Pseudo-Elements (`::before` & `::after`)
    4. Architecture & Diagram Visualizations
        - Combinator Target Matching Tree
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `:nth-child()` and `:nth-of-type()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
27. **Cascade Specificity And Inheritance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Cascade Algorithm
        - Specificity Calculation Vector Matrix `(A, B, C, D)`
        - Cascade Layers (`@layer`) Architecture
    4. Architecture & Diagram Visualizations
        - Cascade Layer Precedence Hierarchy
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do `@layer` declarations alter standard specificity calculations?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
28. **The Css Box Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 4 Box Model Layers
        - `content-box` vs `border-box`
        - Margin Collapsing Mechanics
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `box-sizing: border-box` preferred over `content-box`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
29. **Display Property And Visual Formatting Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Block Formatting Context (BFC) Triggers
        - `display: none` vs `visibility: hidden` vs `opacity: 0`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the modern standard property for creating a Block Formatting Context?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
30. **Positioning Systems And Stacking Contexts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Position Modes Matrix
        - Stacking Contexts & $Z$-Index Rules
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does a child with `z-index: 9999` fail to render above an element with `z-index: 2`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
31. **Sizing Units And Intrinsic Sizing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unit Categories Matrix
        - Intrinsic Sizing Keywords
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the technical difference between `1rem` and `1em`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
32. **Flexible Box Layout Flexbox**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Flexbox Axes System
        - Main Axis vs Cross Axis Alignment
        - Flex Item Sizing (`flex: grow shrink basis`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `flex: 1` expand to in CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
33. **Css Grid Layout System**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - 2D Grid vs 1D Flexbox
        - Fractional Unit (`fr`) & `minmax()`
        - Named Grid Areas (`grid-template-areas`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `auto-fill` and `auto-fit` in CSS Grid?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
34. **Advanced Typography And Web Fonts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `@font-face` Syntax & WOFF2
        - Micro-Typography & Line Clamping
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `font-display: swap` in CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
35. **Modern Css Color Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Evolution of CSS Color Functions
        - The `color-mix()` Function
        - The `currentcolor` Keyword
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What makes `oklch()` superior to traditional `hsl()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
36. **Backgrounds Borders And Shadows**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Gradient Types
        - Box Shadow Layering (`box-shadow`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between blur-radius and spread-radius in a `box-shadow` property?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
37. **Visual Effects Filters And Blending**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Glassmorphism & `backdrop-filter`
        - Clipping Paths (`clip-path`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does `filter: blur()` differ from `backdrop-filter: blur()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
38. **Css Transitions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Transition Properties & Shorthand
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you avoid animating `height` or `margin` properties?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
39. **2D And 3D Transformations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - 2D vs 3D Transform Functions
        - 3D Card Flipping Setup
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `transform-style: preserve-3d` do?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
40. **Keyframe Animations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `@keyframes` Syntax & Shorthand
        - `animation-fill-mode`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `animation-fill-mode: forwards` do?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
41. **Responsive Architecture Principles**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Mobile-First vs Desktop-First
        - The Viewport Meta Tag
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is Mobile-First CSS architecture preferred over Desktop-First?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
42. **Media Queries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Modern Range Syntax (Level 4)
        - User Preference Media Features
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is `prefers-reduced-motion` and why is it important for accessibility?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
43. **Container Queries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Media Queries vs Container Queries
        - Setting Up Container Context
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main problem Container Queries solve that Media Queries could not?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
44. **Fluid Layout Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Math Functions (`calc`, `min`, `max`, `clamp`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the three parameters passed to `clamp()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
45. **Css Custom Properties Variables**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Syntax & Scoping
        - Typed Custom Properties (`@property`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do CSS Custom Properties differ from Sass/SCSS variables?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
46. **Modern Css Architecture And Methodologies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - BEM Naming Convention Syntax
        - ITCSS (Inverted Triangle CSS) Layers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does BEM stand for and what are its advantages?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
47. **Native Css Nesting And Logical Properties**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Native CSS Nesting (`&`)
        - Physical vs Logical Properties Matrix
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the benefit of Logical Properties over Physical Properties in modern CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
48. **Utility First Css And Tailwind Introduction**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Semantic CSS vs Utility-First CSS
        - Component Extraction (`@apply`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main benefit of Utility-First CSS over traditional semantic CSS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
49. **Component Frameworks And Component Styling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CSS Modules Hashing Mechanism
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do CSS Modules prevent global CSS class name collisions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
50. **Production Css Performance Purging And Optimization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Critical CSS Extraction
        - GPU Layer Promotion (`will-change`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Critical CSS and why does inlining it improve performance?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
51. **History Evolution And Ecmascript Standards**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - TC39 Proposal Process
        - Transpilers vs Polyfills
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Babel Configuration Setup (`babel.config.json`)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the technical difference between a Babel transpiler and a polyfill?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
52. **Javascript Engine Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The V8 Engine Execution Pipeline
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are Ignition and TurboFan in the Google Chrome V8 engine?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
53. **Execution Context Call Stack And Memory Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Execution Context Lifecycle
        - Mark-and-Sweep Garbage Collection
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Mark-and-Sweep Garbage Collection in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
54. **Variable Declarations And Scoping**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `var` vs `let` vs `const`
        - The Temporal Dead Zone (TDZ)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the Temporal Dead Zone (TDZ) in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
55. **Primitive And Reference Data Types**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Primitives vs Reference Types
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the 7 primitive data types in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
56. **Type Coercion And Comparison Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 8 Falsy Values in JavaScript
        - Abstract (`==`) vs Strict (`===`) Equality
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the 8 falsy values in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
57. **Comprehensive Operator Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `||` vs `??` (Nullish Coalescing)
        - Optional Chaining (`?.`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the Nullish Coalescing Operator (`??`) differ from the Logical OR Operator (`||`)?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
58. **Vectors Matrices And Vector Spaces**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Vectors & The Dot Product
        - Matrix Multiplication Geometry
        - Linear Independence & Span
    4. Architecture & Diagram Visualizations
        - Matrix Multiplication Inner Dimension Match
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the geometric interpretation of the dot product between two normalized vectors?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
59. **Probability Fundamentals And Axioms**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Kolmogorov Probability Axioms
        - Bayes' Theorem
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Prior Probability and Posterior Probability in Bayes' Theorem?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
60. **Parametric Hypothesis Testing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Error Matrix & Statistical Power
        - Two-Sample Independent $t$-Test
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a $p$-value in hypothesis testing?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
61. **Non Parametric Statistical Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Parametric vs Non-Parametric Decision Matrix
        - Bootstrapping Resampling
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Bootstrapping and why is it useful in Data Science?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
62. **Python 312 Structural Pattern Matching**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `match/case` vs Legacy `if-elif-else`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What makes structural pattern matching different from C/Java `switch` statements?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
63. **Static Type Hinting And Mypy Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Gradual Typing in Python
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Do Python type hints affect runtime execution speed?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
64. **Asyncio Event Loop And Async Await**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Synchronous vs Asynchronous Execution
        - Python 3.11+ `TaskGroup` Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Is Asyncio multi-threaded?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
65. **Modern Python Packaging Pyproject And Uv**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Legacy `setup.py` vs Modern `pyproject.toml`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Modern `pyproject.toml` Manifest Specification
        - High-Speed `uv` CLI Commands
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is `pyproject.toml` and why is it preferred over `requirements.txt`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
66. **Java21 Record Classes And Dto Patterns**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Eliminating DTO Boilerplate
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Can a Java Record Class extend another class or be extended?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
67. **Java21 Sealed Classes And Interfaces**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Controlled Class Hierarchies
        - Subclass Modifiers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does exhaustive pattern matching on a sealed class eliminate the need for a `default` case in switch expressions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
68. **Java21 Virtual Threads Project Loom**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Platform Threads vs Virtual Threads
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Thread Pinning in Java 21 Virtual Threads and how do you avoid it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
69. **Java21 Sequenced Collections**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Missing Abstraction in Legacy Java Collections
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What problem do Sequenced Collections solve in Java 21?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
70. **Matrix Inversion Determinants And Systems**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Determinants & Singular Matrices
        - Solving $A\mathbf{x} = \mathbf{b}$
        - Condition Number ($\kappa$)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you avoid explicitly computing $A^{-1}$ to solve $A\mathbf{x} = \mathbf{b}$?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
71. **Eigenvalues Eigenvectors And Decompositions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Eigenvalues & Eigenvectors
        - Singular Value Decomposition (SVD)
        - PCA & Covariance Matrix Connection
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the relationship between SVD and PCA?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
72. **Multivariable Calculus And Gradient Vectors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Gradient Vector ($\nabla f$)
        - The Hessian Matrix ($H$)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does the Gradient Vector $\nabla f$ represent geometrically?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
73. **Discrete And Continuous Probability Distributions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - PMF, PDF, & CDF
        - Gaussian (Normal) Distribution $\mathcal{N}(\mu, \sigma^2)$
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between a PMF and a PDF?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
74. **Joint Marginal And Conditional Distributions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Joint & Marginal Distributions
        - Covariance & Pearson Correlation
        - The Central Limit Theorem (CLT)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does the Central Limit Theorem state and why is it crucial for statistics?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
75. **Selenium4 Relative Locators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Spatial Locating in Selenium 4
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do Relative Locators in Selenium 4 calculate element positions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
76. **Estimation And Confidence Intervals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Point Estimation & MLE
        - Confidence Intervals (CI)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the correct interpretation of a 95% Confidence Interval?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
77. **Mysql8 Analytical Window Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `GROUP BY` vs Window Functions (`OVER`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `RANK()` and `DENSE_RANK()` in SQL?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
78. **Modern C23 Features Constexpr Typeof Auto**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The C23 Standard Evolution
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does `constexpr` in C23 improve performance over standard `const` variables?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
79. **Anova And Chi Square Tests**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - One-Way ANOVA ($F$-Statistic)
        - Chi-Square Test of Independence ($\chi^2$)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why use ANOVA instead of multiple individual $t$-tests when comparing 4 groups?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
80. **Cpp20 Smart Pointers And Memory Safety**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - RAII & Smart Pointers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `std::unique_ptr` and `std::shared_ptr`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
81. **Conditional Logic And Guard Clauses**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Guard Clauses vs Nested Arrow Code
        - Object Lookup Tables
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Guard Clause and why is it preferred over nested `if-else` blocks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
82. **Loops And Iteration Constructs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `for...in` vs `for...of`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the technical difference between `for...in` and `for...of` in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
83. **Iteration Protocols Iterators And Generators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Iterable & Iterator Protocols
        - Generator Functions (`function*`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does a Generator function differ from a regular function in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
84. **Function Declarations Expressions And Arrow Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Declarations vs Expressions vs Arrow Functions
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the `this` keyword behave differently in Arrow Functions compared to Regular Functions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
85. **Parameters Arguments And Return Values**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Rest Parameters (`...args`) vs `arguments` Object
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main advantage of Rest Parameters (`...args`) over the `arguments` object?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
86. **Scope Chain And Closures**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Lexical Scoping & Scope Chain
        - What is a Closure?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a JavaScript Closure and how does it retain memory?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
87. **Functional Concepts And Higher Order Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Pure Functions vs Side Effects
        - Currying
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Currying in Functional JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
88. **Object Literals Descriptors And Immutability**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Object Immutability Levels
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `Object.freeze()` and `Object.seal()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
89. **Dense Sparse Arrays And Higher Order Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Mutating vs Non-Mutating Methods
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does `.reduce()` work in JavaScript and what is the role of the initial value parameter?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
90. **Destructuring Assignment And Spread Rest Operators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unpacking Data Structures
        - Spread (`...`) for Immutable Merging
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do you rename a variable during Object Destructuring in ES6?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
91. **Keyed Collections Map Set Weakmap Weakset**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Plain Object vs `Map`
        - `WeakMap` & `WeakSet` Garbage Collection
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why can you not iterate over a `WeakMap` or check its size?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
92. **Asynchronous Execution Callbacks Event Queue**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Event Loop & Task Queue Priority
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between the Macrotask Queue and Microtask Queue in the JavaScript Event Loop?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
93. **Es6 Promises Architecture States And Chaining**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Promise States & Immutability
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens if a `.then()` callback returns a plain scalar value versus another Promise?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
94. **Async Await Syntactic Sugar And Async Iteration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Async/Await as Syntactic Sugar
        - Asynchronous Iteration (`for await...of`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens when the `await` keyword is executed in an `async` function?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
95. **Promise Combinators All Allsettled Race Any**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Promise Combinators Comparison Matrix
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main difference between `Promise.all()` and `Promise.allSettled()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
96. **Prototypes Prototype Chain And Inheritance**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Prototypal Inheritance vs Class-Based Inheritance
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens when a property is accessed on a JavaScript object that does not exist on the instance itself?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
97. **Es6 Class Syntax And Constructors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Classes as Syntactic Sugar
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Are ES6 classes true classes like in Java or C++?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
98. **Inheritance Method Overriding And Super**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Subclassing & Mandatory `super()`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is calling `super()` mandatory in a subclass constructor before accessing `this`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
99. **Private Fields Getters Setters Static Members**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Hard Encapsulation (`#privateField`)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do modern `#` private fields in JavaScript differ from the legacy `_` prefix convention?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
100. **Dom Tree Navigation And Selection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `querySelectorAll` (NodeList) vs `getElementsByClassName` (HTMLCollection)
        - Upward Traversal with `.closest()`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main difference between a live `HTMLCollection` and a static `NodeList`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
101. **Dynamic Element Creation And Modification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `appendChild()` vs `append()`
        - HTML5 `dataset` API
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the HTML5 `dataset` API in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
102. **Event Handling Propagation Bubbling Capturing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 3 Event Propagation Phases
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `event.target` and `event.currentTarget`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
103. **Event Delegation And Custom Events**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Event Delegation Architecture
        - Custom Events
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the primary benefits of using the Event Delegation Pattern?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
104. **Fetch Api And Http Network Requests**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The `fetch()` HTTP Status Code Trap
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does `fetch()` not reject when a server returns a 404 or 500 error code?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
105. **Web Storage Cookies Localstorage Sessionstorage**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Client Storage Comparison
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main security risk of storing authentication tokens in LocalStorage compared to HttpOnly Cookies?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
106. **Client Side Storage With Indexeddb**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why IndexedDB Over LocalStorage?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does IndexedDB differ from LocalStorage?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
107. **Websockets And Realtime Communication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - HTTP Polling vs WebSockets
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Exponential Backoff and why is it essential for WebSocket reconnection strategies?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
108. **Es6 Modules Export And Import Syntax**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - CommonJS (`require`) vs ES Modules (`import`)
        - Named vs Default Exports
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `mathUtils.js` (Module)
        - File 2: `main.js` (Consumer)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main structural advantage of ES Modules over CommonJS `require()`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
109. **Dynamic Imports And Toplevel Await**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Static Imports vs Dynamic `import()`
        - Top-Level Await
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Code Splitting and how do Dynamic Imports facilitate it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
110. **Modern Build Tooling Bundlers Tree Shaking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Legacy Bundlers (Webpack) vs Modern Native ESM (Vite)
        - Tree Shaking Mechanics
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Initializing a Lightning-Fast Vite Project
        - Production Build & Source Map Inspection
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Tree Shaking in modern JavaScript build tools and how does it work?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
111. **Critical Rendering Path And Dom Reflows**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Critical Rendering Path
        - Reflow vs Repaint vs Layout Thrashing
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Layout Thrashing in JavaScript and how do you prevent it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
112. **Core Web Vitals And Performance Monitoring**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Google Core Web Vitals Metrics
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Interaction to Next Paint (INP) and how does it differ from FID?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
113. **Memory Management And Leak Prevention**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Mark-and-Sweep Garbage Collection
        - The 4 Common Memory Leak Patterns
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Detached DOM Node memory leak in JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
114. **Web Security Xss Csrf Csp Mitigation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - XSS vs CSRF Vulnerability Matrix
        - Content Security Policy (CSP)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Content Security Policy (CSP) and how does it prevent XSS attacks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
115. **Proxy And Reflect Api Metaprogramming**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is Meta-Programming?
        - Proxy Traps & Reflect API
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you use `Reflect` methods inside Proxy handler traps instead of accessing the target directly?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
116. **Web Workers And Multithreaded Javascript**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Single-Threaded Main Loop vs Worker Threads
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `worker.js` (Background Thread)
        - File 2: `main.js` (UI Thread)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What capabilities and Web APIs are accessible inside a Web Worker?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
117. **Service Workers And Offline Pwa Caching**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Service Worker Proxy Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `sw.js` (Service Worker Script)
        - File 2: `app.js` (Register Service Worker)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the Stale-While-Revalidate caching strategy work?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
118. **Javascript Unit Testing With Vitest**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The AAA Unit Testing Pattern
        - `toBe` vs `toEqual`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Target Module: `math.js`
        - Vitest Test Suite: `math.test.js`
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `toBe` and `toEqual` in Vitest/Jest?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
119. **E2E Testing With Playwright**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unit Testing vs End-to-End (E2E) Testing
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Playwright Test Suite: `dashboard.spec.js`
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is Playwright preferred over older Selenium or Puppeteer testing frameworks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
120. **Javascript Design Patterns**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Design Patterns Categories
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main difference between the Observer Pattern and the Publisher-Subscriber (PubSub) Pattern?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
121. **Internationalization Intl Api**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Native ECMAScript `Intl` API
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the performance advantages of using the native `Intl` API over external libraries like Moment.js?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
122. **Web Components And Shadow Dom**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The 4 Web Components Technologies
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Usage in HTML:
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why must Custom Element tag names contain a hyphen (`-`)?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
123. **Webassembly Integration Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is WebAssembly (Wasm)?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Is WebAssembly intended to replace JavaScript?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
124. **Advanced Debugging Chrome Devtools**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Advanced Breakpoint Types
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Logpoint in Chrome DevTools and how does it differ from a standard Breakpoint?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
125. **Capstone Realtime Iot Dashboard**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Capstone Enterprise Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Reactive State Store (`store.js`)
        - Capstone Dashboard Application (`app.js`)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does this Vanilla JavaScript Capstone architecture achieve high performance without a frontend framework like React?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
126. **Wsgi Architecture And Flask Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is WSGI (PEP 3333)?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is WSGI in Python web development and why is `Flask(__name__)` required?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
127. **Flask Application Factory Pattern**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why the Application Factory Pattern?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `config.py` (Environment Configurations)
        - File 2: `app/__init__.py` (Application Factory)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the Application Factory Pattern in Flask and why is it recommended for production applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
128. **Flask Routing And Url Converters**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Built-in URL Converters
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you use `url_for()` instead of hardcoding URL strings in Flask?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
129. **Flask Request Response Objects**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Flask `request` Context Local
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Context Local in Flask and how does the `request` object work behind the scenes?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
130. **Jinja2 Syntax Control Flow And Macros**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Jinja2 Delimiter Syntax
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `templates/macros/card.html` (Jinja2 Reusable Macro)
        - File 2: `templates/dashboard.html` (Main Page)
        - File 3: `app.py` (Python View Function)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does Jinja2 prevent Cross-Site Scripting (XSS) attacks when rendering dynamic variables?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
131. **Flask Contexts Application And Request**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Application Context vs Request Context
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between the Application Context and Request Context in Flask?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
132. **Flask G Object And Request Scoped State**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is the `g` Object?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `g` and `session` in Flask?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
133. **Flask Wtf Forms And Fields**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Processing Manual HTML Forms vs Flask-WTF
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `forms.py` (FlaskForm Class Definition)
        - File 2: `app.py` (Flask View Function)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `form.validate_on_submit()` do in Flask-WTF?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
134. **Form Validation And Csrf Protection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Custom In-Class Field Validation
        - CSRF Protection Mechanism
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `forms.py` (Form with Custom & Standard Validators)
        - File 2: `templates/register.html` (Rendering Inline Validation Errors)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do you write a custom field validator in Flask-WTF?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
135. **Flask Sqlalchemy Extension Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Object-Relational Mapping (ORM)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `extensions.py` (Unbound Extension Instance)
        - File 2: `config.py`
        - File 3: `app/__init__.py` (Application Factory Integration)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you initialize Flask-SQLAlchemy using `db = SQLAlchemy()` in an `extensions.py` module rather than `db = SQLAlchemy(app)`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
136. **Sqlalchemy Models Fields And Relationships**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SQLAlchemy Model Mapping
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `models.py` (SQLAlchemy Relational Schema)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `backref` and `back_populates` in SQLAlchemy relationships?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
137. **Sqlalchemy Crud Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unit of Work Transaction Management
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `db.session.rollback()` in Flask-SQLAlchemy?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
138. **Schema Migrations With Flask Migrate**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why `db.create_all()` Fails in Production
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `extensions.py`
        - File 2: `app/__init__.py` (Factory Integration)
        - File 3: Command Line Execution Sequence
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does Flask-Migrate detect changes made to SQLAlchemy models when generating migration scripts?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
139. **User Authentication With Flask Login**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Flask-Login Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `models.py` (User Model with UserMixin)
        - File 2: `app.py` (Flask-Login Initialization & Auth Routes)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `@login_manager.user_loader` in Flask-Login?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
140. **Password Hashing And Cookie Security**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - One-Way Password Hashing & Salting
        - Flask Session Cookie Security Configuration
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `security_demo.py` (Password Hashing & Cookie Security Config)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is storing plain MD5 or SHA-256 hashes of passwords insecure, and how does Werkzeug address this?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
141. **Flask Blueprint Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is a Flask Blueprint?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `app/api/routes.py` (Blueprint Module)
        - File 2: `app/__init__.py` (Registering Blueprints in Application Factory)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Flask Blueprint and how does it improve code architecture?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
142. **Restful Api Principles And Resource Routing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - REST Architectural Constraints
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is idempotency in RESTful APIs and which HTTP verbs are idempotent?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
143. **Api Serialization With Flask Marshmallow**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Serialization vs Deserialization
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `schemas.py` (Flask-Marshmallow Schemas)
        - File 2: `routes.py` (Using Schemas in API Views)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the primary role of Marshmallow schemas in a Flask REST API?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
144. **Jwt Authentication With Flask Jwt Extended**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - JSON Web Token (JWT) Structure
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main structural difference between session-based authentication and JWT authentication?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
145. **Application Caching With Flask Caching**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why Backend Caching?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `@cache.cached()` and `@cache.memoize()` in Flask-Caching?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
146. **Asynchronous Background Tasks With Celery**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why Asynchronous Background Tasks?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `celery_app.py` (Celery Integration Helper)
        - File 2: `tasks.py` (Celery Tasks)
        - File 3: `app.py` (Dispatching Tasks & Checking Status)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is Celery used with Flask instead of Python's built-in `threading` module?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
147. **Email Delivery With Flask Mail**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SMTP Protocol & Synchronous vs Async Delivery
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is it crucial to send emails asynchronously in web applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
148. **Custom Error Pages And Handlers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Exception Handling Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `@errorhandler` and `@app_errorhandler` on a Flask Blueprint?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
149. **Application Logging And Sentry**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Production Logging Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `RotatingFileHandler` critical for production Python applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
150. **Automated Testing With Pytest**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Flask `test_client()` Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `conftest.py` (Pytest Shared Fixtures)
        - File 2: `test_api.py` (Pytest Test Cases)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does Flask's `app.test_client()` work and why is it preferred over HTTP requests library like `requests` during unit testing?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
151. **Production Deployment Gunicorn Nginx Docker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Enterprise Production Deployment Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `wsgi.py` (Production Entrypoint)
        - File 2: `Dockerfile` (Production Multi-Stage Container)
        - File 3: `docker-compose.yml` (Multi-Container Orchestration)
        - File 4: `nginx.conf` (Nginx Reverse Proxy Configuration)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why must Flask's built-in development server never be used in production environments, and what roles do Gunicorn and Nginx play?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
152. **Asgi Architecture Uvicorn And Fastapi Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - WSGI vs ASGI Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Running with Uvicorn Server:
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens if you call a synchronous blocking function inside an `async def` endpoint in FastAPI?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
153. **Fastapi App Instantiation Routing And Openapi**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Zero-Configuration Automatic OpenAPI Generation
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does FastAPI generate Swagger UI documentation automatically without third-party plugins?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
154. **Path And Query Parameters**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Parameter Parsing & Automatic Type Conversion
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does FastAPI differentiate between a Path Parameter and a Query Parameter in a route function?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
155. **Pydantic V2 Models And Schema Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Pydantic v2 Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the key improvements of Pydantic v2 over Pydantic v1 in FastAPI?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
156. **Dependency Injection Architecture And Depends**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is Dependency Injection?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the main benefits of FastAPI's Dependency Injection system over traditional middleware?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
157. **Sub Dependencies Security And Yield Cleanups**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Yield Dependencies & Context Cleanup
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Mocking Dependencies in Unit Tests:
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do Yield Dependencies work in FastAPI and how do they prevent resource leaks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
158. **Sqlalchemy 20 Async Engine And Asyncpg**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Synchronous vs Asynchronous Database Drivers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `database.py` (SQLAlchemy 2.0 Async Engine & Dependency)
        - File 2: `main.py` (Using AsyncSession in Route)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `asyncpg` significantly faster than `psycopg2` when used with FastAPI?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
159. **Async Crud Operations And Asyncsession**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SQLAlchemy 2.0 Async Query Style
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `models.py` (Async SQLAlchemy Models)
        - File 2: `main.py` (Async CRUD Routes)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is lazy loading problematic in asynchronous SQLAlchemy and how does `selectinload()` solve it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
160. **Oauth2 Password Bearer And Hashing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - OAuth2 Password Bearer Flow
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `OAuth2PasswordBearer` do under the hood in FastAPI?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
161. **Jwt Authentication And Current User**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The `get_current_user` Dependency Pipeline
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does FastAPI implement Role-Based Access Control (RBAC) cleanly using Dependency Injection?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
162. **Apirouter Architecture And Prefixes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is an APIRouter?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `routers/devices.py` (APIRouter Module)
        - File 2: `main.py` (Main FastAPI App Registering Router)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does `APIRouter` in FastAPI differ from Flask's `Blueprint`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
163. **Modular Directory Structure And Big Applications**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Enterprise Production Directory Layout
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `src/app/core/config.py` (Pydantic-Settings Configuration)
        - File 2: `src/app/main.py` (Global Exception Handler & Main App)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `pydantic-settings` preferred over `os.environ.get()` in FastAPI production codebases?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
164. **Asynchronous Middleware And Cors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is FastAPI Middleware?
        - Cross-Origin Resource Sharing (CORS)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a CORS preflight request and how does FastAPI handle it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
165. **Request Timing Headers And Performance Logging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - High-Precision Latency Tracking
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `time.perf_counter()` preferred over `time.time()` for measuring code latency?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
166. **Fastapi Background Tasks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What are FastAPI BackgroundTasks?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: When should you use FastAPI `BackgroundTasks` versus an external task queue like Celery?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
167. **Lifespan Event Handlers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What are Lifespan Events?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why did FastAPI deprecate `@app.on_event("startup")` in favor of the `lifespan` context manager?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
168. **Websockets Protocol And Endpoint Handling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - HTTP Polling vs Full-Duplex WebSockets
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `await websocket.accept()` in a FastAPI WebSocket endpoint?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
169. **Realtime Connection Manager And Broadcasting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Connection Manager Pattern
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do you scale WebSocket broadcasting across multiple Uvicorn worker processes or servers?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
170. **Async Testing With Pytest And Httpx**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why `httpx.AsyncClient` over Starlette `TestClient`?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `conftest.py` (Pytest Async Fixtures)
        - File 2: `test_main.py` (Async Test Cases)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `httpx.AsyncClient` preferred over `TestClient` when testing async FastAPI applications with Pytest?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
171. **Production Deployment Gunicorn Uvicorn Docker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Production Process Management: Gunicorn + Uvicorn
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `gunicorn_conf.py` (Gunicorn Configuration)
        - File 2: `Dockerfile` (Production Container Definition)
        - File 3: `docker-compose.yml` (Multi-Container Deployment)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why do we use Gunicorn together with Uvicorn in production rather than running Uvicorn alone?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
172. **Esp32 Architecture And Pinout**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - ESP32 System-on-Chip (SoC) Architecture
        - Critical GPIO Pin Classification
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are ESP32 Strapping Pins and why must engineers exercise caution when connecting external hardware components to them?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
173. **Platformio Espidf Toolchain Setup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Embedded Development Frameworks
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `platformio.ini` (PlatformIO Configuration File)
        - File: `src/main.cpp` (Embedded Entrypoint)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is PlatformIO preferred over Arduino IDE for professional embedded engineering?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
174. **Gpio Digital Io And Interrupts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Polling vs Hardware Interrupts
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why must ESP32 Interrupt Service Routine (ISR) functions be declared with the `IRAM_ATTR` attribute?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
175. **Adc Dac And Pwm Timer Control**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - 12-Bit Analog-to-Digital Conversion (ADC)
        - Hardware PWM via LEDC Peripheral
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should embedded engineers avoid connecting analog sensors to ADC2 pins on the ESP32 in connected IoT applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
176. **I2C Spi And Uart Communication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Serial Protocol Comparison Matrix
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `main.cpp` (I2C Bus Address Scanner & Dual Hardware UART)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Compare I2C and SPI protocols. When would you choose SPI over I2C in an embedded system design?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
177. **Freertos Task Creation And Core Pinning**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why FreeRTOS on ESP32?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `xTaskCreate()` and `xTaskCreatePinnedToCore()` in ESP32 FreeRTOS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
178. **Freertos Task Priorities Delays And Stack**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Pre-emptive Priority Scheduling
        - `vTaskDelay()` vs `vTaskDelayUntil()`
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `vTaskDelay()` and `vTaskDelayUntil()` in FreeRTOS?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
179. **Freertos Queues And Inter Task Messaging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why FreeRTOS Queues?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do FreeRTOS Queues achieve thread safety when sharing data between tasks running on different CPU cores?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
180. **Freertos Semaphores Mutexes And Locks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Binary Semaphores vs Mutexes
        - What is Priority Inversion?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Priority Inversion and how do FreeRTOS Mutexes resolve it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
181. **Wifi Station And Access Point Modes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - ESP32 Wi-Fi Operating Modes
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Station (STA) Mode and Access Point (AP) Mode on the ESP32?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
182. **Non Blocking Wifi Reconnect And Events**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Asynchronous System Wi-Fi Events
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is Exponential Backoff and why is it essential for IoT Wi-Fi reconnect logic?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
183. **Http Rest Client Requests**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Embedded HTTP Client Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `http.end()` mandatory after executing an HTTP request with `HTTPClient` on the ESP32?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
184. **Mqtt Protocol And Pubsubclient**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is MQTT?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Compare MQTT and HTTP protocols for resource-constrained IoT devices.
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
185. **Esp32 Websocket Client Streaming**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why WebSockets for Microcontroller Telemetry?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: When should an embedded engineer choose WebSockets over MQTT for an IoT system architecture?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
186. **Deep Sleep Modes And Rtc Memory**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Power Consumption Modes Comparison
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens to standard C++ global variables versus `RTC_DATA_ATTR` variables when the ESP32 enters Deep Sleep?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
187. **Deep Sleep Wakeup Sources**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Deep Sleep Wake-Up Sources Matrix
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between Ext0 and Ext1 wake-up sources on the ESP32?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
188. **Over The Air Ota Firmware Updates**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Dual-Bank OTA Partition Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does the ESP32 dual-bank partition table prevent device bricking during Over-The-Air (OTA) updates?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
189. **Secure Boot Flash Encryption Partitions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Custom Partition Tables
        - Hardware Security Primitives
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `partitions_custom.csv` (Custom 4MB Dual-OTA Partition Table)
        - File: `platformio.ini` (Configuring Custom Partition Table)
        - File: `main.cpp` (Querying Partition & Security Status)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Explain how Secure Boot V2 and Flash Encryption combine to secure ESP32 hardware in the field.
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
190. **Spiffs Littlefs And Static File Serving**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SPIFFS vs LittleFS
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `data/index.html` (Static Web Asset in PlatformIO `data/` Directory)
        - File: `src/main.cpp` (Mounting LittleFS & File I/O)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is LittleFS preferred over SPIFFS for modern ESP32 embedded applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
191. **Espasyncwebserver And Rest Control**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Synchronous vs Asynchronous Web Servers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `ESPAsyncWebServer` superior to the standard synchronous `WebServer.h` library for ESP32 applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
192. **Fullstack Iot System Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - End-to-End Full-Stack IoT Data Pipeline
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `backend_bridge.py` (FastAPI + MQTT Ingestion Bridge)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is an MQTT message broker placed between embedded ESP32 devices and backend FastAPI microservices in full-stack IoT architectures?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
193. **Capstone Production Iot Gateway**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Capstone Architecture Blueprint
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - ESP32 Production FreeRTOS Firmware (`src/main.cpp`)
        - FastAPI Ingestion & WebSockets Backend (`server.py`)
    6. Guided Step-by-Step Hands-On Exercise
    7. Industry Interview Q&A
        - Q1: How does this capstone architecture ensure high reliability and zero telemetry loss across network drops?
    8. Self-Assessment Quiz
    9. Summary & Cheat Sheet
194. **Numpy Core Architecture And Ndarray**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Python Lists vs NumPy `ndarray`
        - Array Strides
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why are NumPy `ndarray` operations significantly faster than standard Python list comprehensions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
195. **Vectorization Slicing And Broadcasting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - NumPy Broadcasting Rules
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the two conditions under which two array dimensions are compatible for NumPy broadcasting?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
196. **Pandas Dataframes Series And Ingestion**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Pandas Data Structures Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why does converting string columns with low cardinality to the `category` dtype in Pandas significantly reduce memory usage?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
197. **Pandas Indexing Filtering And Imputation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - `loc` vs `iloc` Indexing Mechanics
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the crucial difference between `df.loc[0:2]` and `df.iloc[0:2]` in Pandas?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
198. **Pandas Groupby Pivoting And Merging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Split-Apply-Combine Pattern
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `transform()` and `agg()` when performing a `groupby()` in Pandas?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.1.2. Module 2 — Remote Collaboration

1. **Remote Repositories & Origin Config**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Visual Architecture Diagram
        - What is a Remote?
        - Git vs. Hosting Platforms
        - Clone vs. Fork
        - origin vs. upstream
        - Remote-Tracking Branches
        - HTTPS vs. SSH
    3. Practical Code Examples
        - Remote Command Cheat Sheet
        - Example A: Managing Multiple Remotes in Enterprise Environment
        - Example B: Renaming and Inspecting Remotes
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - E2E Remote Association Workflow
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
2. **Syncing Data: Fetch, Pull & Push**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Fetch vs. Pull Architecture Diagram
        - Fetch vs. Pull Comparison
        - git pull: Merge vs. Rebase
        - Ahead and Behind Tracking States
    3. Practical Code Examples
        - Syncing Commands Cheat Sheet
        - Example A: Pulling with Rebase
        - Example B: Pushing and linking branch
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Rejected Push
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
3. **Forking & Upstream Workflows**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - The Forking Workflow Diagram
        - Fork vs. Clone vs. Branch
        - origin vs. upstream
        - Pull Requests (PR) vs. Merge Requests (MR)
        - Merge vs. Rebase in Workflows
    3. Practical Code Examples
        - Remote Fork Commands Cheat Sheet
        - Example A: Full Open-Source Contribution Workflow
        - Example B: Syncing your Local Fork
        - Example C: Rebasing feature branches
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - GitHub Feature Lifecycle Flow
    5. Workout Answers & Solutions
        - Pull Request Best Practices
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

#### 2.1.3. Module 3 — Branching & Merging

1. **Branching Basics & Conflict Resolution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Branch Visualization Diagrams
        - Merging Strategies (FF vs. 3-Way)
        - Why Merge Conflicts Occur
        - Tagging Releases (Lightweight vs. Annotated)
    3. Practical Code Examples
        - Branch Command Cheat Sheet
        - Merge Command Cheat Sheet
        - Example A: Resolving Conflicts with git status Checks
        - Example B: Tagging and Remote Operations
        - Example C: Realistic Feature Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Standard Branch Naming Conventions
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
2. **Merge Conflict Handling in Teams**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Conflict Visualization Diagram
        - Conflict Resolution Workflow
        - Merge vs. Rebase Conflicts
        - Conflict Markers Decoded
        - HEAD vs. Theirs Pointer Reference Map
        - Conflict Types
    3. Practical Code Examples
        - Conflict Commands Cheat Sheet
        - Example A: Managing conflict status
        - Example B: Visual merge tools setup
        - Example C: Practical Team Resolution Workflow
        - Advanced Tip: `git rerere`
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge: Resolving Worksheets
        - Conflict Prevention Workflow Diagram
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

#### 2.1.4. Module 4 — Troubleshooting

1. **Diagnostic & Troubleshooting Guide**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Common Git Troubleshooting Scenarios
        - Scenario 1: Detached HEAD State
        - Scenario 2: Recovering Lost Commits (Reflog)
        - Scenario 3: Committed on the Wrong Branch
        - Scenario 4: Stuck Merge or Rebase
        - Scenario 5: Force Push Recovery
    3. Practical Code Examples
        - Diagnostic Commands Cheat Sheet
        - Example A: Finding lost commits using `git fsck`
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Wrong branch commit
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

#### 2.1.5. Module 5 — Automation & Security

1. **Git Customization: Hooks & Aliases**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Git Hook Lifecycle Diagrams
        - Client-side vs. Server-side Hooks
        - Why Hooks Exist
        - Git Hook Trigger Reference
        - Modern SaaS Hosting Realities
    3. Practical Code Examples
        - Hook & Alias Cheat Sheet
        - Common Git Aliases
        - Example A: Enterprise Pre-commit Pipeline
        - Example B: Portable pre-commit hook (POSIX sh)
        - Example C: Robust commit-msg message parsing (Bash)
    4. Hands-on Workouts
        - MCQ
        - Hook Distribution Strategies
    5. Workout Answers & Solutions
        - Common Mistakes
        - Enterprise Best Practices
        - Key Takeaways
2. **Credential Management & Security**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - HTTPS vs. SSH Authentication
        - Credential Helpers
        - SSH Key Setup Overview
    3. Practical Code Examples
        - Credential Config Cheat Sheet
        - Example A: Setting Up SSH Authentication
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Token Expiration
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

#### 2.1.6. Module 6 — Advanced Workflows

1. **Rewriting History: Amend, Rebase & Squash**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - History Rewriting Diagram
        - Decision Guide
        - History Rewriting Command Comparisons
        - Visualizing Interactive Rebase & Squashing
        - reflog Recovery Mechanics
    3. Practical Code Examples
        - Interactive Rebase Command Reference
        - Example A: Interactive Rebase Setup
        - Example B: Safe Force-Pushing
        - Example C: Complete Cleanup Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Undoing an amend
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
2. **Workspace Helpers: Stash, Bisect & Worktree**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
        - Workspace Helper Decision Guide
    2. Part 1: Git Stash
        - Stash Workflow
        - Stash Internals
        - Stash Commands Cheat Sheet
        - Enterprise Scenario: Stashing
    3. Part 2: Git Bisect
        - Bisect Visualization
        - Automated Bisect
        - Bisect Commands Cheat Sheet
        - Enterprise Scenario: Bisecting
    4. Part 3: Git Worktree
        - Worktree Visualization
        - Worktree vs. Clone
        - Worktree Commands Cheat Sheet
        - Enterprise Scenario: Worktrees
    5. Hands-on Workouts
        - MCQ
        - Coding Challenge
    6. Workout Answers & Solutions
        - Common Mistakes
        - Enterprise Best Practices
        - Key Takeaways
3. **Cherry-picking & Backporting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Cherry-picking Visual Diagram
        - What is Backporting?
        - Cherry-pick vs. Merge vs. Rebase
    3. Practical Code Examples
        - Cherry-pick Command Cheat Sheet
        - Example A: Cherry-picking a Hotfix
        - Example B: Handling Cherry-pick Conflicts
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Hotfixing
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
4. **Tags & Release Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Tag Types Comparison
        - Semantic Versioning (SemVer)
        - Tags vs. Releases
    3. Practical Code Examples
        - Tag Command Cheat Sheet
        - Example A: Creating and Pushing an Annotated Release Tag
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Security verification
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
5. **Branching Strategies for Teams**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Branching Strategies Comparison
        - Git Flow Branch Layout
        - Trunk-Based Development (TBD)
    3. Practical Code Examples
        - Example A: Git Flow feature release sequence
        - Example B: Git Flow hotfix release sequence
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Choosing a strategy
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

#### 2.1.7. Module 7 — Git Internals

1. **Git Internals: Blobs, Trees & Commits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Object Relationship Diagram
        - Object Hierarchy Flow
        - Inside the `.git` Directory
        - SHA-1 vs. SHA-256 Hashes
        - Content-Addressable Storage & Deduplication
        - Sample Commit Object Layout
        - Porcelain vs. Plumbing
    3. Practical Code Examples
        - Internal Investigation Command Reference
        - Example A: Inspecting Objects E2E
        - Example B: Tag objects vs References
        - Example C: Pack files optimization
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
    5. Workout Answers & Solutions
        - Common Mistakes
        - Enterprise Best Practices
        - Key Takeaways

#### 2.1.8. Module 8 — Git Foundations

1. **Git Architecture & Three States**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Git File States & Environments
        - The Lifecycle of a File
        - The State Transition Flow Connected to `git status`
        - Repository Creation Workflows
    3. Practical Code Examples
        - Step-by-Step Lab 1: First-Time Git Setup (Run Only Once)
        - Step-by-Step Lab 2: Initializing and First Staging
        - Step-by-Step Lab 3: Creating Your First Commit
    4. Hands-on Workouts
        - Checkpoint Questions
        - Try It Yourself Exercise: Selective Staging
    5. Workout Answers & Solutions
        - Checkpoint Answers
        - Solution to Try It Yourself Exercise
        - Common Beginner Mistakes
2. **Local Workflow: Init, Stage & Commit**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Git Configuration Scopes & Precedence
        - git init vs. git clone
        - Short Status Output (`git status -s`)
        - Git Ignore Filters (`.gitignore`)
    3. Practical Code Examples
        - Before You Start
        - Step-by-Step Lab 1: Configuration Scopes
        - Step-by-Step Lab 2: Cloning an Existing Repository
        - Step-by-Step Lab 3: Ignoring Cache & Temp Files
    4. Hands-on Workouts
        - Workout Exercises
    5. Workout Answers & Solutions
        - Checkpoint Questions
        - Workout Solutions
        - Summary of New Concepts
        - Next Lesson Preview
3. **Version Control History & Evolution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - The Problem: Coding Without Version Control
        - Version Control System (VCS) Evolution Timeline
        - VCS Comparison Chart
        - Why Git Was Created
        - Git vs. GitHub
        - Why Git is Fast
    3. Practical Code Examples
        - Example A: Basic Environment Checks
        - Example B: Help Document Lookup
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Collaboration without Git
    5. Workout Answers & Solutions
        - Common Problems Solved by Git
        - Why Git Won the Industry
        - Key Takeaways

#### 2.1.9. Module 9 — History Management

1. **Inspecting History: Log & Diff**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Visual History Diagram
        - git diff State Comparisons
        - git log Cheat Sheet
        - git diff Comparison Chart
        - Understanding Diff Output Markers
        - git show
        - Commit Hash Mechanics
    3. Practical Code Examples
        - Example A: Basic log filtering
        - Example B: Snoop searching with `git log -S`
        - Example C: Practical Investigation Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Who updated the file lines?
        - Common Investigation Commands
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
2. **Interactive Staging: Patch Mode & Partial Commits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - What is Interactive Staging?
        - Patch Mode Options Decoded
    3. Practical Code Examples
        - Interactive Staging Cheat Sheet
        - Example A: Running an Interactive Staging Session
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Unrelated modifications
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
3. **Undoing Changes: Reset, Restore & Revert**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
        - Undo Action Decision Flow
    2. Definitions & Core Concepts
        - Command Comparisons
        - Visual Explanation of `git reset` Modes
        - Detached HEAD
        - git log vs. git reflog
    3. Practical Code Examples
        - Example A: git restore Variations
        - Example B: Detached HEAD branch creation
        - Example C: Realistic Recovery Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - When Should I Use... Reference Box
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

### 2.2. Git

#### 2.2.1. Module 1 — Core Concepts and Workflows

1. **Git Architecture & Three States**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Git File States & Environments
        - The Lifecycle of a File
        - The State Transition Flow Connected to `git status`
        - Repository Creation Workflows
    3. Practical Code Examples
        - Step-by-Step Lab 1: First-Time Git Setup (Run Only Once)
        - Step-by-Step Lab 2: Initializing and First Staging
        - Step-by-Step Lab 3: Creating Your First Commit
    4. Hands-on Workouts
        - Checkpoint Questions
        - Try It Yourself Exercise: Selective Staging
    5. Workout Answers & Solutions
        - Checkpoint Answers
        - Solution to Try It Yourself Exercise
        - Common Beginner Mistakes
2. **Local Workflow: Init, Stage & Commit**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Git Configuration Scopes & Precedence
        - git init vs. git clone
        - Short Status Output (`git status -s`)
        - Git Ignore Filters (`.gitignore`)
    3. Practical Code Examples
        - Before You Start
        - Step-by-Step Lab 1: Configuration Scopes
        - Step-by-Step Lab 2: Cloning an Existing Repository
        - Step-by-Step Lab 3: Ignoring Cache & Temp Files
    4. Hands-on Workouts
        - Workout Exercises
    5. Workout Answers & Solutions
        - Checkpoint Questions
        - Workout Solutions
        - Summary of New Concepts
        - Next Lesson Preview
3. **Inspecting History: Log & Diff**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Visual History Diagram
        - git diff State Comparisons
        - git log Cheat Sheet
        - git diff Comparison Chart
        - Understanding Diff Output Markers
        - git show
        - Commit Hash Mechanics
    3. Practical Code Examples
        - Example A: Basic log filtering
        - Example B: Snoop searching with `git log -S`
        - Example C: Practical Investigation Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Who updated the file lines?
        - Common Investigation Commands
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
4. **Version Control History & Evolution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - The Problem: Coding Without Version Control
        - Version Control System (VCS) Evolution Timeline
        - VCS Comparison Chart
        - Why Git Was Created
        - Git vs. GitHub
        - Why Git is Fast
    3. Practical Code Examples
        - Example A: Basic Environment Checks
        - Example B: Help Document Lookup
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Collaboration without Git
    5. Workout Answers & Solutions
        - Common Problems Solved by Git
        - Why Git Won the Industry
        - Key Takeaways
5. **Interactive Staging: Patch Mode & Partial Commits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - What is Interactive Staging?
        - Patch Mode Options Decoded
    3. Practical Code Examples
        - Interactive Staging Cheat Sheet
        - Example A: Running an Interactive Staging Session
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Unrelated modifications
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
6. **Undoing Changes: Reset, Restore & Revert**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
        - Undo Action Decision Flow
    2. Definitions & Core Concepts
        - Command Comparisons
        - Visual Explanation of `git reset` Modes
        - Detached HEAD
        - git log vs. git reflog
    3. Practical Code Examples
        - Example A: git restore Variations
        - Example B: Detached HEAD branch creation
        - Example C: Realistic Recovery Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - When Should I Use... Reference Box
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
7. **Branching Basics & Conflict Resolution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Branch Visualization Diagrams
        - Merging Strategies (FF vs. 3-Way)
        - Why Merge Conflicts Occur
        - Tagging Releases (Lightweight vs. Annotated)
    3. Practical Code Examples
        - Branch Command Cheat Sheet
        - Merge Command Cheat Sheet
        - Example A: Resolving Conflicts with git status Checks
        - Example B: Tagging and Remote Operations
        - Example C: Realistic Feature Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Standard Branch Naming Conventions
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
8. **Remote Repositories & Origin Config**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Visual Architecture Diagram
        - What is a Remote?
        - Git vs. Hosting Platforms
        - Clone vs. Fork
        - origin vs. upstream
        - Remote-Tracking Branches
        - HTTPS vs. SSH
    3. Practical Code Examples
        - Remote Command Cheat Sheet
        - Example A: Managing Multiple Remotes in Enterprise Environment
        - Example B: Renaming and Inspecting Remotes
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - E2E Remote Association Workflow
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
9. **Syncing Data: Fetch, Pull & Push**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Fetch vs. Pull Architecture Diagram
        - Fetch vs. Pull Comparison
        - git pull: Merge vs. Rebase
        - Ahead and Behind Tracking States
    3. Practical Code Examples
        - Syncing Commands Cheat Sheet
        - Example A: Pulling with Rebase
        - Example B: Pushing and linking branch
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Rejected Push
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
10. **Merge Conflict Handling in Teams**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Conflict Visualization Diagram
        - Conflict Resolution Workflow
        - Merge vs. Rebase Conflicts
        - Conflict Markers Decoded
        - HEAD vs. Theirs Pointer Reference Map
        - Conflict Types
    3. Practical Code Examples
        - Conflict Commands Cheat Sheet
        - Example A: Managing conflict status
        - Example B: Visual merge tools setup
        - Example C: Practical Team Resolution Workflow
        - Advanced Tip: `git rerere`
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge: Resolving Worksheets
        - Conflict Prevention Workflow Diagram
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
11. **Forking & Upstream Workflows**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - The Forking Workflow Diagram
        - Fork vs. Clone vs. Branch
        - origin vs. upstream
        - Pull Requests (PR) vs. Merge Requests (MR)
        - Merge vs. Rebase in Workflows
    3. Practical Code Examples
        - Remote Fork Commands Cheat Sheet
        - Example A: Full Open-Source Contribution Workflow
        - Example B: Syncing your Local Fork
        - Example C: Rebasing feature branches
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - GitHub Feature Lifecycle Flow
    5. Workout Answers & Solutions
        - Pull Request Best Practices
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
12. **Git Internals: Blobs, Trees & Commits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Object Relationship Diagram
        - Object Hierarchy Flow
        - Inside the `.git` Directory
        - SHA-1 vs. SHA-256 Hashes
        - Content-Addressable Storage & Deduplication
        - Sample Commit Object Layout
        - Porcelain vs. Plumbing
    3. Practical Code Examples
        - Internal Investigation Command Reference
        - Example A: Inspecting Objects E2E
        - Example B: Tag objects vs References
        - Example C: Pack files optimization
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
    5. Workout Answers & Solutions
        - Common Mistakes
        - Enterprise Best Practices
        - Key Takeaways
13. **Rewriting History: Amend, Rebase & Squash**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - History Rewriting Diagram
        - Decision Guide
        - History Rewriting Command Comparisons
        - Visualizing Interactive Rebase & Squashing
        - reflog Recovery Mechanics
    3. Practical Code Examples
        - Interactive Rebase Command Reference
        - Example A: Interactive Rebase Setup
        - Example B: Safe Force-Pushing
        - Example C: Complete Cleanup Workflow
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Undoing an amend
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
14. **Workspace Helpers: Stash, Bisect & Worktree**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
        - Workspace Helper Decision Guide
    2. Part 1: Git Stash
        - Stash Workflow
        - Stash Internals
        - Stash Commands Cheat Sheet
        - Enterprise Scenario: Stashing
    3. Part 2: Git Bisect
        - Bisect Visualization
        - Automated Bisect
        - Bisect Commands Cheat Sheet
        - Enterprise Scenario: Bisecting
    4. Part 3: Git Worktree
        - Worktree Visualization
        - Worktree vs. Clone
        - Worktree Commands Cheat Sheet
        - Enterprise Scenario: Worktrees
    5. Hands-on Workouts
        - MCQ
        - Coding Challenge
    6. Workout Answers & Solutions
        - Common Mistakes
        - Enterprise Best Practices
        - Key Takeaways
15. **Git Customization: Hooks & Aliases**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Git Hook Lifecycle Diagrams
        - Client-side vs. Server-side Hooks
        - Why Hooks Exist
        - Git Hook Trigger Reference
        - Modern SaaS Hosting Realities
    3. Practical Code Examples
        - Hook & Alias Cheat Sheet
        - Common Git Aliases
        - Example A: Enterprise Pre-commit Pipeline
        - Example B: Portable pre-commit hook (POSIX sh)
        - Example C: Robust commit-msg message parsing (Bash)
    4. Hands-on Workouts
        - MCQ
        - Hook Distribution Strategies
    5. Workout Answers & Solutions
        - Common Mistakes
        - Enterprise Best Practices
        - Key Takeaways
16. **Cherry-picking & Backporting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Cherry-picking Visual Diagram
        - What is Backporting?
        - Cherry-pick vs. Merge vs. Rebase
    3. Practical Code Examples
        - Cherry-pick Command Cheat Sheet
        - Example A: Cherry-picking a Hotfix
        - Example B: Handling Cherry-pick Conflicts
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Hotfixing
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
17. **Tags & Release Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Tag Types Comparison
        - Semantic Versioning (SemVer)
        - Tags vs. Releases
    3. Practical Code Examples
        - Tag Command Cheat Sheet
        - Example A: Creating and Pushing an Annotated Release Tag
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Security verification
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
18. **Branching Strategies for Teams**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - Branching Strategies Comparison
        - Git Flow Branch Layout
        - Trunk-Based Development (TBD)
    3. Practical Code Examples
        - Example A: Git Flow feature release sequence
        - Example B: Git Flow hotfix release sequence
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Choosing a strategy
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
19. **Credential Management & Security**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Definitions & Core Concepts
        - HTTPS vs. SSH Authentication
        - Credential Helpers
        - SSH Key Setup Overview
    3. Practical Code Examples
        - Credential Config Cheat Sheet
        - Example A: Setting Up SSH Authentication
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Token Expiration
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways
20. **Diagnostic & Troubleshooting Guide**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Learning Outcomes
    2. Common Git Troubleshooting Scenarios
        - Scenario 1: Detached HEAD State
        - Scenario 2: Recovering Lost Commits (Reflog)
        - Scenario 3: Committed on the Wrong Branch
        - Scenario 4: Stuck Merge or Rebase
        - Scenario 5: Force Push Recovery
    3. Practical Code Examples
        - Diagnostic Commands Cheat Sheet
        - Example A: Finding lost commits using `git fsck`
    4. Hands-on Workouts
        - MCQ
        - Coding Challenge
        - Scenario Question: Wrong branch commit
    5. Workout Answers & Solutions
        - Common Beginner Mistakes
        - Enterprise Best Practices
        - Key Takeaways

### 2.3. RESTful API Architecture & Design

#### 2.3.1. Module 1 — REST Fundamentals

1. **What Is REST**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **HTTP Methods and Status Codes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **URL Design Best Practices**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Request and Response Format**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **REST vs GraphQL vs gRPC**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.3.2. Module 2 — REST Principles & Standards

1. **HTTP Protocol Architecture & Verbs (GET, POST, PUT, DELETE, PATCH)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: HTTP Protocol Architecture & Verbs (GET, POST, PUT, DELETE, PATCH)
    2. Core Concept
        - Core Concept: HTTP Protocol Architecture & Verbs (GET, POST, PUT, DELETE, PATCH)
    3. Syntax
        - Syntax: HTTP Protocol Architecture & Verbs (GET, POST, PUT, DELETE, PATCH)
    4. Example
        - Example: HTTP Protocol Architecture & Verbs (GET, POST, PUT, DELETE, PATCH)
    5. Pitfall
        - Pitfall: HTTP Protocol Architecture & Verbs (GET, POST, PUT, DELETE, PATCH)
    6. Q & A
        - Q & A: HTTP Protocol Architecture & Verbs (GET, POST, PUT, DELETE, PATCH)
2. **REST Architectural Constraints & Statelessness**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: REST Architectural Constraints & Statelessness
    2. Core Concept
        - Core Concept: REST Architectural Constraints & Statelessness
    3. Syntax
        - Syntax: REST Architectural Constraints & Statelessness
    4. Example
        - Example: REST Architectural Constraints & Statelessness
    5. Pitfall
        - Pitfall: REST Architectural Constraints & Statelessness
    6. Q & A
        - Q & A: REST Architectural Constraints & Statelessness
3. **Resource Naming Conventions & URL Design**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Resource Naming Conventions & URL Design
    2. Core Concept
        - Core Concept: Resource Naming Conventions & URL Design
    3. Syntax
        - Syntax: Resource Naming Conventions & URL Design
    4. Example
        - Example: Resource Naming Conventions & URL Design
    5. Pitfall
        - Pitfall: Resource Naming Conventions & URL Design
    6. Q & A
        - Q & A: Resource Naming Conventions & URL Design
4. **HTTP Status Codes (2xx, 3xx, 4xx, 5xx)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: HTTP Status Codes (2xx, 3xx, 4xx, 5xx)
    2. Core Concept
        - Core Concept: HTTP Status Codes (2xx, 3xx, 4xx, 5xx)
    3. Syntax
        - Syntax: HTTP Status Codes (2xx, 3xx, 4xx, 5xx)
    4. Example
        - Example: HTTP Status Codes (2xx, 3xx, 4xx, 5xx)
    5. Pitfall
        - Pitfall: HTTP Status Codes (2xx, 3xx, 4xx, 5xx)
    6. Q & A
        - Q & A: HTTP Status Codes (2xx, 3xx, 4xx, 5xx)
5. **API Versioning Strategies (URI, Header, Query)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: API Versioning Strategies (URI, Header, Query)
    2. Core Concept
        - Core Concept: API Versioning Strategies (URI, Header, Query)
    3. Syntax
        - Syntax: API Versioning Strategies (URI, Header, Query)
    4. Example
        - Example: API Versioning Strategies (URI, Header, Query)
    5. Pitfall
        - Pitfall: API Versioning Strategies (URI, Header, Query)
    6. Q & A
        - Q & A: API Versioning Strategies (URI, Header, Query)

#### 2.3.3. Module 3 — API Design

1. **Resource Naming Conventions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Pagination Patterns**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Error Response Design**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **API Versioning Strategies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **HATEOAS**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.3.4. Module 4 — Request & Response Engineering

1. **Designing Consistent JSON Payload Schemas**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Designing Consistent JSON Payload Schemas
    2. Core Concept
        - Core Concept: Designing Consistent JSON Payload Schemas
    3. Syntax
        - Syntax: Designing Consistent JSON Payload Schemas
    4. Example
        - Example: Designing Consistent JSON Payload Schemas
    5. Pitfall
        - Pitfall: Designing Consistent JSON Payload Schemas
    6. Q & A
        - Q & A: Designing Consistent JSON Payload Schemas
2. **Pagination, Sorting, and Filtering Patterns**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Pagination, Sorting, and Filtering Patterns
    2. Core Concept
        - Core Concept: Pagination, Sorting, and Filtering Patterns
    3. Syntax
        - Syntax: Pagination, Sorting, and Filtering Patterns
    4. Example
        - Example: Pagination, Sorting, and Filtering Patterns
    5. Pitfall
        - Pitfall: Pagination, Sorting, and Filtering Patterns
    6. Q & A
        - Q & A: Pagination, Sorting, and Filtering Patterns
3. **Global Error Handling & RFC 7807 Problem Details**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Global Error Handling & RFC 7807 Problem Details
    2. Core Concept
        - Core Concept: Global Error Handling & RFC 7807 Problem Details
    3. Syntax
        - Syntax: Global Error Handling & RFC 7807 Problem Details
    4. Example
        - Example: Global Error Handling & RFC 7807 Problem Details
    5. Pitfall
        - Pitfall: Global Error Handling & RFC 7807 Problem Details
    6. Q & A
        - Q & A: Global Error Handling & RFC 7807 Problem Details
4. **Handling File Uploads & Multipart Requests**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Handling File Uploads & Multipart Requests
    2. Core Concept
        - Core Concept: Handling File Uploads & Multipart Requests
    3. Syntax
        - Syntax: Handling File Uploads & Multipart Requests
    4. Example
        - Example: Handling File Uploads & Multipart Requests
    5. Pitfall
        - Pitfall: Handling File Uploads & Multipart Requests
    6. Q & A
        - Q & A: Handling File Uploads & Multipart Requests
5. **API Rate Limiting & Throttling Strategies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: API Rate Limiting & Throttling Strategies
    2. Core Concept
        - Core Concept: API Rate Limiting & Throttling Strategies
    3. Syntax
        - Syntax: API Rate Limiting & Throttling Strategies
    4. Example
        - Example: API Rate Limiting & Throttling Strategies
    5. Pitfall
        - Pitfall: API Rate Limiting & Throttling Strategies
    6. Q & A
        - Q & A: API Rate Limiting & Throttling Strategies

#### 2.3.5. Module 5 — API Documentation

1. **OpenAPI and Swagger**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **FastAPI Auto Docs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Postman Collections**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **API Changelog**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **API Mocking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.3.6. Module 6 — Documentation & Testing

1. **OpenAPI / Swagger Specification Standard**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: OpenAPI / Swagger Specification Standard
    2. Core Concept
        - Core Concept: OpenAPI / Swagger Specification Standard
    3. Syntax
        - Syntax: OpenAPI / Swagger Specification Standard
    4. Example
        - Example: OpenAPI / Swagger Specification Standard
    5. Pitfall
        - Pitfall: OpenAPI / Swagger Specification Standard
    6. Q & A
        - Q & A: OpenAPI / Swagger Specification Standard
2. **Contract-First vs Code-First API Design**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Contract-First vs Code-First API Design
    2. Core Concept
        - Core Concept: Contract-First vs Code-First API Design
    3. Syntax
        - Syntax: Contract-First vs Code-First API Design
    4. Example
        - Example: Contract-First vs Code-First API Design
    5. Pitfall
        - Pitfall: Contract-First vs Code-First API Design
    6. Q & A
        - Q & A: Contract-First vs Code-First API Design
3. **API Integration Testing with Postman & Pytest**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: API Integration Testing with Postman & Pytest
    2. Core Concept
        - Core Concept: API Integration Testing with Postman & Pytest
    3. Syntax
        - Syntax: API Integration Testing with Postman & Pytest
    4. Example
        - Example: API Integration Testing with Postman & Pytest
    5. Pitfall
        - Pitfall: API Integration Testing with Postman & Pytest
    6. Q & A
        - Q & A: API Integration Testing with Postman & Pytest
4. **CORS (Cross-Origin Resource Sharing) Configuration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: CORS (Cross-Origin Resource Sharing) Configuration
    2. Core Concept
        - Core Concept: CORS (Cross-Origin Resource Sharing) Configuration
    3. Syntax
        - Syntax: CORS (Cross-Origin Resource Sharing) Configuration
    4. Example
        - Example: CORS (Cross-Origin Resource Sharing) Configuration
    5. Pitfall
        - Pitfall: CORS (Cross-Origin Resource Sharing) Configuration
    6. Q & A
        - Q & A: CORS (Cross-Origin Resource Sharing) Configuration
5. **Building a Production REST API with Python**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Building a Production REST API with Python
    2. Core Concept
        - Core Concept: Building a Production REST API with Python
    3. Syntax
        - Syntax: Building a Production REST API with Python
    4. Example
        - Example: Building a Production REST API with Python
    5. Pitfall
        - Pitfall: Building a Production REST API with Python
    6. Q & A
        - Q & A: Building a Production REST API with Python

### 2.4. Flask

#### 2.4.1. Module 1 — WSGI Architecture & Flask Core Basics

1. **Lesson 1.1 Web Server Gateway Interface (WSGI) Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is WSGI (PEP 3333)?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is WSGI in Python web development and why is `Flask(__name__)` required?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 1.2 Flask Application Factory Pattern & Configuration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why the Application Factory Pattern?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `config.py` (Environment Configurations)
        - File 2: `app/__init__.py` (Application Factory)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the Application Factory Pattern in Flask and why is it recommended for production applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.4.2. Module 2 — Routing, Request Handling, & Responses

1. **Lesson 2.1 Routing System, Dynamic URL Parameters, & Converter Types**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Built-in URL Converters
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you use `url_for()` instead of hardcoding URL strings in Flask?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 2.2 HTTP Methods, Request Object Inspection, & Response Formatting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Flask `request` Context Local
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Context Local in Flask and how does the `request` object work behind the scenes?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.4.3. Module 3 — Jinja2 Templating Engine

1. **Lesson 3.1 Jinja2 Syntax, Variables, Control Flow, & Macros**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Jinja2 Delimiter Syntax
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `templates/macros/card.html` (Jinja2 Reusable Macro)
        - File 2: `templates/dashboard.html` (Main Page)
        - File 3: `app.py` (Python View Function)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does Jinja2 prevent Cross-Site Scripting (XSS) attacks when rendering dynamic variables?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.4.4. Module 4 — Flask Application Contexts & Globals

1. **Lesson 4.1 Application Context & Request Context Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Application Context vs Request Context
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between the Application Context and Request Context in Flask?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 4.2 The g Global Object & Request-Scoped State**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is the `g` Object?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `g` and `session` in Flask?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.4.5. Module 5 — Advanced Flask Patterns

1. **Flask Response Objects and Streaming**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Response Object Basics
        - Streaming Responses
        - Server-Sent Events (SSE)
        - File Streaming
        - JSON Responses
    2. Lab Exercise
2. **Advanced Form Validation and File Uploads**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - WTForms File Field
        - Secure File Handling
        - MIME Type Validation
        - Multiple File Uploads
        - Custom Validators
    2. Lab Exercise
3. **SQLAlchemy Relationship Types and Lazy Loading**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - One-to-Many Relationship
        - Many-to-Many with Association Table
        - Lazy Loading Strategies
        - Association Object Pattern (with extra fields)
    2. Lab Exercise
4. **Access Control and Role Authorization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Role-Based Access Control (RBAC) Pattern
        - Role-Required Decorator
        - Permission-Based Access (Fine-Grained)
        - Flask-Principal Integration
    2. Lab Exercise

#### 2.4.6. Module 6 — Web Forms & Input Validation (Flask-WTF)

1. **Lesson 5.1 WTForms & Flask-WTF Extension**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Processing Manual HTML Forms vs Flask-WTF
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `forms.py` (FlaskForm Class Definition)
        - File 2: `app.py` (Flask View Function)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `form.validate_on_submit()` do in Flask-WTF?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 5.2 Form Validation & Automatic CSRF Protection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Custom In-Class Field Validation
        - CSRF Protection Mechanism
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `forms.py` (Form with Custom & Standard Validators)
        - File 2: `templates/register.html` (Rendering Inline Validation Errors)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do you write a custom field validator in Flask-WTF?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.4.7. Module 7 — Production Deployment

1. **Reverse Proxy and Nginx Configuration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Nginx as Reverse Proxy for Flask
        - Gunicorn Configuration
        - SSL/HTTPS with Let's Encrypt
        - Flask ProxyFix Middleware
        - Systemd Service
    2. Lab Exercise
2. **Containerization with Docker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Flask Dockerfile
        - Docker Compose (Flask + MySQL + Redis)
        - Environment Management
        - Build and Run Commands
        - Health Check and Restart Policy
    2. Lab Exercise

#### 2.4.8. Module 8 — Relational Databases & ORM (Flask-SQLAlchemy)

1. **Lesson 6.1 Flask-SQLAlchemy Extension Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Object-Relational Mapping (ORM)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `extensions.py` (Unbound Extension Instance)
        - File 2: `config.py`
        - File 3: `app/__init__.py` (Application Factory Integration)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why should you initialize Flask-SQLAlchemy using `db = SQLAlchemy()` in an `extensions.py` module rather than `db = SQLAlchemy(app)`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 6.2 Defining SQLAlchemy Models, Fields, & Relationships**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SQLAlchemy Model Mapping
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `models.py` (SQLAlchemy Relational Schema)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `backref` and `back_populates` in SQLAlchemy relationships?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 6.3 Executing Database CRUD Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Unit of Work Transaction Management
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `db.session.rollback()` in Flask-SQLAlchemy?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
4. **Lesson 6.4 Schema Migrations with Flask-Migrate & Alembic**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why `db.create_all()` Fails in Production
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `extensions.py`
        - File 2: `app/__init__.py` (Factory Integration)
        - File 3: Command Line Execution Sequence
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does Flask-Migrate detect changes made to SQLAlchemy models when generating migration scripts?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.4.9. Module 9 — Session Management, Cookies, & Authentication

1. **Lesson 7.1 User Authentication with Flask-Login**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Flask-Login Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `models.py` (User Model with UserMixin)
        - File 2: `app.py` (Flask-Login Initialization & Auth Routes)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `@login_manager.user_loader` in Flask-Login?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 7.2 Password Hashing & Cookie Security**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - One-Way Password Hashing & Salting
        - Flask Session Cookie Security Configuration
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File: `security_demo.py` (Password Hashing & Cookie Security Config)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is storing plain MD5 or SHA-256 hashes of passwords insecure, and how does Werkzeug address this?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.4.10. Module 10 — Application Structuring with Blueprints

1. **Lesson 8.1 Flask Blueprint Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is a Flask Blueprint?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `app/api/routes.py` (Blueprint Module)
        - File 2: `app/__init__.py` (Registering Blueprints in Application Factory)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a Flask Blueprint and how does it improve code architecture?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.4.11. Module 11 — REST API Development & Serialization

1. **Lesson 9.1 RESTful API Principles & Resource Routing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - REST Architectural Constraints
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is idempotency in RESTful APIs and which HTTP verbs are idempotent?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 9.2 API Serialization with Flask-Marshmallow**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Serialization vs Deserialization
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `schemas.py` (Flask-Marshmallow Schemas)
        - File 2: `routes.py` (Using Schemas in API Views)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the primary role of Marshmallow schemas in a Flask REST API?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 9.3 JWT Authentication with Flask-JWT-Extended**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - JSON Web Token (JWT) Structure
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the main structural difference between session-based authentication and JWT authentication?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.4.12. Module 12 — Advanced Flask Extensions & Background Tasks

1. **Lesson 10.1 Application Caching with Flask-Caching & Redis**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why Backend Caching?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `@cache.cached()` and `@cache.memoize()` in Flask-Caching?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 10.2 Asynchronous Background Tasks with Celery & Redis**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why Asynchronous Background Tasks?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `celery_app.py` (Celery Integration Helper)
        - File 2: `tasks.py` (Celery Tasks)
        - File 3: `app.py` (Dispatching Tasks & Checking Status)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is Celery used with Flask instead of Python's built-in `threading` module?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
3. **Lesson 10.3 Email Delivery with Flask-Mail**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SMTP Protocol & Synchronous vs Async Delivery
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is it crucial to send emails asynchronously in web applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.4.13. Module 13 — Error Handling, Logging, & Testing

1. **Lesson 11.1 Custom Error Pages & Error Handlers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Exception Handling Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the difference between `@errorhandler` and `@app_errorhandler` on a Flask Blueprint?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 11.2 Application Logging & Sentry Integration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Production Logging Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `RotatingFileHandler` critical for production Python applications?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.4.14. Module 14 — Testing & Production Deployment

1. **Lesson 12.1 Automated Testing with Pytest & Test Client**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Flask `test_client()` Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `conftest.py` (Pytest Shared Fixtures)
        - File 2: `test_api.py` (Pytest Test Cases)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does Flask's `app.test_client()` work and why is it preferred over HTTP requests library like `requests` during unit testing?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 12.2 Production Deployment with Gunicorn, Nginx, & Docker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Enterprise Production Deployment Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `wsgi.py` (Production Entrypoint)
        - File 2: `Dockerfile` (Production Multi-Stage Container)
        - File 3: `docker-compose.yml` (Multi-Container Orchestration)
        - File 4: `nginx.conf` (Nginx Reverse Proxy Configuration)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why must Flask's built-in development server never be used in production environments, and what roles do Gunicorn and Nginx play?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

### 2.5. FastAPI

#### 2.5.1. Module 1 — Modern Async Python & FastAPI Core Architecture

1. **Lesson 1.1 Async Python, ASGI Architecture, & Uvicorn Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - WSGI vs ASGI Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Running with Uvicorn Server:
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What happens if you call a synchronous blocking function inside an `async def` endpoint in FastAPI?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Migrated Notes
    16. Topic 2: REST API Design & Constraints (REST vs RPC)
        - The Big Picture
        - Lesson Objectives
        - Detailed Explanation & Core Concepts
        - Real-world Examples: REST vs RPC
        - Code Comparison: FastAPI (Python)
        - Code Comparison: Spring Boot (Java)
        - Professional Notes
        - Cheat Sheet: REST URI Rules
        - Hands-on Workout & Assessment
        - Flashcards
        - Progress Tracker
2. **Lesson 1.2 FastAPI Application Instantiation, Routing, & OpenAPI UI**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Zero-Configuration Automatic OpenAPI Generation
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does FastAPI generate Swagger UI documentation automatically without third-party plugins?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Migrated Notes
    16. Topic 6: The HTTP Protocol (Deep Dive)
        - The Big Picture
        - Anatomy of an HTTP Request
        - Anatomy of an HTTP Response
        - HTTP Methods & Their Properties
        - HTTP Headers: The Control Knobs of the Web
        - Python Example: Inspecting Request Headers and Body
        - Hands-on Workout & Assessment
        - Progress Tracker

#### 2.5.2. Module 2 — Request Validation & Pydantic Data Models

1. **Lesson 2.1 Path Parameters, Query Strings, & Type Annotations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Parameter Parsing & Automatic Type Conversion
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does FastAPI differentiate between a Path Parameter and a Query Parameter in a route function?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Migrated Notes
    16. Topic 8: FastAPI & CRUD Operations
        - The Big Picture
        - Pydantic for Validation and Serialization
        - Implementing CRUD in FastAPI
        - Professional Notes: PUT vs PATCH
        - Hands-on Workout & Assessment
        - Progress Tracker
2. **Lesson 2.2 Pydantic v2 Models & Schema Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Pydantic v2 Architecture
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the key improvements of Pydantic v2 over Pydantic v1 in FastAPI?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.5.3. Module 3 — Dependency Injection System

1. **Lesson 3.1 Dependency Injection Architecture & Depends()**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is Dependency Injection?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What are the main benefits of FastAPI's Dependency Injection system over traditional middleware?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 3.2 Sub-Dependencies, Security Dependencies, & Yield Cleanups**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Yield Dependencies & Context Cleanup
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - Mocking Dependencies in Unit Tests:
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do Yield Dependencies work in FastAPI and how do they prevent resource leaks?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.5.4. Module 4 — Advanced Features

1. **API Metadata and Documentation Enrichment**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - App-Level Metadata
        - Route-Level Metadata
        - Hiding Routes from Docs
        - Customising Docs URLs
    2. Lab
2. **Query Parameters and Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Basic Query Parameters
        - Annotated with Query()
        - List Query Parameters
        - Regex Validation
    2. Lab
3. **Multi-Source Parameter Declarations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Mixing Path, Query, Body
        - Multiple Body Parameters
        - Body with `embed=True`
        - Header and Cookie
    2. Lab
4. **Form Submissions and File Handling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Form Data
        - File Upload
        - File + Form Together
        - Multiple Files
        - File Size Limit
    2. Lab
5. **Headers Cookies and Request Info**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Reading Headers
        - Reading Cookies
        - Setting Response Headers and Cookies
        - Raw Request Object
    2. Lab
6. **Advanced Response Classes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Response Class Variants
        - Streaming Response
        - ORJSONResponse (faster)
        - Custom Headers in Response
    2. Lab
7. **Custom Exception Handling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - HTTPException
        - Custom Exception Classes
        - Override Validation Error Format
        - Global Error Catch-All
    2. Lab
8. **WebSocket Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Basic WebSocket Endpoint
        - Connection Manager (Broadcast)
        - Sending JSON
        - WebSocket Authentication
    2. Lab
9. **OpenAPI Standard and Interactive UI**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Auto-Generated OpenAPI Schema
        - Request/Response Examples
        - Field-Level Examples
        - Custom OpenAPI Function
    2. Lab

#### 2.5.5. Module 5 — Async Database Integration with SQLAlchemy 2.0 & asyncpg

1. **Lesson 4.1 SQLAlchemy 2.0 Async Engine & asyncpg**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Synchronous vs Asynchronous Database Drivers
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `database.py` (SQLAlchemy 2.0 Async Engine & Dependency)
        - File 2: `main.py` (Using AsyncSession in Route)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `asyncpg` significantly faster than `psycopg2` when used with FastAPI?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Migrated Notes
    16. Topic 14: Database Relationships & Normalization
        - The Big Picture
        - Entity Relationships
        - Implementing Relationships in SQLAlchemy
        - Hands-on Workout & Assessment
        - Progress Tracker
2. **Lesson 4.2 Async CRUD Operations & AsyncSession**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - SQLAlchemy 2.0 Async Query Style
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `models.py` (Async SQLAlchemy Models)
        - File 2: `main.py` (Async CRUD Routes)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is lazy loading problematic in asynchronous SQLAlchemy and how does `selectinload()` solve it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Migrated Notes
    16. Topic 15: Database Indexes & ACID Transactions
        - Database Indexes
        - ACID Transactions
        - Implementing Transactions in SQLAlchemy
        - Hands-on Workout & Assessment
        - Progress Tracker

#### 2.5.6. Module 6 — Database Integration

1. **Schema Evolution with Alembic**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Alembic Setup
        - Creating Migrations
        - Migration File
        - Async Alembic
    2. Lab
2. **Scope-Based Fine-Grained Authorization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - JWT with Scopes
        - Scope Validation Dependency
        - Protecting Routes with Scopes
    2. Lab

#### 2.5.7. Module 7 — Security & Authentication

1. **Lesson 5.1 OAuth2 Password Bearer & Password Hashing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - OAuth2 Password Bearer Flow
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What does `OAuth2PasswordBearer` do under the hood in FastAPI?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Migrated Notes
    16. Topic 12: OAuth2 & Session-based Authentication
        - The Big Picture
        - What is OAuth2?
        - The OAuth2 Authorization Code Flow (The Standard Web Flow)
        - OAuth2 Scopes
        - Python Example: OAuth2 Password Flow with Scopes in FastAPI
        - Hands-on Workout & Assessment
        - Progress Tracker
2. **Lesson 5.2 JWT Authentication & Current User Dependency**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The `get_current_user` Dependency Pipeline
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does FastAPI implement Role-Based Access Control (RBAC) cleanly using Dependency Injection?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Migrated Notes
    16. Topic 11: Token-based Authentication & JWT (JSON Web Tokens)
        - The Big Picture
        - Anatomy of a JWT
        - JWT Authentication Flow
        - Password Hashing (Crucial Security)
        - Python Example: JWT Handling in FastAPI
        - Hands-on Workout & Assessment
        - Progress Tracker

#### 2.5.8. Module 8 — Production FastAPI

1. **Application Setup and Environment Configuration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Topics Covered
        - Settings with pydantic-settings
        - Dependency-Cached Settings
        - Lifespan Events (startup/shutdown)
        - Environment-Specific Configuration
    2. Lab

#### 2.5.9. Module 9 — Modular Application Structuring with APIRouter

1. **Lesson 6.1 APIRouter() Architecture & Route Prefixes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is an APIRouter?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `routers/devices.py` (APIRouter Module)
        - File 2: `main.py` (Main FastAPI App Registering Router)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How does `APIRouter` in FastAPI differ from Flask's `Blueprint`?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Migrated Notes
    16. Topic 3: API Architecture, Layered Patterns, and Dependency Injection
        - The Big Picture
        - Lesson Objectives
        - Detailed Explanation & Core Concepts
        - Code Comparison: FastAPI (Python)
        - Code Comparison: Spring Boot (Java)
        - Professional Notes
        - Hands-on Workout & Assessment
        - Flashcards
        - Progress Tracker
2. **Lesson 6.2 Modular Directory Structure & Big Applications**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Enterprise Production Directory Layout
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `src/app/core/config.py` (Pydantic-Settings Configuration)
        - File 2: `src/app/main.py` (Global Exception Handler & Main App)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `pydantic-settings` preferred over `os.environ.get()` in FastAPI production codebases?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.5.10. Module 10 — Asynchronous Middleware & CORS

1. **Lesson 7.1 Asynchronous Custom Middleware & CORS**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What is FastAPI Middleware?
        - Cross-Origin Resource Sharing (CORS)
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is a CORS preflight request and how does FastAPI handle it?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Migrated Notes
    16. Topic 9: API Request Lifecycle, Middleware, and CORS
        - The Big Picture
        - What is Middleware?
        - Understanding CORS (Cross-Origin Resource Sharing)
        - Python Example: Configuring CORS and Custom Middleware in FastAPI
        - Hands-on Workout & Assessment
        - Progress Tracker
2. **Lesson 7.2 Request Timing Headers & Performance Logging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - High-Precision Latency Tracking
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `time.perf_counter()` preferred over `time.time()` for measuring code latency?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Migrated Notes
    16. Topic 16: Caching with Redis & Rate Limiting
        - Caching with Redis
        - Rate Limiting
        - Python Example: Cache-Aside with Redis in FastAPI
        - Hands-on Workout & Assessment
        - Progress Tracker

#### 2.5.11. Module 11 — Background Tasks & Asynchronous Event Handlers

1. **Lesson 8.1 FastAPI Background Tasks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What are FastAPI BackgroundTasks?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: When should you use FastAPI `BackgroundTasks` versus an external task queue like Celery?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 8.2 Lifespan Event Handlers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - What are Lifespan Events?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why did FastAPI deprecate `@app.on_event("startup")` in favor of the `lifespan` context manager?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.5.12. Module 12 — WebSockets & Real-Time Communication

1. **Lesson 9.1 WebSockets Protocol & Endpoint Handling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - HTTP Polling vs Full-Duplex WebSockets
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: What is the purpose of `await websocket.accept()` in a FastAPI WebSocket endpoint?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
2. **Lesson 9.2 Real-Time Connection Manager & Broadcasting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - The Connection Manager Pattern
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do you scale WebSocket broadcasting across multiple Uvicorn worker processes or servers?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.5.13. Module 13 — Testing & Production Deployment

1. **Lesson 10.1 Async Testing with Pytest & httpx.AsyncClient**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Why `httpx.AsyncClient` over Starlette `TestClient`?
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `conftest.py` (Pytest Async Fixtures)
        - File 2: `test_main.py` (Async Test Cases)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why is `httpx.AsyncClient` preferred over `TestClient` when testing async FastAPI applications with Pytest?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Migrated Notes
    16. Topic 17: Testing with Pytest & Mocking
        - The Big Picture
        - Testing with Pytest
        - What is Mocking?
        - Python Example: Writing a FastAPI Test with Pytest
        - Hands-on Workout & Assessment
        - Progress Tracker
2. **Lesson 10.2 Production Deployment with Gunicorn Uvicorn Workers & Docker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Production Process Management: Gunicorn + Uvicorn
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
        - File 1: `gunicorn_conf.py` (Gunicorn Configuration)
        - File 2: `Dockerfile` (Production Container Definition)
        - File 3: `docker-compose.yml` (Multi-Container Deployment)
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: Why do we use Gunicorn together with Uvicorn in production rather than running Uvicorn alone?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet
    15. Migrated Notes
    16. Topic 18: Containerization with Docker & Production Best Practices
        - The Big Picture
        - Core Docker Concepts
        - Production-Grade Dockerfile for FastAPI
        - Docker Compose for Local Development
        - Hands-on Workout & Assessment
        - Progress Tracker

### 2.6. Authentication, Authorization & JWT

#### 2.6.1. Module 1 — Authentication Concepts

1. **Authentication vs Authorization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Session-Based Authentication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Token-Based Authentication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **OAuth2 Flows Overview**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **SSO and SAML**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.6.2. Module 2 — Authentication Fundamentals

1. **Session-Based vs Token-Based Authentication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Session-Based vs Token-Based Authentication
    2. Core Concept
        - Core Concept: Session-Based vs Token-Based Authentication
    3. Syntax
        - Syntax: Session-Based vs Token-Based Authentication
    4. Example
        - Example: Session-Based vs Token-Based Authentication
    5. Pitfall
        - Pitfall: Session-Based vs Token-Based Authentication
    6. Q & A
        - Q & A: Session-Based vs Token-Based Authentication
2. **Password Hashing Standards (Bcrypt, Argon2)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Password Hashing Standards (Bcrypt, Argon2)
    2. Core Concept
        - Core Concept: Password Hashing Standards (Bcrypt, Argon2)
    3. Syntax
        - Syntax: Password Hashing Standards (Bcrypt, Argon2)
    4. Example
        - Example: Password Hashing Standards (Bcrypt, Argon2)
    5. Pitfall
        - Pitfall: Password Hashing Standards (Bcrypt, Argon2)
    6. Q & A
        - Q & A: Password Hashing Standards (Bcrypt, Argon2)
3. **Secure Storage of Credentials in Databases**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Secure Storage of Credentials in Databases
    2. Core Concept
        - Core Concept: Secure Storage of Credentials in Databases
    3. Syntax
        - Syntax: Secure Storage of Credentials in Databases
    4. Example
        - Example: Secure Storage of Credentials in Databases
    5. Pitfall
        - Pitfall: Secure Storage of Credentials in Databases
    6. Q & A
        - Q & A: Secure Storage of Credentials in Databases
4. **OAuth 2.0 & OpenID Connect Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: OAuth 2.0 & OpenID Connect Fundamentals
    2. Core Concept
        - Core Concept: OAuth 2.0 & OpenID Connect Fundamentals
    3. Syntax
        - Syntax: OAuth 2.0 & OpenID Connect Fundamentals
    4. Example
        - Example: OAuth 2.0 & OpenID Connect Fundamentals
    5. Pitfall
        - Pitfall: OAuth 2.0 & OpenID Connect Fundamentals
    6. Q & A
        - Q & A: OAuth 2.0 & OpenID Connect Fundamentals
5. **Multi-Factor Authentication (MFA/TOTP) Mechanics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Multi-Factor Authentication (MFA/TOTP) Mechanics
    2. Core Concept
        - Core Concept: Multi-Factor Authentication (MFA/TOTP) Mechanics
    3. Syntax
        - Syntax: Multi-Factor Authentication (MFA/TOTP) Mechanics
    4. Example
        - Example: Multi-Factor Authentication (MFA/TOTP) Mechanics
    5. Pitfall
        - Pitfall: Multi-Factor Authentication (MFA/TOTP) Mechanics
    6. Q & A
        - Q & A: Multi-Factor Authentication (MFA/TOTP) Mechanics

#### 2.6.3. Module 3 — JWT in Depth

1. **JWT Structure**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Signing Algorithms**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Access and Refresh Tokens**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **JWT Claims**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **JWT Security Pitfalls**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.6.4. Module 4 — JSON Web Tokens (JWT) Deep Dive

1. **JWT Structure: Header, Payload, and Signature**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: JWT Structure: Header, Payload, and Signature
    2. Core Concept
        - Core Concept: JWT Structure: Header, Payload, and Signature
    3. Syntax
        - Syntax: JWT Structure: Header, Payload, and Signature
    4. Example
        - Example: JWT Structure: Header, Payload, and Signature
    5. Pitfall
        - Pitfall: JWT Structure: Header, Payload, and Signature
    6. Q & A
        - Q & A: JWT Structure: Header, Payload, and Signature
2. **Signing Algorithms (HS256 vs RS256)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Signing Algorithms (HS256 vs RS256)
    2. Core Concept
        - Core Concept: Signing Algorithms (HS256 vs RS256)
    3. Syntax
        - Syntax: Signing Algorithms (HS256 vs RS256)
    4. Example
        - Example: Signing Algorithms (HS256 vs RS256)
    5. Pitfall
        - Pitfall: Signing Algorithms (HS256 vs RS256)
    6. Q & A
        - Q & A: Signing Algorithms (HS256 vs RS256)
3. **Access Tokens vs Refresh Tokens Strategy**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Access Tokens vs Refresh Tokens Strategy
    2. Core Concept
        - Core Concept: Access Tokens vs Refresh Tokens Strategy
    3. Syntax
        - Syntax: Access Tokens vs Refresh Tokens Strategy
    4. Example
        - Example: Access Tokens vs Refresh Tokens Strategy
    5. Pitfall
        - Pitfall: Access Tokens vs Refresh Tokens Strategy
    6. Q & A
        - Q & A: Access Tokens vs Refresh Tokens Strategy
4. **Storing Tokens Safely (HttpOnly Cookies vs LocalStorage)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Storing Tokens Safely (HttpOnly Cookies vs LocalStorage)
    2. Core Concept
        - Core Concept: Storing Tokens Safely (HttpOnly Cookies vs LocalStorage)
    3. Syntax
        - Syntax: Storing Tokens Safely (HttpOnly Cookies vs LocalStorage)
    4. Example
        - Example: Storing Tokens Safely (HttpOnly Cookies vs LocalStorage)
    5. Pitfall
        - Pitfall: Storing Tokens Safely (HttpOnly Cookies vs LocalStorage)
    6. Q & A
        - Q & A: Storing Tokens Safely (HttpOnly Cookies vs LocalStorage)
5. **Token Revocation & Blacklisting Strategies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Token Revocation & Blacklisting Strategies
    2. Core Concept
        - Core Concept: Token Revocation & Blacklisting Strategies
    3. Syntax
        - Syntax: Token Revocation & Blacklisting Strategies
    4. Example
        - Example: Token Revocation & Blacklisting Strategies
    5. Pitfall
        - Pitfall: Token Revocation & Blacklisting Strategies
    6. Q & A
        - Q & A: Token Revocation & Blacklisting Strategies

#### 2.6.5. Module 5 — Implementation

1. **JWT with Flask**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **JWT with FastAPI**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Role-Based Access Control**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Password Hashing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Auth Best Practices Checklist**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.6.6. Module 6 — Authorization & Security Best Practices

1. **Role-Based Access Control (RBAC) Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Role-Based Access Control (RBAC) Architecture
    2. Core Concept
        - Core Concept: Role-Based Access Control (RBAC) Architecture
    3. Syntax
        - Syntax: Role-Based Access Control (RBAC) Architecture
    4. Example
        - Example: Role-Based Access Control (RBAC) Architecture
    5. Pitfall
        - Pitfall: Role-Based Access Control (RBAC) Architecture
    6. Q & A
        - Q & A: Role-Based Access Control (RBAC) Architecture
2. **Attribute-Based Access Control (ABAC) Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Attribute-Based Access Control (ABAC) Fundamentals
    2. Core Concept
        - Core Concept: Attribute-Based Access Control (ABAC) Fundamentals
    3. Syntax
        - Syntax: Attribute-Based Access Control (ABAC) Fundamentals
    4. Example
        - Example: Attribute-Based Access Control (ABAC) Fundamentals
    5. Pitfall
        - Pitfall: Attribute-Based Access Control (ABAC) Fundamentals
    6. Q & A
        - Q & A: Attribute-Based Access Control (ABAC) Fundamentals
3. **Securing REST Endpoints & Middleware Interceptors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Securing REST Endpoints & Middleware Interceptors
    2. Core Concept
        - Core Concept: Securing REST Endpoints & Middleware Interceptors
    3. Syntax
        - Syntax: Securing REST Endpoints & Middleware Interceptors
    4. Example
        - Example: Securing REST Endpoints & Middleware Interceptors
    5. Pitfall
        - Pitfall: Securing REST Endpoints & Middleware Interceptors
    6. Q & A
        - Q & A: Securing REST Endpoints & Middleware Interceptors
4. **CSRF Protection & Security Headers (CSP, HSTS)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: CSRF Protection & Security Headers (CSP, HSTS)
    2. Core Concept
        - Core Concept: CSRF Protection & Security Headers (CSP, HSTS)
    3. Syntax
        - Syntax: CSRF Protection & Security Headers (CSP, HSTS)
    4. Example
        - Example: CSRF Protection & Security Headers (CSP, HSTS)
    5. Pitfall
        - Pitfall: CSRF Protection & Security Headers (CSP, HSTS)
    6. Q & A
        - Q & A: CSRF Protection & Security Headers (CSP, HSTS)
5. **Building a Complete Python Security Auth Microservice**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Building a Complete Python Security Auth Microservice
    2. Core Concept
        - Core Concept: Building a Complete Python Security Auth Microservice
    3. Syntax
        - Syntax: Building a Complete Python Security Auth Microservice
    4. Example
        - Example: Building a Complete Python Security Auth Microservice
    5. Pitfall
        - Pitfall: Building a Complete Python Security Auth Microservice
    6. Q & A
        - Q & A: Building a Complete Python Security Auth Microservice

### 2.7. React.js Modern Frontend Development

#### 2.7.1. Module 1 — React Fundamentals

1. **What Is React and Why**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Create React App and Vite**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **JSX Syntax**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Functional Components**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Props and PropTypes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.7.2. Module 2 — React Fundamentals & JSX

1. **Introduction to Modern Single Page Applications**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Introduction to Modern Single Page Applications
    2. Core Concept
        - Core Concept: Introduction to Modern Single Page Applications
    3. Syntax
        - Syntax: Introduction to Modern Single Page Applications
    4. Example
        - Example: Introduction to Modern Single Page Applications
    5. Pitfall
        - Pitfall: Introduction to Modern Single Page Applications
    6. Q & A
        - Q & A: Introduction to Modern Single Page Applications
2. **Setting up React with Vite**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Setting up React with Vite
    2. Core Concept
        - Core Concept: Setting up React with Vite
    3. Syntax
        - Syntax: Setting up React with Vite
    4. Example
        - Example: Setting up React with Vite
    5. Pitfall
        - Pitfall: Setting up React with Vite
    6. Q & A
        - Q & A: Setting up React with Vite
3. **JSX Syntax & Virtual DOM Mechanics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: JSX Syntax & Virtual DOM Mechanics
    2. Core Concept
        - Core Concept: JSX Syntax & Virtual DOM Mechanics
    3. Syntax
        - Syntax: JSX Syntax & Virtual DOM Mechanics
    4. Example
        - Example: JSX Syntax & Virtual DOM Mechanics
    5. Pitfall
        - Pitfall: JSX Syntax & Virtual DOM Mechanics
    6. Q & A
        - Q & A: JSX Syntax & Virtual DOM Mechanics
4. **Functional Components & Props**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Functional Components & Props
    2. Core Concept
        - Core Concept: Functional Components & Props
    3. Syntax
        - Syntax: Functional Components & Props
    4. Example
        - Example: Functional Components & Props
    5. Pitfall
        - Pitfall: Functional Components & Props
    6. Q & A
        - Q & A: Functional Components & Props
5. **Rendering Lists & Conditional Logic**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Rendering Lists & Conditional Logic
    2. Core Concept
        - Core Concept: Rendering Lists & Conditional Logic
    3. Syntax
        - Syntax: Rendering Lists & Conditional Logic
    4. Example
        - Example: Rendering Lists & Conditional Logic
    5. Pitfall
        - Pitfall: Rendering Lists & Conditional Logic
    6. Q & A
        - Q & A: Rendering Lists & Conditional Logic

#### 2.7.3. Module 3 — State Management & Hooks

1. **useState Hook for Local Component State**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: useState Hook for Local Component State
    2. Core Concept
        - Core Concept: useState Hook for Local Component State
    3. Syntax
        - Syntax: useState Hook for Local Component State
    4. Example
        - Example: useState Hook for Local Component State
    5. Pitfall
        - Pitfall: useState Hook for Local Component State
    6. Q & A
        - Q & A: useState Hook for Local Component State
2. **Handling Form Inputs & Synthetic Events**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Handling Form Inputs & Synthetic Events
    2. Core Concept
        - Core Concept: Handling Form Inputs & Synthetic Events
    3. Syntax
        - Syntax: Handling Form Inputs & Synthetic Events
    4. Example
        - Example: Handling Form Inputs & Synthetic Events
    5. Pitfall
        - Pitfall: Handling Form Inputs & Synthetic Events
    6. Q & A
        - Q & A: Handling Form Inputs & Synthetic Events
3. **useEffect Hook for Side Effects & Lifecycle**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: useEffect Hook for Side Effects & Lifecycle
    2. Core Concept
        - Core Concept: useEffect Hook for Side Effects & Lifecycle
    3. Syntax
        - Syntax: useEffect Hook for Side Effects & Lifecycle
    4. Example
        - Example: useEffect Hook for Side Effects & Lifecycle
    5. Pitfall
        - Pitfall: useEffect Hook for Side Effects & Lifecycle
    6. Q & A
        - Q & A: useEffect Hook for Side Effects & Lifecycle
4. **Custom Hooks Reusability**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Custom Hooks Reusability
    2. Core Concept
        - Core Concept: Custom Hooks Reusability
    3. Syntax
        - Syntax: Custom Hooks Reusability
    4. Example
        - Example: Custom Hooks Reusability
    5. Pitfall
        - Pitfall: Custom Hooks Reusability
    6. Q & A
        - Q & A: Custom Hooks Reusability
5. **useRef Hook for DOM References**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: useRef Hook for DOM References
    2. Core Concept
        - Core Concept: useRef Hook for DOM References
    3. Syntax
        - Syntax: useRef Hook for DOM References
    4. Example
        - Example: useRef Hook for DOM References
    5. Pitfall
        - Pitfall: useRef Hook for DOM References
    6. Q & A
        - Q & A: useRef Hook for DOM References

#### 2.7.4. Module 4 — State and Events

1. **useState Hook**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Event Handling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Controlled Components**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Lifting State Up**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Conditional Rendering**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.7.5. Module 5 — Component Patterns

1. **Lists and Keys**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Component Composition**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **useEffect Hook**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **useRef Hook**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Custom Hooks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.7.6. Module 6 — Component Communication & Context API

1. **Lifting State Up in Component Trees**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Lifting State Up in Component Trees
    2. Core Concept
        - Core Concept: Lifting State Up in Component Trees
    3. Syntax
        - Syntax: Lifting State Up in Component Trees
    4. Example
        - Example: Lifting State Up in Component Trees
    5. Pitfall
        - Pitfall: Lifting State Up in Component Trees
    6. Q & A
        - Q & A: Lifting State Up in Component Trees
2. **Prop Drilling & Clean Component Hierarchy**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Prop Drilling & Clean Component Hierarchy
    2. Core Concept
        - Core Concept: Prop Drilling & Clean Component Hierarchy
    3. Syntax
        - Syntax: Prop Drilling & Clean Component Hierarchy
    4. Example
        - Example: Prop Drilling & Clean Component Hierarchy
    5. Pitfall
        - Pitfall: Prop Drilling & Clean Component Hierarchy
    6. Q & A
        - Q & A: Prop Drilling & Clean Component Hierarchy
3. **React Context API for Global State**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: React Context API for Global State
    2. Core Concept
        - Core Concept: React Context API for Global State
    3. Syntax
        - Syntax: React Context API for Global State
    4. Example
        - Example: React Context API for Global State
    5. Pitfall
        - Pitfall: React Context API for Global State
    6. Q & A
        - Q & A: React Context API for Global State
4. **useContext Hook Pattern**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: useContext Hook Pattern
    2. Core Concept
        - Core Concept: useContext Hook Pattern
    3. Syntax
        - Syntax: useContext Hook Pattern
    4. Example
        - Example: useContext Hook Pattern
    5. Pitfall
        - Pitfall: useContext Hook Pattern
    6. Q & A
        - Q & A: useContext Hook Pattern
5. **useReducer for Complex State Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: useReducer for Complex State Management
    2. Core Concept
        - Core Concept: useReducer for Complex State Management
    3. Syntax
        - Syntax: useReducer for Complex State Management
    4. Example
        - Example: useReducer for Complex State Management
    5. Pitfall
        - Pitfall: useReducer for Complex State Management
    6. Q & A
        - Q & A: useReducer for Complex State Management

#### 2.7.7. Module 7 — Routing & API Integration

1. **Client-Side Routing with React Router v6**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Client-Side Routing with React Router v6
    2. Core Concept
        - Core Concept: Client-Side Routing with React Router v6
    3. Syntax
        - Syntax: Client-Side Routing with React Router v6
    4. Example
        - Example: Client-Side Routing with React Router v6
    5. Pitfall
        - Pitfall: Client-Side Routing with React Router v6
    6. Q & A
        - Q & A: Client-Side Routing with React Router v6
2. **Dynamic Route Parameters & Navigation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Dynamic Route Parameters & Navigation
    2. Core Concept
        - Core Concept: Dynamic Route Parameters & Navigation
    3. Syntax
        - Syntax: Dynamic Route Parameters & Navigation
    4. Example
        - Example: Dynamic Route Parameters & Navigation
    5. Pitfall
        - Pitfall: Dynamic Route Parameters & Navigation
    6. Q & A
        - Q & A: Dynamic Route Parameters & Navigation
3. **Fetching Data with Axios & Fetch API**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Fetching Data with Axios & Fetch API
    2. Core Concept
        - Core Concept: Fetching Data with Axios & Fetch API
    3. Syntax
        - Syntax: Fetching Data with Axios & Fetch API
    4. Example
        - Example: Fetching Data with Axios & Fetch API
    5. Pitfall
        - Pitfall: Fetching Data with Axios & Fetch API
    6. Q & A
        - Q & A: Fetching Data with Axios & Fetch API
4. **Handling Loading, Error, and Success UI States**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Handling Loading, Error, and Success UI States
    2. Core Concept
        - Core Concept: Handling Loading, Error, and Success UI States
    3. Syntax
        - Syntax: Handling Loading, Error, and Success UI States
    4. Example
        - Example: Handling Loading, Error, and Success UI States
    5. Pitfall
        - Pitfall: Handling Loading, Error, and Success UI States
    6. Q & A
        - Q & A: Handling Loading, Error, and Success UI States
5. **React Query / TanStack Query Overview**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: React Query / TanStack Query Overview
    2. Core Concept
        - Core Concept: React Query / TanStack Query Overview
    3. Syntax
        - Syntax: React Query / TanStack Query Overview
    4. Example
        - Example: React Query / TanStack Query Overview
    5. Pitfall
        - Pitfall: React Query / TanStack Query Overview
    6. Q & A
        - Q & A: React Query / TanStack Query Overview

#### 2.7.8. Module 8 — Advanced Hooks and Context

1. **useContext Hook**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **useReducer Hook**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **useMemo and useCallback**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Context vs Props**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Error Boundaries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.7.9. Module 9 — React Router

1. **React Router Setup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Dynamic Routes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Navigation and Redirects**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Protected Routes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Query Strings**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.7.10. Module 10 — Advanced Patterns & Optimization

1. **Performance Optimization (useMemo, useCallback)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Performance Optimization (useMemo, useCallback)
    2. Core Concept
        - Core Concept: Performance Optimization (useMemo, useCallback)
    3. Syntax
        - Syntax: Performance Optimization (useMemo, useCallback)
    4. Example
        - Example: Performance Optimization (useMemo, useCallback)
    5. Pitfall
        - Pitfall: Performance Optimization (useMemo, useCallback)
    6. Q & A
        - Q & A: Performance Optimization (useMemo, useCallback)
2. **React.memo for Component Memoization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: React.memo for Component Memoization
    2. Core Concept
        - Core Concept: React.memo for Component Memoization
    3. Syntax
        - Syntax: React.memo for Component Memoization
    4. Example
        - Example: React.memo for Component Memoization
    5. Pitfall
        - Pitfall: React.memo for Component Memoization
    6. Q & A
        - Q & A: React.memo for Component Memoization
3. **Code Splitting & Lazy Loading (React.lazy, Suspense)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Code Splitting & Lazy Loading (React.lazy, Suspense)
    2. Core Concept
        - Core Concept: Code Splitting & Lazy Loading (React.lazy, Suspense)
    3. Syntax
        - Syntax: Code Splitting & Lazy Loading (React.lazy, Suspense)
    4. Example
        - Example: Code Splitting & Lazy Loading (React.lazy, Suspense)
    5. Pitfall
        - Pitfall: Code Splitting & Lazy Loading (React.lazy, Suspense)
    6. Q & A
        - Q & A: Code Splitting & Lazy Loading (React.lazy, Suspense)
4. **Form Validation with React Hook Form & Zod**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Form Validation with React Hook Form & Zod
    2. Core Concept
        - Core Concept: Form Validation with React Hook Form & Zod
    3. Syntax
        - Syntax: Form Validation with React Hook Form & Zod
    4. Example
        - Example: Form Validation with React Hook Form & Zod
    5. Pitfall
        - Pitfall: Form Validation with React Hook Form & Zod
    6. Q & A
        - Q & A: Form Validation with React Hook Form & Zod
5. **Building a Complete Full Stack Python-React App UI**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Building a Complete Full Stack Python-React App UI
    2. Core Concept
        - Core Concept: Building a Complete Full Stack Python-React App UI
    3. Syntax
        - Syntax: Building a Complete Full Stack Python-React App UI
    4. Example
        - Example: Building a Complete Full Stack Python-React App UI
    5. Pitfall
        - Pitfall: Building a Complete Full Stack Python-React App UI
    6. Q & A
        - Q & A: Building a Complete Full Stack Python-React App UI

#### 2.7.11. Module 11 — API Integration

1. **Fetch API in React**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Axios in React**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **React Query Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Forms with React Hook Form**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Full CRUD with Flask API**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.7.12. Module 12 — Testing & Production Deployment

1. **Component Testing with Vitest & React Testing Library**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Component Testing with Vitest & React Testing Library
    2. Core Concept
        - Core Concept: Component Testing with Vitest & React Testing Library
    3. Syntax
        - Syntax: Component Testing with Vitest & React Testing Library
    4. Example
        - Example: Component Testing with Vitest & React Testing Library
    5. Pitfall
        - Pitfall: Component Testing with Vitest & React Testing Library
    6. Q & A
        - Q & A: Component Testing with Vitest & React Testing Library
2. **Building Production Distribution Bundles**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Building Production Distribution Bundles
    2. Core Concept
        - Core Concept: Building Production Distribution Bundles
    3. Syntax
        - Syntax: Building Production Distribution Bundles
    4. Example
        - Example: Building Production Distribution Bundles
    5. Pitfall
        - Pitfall: Building Production Distribution Bundles
    6. Q & A
        - Q & A: Building Production Distribution Bundles
3. **Deploying React App to Nginx & Vercel**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Deploying React App to Nginx & Vercel
    2. Core Concept
        - Core Concept: Deploying React App to Nginx & Vercel
    3. Syntax
        - Syntax: Deploying React App to Nginx & Vercel
    4. Example
        - Example: Deploying React App to Nginx & Vercel
    5. Pitfall
        - Pitfall: Deploying React App to Nginx & Vercel
    6. Q & A
        - Q & A: Deploying React App to Nginx & Vercel
4. **Handling Environment Variables in Frontend**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Handling Environment Variables in Frontend
    2. Core Concept
        - Core Concept: Handling Environment Variables in Frontend
    3. Syntax
        - Syntax: Handling Environment Variables in Frontend
    4. Example
        - Example: Handling Environment Variables in Frontend
    5. Pitfall
        - Pitfall: Handling Environment Variables in Frontend
    6. Q & A
        - Q & A: Handling Environment Variables in Frontend
5. **Frontend Security & XSS Prevention Best Practices**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Frontend Security & XSS Prevention Best Practices
    2. Core Concept
        - Core Concept: Frontend Security & XSS Prevention Best Practices
    3. Syntax
        - Syntax: Frontend Security & XSS Prevention Best Practices
    4. Example
        - Example: Frontend Security & XSS Prevention Best Practices
    5. Pitfall
        - Pitfall: Frontend Security & XSS Prevention Best Practices
    6. Q & A
        - Q & A: Frontend Security & XSS Prevention Best Practices

### 2.8. Postman / API Testing

#### 2.8.1. Module 1 — Postman Fundamentals

1. **What Is Postman**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Sending Requests**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Environments and Variables**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Authentication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Request Chaining**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.8.2. Module 2 — Writing Tests

1. **Postman Test Scripts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Status Code Assertions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Response Body Assertions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Collections and Test Suites**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Newman CLI**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.8.3. Module 3 — API Testing Workflow

1. **Testing REST APIs End-to-End**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Mock Servers in Postman**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **API Documentation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **CI Integration with Newman**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **API Testing Best Practices**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

### 2.9. Selenium

#### 2.9.1. Module 1 — Selenium 4.x Architecture & Locators

1. **Lesson 1.2 Selenium 4.x Relative Locators**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview & Learning Objectives
        - Learning Objectives
    2. Environment & Prerequisites
    3. Theoretical Foundations
        - Spatial Locating in Selenium 4
    4. Architecture & Diagram Visualizations
    5. Code & Hardware Implementation
    6. Enterprise Real-World Applications
    7. Guided Step-by-Step Hands-On Exercise
    8. Common Pitfalls & Troubleshooting
    9. Best Practices & Optimization
    10. Industry Interview Q&A
        - Q1: How do Relative Locators in Selenium 4 calculate element positions?
    11. Self-Assessment Quiz
    12. Portfolio Assignment & Challenge
    13. Spaced Repetition Flashcards
    14. Summary & Cheat Sheet

#### 2.9.2. Module 2 — Selenium Fundamentals

1. **Selenium Introduction and Setup**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is Selenium?
        - Selenium Suite Components
    2. Installation
    3. First Script
    4. Browser Options
    5. Lab Exercise
2. **WebDriver Core and Browser Control**
    - **Course Coverage:** 🟢 Covered in Class
    1. WebDriver Navigation
    2. Browser Properties
    3. Window Management
    4. Screenshots
    5. Cookies
    6. Execute Script
    7. Quit vs Close
    8. Lab Exercise
3. **Locator Strategies**
    - **Course Coverage:** 🟢 Covered in Class
    1. By Locator Types
    2. find_element vs find_elements
    3. Choosing the Right Locator
    4. Relative Locators (Selenium 4)
    5. Lab Exercise
4. **XPath and CSS Selectors**
    - **Course Coverage:** 🟢 Covered in Class
    1. CSS Selector Syntax
    2. XPath Syntax
    3. Practical Examples
    4. CSS vs XPath — When to Use
    5. Lab Exercise
5. **Web Element Interactions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Core Element Methods
    2. Special Keys
    3. CSS Properties and Dimensions
    4. Checkbox and Radio Buttons
    5. Lab Exercise

#### 2.9.3. Module 3 — Waits and Synchronisation

1. **Implicit and Explicit Waits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Why Waits Are Necessary
    2. Implicit Wait
    3. Explicit Wait (Recommended)
    4. Common Expected Conditions
    5. Custom Wait Condition
    6. Implicit vs Explicit
    7. Lab Exercise
2. **Fluent Waits and Custom Conditions**
    - **Course Coverage:** 🟢 Covered in Class
    1. FluentWait
    2. Custom Wait Conditions with Lambda
    3. Retry Decorator for Flaky Interactions
    4. Wait Until Page is Ready
    5. Lab Exercise
3. **Page Load Strategies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Page Load Strategies
    2. Timeouts Configuration
    3. Handling Slow AJAX Pages
    4. Lab Exercise

#### 2.9.4. Module 4 — Advanced Interactions

1. **Action Chains**
    - **Course Coverage:** 🟢 Covered in Class
    1. ActionChains Overview
    2. Mouse Actions
    3. Drag and Drop
    4. Keyboard Actions
    5. Chaining Actions
    6. Lab Exercise
2. **Dropdown and Select Handling**
    - **Course Coverage:** 🟢 Covered in Class
    1. HTML Select Dropdown
    2. Multi-Select Dropdown
    3. Custom Dropdown (not `<select>`)
    4. Lab Exercise
3. **Alerts Frames and Windows**
    - **Course Coverage:** 🟢 Covered in Class
    1. JavaScript Alerts
    2. iFrames
    3. Multiple Windows/Tabs
    4. Lab Exercise
4. **JavaScript Executor**
    - **Course Coverage:** 🟢 Covered in Class
    1. execute_script
    2. execute_async_script
    3. Shadow DOM
    4. Common Use Cases
    5. Lab Exercise
5. **File Upload and Download**
    - **Course Coverage:** 🟢 Covered in Class
    1. File Upload
    2. File Download Configuration
    3. Wait for Download to Complete
    4. Handling Native OS Dialogs
    5. Lab Exercise

#### 2.9.5. Module 5 — Test Architecture

1. **Page Object Model Pattern**
    - **Course Coverage:** 🟢 Covered in Class
    1. Why Page Object Model?
    2. Structure
    3. Base Page
    4. Page Object
    5. Test Using POM
    6. Lab Exercise
2. **Page Factory Pattern**
    - **Course Coverage:** 🟢 Covered in Class
    1. Page Factory — Composable Components
    2. Page that Composes Components
    3. ProductCard Component
    4. Lab Exercise
3. **Base Page and Utilities**
    - **Course Coverage:** 🟢 Covered in Class
    1. Enhanced Base Page
    2. conftest.py — Pytest Fixtures
    3. Lab Exercise

#### 2.9.6. Module 6 — Testing Framework Integration

1. **Pytest with Selenium**
    - **Course Coverage:** 🟢 Covered in Class
    1. Test Structure
    2. Fixtures Hierarchy
    3. Markers
    4. Allure Reporting
    5. Lab Exercise
2. **Test Configuration and Reporting**
    - **Course Coverage:** 🟢 Covered in Class
    1. pytest.ini / pyproject.toml
    2. HTML Report
    3. Parallel Execution with pytest-xdist
    4. Environment Configuration
    5. Lab Exercise
3. **Data Driven Testing**
    - **Course Coverage:** 🟢 Covered in Class
    1. pytest.mark.parametrize
    2. Reading Test Data from CSV
    3. Reading from Excel
    4. Generating Data with Faker
    5. Lab Exercise

#### 2.9.7. Module 7 — Advanced and CI

1. **Headless Browser Testing**
    - **Course Coverage:** 🟢 Covered in Class
    1. What is Headless?
    2. Chrome Headless
    3. Firefox Headless
    4. Headless with Virtual Display (Linux)
    5. Lab Exercise
2. **Selenium Grid**
    - **Course Coverage:** 🟢 Covered in Class
    1. Selenium Grid Architecture
    2. Standalone Grid (Single Node)
    3. Remote WebDriver
    4. Docker Selenium Grid
    5. Lab Exercise
3. **CI/CD Integration**
    - **Course Coverage:** 🟢 Covered in Class
    1. GitHub Actions Workflow
    2. Jenkins Pipeline (Declarative)
    3. Lab Exercise
4. **Screenshot and Visual Testing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Screenshot Capture
    2. Basic Image Comparison with Pillow
    3. Lab Exercise
5. **Capstone E-Commerce Automation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Project Overview
    2. Project Structure
    3. Key Test Scenarios
    4. Deliverables
    5. Lab Exercise

### 2.10. Playwright

#### 2.10.1. Module 1 — Playwright Fundamentals

1. **What Is Playwright**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Playwright Setup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Browser and Page Objects**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Locators and Selectors**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Basic Interactions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.10.2. Module 2 — Test Writing

1. **Test Structure**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Assertions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Page Object Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Test Fixtures**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **API Testing with Playwright**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.10.3. Module 3 — Advanced Playwright

1. **Network Interception**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Screenshot and Video**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Parallel Test Execution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **CI with GitHub Actions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Playwright Reports**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

### 2.11. Linux Systems & Administration

#### 2.11.1. Module 1 — Linux Fundamentals

1. **What Is Linux and Distributions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **File System Hierarchy**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Basic Commands**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **File Permissions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Users and Groups**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.11.2. Module 2 — Linux Basics & Navigation

1. **Linux Operating System Architecture & Shell**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Linux Operating System Architecture & Shell
    2. Core Concept
        - Core Concept: Linux Operating System Architecture & Shell
    3. Syntax
        - Syntax: Linux Operating System Architecture & Shell
    4. Example
        - Example: Linux Operating System Architecture & Shell
    5. Pitfall
        - Pitfall: Linux Operating System Architecture & Shell
    6. Q & A
        - Q & A: Linux Operating System Architecture & Shell
2. **Navigating Filesystem (ls, cd, pwd, tree)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Navigating Filesystem (ls, cd, pwd, tree)
    2. Overview
        - Overview: Navigating Filesystem (ls, cd, pwd, tree)
    3. Core Concept
        - Core Concept: Navigating Filesystem (ls, cd, pwd, tree)
    4. Core Concept
        - Core Concept: Navigating Filesystem (ls, cd, pwd, tree)
    5. Syntax
        - Syntax: Navigating Filesystem (ls, cd, pwd, tree)
    6. Syntax
        - Syntax: Navigating Filesystem (ls, cd, pwd, tree)
    7. Example
        - Example: Navigating Filesystem (ls, cd, pwd, tree)
    8. Example
        - Example: Navigating Filesystem (ls, cd, pwd, tree)
    9. Pitfall
        - Pitfall: Navigating Filesystem (ls, cd, pwd, tree)
    10. Pitfall
        - Pitfall: Navigating Filesystem (ls, cd, pwd, tree)
    11. Q & A
        - Q & A: Navigating Filesystem (ls, cd, pwd, tree)
    12. Q & A
        - Q & A: Navigating Filesystem (ls, cd, pwd, tree)
3. **File Operations (cp, mv, rm, mkdir, touch)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: File Operations (cp, mv, rm, mkdir, touch)
    2. Overview
        - Overview: File Operations (cp, mv, rm, mkdir, touch)
    3. Core Concept
        - Core Concept: File Operations (cp, mv, rm, mkdir, touch)
    4. Core Concept
        - Core Concept: File Operations (cp, mv, rm, mkdir, touch)
    5. Syntax
        - Syntax: File Operations (cp, mv, rm, mkdir, touch)
    6. Syntax
        - Syntax: File Operations (cp, mv, rm, mkdir, touch)
    7. Example
        - Example: File Operations (cp, mv, rm, mkdir, touch)
    8. Example
        - Example: File Operations (cp, mv, rm, mkdir, touch)
    9. Pitfall
        - Pitfall: File Operations (cp, mv, rm, mkdir, touch)
    10. Pitfall
        - Pitfall: File Operations (cp, mv, rm, mkdir, touch)
    11. Q & A
        - Q & A: File Operations (cp, mv, rm, mkdir, touch)
    12. Q & A
        - Q & A: File Operations (cp, mv, rm, mkdir, touch)
4. **Reading Files (cat, less, head, tail)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Reading Files (cat, less, head, tail)
    2. Core Concept
        - Core Concept: Reading Files (cat, less, head, tail)
    3. Syntax
        - Syntax: Reading Files (cat, less, head, tail)
    4. Example
        - Example: Reading Files (cat, less, head, tail)
    5. Pitfall
        - Pitfall: Reading Files (cat, less, head, tail)
    6. Q & A
        - Q & A: Reading Files (cat, less, head, tail)
5. **File Searching (find, locate, grep)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: File Searching (find, locate, grep)
    2. Core Concept
        - Core Concept: File Searching (find, locate, grep)
    3. Syntax
        - Syntax: File Searching (find, locate, grep)
    4. Example
        - Example: File Searching (find, locate, grep)
    5. Pitfall
        - Pitfall: File Searching (find, locate, grep)
    6. Q & A
        - Q & A: File Searching (find, locate, grep)

#### 2.11.3. Module 3 — Shell and Navigation

1. **Shell Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **File Viewing and Searching**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Pipes and Redirection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Text Processing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Wildcards and Globbing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.11.4. Module 4 — Permissions, Users & Groups

1. **Understanding Linux File Permissions (chmod)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Understanding Linux File Permissions (chmod)
    2. Core Concept
        - Core Concept: Understanding Linux File Permissions (chmod)
    3. Syntax
        - Syntax: Understanding Linux File Permissions (chmod)
    4. Example
        - Example: Understanding Linux File Permissions (chmod)
    5. Pitfall
        - Pitfall: Understanding Linux File Permissions (chmod)
    6. Q & A
        - Q & A: Understanding Linux File Permissions (chmod)
2. **File Ownership & Group Management (chown, chgrp)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: File Ownership & Group Management (chown, chgrp)
    2. Core Concept
        - Core Concept: File Ownership & Group Management (chown, chgrp)
    3. Syntax
        - Syntax: File Ownership & Group Management (chown, chgrp)
    4. Example
        - Example: File Ownership & Group Management (chown, chgrp)
    5. Pitfall
        - Pitfall: File Ownership & Group Management (chown, chgrp)
    6. Q & A
        - Q & A: File Ownership & Group Management (chown, chgrp)
3. **User Administration (useradd, usermod, passwd)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: User Administration (useradd, usermod, passwd)
    2. Core Concept
        - Core Concept: User Administration (useradd, usermod, passwd)
    3. Syntax
        - Syntax: User Administration (useradd, usermod, passwd)
    4. Example
        - Example: User Administration (useradd, usermod, passwd)
    5. Pitfall
        - Pitfall: User Administration (useradd, usermod, passwd)
    6. Q & A
        - Q & A: User Administration (useradd, usermod, passwd)
4. **Sudo Access & Privileged Execution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Sudo Access & Privileged Execution
    2. Core Concept
        - Core Concept: Sudo Access & Privileged Execution
    3. Syntax
        - Syntax: Sudo Access & Privileged Execution
    4. Example
        - Example: Sudo Access & Privileged Execution
    5. Pitfall
        - Pitfall: Sudo Access & Privileged Execution
    6. Q & A
        - Q & A: Sudo Access & Privileged Execution
5. **File System Hierarchy Standard (FHS)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: File System Hierarchy Standard (FHS)
    2. Core Concept
        - Core Concept: File System Hierarchy Standard (FHS)
    3. Syntax
        - Syntax: File System Hierarchy Standard (FHS)
    4. Example
        - Example: File System Hierarchy Standard (FHS)
    5. Pitfall
        - Pitfall: File System Hierarchy Standard (FHS)
    6. Q & A
        - Q & A: File System Hierarchy Standard (FHS)

#### 2.11.5. Module 5 — Process & Resource Management

1. **Viewing Processes (ps, top, htop)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Viewing Processes (ps, top, htop)
    2. Core Concept
        - Core Concept: Viewing Processes (ps, top, htop)
    3. Syntax
        - Syntax: Viewing Processes (ps, top, htop)
    4. Example
        - Example: Viewing Processes (ps, top, htop)
    5. Pitfall
        - Pitfall: Viewing Processes (ps, top, htop)
    6. Q & A
        - Q & A: Viewing Processes (ps, top, htop)
2. **Managing Process Signal Handling (kill, pkill)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Managing Process Signal Handling (kill, pkill)
    2. Core Concept
        - Core Concept: Managing Process Signal Handling (kill, pkill)
    3. Syntax
        - Syntax: Managing Process Signal Handling (kill, pkill)
    4. Example
        - Example: Managing Process Signal Handling (kill, pkill)
    5. Pitfall
        - Pitfall: Managing Process Signal Handling (kill, pkill)
    6. Q & A
        - Q & A: Managing Process Signal Handling (kill, pkill)
3. **Background & Foreground Jobs (bg, fg, &)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Background & Foreground Jobs (bg, fg, &)
    2. Core Concept
        - Core Concept: Background & Foreground Jobs (bg, fg, &)
    3. Syntax
        - Syntax: Background & Foreground Jobs (bg, fg, &)
    4. Example
        - Example: Background & Foreground Jobs (bg, fg, &)
    5. Pitfall
        - Pitfall: Background & Foreground Jobs (bg, fg, &)
    6. Q & A
        - Q & A: Background & Foreground Jobs (bg, fg, &)
4. **Memory & Disk Space Auditing (free, df, du)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Memory & Disk Space Auditing (free, df, du)
    2. Core Concept
        - Core Concept: Memory & Disk Space Auditing (free, df, du)
    3. Syntax
        - Syntax: Memory & Disk Space Auditing (free, df, du)
    4. Example
        - Example: Memory & Disk Space Auditing (free, df, du)
    5. Pitfall
        - Pitfall: Memory & Disk Space Auditing (free, df, du)
    6. Q & A
        - Q & A: Memory & Disk Space Auditing (free, df, du)
5. **System Monitoring & Log Inspection (journalctl)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: System Monitoring & Log Inspection (journalctl)
    2. Core Concept
        - Core Concept: System Monitoring & Log Inspection (journalctl)
    3. Syntax
        - Syntax: System Monitoring & Log Inspection (journalctl)
    4. Example
        - Example: System Monitoring & Log Inspection (journalctl)
    5. Pitfall
        - Pitfall: System Monitoring & Log Inspection (journalctl)
    6. Q & A
        - Q & A: System Monitoring & Log Inspection (journalctl)

#### 2.11.6. Module 6 — Process Management

1. **Processes and Jobs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Systemd Services**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Cron Jobs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Log Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **System Monitoring**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.11.7. Module 7 — Networking

1. **Network Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Network Tools**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **SSH**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Firewall with UFW/iptables**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **DNS and /etc/hosts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.11.8. Module 8 — Networking & Systemd Services

1. **Network Interfaces & Troubleshooting (ip, ping, netstat, ss)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Network Interfaces & Troubleshooting (ip, ping, netstat, ss)
    2. Overview
        - Overview: Network Interfaces & Troubleshooting (ip, ping, netstat, ss)
    3. Core Concept
        - Core Concept: Network Interfaces & Troubleshooting (ip, ping, netstat, ss)
    4. Core Concept
        - Core Concept: Network Interfaces & Troubleshooting (ip, ping, netstat, ss)
    5. Syntax
        - Syntax: Network Interfaces & Troubleshooting (ip, ping, netstat, ss)
    6. Syntax
        - Syntax: Network Interfaces & Troubleshooting (ip, ping, netstat, ss)
    7. Example
        - Example: Network Interfaces & Troubleshooting (ip, ping, netstat, ss)
    8. Example
        - Example: Network Interfaces & Troubleshooting (ip, ping, netstat, ss)
    9. Pitfall
        - Pitfall: Network Interfaces & Troubleshooting (ip, ping, netstat, ss)
    10. Pitfall
        - Pitfall: Network Interfaces & Troubleshooting (ip, ping, netstat, ss)
    11. Q & A
        - Q & A: Network Interfaces & Troubleshooting (ip, ping, netstat, ss)
    12. Q & A
        - Q & A: Network Interfaces & Troubleshooting (ip, ping, netstat, ss)
2. **Downloading & Transferring Files (curl, wget, scp)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Downloading & Transferring Files (curl, wget, scp)
    2. Overview
        - Overview: Downloading & Transferring Files (curl, wget, scp)
    3. Core Concept
        - Core Concept: Downloading & Transferring Files (curl, wget, scp)
    4. Core Concept
        - Core Concept: Downloading & Transferring Files (curl, wget, scp)
    5. Syntax
        - Syntax: Downloading & Transferring Files (curl, wget, scp)
    6. Syntax
        - Syntax: Downloading & Transferring Files (curl, wget, scp)
    7. Example
        - Example: Downloading & Transferring Files (curl, wget, scp)
    8. Example
        - Example: Downloading & Transferring Files (curl, wget, scp)
    9. Pitfall
        - Pitfall: Downloading & Transferring Files (curl, wget, scp)
    10. Pitfall
        - Pitfall: Downloading & Transferring Files (curl, wget, scp)
    11. Q & A
        - Q & A: Downloading & Transferring Files (curl, wget, scp)
    12. Q & A
        - Q & A: Downloading & Transferring Files (curl, wget, scp)
3. **SSH Remote Access & Key Authentication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: SSH Remote Access & Key Authentication
    2. Overview
        - Overview: SSH Remote Access & Key Authentication
    3. Core Concept
        - Core Concept: SSH Remote Access & Key Authentication
    4. Core Concept
        - Core Concept: SSH Remote Access & Key Authentication
    5. Syntax
        - Syntax: SSH Remote Access & Key Authentication
    6. Syntax
        - Syntax: SSH Remote Access & Key Authentication
    7. Example
        - Example: SSH Remote Access & Key Authentication
    8. Example
        - Example: SSH Remote Access & Key Authentication
    9. Pitfall
        - Pitfall: SSH Remote Access & Key Authentication
    10. Pitfall
        - Pitfall: SSH Remote Access & Key Authentication
    11. Q & A
        - Q & A: SSH Remote Access & Key Authentication
    12. Q & A
        - Q & A: SSH Remote Access & Key Authentication
4. **Writing Custom Systemd Service Files**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Writing Custom Systemd Service Files
    2. Overview
        - Overview: Writing Custom Systemd Service Files
    3. Core Concept
        - Core Concept: Writing Custom Systemd Service Files
    4. Core Concept
        - Core Concept: Writing Custom Systemd Service Files
    5. Syntax
        - Syntax: Writing Custom Systemd Service Files
    6. Syntax
        - Syntax: Writing Custom Systemd Service Files
    7. Example
        - Example: Writing Custom Systemd Service Files
    8. Example
        - Example: Writing Custom Systemd Service Files
    9. Pitfall
        - Pitfall: Writing Custom Systemd Service Files
    10. Pitfall
        - Pitfall: Writing Custom Systemd Service Files
    11. Q & A
        - Q & A: Writing Custom Systemd Service Files
    12. Q & A
        - Q & A: Writing Custom Systemd Service Files
5. **Managing System Services (systemctl start, stop, enable)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Managing System Services (systemctl start, stop, enable)
    2. Overview
        - Overview: Managing System Services (systemctl start, stop, enable)
    3. Core Concept
        - Core Concept: Managing System Services (systemctl start, stop, enable)
    4. Core Concept
        - Core Concept: Managing System Services (systemctl start, stop, enable)
    5. Syntax
        - Syntax: Managing System Services (systemctl start, stop, enable)
    6. Syntax
        - Syntax: Managing System Services (systemctl start, stop, enable)
    7. Example
        - Example: Managing System Services (systemctl start, stop, enable)
    8. Example
        - Example: Managing System Services (systemctl start, stop, enable)
    9. Pitfall
        - Pitfall: Managing System Services (systemctl start, stop, enable)
    10. Pitfall
        - Pitfall: Managing System Services (systemctl start, stop, enable)
    11. Q & A
        - Q & A: Managing System Services (systemctl start, stop, enable)
    12. Q & A
        - Q & A: Managing System Services (systemctl start, stop, enable)

#### 2.11.9. Module 9 — Package and System Management

1. **APT Package Manager**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **YUM and DNF**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Environment Variables**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Disk Management**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Linux Security Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.11.10. Module 10 — Shell Scripting & Automation

1. **Introduction to Bash Shell Scripting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Introduction to Bash Shell Scripting
    2. Overview
        - Overview: Introduction to Bash Shell Scripting
    3. Core Concept
        - Core Concept: Introduction to Bash Shell Scripting
    4. Core Concept
        - Core Concept: Introduction to Bash Shell Scripting
    5. Syntax
        - Syntax: Introduction to Bash Shell Scripting
    6. Syntax
        - Syntax: Introduction to Bash Shell Scripting
    7. Example
        - Example: Introduction to Bash Shell Scripting
    8. Example
        - Example: Introduction to Bash Shell Scripting
    9. Pitfall
        - Pitfall: Introduction to Bash Shell Scripting
    10. Pitfall
        - Pitfall: Introduction to Bash Shell Scripting
    11. Q & A
        - Q & A: Introduction to Bash Shell Scripting
    12. Q & A
        - Q & A: Introduction to Bash Shell Scripting
2. **Variables, Arguments, and Input**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Variables, Arguments, and Input
    2. Overview
        - Overview: Variables, Arguments, and Input
    3. Core Concept
        - Core Concept: Variables, Arguments, and Input
    4. Core Concept
        - Core Concept: Variables, Arguments, and Input
    5. Syntax
        - Syntax: Variables, Arguments, and Input
    6. Syntax
        - Syntax: Variables, Arguments, and Input
    7. Example
        - Example: Variables, Arguments, and Input
    8. Example
        - Example: Variables, Arguments, and Input
    9. Pitfall
        - Pitfall: Variables, Arguments, and Input
    10. Pitfall
        - Pitfall: Variables, Arguments, and Input
    11. Q & A
        - Q & A: Variables, Arguments, and Input
    12. Q & A
        - Q & A: Variables, Arguments, and Input
3. **Control Flow (if, case, loops)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Control Flow (if, case, loops)
    2. Overview
        - Overview: Control Flow (if, case, loops)
    3. Core Concept
        - Core Concept: Control Flow (if, case, loops)
    4. Core Concept
        - Core Concept: Control Flow (if, case, loops)
    5. Syntax
        - Syntax: Control Flow (if, case, loops)
    6. Syntax
        - Syntax: Control Flow (if, case, loops)
    7. Example
        - Example: Control Flow (if, case, loops)
    8. Example
        - Example: Control Flow (if, case, loops)
    9. Pitfall
        - Pitfall: Control Flow (if, case, loops)
    10. Pitfall
        - Pitfall: Control Flow (if, case, loops)
    11. Q & A
        - Q & A: Control Flow (if, case, loops)
    12. Q & A
        - Q & A: Control Flow (if, case, loops)
4. **Scheduling Tasks with Cron & Crontab**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Scheduling Tasks with Cron & Crontab
    2. Overview
        - Overview: Scheduling Tasks with Cron & Crontab
    3. Core Concept
        - Core Concept: Scheduling Tasks with Cron & Crontab
    4. Core Concept
        - Core Concept: Scheduling Tasks with Cron & Crontab
    5. Syntax
        - Syntax: Scheduling Tasks with Cron & Crontab
    6. Syntax
        - Syntax: Scheduling Tasks with Cron & Crontab
    7. Example
        - Example: Scheduling Tasks with Cron & Crontab
    8. Example
        - Example: Scheduling Tasks with Cron & Crontab
    9. Pitfall
        - Pitfall: Scheduling Tasks with Cron & Crontab
    10. Pitfall
        - Pitfall: Scheduling Tasks with Cron & Crontab
    11. Q & A
        - Q & A: Scheduling Tasks with Cron & Crontab
    12. Q & A
        - Q & A: Scheduling Tasks with Cron & Crontab
5. **Automating Server Maintenance Scripts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Automating Server Maintenance Scripts
    2. Overview
        - Overview: Automating Server Maintenance Scripts
    3. Core Concept
        - Core Concept: Automating Server Maintenance Scripts
    4. Core Concept
        - Core Concept: Automating Server Maintenance Scripts
    5. Syntax
        - Syntax: Automating Server Maintenance Scripts
    6. Syntax
        - Syntax: Automating Server Maintenance Scripts
    7. Example
        - Example: Automating Server Maintenance Scripts
    8. Example
        - Example: Automating Server Maintenance Scripts
    9. Pitfall
        - Pitfall: Automating Server Maintenance Scripts
    10. Pitfall
        - Pitfall: Automating Server Maintenance Scripts
    11. Q & A
        - Q & A: Automating Server Maintenance Scripts
    12. Q & A
        - Q & A: Automating Server Maintenance Scripts

### 2.12. Bash Scripting

#### 2.12.1. Module 1 — Bash Fundamentals

1. **What Is Bash**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Writing Your First Script**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Variables and Data Types**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Input and Output**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Special Variables**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.12.2. Module 2 — Control Flow

1. **Conditionals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Loops**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Case Statements**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Error Handling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.12.3. Module 3 — Bash Automation

1. **Text Processing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **File Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Cron Jobs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Script Debugging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Practical Automation Scripts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
### 2.13. Docker & Containerization

#### 2.13.1. Module 1 — Docker Fundamentals

1. **What Is Docker and Why Containers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Installing Docker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Docker Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Running Your First Container**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Docker CLI Essentials**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.13.2. Module 2 — Docker Fundamentals

1. **Introduction to Containerization vs VMs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Introduction to Containerization vs VMs
    2. Core Concept
        - Core Concept: Introduction to Containerization vs VMs
    3. Syntax
        - Syntax: Introduction to Containerization vs VMs
    4. Example
        - Example: Introduction to Containerization vs VMs
    5. Pitfall
        - Pitfall: Introduction to Containerization vs VMs
    6. Q & A
        - Q & A: Introduction to Containerization vs VMs
2. **Installing Docker Engine & Desktop**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Installing Docker Engine & Desktop
    2. Core Concept
        - Core Concept: Installing Docker Engine & Desktop
    3. Syntax
        - Syntax: Installing Docker Engine & Desktop
    4. Example
        - Example: Installing Docker Engine & Desktop
    5. Pitfall
        - Pitfall: Installing Docker Engine & Desktop
    6. Q & A
        - Q & A: Installing Docker Engine & Desktop
3. **Docker Architecture & Daemon**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Docker Architecture & Daemon
    2. Core Concept
        - Core Concept: Docker Architecture & Daemon
    3. Syntax
        - Syntax: Docker Architecture & Daemon
    4. Example
        - Example: Docker Architecture & Daemon
    5. Pitfall
        - Pitfall: Docker Architecture & Daemon
    6. Q & A
        - Q & A: Docker Architecture & Daemon
4. **Working with Docker CLI Commands**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Working with Docker CLI Commands
    2. Core Concept
        - Core Concept: Working with Docker CLI Commands
    3. Syntax
        - Syntax: Working with Docker CLI Commands
    4. Example
        - Example: Working with Docker CLI Commands
    5. Pitfall
        - Pitfall: Working with Docker CLI Commands
    6. Q & A
        - Q & A: Working with Docker CLI Commands
5. **Understanding Docker Images & Registries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Understanding Docker Images & Registries
    2. Core Concept
        - Core Concept: Understanding Docker Images & Registries
    3. Syntax
        - Syntax: Understanding Docker Images & Registries
    4. Example
        - Example: Understanding Docker Images & Registries
    5. Pitfall
        - Pitfall: Understanding Docker Images & Registries
    6. Q & A
        - Q & A: Understanding Docker Images & Registries

#### 2.13.3. Module 3 — Docker Images

1. **Dockerfile Syntax**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Building Images**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Multi-Stage Builds**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Pushing to Docker Hub**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Image Best Practices**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.13.4. Module 4 — Dockerfiles & Custom Images

1. **Writing your First Dockerfile**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Writing your First Dockerfile
    2. Core Concept
        - Core Concept: Writing your First Dockerfile
    3. Syntax
        - Syntax: Writing your First Dockerfile
    4. Example
        - Example: Writing your First Dockerfile
    5. Pitfall
        - Pitfall: Writing your First Dockerfile
    6. Q & A
        - Q & A: Writing your First Dockerfile
2. **FROM, RUN, CMD, and ENTRYPOINT Directives**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: FROM, RUN, CMD, and ENTRYPOINT Directives
    2. Core Concept
        - Core Concept: FROM, RUN, CMD, and ENTRYPOINT Directives
    3. Syntax
        - Syntax: FROM, RUN, CMD, and ENTRYPOINT Directives
    4. Example
        - Example: FROM, RUN, CMD, and ENTRYPOINT Directives
    5. Pitfall
        - Pitfall: FROM, RUN, CMD, and ENTRYPOINT Directives
    6. Q & A
        - Q & A: FROM, RUN, CMD, and ENTRYPOINT Directives
3. **Managing Image Layers & Caching**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Managing Image Layers & Caching
    2. Core Concept
        - Core Concept: Managing Image Layers & Caching
    3. Syntax
        - Syntax: Managing Image Layers & Caching
    4. Example
        - Example: Managing Image Layers & Caching
    5. Pitfall
        - Pitfall: Managing Image Layers & Caching
    6. Q & A
        - Q & A: Managing Image Layers & Caching
4. **Multi-Stage Docker Builds**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Multi-Stage Docker Builds
    2. Core Concept
        - Core Concept: Multi-Stage Docker Builds
    3. Syntax
        - Syntax: Multi-Stage Docker Builds
    4. Example
        - Example: Multi-Stage Docker Builds
    5. Pitfall
        - Pitfall: Multi-Stage Docker Builds
    6. Q & A
        - Q & A: Multi-Stage Docker Builds
5. **Optimizing Dockerfile Size & Security**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Optimizing Dockerfile Size & Security
    2. Core Concept
        - Core Concept: Optimizing Dockerfile Size & Security
    3. Syntax
        - Syntax: Optimizing Dockerfile Size & Security
    4. Example
        - Example: Optimizing Dockerfile Size & Security
    5. Pitfall
        - Pitfall: Optimizing Dockerfile Size & Security
    6. Q & A
        - Q & A: Optimizing Dockerfile Size & Security

#### 2.13.5. Module 5 — Containers

1. **Container Lifecycle**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Port Mapping and Volumes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Environment Variables**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Container Networking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Logging and Debugging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.13.6. Module 6 — Docker Networking & Storage

1. **Docker Volumes & Bind Mounts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Docker Volumes & Bind Mounts
    2. Core Concept
        - Core Concept: Docker Volumes & Bind Mounts
    3. Syntax
        - Syntax: Docker Volumes & Bind Mounts
    4. Example
        - Example: Docker Volumes & Bind Mounts
    5. Pitfall
        - Pitfall: Docker Volumes & Bind Mounts
    6. Q & A
        - Q & A: Docker Volumes & Bind Mounts
2. **Persisting Database Data in Docker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Persisting Database Data in Docker
    2. Core Concept
        - Core Concept: Persisting Database Data in Docker
    3. Syntax
        - Syntax: Persisting Database Data in Docker
    4. Example
        - Example: Persisting Database Data in Docker
    5. Pitfall
        - Pitfall: Persisting Database Data in Docker
    6. Q & A
        - Q & A: Persisting Database Data in Docker
3. **Docker Bridge, Host, and Overlay Networks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Docker Bridge, Host, and Overlay Networks
    2. Core Concept
        - Core Concept: Docker Bridge, Host, and Overlay Networks
    3. Syntax
        - Syntax: Docker Bridge, Host, and Overlay Networks
    4. Example
        - Example: Docker Bridge, Host, and Overlay Networks
    5. Pitfall
        - Pitfall: Docker Bridge, Host, and Overlay Networks
    6. Q & A
        - Q & A: Docker Bridge, Host, and Overlay Networks
4. **Container Port Mapping & Communication**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Container Port Mapping & Communication
    2. Core Concept
        - Core Concept: Container Port Mapping & Communication
    3. Syntax
        - Syntax: Container Port Mapping & Communication
    4. Example
        - Example: Container Port Mapping & Communication
    5. Pitfall
        - Pitfall: Container Port Mapping & Communication
    6. Q & A
        - Q & A: Container Port Mapping & Communication
5. **Container Inspection & Logging**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Container Inspection & Logging
    2. Core Concept
        - Core Concept: Container Inspection & Logging
    3. Syntax
        - Syntax: Container Inspection & Logging
    4. Example
        - Example: Container Inspection & Logging
    5. Pitfall
        - Pitfall: Container Inspection & Logging
    6. Q & A
        - Q & A: Container Inspection & Logging

#### 2.13.7. Module 7 — Docker Compose

1. **Docker Compose Overview**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Writing docker-compose.yml**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Multi-Service Applications**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Compose Networking**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Compose Commands**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.13.8. Module 8 — Multi-Container Apps with Docker Compose

1. **Introduction to docker-compose.yml**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Introduction to docker-compose.yml
    2. Core Concept
        - Core Concept: Introduction to docker-compose.yml
    3. Syntax
        - Syntax: Introduction to docker-compose.yml
    4. Example
        - Example: Introduction to docker-compose.yml
    5. Pitfall
        - Pitfall: Introduction to docker-compose.yml
    6. Q & A
        - Q & A: Introduction to docker-compose.yml
2. **Defining Services, Networks, and Volumes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Defining Services, Networks, and Volumes
    2. Core Concept
        - Core Concept: Defining Services, Networks, and Volumes
    3. Syntax
        - Syntax: Defining Services, Networks, and Volumes
    4. Example
        - Example: Defining Services, Networks, and Volumes
    5. Pitfall
        - Pitfall: Defining Services, Networks, and Volumes
    6. Q & A
        - Q & A: Defining Services, Networks, and Volumes
3. **Environment Variables & Configuration**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Environment Variables & Configuration
    2. Core Concept
        - Core Concept: Environment Variables & Configuration
    3. Syntax
        - Syntax: Environment Variables & Configuration
    4. Example
        - Example: Environment Variables & Configuration
    5. Pitfall
        - Pitfall: Environment Variables & Configuration
    6. Q & A
        - Q & A: Environment Variables & Configuration
4. **Orchestrating Python Web App + Database**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Orchestrating Python Web App + Database
    2. Core Concept
        - Core Concept: Orchestrating Python Web App + Database
    3. Syntax
        - Syntax: Orchestrating Python Web App + Database
    4. Example
        - Example: Orchestrating Python Web App + Database
    5. Pitfall
        - Pitfall: Orchestrating Python Web App + Database
    6. Q & A
        - Q & A: Orchestrating Python Web App + Database
5. **Docker Compose Commands & Lifecycle**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Docker Compose Commands & Lifecycle
    2. Core Concept
        - Core Concept: Docker Compose Commands & Lifecycle
    3. Syntax
        - Syntax: Docker Compose Commands & Lifecycle
    4. Example
        - Example: Docker Compose Commands & Lifecycle
    5. Pitfall
        - Pitfall: Docker Compose Commands & Lifecycle
    6. Q & A
        - Q & A: Docker Compose Commands & Lifecycle

#### 2.13.9. Module 9 — Docker in Production

1. **Docker with CI/CD**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Docker Secrets and Configs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Health Checks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Resource Limits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Docker Registry Setup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.13.10. Module 10 — Production Deployment & Best Practices

1. **Docker Security & Non-Root Users**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Docker Security & Non-Root Users
    2. Core Concept
        - Core Concept: Docker Security & Non-Root Users
    3. Syntax
        - Syntax: Docker Security & Non-Root Users
    4. Example
        - Example: Docker Security & Non-Root Users
    5. Pitfall
        - Pitfall: Docker Security & Non-Root Users
    6. Q & A
        - Q & A: Docker Security & Non-Root Users
2. **Container Health Checks & Restart Policies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Container Health Checks & Restart Policies
    2. Core Concept
        - Core Concept: Container Health Checks & Restart Policies
    3. Syntax
        - Syntax: Container Health Checks & Restart Policies
    4. Example
        - Example: Container Health Checks & Restart Policies
    5. Pitfall
        - Pitfall: Container Health Checks & Restart Policies
    6. Q & A
        - Q & A: Container Health Checks & Restart Policies
3. **Pushing Images to Docker Hub & AWS ECR**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Pushing Images to Docker Hub & AWS ECR
    2. Core Concept
        - Core Concept: Pushing Images to Docker Hub & AWS ECR
    3. Syntax
        - Syntax: Pushing Images to Docker Hub & AWS ECR
    4. Example
        - Example: Pushing Images to Docker Hub & AWS ECR
    5. Pitfall
        - Pitfall: Pushing Images to Docker Hub & AWS ECR
    6. Q & A
        - Q & A: Pushing Images to Docker Hub & AWS ECR
4. **Docker Cleanup & Pruning System Resources**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Docker Cleanup & Pruning System Resources
    2. Core Concept
        - Core Concept: Docker Cleanup & Pruning System Resources
    3. Syntax
        - Syntax: Docker Cleanup & Pruning System Resources
    4. Example
        - Example: Docker Cleanup & Pruning System Resources
    5. Pitfall
        - Pitfall: Docker Cleanup & Pruning System Resources
    6. Q & A
        - Q & A: Docker Cleanup & Pruning System Resources
5. **Building a Complete Python Flask App Container Stack**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
        - Overview: Building a Complete Python Flask App Container Stack
    2. Core Concept
        - Core Concept: Building a Complete Python Flask App Container Stack
    3. Syntax
        - Syntax: Building a Complete Python Flask App Container Stack
    4. Example
        - Example: Building a Complete Python Flask App Container Stack
    5. Pitfall
        - Pitfall: Building a Complete Python Flask App Container Stack
    6. Q & A
        - Q & A: Building a Complete Python Flask App Container Stack

### 2.14. Kubernetes

#### 2.14.1. Module 1 — Kubernetes Fundamentals

1. **What Is Kubernetes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Cluster Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **kubectl Setup and Commands**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Pods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Namespaces**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.14.2. Module 2 — Core Workloads

1. **Deployments**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Services**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **ConfigMaps and Secrets**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Persistent Volumes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **DaemonSets and StatefulSets**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.14.3. Module 3 — Networking and Ingress

1. **Kubernetes Networking Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Ingress Controller**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Network Policies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Helm Charts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Horizontal Pod Autoscaler**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.14.4. Module 4 — Production Kubernetes

1. **Resource Requests and Limits**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Liveness and Readiness Probes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **RBAC**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Kubernetes on AWS EKS**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Monitoring with Prometheus and Grafana**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

### 2.15. Jenkins

#### 2.15.1. Module 1 — Jenkins Fundamentals

1. **What Is Jenkins**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Jenkins Installation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Jenkins UI Overview**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Freestyle Jobs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Build Triggers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.15.2. Module 2 — Jenkins Pipeline

1. **Declarative Pipeline**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Scripted Pipeline**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Pipeline Stages**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Pipeline with Docker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Shared Libraries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.15.3. Module 3 — Jenkins Integration

1. **Jenkins with Git**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Jenkins with Maven**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Jenkins with Docker**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Notifications and Reports**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Jenkins Best Practices**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

### 2.16. GitHub Actions

#### 2.16.1. Module 1 — GitHub Actions Fundamentals

1. **What Is GitHub Actions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Workflow File Structure**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Triggers and Events**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Jobs and Steps**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Actions Marketplace**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.16.2. Module 2 — Building CI/CD Pipelines

1. **Python CI Pipeline**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Java CI Pipeline**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Docker Build and Push**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **Deploy to Server**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Matrix Builds**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

#### 2.16.3. Module 3 — Advanced GitHub Actions

1. **Secrets and Environment Variables**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
2. **Reusable Workflows**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
3. **Caching Dependencies**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
4. **GitHub Actions for IoT**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References
5. **Monitoring Workflow Runs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overview
    2. Learning Objectives
    3. Theory / Concept
    4. Syntax & API
    5. Worked Example
    6. Common Mistakes
    7. Exercise
    8. Quiz
    9. Summary & Cheat Sheet
    10. References

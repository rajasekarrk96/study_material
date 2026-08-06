# Css3 -- Syllabus

> Source: `_source_modular_courses.md`



#### 8.1. Module 1 — Core Fundamentals, Syntax, & Specificity Architecture

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

#### 8.2. Module 2 — The Box Model, Sizing, & Layout Fundamentals

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

#### 8.3. Module 3 — Modern Layout Engine: Flexbox & CSS Grid

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

#### 8.4. Module 4 — Typography, Colors, Backgrounds, & Visual Effects

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

#### 8.5. Module 5 — Transitions, 2D/3D Transforms, & Animations

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

#### 8.6. Module 6 — Responsive Web Design, Media Queries, & Container Queries

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

#### 8.7. Module 7 — Advanced CSS Architecture & Modern Specifications

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

#### 8.8. Module 8 — CSS Frameworks Intro & Production Performance

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

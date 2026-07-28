# IoT Full Stack Engineering Program - Master Syllabus

# Course 1: HTML5

## Module 1 - Web & Browser Architecture Fundamentals

### Lesson 1.1 Web Architecture & Protocols

#### Topics

- Client-Server Architecture
- Request-Response Cycle
- HTTP and HTTPS Protocols
- HTTP Methods (GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD)
- HTTP Status Codes (1xx, 2xx, 3xx, 4xx, 5xx)
- Web Servers vs Application Servers
- Universal Resource Identifiers (URI, URL, URN)
- Domain Name System (DNS) Resolution Process

### Lesson 1.2 Browser Rendering Engine Architecture

#### Topics

- Anatomy of a Modern Web Browser
- Browser Engines (Blink, Gecko, WebKit)
- HTML Parsing and DOM Tree Construction
- CSS Parsing and CSSOM Construction
- Render Tree Generation
- Layout and Reflow Process
- Paint and Repaint Operations
- Compositing and GPU Acceleration
- Critical Rendering Path (CRP) Optimization

### Lesson 1.3 HTML Standards & Document Structure

#### Topics

- History of HTML (HTML 1.0 to HTML5)
- W3C and WHATWG Living Standard Specifications
- DOCTYPE Declaration and Quirks vs Standards Mode
- Root Element (`<html>`) and Language Attributes
- Document Head (`<head>`) Architecture
- Character Encodings (ASCII, ISO-8859-1, UTF-8, UTF-16)
- Viewport Configuration for Mobile Responsiveness
- Metadata (`<meta>`) Tags for SEO, Refresh, and Authoring
- Open Graph Protocol and Twitter Card Meta Tags
- Document Body (`<body>`) Structure

## Module 2 - HTML Syntax, Text Formatting, & Hyperlinks

### Lesson 2.1 Syntax Rules & Element Classification

#### Topics

- Tag Syntax (Opening, Closing, Self-Closing / Void Elements)
- Element Attributes (Global Attributes, Event Attributes, Custom Data Attributes)
- Block-Level vs Inline-Level Elements
- Inline-Block Display Behavior
- Nesting Rules and Syntax Validation Standards
- HTML Entity Encoding and Escaping Special Characters

### Lesson 2.2 Text Content & Formatting Elements

#### Topics

- Heading Hierarchy (`<h1>` through `<h6>`)
- Paragraphs (`<p>`) and Line Breaks (`<br>`, `<wbr>`)
- Horizontal Rules (`<hr>`)
- Structural Text Formatting (`<strong>`, `<em>`, `<b>`, `<i>`, `<mark>`, `<small>`)
- Subscripts (`<sub>`) and Superscripts (`<sup>`)
- Inserted (`<ins>`) and Deleted (`<del>`) Text
- Computer Code Formatting (`<code>`, `<pre>`, `<kbd>`, `<samp>`, `<var>`)
- Quotations and Citations (`<blockquote>`, `<q>`, `<cite>`, `<abbr>`, `<address>`)
- Bidirectional Text Formatting (`<bdo>`, `<bdi>`)

### Lesson 2.3 Hyperlinks & Anchor Navigation

#### Topics

- Anchor Element (`<a>`) Architecture
- Absolute vs Relative URLs
- Fragment Identifiers and In-Page Anchor Jumping
- Link Targets (`_blank`, `_self`, `_parent`, `_top`)
- Link Security Attributes (`rel="noopener"`, `rel="noreferrer"`, `rel="nofollow"`)
- Non-HTML Protocols (`mailto:`, `tel:`, `sms:`, `ftp:`)
- Download Attribute (`download`)
- Link Preloading and Prefetching Attributes

## Module 3 - Semantic HTML5 & Document Layout Architecture

### Lesson 3.1 Structural Semantic Elements

#### Topics

- Semantic Web Philosophy and Benefits
- Structural Landmarks (`<header>`, `<nav>`, `<main>`, `<footer>`)
- Content Sectioning (`<article>`, `<section>`, `<aside>`)
- Heading Groups (`<hgroup>`)
- Figures and Captions (`<figure>`, `<figcaption>`)
- Interactive Disclosure Elements (`<details>`, `<summary>`)
- Dialog and Modal Structure (`<dialog>`)
- Time and Date Markup (`<time>`)

### Lesson 3.2 Document Outline & Accessibility Tree

#### Topics

- HTML5 Document Outline Algorithm
- Accessible Rich Internet Applications (ARIA) Landmark Roles
- ARIA States and Properties (`aria-label`, `aria-labelledby`, `aria-describedby`, `aria-hidden`, `aria-expanded`, `aria-live`)
- Accessibility Tree Mapping from DOM Tree
- Screen Reader Navigation Patterns
- Keyboard Focus Order and `tabindex` Attribute Management

## Module 4 - Data Organization: Lists & Tables

### Lesson 4.1 List Elements & Structure

#### Topics

- Ordered Lists (`<ol>`) and Attributes (`type`, `start`, `reversed`)
- Unordered Lists (`<ul>`)
- List Items (`<li>`)
- Description / Definition Lists (`<dl>`, `<dt>`, `<dd>`)
- Nested List Architectures
- Semantic Use Cases for Lists in Navigation Menus

### Lesson 4.2 Tabular Data & Advanced Table Markup

#### Topics

- Table Architecture (`<table>`, `<caption>`)
- Table Structure (`<thead>`, `<tbody>`, `<tfoot>`)
- Table Rows (`<tr>`) and Headers (`<th>`)
- Table Data Cells (`<td>`)
- Multi-Column and Multi-Row Spanning (`colspan`, `rowspan`)
- Column Groups (`<colgroup>`, `<col>`)
- Accessibility Attributes for Tables (`scope`, `headers`, `id`)
- Responsive Table Layout Patterns

## Module 5 - Forms, Inputs, & Client-Side Validation

### Lesson 5.1 Form Architecture & Submissions

#### Topics

- Form Element (`<form>`) Attributes
- Action URLs and Target Specifications
- HTTP Methods in Forms (GET vs POST)
- Form Encoding Types (`application/x-www-form-urlencoded`, `multipart/form-data`, `text/plain`)
- Autocomplete and Novalidate Attributes

### Lesson 5.2 Form Controls & Input Types

#### Topics

- Label Association (`<label>`, `for` attribute, Implicit vs Explicit)
- Text Inputs (`text`, `password`, `email`, `url`, `tel`, `search`)
- Numeric and Range Controls (`number`, `range`)
- Date and Time Controls (`date`, `time`, `datetime-local`, `month`, `week`)
- Choice Controls (`checkbox`, `radio`, `color`)
- Action Controls (`submit`, `reset`, `button`, `image`)
- File Upload Controls (`file`, `accept`, `multiple`)
- Hidden Inputs (`hidden`) for State Preservation
- Multi-Line Text Inputs (`<textarea>`)
- Selection Controls (`<select>`, `<option>`, `<optgroup>`)
- Data Lists for Autocomplete (`<datalist>`)
- Output and Progress Indicators (`<output>`, `<progress>`, `<meter>`)
- Form Grouping (`<fieldset>`, `<legend>`)

### Lesson 5.3 Native Client-Side Form Validation

#### Topics

- Validation Attributes (`required`, `min`, `max`, `step`, `minlength`, `maxlength`, `pattern`)
- Regular Expression Patterns in HTML Forms
- Form Control States (`:valid`, `:invalid`, `:required`, `:optional`, `:user-invalid`)
- Constraint Validation API Overview
- Custom Validation Messages and Error Tooltips

## Module 6 - Multimedia, Embedded Content, & Graphics

### Lesson 6.1 Media Elements: Images, Audio, & Video

#### Topics

- Image Element (`<img>`) and Core Attributes (`src`, `alt`, `title`, `width`, `height`)
- Responsive Images (`srcset`, `sizes` attributes)
- Picture Element (`<picture>`) and Media Queries for Images
- Modern Image Formats (JPEG, PNG, GIF, SVG, WebP, AVIF)
- Audio Element (`<audio>`, `<source>`)
- Video Element (`<video>`, `<source>`, `poster`)
- Media Attributes (`controls`, `autoplay`, `loop`, `muted`, `preload`)
- Text Tracks for Subtitles and Captions (`<track>`, WebVTT format)

### Lesson 6.2 Embedded External Content

#### Topics

- Inline Frames (`<iframe>`) and Security Sandboxing (`sandbox`, `allow`, `csp`)
- Object and Parameter Elements (`<object>`, `<param>`)
- Embed Element (`<embed>`)
- Integration of External Maps, Videos, and IoT Web Portals

### Lesson 6.3 Vector Graphics & HTML5 Canvas

#### Topics

- Scalable Vector Graphics (SVG) Inline Markup
- SVG Elements (`<svg>`, `<rect>`, `<circle>`, `<ellipse>`, `<line>`, `<polyline>`, `<polygon>`, `<path>`, `<g>`, `<text>`)
- SVG Styling and Animation Integration
- HTML5 Canvas (`<canvas>`) Element Setup
- Canvas 2D Context API Basics
- Canvas vs SVG Feature Comparison Matrix

## Module 7 - HTML5 Advanced APIs & Storage Mechanisms

### Lesson 7.1 Web Storage & IndexedDB

#### Topics

- Cookies vs Web Storage Architecture
- LocalStorage API (`setItem`, `getItem`, `removeItem`, `clear`)
- SessionStorage API Mechanics
- Storage Event Handling across Browser Tabs
- Quota Limits and Security Considerations
- Introduction to IndexedDB for Client-Side Relational/NoSQL Storage

### Lesson 7.2 Geolocation & Device APIs

#### Topics

- Geolocation API (`navigator.geolocation`)
- Position Retrieval (`getCurrentPosition`, `watchPosition`, `clearWatch`)
- Coordinates Object (Latitude, Longitude, Altitude, Accuracy)
- Error Handling and User Permission Models
- Device Orientation and Motion APIs

### Lesson 7.3 HTML5 Drag and Drop API

#### Topics

- Draggable Attribute (`draggable="true"`)
- Drag Events (`dragstart`, `drag`, `dragend`, `dragenter`, `dragover`, `dragleave`, `drop`)
- DataTransfer Object (`setData`, `getData`, `clearData`, `effectAllowed`, `dropEffect`)
- Custom Drag Images and Drop Targets

### Lesson 7.4 Web Workers & Multithreading

#### Topics

- Single-Threaded JavaScript Limitations
- Web Workers Architecture
- Dedicated Workers Creation and Lifecycle
- Shared Workers Overview
- Worker Messaging Interface (`postMessage`, `onmessage`, `onerror`)
- Terminating Workers (`terminate`)

## Module 8 - Web Components & Modern HTML Specifications

### Lesson 8.1 Shadow DOM & Custom Elements

#### Topics

- Web Components Specification Overview
- Custom Elements API (`customElements.define`)
- Autonomous Custom Elements vs Customized Built-in Elements
- Custom Element Lifecycle Callbacks (`connectedCallback`, `disconnectedCallback`, `attributeChangedCallback`)
- Shadow DOM Architecture (Shadow Root, Open vs Closed Mode)
- Encapsulation of Markup and Styles

### Lesson 8.2 HTML Templates & Slots

#### Topics

- HTML Template Element (`<template>`)
- DocumentFragment Instantiation and Cloning
- Slot Element (`<slot>`) for Light DOM Distribution
- Named Slots and Default Slot Content

## Module 9 - Accessibility (a11y), SEO, & Performance Optimization

### Lesson 9.1 Web Content Accessibility Guidelines (WCAG)

#### Topics

- WCAG 2.1 / 2.2 Principles (Perceivable, Operable, Understandable, Robust)
- Conformance Levels (A, AA, AAA)
- Keyboard Navigation and Focus Trapping
- Color Contrast Requirements
- Accessible Form Controls and Error Handling

### Lesson 9.2 Search Engine Optimization (SEO) & Microdata

#### Topics

- On-Page SEO Best Practices
- Schema.org Microdata and RDFa Syntax
- JSON-LD Structured Data Implementation
- Canonical URLs (`<link rel="canonical">`)
- Robots Meta Tags and `robots.txt` Integration

### Lesson 9.3 Performance Optimization & Best Practices

#### Topics

- Resource Hints (`dns-prefetch`, `preconnect`, `prefetch`, `preload`, `modulepreload`)
- Script Execution Modes (`async` vs `defer`)
- Native Lazy Loading (`loading="lazy"`) for Images and Iframes
- Deprecated HTML Elements and Attributes
- HTML Validation via W3C Validator Tools

---

# Course 2: CSS3

## Module 1 - Core Fundamentals, Syntax, & Specificity Architecture

### Lesson 1.1 CSS Syntax & Inclusion Methods

#### Topics

- CSS Syntax Rules (Selectors, Declarations, Properties, Values)
- Inclusion Methods (Inline Styles, Internal Style Sheets, External Style Sheets)
- At-Rules Syntax (`@charset`, `@import`, `@namespace`)
- CSS Parsing Engine and Syntax Validation

### Lesson 1.2 Comprehensive Selector Systems

#### Topics

- Basic Selectors (Universal `*`, Type/Element, Class `.`, ID `#`)
- Attribute Selectors (`[attr]`, `[attr=val]`, `[attr^=val]`, `[attr$=val]`, `[attr*=val]`, `[attr~=val]`, `[attr|=val]`)
- Combinators (Descendant ` `, Child `>`, Adjacent Sibling `+`, General Sibling `~`)
- Structural Pseudo-Classes (`:first-child`, `:last-child`, `:nth-child()`, `:nth-of-type()`, `:only-child`, `:empty`)
- State Pseudo-Classes (`:hover`, `:focus`, `:focus-within`, `:focus-visible`, `:active`, `:visited`, `:target`, `:checked`, `:disabled`)
- Logic Pseudo-Classes (`:is()`, `:where()`, `:not()`, `:has()`)
- Pseudo-Elements (`::before`, `::after`, `::first-line`, `::first-letter`, `::selection`, `::placeholder`, `::marker`)

### Lesson 1.3 Cascade, Specificity, & Inheritance

#### Topics

- The Cascade Algorithm (Origin, Importance, Specificity, Order of Appearance)
- Specificity Calculation Matrix (Inline > ID > Class/Attribute/Pseudo-class > Element)
- The `!important` Flag Mechanics and Anti-Patterns
- Inheritance Properties (Inherited vs Non-Inherited Properties)
- Explicit Inheritance Keywords (`inherit`, `initial`, `unset`, `revert`, `revert-layer`)
- Cascade Layers (`@layer`) Architecture and Precedence Rules

## Module 2 - The Box Model, Sizing, & Layout Fundamentals

### Lesson 2.1 The CSS Box Model

#### Topics

- Box Model Components (Content, Padding, Border, Margin)
- Box Sizing Modes (`content-box` vs `border-box`)
- Global Box Sizing Reset Pattern
- Margin Collapsing Mechanics and Prevention
- Negative Margins and Layout Tricks

### Lesson 2.2 Display Property & Visual Formatting Model

#### Topics

- Display Property Values (`block`, `inline`, `inline-block`, `none`, `contents`)
- Formatting Contexts (Block Formatting Context - BFC, Inline Formatting Context - IFC)
- Creating Block Formatting Contexts
- Visibility (`visible`, `hidden`, `collapse`) vs Display `none`

### Lesson 2.3 Positioning Systems & Stacking Contexts

#### Topics

- Normal Flow Layout
- Relative Positioning (`position: relative`)
- Absolute Positioning (`position: absolute`)
- Fixed Positioning (`position: fixed`)
- Sticky Positioning (`position: sticky`)
- Offset Properties (`top`, `right`, `bottom`, `left`)
- Stacking Contexts and `z-index` Order Rules

### Lesson 2.4 Sizing Units & Intrinsic Sizing

#### Topics

- Absolute Units (`px`, `pt`, `cm`, `mm`, `in`)
- Relative Font Units (`em`, `rem`, `ch`, `ex`)
- Viewport Units (`vw`, `vh`, `vmin`, `vmax`, `cqw`, `cqh`)
- Percentage Units (`%`)
- Intrinsic Sizing Keywords (`max-content`, `min-content`, `fit-content`)
- Sizing Boundaries (`min-width`, `max-width`, `min-height`, `max-height`)

## Module 3 - Modern Layout Engine: Flexbox & CSS Grid

### Lesson 3.1 Flexible Box Layout (Flexbox)

#### Topics

- Flexbox Architecture (Flex Container vs Flex Items)
- Container Properties (`display: flex | inline-flex`)
- Flex Direction (`flex-direction: row | row-reverse | column | column-reverse`)
- Wrapping Items (`flex-wrap: nowrap | wrap | wrap-reverse`)
- Flex Flow Shorthand (`flex-flow`)
- Main Axis Alignment (`justify-content: flex-start | flex-end | center | space-between | space-around | space-evenly`)
- Cross Axis Alignment (`align-items: stretch | flex-start | flex-end | center | baseline`)
- Multi-Line Alignment (`align-content`)
- Gap Properties (`gap`, `row-gap`, `column-gap`)
- Item Sizing Properties (`flex-grow`, `flex-shrink`, `flex-basis`, `flex` shorthand)
- Item Alignment & Ordering (`align-self`, `order`)

### Lesson 3.2 CSS Grid Layout System

#### Topics

- Grid Layout Terminology (Grid Container, Item, Track, Cell, Area, Line, Gap)
- Container Setup (`display: grid | inline-grid`)
- Track Definition (`grid-template-columns`, `grid-template-rows`)
- The Fractional Unit (`fr`)
- Track Repeat and Functions (`repeat()`, `minmax()`)
- Automatic Track Sizing (`auto-fill` vs `auto-fit`)
- Grid Template Areas (`grid-template-areas`, `grid-area`)
- Implicit Grid Track Generation (`grid-auto-columns`, `grid-auto-rows`, `grid-auto-flow`)
- Line-Based Item Placement (`grid-column-start`, `grid-column-end`, `grid-row-start`, `grid-row-end`, `grid-column`, `grid-row`)
- Grid Alignment (`justify-items`, `align-items`, `justify-content`, `align-content`, `justify-self`, `align-self`)
- Subgrid (`grid-template-columns: subgrid`) Specification

## Module 4 - Typography, Colors, Backgrounds, & Visual Effects

### Lesson 4.1 Advanced Typography & Web Fonts

#### Topics

- Font Families and Fallback Font Stacks
- Web Safe Fonts vs Web Fonts
- Custom Font Embedding (`@font-face`)
- Font Formats (WOFF, WOFF2, TTF, OTF, SVG)
- Font Properties (`font-size`, `font-weight`, `font-style`, `font-variant`, `line-height`)
- Text Formatting (`text-align`, `text-transform`, `text-decoration`, `text-indent`, `letter-spacing`, `word-spacing`)
- Text Truncation and Ellipsis (`white-space`, `overflow`, `text-overflow`, line-clamping)
- Variable Fonts and Font Variation Settings

### Lesson 4.2 Modern CSS Color Systems

#### Topics

- Named Colors and Hexadecimal Notation (`#RGB`, `#RRGGBB`, `#RRGGBBAA`)
- RGB and RGBA Color Functions (`rgb()`, `rgba()`)
- HSL and HSLA Color Functions (`hsl()`, `hsla()`)
- Modern Color Spaces (`hwb()`, `lab()`, `lch()`, `oklab()`, `oklch()`)
- Color Mixing Function (`color-mix()`)
- Alpha Channel Opacity Management
- The `currentcolor` Keyword

### Lesson 4.3 Backgrounds, Borders, & Shadows

#### Topics

- Background Color and Image (`background-color`, `background-image`)
- Background Repetition and Positioning (`background-repeat`, `background-position`)
- Background Sizing (`background-size: cover | contain | <length>`)
- Background Attachment (`background-attachment: scroll | fixed | local`)
- Linear, Radial, and Conic Gradients
- Border Styling (`border-width`, `border-style`, `border-color`, `border-radius`)
- Outline vs Border Characteristics
- Box Shadow Effects (`box-shadow` inset, offsets, blur, spread)
- Text Shadows (`text-shadow`)

### Lesson 4.4 Visual Effects, Filters, & Blending

#### Topics

- Opacity and Element Transparency
- CSS Filter Effects (`blur()`, `brightness()`, `contrast()`, `drop-shadow()`, `grayscale()`, `hue-rotate()`, `invert()`, `saturate()`, `sepia()`)
- Backdrop Filter (`backdrop-filter`) for Glassmorphism
- Blend Modes (`mix-blend-mode`, `background-blend-mode`)
- Clipping Paths (`clip-path`) and Masking (`mask-image`)

## Module 5 - Transitions, 2D/3D Transforms, & Animations

### Lesson 5.1 CSS Transitions

#### Topics

- Transition Properties (`transition-property`, `transition-duration`)
- Timing Functions (`transition-timing-function: linear | ease | ease-in | ease-out | ease-in-out | cubic-bezier()`)
- Transition Delays (`transition-delay`)
- Transition Shorthand Property
- Transitioning Hardware-Accelerated Properties

### Lesson 5.2 2D and 3D Transformations

#### Topics

- 2D Transform Functions (`translate()`, `scale()`, `rotate()`, `skew()`)
- Transform Origin (`transform-origin`)
- 3D Transform Setup (`perspective`, `perspective-origin`)
- 3D Transform Functions (`translate3d()`, `rotateX()`, `rotateY()`, `rotateZ()`, `scale3d()`)
- Transform Style (`transform-style: preserve-3d`)
- Backface Visibility (`backface-visibility: hidden | visible`)

### Lesson 5.3 Keyframe Animations

#### Topics

- `@keyframes` Rule Syntax and Percentage Steps
- Animation Name and Duration (`animation-name`, `animation-duration`)
- Animation Timing and Delay (`animation-timing-function`, `animation-delay`)
- Iteration and Direction (`animation-iteration-count`, `animation-direction`)
- Fill Modes (`animation-fill-mode: none | forwards | backwards | both`)
- Play State (`animation-play-state: running | paused`)
- Performance Optimization for Animations (GPU Composition, `will-change` property)

## Module 6 - Responsive Web Design, Media Queries, & Container Queries

### Lesson 6.1 Responsive Architecture Principles

#### Topics

- Mobile-First vs Desktop-First Design Strategies
- Viewport Configuration and Scaling Rules
- Fluid Layouts and Relative Sizing Calculations
- Responsive Media and Aspect Ratio Management (`aspect-ratio` property)

### Lesson 6.2 Media Queries

#### Topics

- `@media` Rule Syntax
- Media Types (`screen`, `print`, `all`)
- Media Features (`width`, `height`, `orientation`, `resolution`, `aspect-ratio`)
- Level 4 Range Syntax (`(width >= 768px)`)
- Logical Operators (`and`, `not`, `only`, `,` comma or)
- User Preference Media Features (`prefers-color-scheme`, `prefers-reduced-motion`, `prefers-contrast`)

### Lesson 6.3 Container Queries

#### Topics

- Container Queries Concept vs Media Queries
- Defining Containers (`container-type: inline-size | size`, `container-name`)
- Container Query Syntax (`@container`)
- Container Query Units (`cqw`, `cqh`, `cqi`, `cqb`, `cqmin`, `cqmax`)
- Component-Driven Responsive Architecture

### Lesson 6.4 Fluid Layout Functions

#### Topics

- CSS Math Functions (`calc()`)
- Bound Functions (`min()`, `max()`)
- Clamp Function (`clamp(MIN, VAL, MAX)`) for Fluid Typography and Spacing

## Module 7 - Advanced CSS Architecture & Modern Specifications

### Lesson 7.1 CSS Custom Properties (Variables)

#### Topics

- Custom Property Declaration (`--custom-variable-name`)
- Variable Retrieval (`var(--custom-variable-name, fallback)`)
- Variable Scoping and Cascade Mechanics
- Dynamic Manipulation of CSS Variables via JavaScript
- Building Light/Dark Theme Switchers using Custom Properties

### Lesson 7.2 Modern CSS Architecture & Methodologies

#### Topics

- BEM (Block, Element, Modifier) Naming Convention
- OOCSS (Object-Oriented CSS) Principles
- SMACSS (Scalable and Modular Architecture for CSS)
- Utility-First CSS Architecture
- CSS Modules and Scoped Styling Concepts

### Lesson 7.3 Native CSS Nesting & Logical Properties

#### Topics

- CSS Native Nesting Syntax and Nesting Selector (`&`)
- Direct Nesting vs Child Nesting Rules
- Logical Properties vs Physical Properties (`margin-inline`, `padding-block`, `inset-block`, `border-inline`)
- Writing Modes (`writing-mode: horizontal-tb | vertical-rl | vertical-lr`)
- Internationalization Layout Adaptation

## Module 8 - CSS Frameworks Intro & Production Performance

### Lesson 8.1 Utility-First CSS & Tailwind Introduction

#### Topics

- Utility-First Architecture Paradigm
- Tailwind CSS Engine Overview
- Just-In-Time (JIT) Compiler Mechanics
- Core Utility Categories (Spacing, Typography, Flexbox, Grid)
- Customization via `tailwind.config.js` / Modern Directives (`@theme`)

### Lesson 8.2 Component Frameworks & Bootstrap Overview

#### Topics

- Bootstrap Grid System Architecture
- Prebuilt Component Styling Patterns
- Overriding Framework Styles cleanly

### Lesson 8.3 Production Optimization & Performance

#### Topics

- Critical Rendering Path (CRP) Impact of CSS
- Reflow vs Repaint Triggering Properties
- Unused CSS Removal (PurgeCSS / Tree Shaking)
- Minification and Compression Techniques
- Critical CSS Extraction and Inline Delivery Strategies

---

# Course 3: JavaScript

## Module 1 - Language Architecture, Engine, & Execution Mechanics

### Lesson 1.1 History, Evolution, & ECMAScript Standards

#### Topics

- Origins of JavaScript and TC39 Committee
- ECMAScript Specifications (ES5, ES6/ES2015 to Latest ES Standards)
- JavaScript Runplaces (Browser Engines, Node.js, Deno, Bun)
- Backward Compatibility and Polyfills / Transpilation (Babel)

### Lesson 1.2 JavaScript Engine Architecture

#### Topics

- Anatomy of JavaScript Engines (V8, SpiderMonkey, JavaScriptCore)
- Source Code Parsing and Abstract Syntax Tree (AST) Generation
- Just-In-Time (JIT) Compilation (Interpreter vs Compiler, Ignition & TurboFan)
- Bytecode Generation and Machine Code Execution

### Lesson 1.3 Execution Context, Call Stack, & Memory Management

#### Topics

- Execution Context Types (Global, Function, Eval)
- Phases of Execution Context (Creation Phase vs Execution Phase)
- Variable Environment and Lexical Environment
- The Call Stack and Stack Overflow Errors
- Memory Heap Allocation
- Garbage Collection Algorithms (Mark-and-Sweep, Reference Counting)
- Memory Leaks Identification and Prevention Strategies

## Module 2 - Variables, Data Types, & Operators

### Lesson 2.1 Variable Declarations & Scoping

#### Topics

- Variable Keyword Comparison (`var`, `let`, `const`)
- Scope Levels (Global Scope, Function Scope, Block Scope)
- Variable Re-declaration and Re-assignment Rules
- Hoisting Mechanics (Variable Hoisting vs Function Hoisting)
- Temporal Dead Zone (TDZ) Architecture

### Lesson 2.2 Primitive & Reference Data Types

#### Topics

- Primitive Types (`Number`, `String`, `Boolean`, `Undefined`, `Null`, `Symbol`, `BigInt`)
- Reference Type (`Object`, including Arrays and Functions)
- Pass-by-Value vs Pass-by-Reference Mechanics
- Type Inspection (`typeof`, `instanceof`, `Array.isArray()`)
- Symbol Creation and Unique Identifiers
- BigInt Operations and Precision Capabilities

### Lesson 2.3 Type Coercion & Comparison Operations

#### Topics

- Implicit vs Explicit Type Conversion
- String, Number, and Boolean Conversion Functions
- Truthy and Falsy Values Matrix
- Abstract Equality (`==`) vs Strict Equality (`===`) Coercion Rules
- Object-to-Primitive Coercion (`valueOf()`, `toString()`, `[Symbol.toPrimitive]`)

### Lesson 2.4 Comprehensive Operator Systems

#### Topics

- Arithmetic and Increment/Decrement Operators
- Assignment and Compound Assignment Operators
- Comparison and Relational Operators
- Logical Operators (`&&`, `||`, `!`) and Short-Circuit Evaluation
- Nullish Coalescing Operator (`??`)
- Optional Chaining Operator (`?.`)
- Ternary / Conditional Operator (`? :`)
- Bitwise Operators (`&`, `|`, `^`, `~`, `<<`, `>>`, `>>>`)
- Comma Operator and Unary Operators (`delete`, `typeof`, `void`)

## Module 3 - Control Flow, Loops, & Iteration Protocols

### Lesson 3.1 Conditional Logic

#### Topics

- `if`, `else if`, `else` Statements
- Switch Statement Syntax, Fallthrough, and Strict Comparison
- Guard Clauses and Early Return Patterns
- Lookup Tables as Alternatives to Switch/If Statements

### Lesson 3.2 Loops & Iteration Constructs

#### Topics

- `for` Loop Syntax and Variable Scoping
- `while` and `do...while` Loops
- Loop Control Keywords (`break`, `continue`, Labeled Statements)
- `for...in` Loop (Object Property Enumeration)
- `for...of` Loop (Iterable Value Iteration)

### Lesson 3.3 Iteration Protocols

#### Topics

- Iterable Protocol (`[Symbol.iterator]`)
- Iterator Protocol (`next()` method returning `{ value, done }`)
- Built-in Iterables (Arrays, Strings, Maps, Sets)
- Custom Iterable Object Implementation

## Module 4 - Functions, Scope, & Closures

### Lesson 4.1 Function Declarations, Expressions, & Arrow Functions

#### Topics

- Function Declarations and Hoisting
- Function Expressions (Named vs Anonymous)
- Arrow Functions (`() => {}`) Syntax and Rules
- Differences between Regular Functions and Arrow Functions
- Immediately Invoked Function Expressions (IIFE)
- First-Class Function Capabilities

### Lesson 4.2 Parameters, Arguments, & Return Values

#### Topics

- Positional Parameters and Arguments
- Default Parameter Values
- Rest Parameters (`...args`)
- The `arguments` Object in Regular Functions
- Function Return Values and Implicit Returns

### Lesson 4.3 Scope Chain & Closures

#### Topics

- Lexical Scoping and Scope Chain Resolution
- Outer Environment Reference
- Closure Definition and Mechanism
- Retaining Scope State via Closures
- Encapsulation and Private Data Patterns using Closures
- Memory Implications and Stale Closures

### Lesson 4.4 Functional Concepts & Higher-Order Functions

#### Topics

- Higher-Order Functions Definition
- Pure Functions and Side Effects
- Immutability Principles
- Function Composition and Currying Basics

## Module 5 - Objects, Arrays, & Data Structures

### Lesson 5.1 Object Literals & Operations

#### Topics

- Object Creation Syntax (Literal, `Object()`, `Object.create()`)
- Property Access (Dot Notation vs Bracket Notation)
- Dynamic Property Keys and Computed Property Names
- Adding, Modifying, and Deleting Object Properties
- Property Descriptors (`value`, `writable`, `enumerable`, `configurable`)
- Object Immutability Methods (`Object.freeze()`, `Object.seal()`, `Object.preventExtensions()`)
- Object Static Methods (`Object.keys()`, `Object.values()`, `Object.entries()`, `Object.fromEntries()`, `Object.assign()`)

### Lesson 5.2 Arrays & Array Methods

#### Topics

- Array Creation and Dense vs Sparse Arrays
- Index-Based Access and Length Property Mechanics
- Mutator Methods (`push`, `pop`, `shift`, `unshift`, `splice`, `reverse`, `sort`, `fill`)
- Non-Mutating Accessor Methods (`slice`, `concat`, `join`, `indexOf`, `lastIndexOf`, `includes`)
- Higher-Order Iteration Methods (`forEach`, `map`, `filter`, `reduce`, `reduceRight`, `find`, `findIndex`, `findLast`, `some`, `every`, `flat`, `flatMap`)
- Array Sorting Mechanics and Custom Comparator Functions

### Lesson 5.3 Destructuring Assignment & Spread/Rest Syntax

#### Topics

- Array Destructuring Syntax and Default Values
- Object Destructuring Syntax and Property Renaming
- Nested Destructuring Patterns
- Parameter Destructuring in Functions
- Spread Operator (`...`) for Array Expansion and Object Merging
- Rest Syntax for Destructuring Collects

### Lesson 5.4 Advanced Built-in Data Structures

#### Topics

- Map Collection (`Map`, `set`, `get`, `has`, `delete`, `clear`, `size`)
- WeakMap Collection (Garbage Collection Capabilities)
- Set Collection (`Set`, `add`, `has`, `delete`, `clear`, Unique Values)
- WeakSet Collection
- Date Object and Time Manipulation
- Math Object Methods and Calculations
- ArrayBuffer and TypedArrays for Binary Data Handling

## Module 6 - Object-Oriented Programming (OOP) & Prototype System

### Lesson 6.1 Prototype Chain & Inheritance

#### Topics

- Prototype-Based OOP Architecture
- Prototype Property (`prototype`) vs Internal Prototype (`[[Prototype]]` / `__proto__`)
- Prototype Chain Lookup Mechanism
- Adding Methods to Prototypes
- Prototypal Inheritance Implementation
- Prototype Pollution Vulnerabilities

### Lesson 6.2 ES6 Class Syntax & Mechanics

#### Topics

- `class` Declaration Syntax
- Constructor Method (`constructor`)
- Instance Fields and Methods
- Static Methods and Static Fields
- Private Class Fields (`#fieldName`) and Private Methods
- Getters and Setters (`get`, `set`)

### Lesson 6.3 Class Inheritance & Polymorphism

#### Topics

- Class Extension (`extends`)
- Super Keyword (`super()` constructor call, `super.method()`)
- Method Overriding
- Polymorphism in JavaScript

### Lesson 6.4 The `this` Keyword Execution Rules

#### Topics

- Global `this` Binding
- Implicit Binding (Method Invocation)
- Explicit Binding (`call()`, `apply()`, `bind()`)
- New Binding (Constructor Function Invocation)
- Lexical `this` in Arrow Functions

## Module 7 - Document Object Model (DOM) & Browser Object Model (BOM)

### Lesson 7.1 DOM Architecture & Selection

#### Topics

- DOM Tree Hierarchy (Document, Element, Text, Comment Nodes)
- Node vs Element Types
- Legacy Selection Methods (`getElementById`, `getElementsByClassName`, `getElementsByTagName`)
- Modern Selection Methods (`querySelector`, `querySelectorAll`)
- Live NodeLists vs Static NodeLists

### Lesson 7.2 DOM Manipulation & Traversal

#### Topics

- Element Traversal (`parentElement`, `children`, `firstElementChild`, `lastElementChild`, `nextElementSibling`, `previousElementSibling`)
- Creating Nodes (`createElement`, `createTextNode`, `cloneNode`)
- Inserting Elements (`appendChild`, `prepend`, `insertBefore`, `insertAdjacentElement`)
- Removing and Replacing Elements (`remove`, `removeChild`, `replaceChild`)
- Text Content Manipulation (`textContent`, `innerText`, `innerHTML`)
- Performance Optimization with `DocumentFragment`

### Lesson 7.3 Attribute, Style, & Class Manipulation

#### Topics

- Attribute Inspection and Modification (`getAttribute`, `setAttribute`, `removeAttribute`, `hasAttribute`)
- Custom Data Attributes (`dataset` property)
- Class List API (`classList.add`, `classList.remove`, `classList.toggle`, `classList.contains`)
- Inline Style Manipulation (`element.style`)
- Reading Computed Styles (`window.getComputedStyle()`)

### Lesson 7.4 Browser Object Model (BOM)

#### Topics

- Window Object Architecture
- Navigator Object (User Agent, Hardware, Online Status, Geolocation Reference)
- Location Object (URL Parsing, Redirection, Reloading)
- History Object (`pushState`, `replaceState`, `back`, `forward`, `go`)
- Screen Object Specifications
- Timers (`setTimeout`, `setInterval`, `requestAnimationFrame`, `clearTimeout`, `clearInterval`, `cancelAnimationFrame`)

## Module 8 - Event Architecture & Asynchronous JavaScript

### Lesson 8.1 Event Listeners & Event Flow

#### Topics

- Event Registration (`addEventListener`, `removeEventListener`)
- Event Object Properties and Methods
- Preventing Default Behavior (`preventDefault()`)
- Stopping Propagation (`stopPropagation()`, `stopImmediatePropagation()`)
- Event Propagation Phases (Capturing Phase, Target Phase, Bubbling Phase)

### Lesson 8.2 Event Delegation & User Interactions

#### Topics

- Event Delegation Pattern and Benefits
- Mouse Events (`click`, `dblclick`, `mousedown`, `mouseup`, `mousemove`, `mouseover`, `mouseout`)
- Keyboard Events (`keydown`, `keyup`, `code` vs `key` properties)
- Form Events (`submit`, `change`, `input`, `focus`, `blur`)
- Touch and Pointer Events
- Custom Events (`CustomEvent` API)

### Lesson 8.3 The Event Loop & Asynchronous Architecture

#### Topics

- Single-Threaded Concurrency Model
- Web APIs / Browser Environment Offloading
- Call Stack Execution
- Macrotask Queue / Callback Queue (`setTimeout`, `setInterval`, I/O)
- Microtask Queue (`Promise`, `queueMicrotask`, `MutationObserver`)
- Event Loop Step-by-step Execution Order and Priority

### Lesson 8.4 Callbacks, Promises, & Async/Await

#### Topics

- Asynchronous Callback Pattern and Callback Hell
- Promise States (Pending, Fulfilled, Rejected)
- Promise Construction (`new Promise((resolve, reject) => {})`)
- Chaining Promises (`.then()`, `.catch()`, `.finally()`)
- Promise Combinator Static Methods (`Promise.all()`, `Promise.allSettled()`, `Promise.race()`, `Promise.any()`)
- `async` Function Declaration
- `await` Operator Rules and Top-Level Await
- Error Handling in Async/Await (`try...catch...finally`)

### Lesson 8.5 Networking, HTTP, & Data Fetching

#### Topics

- XMLHttpRequest (XHR) Legacy API
- Fetch API Architecture (`fetch()`)
- Request and Response Objects
- Headers Interface (`Headers`)
- Response Body Stream Parsing (`.json()`, `.text()`, `.blob()`, `.arrayBuffer()`)
- HTTP Status Code Handling in Fetch
- JSON Data Formatting (`JSON.parse()`, `JSON.stringify()`, Replacer/Reviver)
- Cross-Origin Resource Sharing (CORS) Security Mechanics
- WebSockets Client Basics (`WebSocket` API)

## Module 9 - ES6+ Modern Features, Modules, & Design Patterns

### Lesson 9.1 Modern ES6+ Syntax Enhancements

#### Topics

- Template Literals and Tagged Template Functions
- Enhanced Object Literals (Property Shorthand, Method Shorthand)
- Symbol Data Type and Well-Known Symbols
- Generators (`function*`) and `yield` Expression
- Proxy API (`new Proxy(target, handler)`) and Traps
- Reflect API Static Methods

### Lesson 9.2 Module Systems

#### Topics

- History of Modular JS (Script Tags, IIFE, AMD, UMD)
- CommonJS Module System (`module.exports`, `require`)
- ES Modules (ESM) Syntax (`export`, `export default`, `import`, Named vs Default Imports)
- Dynamic Import Expressions (`import()`)
- Browser Support for ESM (`<script type="module">`)

### Lesson 9.3 JavaScript Design Patterns

#### Topics

- Module Pattern and Factory Pattern
- Singleton Pattern
- Observer / Publisher-Subscriber (Pub-Sub) Pattern
- Strategy Pattern
- Decorator Pattern

## Module 10 - Error Handling, Debugging, & Performance Optimization

### Lesson 10.1 Robust Error Handling

#### Topics

- Exception Throwing (`throw`)
- `try...catch...finally` Blocks
- Built-in Error Types (`Error`, `SyntaxError`, `TypeError`, `ReferenceError`, `RangeError`, `URIError`)
- Creating Custom Error Classes (`extends Error`)
- Global Unhandled Rejection and Error Events

### Lesson 10.2 Debugging Strategies

#### Topics

- Browser Developer Tools Inspector
- Console API (`console.log`, `table`, `dir`, `time`, `timeEnd`, `group`, `trace`, `assert`)
- Breakpoints (Source Breakpoints, Conditional Breakpoints, XHR/Fetch Breakpoints, DOM Breakpoints)
- Call Stack and Scope Inspection
- Debugger Statement (`debugger`)

### Lesson 10.3 Performance & Security Optimization

#### Topics

- Debouncing and Throttling Algorithms
- Memory Leak Diagnosis using Memory Profiler
- DOM Layout Thrashing Avoidance
- Code Splitting and Tree Shaking Concepts
- Cross-Site Scripting (XSS) Prevention and Sanitization
- Content Security Policy (CSP) Fundamentals

---

# Course 4: Python Programming

## Module 1 - Python Architecture, Environment, & Ecosystem

### Lesson 1.1 Python Overview & Philosophy

#### Topics

- History and Evolution of Python (Python 2 vs Python 3)
- The Zen of Python (PEP 20 Principles)
- Python Use Cases (Web, Data Science, Automation, IoT, AI)
- Interpreted vs Compiled Language Mechanics

### Lesson 1.2 CPython Architecture & Execution Engine

#### Topics

- Major Python Implementations (CPython, PyPy, Jython, IronPython)
- Source Code Compilation to Bytecode (`.pyc` files)
- Python Virtual Machine (PVM) Architecture
- Global Interpreter Lock (GIL) Mechanics and Impact

### Lesson 1.3 Environment Setup & Tooling

#### Topics

- Installing Python (OS-specific Binaries, Source Compilation)
- Environment Variables (`PATH`, `PYTHONPATH`, `PYTHONSTARTUP`)
- Interactive Shell / REPL
- IDEs Setup (VS Code, PyCharm)
- Package Installer for Python (`pip`) Setup and Configuration
- Virtual Environments (`venv`, `virtualenv`)
- Dependency Management Tools (Poetry, `pyproject.toml`, `requirements.txt`)

## Module 2 - Fundamentals: Variables, Data Types, & Syntax Rules

### Lesson 2.1 Syntax Rules & Style Conventions

#### Topics

- Indentation Code Blocks Standard (PEP 8)
- Single-Line and Multi-Line Comments (`#`, Docstrings `"""`)
- Line Continuation Rules
- Reserved Keywords and Identifiers

### Lesson 2.2 Variables & Dynamic Typing System

#### Topics

- Variable Creation and Memory Name Binding
- Dynamic Typing vs Static Typing
- Type Hinting Overview (PEP 484 Annotation Syntax)
- Reference Counting and Memory Allocation (`sys.getrefcount`)

### Lesson 2.3 Built-in Primitive Data Types

#### Topics

- Integer Type (`int`) - Arbitrary Precision Characteristics
- Floating-Point Type (`float`) - IEEE 754 Representation
- Complex Numbers (`complex`)
- Boolean Type (`bool`)
- None Type (`NoneType`)
- Type Inspection (`type()`, `isinstance()`)
- Explicit Type Conversion / Casting

## Module 3 - Operators, Control Flow, & Pattern Matching

### Lesson 3.1 Comprehensive Operator Systems

#### Topics

- Arithmetic Operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
- Comparison / Relational Operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Logical Operators (`and`, `or`, `not`) and Short-Circuiting
- Assignment and Compound Operators (`+=`, `-=`, etc.)
- Bitwise Operators (`&`, `|`, `^`, `~`, `<<`, `>>`)
- Identity Operators (`is`, `is not`) vs Equality (`==`)
- Membership Operators (`in`, `not in`)
- Assignment Expression / Walrus Operator (`:=`)

### Lesson 3.2 Conditional Execution

#### Topics

- `if`, `elif`, `else` Structural Logic
- Conditional Expressions (Ternary Operator)
- Structural Pattern Matching (`match...case` Syntax - Python 3.10+)

### Lesson 3.3 Iteration & Loop Structures

#### Topics

- `while` Loop Syntax and Infinite Loops
- `for` Loop over Iterables
- Range Generator Function (`range(start, stop, step)`)
- Enumerate Function (`enumerate()`)
- Zipper Function (`zip()`)
- Loop Control Directives (`break`, `continue`)
- Loop `else` Clause Architecture

## Module 4 - Sequences & Core Collections Data Structures

### Lesson 4.1 Strings & Text Processing

#### Topics

- String Immutability
- Indexing and Slicing Mechanics (`[start:stop:step]`)
- String Methods (`split`, `join`, `strip`, `replace`, `find`, `upper`, `lower`, `startswith`, `endswith`)
- String Formatting Techniques (`%` Formatting, `.format()`, f-strings)
- Character Encodings (ASCII, UTF-8, Bytes vs Strings, `encode()`, `decode()`)

### Lesson 4.2 Lists & Sequence Operations

#### Topics

- Ordered Mutable Sequence Characteristics
- Indexing, Slicing, and Re-assignment
- List Operations (`+` Concatenation, `*` Repetition)
- List Modification Methods (`append`, `extend`, `insert`, `remove`, `pop`, `clear`)
- Searching and Ordering Methods (`index`, `count`, `sort`, `reverse`)
- Shallow Copying vs Deep Copying (`copy` module)

### Lesson 4.3 Tuples & Immutable Sequences

#### Topics

- Tuple Syntax and Immutability
- Packing and Unpacking Tuples
- Single-Element Tuple Syntax
- Tuple Methods (`count`, `index`)
- Named Tuples (`collections.namedtuple`)

### Lesson 4.4 Dictionaries (Key-Value Mappings)

#### Topics

- Dictionary Key Requirements (Hashability Principle)
- Dictionary Creation and Access
- Modifying and Adding Entries
- Dictionary Methods (`keys`, `values`, `items`, `get`, `pop`, `popitem`, `update`, `setdefault`)
- Dictionary Order Retention (Python 3.7+ Standard)

### Lesson 4.5 Sets & Frozensets

#### Topics

- Unordered Unique Collections
- Set Creation and Element Insertion
- Set Mathematical Operations (Union `|`, Intersection `&`, Difference `-`, Symmetric Difference `^`)
- Set Methods (`add`, `remove`, `discard`, `pop`, `issubset`, `issuperset`)
- Frozenset Immutable Variant

### Lesson 4.6 Advanced Collections Module

#### Topics

- Default Dictionary (`collections.defaultdict`)
- Element Counter (`collections.Counter`)
- Double-Ended Queue (`collections.deque`)
- Ordered Dictionary (`collections.OrderedDict`)
- Chain Map (`collections.ChainMap`)

## Module 5 - Functions, Comprehensions, & Functional Programming

### Lesson 5.1 Function Definitions & Signature Architecture

#### Topics

- Function Definition Syntax (`def`) and Calling Mechanics
- Return Statements and Multi-Value Returns (Tuple Unpacking)
- Positional vs Keyword Arguments
- Default Parameter Values and Mutable Default Parameter Gotchas
- Arbitrary Positional Arguments (`*args`)
- Arbitrary Keyword Arguments (`**kwargs`)
- Keyword-Only Parameters (`*`) and Positional-Only Parameters (`/`)

### Lesson 5.2 Scope Rules & Lexical Namespace

#### Topics

- Namespace Resolution Hierarchy (LEGB Rule: Local, Enclosing, Global, Built-in)
- Modifying Global Variables (`global` keyword)
- Modifying Enclosing Variables (`nonlocal` keyword)

### Lesson 5.3 Lambda Functions & Functional Utilities

#### Topics

- Anonymous Lambda Syntax (`lambda arguments: expression`)
- Use Cases and Limitations of Lambda Functions
- Mapping Function (`map()`)
- Filtering Function (`filter()`)
- Reducing Function (`functools.reduce()`)

### Lesson 5.4 Comprehension Expressions

#### Topics

- List Comprehensions Syntax and Conditional Filtering
- Dictionary Comprehensions
- Set Comprehensions
- Generator Expressions Syntax vs List Comprehensions
- Nested Comprehension Expressions

## Module 6 - Advanced Functional Features: Decorators, Generators, & Iterators

### Lesson 6.1 Iterators & Iterator Protocol

#### Topics

- Iterable Objects vs Iterator Objects
- Dunder Methods (`__iter__()` and `__next__()`)
- Creating Custom Iterator Classes
- Handling `StopIteration` Exception

### Lesson 6.2 Generator Functions & Yield Engine

#### Topics

- Generator Functions Syntax (`yield` statement)
- Execution Suspension and Resumption Mechanics
- Memory Efficiency of Generators for Large Datasets
- Generator Methods (`send()`, `throw()`, `close()`)
- Delegating Generators (`yield from` syntax)

### Lesson 6.3 Decorator Architecture

#### Topics

- First-Class Functions and Enclosing Closures in Python
- Function Decorator Syntax (`@decorator_name`)
- Building Custom Function Decorators
- Decorators Accepting Arguments
- Stacking Multiple Decorators
- Preserving Function Metadata (`functools.wraps`)
- Class-Based Decorators

## Module 7 - Object-Oriented Programming (OOP)

### Lesson 7.1 Class Definitions & Object Instantiation

#### Topics

- Class Blueprint Syntax (`class`)
- Instance Creation and Memory Allocation
- Instance Attributes and Methods
- The `self` Parameter Mechanics
- Constructor Method (`__init__`) and Initialization
- Object Creation Low-Level Control (`__new__`)

### Lesson 7.2 Encapsulation & Property Management

#### Topics

- Access Control Conventions (Public, Protected `_name`, Private `__name`)
- Name Mangling Engine Mechanics
- Property Decorator (`@property`, `@getter.setter`, `@getter.deleter`)

### Lesson 7.3 Inheritance & Polymorphism

#### Topics

- Single Inheritance Syntax
- Multiple Inheritance Architecture
- Diamond Problem and Method Resolution Order (MRO)
- C3 Linearization Algorithm
- Super Function (`super()`) Usage and Cooperative Multiple Inheritance
- Method Overriding and Duck Typing Philosophy

### Lesson 7.4 Class Methods & Static Methods

#### Topics

- Instance Methods vs Class Methods vs Static Methods
- Class Method Decorator (`@classmethod`) and `cls` Parameter
- Static Method Decorator (`@staticmethod`)
- Factory Pattern Implementation via `@classmethod`

### Lesson 7.5 Dunder / Magic Methods (Data Model)

#### Topics

- String Representation Methods (`__str__`, `__repr__`)
- Arithmetic Operator Overloading (`__add__`, `__sub__`, `__mul__`, etc.)
- Comparison Operator Overloading (`__eq__`, `__lt__`, `__gt__`, etc.)
- Container Emulation Methods (`__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`)
- Callable Objects (`__call__`)

### Lesson 7.6 Abstract Base Classes (ABC) & Protocols

#### Topics

- Abstract Base Classes Module (`abc.ABC`)
- Abstract Methods (`@abstractmethod`) and Interface Enforcement
- Structural Subtyping via Protocols (`typing.Protocol`)

## Module 8 - Exception Handling, Context Managers, & Logging

### Lesson 8.1 Exception Architecture & Handling

#### Topics

- Built-in Exception Hierarchy (`BaseException`, `Exception`, `ValueError`, `TypeError`, etc.)
- Handling Exceptions (`try`, `except`)
- Catching Multiple Specific Exceptions
- The `else` Block in Exception Handling
- The `finally` Cleanup Block
- Exception Chaining (`raise ... from ...`)
- Raising Custom Exceptions (`raise`)

### Lesson 8.2 Context Managers & Resource Management

#### Topics

- Resource Management and Leak Risks
- The `with` Statement Architecture
- Building Context Managers via Class Dunder Methods (`__enter__`, `__exit__`)
- Exception Handling inside `__exit__`
- Building Context Managers via `contextlib` Generator Decorator (`@contextmanager`)

### Lesson 8.3 Logging Framework

#### Topics

- Python `logging` Standard Module Overview
- Logging Levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Loggers, Handlers, Formatters, and Filters
- File Logging and Console Logging Configuration
- Rotating File Handlers (`RotatingFileHandler`, `TimedRotatingFileHandler`)

## Module 9 - File I/O, Data Serialization, & Format Handling

### Lesson 9.1 File Handling System

#### Topics

- Opening Files (`open()`) and File Modes (`r`, `w`, `a`, `b`, `+`)
- Reading Methods (`read`, `readline`, `readlines`)
- Writing Methods (`write`, `writelines`)
- File Pointer Manipulation (`seek()`, `tell()`)
- Path Operations (`os.path` vs `pathlib.Path`)

### Lesson 9.2 Data Serialization Formats

#### Topics

- JSON Handling (`json.dumps`, `json.loads`, `json.dump`, `json.load`)
- Custom JSON Encoder and Decoder Classes
- CSV Processing (`csv.reader`, `csv.writer`, `csv.DictReader`, `csv.DictWriter`)
- XML Processing (`xml.etree.ElementTree`)
- YAML Configuration Parsing (`PyYAML` library)
- Binary Serialization (`pickle` module and Security Warnings)

## Module 10 - Regular Expressions & Text Parsing

### Lesson 10.1 Regex Module (`re`) Mechanics

#### Topics

- Regular Expression Syntax and Metacharacters
- Character Classes and Quantifiers
- Anchors and Boundaries
- Search Functions (`re.match`, `re.search`, `re.findall`, `re.finditer`)
- String Substitution (`re.sub`) and Splitting (`re.split`)
- Compiling Regex Patterns (`re.compile`)
- Capturing Groups, Non-Capturing Groups, and Lookaround Assertions

## Module 11 - Modules, Packages, & Distribution

### Lesson 11.1 Modules & Import System

#### Topics

- Creating Custom Modules (`.py` files)
- Import Statements Variations (`import mod`, `from mod import func`, `import mod as alias`)
- Module Search Path (`sys.path`)
- Executable Modules Guard (`if __name__ == '__main__':`)
- Reloading Modules (`importlib.reload`)

### Lesson 11.2 Package Architecture

#### Topics

- Package Directory Structure
- Package Initialization File (`__init__.py`) Roles
- Relative Imports (Single dot `.`, Double dot `..`)
- Namespace Packages (PEP 420)

### Lesson 11.3 Package Packaging & Distribution

#### Topics

- Modern Packaging Standards (`pyproject.toml`, `setup.cfg`)
- Building Source Distributions and Wheels (`build` tool)
- Publishing Packages to PyPI via Twine

## Module 12 - Concurrency & Asynchronous Programming

### Lesson 12.1 Concurrency vs Parallelism Fundamentals

#### Topics

- CPU-Bound vs I/O-Bound Workloads
- Threading vs Multiprocessing vs Async IO

### Lesson 12.2 Multithreading Engine

#### Topics

- Threading Module (`threading.Thread`)
- Thread Creation and Lifecycle Management
- Race Conditions and Thread Safety
- Synchronization Primitives (`Lock`, `RLock`, `Semaphore`, `Event`, `Condition`)
- Thread Pools (`concurrent.futures.ThreadPoolExecutor`)

### Lesson 12.3 Multiprocessing Engine

#### Topics

- Multiprocessing Module (`multiprocessing.Process`)
- Bypassing the GIL for CPU-Bound Tasks
- Inter-Process Communication (IPC) via `Queue` and `Pipe`
- Shared Memory (`Value`, `Array`, `Manager`)
- Process Pools (`concurrent.futures.ProcessPoolExecutor`)

### Lesson 12.4 Asynchronous Programming (AsyncIO)

#### Topics

- AsyncIO Framework Fundamentals
- Event Loop Lifecycle and Architecture
- Coroutines Definition (`async def`) and Awaiting (`await`)
- Task Scheduling (`asyncio.create_task()`)
- Concurrent Execution (`asyncio.gather()`)
- Async Iterators and Async Context Managers

## Module 13 - Python Data Ecosystem & Hardware Interfacing

### Lesson 13.1 NumPy Array Processing

#### Topics

- NumPy N-Dimensional Array (`ndarray`) Architecture
- Array Creation Routines and Vectorized Operations
- Indexing, Slicing, and Boolean Masking
- Broadcasting Rules Engine
- Shape Manipulation and Linear Algebra Basics

### Lesson 13.2 Pandas Data Analysis

#### Topics

- Series and DataFrame Data Structures
- Data Import/Export (CSV, Excel, JSON, SQL)
- Data Cleaning, Filtering, and Missing Value Handling
- Data Aggregation and GroupBy Operations
- Merging, Joining, and Reshaping DataFrames

### Lesson 13.3 Matplotlib Data Visualization

#### Topics

- Pyplot Interface vs Object-Oriented Figure/Axes API
- Plot Types (Line, Scatter, Bar, Histogram)
- Formatting Labels, Legends, Grids, and Color Maps

### Lesson 13.4 OpenCV Image Processing Fundamentals

#### Topics

- Image Representation as NumPy Arrays
- Reading, Displaying, and Writing Images
- Color Space Transformations (BGR, Gray, HSV)
- Image Resizing, Cropping, and Geometric Transformations
- Thresholding, Edge Detection (Canny), and Contour Extraction

### Lesson 13.5 Network Requests & Hardware Serial Communication

#### Topics

- HTTP Requests via `requests` Library (GET, POST, Headers, JSON payloads, Timeouts)
- Hardware Serial Communication via `pySerial` (`serial.Serial`)
- Configuring Serial Baud Rates, Parity, Stop Bits, and Byte Reading/Writing

## Module 14 - Automated Testing, Debugging, & Performance Tuning

### Lesson 14.1 Unit Testing & Pytest Framework

#### Topics

- Unit Testing Concepts and Test-Driven Development (TDD)
- Built-in `unittest` Framework (`TestCase`, Assertions)
- Pytest Test Runner, Test Discovery, and Parameterized Tests
- Pytest Fixtures Architecture
- Test Coverage Analysis (`pytest-cov`)

### Lesson 14.2 Test Mocking

#### Topics

- Mocking Fundamentals (`unittest.mock` Module)
- Mock Objects (`Mock`, `MagicMock`)
- Patching Objects and Functions (`@patch` Decorator)
- Mocking Hardware Serial Connections and External API Requests

### Lesson 14.3 Profiling & Code Optimization

#### Topics

- Code Performance Profiling (`cProfile`, `profile`)
- Micro-Benchmarking with `timeit`
- Memory Profiling Strategies

---

# Course 5: MySQL Database

## Module 1 - Database Architecture & Relational Concepts

### Lesson 1.1 Database Systems & Relational Theory

#### Topics

- File-Based Data Storage Limitations vs Database Systems
- DBMS vs RDBMS Architecture
- Relational Model Concepts (Tables, Tuples/Rows, Attributes/Columns, Domains)
- Relational Integrity Rules (Entity Integrity, Referential Integrity)
- ACID Properties of Database Transactions

### Lesson 1.2 MySQL Server Architecture & Engines

#### Topics

- MySQL Client-Server Architecture
- MySQL Memory Architecture and Connection Handling
- SQL Parser, Query Optimizer, and Execution Engine
- Storage Engine Architecture Overview
- InnoDB Engine Deep Dive (ACID Compliance, Row-Level Locking, Foreign Keys)
- MyISAM Engine Overview vs Memory and CSV Engines

## Module 2 - Database Design, ER Modeling, & Normalization

### Lesson 2.1 Entity-Relationship (ER) Modeling

#### Topics

- Entities, Attributes (Simple, Composite, Multi-Valued, Derived), and Keys
- Relationship Types (One-to-One, One-to-Many, Many-to-Many)
- ER Diagram Symbols and Cardinality Constraints
- Mapping ER Diagrams into Relational Schemas

### Lesson 2.2 Normalization Theory & Rules

#### Topics

- Database Anomalies (Insertion, Update, Deletion Anomalies)
- Functional Dependencies and Attribute Closure
- First Normal Form (1NF) Rules
- Second Normal Form (2NF) Rules
- Third Normal Form (3NF) Rules
- Boyce-Codd Normal Form (BCNF) Rules
- Denormalization Strategies for High-Performance Systems

## Module 3 - Data Definition Language (DDL) & Integrity Constraints

### Lesson 3.1 MySQL Data Types

#### Topics

- Numeric Data Types (`TINYINT`, `INT`, `BIGINT`, `FLOAT`, `DOUBLE`, `DECIMAL`)
- Date and Time Types (`DATE`, `TIME`, `DATETIME`, `TIMESTAMP`, `YEAR`)
- String Types (`CHAR`, `VARCHAR`, `TEXT`, `BLOB`, `ENUM`)
- JSON Native Data Type Specs
- Spatial Data Types Overview

### Lesson 3.2 Data Definition Commands (DDL)

#### Topics

- Database Operations (`CREATE DATABASE`, `DROP DATABASE`, `ALTER DATABASE`)
- Table Creation (`CREATE TABLE`) Syntax
- Table Alteration (`ALTER TABLE` - Add, Modify, Drop Columns)
- Dropping vs Truncating Tables (`DROP TABLE` vs `TRUNCATE TABLE`)
- Renaming Tables and Managing Character Sets / Collations

### Lesson 3.3 Data Integrity Constraints

#### Topics

- Primary Key Constraint (`PRIMARY KEY`)
- Auto-Increment Attribute (`AUTO_INCREMENT`)
- Foreign Key Constraint (`FOREIGN KEY`) and Referential Actions (`ON DELETE`, `ON UPDATE`: `CASCADE`, `SET NULL`, `RESTRICT`, `NO ACTION`)
- Unique Constraint (`UNIQUE`)
- Not Null Constraint (`NOT NULL`)
- Default Constraint (`DEFAULT`)
- Check Constraint (`CHECK`)

## Module 4 - Data Manipulation Language (DML) & Basic Retrieval

### Lesson 4.1 Data Mutation Operations (DML)

#### Topics

- Inserting Records (`INSERT INTO ... VALUES`, Multi-row Insert, Insert from Select)
- Updating Records (`UPDATE ... SET ... WHERE`)
- Deleting Records (`DELETE FROM ... WHERE`)

### Lesson 4.2 Query Retrieval (DQL) Fundamentals

#### Topics

- Select Projection (`SELECT`) Syntax
- Column Aliases (`AS`)
- Removing Duplicates (`DISTINCT`)
- Calculated Columns and Expressions

### Lesson 4.3 Data Filtering & Sorting

#### Topics

- Conditional Filtering (`WHERE` Clause)
- Comparison Operators (`=`, `!=`, `<`, `>`, `<=`, `>=`)
- Logical Operators (`AND`, `OR`, `NOT`)
- Range Filtering (`BETWEEN ... AND ...`)
- Set Membership Filtering (`IN (...)`)
- Pattern Matching (`LIKE` with Wildcards `%`, `_`)
- Null Value Checking (`IS NULL`, `IS NOT NULL`)
- Sorting Results (`ORDER BY` ASC/DESC, Multi-Column Sorting)
- Result Pagination (`LIMIT` and `OFFSET`)

## Module 5 - Aggregation, Grouping, & SQL Functions

### Lesson 5.1 Aggregate Functions

#### Topics

- Counting Records (`COUNT(*)`, `COUNT(column)`, `COUNT(DISTINCT column)`)
- Summation and Averaging (`SUM()`, `AVG()`)
- Extreme Value Retrieval (`MIN()`, `MAX()`)
- Handling NULL Values in Aggregations

### Lesson 5.2 Grouping Data

#### Topics

- Grouping Records (`GROUP BY` Clause)
- Multi-Column Grouping
- Filtering Grouped Data (`HAVING` Clause vs `WHERE` Clause)
- SQL Query Processing Order (`FROM` -> `WHERE` -> `GROUP BY` -> `HAVING` -> `SELECT` -> `ORDER BY` -> `LIMIT`)

### Lesson 5.3 Built-in Scalar Functions

#### Topics

- String Functions (`CONCAT`, `SUBSTRING`, `LENGTH`, `UPPER`, `LOWER`, `REPLACE`, `TRIM`)
- Numeric Functions (`ROUND`, `FLOOR`, `CEIL`, `ABS`, `MOD`, `POWER`)
- Date/Time Functions (`NOW`, `CURDATE`, `CURTIME`, `DATE_ADD`, `DATEDIFF`, `DATE_FORMAT`)
- Control Flow Functions (`IF()`, `IFNULL()`, `COALESCE()`, `CASE ... WHEN ... THEN ... ELSE ... END`)

## Module 6 - Relational Joins & Set Operations

### Lesson 6.1 Relational Join Architecture

#### Topics

- Cartesian Product / Cross Join (`CROSS JOIN`)
- Equi-Joins vs Non-Equi-Joins
- Inner Join (`INNER JOIN ... ON ...`) Mechanics and Multi-Table Inner Joins

### Lesson 6.2 Outer Joins & Self Joins

#### Topics

- Left Outer Join (`LEFT JOIN ... ON ...`) Operations
- Right Outer Join (`RIGHT JOIN ... ON ...`) Operations
- Simulating Full Outer Join via Union
- Self Joins (Joining a Table with Itself for Hierarchical Structures)

### Lesson 6.3 Set Operations

#### Topics

- Union Operation (`UNION` vs `UNION ALL`)
- Set Intersection Simulation in MySQL
- Set Difference Simulation in MySQL

## Module 7 - Subqueries, Common Table Expressions (CTEs), & Window Functions

### Lesson 7.1 Subquery Operations

#### Topics

- Single-Row Subqueries (Scalar Return)
- Multi-Row Subqueries (`IN`, `ANY`, `ALL` Operators)
- Subqueries in `WHERE`, `FROM`, and `SELECT` Clauses

### Lesson 7.2 Correlated Subqueries & CTEs

#### Topics

- Correlated Subquery Execution Mechanics
- Existence Checks (`EXISTS`, `NOT EXISTS`)
- Derived Tables Architecture
- Common Table Expressions (CTEs via `WITH` Clause)
- Recursive CTEs for Hierarchical Tree Queries

### Lesson 7.3 Window Functions (MySQL 8.0+)

#### Topics

- Window Functions vs Aggregate Functions
- Over Clause (`OVER(PARTITION BY ... ORDER BY ...)`)
- Ranking Functions (`ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`)
- Value Functions (`LAG()`, `LEAD()`, `FIRST_VALUE()`, `LAST_VALUE()`)

## Module 8 - Views, Indexes, & Query Optimization

### Lesson 8.1 Database Views

#### Topics

- View Creation (`CREATE VIEW`) and Purpose
- Querying and Modifying Data through Views
- Dropping and Altering Views
- Security Abstraction Benefits of Views

### Lesson 8.2 Index Architecture & Types

#### Topics

- Index Data Structures (B-Tree Indexing vs Hash Indexing)
- Index Types (Primary Index, Unique Index, Secondary/Composite Index, Full-Text Index)
- Composite Indexes and the Leftmost Prefix Rule
- Index Overhead on DML Operations (Insert/Update/Delete Costs)

### Lesson 8.3 Query Profiling & Performance Tuning

#### Topics

- Execution Plan Analysis (`EXPLAIN` and `EXPLAIN ANALYZE` Commands)
- Key Inspection (`possible_keys`, `key`, `key_len`, `rows`, `Extra`)
- Identifying Table Scans vs Index Scans
- MySQL Slow Query Log Setup and Analysis
- Query Rewriting Strategies for Performance Optimization

## Module 9 - Stored Procedures, User Functions, Triggers, & Events

### Lesson 9.1 Stored Procedures

#### Topics

- Stored Procedure Definition (`CREATE PROCEDURE`) and Delimiters
- Parameter Modes (`IN`, `OUT`, `INOUT`)
- Variable Declarations (`DECLARE`) and Assignment (`SET`)
- Conditional Control (`IF...THEN`, `CASE`)
- Loop Statements (`WHILE`, `LOOP`, `REPEAT`)
- Invoking Procedures (`CALL`) and Dropping Procedures

### Lesson 9.2 User-Defined Functions (UDF)

#### Topics

- Creating Scalar Functions (`CREATE FUNCTION`)
- Deterministic vs Non-Deterministic Functions
- Function Invocation in SQL Queries

### Lesson 9.3 Triggers & Event Scheduler

#### Topics

- Trigger Architecture (`CREATE TRIGGER`)
- Trigger Events (`BEFORE`, `AFTER` on `INSERT`, `UPDATE`, `DELETE`)
- Pseudo-Table References (`OLD` and `NEW` Modifiers)
- Enforcing Audit Logging and Complex Validation via Triggers
- MySQL Event Scheduler (`CREATE EVENT`) for Periodic Tasks

## Module 10 - Transactions, Concurrency Control, & Locking

### Lesson 10.1 Transaction Management

#### Topics

- Transaction Definition and Boundaries
- Transaction Control Commands (`START TRANSACTION`, `COMMIT`, `ROLLBACK`)
- Savepoints (`SAVEPOINT`, `ROLLBACK TO SAVEPOINT`)
- Autocommit Mode Management (`SET autocommit = 0`)

### Lesson 10.2 Concurrency Anomalies & Isolation Levels

#### Topics

- Concurrency Read Anomalies (Dirty Read, Non-Repeatable Read, Phantom Read)
- Transaction Isolation Levels (`READ UNCOMMITTED`, `READ COMMITTED`, `REPEATABLE READ`, `SERIALIZABLE`)
- InnoDB Multi-Version Concurrency Control (MVCC) Engine

### Lesson 10.3 Locking Mechanics

#### Topics

- Lock Granularity (Table Locks vs Row-Level Locks)
- Shared Locks (S) vs Exclusive Locks (X)
- Intent Locks (IS, IX)
- Reading Locks (`FOR UPDATE`, `FOR SHARE`)
- Deadlock Causes, Detection, and Resolution Strategies

## Module 11 - Database Security, Administration, & Replication

### Lesson 11.1 User Management & Security

#### Topics

- Creating Users (`CREATE USER`) and Authentication Plugins
- Granting and Revoking Privileges (`GRANT`, `REVOKE`)
- Privilege Hierarchy (Global, Database, Table, Column Level)
- Password Policies and Role-Based Access Control (RBAC)

### Lesson 11.2 Backup, Restore, & Recovery

#### Topics

- Logical Backups via `mysqldump` Utility
- Physical Backups Overview
- Restoring Databases from SQL Dumps
- Binary Logging (`binlog`) Setup and Point-In-Time Recovery (PITR)

### Lesson 11.3 Replication Concepts

#### Topics

- MySQL Primary-Replica (Master-Slave) Replication Architecture
- Asynchronous vs Semi-Synchronous Replication
- High Availability Concepts

## Module 12 - MySQL Integration with Python

### Lesson 12.1 Low-Level Database Drivers

#### Topics

- Connecting Python to MySQL (`mysql-connector-python`, `PyMySQL`)
- Connection Objects and Configuration Arguments
- Cursor Objects (`cursor.execute()`, `cursor.executemany()`)
- Parameterized Queries to Prevent SQL Injection Vulnerabilities
- Fetching Query Results (`fetchone()`, `fetchall()`, `fetchmany()`)
- Managing Database Transactions via Python (`commit()`, `rollback()`)
- Connection Pooling Strategies

### Lesson 12.2 ORM Architectural Concepts

#### Topics

- Object-Relational Impedance Mismatch Problem
- Active Record vs Data Mapper Patterns
- Declarative Mapping Overview

---

# Course 6: Flask

## Module 1 - Microframework Architecture & Setup

### Lesson 1.1 Microframework Architecture & Design Philosophy

#### Topics

- Microframework Philosophy vs Monolithic Frameworks
- WSGI (Web Server Gateway Interface) Standard Specification (PEP 3333)
- Flask Core Dependencies: Werkzeug WSGI Toolkit and Jinja2 Template Engine
- Flask Application Instance (`Flask(__name__)`) Architecture

### Lesson 1.2 Environment & Application Initialization

#### Topics

- Virtual Environment Setup and Flask Installation
- "Hello World" Application Anatomy
- Development Server Execution (`flask run`)
- Environment Variables (`FLASK_APP`, `FLASK_ENV`, `FLASK_DEBUG`)
- Application Configuration Systems (`app.config` object, `.env` files, Configuration Classes)

## Module 2 - Routing, Requests, & Responses

### Lesson 2.1 Routing Architecture

#### Topics

- Route Registration via Decorator (`@app.route()`)
- Dynamic URL Parameters (`<variable_name>`)
- Path Converters (`string`, `int`, `float`, `path`, `uuid`)
- HTTP Method Specification (`methods=['GET', 'POST', ...]`)
- Modern Route Decorators (`@app.get()`, `@app.post()`)
- Endpoint Naming and URL Building (`url_for()`)

### Lesson 2.2 Request Object Handling

#### Topics

- Importing Request Context (`request` object)
- Retrieving Query Parameters (`request.args`)
- Retrieving Form Data (`request.form`)
- Retrieving JSON Payloads (`request.get_json()`, `request.json`)
- Retrieving Headers, Cookies, and Remote Address
- Handling File Upload Payloads (`request.files`)

### Lesson 2.3 Response Generation & Headers

#### Topics

- Returning Strings, Tuples `(body, status, headers)`, and HTML
- Explicit Response Objects (`make_response()`)
- JSON Responses (`jsonify()`)
- Redirections (`redirect()`)
- Aborting Requests and HTTP Errors (`abort()`)
- Custom Response Headers and Cookie Setting (`response.set_cookie()`)

## Module 3 - Context System, Middleware, & Request Lifecycle

### Lesson 3.1 Application Context & Request Context

#### Topics

- Context Locals Concept in Flask
- Application Context (`current_app`, `g` object)
- Request Context (`request`, `session`)
- Context Lifecycles and Context Pushing/Popping Mechanics

### Lesson 3.2 Request Hooks & Middleware

#### Topics

- Request Lifecycle Hooks (`@app.before_request`, `@app.after_request`, `@app.teardown_request`, `@app.teardown_appcontext`)
- WSGI Middleware Integration for Flask Applications

## Module 4 - Templating System (Jinja2)

### Lesson 4.1 Jinja2 Template Engine Basics

#### Topics

- Rendering Templates (`render_template()`)
- Variable Interpolation `{{ variable }}`
- Control Flow Expressions (`{% if %}`, `{% for %}`)
- Template Comments (`{# comment #}`)
- Accessing Flask Objects in Templates (`request`, `session`, `g`, `url_for`)

### Lesson 4.2 Template Inheritance & Components

#### Topics

- Base Template Layout Strategy
- Defining and Overriding Blocks (`{% block content %}`)
- Extending Base Templates (`{% extends "base.html" %}`)
- Sub-Template Inclusion (`{% include "header.html" %}`)
- Reusable Macros (`{% macro %}`) Creation and Importing

### Lesson 4.3 Custom Filters & Security

#### Topics

- Jinja2 Built-in Filters (`upper`, `lower`, `default`, `length`, `join`)
- Custom Filter Registration (`@app.template_filter()`)
- Escaping HTML and XSS Prevention (`autoescape`, `safe` filter)

## Module 5 - Web Forms & Input Validation (Flask-WTF)

### Lesson 5.1 WTForms & Flask-WTF Extension

#### Topics

- Flask-WTF Setup and Form Class Definition
- Field Types (`StringField`, `PasswordField`, `BooleanField`, `SubmitField`, `SelectField`, `TextAreaField`)
- Form Rendering in Jinja2 Templates

### Lesson 5.2 Form Validation & Error Display

#### Topics

- Built-in Form Validators (`DataRequired`, `Email`, `Length`, `EqualTo`, `NumberRange`)
- Custom Field Validation Methods
- Validating Form Submissions (`validate_on_submit()`)
- Inline Form Error Display in HTML Layouts

### Lesson 5.3 CSRF Protection & File Uploads

#### Topics

- Cross-Site Request Forgery (CSRF) Vulnerability Mechanics
- Enabling CSRF Protection (`CSRFProtect`)
- CSRF Token Embedding in Forms
- File Field Upload Validation (`FileField`, `FileAllowed`, `FileRequired`)
- Secure Filename Sanitization (`secure_filename()`)

## Module 6 - Relational Database Integration & SQLAlchemy ORM

### Lesson 6.1 Flask-SQLAlchemy Extension Architecture

#### Topics

- Integrating Flask-SQLAlchemy (`SQLAlchemy(app)`)
- Database Connection String Configuration (`SQLALCHEMY_DATABASE_URI`)
- Declarative Base Model Definition (`db.Model`)
- Column Data Types and Constraints Definition

### Lesson 6.2 Relational Model Relationships

#### Topics

- One-to-Many Relationships (`db.relationship()`, `db.ForeignKey()`)
- Many-to-Many Relationships (Association Tables)
- One-to-One Relationships
- Relationship Options (`backref`, `back_populates`, `lazy` loading strategies)
- Cascading Deletes (`cascade="all, delete-orphan"`)

### Lesson 6.3 CRUD Operations via SQLAlchemy

#### Topics

- Inserting Records (`db.session.add()`, `db.session.add_all()`)
- Querying Data (`Model.query.all()`, `.get()`, `.filter()`, `.filter_by()`, `.first()`, `.order_by()`)
- Query Pagination (`Model.query.paginate()`)
- Updating and Deleting Records (`db.session.delete()`)
- Transaction Management (`db.session.commit()`, `db.session.rollback()`)

### Lesson 6.4 Schema Migrations (Flask-Migrate)

#### Topics

- Database Schema Evolution Challenges
- Flask-Migrate Extension Integration (Alembic Engine)
- Migration Environment Initialization (`flask db init`)
- Generating Migration Scripts (`flask db migrate`)
- Applying and Downgrading Migrations (`flask db upgrade`, `flask db downgrade`)

## Module 7 - Sessions, Cookies, & User Authentication

### Lesson 7.1 Cookie Handling & Client-Side Sessions

#### Topics

- Setting and Reading Cookies in Flask
- Flask Client-Side Session Mechanism (`session` object)
- Secret Key Configuration (`app.secret_key`) for Cryptographic Signing
- Session Security Attributes (`PERMANENT_SESSION_LIFETIME`, `SESSION_COOKIE_HTTPONLY`, `SESSION_COOKIE_SECURE`, `SESSION_COOKIE_SAMESITE`)
- Server-Side Sessions via Flask-Session Extension

### Lesson 7.2 User Authentication with Flask-Login

#### Topics

- User Model Requirements (`UserMixin` class)
- LoginManager Setup (`LoginManager(app)`)
- User Loader Callback Function (`@login_manager.user_loader`)
- Password Hashing and Verification (`generate_password_hash()`, `check_password_hash()`)
- User Login (`login_user()`) and Logout (`logout_user()`)

### Lesson 7.3 Access Control & Authorization

#### Topics

- Protecting Routes (`@login_required` decorator)
- Handling Unauthorized Access Attempts
- Custom Decorators for Role-Based Access Control (RBAC)

## Module 8 - Application Structuring & Blueprints

### Lesson 8.1 Modular Architecture with Blueprints

#### Topics

- Monolithic Single-File Flask App Limitations
- Flask Blueprint Architecture (`Blueprint()`)
- Registering Blueprints with Application Instance (`app.register_blueprint()`)
- Blueprint-Specific Route Definitions, Template Folders, and Static Folders
- Modular URL Prefixing

### Lesson 8.2 Application Factory Pattern

#### Topics

- Application Factory Function (`create_app()`) Architecture
- Deferred Extension Initialization (`db.init_app(app)`)
- Dynamic Configuration Loading by Environment
- Eliminating Circular Dependencies in Flask Packages

## Module 9 - RESTful APIs & JWT Authentication

### Lesson 9.1 RESTful API Architecture

#### Topics

- REST Design Principles in Flask
- Returning JSON Payload Structures
- Status Code Standardization for APIs
- Handling Error Responses as JSON

### Lesson 9.2 API Serialization (Flask-Marshmallow)

#### Topics

- Serialization and Deserialization Concepts
- Marshmallow Schema Definitions (`Schema`)
- Model Schema Mapping (`SQLAlchemyAutoSchema`)
- Validating Incoming Request Payloads via Schemas

### Lesson 9.3 JSON Web Token (JWT) Authentication

#### Topics

- JWT Structure (Header, Payload, Signature)
- Flask-JWT-Extended Integration
- Token Generation (`create_access_token()`, `create_refresh_token()`)
- Endpoint Protection via JWT (`@jwt_required()`)
- Token Refreshing Mechanisms and Revocation / Blacklisting

## Module 10 - Caching, Background Tasks, & Mail Integration

### Lesson 10.1 Application Caching (Flask-Caching)

#### Topics

- Caching Strategies for Web Applications
- Flask-Caching Extension Setup
- Cache Backends (Simple, Redis, Memcached)
- View Function Caching (`@cache.cached()`)
- Function Memoization (`@cache.memoize()`)

### Lesson 10.2 Asynchronous Tasks with Celery

#### Topics

- Offloading Heavy Computations from Request-Response Loop
- Celery Task Queue Architecture
- Message Brokers Integration (Redis / RabbitMQ)
- Defining Celery Tasks in Flask
- Running Celery Workers and Task Results Retrieval

### Lesson 10.3 Email Delivery (Flask-Mail)

#### Topics

- SMTP Configuration in Flask
- Creating Messages (`Message` class)
- Sending Synchronous and Asynchronous Emails

## Module 11 - Error Handling, Logging, & Testing

### Lesson 11.1 Custom Error Handling

#### Topics

- Error Handler Registration (`@app.errorhandler(404)`)
- Rendering Custom HTML Error Pages
- JSON Error Responses for API Routes

### Lesson 11.2 Application Logging

#### Topics

- Flask Application Logger (`app.logger`)
- Configuring Log Handlers and Output Formats in Production

### Lesson 11.3 Automated Testing with Pytest

#### Topics

- Pytest Setup for Flask Applications
- Flask Test Client (`app.test_client()`) Fixtures
- Testing Routes, Forms, Authentication, and Database Models

## Module 12 - Production Deployment & Performance Tuning

### Lesson 12.1 Production WSGI Application Servers

#### Topics

- Development Server Limitations
- Production WSGI Servers (Gunicorn, uWSGI)
- Configuring Gunicorn Worker Processes and Threads

### Lesson 12.2 Reverse Proxy Setup (Nginx)

#### Topics

- Nginx Architecture as Reverse Proxy
- Nginx Proxy Configuration (`proxy_pass`) for Gunicorn
- Static File Delivery via Nginx
- SSL/TLS Certificate Installation (Let's Encrypt / Certbot)

### Lesson 12.3 Containerization with Docker

#### Topics

- Dockerizing Flask Applications (`Dockerfile`)
- Docker Compose for Orchestrating Flask, MySQL, Redis, and Nginx

---

# Course 7: FastAPI

## Module 1 - Modern Web Architecture & FastAPI Core

### Lesson 1.1 Modern Asynchronous Web Frameworks

#### Topics

- Web Framework Generation Evolution (WSGI to ASGI)
- FastAPI Framework Core Capabilities and Performance Metrics
- Comparison with Flask, Django, and NodeJS Express
- Core Dependencies: Starlette Engine and Pydantic Data Engine

### Lesson 1.2 ASGI Engine & Uvicorn Server

#### Topics

- ASGI Specification (PEP 3143) Overview
- Asynchronous Event Loop Integration
- ASGI Servers Architecture (Uvicorn, Hypercorn)
- Running FastAPI Development Server (`uvicorn main:app --reload`)

### Lesson 1.3 Application Setup & Environment

#### Topics

- FastAPI Package Installation (`fastapi[standard]`)
- Application Instance Instantiation (`FastAPI()`)
- First Endpoint Definition (`@app.get("/")`)

## Module 2 - Automatic Documentation & OpenAPI Specifications

### Lesson 2.1 OpenAPI Standard & Interactive UI

#### Topics

- OpenAPI (formerly Swagger) 3.0 Specification
- Interactive Swagger UI Documentation (`/docs`)
- ReDoc Documentation Interface (`/redoc`)
- Customizing OpenAPI Documentation URLs

### Lesson 2.2 API Metadata & Documentation Enrichment

#### Topics

- Application Title, Description, Version, and License Configuration
- Route Tags Grouping (`tags=["users"]`)
- Operation Summary, Description, and Response Descriptions
- Deprecating Endpoints via Metadata (`deprecated=True`)

## Module 3 - Request Data Processing & Pydantic Validation

### Lesson 3.1 Path Parameters & Type Enforcement

#### Topics

- Path Parameter Syntax (`/items/{item_id}`)
- Python Type Hints for Automatic Path Parameter Conversion
- Path Validation and Metadata (`Path(gt=0, title="The ID")`)
- Enum Parameter Constraining via Standard Python `Enum`

### Lesson 3.2 Query Parameters & Validation

#### Topics

- Optional vs Required Query Parameters
- Query Parameter Default Values
- Query Parameter Type Conversion (Booleans, Integers, Lists)
- Query Validation and Constraints (`Query(min_length=3, max_length=50, pattern="^a")`)

### Lesson 3.3 Request Body Validation via Pydantic Models

#### Topics

- Pydantic BaseModel Class Inheritance
- Field Declarations and Type Annotations
- JSON Payload Parsing and Deserialization
- Nested Pydantic Models and Lists of Models
- Pydantic `Field()` Validation Constraints (`gt`, `lt`, `min_length`, `max_length`)
- Custom Validators (`@field_validator`, `@model_validator`)
- Schema Examples Configuration (`json_schema_extra`)

### Lesson 3.4 Multi-Source Parameter Declarations

#### Topics

- Combining Path, Query, and Request Body Parameters in Endpoint Signatures
- Singular Values in Request Body (`Body()`)

## Module 4 - Form Handling, File Uploads, & Response Engine

### Lesson 4.1 Form Submissions & File Handling

#### Topics

- Form Data Processing (`Form(...)`)
- File Upload Controls (`File(...)`, `UploadFile` class)
- `UploadFile` Attributes (`filename`, `content_type`, `file`)
- Asynchronous File Operations (`await file.read()`, `await file.write()`)
- Validating Uploaded File Sizes and MIME Types

### Lesson 4.2 Headers, Cookies, & Request Information

#### Topics

- Extracting Custom Headers (`Header(...)`)
- Automatic Hyphen-to-Underscore Header Name Conversion
- Extracting Cookies (`Cookie(...)`)
- Accessing Low-Level Request Object (`Request`)

### Lesson 4.3 Response Models & Status Codes

#### Topics

- Explicit Response Status Codes (`status_code=status.HTTP_201_CREATED`)
- Response Data Filtering via Response Models (`response_model=UserOut`)
- Excluding Default or Unset Values (`response_model_exclude_unset=True`)
- Include and Exclude Sets (`response_model_include`, `response_model_exclude`)

### Lesson 4.4 Advanced Response Classes

#### Topics

- Custom Response Classes (`JSONResponse`, `HTMLResponse`, `PlainTextResponse`)
- Redirect Responses (`RedirectResponse`)
- File Downloads (`FileResponse`)
- Real-Time Data Streaming Responses (`StreamingResponse`)

## Module 5 - FastAPI Dependency Injection (DI) System

### Lesson 5.1 Dependency Injection Fundamentals

#### Topics

- Dependency Injection Philosophy and Architectural Advantages
- Creating Dependency Functions
- Injecting Dependencies via `Depends()` Signature Parameter
- Shared Logic Encapsulation via Dependencies

### Lesson 5.2 Advanced Dependency Patterns

#### Topics

- Class-Based Dependencies (`__call__` method instantiation)
- Parameterized Class Dependencies
- Hierarchical Sub-Dependencies (Dependencies depending on other dependencies)
- Path Operation Decorator Dependencies (`dependencies=[Depends(...)]`)
- Global Application Dependencies (`FastAPI(dependencies=[...])`)

### Lesson 5.3 Context Manager & Yield Dependencies

#### Topics

- Dependencies with `yield` Statement
- Execution Lifecycle (Pre-endpoint execution vs Post-endpoint cleanup)
- Managing Resource Connections (Database Sessions, Files, Sockets) via Yield Dependencies

## Module 6 - Asynchronous Database Access with SQLAlchemy 2.0 & Alembic

### Lesson 6.1 Async Database Drivers & Orm Configuration

#### Topics

- Synchronous vs Asynchronous I/O Bottlenecks in Data Access
- Async Drivers (`aiomysql` for MySQL, `asyncpg` for PostgreSQL)
- SQLAlchemy 2.0 Async Engine Setup (`create_async_engine()`)
- Async Session Factory (`async_sessionmaker()`, `AsyncSession`)

### Lesson 6.2 Database Dependency Pipeline

#### Topics

- Building Async Database Session Yield Dependency (`get_db`)
- Handling Automatic Session Closure and Exception Rollbacks

### Lesson 6.3 Async CRUD Operations

#### Topics

- Defining Declarative Models inheriting from `DeclarativeBase`
- Async Queries Execution (`select()`, `await session.execute()`, `scalars()`)
- Async Mutations (Insert, Update, Delete) and Commit Operations (`await session.commit()`)

### Lesson 6.4 Schema Evolution with Alembic

#### Topics

- Alembic Integration with Async SQLAlchemy Models
- Asynchronous Migration Script Generation and Execution

## Module 7 - Security, OAuth2, & JWT Authentication

### Lesson 7.1 Security Utilities Framework

#### Topics

- FastAPI `fastapi.security` Module
- Security Schemes Overview (HTTP Basic, HTTP Bearer, API Keys)

### Lesson 7.2 OAuth2 & Password Flow Architecture

#### Topics

- OAuth2 Specifications Framework
- OAuth2 Password Bearer Scheme (`OAuth2PasswordBearer`)
- Handling Login Request Forms (`OAuth2PasswordRequestForm`)
- Password Hashing Engine (`passlib` with `bcrypt` / `pwdlib`)

### Lesson 7.3 JSON Web Token (JWT) Implementation

#### Topics

- Generating Cryptographic JWT Access Tokens (`pyjwt`)
- Token Expiration and Payload Encoding
- Current User Extraction Dependency (`get_current_user`)
- Validating Authorization Bearer Headers

### Lesson 7.4 Scope-Based Fine-Grained Authorization

#### Topics

- OAuth2 Scopes Concept (`SecurityScopes`)
- Injecting Scopes into Route Endpoints via `Security()`
- User Role and Permission Validation Pipeline

## Module 8 - Middleware, CORS, & Exception Architecture

### Lesson 8.1 Custom Middleware Construction

#### Topics

- ASGI Middleware Architecture
- Writing HTTP Middleware (`@app.middleware("http")`)
- Request Interception, Header Injection, and Processing Time Logging

### Lesson 8.2 Cross-Origin Resource Sharing (CORS)

#### Topics

- CORS Security Constraints
- Configuring `CORSMiddleware`
- Allowing Origins, Credentials, HTTP Methods, and Headers

### Lesson 8.3 Custom Exception Handling

#### Topics

- Raising HTTP Exceptions (`HTTPException`)
- Creating Custom Exception Classes
- Global Custom Exception Handlers (`@app.exception_handler()`)
- Overriding Default Validation Error Handlers (`RequestValidationError`)

## Module 9 - Real-Time Communication with WebSockets

### Lesson 9.1 WebSocket Architecture

#### Topics

- Full-Duplex Communication Protocol (RFC 6455)
- HTTP Handshake Upgrade to WebSocket Connection
- WebSockets vs HTTP Polling / Server-Sent Events

### Lesson 9.2 FastAPI WebSocket Handlers

#### Topics

- WebSocket Endpoint Decorator (`@app.websocket("/ws")`)
- WebSocket Connection Handshake (`await websocket.accept()`)
- Receiving Text and JSON (`await websocket.receive_text()`, `receive_json()`)
- Sending Text and JSON (`await websocket.send_text()`, `send_json()`)
- Managing Connection Closure (`WebSocketDisconnect`)

### Lesson 9.3 Connection Manager Architecture

#### Topics

- Building a Connection Manager Class
- Tracking Active Client Connections
- Unicast vs Broadcast Messaging Mechanisms

## Module 10 - Background Tasks, Lifespan Events, & Performance

### Lesson 10.1 Background Tasks Processing

#### Topics

- FastAPI `BackgroundTasks` Class
- Adding Execution Tasks (`background_tasks.add_task()`)
- Post-Response Async Operations (Log writing, Email delivery, Telemetry processing)

### Lesson 10.2 Application Lifespan Events

#### Topics

- Modern Lifespan Event Context Manager (`@asynccontextmanager`)
- Startup Tasks Execution (Database Connection Pooling, AI Model Loading)
- Shutdown Tasks Execution (Resource Cleanup, Socket Release)

### Lesson 10.3 Testing & Production Deployment

#### Topics

- Testing FastAPI Applications via Pytest and `httpx.AsyncClient`
- Overriding Dependencies in Tests (`app.dependency_overrides`)
- Production Deployment using Gunicorn with Uvicorn Worker Class (`uvicorn.workers.UvicornWorker`)
- High-Performance Containerization with Docker

---

# Course 8: IoT & Embedded Systems

## Module 1 - Electrical Engineering & Circuit Fundamentals

### Lesson 1.1 Core Electrical Physics

#### Topics

- Charge ($Q$), Current ($I$), Voltage ($V$), Resistance ($R$)
- Electrical Power ($P = VI = I^2R = V^2/R$) and Energy ($E = P \cdot t$)
- Alternating Current (AC) vs Direct Current (DC)
- Signal Waveforms (Sine, Square, Triangular, PWM)
- Frequency ($f$), Period ($T$), Amplitude, Phase, Peak-to-Peak, RMS Values

### Lesson 1.2 Circuit Analysis Laws

#### Topics

- Ohm’s Law ($V = IR$)
- Kirchhoff’s Voltage Law (KVL)
- Kirchhoff’s Current Law (KCL)
- Resistors in Series and Parallel Configurations
- Capacitors in Series and Parallel Configurations
- Inductors in Series and Parallel Configurations
- Voltage Divider Circuit Calculation and Load Effects
- Current Divider Circuit Calculations

### Lesson 1.3 Diagnostic & Measurement Instrumentation

#### Topics

- Digital Multimeter (Voltage, Current, Resistance, Continuity, Diode Test)
- Digital Storage Oscilloscope (DSO) Operation (Probing, Triggering, Timebase, Coupling)
- Logic Analyzers (Protocol Decoding: UART, SPI, I2C)
- Adjustable Bench Power Supplies and Current Limiting

## Module 2 - Analog Electronics Components & Circuit Design

### Lesson 2.1 Passive Components

#### Topics

- Fixed & Variable Resistors (Carbon, Metal Film, Potentiometers, LDRs, Thermistors NTC/PTC)
- Resistor Color Codes and SMD Markings (E24, E96 Series)
- Ceramic, Electrolytic, and Tantalum Capacitors
- Decoupling and Bypass Capacitor Placement Strategies
- Inductors, Chokes, Ferrite Beads, and Energy Storage

### Lesson 2.2 Semiconductor Diodes & Applications

#### Topics

- P-N Junction Physics and Forward/Reverse Bias
- Standard Signal Diodes (1N4148) and Power Diodes (1N4007)
- Schottky Diodes (Low Forward Voltage Drop, Fast Switching)
- Zener Diodes and Voltage Regulation Circuits
- Light Emitting Diodes (LEDs) and Current-Limiting Resistor Calculations
- Flyback / Freewheeling Diodes for Inductive Load Protection

### Lesson 2.3 Transistors & Solid-State Switching

#### Topics

- Bipolar Junction Transistors (BJT: NPN vs PNP)
- BJT Operating Regions (Cutoff, Active, Saturation)
- BJT as a Digital Switch and Relay Driver
- Field Effect Transistors (N-Channel and P-Channel MOSFETs)
- MOSFET Gate Threshold Voltage ($V_{GS(th)}$), On-Resistance ($R_{DS(on)}$), Logic-Level MOSFETs
- High-Side vs Low-Side Switching Architecture

### Lesson 2.4 Operational Amplifiers (Op-Amps)

#### Topics

- Ideal vs Real Op-Amp Characteristics (LM358, TL072)
- Inverting Amplifier Configuration
- Non-Inverting Amplifier Configuration
- Voltage Follower / Buffer Configuration
- Differential Amplifier Configuration
- Op-Amp Comparators and Hysteresis (Schmitt Triggers)

## Module 3 - Digital Electronics & Logic Systems

### Lesson 3.1 Number Systems & Digital Codes

#### Topics

- Binary, Octal, Decimal, Hexadecimal Number Systems
- Base Conversions
- Two's Complement Signed Number Representation
- American Standard Code for Information Interchange (ASCII)
- Binary Coded Decimal (BCD)

### Lesson 3.2 Boolean Algebra & Logic Gates

#### Topics

- Fundamental Logic Gates (AND, OR, NOT)
- Universal Logic Gates (NAND, NOR)
- Exclusive Logic Gates (XOR, XNOR)
- Truth Tables and Boolean Algebra Laws
- De Morgan’s Theorems
- Karnaugh Maps (K-Maps) Logic Simplification (2, 3, 4 Variables)

### Lesson 3.3 Combinational & Sequential Logic

#### Topics

- Adders (Half Adder, Full Adder) and Subtractors
- Multiplexers (MUX) and Demultiplexers (DEMUX)
- Decoders and Encoders
- Latches (SR Latch) vs Flip-Flops
- Flip-Flop Types (D, JK, T Flip-Flops)
- Shift Registers (74HC595 SIPO Shift Register)
- Asynchronous and Synchronous Counters

### Lesson 3.4 Logic Families & Voltage Level Shifting

#### Topics

- TTL (5V) vs CMOS (3.3V / 1.8V) Logic Families
- Logic Voltage Thresholds ($V_{IL}, V_{IH}, V_{OL}, V_{OH}$)
- Bidirectional Logic Level Shifters (MOSFET-Based, Dedicated ICs like TXS0108E)
- Resistor Divider Level Shifting Limitations

## Module 4 - Embedded Systems Architecture & Microcontrollers

### Lesson 4.1 Microcontroller Core Architecture

#### Topics

- Microprocessor vs Microcontroller (MCU) Architecture
- Von Neumann vs Harvard Memory Architectures
- RISC vs CISC Instruction Set Architectures
- Microcontroller Memory Layout (Flash, SRAM, EEPROM)
- Central Processing Unit (CPU), Registers, Program Counter (PC), Stack Pointer (SP)

### Lesson 4.2 Core Peripherals & Clock Management

#### Topics

- Clock Systems (Internal RC Oscillators, External Quartz Crystals, Phase-Locked Loops - PLL)
- Reset Sources and Power-On Reset (POR)
- Brown-Out Detector (BOD) Circuitry
- Watchdog Timers (WDT, Windowed WDT) for Fault Recovery

## Module 5 - Hardware Platforms Deep Dive

### Lesson 5.1 Arduino Platform & ATmega328P

#### Topics

- ATmega328P Microcontroller Architecture
- Arduino UNO Pinout and Board Layout
- Bare-Metal C vs Arduino Framework
- Direct Port Manipulation Registers (DDRx, PORTx, PINx)

### Lesson 5.2 ESP8266 Wi-Fi System-on-Chip (SoC)

#### Topics

- Tensilica L106 32-Bit Core Architecture
- Memory Partitioning and External SPI Flash
- ESP-8266EX GPIO Constraints and Pin Multiplexing

### Lesson 5.3 ESP32 Dual-Core Flagship SoC

#### Topics

- Xtensa Dual-Core 32-Bit LX6 Microprocessor Architecture
- Ultra-Low Power (ULP) Co-Processor
- Memory Layout (520 KB SRAM, Embedded/External PSRAM)
- Wi-Fi (802.11 b/g/n) and Dual-Mode Bluetooth (Classic & BLE) Subsystems
- ESP-IDF (Espressif IoT Development Framework) vs Arduino ESP32 Core
- Flash Partition Tables (`partitions.csv`)

### Lesson 5.4 Raspberry Pi Pico & Pico W (RP2040)

#### Topics

- Dual ARM Cortex-M0+ @ 133 MHz Architecture
- Programmable I/O (PIO) State Machines Deep Dive
- CYW43439 Wireless Controller on Pico W
- MicroPython vs C/C++ SDK Development

### Lesson 5.5 Raspberry Pi Zero 2 W (Single Board Computer)

#### Topics

- Broadcom BCM2710A1 Quad-Core 64-Bit ARM Cortex-A53
- Embedded Linux Operating System (Raspberry Pi OS)
- SBC Gateway vs Microcontroller Division of Responsibilities

## Module 6 - Low-Level Peripheral Programming

### Lesson 6.1 General Purpose Input/Output (GPIO)

#### Topics

- GPIO Modes (Digital Input, Digital Output, Push-Pull, Open-Drain)
- Internal Pull-Up and Pull-Down Resistors
- Mechanical Switch Bouncing Physics
- Hardware RC Debouncing Filters
- Software Debouncing Algorithms (State Machines, Timer-Based)

### Lesson 6.2 Analog-to-Digital Converter (ADC)

#### Topics

- Successive Approximation Register (SAR) ADC Architecture
- ADC Resolution (8-Bit, 10-Bit, 12-Bit) and Quantization Error
- Reference Voltage ($V_{REF}$) and Calculation Formulas
- Sampling Rate, Settling Time, and Noise Reduction
- Attenuation Settings and ADC Non-Linearity Calibration (ESP32 ADC Calibration)

### Lesson 6.3 Digital-to-Analog Converter (DAC) & Pulse Width Modulation (PWM)

#### Topics

- R-2R Ladder and Internal DAC Peripherals
- PWM Signal Generation (Frequency, Resolution, Duty Cycle Calculations)
- Hardware Timer-Based PWM Peripherals (ESP32 LEDC Peripheral)
- Applications: LED Dimming, DC Motor Speed Control, Servo Position Control

### Lesson 6.4 Interrupt Systems & Timers

#### Topics

- Polling vs Interrupt Driven Architecture
- Hardware External Pin Interrupts (Rising, Falling, Change, Low/High Level)
- Interrupt Service Routine (ISR) Programming Rules
- The `volatile` Keyword in C/C++
- Critical Sections and Disabling Interrupts
- Hardware Timers and Timer Interrupts

## Module 7 - Wired Communication Protocols

### Lesson 7.1 UART (Universal Asynchronous Receiver-Transmitter)

#### Topics

- Asynchronous Framing (Start Bit, Data Bits, Parity Bit, Stop Bits)
- Baud Rate Standard Speeds (9600, 115200, etc.) and Error Percentages
- Hardware Flow Control (RTS / CTS)
- RS-232 Voltage Level Converter (MAX232)
- RS-485 Differential Signal Standard and Modbus RTU Protocol

### Lesson 7.2 I2C (Inter-Integrated Circuit) Protocol

#### Topics

- Synchronous Multi-Master / Multi-Slave 2-Wire Protocol (SDA, SCL)
- Open-Drain Outputs and Pull-Up Resistor Calculations
- 7-Bit and 10-Bit Slave Addressing Structure
- START, STOP, ACK, NACK Conditions
- Clock Stretching and Bus Arbitration
- I2C Scanner Software Implementation

### Lesson 7.3 SPI (Serial Peripheral Interface) Protocol

#### Topics

- Synchronous Full-Duplex 4-Wire Protocol (MOSI, MISO, SCK, CS/SS)
- Master-Slave Architecture
- Clock Polarity (CPOL) and Clock Phase (CPHA) Modes (SPI Modes 0, 1, 2, 3)
- High-Speed Data Transfers and Daisy-Chaining Devices

### Lesson 7.4 CAN (Controller Area Network) Bus

#### Topics

- ISO 11898 Standard for Automotive and Industrial Systems
- Differential Signaling (CAN-High, CAN-Low)
- CAN Frame Structure (Standard 11-bit ID vs Extended 29-bit ID)
- Bitwise Arbitration and Message Priority
- CAN Controllers (MCP2515) and Transceivers (SN65HVD230)

## Module 8 - Sensor & Actuator Interfacing

### Lesson 8.1 Environmental Sensors

#### Topics

- Temperature & Humidity Sensors (DHT11/DHT22 One-Wire Protocol, BME280 I2C/SPI)
- Digital Temperature Probe (DS18B20 1-Wire Bus Protocol)
- Barometric Pressure Sensors (BMP280)
- Gas and Air Quality Sensors (MQ-2, MQ-135, SGP30 Multi-Pixel Gas Sensor)

### Lesson 8.2 Motion, Position, & Distance Sensors

#### Topics

- Inertial Measurement Units (IMU: MPU6050 6-DOF Accelerometer + Gyroscope)
- I2C Data Acquisition and Complementary / Kalman Filter Fusion
- Ultrasonic Distance Sensor (HC-SR04 Trigger and Echo Timing)
- Time-of-Flight (ToF) Laser Distance Sensor (VL53L0X)
- Passive Infrared (PIR) Motion Detectors

### Lesson 8.3 Optical, Bio, & Soil Sensors

#### Topics

- Ambient Light Sensor (BH1750 $I^2C$)
- Pulse Oximeter and Heart Rate Sensor (MAX30102 $I^2C$)
- Resistive vs Capacitive Corrosion-Resistant Soil Moisture Sensors

### Lesson 8.4 Actuators & Motor Interfacing

#### Topics

- Electromagnetic Relays and Optocoupler Isolation (PC817)
- Solid-State Relays (SSR)
- DC Motor Control via H-Bridge Drivers (L298N, DRV8833)
- Servo Motors Control (PWM 50 Hz Protocol)
- Stepper Motors (Unipolar vs Bipolar, A4988 / TMC2209 Drivers, Microstepping)

### Lesson 8.5 Display Technology Interfacing

#### Topics

- Alphanumeric Character LCDs (16x2, 20x4 with PCF8574 $I^2C$ Backpack)
- Monochromatic OLED Displays (0.96 inch SSD1306 $I^2C$/SPI)
- Color TFT LCD Displays (ST7735, ILI9341 via SPI)
- E-Paper / E-Ink Displays Low-Power Drivers

## Module 9 - Power Electronics, Battery Management, & Low-Power Design

### Lesson 9.1 Power Regulation Architectures

#### Topics

- Linear Voltage Regulators (7805, AMS1117, Low Dropout LDOs)
- Switching Regulators (Buck Converter / Step-Down, Boost Converter / Step-Up)
- Power Efficiency Comparison: Linear vs Switching Regulators

### Lesson 9.2 Battery Technologies & Charging Systems

#### Topics

- Li-Ion and LiPo Chemistry Characteristics
- Nominal Voltage, Charge Voltage, Cutoff Voltage
- TP4056 Linear Li-Ion Battery Charger IC with Protection Circuitry
- Battery Management Systems (BMS) for Multi-Cell Packs
- Fuel Gauge / Coulomb Counting ICs

### Lesson 9.3 Low-Power Optimization Strategies

#### Topics

- Microcontroller Power Consumption Profile Analysis
- ESP32 Power Modes (Active, Modem Sleep, Light Sleep, Deep Sleep, Hibernation)
- Configuring Wake-Up Sources (Timer Wake-up, EXT0/EXT1 Touch/GPIO Wake-up)
- Preserving SRAM Data in Deep Sleep (RTC Fast/Slow Memory)
- ULP Co-processor Sensor Monitoring during Deep Sleep

## Module 10 - Wireless Communication Technologies

### Lesson 10.1 Wi-Fi (IEEE 802.11) Integration

#### Topics

- 2.4 GHz Spectrum and Channels
- Station (STA) Mode vs Access Point (AP) Mode vs Dual Mode
- Wi-Fi Scan, Connection Handling, and Auto-Reconnect Logic
- WPA2/WPA3 Personal and Enterprise Security Protocols
- Non-Volatile Storage (NVS) Wi-Fi Credential Management

### Lesson 10.2 Bluetooth & Bluetooth Low Energy (BLE)

#### Topics

- Bluetooth Classic vs Bluetooth Low Energy (BLE) Architecture
- Generic Access Profile (GAP): Advertising, Scanning, Broadcaster, Peripheral, Central Roles
- Generic Attribute Profile (GATT): Services, Characteristics, Descriptors, UUIDs
- BLE Read, Write, Notify, and Indicate Operations
- Building Custom BLE Peripheral Profiles on ESP32

### Lesson 10.3 Long-Range Sub-GHz Wireless (LoRa & LoRaWAN)

#### Topics

- LoRa Modulation Technology (Chirp Spread Spectrum - CSS)
- Frequency Bands (868 MHz EU, 915 MHz US, 433 MHz)
- LoRa Peer-to-Peer (P2P) Communication
- LoRaWAN Network Architecture (End Nodes, Gateways, Network Server, Application Server)
- Activation Methods: Over-The-Air Activation (OTAA) vs Activation By Personalization (ABP)
- Device Classes (Class A, Class B, Class C)

### Lesson 10.4 Cellular IoT Technologies

#### Topics

- 2G/3G Phase-Out and Modern Cellular IoT (LTE-M / eMTC, NB-IoT)
- AT Commands Interfacing with Cellular Modems (SIM800L, SIM7600)
- Network Registration, APN Configuration, and PPP Connections

## Module 11 - IoT Networking Protocols

### Lesson 11.1 Transport Layer Standards

#### Topics

- OSI Model vs TCP/IP Stack in IoT Architectures
- TCP vs UDP Characteristics in Constrained Environments

### Lesson 11.2 MQTT (Message Queuing Telemetry Transport) Protocol

#### Topics

- MQTT Publish/Subscribe Architecture
- Broker Role (Eclipse Mosquitto, EMQX)
- Topic Structure, Namespaces, and Wildcards (`+` single-level, `#` multi-level)
- Quality of Service (QoS) Levels: QoS 0 (At most once), QoS 1 (At least once), QoS 2 (Exactly once)
- Retained Messages and Last Will and Testament (LWT)
- Keep-Alive Pings and Connection Timeout Handling
- Secure MQTT over TLS/SSL (Port 8883) with Client Certificates

### Lesson 11.3 HTTP / HTTPS in Embedded Systems

#### Topics

- Embedded HTTP Client Request Construction
- RESTful Telemetry POST/GET Requests from Embedded C++
- Parsing JSON Response Streams via ArduinoJson Library
- TLS/SSL Certificate Verification on Microcontrollers

### Lesson 11.4 WebSockets & CoAP Protocols

#### Topics

- Full-Duplex Persistent WebSockets on Embedded Devices
- Constrained Application Protocol (CoAP) Architecture over UDP
- Resource Discovery and Observe Option in CoAP

## Module 12 - Real-Time Operating Systems (RTOS) for Embedded IoT

### Lesson 12.1 RTOS Concepts & Architecture

#### Topics

- Superloop / Bare-Metal vs Real-Time Operating Systems
- Determinism and Hard vs Soft Real-Time Requirements
- Preemptive Multitasking vs Cooperative Scheduling

### Lesson 12.2 FreeRTOS Integration (ESP32 Architecture)

#### Topics

- FreeRTOS Kernel Architecture on ESP32 Dual Core
- Creating Tasks (`xTaskCreate`, `xTaskCreatePinnedToCore`)
- Task Priorities and Task States (Running, Ready, Blocked, Suspended)
- Delay Functions (`vTaskDelay`, `vTaskDelayUntil`)
- Inter-Task Communication via Queues (`xQueueCreate`, `xQueueSend`, `xQueueReceive`)
- Synchronization Primitives: Binary Semaphores, Counting Semaphores, Mutexes
- Priority Inversion Problem and Priority Inheritance Mechanism
- Event Groups and Direct-to-Task Notifications

## Module 13 - IoT Cloud Platforms & Infrastructure

### Lesson 13.1 Open & Developer IoT Platforms

#### Topics

- ThingSpeak IoT Platform (Channels, Write/Read REST APIs, MATLAB Analytics)
- Adafruit IO Platform Integration
- Blynk 2.0 Platform (Virtual Pins, Mobile App Dashboards)
- Firebase Realtime Database and Firestore REST/MQTT Integrations

### Lesson 13.2 Enterprise IoT Clouds: AWS IoT Core

#### Topics

- AWS IoT Core Architecture Overview
- Registering Devices ("Things") and X.509 Certificate Generation
- Device Shadow Concept (Desired, Reported, Delta States)
- AWS IoT Rules Engine and Routing Data to DynamoDB/S3
- AWS IoT Device SDK Integration for Python and C++

### Lesson 13.3 Private Cloud MQTT Broker Deployment

#### Topics

- Deploying Mosquitto MQTT Broker on Cloud Virtual Private Servers (AWS EC2 / DigitalOcean)
- Configuring TLS/SSL Encryption with Let's Encrypt Certificates
- User Authentication Database Setup for Mosquitto
- Firewall and Port Configuration Rules

## Module 14 - Edge AI, Machine Learning, & TinyML

### Lesson 14.1 Edge Computing Fundamentals

#### Topics

- Cloud vs Fog vs Edge Computing Architectures
- Latency, Bandwidth, Privacy, and Offline Operation Advantages

### Lesson 14.2 Embedded Computer Vision (Edge CV)

#### Topics

- ESP32-CAM Hardware Architecture (OV2640 Sensor, PSRAM)
- Frame Buffer Video Capture Pipelines
- Face Detection and Color Tracking on Embedded Chips
- Raspberry Pi OpenCV Vision Pipelines

### Lesson 14.3 TinyML & On-Device Inference

#### Topics

- Machine Learning Model Optimization (Quantization: FP32 to INT8, Pruning)
- TensorFlow Lite for Microcontrollers (TFLite Micro) Architecture
- Model Deployment to Microcontrollers (ESP32 / RP2040)
- Vibration Anomaly Detection, Gesture Recognition, and Keyword Spotting
- Edge Impulse Platform (Data Collection, Impulse Design, C++ Library Export)

## Module 15 - End-to-End IoT Full-Stack Integration

### Lesson 15.1 Hardware-to-Backend Telemetry Pipeline

#### Topics

- Microcontroller Sensor Telemetry Packet Formats (JSON / Protocol Buffers / CSV)
- PySerial Python Gateway Listener Daemon Implementation
- Ingesting Hardware Data into MySQL Database via Python API

### Lesson 15.2 Real-Time Control & Visualization Dashboard

#### Topics

- Developing Responsive Web Interface (HTML5/CSS3/JS)
- Real-Time Line Charts and Gauges Rendering (Chart.js / Canvas)
- Bidirectional Control Loop: UI Switch -> Web Endpoint -> MQTT/Serial -> MCU Relay Trigger

## Module 16 - Over-The-Air (OTA) Firmware Updates

### Lesson 16.1 OTA Architecture & Flash Partitioning

#### Topics

- Dual-Bank Flash Memory Layout (Factory App, OTA_0, OTA_1, OTA Data)
- Rollback Mechanism on Boot Failure

### Lesson 16.2 OTA Implementation Methods

#### Topics

- Web Browser Drag-and-Drop OTA Upload
- Remote HTTP/HTTPS Server Firmware Polling
- Secure MQTT-Triggered OTA Updates

### Lesson 16.3 Firmware Security in OTA

#### Topics

- RSA/ECC Cryptographic Code Signing
- Encrypted Firmware Image Delivery
- Anti-Rollback Protection

## Module 17 - IoT Security, Hardware Security, & Industrial IoT (IIoT)

### Lesson 17.1 IoT Security Threat Landscape

#### Topics

- OWASP Top 10 IoT Vulnerabilities
- Hardcoded Credentials and Insecure Default Configurations
- Unencrypted Telemetry Sniffing Attacks
- Man-in-the-Middle (MitM) Attack Vectors

### Lesson 17.2 Hardware Cryptography & Secure Elements

#### Topics

- Symmetric Encryption (AES-128 / AES-256) Hardware Accelerators
- Asymmetric Encryption (RSA, ECC)
- Cryptographic Hashing (SHA-256)
- ESP32 Secure Boot and Flash Encryption Engines
- Hardware Security Modules (HSM) / Dedicated Crypto Chips (ATECC608A)

### Lesson 17.3 Industrial IoT (IIoT) & Smart Domains

#### Topics

- Operational Technology (OT) vs Information Technology (IT) Convergence
- Modbus TCP and OPC UA Industrial Protocols
- Industry 4.0 and Smart Factory Architecture
- Precision Agriculture IoT
- Smart Healthcare Wearables and Medical IoT Security
- Smart City & Infrastructure Automation

---

# Course 9: PCB Design

## Module 1 - Electronics Fundamentals & PCB Concepts

### Lesson 1.1 Fundamentals for PCB Layout Engineers

#### Topics

- Electrical Signals Breakdown (DC, AC, Analog, Digital, Power, Ground)
- Printed Circuit Board Purpose and Evolution
- Single-Sided, Double-Sided, and Multi-Layer PCB Structures

### Lesson 1.2 PCB Materials & Physical Layers

#### Topics

- Substrate Materials (FR-4 Dielectric Constant $D_r$, Aluminum Core, Polyimide Flexible PCBs)
- Copper Foil Thickness Specifications (0.5 oz, 1 oz = 35 µm, 2 oz)
- Layer Stackup Architecture (Prepreg, Core, Copper Layers)
- Solder Mask Colors, Expansions, and Clearances
- Silkscreen Markings and Resolution Limits
- Surface Finishes (HASL, Lead-Free HASL, ENIG - Electroless Nickel Immersion Gold, OSP)

### Lesson 1.3 Electronic Component Packaging Standards

#### Topics

- Through-Hole Technology (THT) Packages (DIP, Axial, Radial)
- Surface Mount Technology (SMT) Passive Chip Sizes (1206, 0805, 0603, 0402, 0201)
- SMT Active IC Packages (SOIC, SSOP, TSSOP, QFP, QFN, BGA)
- Pitch Dimensions (Standard 2.54mm / 100mil, Fine-Pitch 0.5mm)

## Module 2 - Schematic Capture & Symbol Creation

### Lesson 2.1 Schematic Drafting Best Practices

#### Topics

- Schematic Standards (IEEE/ANSI vs IEC Symbols)
- Logical Signal Flow Conventions (Inputs on Left, Outputs on Right, Power Top, Ground Bottom)
- Multi-Sheet and Hierarchical Schematic Design Architecture
- Net Labels, Global Labels, Bus Connections, and No-Connect Flags

### Lesson 2.2 EDA Software Ecosystem & KiCad Fundamentals

#### Topics

- Overview of Professional EDA Tools (KiCad, EasyEDA, Altium Designer)
- KiCad Project Manager, Schematic Editor (Eeschema), and PCB Editor
- Project Structure and File Extensions

### Lesson 2.3 Custom Schematic Symbol Creation

#### Topics

- Symbol Editor Interface
- Defining Symbol Graphical Pins
- Pin Types Assignment (Input, Output, Bidirectional, Tri-State, Passive, Power Input, Power Output)
- Reference Designator Prefixes (R, C, L, U, Q, D, J, SW)
- Managing Local and Global Symbol Libraries

### Lesson 2.4 Electrical Rules Check (ERC)

#### Topics

- Running ERC on Schematics
- Resolving Conflict Errors (Unconnected Pins, Driver Conflicts, Missing Power Flags `#PWR`)

## Module 3 - Component Footprints & Library Management

### Lesson 3.1 Footprint Mapping & Standards

#### Topics

- Association of Schematic Symbols to PCB Footprints
- IPC-7351 Standard for SMT Land Patterns (Density Levels A, B, C)

### Lesson 3.2 Designing Custom Footprints

#### Topics

- Footprint Editor Interface
- Surface Mount Pads vs Through-Hole Pads Configuration
- Pad Dimensions, Pitch, and Hole Diameter Calculations
- Courtyard Definition Layers
- Silkscreen Reference Markings and Pin 1 Orientation Indicators
- Associating 3D Models (`.STEP` files) to Footprints

### Lesson 3.3 Library Management Standards

#### Topics

- Creating Project-Specific Footprint Libraries
- Version Control Management for CAD Assets

## Module 4 - Board Layout, Mechanical Constraints, & Component Placement

### Lesson 4.1 Mechanical Outline & Constraints

#### Topics

- Importing Mechanical Enclosure Outlines (DXF Format)
- Defining Edge.Cuts Layer in PCB Editor
- Mounting Holes Placement and Keep-Out Zones
- Connector Edge Constraints

### Lesson 4.2 Layer Stackup Planning

#### Topics

- 2-Layer Board Design Strategy
- 4-Layer Board Stackup Configurations (Signal - GND - Power - Signal vs GND - Signal - Signal - Power)
- Multi-Layer Ground Plane Isolation Benefits

### Lesson 4.3 Strategic Component Placement

#### Topics

- Functional Block Placement Strategy (Power Supply, Microcontroller, Analog Front-End, RF, Connectors)
- Decoupling Capacitor Placement Rules (Immediate Proximity to IC Power Pins)
- Thermal Management Placement (Heat Dissipation, Thermal Vias)
- Signal Path Optimization to Minimize Trace Lengths

## Module 5 - PCB Routing, Power Planes, & Grounding Architectures

### Lesson 5.1 Trace Routing Fundamentals

#### Topics

- Trace Width Calculation based on Current Carrying Capacity (IPC-2221 Standards)
- Trace Clearance / Spacing Rules
- Routing Angles ($45^\circ$ Chamfered Bends vs $90^\circ$ Sharp Corners Avoidance)
- Via Types (Through-Hole Via, Blind Via, Buried Via, Microvia, Via-in-Pad)
- Via Hole and Annular Ring Size Rules

### Lesson 5.2 Power & Ground Architecture

#### Topics

- Copper Pour / Filled Zones Creation
- Ground Plane Architecture (Solid Unbroken Ground Planes)
- Star Grounding Topology vs Ground Loops
- Analog Ground (AGND) and Digital Ground (DGND) Isolation Strategies
- Power Traces vs Dedicated Power Planes
- Ground Stitching Vias Placement

### Lesson 5.3 High-Speed & Differential Pair Routing

#### Topics

- Differential Pair Routing (USB D+/D-, RS-485 A/B, Ethernet)
- Skew and Trace Length Matching Tuning
- Controlled Impedance Trace Geometry (Single-Ended $50\,\Omega$, Differential $90\,\Omega / 120\,\Omega$)
- Microstrip vs Stripline Topology

## Module 6 - Signal Integrity, Power Integrity, & EMI/EMC Design

### Lesson 6.1 Signal Integrity (SI) Principles

#### Topics

- Crosstalk Mitigation (3W Rule for Trace Spacing)
- Impedance Mismatches and Signal Reflections
- Ringing, Overshoot, and Undershoot Control
- Series Termination Resistor Placement

### Lesson 6.2 Power Integrity (PI) Optimization

#### Topics

- Target Impedance of Power Delivery Network (PDN)
- Multi-Tier Decoupling Capacitor Array Sizing
- Voltage Drop (IR Drop) Analysis on Power Traces

### Lesson 6.3 EMI / EMC Compliance Design

#### Topics

- Electromagnetic Interference (EMI) Sources in Embedded Hardware
- Loop Area Minimization for High-Frequency Currents
- Faraday Shielding Cans Integration
- Ferrite Beads and Common Mode Choke Filters
- ESD Protection Diodes (TVS Arrays) Layout at Board Edge Connectors
- Designing PCBs for FCC / CE Certification Standards

## Module 7 - RF & Wireless Antenna PCB Design

### Lesson 7.1 RF Trace Layout Rules

#### Topics

- 2.4 GHz Wi-Fi / Bluetooth PCB Trace Guidelines
- Antenna Keep-Out Zones (No Copper on Any Layer underneath Antenna)
- Pi-Network Matching Circuit Layout ($\pi$-Filter: Series and Shunt Components)

### Lesson 7.2 Antenna Configurations

#### Topics

- Trace Antennas (Meandered Inverted-F Antenna - MIFA, PCB Monopole)
- Chip Antennas Layout
- U.FL / IPEX Coaxial Connector Layout for External Antennas
- Coplanar Waveguide with Ground (CPWG) Calculation

## Module 8 - Design Rules Check (DRC), Manufacturing Files, & DFM/DFA

### Lesson 8.1 Design Rules Check (DRC)

#### Topics

- Configuring DRC Clearance, Width, and Via Rules
- Running DRC and Resolving Layout Errors
- Unrouted Nets Check

### Lesson 8.2 Fabrication Files Generation (Gerber & Drill Files)

#### Topics

- Gerber File Format Overview (RS-274X, Gerber X2)
- Generating Individual Layer Files (Copper, Solder Mask, Silkscreen, Paste Mask, Edge.Cuts)
- Generating Excellon Drill Files (`.DRL`)
- IPC-2581 / ODB++ Output Overview

### Lesson 8.3 Assembly Files & Bill of Materials (BOM)

#### Topics

- Generating Bill of Materials (BOM) CSV File
- Structuring BOM Fields (Item, Quantity, Reference Designator, Value, Package, MPN, Supplier)
- Pick and Place / Centroid File Generation (X, Y Coordinates, Rotation, Board Side)

### Lesson 8.4 Design for Manufacturability (DFM) & Assembly (DFA)

#### Topics

- Fabricator Capabilities Matrix (Min Trace Width/Spacing, Min Hole Size, Aspect Ratio)
- Panelization Strategies (V-Scoring, Tab-Routing with Mouse Bites)
- Solder Mask Webbing between Fine-Pitch Pads
- Thermal Relief Connections on Copper Pours

## Module 9 - Manufacturing, Assembly, & Hardware Debugging

### Lesson 9.1 PCB Manufacturing Process

#### Topics

- Chemical Etching and Photolithography Process
- Multi-Layer Lamination and Drilling
- Electroplating Copper in Vias
- Solder Mask Application and Silkscreen Printing
- Surface Finish Application and Electrical Flying Probe Testing

### Lesson 9.2 PCB Assembly (PCBA) Methods

#### Topics

- Stainless Steel Stencil Creation
- Solder Paste Application via Stencil
- Manual SMT Component Placement vs Pick-and-Place Machine
- Reflow Soldering Temperature Profile (Preheat, Soak, Reflow, Cool down)
- Through-Hole Component Wave Soldering / Manual Soldering
- Inspection Methods (AOI - Automated Optical Inspection, X-Ray for BGA)

### Lesson 9.3 Hardware Bring-Up & Debugging

#### Topics

- Visual Inspection under Microscope
- Cold Continuity Check (Power Rail to Ground Short Circuit Verification)
- First Power-Up Procedure with Current-Limited Bench Power Supply
- Voltage Rail Verification via Multimeter
- Oscilloscope Probing of Clock, Reset, and Communication Lines
- Hardware Modification (Trace Cutting, Bodge Wires / Jumper Wires Installation)

---

# Course 10: Industry Projects

## Module 1 - Beginner Level Projects (Foundational Full Stack & Basic Hardware)

### Lesson 1.1 Project 1: Web-Based Environmental Data Logger & Monitor

#### Topics

- Project Domain: Smart Home & Environmental Monitoring
- Architecture: ESP32 Hardware + Flask Backend + MySQL Database + HTML5/CSS3/JS Frontend
- Microcontroller Firmware: Reading Temperature/Humidity (DHT22) via GPIO, formatting HTTP POST JSON telemetry payload over Wi-Fi
- Backend Services: Flask REST API endpoint (`/api/v1/telemetry`) receiving POST data, validating payload, executing MySQL insert statement
- Database Schema: `sensor_readings` table (id, device_id, temperature, humidity, timestamp)
- Web Frontend: Responsive dashboard rendering current readings and interactive historical trend line charts using Chart.js

### Lesson 1.2 Project 2: Smart Appliance Relay Switch with Real-Time Feedback

#### Topics

- Project Domain: Home Automation & Appliance Control
- Architecture: ESP32 + 2-Channel Relay Module + Flask REST API + Web Interface
- Microcontroller Firmware: ESP32 HTTP Client polling state endpoint / listening to commands, toggling GPIO output pins connected to Optocoupler Relay
- Backend Services: Flask application serving device status API and toggle endpoints (`/api/v1/relay/toggle`)
- Web Frontend: Modern UI with glassmorphism toggle switches, displaying real-time relay state indicators (ON/OFF) via Fetch API

### Lesson 1.3 Project 3: Digital RFID Attendance & Door Access Control System

#### Topics

- Project Domain: Security & Access Control
- Architecture: RC522 RFID Reader + ESP32 + Python Gateway Daemon + MySQL + Web Admin Panel
- Microcontroller Firmware: SPI communication with RC522 reader, reading 4-byte card UID, transmitting UID via Serial / Wi-Fi
- Backend Services: Python authentication logic verifying UID against `users` database table, logging access logs (`timestamp`, `uid`, `status`)
- Web Frontend: Admin table displaying real-time entry logs, user registration interface for assigning new RFID tags

## Module 2 - Intermediate Level Projects (Async APIs, Custom Protocols, & Hardware Controls)

### Lesson 2.1 Project 4: MQTT-Based Real-Time Industrial Tank Level & Pump Controller

#### Topics

- Project Domain: Industrial Process Monitoring & Automation
- Architecture: Ultrasonic Sensor + ESP32 + Mosquitto MQTT Broker + FastAPI Backend + MySQL + WebSockets + Web Dashboard
- Microcontroller Firmware: Dual-Core FreeRTOS tasks (Task 1: Sensor distance measurement; Task 2: MQTT client publishing to `industrial/tank/level`)
- MQTT Broker Setup: Mosquitto broker setup on cloud instance with TLS security and authentication
- Backend Services: FastAPI async service subscribing to MQTT topics, storing time-series data into MySQL, broadcasting level data over WebSockets (`/ws/tank`)
- Automated Control Logic: Backend automated threshold evaluation triggering MQTT pump command (`industrial/pump/control`) to actuate relay
- Web Frontend: Animated 2D tank liquid level indicator updated in real-time via WebSocket connection without page reloads

### Lesson 2.2 Project 5: Cellular GPS Fleet Vehicle Tracker & Telematics Portal

#### Topics

- Project Domain: Automotive Telematics & Logistics Management
- Architecture: NEO-6M GPS Module + SIM800L GSM/GPRS Modem + ESP32 + FastAPI + MySQL (Spatial Indexing) + Leaflet.js Mapping Frontend
- Microcontroller Firmware: UART NMEA sentence parsing (TinyGPS++ library), GPRS APN initialization, sending periodic HTTP POST coordinates payload over cellular network
- Backend Services: FastAPI service receiving latitude/longitude/speed data, storing geographic points into MySQL database using spatial data types
- Web Frontend: OpenStreetMap / Leaflet.js interactive map interface rendering live vehicle location marker and historical route path playback

### Lesson 2.3 Project 6: Wi-Fi Smart Power Meter & Energy Analytics Dashboard

#### Topics

- Project Domain: Energy & Smart Grid Management
- Architecture: SCT-013 Non-Invasive AC Current Sensor + ZMPT101B Voltage Module + ESP32 + Custom 2-Layer PCB + FastAPI + MySQL + Frontend Dashboard
- Hardware & PCB: Designing custom 2-layer PCB in KiCad with AC conditioning circuitry, ADC level shifting, and ESP32 module
- Microcontroller Firmware: High-frequency ADC sampling to compute RMS Voltage, RMS Current, Active Power (Watts), and Total Energy (kWh)
- Backend & Database: MySQL schema storing hourly/daily energy consumption metrics, FastAPI endpoint serving analytics data
- Web Frontend: Daily energy cost estimation widget, interactive bar charts showing power consumption trends

## Module 3 - Advanced Level Projects (Edge AI, Multi-Node Networks, Security, & Custom PCBs)

### Lesson 3.1 Project 7: Edge AI Vision-Based Smart Parking & Automatic License Plate Recognition

#### Topics

- Project Domain: Smart City & Computer Vision Infrastructure
- Architecture: ESP32-CAM / Raspberry Pi + OpenCV Python Pipeline + FastAPI Backend + MySQL Database + Servo Gate Actuator + Custom PCB
- Edge Vision System: Capturing image stream at parking entrance, executing OpenCV license plate localization, optical character recognition (OCR) parsing
- Backend Services: FastAPI endpoint verifying plate against registered database memberships, calculating occupied parking slots, updating `parking_logs`
- Actuator Integration: Triggering barrier gate servo motor via micro-controller signal upon authorization
- Web Frontend: Live video feed display, real-time available slot counter, billing logs management system

### Lesson 3.2 Project 8: Precision Agriculture Multi-Node Mesh Network with LoRaWAN & Solar Power

#### Topics

- Project Domain: Smart Agriculture & Environmental Conservation
- Architecture: Multi-Node LoRa End Devices + SX1302 LoRaWAN Gateway + The Things Network (TTN) / Private ChirpStack Server + FastAPI + MySQL + Custom Solar PCB
- Hardware & PCB: Solar-powered LoRa node PCB featuring MPPT LiFePO4 battery charging circuit, deep sleep hardware integration, soil moisture/temperature/NPK sensor interfaces
- Firmware Architecture: Deep sleep duty-cycling (sleeping 15 mins, waking up for 3 seconds to sample sensors and transmit LoRaWAN packet), OTAA network join
- Cloud Ingestion: MQTT integration with LoRaWAN Network Server, FastAPI data ingestion pipeline, MySQL time-series storage
- Automated Irrigation: Automated trigger signaling field valve nodes over LoRaWAN when soil moisture drops below threshold
- Web Frontend: Map layout of field nodes, soil health analytics, automated vs manual irrigation override switches

### Lesson 3.3 Project 9: Wearable Patient Health Monitor & Emergency Alert System

#### Topics

- Project Domain: Healthcare & Biomedical IoT
- Architecture: MAX30102 Heart Rate/SpO2 Sensor + MPU6050 Accelerometer + ESP32 Pico W + BLE / Wi-Fi + FastAPI + MySQL + Twilio SMS Alert API + Compact PCB
- Hardware Design: Designing wearable ultra-compact 4-Layer PCB layout with onboard antenna keep-out zone
- Microcontroller Firmware: FreeRTOS tasks processing PPG pulse waveforms for Heart Rate & $SpO_2$, acceleration threshold monitoring for fall detection algorithms
- Alert Processing: Immediate emergency trigger sending HTTPS request to FastAPI backend on fall detection or abnormal vitals, initiating Twilio SMS/Call alerts to emergency contacts
- Web Frontend: Hospital telemetry dashboard displaying live vital signs charts, patient health status indicators, historical health records

## Module 4 - Industry 4.0 / 5.0 Enterprise Final Year Projects

### Lesson 4.1 Project 10: Industrial Predictive Maintenance & Vibration Monitoring System (TinyML)

#### Topics

- Project Domain: Industrial IoT & Industry 4.0
- Architecture: ADXL345 3-Axis High-Frequency Accelerometer + ESP32 (TinyML TFLite Micro) + Modbus RTU / MQTT over TLS + FastAPI + MySQL + Enterprise Dashboard
- Edge AI Implementation: High-frequency accelerometer sampling ($1\,\text{kHz}$), Fast Fourier Transform (FFT) spectral extraction, deploying TensorFlow Lite for Microcontrollers model for real-time bearing anomaly classification
- Microcontroller Firmware: Executing TinyML inference on-device to classify machine health state (Normal, Unbalanced, Misalignment, Bearing Fault)
- Security & Industrial Connectivity: MQTT over TLS 1.3 with X.509 mutual certificate authentication to cloud broker
- Backend & Storage: FastAPI enterprise backend service, storing high-resolution fault events into MySQL database
- Web Dashboard: FFT spectrum visualization chart, predictive health percentage indicators, automated maintenance work order generator

### Lesson 4.2 Project 11: Autonomous Environmental Survey Drone Telemetry Gateway

#### Topics

- Project Domain: Drone Robotics & Environmental Telemetry
- Architecture: Pixhawk / RP2040 Flight Controller Interface + Environmental Gas Sensors (SGP30, SDS011 Dust) + ESP32 Telemetry Transceiver + FastAPI + MySQL + 3D Map Visualizer
- Hardware Integration: UART communication bridge between Pixhawk flight controller (MAVLink protocol) and ESP32 telemetry transmitter
- Firmware Engine: Aggregating flight telemetry (GPS coordinates, altitude, pitch, roll, yaw) with environmental gas concentration values
- Backend Services: High-throughput async FastAPI data ingestion pipe, streaming telemetry to clients via WebSockets
- Web Frontend: 3D map representation (Cesium.js / Three.js) plotting drone flight trajectory in 3D space with color-coded air pollution heatmaps

### Lesson 4.3 Project 12: Smart Building Energy Optimization & Microgrid HVAC Controller

#### Topics

- Project Domain: Building Automation & Smart Grid Energy Systems
- Architecture: Custom 4-Layer Industrial Controller PCB + Modbus RS-485 Sensor Network + Light/Occupancy Nodes + FastAPI Backend + MySQL Database + Web App
- Industrial Hardware PCB Design: 4-Layer KiCad PCB layout featuring isolated RS-485 transceivers, buck power regulation, industrial terminal blocks, relays
- Sensor Network Protocol: Modbus RTU communication over RS-485 daisy-chain network reading ambient temperature, light levels, and PIR occupancy across building zones
- Optimization Algorithm: Backend Python controller algorithm evaluating energy tariff schedules, zone occupancy, and ambient conditions to dynamically regulate HVAC and lighting
- Database Schema: MySQL schema for zone configuration, minute-by-minute energy metrics, system audit logs, user permissions
- Web Interface: Building floorplan visualization with interactive zone overlays, energy usage reports, manual override controls

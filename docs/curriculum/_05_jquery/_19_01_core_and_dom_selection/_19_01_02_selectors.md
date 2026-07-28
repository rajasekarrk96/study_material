---
id: "19_01_02"
title: "jQuery Selectors"
course: "jQuery"
module: 1
module_title: "Core and DOM Selection"
lesson: 2
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["selectors", "id-selector", "class-selector", "element-selector", "attribute-selector"]
prerequisites: []
lab_required: true
---

# jQuery Selectors


## Selecting DOM Elements

```javascript
// Basic Selectors
$('#header')          // By ID
$('.btn-primary')     // By Class
$('p')                // By Tag Name

// Compound Selectors
$('h1, h2, h3')       // Multiple tags
$('div.content p')    // Descendant
$('ul > li')          // Direct Child

// Attribute Selectors
$('input[type="text"]')
$('a[href^="https"]')  // Starts with
```

## Lab Exercise
1. Target all external links on a page and add a `target="_blank"` attribute using jQuery selectors.

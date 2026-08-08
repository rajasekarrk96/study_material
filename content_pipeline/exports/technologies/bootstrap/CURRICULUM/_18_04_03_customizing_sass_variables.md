---
id: "18_04_03"
title: "Customizing Sass Variables"
course: "Bootstrap"
module: 4
module_title: "Advanced Layout and Customization"
lesson: 3
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["sass", "scss", "custom-theme", "variables", "bootstrap-customization"]
prerequisites: []
lab_required: true
---

# Customizing Sass Variables


## Customizing Bootstrap with SCSS

```scss
// Custom variables overrides MUST come before importing Bootstrap
$primary: #6f42c1;
$body-bg: #f8f9fa;
$font-family-base: 'Inter', sans-serif;

@import "bootstrap/scss/bootstrap";
```

## Lab Exercise
1. Set up a custom SCSS compilation pipeline overriding default Bootstrap primary colors and border radius.

---
id: "18_01_01"
title: "Bootstrap Grid System"
course: "Bootstrap"
module: 1
module_title: "Grid System and Layout"
lesson: 1
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["bootstrap", "grid", "flexbox", "container", "row", "col", "breakpoints", "responsive"]
prerequisites: []
lab_required: true
---

# Bootstrap Grid System


## The Bootstrap 12-Column Grid

Bootstrap's grid system uses containers, rows, and columns to layout and align content. Built with flexbox, it is fully responsive across 6 default breakpoints.

### Breakpoints

| Breakpoint | Class Prefix | Dimensions |
|---|---|---|
| Extra small | `.col-` | <576px |
| Small | `.col-sm-` | ≥576px |
| Medium | `.col-md-` | ≥768px |
| Large | `.col-lg-` | ≥992px |
| Extra large | `.col-xl-` | ≥1200px |
| Extra extra large | `.col-xxl-` | ≥1400px |

## Grid HTML Structure

```html
<div class="container">
  <div class="row">
    <div class="col-md-8">Main Content (8 cols)</div>
    <div class="col-md-4">Sidebar (4 cols)</div>
  </div>
</div>
```

## Equal Width vs Specific Widths

```html
<!-- Equal Width Columns -->
<div class="row">
  <div class="col">1 of 3</div>
  <div class="col">2 of 3</div>
  <div class="col">3 of 3</div>
</div>

<!-- Responsive Column Stacking -->
<div class="row">
  <div class="col-12 col-md-6 col-lg-4">Card 1</div>
  <div class="col-12 col-md-6 col-lg-4">Card 2</div>
  <div class="col-12 col-md-6 col-lg-4">Card 3</div>
</div>
```

## Lab Exercise
1. Create a responsive 3-column layout that stacks into a single column on mobile screens (<576px).
2. Build a header with a 2-column logo area and 10-column navigation bar using Bootstrap grid.

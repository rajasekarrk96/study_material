---
id: "18_02_02"
title: "Color Palette and Themes"
course: "Bootstrap"
module: 2
module_title: "Typography and Utilities"
lesson: 2
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["colors", "text-primary", "bg-dark", "theme-colors", "dark-mode", "bg-gradient"]
prerequisites: []
lab_required: true
---

# Color Palette and Themes


## Theme Colors

Bootstrap comes with a default set of semantic theme colors:

| Color Role | Background Class | Text Class |
|---|---|---|
| Primary | `.bg-primary` | `.text-primary` |
| Secondary | `.bg-secondary` | `.text-secondary` |
| Success | `.bg-success` | `.text-success` |
| Danger | `.bg-danger` | `.text-danger` |
| Warning | `.bg-warning` | `.text-warning` |
| Info | `.bg-info` | `.text-info` |
| Light | `.bg-light` | `.text-light` |
| Dark | `.bg-dark` | `.text-dark` |

```html
<div class="p-3 mb-2 bg-primary text-white">.bg-primary</div>
<div class="p-3 mb-2 bg-success text-white">.bg-success</div>
```

## Lab Exercise
1. Create a notification alert list demonstrating all 6 semantic theme colors with contrasting text.

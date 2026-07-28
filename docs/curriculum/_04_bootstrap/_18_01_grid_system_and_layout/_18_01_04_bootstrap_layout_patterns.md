---
id: "18_01_04"
title: "Bootstrap Layout Patterns"
course: "Bootstrap"
module: 1
module_title: "Grid System and Layout"
lesson: 4
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["patterns", "holy-grail", "dashboard", "sidebar", "sticky-footer"]
prerequisites: []
lab_required: true
---

# Bootstrap Layout Patterns


## Common Bootstrap Layout Patterns

### Holy Grail / Dashboard Layout

```html
<div class="container-fluid">
  <div class="row min-vh-100">
    <nav class="col-md-3 col-lg-2 d-md-block bg-dark sidebar collapse p-3 text-white">
      <h5>Dashboard</h5>
    </nav>
    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 py-4">
      <h1>Main Content Area</h1>
    </main>
  </div>
</div>
```

## Lab Exercise
1. Assemble a complete admin dashboard shell with a fixed top navbar, a responsive left sidebar, and a main content grid.

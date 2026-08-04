---
id: "18_03_04"
title: "Forms and Input Groups"
course: "Bootstrap"
module: 3
module_title: "Core Components"
lesson: 4
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["form-control", "form-label", "form-select", "input-group", "form-check"]
prerequisites: []
lab_required: true
---

# Forms and Input Groups


## Form Controls and Input Groups

```html
<form>
  <div class="mb-3">
    <label for="emailInput" class="form-label">Email address</label>
    <input type="email" class="form-control" id="emailInput" placeholder="name@example.com">
  </div>
  <div class="input-group mb-3">
    <span class="input-group-text">@</span>
    <input type="text" class="form-control" placeholder="Username">
  </div>
</form>
```

## Lab Exercise
1. Construct a complete checkout form with name, email, payment selector, and terms checkbox.

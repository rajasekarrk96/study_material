---
id: "18_03_02"
title: "Cards and Accordions"
course: "Bootstrap"
module: 3
module_title: "Core Components"
lesson: 2
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["card", "card-body", "card-img-top", "accordion", "accordion-item", "collapse"]
prerequisites: []
lab_required: true
---

# Cards and Accordions


## Cards and Accordions

```html
<!-- Card Component -->
<div class="card" style="width: 18rem;">
  <img src="https://via.placeholder.com/150" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>

<!-- Accordion Component -->
<div class="accordion" id="faqAccordion">
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne">
        Question #1
      </button>
    </h2>
    <div id="collapseOne" class="accordion-collapse collapse show">
      <div class="accordion-body">Answer text goes here...</div>
    </div>
  </div>
</div>
```

## Lab Exercise
1. Build an interactive FAQ section using the Bootstrap Accordion component.

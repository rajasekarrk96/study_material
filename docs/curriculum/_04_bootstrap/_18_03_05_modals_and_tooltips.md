---
id: "18_03_05"
title: "Modals and Tooltips"
course: "Bootstrap"
module: 3
module_title: "Core Components"
lesson: 5
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["modal", "modal-dialog", "tooltip", "popover", "javascript-plugins"]
prerequisites: []
lab_required: true
---

# Modals and Tooltips


## Modals and Tooltips

```html
<!-- Modal Trigger -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
  Launch demo modal
</button>

<!-- Modal Structure -->
<div class="modal fade" id="exampleModal" tabindex="-1">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Modal Title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body">Modal body text...</div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
```

## Lab Exercise
1. Trigger a modal confirm dialog on deleting an item from a list.

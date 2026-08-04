---
id: "23_06_02"
title: "Bookmarks and Selection Pane"
course: "Power BI"
module: 6
module_title: "Interactivity and Analytics"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["bookmarks", "selection-pane", "buttons", "navigation"]
prerequisites: []
lab_required: true
---

# Bookmarks and Selection Pane

## Overview of Bookmarks and Selection Pane

In this lesson, you will master **Bookmarks and Selection Pane** as part of Module 6: Interactivity and Analytics in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Bookmarks and Selection Pane is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Bookmarks and Selection Pane
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

## Lab Exercise
1. Implement Bookmarks and Selection Pane in a sample Financials dataset and verify measure results against raw tables.

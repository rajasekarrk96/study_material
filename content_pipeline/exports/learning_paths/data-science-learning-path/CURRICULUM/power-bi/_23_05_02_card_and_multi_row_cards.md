---
id: "23_05_02"
title: "Cards and Multi-Row Cards"
course: "Power BI"
module: 5
module_title: "Visualizations and Reports"
lesson: 2
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["kpi-card", "multi-row-card", "new-card-visual"]
prerequisites: []
lab_required: true
---

# Cards and Multi-Row Cards

## Overview of Cards and Multi-Row Cards

In this lesson, you will master **Cards and Multi-Row Cards** as part of Module 5: Visualizations and Reports in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Cards and Multi-Row Cards is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Cards and Multi-Row Cards
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

## Lab Exercise
1. Implement Cards and Multi-Row Cards in a sample Financials dataset and verify measure results against raw tables.

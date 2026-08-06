---
id: "23_05_04"
title: "Maps and Geospatial Visuals"
course: "Power BI"
module: 5
module_title: "Visualizations and Reports"
lesson: 4
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["map", "filled-map", "shape-map", "azure-maps"]
prerequisites: []
lab_required: true
---

# Maps and Geospatial Visuals

## Overview of Maps and Geospatial Visuals

In this lesson, you will master **Maps and Geospatial Visuals** as part of Module 5: Visualizations and Reports in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Maps and Geospatial Visuals is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Maps and Geospatial Visuals
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

## Lab Exercise
1. Implement Maps and Geospatial Visuals in a sample Financials dataset and verify measure results against raw tables.

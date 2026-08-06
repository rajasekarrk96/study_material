---
id: "23_02_03"
title: "Column Transformations"
course: "Power BI"
module: 2
module_title: "Power Query ETL"
lesson: 3
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["split-column", "merge-columns", "conditional-column", "extract"]
prerequisites: []
lab_required: true
---

# Column Transformations

## Overview of Column Transformations

In this lesson, you will master **Column Transformations** as part of Module 2: Power Query ETL in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Column Transformations is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Column Transformations
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

## Lab Exercise
1. Implement Column Transformations in a sample Financials dataset and verify measure results against raw tables.

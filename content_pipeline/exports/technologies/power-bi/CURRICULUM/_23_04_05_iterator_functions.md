---
id: "23_04_05"
title: "Iterator Functions (SUMX, AVERAGEX)"
course: "Power BI"
module: 4
module_title: "DAX Calculations"
lesson: 5
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["sumx", "averagex", "countx", "row-context-iteration"]
prerequisites: []
lab_required: true
---

# Iterator Functions (SUMX, AVERAGEX)

## Overview of Iterator Functions (SUMX, AVERAGEX)

In this lesson, you will master **Iterator Functions (SUMX, AVERAGEX)** as part of Module 4: DAX Calculations in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Iterator Functions (SUMX, AVERAGEX) is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Iterator Functions (SUMX, AVERAGEX)
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

## Lab Exercise
1. Implement Iterator Functions (SUMX, AVERAGEX) in a sample Financials dataset and verify measure results against raw tables.

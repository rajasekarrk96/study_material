---
id: "23_02_02"
title: "Data Cleaning and Formatting"
course: "Power BI"
module: 2
module_title: "Power Query ETL"
lesson: 2
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["clean", "trim", "replace-values", "change-type", "nulls"]
prerequisites: []
lab_required: true
---

# Data Cleaning and Formatting

## Overview of Data Cleaning and Formatting

In this lesson, you will master **Data Cleaning and Formatting** as part of Module 2: Power Query ETL in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Data Cleaning and Formatting is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Data Cleaning and Formatting
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

## Lab Exercise
1. Implement Data Cleaning and Formatting in a sample Financials dataset and verify measure results against raw tables.

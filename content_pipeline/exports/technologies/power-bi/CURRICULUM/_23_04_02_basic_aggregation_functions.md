---
id: "23_04_02"
title: "Basic Aggregation Functions"
course: "Power BI"
module: 4
module_title: "DAX Calculations"
lesson: 2
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["sum", "average", "count", "distinctcount", "min", "max"]
prerequisites: []
lab_required: true
---

# Basic Aggregation Functions

## Overview of Basic Aggregation Functions

In this lesson, you will master **Basic Aggregation Functions** as part of Module 4: DAX Calculations in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Basic Aggregation Functions is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Basic Aggregation Functions
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

## Lab Exercise
1. Implement Basic Aggregation Functions in a sample Financials dataset and verify measure results against raw tables.

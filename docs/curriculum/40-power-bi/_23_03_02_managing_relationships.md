---
id: "23_03_02"
title: "Managing Relationships"
course: "Power BI"
module: 3
module_title: "Data Modeling"
lesson: 2
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["cardinality", "one-to-many", "many-to-many", "cross-filter-direction"]
prerequisites: []
lab_required: true
---

# Managing Relationships

## Overview of Managing Relationships

In this lesson, you will master **Managing Relationships** as part of Module 3: Data Modeling in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Managing Relationships is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Managing Relationships
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

## Lab Exercise
1. Implement Managing Relationships in a sample Financials dataset and verify measure results against raw tables.

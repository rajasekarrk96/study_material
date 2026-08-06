---
id: "23_02_04"
title: "Merging and Appending Queries"
course: "Power BI"
module: 2
module_title: "Power Query ETL"
lesson: 4
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["merge-queries", "append-queries", "joins", "left-outer"]
prerequisites: []
lab_required: true
---

# Merging and Appending Queries

## Overview of Merging and Appending Queries

In this lesson, you will master **Merging and Appending Queries** as part of Module 2: Power Query ETL in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Merging and Appending Queries is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Merging and Appending Queries
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

## Lab Exercise
1. Implement Merging and Appending Queries in a sample Financials dataset and verify measure results against raw tables.

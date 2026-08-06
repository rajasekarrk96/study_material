---
id: "23_03_01"
title: "Star Schema and Snowflake Schema"
course: "Power BI"
module: 3
module_title: "Data Modeling"
lesson: 1
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["data-modeling", "star-schema", "fact-table", "dimension-table", "snowflake"]
prerequisites: []
lab_required: true
---

# Star Schema and Snowflake Schema

## Overview of Star Schema and Snowflake Schema

In this lesson, you will master **Star Schema and Snowflake Schema** as part of Module 3: Data Modeling in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Star Schema and Snowflake Schema is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Star Schema and Snowflake Schema
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

## Lab Exercise
1. Implement Star Schema and Snowflake Schema in a sample Financials dataset and verify measure results against raw tables.

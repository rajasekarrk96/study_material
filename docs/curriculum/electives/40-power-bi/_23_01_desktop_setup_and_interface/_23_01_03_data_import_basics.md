---
id: "23_01_03"
title: "Data Import Basics"
course: "Power BI"
module: 1
module_title: "Desktop Setup and Interface"
lesson: 3
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["import", "excel", "csv", "sql", "connectors"]
prerequisites: []
lab_required: true
---

# Data Import Basics

## Overview of Data Import Basics

In this lesson, you will master **Data Import Basics** as part of Module 1: Desktop Setup and Interface in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Data Import Basics is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Data Import Basics
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

## Lab Exercise
1. Implement Data Import Basics in a sample Financials dataset and verify measure results against raw tables.

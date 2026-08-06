---
id: "23_01_04"
title: "File Types and Saving"
course: "Power BI"
module: 1
module_title: "Desktop Setup and Interface"
lesson: 4
version: "2.0"
difficulty: "beginner"
duration_minutes: 60
tags: ["pbix", "pbit", "pbip", "dataset"]
prerequisites: []
lab_required: true
---

# File Types and Saving

## Overview of File Types and Saving

In this lesson, you will master **File Types and Saving** as part of Module 1: Desktop Setup and Interface in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why File Types and Saving is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for File Types and Saving
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

## Lab Exercise
1. Implement File Types and Saving in a sample Financials dataset and verify measure results against raw tables.

---
id: "23_07_05"
title: "Workspace Roles and Sharing"
course: "Power BI"
module: 7
module_title: "Power BI Service and Administration"
lesson: 5
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["admin", "member", "contributor", "viewer", "workspace"]
prerequisites: []
lab_required: true
---

# Workspace Roles and Sharing

## Overview of Workspace Roles and Sharing

In this lesson, you will master **Workspace Roles and Sharing** as part of Module 7: Power BI Service and Administration in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Workspace Roles and Sharing is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Workspace Roles and Sharing
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

## Lab Exercise
1. Implement Workspace Roles and Sharing in a sample Financials dataset and verify measure results against raw tables.

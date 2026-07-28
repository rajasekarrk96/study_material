---
id: "23_07_03"
title: "Scheduled Refresh and Gateways"
course: "Power BI"
module: 7
module_title: "Power BI Service and Administration"
lesson: 3
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["data-gateway", "scheduled-refresh", "on-premises"]
prerequisites: []
lab_required: true
---

# Scheduled Refresh and Gateways

## Overview of Scheduled Refresh and Gateways

In this lesson, you will master **Scheduled Refresh and Gateways** as part of Module 7: Power BI Service and Administration in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Scheduled Refresh and Gateways is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Scheduled Refresh and Gateways
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

## Lab Exercise
1. Implement Scheduled Refresh and Gateways in a sample Financials dataset and verify measure results against raw tables.

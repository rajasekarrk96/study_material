# Dashboards vs Reports

> **Course**: Power Bi | **Module**: Power BI Service and Administration | **Difficulty**: beginner

---

In this lesson, you will master **Dashboards vs Reports** as part of Module 7: Power BI Service and Administration in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Dashboards vs Reports is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Dashboards vs Reports
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

---

1. Implement Dashboards vs Reports in a sample Financials dataset and verify measure results against raw tables.

---

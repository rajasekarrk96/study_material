# Merging and Appending Queries

> **Course**: Power Bi | **Module**: Power Query ETL | **Difficulty**: intermediate

---

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

---

1. Implement Merging and Appending Queries in a sample Financials dataset and verify measure results against raw tables.

---

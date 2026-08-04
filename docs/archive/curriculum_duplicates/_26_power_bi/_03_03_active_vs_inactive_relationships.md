# Active vs Inactive Relationships

> **Course**: Power Bi | **Module**: Data Modeling | **Difficulty**: intermediate

---

In this lesson, you will master **Active vs Inactive Relationships** as part of Module 3: Data Modeling in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Active vs Inactive Relationships is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Active vs Inactive Relationships
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

---

1. Implement Active vs Inactive Relationships in a sample Financials dataset and verify measure results against raw tables.

---

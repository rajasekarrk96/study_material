# Iterator Functions (SUMX, AVERAGEX)

> **Course**: Power Bi | **Module**: DAX Calculations | **Difficulty**: advanced

---

In this lesson, you will master **Iterator Functions (SUMX, AVERAGEX)** as part of Module 4: DAX Calculations in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Iterator Functions (SUMX, AVERAGEX) is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Iterator Functions (SUMX, AVERAGEX)
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

---

1. Implement Iterator Functions (SUMX, AVERAGEX) in a sample Financials dataset and verify measure results against raw tables.

---

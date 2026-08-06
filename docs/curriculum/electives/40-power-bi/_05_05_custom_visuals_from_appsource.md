# Custom Visuals from AppSource

> **Course**: Power Bi | **Module**: Visualizations and Reports | **Difficulty**: intermediate

---

In this lesson, you will master **Custom Visuals from AppSource** as part of Module 5: Visualizations and Reports in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Custom Visuals from AppSource is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Custom Visuals from AppSource
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

---

1. Implement Custom Visuals from AppSource in a sample Financials dataset and verify measure results against raw tables.

---

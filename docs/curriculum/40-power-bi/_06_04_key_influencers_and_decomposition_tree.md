# Key Influencers and Decomposition Tree

> **Course**: Power Bi | **Module**: Interactivity and Analytics | **Difficulty**: advanced

---

In this lesson, you will master **Key Influencers and Decomposition Tree** as part of Module 6: Interactivity and Analytics in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Key Influencers and Decomposition Tree is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Key Influencers and Decomposition Tree
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

---

1. Implement Key Influencers and Decomposition Tree in a sample Financials dataset and verify measure results against raw tables.

---

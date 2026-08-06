# Unpivoting and Pivoting Columns

> **Course**: Power Bi | **Module**: Power Query ETL | **Difficulty**: intermediate

---

In this lesson, you will master **Unpivoting and Pivoting Columns** as part of Module 2: Power Query ETL in Power BI.

### Key Concepts & Workflow

1. **Architecture & Purpose**: Understand why Unpivoting and Pivoting Columns is critical for enterprise Business Intelligence.
2. **Step-by-Step Implementation**:
   - Open Power BI Desktop and load the target dataset.
   - Navigate to the appropriate view (Report, Data, or Model).
   - Apply transformations and DAX measures as required.
3. **Best Practices**:
   - Maintain star schema data modeling principles.
   - Keep DAX measures modular and well-commented.
   - Optimize visual performance using Performance Analyzer.

```dax
// Example DAX Measure for Unpivoting and Pivoting Columns
Total Sales = SUM(Sales[SalesAmount])
YTD Sales = TOTALYTD([Total Sales], 'Calendar'[Date])
```

---

1. Implement Unpivoting and Pivoting Columns in a sample Financials dataset and verify measure results against raw tables.

---

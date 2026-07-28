---
id: "23_02_05"
title: "Unpivoting and Pivoting Columns"
course: "Power BI"
module: 2
module_title: "Power Query ETL"
lesson: 5
version: "2.0"
difficulty: "intermediate"
duration_minutes: 60
tags: ["unpivot", "pivot", "normalize-data"]
prerequisites: []
lab_required: true
---

# Unpivoting and Pivoting Columns

## Overview of Unpivoting and Pivoting Columns

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

## Lab Exercise
1. Implement Unpivoting and Pivoting Columns in a sample Financials dataset and verify measure results against raw tables.

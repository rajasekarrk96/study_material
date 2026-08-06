# Power BI — Master Syllabus

**Target Role:** Data Analyst / Business Intelligence Developer  
**Difficulty Level:** Beginner → Intermediate  
**Estimated Duration:** 35 Hours  
**Prerequisites:** Basic data literacy, Excel familiarity  

---

## Study Flow

---

### Module 1 — Power BI Ecosystem and Setup

#### 1.1. Getting Started

1. **Power BI Ecosystem and Setup**
    - **Course Coverage:** 🟢 Covered in Class
    1. Power BI Desktop vs Service vs Mobile
    2. Installation and licensing
    3. Data flow — source → model → report → service
    4. Lab Exercise

2. **Interface and Views**
    - **Course Coverage:** 🟢 Covered in Class
    1. Report View, Data View, Model View
    2. Ribbons and panes — Fields, Visualizations, Filters
    3. Navigation and keyboard shortcuts
    4. Lab Exercise

3. **Data Import Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Connecting to Excel, CSV, SQL Server, web
    2. Direct Query vs Import mode
    3. Incremental refresh overview
    4. Lab Exercise

4. **File Types and Saving**
    - **Course Coverage:** 🟢 Covered in Class
    1. .pbix vs .pbit (templates)
    2. Publishing and version control
    3. Lab Exercise

---

### Module 2 — Power Query — Data Transformation

#### 2.1. ETL in Power BI

1. **Power Query Editor Overview**
    - **Course Coverage:** 🟢 Covered in Class
    1. Applied steps panel and M formula language
    2. Query dependencies
    3. Lab Exercise

2. **Data Cleaning and Formatting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Removing duplicates, nulls, errors
    2. Changing data types
    3. Replacing values and trimming text
    4. Lab Exercise

3. **Column Transformations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Split column, merge columns
    2. Conditional columns
    3. Custom columns with M expressions
    4. Lab Exercise

4. **Merging and Appending Queries**
    - **Course Coverage:** 🟢 Covered in Class
    1. Merge types — inner, left outer, right outer, full outer
    2. Append queries for union
    3. Fuzzy matching
    4. Lab Exercise

5. **Unpivoting and Pivoting Columns**
    - **Course Coverage:** 🟢 Covered in Class
    1. Unpivoting for tidy data
    2. Pivoting for cross-tab format
    3. Lab Exercise

6. **M Code Basics**
    - **Course Coverage:** 🟢 Covered in Class
    1. M language syntax — let…in structure
    2. Writing custom M functions
    3. Parameterized queries
    4. Lab Exercise

---

### Module 3 — Data Modelling

#### 3.1. Relationships and Schema Design

1. **Star Schema and Snowflake Schema**
    - **Course Coverage:** 🟢 Covered in Class
    1. Fact tables and dimension tables
    2. Star vs snowflake — trade-offs
    3. Date dimension table
    4. Lab Exercise

2. **Managing Relationships**
    - **Course Coverage:** 🟢 Covered in Class
    1. Cardinality — one-to-many, many-to-many
    2. Cross-filter direction
    3. Relationship detection and auto-detection
    4. Lab Exercise

3. **Active vs Inactive Relationships**
    - **Course Coverage:** 🟢 Covered in Class
    1. When inactive relationships are useful
    2. USERELATIONSHIP in DAX
    3. Lab Exercise

4. **Role-Playing Dimensions**
    - **Course Coverage:** 🟢 Covered in Class
    1. Reusing date dimension for multiple roles
    2. Order date vs ship date pattern
    3. Lab Exercise

---

### Module 4 — DAX (Data Analysis Expressions)

#### 4.1. DAX Fundamentals

1. **Calculated Columns vs Measures**
    - **Course Coverage:** 🟢 Covered in Class
    1. Row context vs filter context
    2. When to use columns vs measures
    3. Naming conventions
    4. Lab Exercise

2. **Basic Aggregation Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. SUM, AVERAGE, COUNT, COUNTROWS, DISTINCTCOUNT
    2. MIN, MAX, MEDIAN
    3. Lab Exercise

3. **CALCULATE Function Deep Dive**
    - **Course Coverage:** 🟢 Covered in Class
    1. Modifying filter context
    2. ALL, ALLEXCEPT, REMOVEFILTERS
    3. FILTER and complex conditions
    4. Lab Exercise

4. **Time Intelligence Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. TOTALYTD, TOTALQTD, TOTALMTD
    2. DATEADD, SAMEPERIODLASTYEAR
    3. Rolling averages
    4. Lab Exercise

5. **Iterator Functions — SUMX, AVERAGEX**
    - **Course Coverage:** 🟢 Covered in Class
    1. Row-by-row iteration
    2. SUMX vs SUM — when to use each
    3. RANKX
    4. Lab Exercise

6. **DAX Variables and Optimization**
    - **Course Coverage:** 🟢 Covered in Class
    1. VAR…RETURN syntax
    2. Query folding and performance
    3. DAX Studio overview
    4. Lab Exercise

---

### Module 5 — Visualizations

#### 5.1. Core Visuals

1. **Bar, Column, and Line Charts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Clustered, stacked, 100% stacked
    2. Combo charts (bar + line)
    3. Conditional formatting
    4. Lab Exercise

2. **Cards and Multi-Row Cards**
    - **Course Coverage:** 🟢 Covered in Class
    1. KPI cards
    2. Dynamic title with DAX
    3. Lab Exercise

3. **Matrix and Table Visuals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Totals and subtotals
    2. Stepped layout and expand/collapse
    3. Conditional formatting in matrix
    4. Lab Exercise

4. **Maps and Geospatial Visuals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Bing maps — bubble and filled
    2. ArcGIS and shape maps
    3. Geocoding hierarchy
    4. Lab Exercise

5. **Custom Visuals from AppSource**
    - **Course Coverage:** 🟡 Optional Discussion
    1. Installing marketplace visuals
    2. Bullet chart, Gantt, Word Cloud
    3. Certified vs uncertified visuals
    4. Lab Exercise

---

### Module 6 — Interactivity and Advanced Features

#### 6.1. Interactive Reports

1. **Slicers and Filters**
    - **Course Coverage:** 🟢 Covered in Class
    1. Slicer types — list, dropdown, between
    2. Syncing slicers across pages
    3. Filter pane — visual, page, report filters
    4. Lab Exercise

2. **Bookmarks and Selection Pane**
    - **Course Coverage:** 🟢 Covered in Class
    1. Creating bookmark-driven navigation
    2. Toggle buttons with bookmarks
    3. Visibility control
    4. Lab Exercise

3. **Drillthrough and Report Page Tooltips**
    - **Course Coverage:** 🟢 Covered in Class
    1. Page-level drillthrough setup
    2. Cross-report drillthrough
    3. Custom tooltip pages
    4. Lab Exercise

4. **Key Influencers and Decomposition Tree**
    - **Course Coverage:** 🟡 Optional Discussion
    1. AI visuals — Key Influencers
    2. Decomposition Tree for root cause analysis
    3. Q&A visual
    4. Lab Exercise

---

### Module 7 — Power BI Service and Sharing

#### 7.1. Publishing and Governance

1. **Publishing to Power BI Service**
    - **Course Coverage:** 🟢 Covered in Class
    1. Workspaces and apps
    2. Publishing workflow
    3. Dataset vs report vs dashboard
    4. Lab Exercise

2. **Dashboards vs Reports**
    - **Course Coverage:** 🟢 Covered in Class
    1. Pinning visuals to dashboards
    2. Dashboard alerts and subscriptions
    3. Lab Exercise

3. **Scheduled Refresh and Gateways**
    - **Course Coverage:** 🟢 Covered in Class
    1. On-premises data gateway
    2. Configuring refresh schedule
    3. Refresh failures and monitoring
    4. Lab Exercise

4. **Row-Level Security (RLS)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Static RLS — DAX filter rules
    2. Dynamic RLS — USERPRINCIPALNAME()
    3. Testing RLS
    4. Lab Exercise

5. **Workspace Roles and Sharing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Admin, Member, Contributor, Viewer roles
    2. Sharing reports and apps
    3. Sensitivity labels
    4. Lab Exercise

6. **Capstone — Sales Executive Dashboard**
    - **Course Coverage:** 🟢 Covered in Class
    1. End-to-end project — data import through publishing
    2. Multi-page report with cross-filtering
    3. RLS for regional managers
    4. Scheduled refresh setup
    5. Lab Exercise

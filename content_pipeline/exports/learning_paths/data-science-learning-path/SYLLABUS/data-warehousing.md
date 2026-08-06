# Data Warehousing — Master Syllabus

**Target Role:** Data Engineer / Analytics Engineer  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 30 Hours  
**Prerequisites:** SQL, Database Technologies  

---

## Study Flow

---

### Module 1 — Data Warehouse Concepts

#### 1.1. Architecture Fundamentals

1. **Data Warehouse vs Data Lake vs Data Lakehouse**
    - **Course Coverage:** 🟢 Covered in Class
    1. Structured vs semi-structured data
    2. OLAP vs OLTP
    3. Data lakehouse pattern
    4. Lab Exercise

2. **Dimensional Modelling**
    - **Course Coverage:** 🟢 Covered in Class
    1. Star schema vs snowflake schema
    2. Fact tables and dimension tables
    3. SCD — Slowly Changing Dimensions (Type 1, 2, 3)
    4. Conformed dimensions
    5. Lab Exercise

3. **ETL vs ELT**
    - **Course Coverage:** 🟢 Covered in Class
    1. Extract, Transform, Load pipeline
    2. ELT with modern cloud warehouses
    3. Data quality and validation
    4. Lab Exercise

---

### Module 2 — Modern Cloud Data Warehouses

#### 2.1. BigQuery, Redshift, Snowflake Overview

1. **Amazon Redshift**
    - **Course Coverage:** 🟢 Covered in Class
    1. Columnar storage and MPP architecture
    2. Distribution and sort keys
    3. Redshift Spectrum for data lake queries
    4. Lab Exercise

2. **Google BigQuery**
    - **Course Coverage:** 🟢 Covered in Class
    1. Serverless architecture
    2. BigQuery ML
    3. Partitioning and clustering
    4. Lab Exercise

---

### Module 3 — dbt (Data Build Tool)

#### 3.1. Analytics Engineering with dbt

1. **dbt Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Models, sources, refs
    2. Materializations — table, view, incremental
    3. Tests and documentation
    4. Lab Exercise

2. **dbt Advanced Patterns**
    - **Course Coverage:** 🟡 Optional Discussion
    1. Macros and Jinja templating
    2. Packages and hooks
    3. Deployment — dbt Cloud vs Core
    4. Lab Exercise

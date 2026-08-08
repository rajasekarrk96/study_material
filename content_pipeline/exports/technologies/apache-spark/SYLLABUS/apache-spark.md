# Apache Spark — Master Syllabus

**Target Role:** Data Engineer / Big Data Engineer  
**Difficulty Level:** Intermediate → Advanced  
**Estimated Duration:** 40 Hours  
**Prerequisites:** Python, SQL, Big Data Fundamentals  

---

## Study Flow

---

### Module 1 — Spark Fundamentals

#### 1.1. Spark Architecture

1. **Spark Architecture Overview**
    - **Course Coverage:** 🟢 Covered in Class
    1. Driver, Executor, Cluster Manager
    2. RDD — Resilient Distributed Datasets
    3. DAG — Directed Acyclic Graph execution
    4. Lab Exercise

2. **PySpark Setup and SparkSession**
    - **Course Coverage:** 🟢 Covered in Class
    1. SparkSession and SparkContext
    2. Deployment modes — local, standalone, YARN
    3. Lab Exercise

---

### Module 2 — Spark DataFrames and SQL

#### 2.1. DataFrame API

1. **DataFrame Operations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Creating DataFrames — from CSV, JSON, Parquet
    2. Transformations — select, filter, groupBy, join
    3. Actions — count, collect, show, write
    4. Lab Exercise

2. **Spark SQL**
    - **Course Coverage:** 🟢 Covered in Class
    1. Registering temp views
    2. SQL queries on DataFrames
    3. Performance — predicate pushdown, column pruning
    4. Lab Exercise

3. **Spark Optimization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Catalyst optimizer
    2. Tungsten execution engine
    3. Partitioning, caching, broadcasting
    4. Lab Exercise

---

### Module 3 — Spark ML and Streaming

#### 3.1. MLlib

1. **Spark MLlib Pipelines**
    - **Course Coverage:** 🟢 Covered in Class
    1. Transformers and Estimators
    2. ML Pipeline API
    3. Regression, Classification, Clustering in MLlib
    4. Lab Exercise

2. **Structured Streaming**
    - **Course Coverage:** 🟢 Covered in Class
    1. Streaming DataFrame API
    2. Reading from Kafka
    3. Windowing and watermarks
    4. Lab Exercise

---

### Module 4 — Delta Lake and Production

#### 4.1. Delta Lake

1. **Delta Lake Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. ACID transactions on data lakes
    2. Time travel and versioning
    3. Schema evolution
    4. Lab Exercise

2. **Databricks Platform**
    - **Course Coverage:** 🟡 Optional Discussion
    1. Databricks workspace and clusters
    2. Unity Catalog
    3. Lab Exercise

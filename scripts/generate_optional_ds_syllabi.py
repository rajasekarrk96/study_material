"""
Generate placeholder syllabi for optional DS courses that have no source in docs/syllabus/.
Run from project root: python scripts/generate_optional_ds_syllabi.py
"""
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

EXPORT_DIR = Path(r"d:\My Drive\all files\PROJECT FILES\notes\exports\data-science-learning-path")

SYLLABI = {

"tableau.md": """# Tableau — Master Syllabus

**Target Role:** Data Analyst / BI Developer  
**Difficulty Level:** Beginner → Intermediate  
**Estimated Duration:** 30 Hours  
**Prerequisites:** Data Analysis fundamentals, basic SQL  

---

## Study Flow

---

### Module 1 — Tableau Fundamentals

#### 1.1. Getting Started

1. **Tableau Desktop Interface**
    - **Course Coverage:** 🟢 Covered in Class
    1. Workspace layout — shelves, marks, filters
    2. Data pane vs Analytics pane
    3. Connecting to data sources
    4. Lab Exercise

2. **Data Connection and Preparation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Connecting to Excel, CSV, SQL databases
    2. Data interpreter and cleaning
    3. Joins, unions, and data blending
    4. Lab Exercise

3. **Dimensions and Measures**
    - **Course Coverage:** 🟢 Covered in Class
    1. Blue vs green pills
    2. Discrete vs continuous
    3. Aggregation types
    4. Lab Exercise

---

### Module 2 — Charts and Visualizations

#### 2.1. Core Chart Types

1. **Bar and Line Charts**
    - **Course Coverage:** 🟢 Covered in Class
    1. Horizontal and vertical bar charts
    2. Dual-axis charts
    3. Trend lines and reference lines
    4. Lab Exercise

2. **Maps and Geographic Visualizations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Symbol maps and filled maps
    2. Geocoding and custom territories
    3. Lab Exercise

3. **Advanced Charts**
    - **Course Coverage:** 🟡 Optional Discussion
    1. Box-and-whisker plots
    2. Scatter plots and bullet charts
    3. Treemaps, heat maps, highlight tables
    4. Lab Exercise

---

### Module 3 — Calculations and Analytics

#### 3.1. Calculated Fields

1. **Basic Calculations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Arithmetic and string functions
    2. IF/CASE logic
    3. Date calculations
    4. Lab Exercise

2. **Table Calculations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Running total, percent of total
    2. Rank and window calculations
    3. FIXED, INCLUDE, EXCLUDE LOD expressions
    4. Lab Exercise

---

### Module 4 — Dashboards and Publishing

#### 4.1. Dashboard Design

1. **Dashboard Layout and Design**
    - **Course Coverage:** 🟢 Covered in Class
    1. Layout containers — vertical/horizontal
    2. Device-specific layouts
    3. Interactivity — filters, actions, parameters
    4. Lab Exercise

2. **Tableau Server and Tableau Public**
    - **Course Coverage:** 🟢 Covered in Class
    1. Publishing workbooks
    2. Row-level security basics
    3. Embedded analytics overview
    4. Lab Exercise
""",

"excel-data-analysis.md": """# Excel for Data Analysis — Master Syllabus

**Target Role:** Data Analyst / Business Analyst  
**Difficulty Level:** Beginner  
**Estimated Duration:** 25 Hours  
**Prerequisites:** None  

---

## Study Flow

---

### Module 1 — Excel Fundamentals for Analysis

#### 1.1. Data Entry and Navigation

1. **Excel Interface and Navigation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Ribbons, sheets, cell references
    2. Named ranges
    3. Keyboard shortcuts for analysts
    4. Lab Exercise

2. **Data Formatting and Validation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Number, date, text formats
    2. Conditional formatting
    3. Data validation rules
    4. Lab Exercise

---

### Module 2 — Core Analysis Functions

#### 2.1. Formulas and Functions

1. **Lookup Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. VLOOKUP, HLOOKUP, XLOOKUP
    2. INDEX-MATCH
    3. Lab Exercise

2. **Statistical Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. COUNT, COUNTIF, COUNTIFS
    2. SUMIF, AVERAGEIF
    3. STDEV, VAR, CORREL
    4. Lab Exercise

3. **Text Functions**
    - **Course Coverage:** 🟢 Covered in Class
    1. LEFT, RIGHT, MID, LEN
    2. TRIM, CLEAN, SUBSTITUTE
    3. Lab Exercise

---

### Module 3 — Pivot Tables and Charts

#### 3.1. PivotTables

1. **PivotTable Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Creating and configuring PivotTables
    2. Grouping, filtering, slicers
    3. Calculated fields
    4. Lab Exercise

2. **Charts and Dashboards**
    - **Course Coverage:** 🟢 Covered in Class
    1. PivotCharts
    2. Sparklines
    3. Dashboard with slicers and timelines
    4. Lab Exercise

---

### Module 4 — Power Query and Power Pivot

#### 4.1. Modern Excel Data Tools

1. **Power Query (Get & Transform)**
    - **Course Coverage:** 🟢 Covered in Class
    1. Importing and transforming data
    2. Merging and appending queries
    3. M language basics
    4. Lab Exercise

2. **Power Pivot and Data Models**
    - **Course Coverage:** 🟡 Optional Discussion
    1. Creating relationships
    2. DAX fundamentals
    3. Calculated columns and measures
    4. Lab Exercise
""",

"cloud-ai-services.md": """# Cloud AI Services — Master Syllabus

**Target Role:** ML Engineer / Cloud Data Scientist  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 35 Hours  
**Prerequisites:** Machine Learning fundamentals, Python, basic cloud concepts  

---

## Study Flow

---

### Module 1 — Cloud AI Platform Overview

#### 1.1. Introduction

1. **Cloud AI Ecosystem**
    - **Course Coverage:** 🟢 Covered in Class
    1. AWS AI/ML stack — SageMaker, Rekognition, Comprehend
    2. GCP AI stack — Vertex AI, AutoML, BigQuery ML
    3. Azure AI stack — Azure ML, Cognitive Services
    4. Lab Exercise

2. **Managed ML Platforms**
    - **Course Coverage:** 🟢 Covered in Class
    1. AutoML concepts
    2. Notebook environments in the cloud
    3. Compute — GPUs, TPUs
    4. Lab Exercise

---

### Module 2 — AWS AI Services

#### 2.1. AWS SageMaker

1. **SageMaker Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. SageMaker Studio
    2. Training jobs and experiments
    3. Model registry
    4. Lab Exercise

2. **AWS Pre-built AI Services**
    - **Course Coverage:** 🟢 Covered in Class
    1. Rekognition — image and video analysis
    2. Comprehend — NLP
    3. Textract — document understanding
    4. Forecast — time series
    5. Lab Exercise

---

### Module 3 — GCP AI Services

#### 3.1. Vertex AI

1. **Vertex AI Workbench and Pipelines**
    - **Course Coverage:** 🟢 Covered in Class
    1. Managed notebooks
    2. Vertex AI Pipelines (Kubeflow-based)
    3. Model monitoring
    4. Lab Exercise

2. **GCP Pre-built AI APIs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Vision AI, Video AI
    2. Natural Language API
    3. Translation and Speech APIs
    4. Lab Exercise

---

### Module 4 — Azure AI Services

#### 4.1. Azure Machine Learning

1. **Azure ML Studio**
    - **Course Coverage:** 🟢 Covered in Class
    1. Workspaces, compute clusters, datastores
    2. Designer and AutoML
    3. Azure ML Pipelines
    4. Lab Exercise

2. **Azure Cognitive Services**
    - **Course Coverage:** 🟡 Optional Discussion
    1. Computer Vision, Form Recognizer
    2. Azure OpenAI Service integration
    3. Lab Exercise
""",

"big-data-fundamentals.md": """# Big Data Fundamentals — Master Syllabus

**Target Role:** Data Engineer / Big Data Engineer  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 30 Hours  
**Prerequisites:** Python, SQL, Linux basics  

---

## Study Flow

---

### Module 1 — Big Data Concepts

#### 1.1. Introduction

1. **Big Data — The 5 Vs**
    - **Course Coverage:** 🟢 Covered in Class
    1. Volume, Velocity, Variety, Veracity, Value
    2. Big Data vs Traditional Data
    3. Use cases — recommendation, fraud detection, genomics
    4. Lab Exercise

2. **Distributed Systems Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. CAP theorem
    2. Horizontal vs vertical scaling
    3. Fault tolerance and replication
    4. Lab Exercise

---

### Module 2 — Hadoop Ecosystem

#### 2.1. Hadoop Architecture

1. **HDFS — Hadoop Distributed File System**
    - **Course Coverage:** 🟢 Covered in Class
    1. NameNode and DataNode
    2. Block replication
    3. HDFS commands
    4. Lab Exercise

2. **MapReduce Programming Model**
    - **Course Coverage:** 🟢 Covered in Class
    1. Map and Reduce phases
    2. Combiner and partitioner
    3. Writing MapReduce jobs in Python
    4. Lab Exercise

3. **YARN Resource Manager**
    - **Course Coverage:** 🟡 Optional Discussion
    1. ResourceManager and NodeManager
    2. Application lifecycle
    3. Lab Exercise

---

### Module 3 — Apache Hive and Pig

#### 3.1. SQL-on-Hadoop

1. **Apache Hive**
    - **Course Coverage:** 🟢 Covered in Class
    1. HiveQL — DDL and DML
    2. Partitioning and bucketing
    3. Hive on Tez vs MapReduce
    4. Lab Exercise

2. **Apache Pig**
    - **Course Coverage:** 🟡 Optional Discussion
    1. Pig Latin data flow language
    2. Pig vs Hive comparison
    3. Lab Exercise

---

### Module 4 — Data Lakes and Modern Architecture

#### 4.1. Modern Big Data Architecture

1. **Data Lake Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Lambda architecture
    2. Kappa architecture
    3. Data lake vs data warehouse
    4. Lab Exercise

2. **Apache Kafka — Streaming Foundation**
    - **Course Coverage:** 🟢 Covered in Class
    1. Producer, consumer, broker, topic
    2. Partitions and offsets
    3. Kafka with Python
    4. Lab Exercise
""",

"apache-spark.md": """# Apache Spark — Master Syllabus

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
""",

"apache-airflow.md": """# Apache Airflow — Master Syllabus

**Target Role:** Data Engineer / MLOps Engineer  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 25 Hours  
**Prerequisites:** Python, SQL, Docker basics  

---

## Study Flow

---

### Module 1 — Airflow Fundamentals

#### 1.1. DAGs and Tasks

1. **Airflow Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Webserver, Scheduler, Executor, Metadata DB
    2. Executors — LocalExecutor, CeleryExecutor, KubernetesExecutor
    3. Lab Exercise

2. **DAG Definition**
    - **Course Coverage:** 🟢 Covered in Class
    1. DAG object and schedule_interval
    2. Task dependencies — set_upstream/set_downstream
    3. Bitshift operators >> and <<
    4. Lab Exercise

3. **Core Operators**
    - **Course Coverage:** 🟢 Covered in Class
    1. BashOperator, PythonOperator
    2. BranchPythonOperator
    3. EmailOperator and SLAs
    4. Lab Exercise

---

### Module 2 — Advanced DAG Patterns

#### 2.1. Dynamic and Parameterized DAGs

1. **TaskFlow API (Airflow 2.x)**
    - **Course Coverage:** 🟢 Covered in Class
    1. @dag and @task decorators
    2. XCom and data passing
    3. Dynamic task mapping
    4. Lab Exercise

2. **Airflow Connections and Variables**
    - **Course Coverage:** 🟢 Covered in Class
    1. Connection types — PostgreSQL, S3, HTTP
    2. Hooks — PostgresHook, S3Hook
    3. Variables and secrets
    4. Lab Exercise

---

### Module 3 — Monitoring and Production

#### 3.1. Airflow in Production

1. **Monitoring and Alerting**
    - **Course Coverage:** 🟢 Covered in Class
    1. Task retries and timeouts
    2. SLA misses and email alerts
    3. Airflow metrics with StatsD
    4. Lab Exercise

2. **Airflow with Docker and Kubernetes**
    - **Course Coverage:** 🟢 Covered in Class
    1. Docker Compose setup
    2. KubernetesPodOperator
    3. Airflow on Helm
    4. Lab Exercise
""",

"mlflow.md": """# MLflow — Master Syllabus

**Target Role:** MLOps Engineer / ML Engineer  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 20 Hours  
**Prerequisites:** Machine Learning, Python, Docker basics  

---

## Study Flow

---

### Module 1 — MLflow Tracking

#### 1.1. Experiment Tracking

1. **MLflow Tracking Server**
    - **Course Coverage:** 🟢 Covered in Class
    1. Tracking URI — local and remote
    2. Experiments, runs, metrics, params, artifacts
    3. MLflow UI
    4. Lab Exercise

2. **Logging with MLflow**
    - **Course Coverage:** 🟢 Covered in Class
    1. mlflow.log_param, mlflow.log_metric
    2. mlflow.log_artifact
    3. Auto-logging — mlflow.sklearn.autolog
    4. Lab Exercise

---

### Module 2 — MLflow Models

#### 2.1. Model Management

1. **MLflow Model Format**
    - **Course Coverage:** 🟢 Covered in Class
    1. MLmodel file and flavors
    2. Saving and loading models
    3. Custom Python function flavors
    4. Lab Exercise

2. **MLflow Model Registry**
    - **Course Coverage:** 🟢 Covered in Class
    1. Staging, Production, Archived stages
    2. Model versioning
    3. Webhooks and notifications
    4. Lab Exercise

---

### Module 3 — MLflow Projects and Deployment

#### 3.1. Reproducible ML

1. **MLflow Projects**
    - **Course Coverage:** 🟢 Covered in Class
    1. MLproject file — entry points, parameters
    2. Running projects locally and on Databricks
    3. Lab Exercise

2. **Model Serving**
    - **Course Coverage:** 🟢 Covered in Class
    1. mlflow models serve
    2. Docker container deployment
    3. Integration with FastAPI
    4. Lab Exercise
""",

"kubeflow.md": """# Kubeflow — Master Syllabus

**Target Role:** MLOps Engineer / Platform Engineer  
**Difficulty Level:** Advanced  
**Estimated Duration:** 30 Hours  
**Prerequisites:** Kubernetes, Python, Machine Learning, Docker  

---

## Study Flow

---

### Module 1 — Kubeflow Fundamentals

#### 1.1. Kubeflow on Kubernetes

1. **Kubeflow Architecture**
    - **Course Coverage:** 🟢 Covered in Class
    1. Kubeflow components — Pipelines, Notebooks, Katib, Serving
    2. Kubernetes CRDs for ML workloads
    3. Kubeflow installation — kubeadm and managed options
    4. Lab Exercise

2. **Kubeflow Notebooks**
    - **Course Coverage:** 🟢 Covered in Class
    1. Notebook Server lifecycle
    2. PVC mounting and GPU allocation
    3. Lab Exercise

---

### Module 2 — Kubeflow Pipelines

#### 2.1. Pipeline SDK

1. **Pipeline Components and Steps**
    - **Course Coverage:** 🟢 Covered in Class
    1. @kfp.component decorator
    2. ContainerOp vs Python function components
    3. Artifact passing between steps
    4. Lab Exercise

2. **Pipeline Compilation and Execution**
    - **Course Coverage:** 🟢 Covered in Class
    1. Compiling to YAML
    2. Submitting runs and experiments
    3. Conditional and parallel steps
    4. Lab Exercise

---

### Module 3 — Katib and Serving

#### 3.1. Hyperparameter Tuning with Katib

1. **Katib Experiment Spec**
    - **Course Coverage:** 🟢 Covered in Class
    1. Search algorithm — Random, Bayesian, Hyperband
    2. Metrics collector
    3. Lab Exercise

2. **KServe (Model Serving)**
    - **Course Coverage:** 🟢 Covered in Class
    1. InferenceService CRD
    2. Canary rollout and A/B testing
    3. Transformer and explainer components
    4. Lab Exercise
""",

"data-warehousing.md": """# Data Warehousing — Master Syllabus

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
""",

"snowflake.md": """# Snowflake — Master Syllabus

**Target Role:** Data Engineer / Analytics Engineer / Data Architect  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 25 Hours  
**Prerequisites:** SQL, Data Warehousing concepts  

---

## Study Flow

---

### Module 1 — Snowflake Architecture

#### 1.1. Core Concepts

1. **Snowflake Architecture Overview**
    - **Course Coverage:** 🟢 Covered in Class
    1. Three-layer architecture — Storage, Compute, Cloud Services
    2. Virtual warehouses and credits
    3. Multi-cluster warehouses
    4. Lab Exercise

2. **Data Storage in Snowflake**
    - **Course Coverage:** 🟢 Covered in Class
    1. Micro-partitions and data clustering
    2. Automatic compression and columnar format
    3. Zero-copy cloning
    4. Lab Exercise

---

### Module 2 — Snowflake SQL and Data Loading

#### 2.1. SQL in Snowflake

1. **Snowflake DDL and DML**
    - **Course Coverage:** 🟢 Covered in Class
    1. Databases, schemas, tables, views
    2. Streams and tasks
    3. Dynamic data masking
    4. Lab Exercise

2. **Data Loading and Unloading**
    - **Course Coverage:** 🟢 Covered in Class
    1. COPY INTO command
    2. Snowpipe — continuous ingestion
    3. External stages — S3, GCS, Azure Blob
    4. Lab Exercise

---

### Module 3 — Snowflake Advanced Features

#### 3.1. Semi-structured Data and Sharing

1. **Semi-Structured Data (VARIANT)**
    - **Course Coverage:** 🟢 Covered in Class
    1. JSON, AVRO, Parquet in Snowflake
    2. FLATTEN function
    3. PARSE_JSON and lateral joins
    4. Lab Exercise

2. **Snowflake Data Sharing**
    - **Course Coverage:** 🟡 Optional Discussion
    1. Data sharing without copying
    2. Marketplace listings
    3. Lab Exercise

3. **Snowpark (Python in Snowflake)**
    - **Course Coverage:** 🟡 Optional Discussion
    1. DataFrame API in Snowpark
    2. Python UDFs
    3. Snowpark ML overview
    4. Lab Exercise
""",

"feature-engineering.md": """# Feature Engineering — Master Syllabus

**Target Role:** ML Engineer / Data Scientist  
**Difficulty Level:** Intermediate  
**Estimated Duration:** 25 Hours  
**Prerequisites:** Machine Learning, Python, Pandas, Statistics  

---

## Study Flow

---

### Module 1 — Feature Engineering Foundations

#### 1.1. Understanding Features

1. **Feature Types and Representations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Numerical, categorical, ordinal, binary
    2. Text, image, audio as features
    3. Feature importance vs feature quality
    4. Lab Exercise

2. **Exploratory Data Analysis for FE**
    - **Course Coverage:** 🟢 Covered in Class
    1. Distribution analysis
    2. Correlation and multicollinearity
    3. Target leakage identification
    4. Lab Exercise

---

### Module 2 — Numerical and Categorical Features

#### 2.1. Transformations

1. **Numerical Feature Engineering**
    - **Course Coverage:** 🟢 Covered in Class
    1. Log, sqrt, Box-Cox transformations
    2. Binning — equal-width, equal-frequency
    3. Interaction features and ratios
    4. Polynomial features
    5. Lab Exercise

2. **Categorical Feature Engineering**
    - **Course Coverage:** 🟢 Covered in Class
    1. One-Hot Encoding, Ordinal Encoding
    2. Target encoding, Leave-One-Out encoding
    3. Frequency encoding
    4. Hashing trick
    5. Lab Exercise

---

### Module 3 — Advanced Feature Engineering

#### 3.1. Time, Text, and Embeddings

1. **Time Series Features**
    - **Course Coverage:** 🟢 Covered in Class
    1. Lag features, rolling statistics
    2. Date-based features — day of week, quarter
    3. Fourier features for seasonality
    4. Lab Exercise

2. **Text Features**
    - **Course Coverage:** 🟢 Covered in Class
    1. Bag of Words, TF-IDF
    2. Word embeddings — Word2Vec, GloVe
    3. Sentence embeddings
    4. Lab Exercise

3. **Feature Selection Methods**
    - **Course Coverage:** 🟢 Covered in Class
    1. Filter methods — correlation, chi-squared
    2. Wrapper methods — RFE
    3. Embedded methods — Lasso, tree importance
    4. SHAP-based feature selection
    5. Lab Exercise

---

### Module 4 — Feature Stores

#### 4.1. Feature Store Architecture

1. **What is a Feature Store?**
    - **Course Coverage:** 🟡 Optional Discussion
    1. Online vs offline feature stores
    2. Feature reuse and consistency
    3. Feast, Hopsworks, Tecton overview
    4. Lab Exercise
""",

"data-visualization.md": """# Data Visualization — Master Syllabus

**Target Role:** Data Analyst / Data Scientist  
**Difficulty Level:** Beginner → Intermediate  
**Estimated Duration:** 25 Hours  
**Prerequisites:** Python, Pandas basics  

---

## Study Flow

---

### Module 1 — Visualization Fundamentals

#### 1.1. Principles of Visual Design

1. **Data Visualization Theory**
    - **Course Coverage:** 🟢 Covered in Class
    1. Preattentive attributes — color, size, shape
    2. Gestalt principles
    3. Choosing the right chart type
    4. Lab Exercise

2. **Color Theory for Data**
    - **Course Coverage:** 🟢 Covered in Class
    1. Sequential, diverging, categorical palettes
    2. Accessibility — colorblind-safe palettes
    3. Lab Exercise

---

### Module 2 — Python Visualization Libraries

#### 2.1. Matplotlib and Seaborn

1. **Matplotlib Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Figure, Axes, Artists hierarchy
    2. Line, bar, scatter, histogram plots
    3. Subplots and layout management
    4. Lab Exercise

2. **Seaborn Statistical Plots**
    - **Course Coverage:** 🟢 Covered in Class
    1. Distribution plots — histplot, kdeplot, boxplot
    2. Categorical plots — barplot, violinplot
    3. Pair plots and heatmaps
    4. Lab Exercise

3. **Plotly and Interactive Visualizations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Plotly Express for quick charts
    2. Graph Objects for custom charts
    3. Plotly Dash for dashboards
    4. Lab Exercise

---

### Module 3 — Advanced Visualizations

#### 3.1. Specialized Chart Types

1. **Geospatial Visualization**
    - **Course Coverage:** 🟡 Optional Discussion
    1. Choropleth maps with Plotly
    2. Folium for interactive maps
    3. Lab Exercise

2. **Network Graphs**
    - **Course Coverage:** 🟡 Optional Discussion
    1. NetworkX and Gephi
    2. Force-directed layouts
    3. Lab Exercise

3. **Dashboard Design with Dash and Streamlit**
    - **Course Coverage:** 🟢 Covered in Class
    1. Streamlit app structure
    2. Interactive widgets — sliders, selectboxes
    3. Deploying Streamlit apps
    4. Lab Exercise
""",

}


def write_syllabi():
    syl_dir = EXPORT_DIR / "SYLLABUS"
    syl_dir.mkdir(parents=True, exist_ok=True)
    for filename, content in SYLLABI.items():
        dest = syl_dir / filename
        dest.write_text(content.strip() + "\n", encoding="utf-8")
        lines = content.count("\n")
        print(f"  [GEN] SYLLABUS/{filename}  ({lines} lines)")
    print(f"\n  Done — {len(SYLLABI)} optional syllabi generated.")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("  Generating Optional DS Course Syllabi")
    print("="*60 + "\n")
    write_syllabi()

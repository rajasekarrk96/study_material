# Apache Airflow — Master Syllabus

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

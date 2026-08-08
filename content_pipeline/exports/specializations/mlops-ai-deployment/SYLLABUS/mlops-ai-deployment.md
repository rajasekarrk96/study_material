# MLOps and AI Deployment — Master Syllabus

---

# Course Information

**Course Name:** MLOps and AI Deployment

**Category:** Specialization Course

**Learning Path(s):**

- ML Engineer
- MLOps Engineer
- DevOps Engineer

**Difficulty:** Beginner

**Estimated Duration:** 20 Hours

**Prerequisites:**

- Machine Learning
- Docker
- Core Python

**Course Status:** COMING_SOON

---

# Module 1 — Experiment Tracking

## Lesson 1.1 — MLflow Fundamentals

**Course Coverage:** 🟢 Covered in Class

### Topics

- Mlflow Tracking
- Start Run
- Log Param
- Log Metric
- Log Artifact
- Mlflow Ui
- Autolog

## Lesson 1.2 — MLflow Advanced Features

**Course Coverage:** 🟢 Covered in Class

### Topics

- Nested Runs
- Log Dict
- Log Figure
- Log Table
- Search Runs
- Remote Tracking
- Mlflow Evaluate

## Lesson 1.3 — Weights and Biases

**Course Coverage:** 🟢 Covered in Class

### Topics

- Wandb Init
- Wandb Log
- Wandb Artifact
- Wandb Table
- Sweeps
- Wandb Reports
- Wandb Alert

## Lesson 1.4 — DVC Data Version Control

**Course Coverage:** 🟢 Covered in Class

### Topics

- Dvc Init
- Dvc Add
- Dvc Push
- Dvc Pull
- Dvc Run
- Dvc Repro
- Dvc Metrics

## Lesson 1.5 — Experiment Design and Hyperparameter Tuning

**Course Coverage:** 🟢 Covered in Class

### Topics

- Grid Search
- Random Search
- Optuna
- Hyperband
- Ray Tune
- Wandb Sweeps
- Hpo

## Lesson 1.6 — Reproducibility and Experiment Management

**Course Coverage:** 🟢 Covered in Class

### Topics

- Seed Control
- Conda Env
- Docker Repro
- Mlflow Projects
- Git Hash
- Deterministic

## Lesson 1.7 — Comparing and Selecting Models

**Course Coverage:** 🟢 Covered in Class

### Topics

- Multi Metric
- Pareto Frontier
- Statistical Significance
- Mlflow Compare
- Champion Challenger

---

# Module 2 — Model Packaging

## Lesson 2.1 — MLflow Model Logging and Flavors

**Course Coverage:** 🟢 Covered in Class

### Topics

- Sklearn Flavor
- Pytorch Flavor
- Pyfunc
- Transformers Flavor
- Signature
- Input Example

## Lesson 2.2 — MLflow Model Registry

**Course Coverage:** 🟢 Covered in Class

### Topics

- Register Model
- Model Versions
- Staging Production
- Model Alias
- Webhooks
- Registry Ui
- Lineage

## Lesson 2.3 — ONNX Model Export

**Course Coverage:** 🟢 Covered in Class

### Topics

- Onnx
- Torch Onnx Export
- Onnxruntime
- Opset
- Optimum
- Onnx Checker

## Lesson 2.4 — TorchScript and TorchServe

**Course Coverage:** 🟢 Covered in Class

### Topics

- Torchscript
- Jit Script
- Jit Trace
- Torchserve
- Mar Package
- Handler
- Prometheus Torchserve

## Lesson 2.5 — BentoML

**Course Coverage:** 🟢 Covered in Class

### Topics

- Bentoml Service
- Runner
- Bento Build
- Bentoml Containerize
- Bentocloud
- Adaptive Batching

## Lesson 2.6 — Model Cards and Documentation

**Course Coverage:** 🟢 Covered in Class

### Topics

- Model Card
- Hf Model Card
- Eval Results
- Bias Section
- License
- Dataset Cards
- Model Card Toolkit

---

# Module 3 — ML CI/CD

## Lesson 3.1 — ML Pipeline Fundamentals

**Course Coverage:** 🟢 Covered in Class

### Topics

- Dag Pipeline
- Parameterization
- Caching
- Artifacts
- Orchestration Tools
- Airflow
- Zenml

## Lesson 3.2 — GitHub Actions for ML

**Course Coverage:** 🟢 Covered in Class

### Topics

- ML Ci Workflow
- Dvc Pull
- Cml
- Model Validation Gate
- GPU Runner
- Mlflow Logging

## Lesson 3.3 — ZenML

**Course Coverage:** 🟢 Covered in Class

### Topics

- Zenml Pipeline
- Step Decorator
- Pipeline Decorator
- Zenml Stack
- Zenml Integrations
- Zenml Cloud

## Lesson 3.4 — Kubeflow Pipelines

**Course Coverage:** 🟢 Covered in Class

### Topics

- Kfp Component
- Kfp Pipeline
- Containerized Steps
- Kfp Compiler
- Kfp Client
- Kfp V2

## Lesson 3.5 — MLflow Projects

**Course Coverage:** 🟢 Covered in Class

### Topics

- Mlproject
- Entry Points
- Conda Yaml
- Docker Env
- Mlflow Run
- Multi Step Project

## Lesson 3.6 — Continuous Training Pipelines

**Course Coverage:** 🟢 Covered in Class

### Topics

- Ct Concept
- Drift Trigger
- Schedule Trigger
- S3 Event
- Shadow Deployment
- Canary Training
- Feedback Loop

## Lesson 3.7 — Model Testing in CI

**Course Coverage:** 🟢 Covered in Class

### Topics

- Unit Tests ML
- Integration Tests
- Quality Gate
- Great Expectations
- Pytest ML
- Checklist
- Evidently Ci

---

# Module 4 — Model Serving

## Lesson 4.1 — FastAPI Model Serving

**Course Coverage:** 🟢 Covered in Class

### Topics

- Fastapi
- Lifespan
- Predict Endpoint
- Async Inference
- Batch Endpoint
- Health Check
- Prometheus

## Lesson 4.2 — Triton Inference Server

**Course Coverage:** 🟢 Covered in Class

### Topics

- Triton
- Model Repository
- Config Pbtxt
- Dynamic Batching
- Tritonclient
- Ensemble
- Perf Analyzer

## Lesson 4.3 — Seldon Core

**Course Coverage:** 🟢 Covered in Class

### Topics

- Seldon Deployment
- Crd Yaml
- Pre Packaged
- Custom Python
- Canary
- Explainers
- Seldon Client

## Lesson 4.4 — KServe

**Course Coverage:** 🟢 Covered in Class

### Topics

- Inference Service
- Custom Predictor
- Autoscaling
- Knative
- Scale To Zero
- Transformer
- Grpc V2

## Lesson 4.5 — Containerization for ML

**Course Coverage:** 🟢 Covered in Class

### Topics

- Multi Stage Docker
- Cuda Base
- Model Baking
- Model Mounting
- Buildx
- Ecr
- Trivy

## Lesson 4.6 — Kubernetes for ML Workloads

**Course Coverage:** 🟢 Covered in Class

### Topics

- Deployments
- GPU Scheduling
- Resource Limits
- Hpa
- Helm Charts
- Kubectl
- Namespace

## Lesson 4.7 — A/B Testing and Canary Deployments

**Course Coverage:** 🟢 Covered in Class

### Topics

- Ab Design
- Feature Flags
- Canary
- Istio
- Nginx Ingress
- Per Variant
- Rollback

---

# Module 5 — LLM Deployment

## Lesson 5.1 — Production LLM Serving Architecture

**Course Coverage:** 🟢 Covered in Class

### Topics

- Load Balancer
- Litellm Proxy
- GPU Fleet
- Sla Targets
- Autoscaling
- Cost Per Token
- Fallback Chains

## Lesson 5.2 — vLLM Production Deployment

**Course Coverage:** 🟢 Covered in Class

### Topics

- Vllm Docker
- Tensor Parallel
- Prefix Caching
- Max Num Seqs
- Quantized
- Health Endpoint
- K8s Vllm

## Lesson 5.3 — Fine-Tuned Model Deployment

**Course Coverage:** 🟢 Covered in Class

### Topics

- Merge Lora
- Push To Hub
- Private Hub
- Vllm Hub
- Tgi Hub
- Gguf Deploy
- Model Versioning

## Lesson 5.4 — Agent Deployment at Scale

**Course Coverage:** 🟢 Covered in Class

### Topics

- Langgraph Cloud
- Self Hosted
- Redis Thread
- Celery Agents
- Keda
- Multi Tenant
- Cost Tracking

## Lesson 5.5 — Embedding Service Deployment

**Course Coverage:** 🟢 Covered in Class

### Topics

- Infinity Emb
- Tei
- Batch Encoding
- Hpa GPU
- Semantic Cache
- Self Hosted Cost

## Lesson 5.6 — Model Versioning and Blue-Green

**Course Coverage:** 🟢 Covered in Class

### Topics

- Blue Green
- Dns Swap
- Schema Compat
- Registry Trigger
- Rollback
- Feature Flag Model

## Lesson 5.7 — Serverless ML Deployment

**Course Coverage:** 🟢 Covered in Class

### Topics

- Lambda ML
- Modal
- Replicate
- Banana
- Cold Start
- Warm Pools
- Pay Per Inference

---

# Module 6 — ML Monitoring

## Lesson 6.1 — ML Monitoring Fundamentals

**Course Coverage:** 🟢 Covered in Class

### Topics

- Monitoring Dimensions
- Performance Degradation
- Feedback Loop
- Alerting
- Dashboard
- Slo Sla

## Lesson 6.2 — Data Drift Detection

**Course Coverage:** 🟢 Covered in Class

### Topics

- Covariate Shift
- Label Drift
- Ks Test
- Psi
- Evidently
- Nannyml
- Whylogs

## Lesson 6.3 — Model Performance Monitoring

**Course Coverage:** 🟢 Covered in Class

### Topics

- Online Metrics
- Delayed Labels
- Proxy Metrics
- Evidently Report
- Slice Monitoring
- Alerting

## Lesson 6.4 — LLM Monitoring

**Course Coverage:** 🟢 Covered in Class

### Topics

- Ttft
- Tpot
- Quality Monitoring
- Cost Monitoring
- Safety Monitoring
- Langfuse
- Phoenix

## Lesson 6.5 — Evidently AI

**Course Coverage:** 🟢 Covered in Class

### Topics

- Report
- Test Suite
- Presets
- Custom Metrics
- Evidently Ui
- Ci Integration
- Monitoring Dashboard

## Lesson 6.6 — Prometheus and Grafana for ML

**Course Coverage:** 🟢 Covered in Class

### Topics

- Prometheus Scrape
- Custom Metrics
- Alertmanager
- Grafana Dashboard
- Loki
- Dcgm Exporter

## Lesson 6.7 — Root Cause Analysis and Debugging

**Course Coverage:** 🟢 Covered in Class

### Topics

- Log Correlation
- Opentelemetry
- Jaeger
- Error Categorization
- Shap Production
- Replay
- Post Mortem

---

# Module 7 — Feature Stores

## Lesson 7.1 — Feature Store Fundamentals

**Course Coverage:** 🟢 Covered in Class

### Topics

- Feature Store
- Online Offline
- Feature Reuse
- Training Serving Skew
- Point In Time
- Feast
- Hopsworks

## Lesson 7.2 — Feast Feature Store

**Course Coverage:** 🟢 Covered in Class

### Topics

- Feast
- Entity
- Feature View
- Feature Service
- Feast Materialize
- Online Features
- Feast Mlflow

## Lesson 7.3 — Apache Airflow for ML

**Course Coverage:** 🟢 Covered in Class

### Topics

- Airflow Dag
- Python Operator
- Sensor
- Xcoms
- Connections
- Kubernetes Pod Op
- Mlflow Airflow

## Lesson 7.4 — Prefect for ML Pipelines

**Course Coverage:** 🟢 Covered in Class

### Topics

- Prefect Flow
- Task Decorator
- Prefect Deploy
- Prefect Cloud
- Concurrent Runner
- Retries
- Artifacts

## Lesson 7.5 — Data Validation with Great Expectations

**Course Coverage:** 🟢 Covered in Class

### Topics

- Expectation Suite
- Checkpoint
- Data Docs
- Ge Airflow
- Column Exists
- Null Check
- Statistical Check

## Lesson 7.6 — Streaming Data Pipelines for ML

**Course Coverage:** 🟢 Covered in Class

### Topics

- Kafka
- Confluent Kafka
- Flink
- Online Feature
- Prediction Logging
- Kafka Connect
- S3 Ingestion

## Lesson 7.7 — Data Lake and Lakehouse for ML

**Course Coverage:** 🟢 Covered in Class

### Topics

- Delta Lake
- Apache Iceberg
- Deltalake Python
- Training Data Version
- Feature Materialization
- Databricks

---

# Module 8 — MLOps Platforms

## Lesson 8.1 — SageMaker MLOps

**Course Coverage:** 🟢 Covered in Class

### Topics

- Sagemaker Training
- Sagemaker Pipelines
- Model Registry
- Sagemaker Endpoints
- Model Monitor
- Feature Store
- Clarify

## Lesson 8.2 — Vertex AI MLOps

**Course Coverage:** 🟢 Covered in Class

### Topics

- Vertex Pipelines
- Custom Job
- Model Registry
- Vertex Endpoints
- Vertex Feature Store
- Monitoring Job
- Aiplatform Sdk

## Lesson 8.3 — Azure ML

**Course Coverage:** 🟢 Covered in Class

### Topics

- Azure Workspace
- Azure Pipelines
- Command Component
- Managed Endpoint
- Azure Monitoring
- Azure AI ML

## Lesson 8.4 — Databricks ML

**Course Coverage:** 🟢 Covered in Class

### Topics

- Databricks Mlflow
- Unity Catalog
- Feature Engineering
- Model Serving
- Automl
- Delta Live Tables
- Databricks Jobs

## Lesson 8.5 — Cost Optimization and Governance

**Course Coverage:** 🟢 Covered in Class

### Topics

- GPU Cost
- Spot Instances
- Model Compression
- Inference Caching
- Finops
- Governance
- Compliance

---

# Module 9 — Industry Projects

## Lesson 9.1 — End-to-End ML Pipeline Tabular

**Course Coverage:** 🟢 Covered in Class

### Topics

- Dvc
- Zenml
- Mlflow
- Fastapi
- Docker
- Evidently
- Model Registry
- Credit Scoring

## Lesson 9.2 — LLM Fine-Tuning MLOps Pipeline

**Course Coverage:** 🟢 Covered in Class

### Topics

- Qlora
- Wandb
- Mlflow
- Vllm
- Litellm
- Langfuse
- Blue Green LLM

## Lesson 9.3 — RAG System MLOps

**Course Coverage:** 🟢 Covered in Class

### Topics

- Prefect
- Re Index
- Embedding Version
- Ragas Gate
- Langfuse
- Qdrant
- Ab Chunk

## Lesson 9.4 — Real-Time Prediction Service

**Course Coverage:** 🟢 Covered in Class

### Topics

- Feast
- Torchserve
- Fastapi
- Nannyml
- Prometheus
- Hpa
- Canary

## Lesson 9.5 — Multi-Model Serving Platform

**Course Coverage:** 🟢 Covered in Class

### Topics

- Triton
- Model Registry
- API Gateway
- Auto Load
- Grafana
- Cost Per Model
- Helm

## Lesson 9.6 — Full-Stack AI System Grand Capstone

**Course Coverage:** 🟢 Covered in Class

### Topics

- Feature Store
- Model Registry
- Vllm
- Langgraph
- RAG
- Kubernetes
- Grafana
- Langfuse
- Guardrails

---

# Software & Tools

- Python 3.10+
- MLflow
- Docker
- Kubernetes
- FastAPI
- Prometheus
- Grafana

---

# Hardware Requirements

- A computer with Docker installed and cloud account access recommended

---

# Course Completion Summary

**Estimated Hours:** 20 Hours

**Modules:** 9

**Lessons:** 59

**Difficulty:** Beginner

**Course Status:** COMING_SOON

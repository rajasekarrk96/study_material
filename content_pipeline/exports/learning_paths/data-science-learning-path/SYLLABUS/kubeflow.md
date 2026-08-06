# Kubeflow — Master Syllabus

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

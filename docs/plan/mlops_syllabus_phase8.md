# Phase 8: MLOps & AI Deployment — Enterprise Syllabus
## Learning OS Enterprise Standard | Curriculum Architecture v2.0

**Classification**: Chief Curriculum Architect — Syllabus Design Document  
**Phase**: 8 of 8 — FINAL PHASE  
**Domain**: MLOps & AI Deployment  
**Required Previous Phases**: All Phases 1–7  
**Folder Root**: `docs/curriculum/_17_mlops_ai_deployment/`  
**Last Updated**: 2026-07-28

---

## Dependency Graph

```
All Phases 1–7 produce models, agents, and pipelines.
_17_mlops_ai_deployment  ◄── THIS PHASE
    └─ Closes the loop: production → monitor → retrain → redeploy
```

Cross-phase reuse nodes:
- `ML.10_*` training pipelines → MLOps-managed workflows
- `GenAI.14_08` LLM serving → production LLM infra
- `GenAI.14_09` Quantization/compression → serving optimization
- `RAG.15_08` Production RAG → monitored via ML observability
- `Agents.16_08` Agent APIs → part of ML system deployment
- `DL.11_04` PyTorch training → packaged with MLflow/Torchserve

---

## Skills Gained (This Phase)

- Track experiments with MLflow, Weights & Biases, and DVC
- Package and version models with MLflow Model Registry
- Build automated CI/CD pipelines for ML models
- Serve models with FastAPI, TorchServe, Triton Inference Server
- Deploy LLMs and agents at production scale
- Monitor ML models: data drift, concept drift, performance
- Design and operate feature stores
- Build production data pipelines with Airflow, Prefect, and ZenML
- Containerize and orchestrate ML workloads with Docker + Kubernetes
- Apply cost optimization and SLA management for AI systems

---

## Course Structure

```
_17_mlops_ai_deployment/
├── _17_01_experiment_tracking/
├── _17_02_model_packaging_and_registry/
├── _17_03_ml_cicd_pipelines/
├── _17_04_model_serving_infrastructure/
├── _17_05_llm_and_agent_deployment/
├── _17_06_ml_monitoring_and_observability/
├── _17_07_feature_stores_and_data_pipelines/
├── _17_08_mlops_platforms/
└── _17_09_industry_projects/
```

---

## MODULE 01 — Experiment Tracking

**Folder**: `_17_01_experiment_tracking/`  
**Lesson Count**: 7  
**Learning Order**: 1st

### Lessons

#### Lesson 01.01 — MLflow Fundamentals
**File**: `_17_01_01_mlflow_fundamentals.md`

| Topics | Subtopics |
|---|---|
| MLflow overview | Tracking, Models, Registry, Projects |
| `mlflow.start_run` | Context manager |
| `mlflow.log_param` | Hyperparameter logging |
| `mlflow.log_metric` | Single and step-based metrics |
| `mlflow.log_artifact` | Files, plots, configs |
| `mlflow.set_experiment` | Organize runs |
| MLflow UI | `mlflow ui`, compare runs |
| Auto-logging | `mlflow.autolog()` for sklearn/torch |

---

#### Lesson 01.02 — MLflow Advanced Features
**File**: `_17_01_02_mlflow_advanced_features.md`

| Topics | Subtopics |
|---|---|
| Nested runs | Parent-child run hierarchy |
| `mlflow.log_dict` | JSON artifact logging |
| `mlflow.log_figure` | Matplotlib/Plotly figures |
| `mlflow.log_table` | Pandas DataFrame logging |
| `mlflow.set_tags` | Metadata tagging |
| Run search | `MlflowClient.search_runs`, filter |
| Remote tracking server | `MLFLOW_TRACKING_URI`, S3/GCS/Azure backend |
| `mlflow.evaluate` | Model evaluation logging |

---

#### Lesson 01.03 — Weights & Biases (W&B)
**File**: `_17_01_03_weights_and_biases.md`

| Topics | Subtopics |
|---|---|
| `wandb.init` | Project, entity, config |
| `wandb.log` | Metrics, images, tables |
| `wandb.Artifact` | Dataset and model versioning |
| `wandb.Table` | Structured logging |
| W&B Sweeps | Hyperparameter search |
| W&B Reports | Shareable analysis |
| Integrations | HuggingFace Trainer, PyTorch Lightning |
| `wandb.alert` | Metric threshold alerts |

---

#### Lesson 01.04 — DVC — Data Version Control
**File**: `_17_01_04_dvc_data_version_control.md`

| Topics | Subtopics |
|---|---|
| DVC concepts | Data files tracked like code |
| `dvc init` | Initialize in git repo |
| `dvc add` | Track large files |
| `dvc push` / `dvc pull` | Remote storage sync |
| DVC remotes | S3, GCS, Azure, SSH |
| `dvc run` | Pipeline stage definition |
| `dvc repro` | Reproduce pipeline |
| `dvc metrics` | Track experiment metrics in git |

---

#### Lesson 01.05 — Experiment Design and Hyperparameter Tuning
**File**: `_17_01_05_experiment_design_hparam_tuning.md`

| Topics | Subtopics |
|---|---|
| Grid search | `sklearn.model_selection.GridSearchCV` |
| Random search | `RandomizedSearchCV` |
| Bayesian optimization | `optuna`, TPE sampler |
| `optuna.study.create_study` | Direction, sampler |
| Hyperband | ASHA scheduler |
| Ray Tune | `tune.run`, distributed HPO |
| W&B Sweeps | `sweep_config`, `bayes` method |
| MLflow + Optuna | Log HPO results |

---

#### Lesson 01.06 — Reproducibility and Experiment Management
**File**: `_17_01_06_reproducibility_experiment_management.md`

| Topics | Subtopics |
|---|---|
| Seed control | `random`, `numpy`, `torch` seeds |
| Environment capture | `conda env export`, `pip freeze` |
| Docker for reproducibility | Lock environment |
| `mlflow.projects` | Project spec with conda/docker env |
| Git integration | Commit hash in run metadata |
| Deterministic ops | `torch.use_deterministic_algorithms` |
| Experiment naming | Convention and tagging strategy |

---

#### Lesson 01.07 — Comparing and Selecting Models
**File**: `_17_01_07_comparing_selecting_models.md`

| Topics | Subtopics |
|---|---|
| Multi-metric comparison | Primary + secondary metrics |
| Pareto frontier | Accuracy vs latency vs size |
| Statistical significance | Bootstrap, paired t-test |
| MLflow comparison UI | Side-by-side run comparison |
| W&B parallel coordinates | Hyperparameter visualization |
| Champion-challenger | Canary deployment for model comparison |
| Model selection criteria | Business metric alignment |

---

## MODULE 02 — Model Packaging and Registry

**Folder**: `_17_02_model_packaging_and_registry/`  
**Lesson Count**: 6  
**Learning Order**: 2nd

### Lessons

#### Lesson 02.01 — MLflow Model Logging and Flavors
**File**: `_17_02_01_mlflow_model_logging_flavors.md`

| Topics | Subtopics |
|---|---|
| Model flavors | `sklearn`, `pytorch`, `tensorflow`, `pyfunc` |
| `mlflow.sklearn.log_model` | Sklearn model logging |
| `mlflow.pytorch.log_model` | PyTorch logging |
| `mlflow.pyfunc.log_model` | Custom model wrapper |
| `mlflow.transformers.log_model` | HuggingFace logging |
| Signature | Input/output schema |
| Input example | Sample input for validation |
| `mlflow.models.Model` | Direct model management |

---

#### Lesson 02.02 — MLflow Model Registry
**File**: `_17_02_02_mlflow_model_registry.md`

| Topics | Subtopics |
|---|---|
| Register a model | `mlflow.register_model` |
| Model versions | Automatic versioning |
| Stages | Staging → Production → Archived |
| `MlflowClient` | `transition_model_version_stage` |
| Model aliases | `@champion`, `@challenger` |
| Webhooks | Trigger on stage transition |
| Registry UI | Version comparison, lineage |
| Registry as source of truth | CI/CD reads from registry |

---

#### Lesson 02.03 — ONNX and Model Export
**File**: `_17_02_03_onnx_model_export.md`

| Topics | Subtopics |
|---|---|
| ONNX format | Cross-framework interop |
| `torch.onnx.export` | PyTorch → ONNX |
| `onnxruntime` | Fast inference, CPU/GPU |
| Opset version | ONNX operator compatibility |
| ONNX optimization | `onnxruntime.quantization` |
| `optimum` library | HuggingFace → ONNX/TensorRT |
| Verification | `onnx.checker.check_model` |

---

#### Lesson 02.04 — TorchScript and TorchServe
**File**: `_17_02_04_torchscript_torchserve.md`

| Topics | Subtopics |
|---|---|
| TorchScript | `torch.jit.script`, `torch.jit.trace` |
| Save/load | `torch.jit.save`, `torch.jit.load` |
| TorchServe | REST/gRPC model serving |
| `torch-model-archiver` | `.mar` package |
| Handler | `BaseHandler`, custom `handle` |
| Multi-model serving | Multiple `.mar` files |
| Metrics | TorchServe Prometheus metrics |

---

#### Lesson 02.05 — BentoML
**File**: `_17_02_05_bentoml.md`

| Topics | Subtopics |
|---|---|
| BentoML concepts | Service, Runner, Bento |
| `@bentoml.service` | Decorator-based service |
| Runners | `bentoml.picklable_model.get` |
| `bentoml build` | Package into Bento |
| `bentoml containerize` | Docker image |
| `bentoml serve` | Local serving |
| BentoCloud | Managed deployment |
| Adaptive batching | `max_batch_size`, `max_latency_ms` |

---

#### Lesson 02.06 — Model Cards and Documentation
**File**: `_17_02_06_model_cards_documentation.md`

| Topics | Subtopics |
|---|---|
| Model Card overview | Intended use, limitations, metrics |
| HuggingFace Model Card | `README.md` in model repo |
| `model_card_toolkit` | Google toolkit |
| Eval results format | `results` YAML in model card |
| Bias and fairness section | Disaggregated performance |
| License section | Apache 2.0, MIT, Llama Community |
| Dataset cards | Source, preprocessing, splits |

---

## MODULE 03 — ML CI/CD Pipelines

**Folder**: `_17_03_ml_cicd_pipelines/`  
**Lesson Count**: 7  
**Learning Order**: 3rd

### Lessons

#### Lesson 03.01 — ML Pipeline Fundamentals
**File**: `_17_03_01_ml_pipeline_fundamentals.md`

| Topics | Subtopics |
|---|---|
| ML pipeline stages | Data → Feature → Train → Eval → Deploy |
| DAG-based pipelines | Directed acyclic graph |
| Parameterization | Config-driven pipelines |
| Caching | Skip unchanged upstream steps |
| Artifacts | Pass outputs between steps |
| Pipeline vs workflow | Distinction and overlap |
| Orchestration tools | Airflow, Prefect, ZenML, Kubeflow |

---

#### Lesson 03.02 — GitHub Actions for ML
**File**: `_17_03_02_github_actions_ml.md`

| Topics | Subtopics |
|---|---|
| ML CI workflow | Trigger on PR/push |
| `actions/checkout` | Code checkout |
| `actions/setup-python` | Python environment |
| DVC pull in CI | Reproduce data artifacts |
| Run training in CI | GPU runner, self-hosted |
| MLflow logging | Log results to remote server |
| Model validation gate | Fail if accuracy drops |
| `cml` | Continuous Machine Learning, PR comments |

---

#### Lesson 03.03 — ZenML
**File**: `_17_03_03_zenml.md`

| Topics | Subtopics |
|---|---|
| ZenML concepts | Pipeline, Step, Artifact, Stack |
| `@step` decorator | Typed input/output |
| `@pipeline` decorator | Compose steps |
| ZenML Stack | Orchestrator + artifact store + model deployer |
| `zenml stack set` | Configure active stack |
| `zenml pipeline run` | Execute |
| Integrations | MLflow, W&B, Seldon, BentoML |
| ZenML Cloud | Managed platform |

---

#### Lesson 03.04 — Kubeflow Pipelines
**File**: `_17_03_04_kubeflow_pipelines.md`

| Topics | Subtopics |
|---|---|
| Kubeflow overview | ML platform on Kubernetes |
| `kfp.dsl.component` | Component definition |
| `kfp.dsl.pipeline` | Pipeline composition |
| Containerized steps | Each step = Docker container |
| Input/output artifacts | `Dataset`, `Model` types |
| `kfp.compiler.Compiler` | Compile to YAML |
| `kfp.Client` | Submit and monitor |
| KFP v2 | Improved IR YAML format |

---

#### Lesson 03.05 — MLflow Projects
**File**: `_17_03_05_mlflow_projects.md`

| Topics | Subtopics |
|---|---|
| `MLproject` file | Entry points, parameters |
| Conda env | `conda.yaml` |
| Docker env | `docker_env` |
| `mlflow run` | Local and remote execution |
| Git URI | Run from remote repo |
| Databricks | `mlflow run` on Databricks cluster |
| Multi-step projects | Chain projects as pipeline |

---

#### Lesson 03.06 — Continuous Training Pipelines
**File**: `_17_03_06_continuous_training_pipelines.md`

| Topics | Subtopics |
|---|---|
| CT concept | Auto-retrain on data drift / schedule |
| Drift trigger | Data quality check → retrain |
| Schedule trigger | `cron`, Airflow schedule |
| New data trigger | S3 event → retrain pipeline |
| Shadow deployment | Train new model, evaluate before swap |
| Canary training | Gradual rollout of new model |
| Feedback loop | Production data → training data |

---

#### Lesson 03.07 — Model Testing in CI
**File**: `_17_03_07_model_testing_ci.md`

| Topics | Subtopics |
|---|---|
| Unit tests for ML | Data validation, transform tests |
| Integration tests | End-to-end pipeline test |
| Model quality gate | Accuracy, latency thresholds |
| `Great Expectations` | Data quality assertions |
| `pytest` for ML | Model inference tests |
| Behavioral testing | `CheckList`, slice performance |
| `Evidently AI` in CI | Data drift report in pipeline |

---

## MODULE 04 — Model Serving Infrastructure

**Folder**: `_17_04_model_serving_infrastructure/`  
**Lesson Count**: 7  
**Learning Order**: 4th

### Lessons

#### Lesson 04.01 — FastAPI Model Serving
**File**: `_17_04_01_fastapi_model_serving.md`

| Topics | Subtopics |
|---|---|
| FastAPI overview | Async, Pydantic, auto-docs |
| Model loading | Load once at startup, `lifespan` |
| `/predict` endpoint | Request/Response schema |
| Async inference | `async def predict` |
| Batch endpoint | List input → list output |
| Background tasks | `BackgroundTasks` |
| Health check | `/health`, `/ready` |
| Prometheus metrics | `prometheus-fastapi-instrumentator` |

---

#### Lesson 04.02 — NVIDIA Triton Inference Server
**File**: `_17_04_02_triton_inference_server.md`

| Topics | Subtopics |
|---|---|
| Triton overview | Multi-framework, multi-GPU serving |
| Model repository | Directory structure |
| Backend support | TensorRT, ONNX, TorchScript, Python |
| `config.pbtxt` | Model config file |
| Dynamic batching | `max_queue_delay_microseconds` |
| `tritonclient` | HTTP and gRPC client |
| Ensemble models | Pipeline of models in Triton |
| Perf Analyzer | Benchmarking tool |

---

#### Lesson 04.03 — Seldon Core
**File**: `_17_04_03_seldon_core.md`

| Topics | Subtopics |
|---|---|
| Seldon overview | Kubernetes-native ML serving |
| `SeldonDeployment` | CRD YAML |
| Pre-packaged servers | sklearn, XGBoost, MLflow |
| Custom Python runtime | `SeldonComponent`, `predict` method |
| Canary deployments | Traffic split by percentage |
| Explainers | Anchors, SHAP sidecar |
| `seldon-core` Python client | `microservice_api` |

---

#### Lesson 04.04 — KServe (KFServing)
**File**: `_17_04_04_kserve.md`

| Topics | Subtopics |
|---|---|
| KServe overview | Serverless ML serving on K8s |
| `InferenceService` | CRD definition |
| Pre-built runtimes | sklearn, XGBoost, PyTorch, ONNX |
| Custom runtime | `CustomPredictor` |
| Autoscaling | Knative, scale-to-zero |
| Canary rollout | `trafficPercent` |
| Transformers | Pre/post-processing sidecar |
| gRPC V2 protocol | Open Inference Protocol |

---

#### Lesson 04.05 — Containerization for ML
**File**: `_17_04_05_containerization_ml.md`

| Topics | Subtopics |
|---|---|
| Multi-stage Docker | Build → runtime layers |
| CUDA base images | `nvidia/cuda:12.1-cudnn8-runtime` |
| Model baking | Copy model into image |
| Model mounting | Persistent volume / S3 pull |
| Image optimization | Layer caching, `.dockerignore` |
| `docker buildx` | Multi-arch build |
| Container registry | ECR, GCR, DockerHub |
| Security scan | `trivy`, `snyk` |

---

#### Lesson 04.06 — Kubernetes for ML Workloads
**File**: `_17_04_06_kubernetes_ml_workloads.md`

| Topics | Subtopics |
|---|---|
| Deployments and Services | Rolling update, ClusterIP, LoadBalancer |
| GPU node scheduling | `nvidia.com/gpu: 1` resource request |
| Resource limits | CPU, memory, GPU limits |
| ConfigMaps and Secrets | External config, API keys |
| Horizontal Pod Autoscaler | `targetCPUUtilizationPercentage` |
| Helm charts | Package ML deployment |
| `kubectl` | `apply`, `logs`, `exec`, `port-forward` |
| Namespace isolation | Per-team ML namespaces |

---

#### Lesson 04.07 — A/B Testing and Canary Deployments
**File**: `_17_04_07_ab_testing_canary_deployments.md`

| Topics | Subtopics |
|---|---|
| A/B test design | Traffic split, metric collection |
| Feature flags | `LaunchDarkly`, `Unleash` for ML |
| Canary deployment | 5% → 25% → 100% rollout |
| Istio traffic management | `VirtualService`, weight |
| Nginx Ingress | Weighted canary annotation |
| Metrics collection | Per-variant accuracy, latency |
| Rollback trigger | Automatic on SLA breach |

---

## MODULE 05 — LLM and Agent Deployment

**Folder**: `_17_05_llm_and_agent_deployment/`  
**Lesson Count**: 7  
**Learning Order**: 5th

### Lessons

#### Lesson 05.01 — Production LLM Serving Architecture
**File**: `_17_05_01_production_llm_serving_architecture.md`

| Topics | Subtopics |
|---|---|
| Architecture | Load balancer → Gateway → vLLM/TGI |
| Multi-model gateway | `litellm` proxy |
| GPU fleet management | Model placement, utilization |
| SLA targets | TTFT < 500ms, TPOT < 50ms |
| Autoscaling LLM | KEDA + vLLM |
| Cost per token | Compute cost estimation |
| Fallback chains | Primary → fallback → local model |

---

#### Lesson 05.02 — vLLM Production Deployment
**File**: `_17_05_02_vllm_production_deployment.md`

| Topics | Subtopics |
|---|---|
| vLLM Docker | `vllm/vllm-openai` image |
| Multi-GPU tensor parallel | `--tensor-parallel-size` |
| Prefix caching | `--enable-prefix-caching` |
| Request queuing | `--max-num-seqs` |
| Quantized model | `--quantization awq/gptq` |
| Health endpoints | `/health`, `/v1/models` |
| Kubernetes deployment | Helm + GPU node selector |
| Prometheus + Grafana | vLLM metrics dashboard |

---

#### Lesson 05.03 — Fine-Tuned Model Deployment
**File**: `_17_05_03_fine_tuned_model_deployment.md`

| Topics | Subtopics |
|---|---|
| Merge LoRA → base | `merge_and_unload()` |
| Push to HuggingFace Hub | `model.push_to_hub()` |
| Private Hub | Private model repo |
| vLLM from Hub | `--model org/model-name` |
| TGI from Hub | Docker with `MODEL_ID` env |
| GGUF deployment | `llama.cpp` server |
| Versioning | Model registry → deployment |

---

#### Lesson 05.04 — Agent Deployment at Scale
**File**: `_17_05_04_agent_deployment_at_scale.md`

| Topics | Subtopics |
|---|---|
| LangGraph Cloud | Managed agent hosting |
| Self-hosted LangGraph | `langgraph up`, Docker |
| FastAPI + Redis | Thread state in Redis |
| Celery agent workers | Distributed async agents |
| KEDA scaling | Scale agents on queue depth |
| Multi-tenant isolation | Per-org thread isolation |
| Cost tracking | Token + tool API cost per session |

---

#### Lesson 05.05 — Embedding Service Deployment
**File**: `_17_05_05_embedding_service_deployment.md`

| Topics | Subtopics |
|---|---|
| `infinity-emb` | High-throughput embedding server |
| `sentence-transformers` server | Custom FastAPI |
| TEI (Text Embeddings Inference) | HuggingFace embedding server |
| Batch encoding throughput | Tokens/second benchmarking |
| Autoscaling embeddings | HPA on GPU utilization |
| Caching | Redis semantic cache |
| Cost | Compare API vs self-hosted |

---

#### Lesson 05.06 — Model Versioning and Blue-Green
**File**: `_17_05_06_model_versioning_blue_green.md`

| Topics | Subtopics |
|---|---|
| Blue-green deployment | Two identical environments |
| DNS / load balancer swap | Instant cutover |
| Database migration | Schema compatibility |
| Model registry → deploy | Trigger on registry stage change |
| Rollback procedure | Swap DNS back to blue |
| Testing in green | Integration tests before cutover |
| Feature flag per model | Selective traffic routing |

---

#### Lesson 05.07 — Serverless ML Deployment
**File**: `_17_05_07_serverless_ml_deployment.md`

| Topics | Subtopics |
|---|---|
| AWS Lambda + ML | Layer size limits, cold start |
| `Modal` | `@app.function`, GPU functions |
| `Replicate` | Deploy ML models as API |
| `Banana` / `Beam` | Serverless GPU inference |
| Cold start mitigation | Warm pools, provisioned concurrency |
| Pricing model | Pay-per-inference |
| Use cases | Low-traffic, burst inference |

---

## MODULE 06 — ML Monitoring and Observability

**Folder**: `_17_06_ml_monitoring_and_observability/`  
**Lesson Count**: 7  
**Learning Order**: 6th

### Lessons

#### Lesson 06.01 — ML Monitoring Fundamentals
**File**: `_17_06_01_ml_monitoring_fundamentals.md`

| Topics | Subtopics |
|---|---|
| Monitoring dimensions | Model performance, data quality, system health |
| Performance degradation | Silent failures in production |
| Feedback loop | Ground truth collection |
| Monitoring cadence | Real-time, hourly, daily |
| Alerting | PagerDuty, Slack, email |
| Dashboard | Grafana, Kibana |
| SLO / SLA | Error budget, availability |

---

#### Lesson 06.02 — Data Drift Detection
**File**: `_17_06_02_data_drift_detection.md`

| Topics | Subtopics |
|---|---|
| Covariate shift | Input distribution change |
| Label drift | Target distribution change |
| Feature drift | Individual feature statistics |
| Statistical tests | KS test, PSI, chi-squared |
| `Evidently AI` | `DatasetDriftReport`, `ColumnDriftReport` |
| `NannyML` | Confidence-based drift without labels |
| `whylogs` | Profile-based drift |
| Drift dashboard | `Evidently AI` HTML reports |

---

#### Lesson 06.03 — Model Performance Monitoring
**File**: `_17_06_03_model_performance_monitoring.md`

| Topics | Subtopics |
|---|---|
| Online metrics | Latency, throughput, error rate |
| Delayed labels | Business outcomes as labels |
| Proxy metrics | Engagement, conversion |
| `Evidently AI` classification report | Precision, recall, F1 over time |
| Regression monitoring | MAE, RMSE drift |
| Slice monitoring | Performance per segment |
| Alerting on metric drop | Threshold-based + anomaly |

---

#### Lesson 06.04 — LLM Monitoring
**File**: `_17_06_04_llm_monitoring.md`

| Topics | Subtopics |
|---|---|
| LLM-specific metrics | Latency, TTFT, TPOT, throughput |
| Quality monitoring | Faithfulness, coherence over time |
| Cost monitoring | Token spend per endpoint |
| Safety monitoring | Toxicity rate, refusal rate |
| `Langfuse` | Full LLM observability |
| `Phoenix (Arize)` | LLM traces + evals |
| Feedback loops | User thumbs up/down tracking |
| Alerting | Quality drop, cost spike |

---

#### Lesson 06.05 — Evidently AI
**File**: `_17_06_05_evidently_ai.md`

| Topics | Subtopics |
|---|---|
| `Report` | Combine multiple metrics |
| `TestSuite` | Pass/fail assertions |
| Presets | `DataQualityPreset`, `DataDriftPreset` |
| Custom metrics | `ColumnSummaryMetric` |
| `evidently.ui` | Local monitoring dashboard |
| CI integration | JSON report → GitHub annotations |
| Monitoring dashboard | Live metrics from production |

---

#### Lesson 06.06 — Prometheus and Grafana for ML
**File**: `_17_06_06_prometheus_grafana_ml.md`

| Topics | Subtopics |
|---|---|
| Prometheus scraping | `prometheus-fastapi-instrumentator` |
| Custom metrics | `prometheus_client.Counter`, `Gauge`, `Histogram` |
| `model_prediction_total` | Custom prediction counter |
| Alertmanager | `AlertingRule`, notification routing |
| Grafana dashboard | Import ML dashboards |
| `grafana-loki` | Log aggregation |
| GPU metrics | `dcgm-exporter`, GPU utilization |

---

#### Lesson 06.07 — Root Cause Analysis and Debugging
**File**: `_17_06_07_root_cause_analysis_debugging.md`

| Topics | Subtopics |
|---|---|
| Log correlation | Request ID through all services |
| Distributed tracing | `OpenTelemetry`, Jaeger |
| Error categorization | Input error, model error, infra error |
| Slice analysis | Underperforming data subgroups |
| `SHAP` in production | On-demand explanation for failures |
| Replay debugging | Re-run production inputs |
| Post-mortem template | Incident → root cause → fix |

---

## MODULE 07 — Feature Stores and Data Pipelines

**Folder**: `_17_07_feature_stores_and_data_pipelines/`  
**Lesson Count**: 7  
**Learning Order**: 7th

### Lessons

#### Lesson 07.01 — Feature Store Fundamentals
**File**: `_17_07_01_feature_store_fundamentals.md`

| Topics | Subtopics |
|---|---|
| Feature store concept | Centralized feature management |
| Online vs offline | Low-latency serving vs historical |
| Feature reuse | Avoid recomputing across teams |
| Training-serving skew | Same features in training and prod |
| Point-in-time joins | Historical features without leakage |
| Components | Registry, offline store, online store |
| Feature store tools | Feast, Hopsworks, Tecton |

---

#### Lesson 07.02 — Feast Feature Store
**File**: `_17_07_02_feast_feature_store.md`

| Topics | Subtopics |
|---|---|
| Feast concepts | Entity, Feature View, Feature Service |
| `feast init` | Project initialization |
| `FeatureStore` | `apply`, `get_historical_features` |
| Online store | Redis, DynamoDB, SQLite |
| Offline store | BigQuery, Parquet, Redshift |
| `feast materialize` | Push to online store |
| Feature retrieval | `store.get_online_features` |
| Integration | Feast + MLflow + model serving |

---

#### Lesson 07.03 — Apache Airflow for ML
**File**: `_17_07_03_apache_airflow_ml.md`

| Topics | Subtopics |
|---|---|
| Airflow DAG | `@dag`, `@task` decorators |
| Operators | `PythonOperator`, `BashOperator`, `DockerOperator` |
| Sensors | `S3KeySensor`, `HttpSensor` |
| XComs | Task-to-task data passing |
| Connections | Airflow connections for external services |
| `KubernetesPodOperator` | Run in K8s pod |
| `mlflow` in Airflow | Log training runs from DAG |
| Schedule | `schedule="@daily"` cron |

---

#### Lesson 07.04 — Prefect for ML Pipelines
**File**: `_17_07_04_prefect_ml_pipelines.md`

| Topics | Subtopics |
|---|---|
| Prefect concepts | Flow, Task, Deployment |
| `@flow` decorator | Top-level pipeline |
| `@task` decorator | Individual step |
| `prefect.deploy` | Create deployment |
| Prefect Cloud | Managed scheduling + monitoring |
| Concurrency | `task_runner=ConcurrentTaskRunner` |
| Retries | `@task(retries=3)` |
| Artifacts | `create_markdown_artifact` |

---

#### Lesson 07.05 — Data Validation with Great Expectations
**File**: `_17_07_05_data_validation_great_expectations.md`

| Topics | Subtopics |
|---|---|
| GE concepts | Expectation Suite, Checkpoint |
| `expect_column_to_exist` | Schema check |
| `expect_column_values_to_not_be_null` | Null check |
| `expect_column_mean_to_be_between` | Statistical check |
| `DataContext` | GE project |
| Data Docs | HTML quality report |
| CI integration | GE checkpoint in pipeline |
| `great_expectations` + Airflow | `GreatExpectationsOperator` |

---

#### Lesson 07.06 — Streaming Data Pipelines for ML
**File**: `_17_07_06_streaming_data_pipelines_ml.md`

| Topics | Subtopics |
|---|---|
| Kafka for ML | Produce predictions → Kafka topic |
| `confluent-kafka-python` | Producer and consumer |
| Flink for feature engineering | Real-time aggregation |
| `kafka-python` | Simple producer/consumer |
| Online feature computation | Real-time feature from events |
| Prediction logging | Structured events to Kafka |
| Data lake ingestion | Kafka → S3 via Kafka Connect |

---

#### Lesson 07.07 — Data Lake and Lakehouse for ML
**File**: `_17_07_07_data_lake_lakehouse_ml.md`

| Topics | Subtopics |
|---|---|
| Data Lake architecture | Raw → processed → curated zones |
| Delta Lake | ACID transactions on Parquet |
| Apache Iceberg | Table format, time travel |
| `deltalake` Python | `DeltaTable`, `write_deltalake` |
| Training data versioning | Snapshot-based dataset version |
| Feature materialization | Scheduled batch → feature store |
| Databricks Lakehouse | Unity Catalog, Delta Live Tables |

---

## MODULE 08 — MLOps Platforms

**Folder**: `_17_08_mlops_platforms/`  
**Lesson Count**: 5  
**Learning Order**: 8th

### Lessons

#### Lesson 08.01 — SageMaker MLOps
**File**: `_17_08_01_sagemaker_mlops.md`

| Topics | Subtopics |
|---|---|
| SageMaker Training | `Estimator`, `fit()` |
| SageMaker Pipelines | `Pipeline`, `TrainingStep` |
| SageMaker Model Registry | `ModelPackageGroup` |
| SageMaker Endpoints | `deploy()`, multi-model |
| SageMaker Monitoring | `ModelMonitor`, `DataCaptureConfig` |
| SageMaker Feature Store | `FeatureGroup` |
| SageMaker Clarify | Bias detection, explainability |

---

#### Lesson 08.02 — Vertex AI MLOps
**File**: `_17_08_02_vertex_ai_mlops.md`

| Topics | Subtopics |
|---|---|
| Vertex AI Pipelines | `kfp.v2.dsl`, compiled YAML |
| Vertex AI Training | `CustomJob`, `HyperparameterTuningJob` |
| Model Registry | `aiplatform.Model.upload` |
| Vertex AI Endpoints | `model.deploy()` |
| Vertex AI Feature Store | Online serving |
| Vertex AI Monitoring | `ModelDeploymentMonitoringJob` |
| `google-cloud-aiplatform` | Python SDK |

---

#### Lesson 08.03 — Azure ML
**File**: `_17_08_03_azure_ml.md`

| Topics | Subtopics |
|---|---|
| Azure ML Workspace | Resources, compute clusters |
| Azure ML Pipelines | `@pipeline`, `@command_component` |
| Azure ML Registry | `model.register` |
| Online endpoints | `ManagedOnlineEndpoint` |
| Azure ML Monitoring | Data drift monitor |
| `azure-ai-ml` SDK v2 | Python SDK |
| Compute targets | `AmlCompute`, `ComputeInstance` |

---

#### Lesson 08.04 — Databricks ML
**File**: `_17_08_04_databricks_ml.md`

| Topics | Subtopics |
|---|---|
| Databricks MLflow | Managed MLflow |
| Unity Catalog models | Governed model registry |
| Feature Engineering | `FeatureEngineeringClient` |
| Model Serving | Databricks Model Serving endpoints |
| AutoML | `databricks.automl.classify` |
| Delta Live Tables | Streaming + batch pipelines |
| Databricks Jobs | Scheduled ML workflows |

---

#### Lesson 08.05 — Cost Optimization and Governance
**File**: `_17_08_05_cost_optimization_governance.md`

| Topics | Subtopics |
|---|---|
| GPU cost tracking | Per-job cost tagging |
| Spot / preemptible instances | 60-90% cost savings |
| Model compression | Quantization → smaller compute |
| Inference caching | Reduce duplicate calls |
| FinOps for ML | Showback, chargeback |
| Governance | Model lineage, audit trail |
| Compliance | GDPR, HIPAA, SOC2 considerations |
| Resource quotas | Namespace quotas in K8s |

---

## MODULE 09 — Industry Projects

**Folder**: `_17_09_industry_projects/`  
**Lesson Count**: 6  
**Learning Order**: 9th (Capstone)

### Lessons

#### Lesson 09.01 — End-to-End ML Pipeline (Tabular)
**File**: `_17_09_01_end_to_end_ml_pipeline_tabular.md`

| Topics | Subtopics |
|---|---|
| Dataset | Credit scoring (tabular) |
| Pipeline | DVC + ZenML + MLflow |
| Steps | Ingest → validate → feature → train → eval |
| CI/CD | GitHub Actions + model gate |
| Serving | FastAPI + Docker |
| Monitoring | Evidently drift + Grafana |
| Registry | MLflow Model Registry |

---

#### Lesson 09.02 — LLM Fine-Tuning MLOps Pipeline
**File**: `_17_09_02_llm_finetuning_mlops_pipeline.md`

| Topics | Subtopics |
|---|---|
| Pipeline | DVC data → QLoRA train → eval → register |
| Tracking | W&B + MLflow |
| CI gate | MMLU / task eval threshold |
| Serving | vLLM + LiteLLM proxy |
| Monitoring | Langfuse + token cost |
| Registry | MLflow + HF Hub |
| Rollback | Blue-green LLM swap |

---

#### Lesson 09.03 — RAG System MLOps
**File**: `_17_09_03_rag_system_mlops.md`

| Topics | Subtopics |
|---|---|
| Pipeline | Ingest → embed → index → serve |
| Orchestration | Prefect scheduled re-index |
| Embedding versioning | Model version → re-embed trigger |
| CI/CD | RAGAS gate in pipeline |
| Monitoring | Langfuse traces + drift on queries |
| Vector DB | Qdrant managed |
| A/B testing | Chunk size experiment |

---

#### Lesson 09.04 — Real-Time Prediction Service
**File**: `_17_09_04_real_time_prediction_service.md`

| Topics | Subtopics |
|---|---|
| Use case | Real-time fraud detection |
| Feature store | Feast online features |
| Serving | TorchServe + FastAPI |
| Latency | P99 < 50ms SLA |
| Monitoring | NannyML + Prometheus |
| Scaling | HPA on request rate |
| Canary | 10% → 50% → 100% |

---

#### Lesson 09.05 — Multi-Model Serving Platform
**File**: `_17_09_05_multi_model_serving_platform.md`

| Topics | Subtopics |
|---|---|
| Architecture | Triton + model registry + gateway |
| Models | Classification + NLP + CV ensembled |
| Routing | Request type → model selection |
| Auto-load | Registry event → Triton load |
| Monitoring | Per-model Grafana metrics |
| Cost | GPU utilization per model |
| Helm | Unified Helm chart for platform |

---

#### Lesson 09.06 — Full-Stack AI System (Grand Capstone)
**File**: `_17_09_06_full_stack_ai_system_grand_capstone.md`

| Topics | Subtopics |
|---|---|
| System | End-to-end: data → ML → LLM → Agent → RAG |
| Components | Feature store + Model registry + LLM serving + Agent + RAG |
| CI/CD | Full pipeline: train → eval → deploy |
| Monitoring | ML + LLM + Agent observability |
| Security | Guardrails + audit + compliance |
| Platform | Kubernetes + Helm + Grafana + Langfuse |
| Evaluation | Automated benchmark suite |
| Documentation | Model cards + architecture diagram |

---

## Full Folder Structure

```
docs/curriculum/_17_mlops_ai_deployment/
│
├── _17_01_experiment_tracking/
│   ├── _17_01_01_mlflow_fundamentals.md
│   ├── _17_01_02_mlflow_advanced_features.md
│   ├── _17_01_03_weights_and_biases.md
│   ├── _17_01_04_dvc_data_version_control.md
│   ├── _17_01_05_experiment_design_hparam_tuning.md
│   ├── _17_01_06_reproducibility_experiment_management.md
│   └── _17_01_07_comparing_selecting_models.md
│
├── _17_02_model_packaging_and_registry/
│   ├── _17_02_01_mlflow_model_logging_flavors.md
│   ├── _17_02_02_mlflow_model_registry.md
│   ├── _17_02_03_onnx_model_export.md
│   ├── _17_02_04_torchscript_torchserve.md
│   ├── _17_02_05_bentoml.md
│   └── _17_02_06_model_cards_documentation.md
│
├── _17_03_ml_cicd_pipelines/
│   ├── _17_03_01_ml_pipeline_fundamentals.md
│   ├── _17_03_02_github_actions_ml.md
│   ├── _17_03_03_zenml.md
│   ├── _17_03_04_kubeflow_pipelines.md
│   ├── _17_03_05_mlflow_projects.md
│   ├── _17_03_06_continuous_training_pipelines.md
│   └── _17_03_07_model_testing_ci.md
│
├── _17_04_model_serving_infrastructure/
│   ├── _17_04_01_fastapi_model_serving.md
│   ├── _17_04_02_triton_inference_server.md
│   ├── _17_04_03_seldon_core.md
│   ├── _17_04_04_kserve.md
│   ├── _17_04_05_containerization_ml.md
│   ├── _17_04_06_kubernetes_ml_workloads.md
│   └── _17_04_07_ab_testing_canary_deployments.md
│
├── _17_05_llm_and_agent_deployment/
│   ├── _17_05_01_production_llm_serving_architecture.md
│   ├── _17_05_02_vllm_production_deployment.md
│   ├── _17_05_03_fine_tuned_model_deployment.md
│   ├── _17_05_04_agent_deployment_at_scale.md
│   ├── _17_05_05_embedding_service_deployment.md
│   ├── _17_05_06_model_versioning_blue_green.md
│   └── _17_05_07_serverless_ml_deployment.md
│
├── _17_06_ml_monitoring_and_observability/
│   ├── _17_06_01_ml_monitoring_fundamentals.md
│   ├── _17_06_02_data_drift_detection.md
│   ├── _17_06_03_model_performance_monitoring.md
│   ├── _17_06_04_llm_monitoring.md
│   ├── _17_06_05_evidently_ai.md
│   ├── _17_06_06_prometheus_grafana_ml.md
│   └── _17_06_07_root_cause_analysis_debugging.md
│
├── _17_07_feature_stores_and_data_pipelines/
│   ├── _17_07_01_feature_store_fundamentals.md
│   ├── _17_07_02_feast_feature_store.md
│   ├── _17_07_03_apache_airflow_ml.md
│   ├── _17_07_04_prefect_ml_pipelines.md
│   ├── _17_07_05_data_validation_great_expectations.md
│   ├── _17_07_06_streaming_data_pipelines_ml.md
│   └── _17_07_07_data_lake_lakehouse_ml.md
│
├── _17_08_mlops_platforms/
│   ├── _17_08_01_sagemaker_mlops.md
│   ├── _17_08_02_vertex_ai_mlops.md
│   ├── _17_08_03_azure_ml.md
│   ├── _17_08_04_databricks_ml.md
│   └── _17_08_05_cost_optimization_governance.md
│
└── _17_09_industry_projects/
    ├── _17_09_01_end_to_end_ml_pipeline_tabular.md
    ├── _17_09_02_llm_finetuning_mlops_pipeline.md
    ├── _17_09_03_rag_system_mlops.md
    ├── _17_09_04_real_time_prediction_service.md
    ├── _17_09_05_multi_model_serving_platform.md
    └── _17_09_06_full_stack_ai_system_grand_capstone.md
```

---

## Learning Order

```
01 Experiment Tracking  (MLflow → W&B → DVC → HPO → Reproducibility)
    ↓
02 Model Packaging & Registry  (Flavors → Registry → ONNX → BentoML)
    ↓
03 ML CI/CD Pipelines  (Fundamentals → GHA → ZenML → Kubeflow → CT)
    ↓
04 Model Serving Infrastructure  (FastAPI → Triton → Seldon → K8s → A/B)
    ↓
05 LLM & Agent Deployment  (vLLM prod → Fine-tuned → Agents → Embeddings)
    ↓
06 ML Monitoring & Observability  (Drift → Perf → LLM → Evidently → Grafana)
    ↓
07 Feature Stores & Data Pipelines  (Feast → Airflow → Prefect → Streaming)
    ↓
08 MLOps Platforms  (SageMaker → Vertex → Azure → Databricks → FinOps)
    ↓
09 Industry Projects (Grand Capstone)
```

---

## Summary Statistics

| Module | Title | Lessons |
|---|---|---|
| 01 | Experiment Tracking | 7 |
| 02 | Model Packaging & Registry | 6 |
| 03 | ML CI/CD Pipelines | 7 |
| 04 | Model Serving Infrastructure | 7 |
| 05 | LLM & Agent Deployment | 7 |
| 06 | ML Monitoring & Observability | 7 |
| 07 | Feature Stores & Data Pipelines | 7 |
| 08 | MLOps Platforms | 5 |
| 09 | Industry Projects | 6 |
| **TOTAL** | | **59 lessons** |

---

## 🎓 Complete AI Curriculum — All 8 Phases

| Phase | Domain | Lessons |
|---|---|---|
| 1 | Machine Learning | 107 |
| 2 | Deep Learning | 95 |
| 3 | Computer Vision | 72 |
| 4 | NLP | 72 |
| 5 | Generative AI & LLMs | 71 |
| 6 | RAG Engineering | 59 |
| 7 | AI Agents | 58 |
| 8 | MLOps & AI Deployment | 59 |
| **GRAND TOTAL** | | **593 lessons** |

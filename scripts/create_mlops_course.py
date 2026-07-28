import os
BASE = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum\_17_mlops_ai_deployment'
LESSONS = [
    ("_17_01_experiment_tracking","_17_01_01_mlflow_fundamentals.md",1,1,"MLflow Fundamentals","Experiment Tracking",["mlflow-tracking","start-run","log-param","log-metric","log-artifact","mlflow-ui","autolog"],"intermediate"),
    ("_17_01_experiment_tracking","_17_01_02_mlflow_advanced_features.md",1,2,"MLflow Advanced Features","Experiment Tracking",["nested-runs","log-dict","log-figure","log-table","search-runs","remote-tracking","mlflow-evaluate"],"intermediate"),
    ("_17_01_experiment_tracking","_17_01_03_weights_and_biases.md",1,3,"Weights and Biases","Experiment Tracking",["wandb-init","wandb-log","wandb-artifact","wandb-table","sweeps","wandb-reports","wandb-alert"],"intermediate"),
    ("_17_01_experiment_tracking","_17_01_04_dvc_data_version_control.md",1,4,"DVC Data Version Control","Experiment Tracking",["dvc-init","dvc-add","dvc-push","dvc-pull","dvc-run","dvc-repro","dvc-metrics"],"intermediate"),
    ("_17_01_experiment_tracking","_17_01_05_experiment_design_hparam_tuning.md",1,5,"Experiment Design and Hyperparameter Tuning","Experiment Tracking",["grid-search","random-search","optuna","hyperband","ray-tune","wandb-sweeps","hpo"],"intermediate"),
    ("_17_01_experiment_tracking","_17_01_06_reproducibility_experiment_management.md",1,6,"Reproducibility and Experiment Management","Experiment Tracking",["seed-control","conda-env","docker-repro","mlflow-projects","git-hash","deterministic"],"intermediate"),
    ("_17_01_experiment_tracking","_17_01_07_comparing_selecting_models.md",1,7,"Comparing and Selecting Models","Experiment Tracking",["multi-metric","pareto-frontier","statistical-significance","mlflow-compare","champion-challenger"],"intermediate"),
    ("_17_02_model_packaging_and_registry","_17_02_01_mlflow_model_logging_flavors.md",2,1,"MLflow Model Logging and Flavors","Model Packaging",["sklearn-flavor","pytorch-flavor","pyfunc","transformers-flavor","signature","input-example"],"intermediate"),
    ("_17_02_model_packaging_and_registry","_17_02_02_mlflow_model_registry.md",2,2,"MLflow Model Registry","Model Packaging",["register-model","model-versions","staging-production","model-alias","webhooks","registry-ui","lineage"],"intermediate"),
    ("_17_02_model_packaging_and_registry","_17_02_03_onnx_model_export.md",2,3,"ONNX Model Export","Model Packaging",["onnx","torch-onnx-export","onnxruntime","opset","optimum","onnx-checker"],"intermediate"),
    ("_17_02_model_packaging_and_registry","_17_02_04_torchscript_torchserve.md",2,4,"TorchScript and TorchServe","Model Packaging",["torchscript","jit-script","jit-trace","torchserve","mar-package","handler","prometheus-torchserve"],"intermediate"),
    ("_17_02_model_packaging_and_registry","_17_02_05_bentoml.md",2,5,"BentoML","Model Packaging",["bentoml-service","runner","bento-build","bentoml-containerize","bentocloud","adaptive-batching"],"intermediate"),
    ("_17_02_model_packaging_and_registry","_17_02_06_model_cards_documentation.md",2,6,"Model Cards and Documentation","Model Packaging",["model-card","hf-model-card","eval-results","bias-section","license","dataset-cards","model-card-toolkit"],"intermediate"),
    ("_17_03_ml_cicd_pipelines","_17_03_01_ml_pipeline_fundamentals.md",3,1,"ML Pipeline Fundamentals","ML CI/CD",["dag-pipeline","parameterization","caching","artifacts","orchestration-tools","airflow","zenml"],"intermediate"),
    ("_17_03_ml_cicd_pipelines","_17_03_02_github_actions_ml.md",3,2,"GitHub Actions for ML","ML CI/CD",["ml-ci-workflow","dvc-pull","cml","model-validation-gate","gpu-runner","mlflow-logging"],"intermediate"),
    ("_17_03_ml_cicd_pipelines","_17_03_03_zenml.md",3,3,"ZenML","ML CI/CD",["zenml-pipeline","step-decorator","pipeline-decorator","zenml-stack","zenml-integrations","zenml-cloud"],"intermediate"),
    ("_17_03_ml_cicd_pipelines","_17_03_04_kubeflow_pipelines.md",3,4,"Kubeflow Pipelines","ML CI/CD",["kfp-component","kfp-pipeline","containerized-steps","kfp-compiler","kfp-client","kfp-v2"],"advanced"),
    ("_17_03_ml_cicd_pipelines","_17_03_05_mlflow_projects.md",3,5,"MLflow Projects","ML CI/CD",["mlproject","entry-points","conda-yaml","docker-env","mlflow-run","multi-step-project"],"intermediate"),
    ("_17_03_ml_cicd_pipelines","_17_03_06_continuous_training_pipelines.md",3,6,"Continuous Training Pipelines","ML CI/CD",["ct-concept","drift-trigger","schedule-trigger","s3-event","shadow-deployment","canary-training","feedback-loop"],"advanced"),
    ("_17_03_ml_cicd_pipelines","_17_03_07_model_testing_ci.md",3,7,"Model Testing in CI","ML CI/CD",["unit-tests-ml","integration-tests","quality-gate","great-expectations","pytest-ml","checklist","evidently-ci"],"intermediate"),
    ("_17_04_model_serving_infrastructure","_17_04_01_fastapi_model_serving.md",4,1,"FastAPI Model Serving","Model Serving",["fastapi","lifespan","predict-endpoint","async-inference","batch-endpoint","health-check","prometheus"],"intermediate"),
    ("_17_04_model_serving_infrastructure","_17_04_02_triton_inference_server.md",4,2,"Triton Inference Server","Model Serving",["triton","model-repository","config-pbtxt","dynamic-batching","tritonclient","ensemble","perf-analyzer"],"advanced"),
    ("_17_04_model_serving_infrastructure","_17_04_03_seldon_core.md",4,3,"Seldon Core","Model Serving",["seldon-deployment","crd-yaml","pre-packaged","custom-python","canary","explainers","seldon-client"],"advanced"),
    ("_17_04_model_serving_infrastructure","_17_04_04_kserve.md",4,4,"KServe","Model Serving",["inference-service","custom-predictor","autoscaling","knative","scale-to-zero","transformer","grpc-v2"],"advanced"),
    ("_17_04_model_serving_infrastructure","_17_04_05_containerization_ml.md",4,5,"Containerization for ML","Model Serving",["multi-stage-docker","cuda-base","model-baking","model-mounting","buildx","ecr","trivy"],"intermediate"),
    ("_17_04_model_serving_infrastructure","_17_04_06_kubernetes_ml_workloads.md",4,6,"Kubernetes for ML Workloads","Model Serving",["deployments","gpu-scheduling","resource-limits","hpa","helm-charts","kubectl","namespace"],"intermediate"),
    ("_17_04_model_serving_infrastructure","_17_04_07_ab_testing_canary_deployments.md",4,7,"A/B Testing and Canary Deployments","Model Serving",["ab-design","feature-flags","canary","istio","nginx-ingress","per-variant","rollback"],"intermediate"),
    ("_17_05_llm_and_agent_deployment","_17_05_01_production_llm_serving_architecture.md",5,1,"Production LLM Serving Architecture","LLM Deployment",["load-balancer","litellm-proxy","gpu-fleet","sla-targets","autoscaling","cost-per-token","fallback-chains"],"advanced"),
    ("_17_05_llm_and_agent_deployment","_17_05_02_vllm_production_deployment.md",5,2,"vLLM Production Deployment","LLM Deployment",["vllm-docker","tensor-parallel","prefix-caching","max-num-seqs","quantized","health-endpoint","k8s-vllm"],"advanced"),
    ("_17_05_llm_and_agent_deployment","_17_05_03_fine_tuned_model_deployment.md",5,3,"Fine-Tuned Model Deployment","LLM Deployment",["merge-lora","push-to-hub","private-hub","vllm-hub","tgi-hub","gguf-deploy","model-versioning"],"intermediate"),
    ("_17_05_llm_and_agent_deployment","_17_05_04_agent_deployment_at_scale.md",5,4,"Agent Deployment at Scale","LLM Deployment",["langgraph-cloud","self-hosted","redis-thread","celery-agents","keda","multi-tenant","cost-tracking"],"advanced"),
    ("_17_05_llm_and_agent_deployment","_17_05_05_embedding_service_deployment.md",5,5,"Embedding Service Deployment","LLM Deployment",["infinity-emb","tei","batch-encoding","hpa-gpu","semantic-cache","self-hosted-cost"],"intermediate"),
    ("_17_05_llm_and_agent_deployment","_17_05_06_model_versioning_blue_green.md",5,6,"Model Versioning and Blue-Green","LLM Deployment",["blue-green","dns-swap","schema-compat","registry-trigger","rollback","feature-flag-model"],"intermediate"),
    ("_17_05_llm_and_agent_deployment","_17_05_07_serverless_ml_deployment.md",5,7,"Serverless ML Deployment","LLM Deployment",["lambda-ml","modal","replicate","banana","cold-start","warm-pools","pay-per-inference"],"intermediate"),
    ("_17_06_ml_monitoring_and_observability","_17_06_01_ml_monitoring_fundamentals.md",6,1,"ML Monitoring Fundamentals","ML Monitoring",["monitoring-dimensions","performance-degradation","feedback-loop","alerting","dashboard","slo-sla"],"intermediate"),
    ("_17_06_ml_monitoring_and_observability","_17_06_02_data_drift_detection.md",6,2,"Data Drift Detection","ML Monitoring",["covariate-shift","label-drift","ks-test","psi","evidently","nannyml","whylogs"],"intermediate"),
    ("_17_06_ml_monitoring_and_observability","_17_06_03_model_performance_monitoring.md",6,3,"Model Performance Monitoring","ML Monitoring",["online-metrics","delayed-labels","proxy-metrics","evidently-report","slice-monitoring","alerting"],"intermediate"),
    ("_17_06_ml_monitoring_and_observability","_17_06_04_llm_monitoring.md",6,4,"LLM Monitoring","ML Monitoring",["ttft","tpot","quality-monitoring","cost-monitoring","safety-monitoring","langfuse","phoenix"],"intermediate"),
    ("_17_06_ml_monitoring_and_observability","_17_06_05_evidently_ai.md",6,5,"Evidently AI","ML Monitoring",["report","test-suite","presets","custom-metrics","evidently-ui","ci-integration","monitoring-dashboard"],"intermediate"),
    ("_17_06_ml_monitoring_and_observability","_17_06_06_prometheus_grafana_ml.md",6,6,"Prometheus and Grafana for ML","ML Monitoring",["prometheus-scrape","custom-metrics","alertmanager","grafana-dashboard","loki","dcgm-exporter"],"intermediate"),
    ("_17_06_ml_monitoring_and_observability","_17_06_07_root_cause_analysis_debugging.md",6,7,"Root Cause Analysis and Debugging","ML Monitoring",["log-correlation","opentelemetry","jaeger","error-categorization","shap-production","replay","post-mortem"],"advanced"),
    ("_17_07_feature_stores_and_data_pipelines","_17_07_01_feature_store_fundamentals.md",7,1,"Feature Store Fundamentals","Feature Stores",["feature-store","online-offline","feature-reuse","training-serving-skew","point-in-time","feast","hopsworks"],"intermediate"),
    ("_17_07_feature_stores_and_data_pipelines","_17_07_02_feast_feature_store.md",7,2,"Feast Feature Store","Feature Stores",["feast","entity","feature-view","feature-service","feast-materialize","online-features","feast-mlflow"],"intermediate"),
    ("_17_07_feature_stores_and_data_pipelines","_17_07_03_apache_airflow_ml.md",7,3,"Apache Airflow for ML","Feature Stores",["airflow-dag","python-operator","sensor","xcoms","connections","kubernetes-pod-op","mlflow-airflow"],"intermediate"),
    ("_17_07_feature_stores_and_data_pipelines","_17_07_04_prefect_ml_pipelines.md",7,4,"Prefect for ML Pipelines","Feature Stores",["prefect-flow","task-decorator","prefect-deploy","prefect-cloud","concurrent-runner","retries","artifacts"],"intermediate"),
    ("_17_07_feature_stores_and_data_pipelines","_17_07_05_data_validation_great_expectations.md",7,5,"Data Validation with Great Expectations","Feature Stores",["expectation-suite","checkpoint","data-docs","ge-airflow","column-exists","null-check","statistical-check"],"intermediate"),
    ("_17_07_feature_stores_and_data_pipelines","_17_07_06_streaming_data_pipelines_ml.md",7,6,"Streaming Data Pipelines for ML","Feature Stores",["kafka","confluent-kafka","flink","online-feature","prediction-logging","kafka-connect","s3-ingestion"],"advanced"),
    ("_17_07_feature_stores_and_data_pipelines","_17_07_07_data_lake_lakehouse_ml.md",7,7,"Data Lake and Lakehouse for ML","Feature Stores",["delta-lake","apache-iceberg","deltalake-python","training-data-version","feature-materialization","databricks"],"advanced"),
    ("_17_08_mlops_platforms","_17_08_01_sagemaker_mlops.md",8,1,"SageMaker MLOps","MLOps Platforms",["sagemaker-training","sagemaker-pipelines","model-registry","sagemaker-endpoints","model-monitor","feature-store","clarify"],"advanced"),
    ("_17_08_mlops_platforms","_17_08_02_vertex_ai_mlops.md",8,2,"Vertex AI MLOps","MLOps Platforms",["vertex-pipelines","custom-job","model-registry","vertex-endpoints","vertex-feature-store","monitoring-job","aiplatform-sdk"],"advanced"),
    ("_17_08_mlops_platforms","_17_08_03_azure_ml.md",8,3,"Azure ML","MLOps Platforms",["azure-workspace","azure-pipelines","command-component","managed-endpoint","azure-monitoring","azure-ai-ml"],"advanced"),
    ("_17_08_mlops_platforms","_17_08_04_databricks_ml.md",8,4,"Databricks ML","MLOps Platforms",["databricks-mlflow","unity-catalog","feature-engineering","model-serving","automl","delta-live-tables","databricks-jobs"],"advanced"),
    ("_17_08_mlops_platforms","_17_08_05_cost_optimization_governance.md",8,5,"Cost Optimization and Governance","MLOps Platforms",["gpu-cost","spot-instances","model-compression","inference-caching","finops","governance","compliance"],"advanced"),
    ("_17_09_industry_projects","_17_09_01_end_to_end_ml_pipeline_tabular.md",9,1,"End-to-End ML Pipeline Tabular","Industry Projects",["dvc","zenml","mlflow","fastapi","docker","evidently","model-registry","credit-scoring"],"advanced"),
    ("_17_09_industry_projects","_17_09_02_llm_finetuning_mlops_pipeline.md",9,2,"LLM Fine-Tuning MLOps Pipeline","Industry Projects",["qlora","wandb","mlflow","vllm","litellm","langfuse","blue-green-llm"],"advanced"),
    ("_17_09_industry_projects","_17_09_03_rag_system_mlops.md",9,3,"RAG System MLOps","Industry Projects",["prefect","re-index","embedding-version","ragas-gate","langfuse","qdrant","ab-chunk"],"advanced"),
    ("_17_09_industry_projects","_17_09_04_real_time_prediction_service.md",9,4,"Real-Time Prediction Service","Industry Projects",["feast","torchserve","fastapi","nannyml","prometheus","hpa","canary"],"advanced"),
    ("_17_09_industry_projects","_17_09_05_multi_model_serving_platform.md",9,5,"Multi-Model Serving Platform","Industry Projects",["triton","model-registry","api-gateway","auto-load","grafana","cost-per-model","helm"],"advanced"),
    ("_17_09_industry_projects","_17_09_06_full_stack_ai_system_grand_capstone.md",9,6,"Full-Stack AI System Grand Capstone","Industry Projects",["feature-store","model-registry","vllm","langgraph","rag","kubernetes","grafana","langfuse","guardrails"],"advanced"),
]
created = 0
skipped = 0
for folder, fname, mod, les, title, mod_title, tags, diff in LESSONS:
    dirpath = os.path.join(BASE, folder)
    os.makedirs(dirpath, exist_ok=True)
    fpath = os.path.join(dirpath, fname)
    if not os.path.exists(fpath):
        lid = f"17_{mod:02d}_{les:02d}"
        tag_str = ", ".join('"'+t+'"' for t in tags)
        content = f'---\nid: "{lid}"\ntitle: "{title}"\ncourse: "MLOps and AI Deployment"\nmodule: {mod}\nmodule_title: "{mod_title}"\nlesson: {les}\nversion: "2.0"\ndifficulty: "{diff}"\nduration_minutes: 60\ntags: [{tag_str}]\nprerequisites: []\nlab_required: true\n---\n\n# {title}\n\n> **Status**: Syllabus stub. Full lesson content to be authored.\n\n---\n\n## Topics Covered\n\n*(See Phase 8 MLOps Syllabus for full topic and subtopic breakdown)*\n\n---\n\n## Learning Objectives\n\n- To be defined during content authoring.\n'
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[CREATE] {fname}")
        created += 1
    else:
        print(f"[SKIP]   {fname}")
        skipped += 1
print(f"\nDONE - Created: {created}  Skipped: {skipped}  Total: {created+skipped}")

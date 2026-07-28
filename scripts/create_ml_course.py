import os

BASE = r'd:\My Drive\all files\PROJECT FILES\notes\docs\curriculum\_10_machine_learning'

LESSONS = [
    ("_10_01_foundations","_10_01_01_what_is_machine_learning.md",1,1,"What is Machine Learning?","Foundations",["ml-types","supervised","unsupervised"],"beginner"),
    ("_10_01_foundations","_10_01_02_scikit_learn_ecosystem.md",1,2,"The Scikit-Learn Ecosystem","Foundations",["scikit-learn","estimator-api"],"beginner"),
    ("_10_01_foundations","_10_01_03_data_splitting_and_leakage.md",1,3,"Data Splitting and Leakage","Foundations",["train-test-split","cross-validation","data-leakage"],"beginner"),
    ("_10_01_foundations","_10_01_04_bias_variance_tradeoff.md",1,4,"The Bias-Variance Tradeoff","Foundations",["bias","variance","overfitting"],"intermediate"),
    ("_10_01_foundations","_10_01_05_no_free_lunch_theorem.md",1,5,"The No Free Lunch Theorem","Foundations",["nfl-theorem","model-selection"],"intermediate"),
    ("_10_01_foundations","_10_01_06_ml_environment_setup.md",1,6,"ML Environment Setup","Foundations",["conda","jupyter","gpu","cuda"],"beginner"),
    ("_10_02_mathematics_for_ml","_10_02_01_information_theory_for_ml.md",2,1,"Information Theory for ML","Mathematics for ML",["entropy","cross-entropy","kl-divergence"],"intermediate"),
    ("_10_02_mathematics_for_ml","_10_02_02_optimization_theory_for_ml.md",2,2,"Optimization Theory for ML","Mathematics for ML",["gradient-descent","sgd","adam"],"intermediate"),
    ("_10_02_mathematics_for_ml","_10_02_03_linear_algebra_applied_ml.md",2,3,"Linear Algebra Applied in ML","Mathematics for ML",["pca","svd","kernel-trick"],"intermediate"),
    ("_10_02_mathematics_for_ml","_10_02_04_probabilistic_foundations_ml.md",2,4,"Probabilistic Foundations for ML","Mathematics for ML",["mle","map","bayesian"],"intermediate"),
    ("_10_03_data_preparation","_10_03_01_exploratory_data_analysis.md",3,1,"Exploratory Data Analysis","Data Preparation",["eda","univariate","bivariate"],"intermediate"),
    ("_10_03_data_preparation","_10_03_02_handling_missing_values.md",3,2,"Handling Missing Values","Data Preparation",["imputation","mcar","mice"],"intermediate"),
    ("_10_03_data_preparation","_10_03_03_handling_outliers.md",3,3,"Handling Outliers","Data Preparation",["outliers","z-score","isolation-forest"],"intermediate"),
    ("_10_03_data_preparation","_10_03_04_data_encoding.md",3,4,"Data Encoding","Data Preparation",["one-hot","ordinal","target-encoding"],"intermediate"),
    ("_10_03_data_preparation","_10_03_05_data_scaling_normalization.md",3,5,"Data Scaling and Normalization","Data Preparation",["standard-scaler","minmax","robust-scaler"],"intermediate"),
    ("_10_03_data_preparation","_10_03_06_handling_class_imbalance.md",3,6,"Handling Class Imbalance","Data Preparation",["smote","adasyn","undersampling"],"intermediate"),
    ("_10_03_data_preparation","_10_03_07_data_splitting_strategies.md",3,7,"Data Splitting Strategies","Data Preparation",["stratified","group-kfold","time-series-split"],"intermediate"),
    ("_10_04_feature_engineering","_10_04_01_feature_creation_transformation.md",4,1,"Feature Creation and Transformation","Feature Engineering",["feature-creation","log-transform","binning"],"intermediate"),
    ("_10_04_feature_engineering","_10_04_02_feature_selection_filter.md",4,2,"Feature Selection: Filter Methods","Feature Engineering",["variance-threshold","selectkbest","chi2"],"intermediate"),
    ("_10_04_feature_engineering","_10_04_03_feature_selection_wrapper.md",4,3,"Feature Selection: Wrapper Methods","Feature Engineering",["rfe","rfecv","forward-selection"],"intermediate"),
    ("_10_04_feature_engineering","_10_04_04_feature_selection_embedded.md",4,4,"Feature Selection: Embedded Methods","Feature Engineering",["lasso","select-from-model","permutation-importance"],"intermediate"),
    ("_10_04_feature_engineering","_10_04_05_dimensionality_reduction_unsupervised.md",4,5,"Dimensionality Reduction","Feature Engineering",["pca","tsne","umap","truncated-svd"],"intermediate"),
    ("_10_04_feature_engineering","_10_04_06_feature_engineering_time_series.md",4,6,"Feature Engineering for Time Series","Feature Engineering",["lag-features","rolling-statistics","tsfresh"],"intermediate"),
    ("_10_04_feature_engineering","_10_04_07_sklearn_pipelines_columntransformer.md",4,7,"Sklearn Pipelines and ColumnTransformer","Feature Engineering",["pipeline","column-transformer","joblib"],"intermediate"),
    ("_10_05_model_evaluation","_10_05_01_regression_metrics.md",5,1,"Regression Metrics","Model Evaluation",["mae","rmse","r-squared","mape"],"intermediate"),
    ("_10_05_model_evaluation","_10_05_02_classification_metrics.md",5,2,"Classification Metrics","Model Evaluation",["confusion-matrix","precision","recall","roc-auc"],"intermediate"),
    ("_10_05_model_evaluation","_10_05_03_cross_validation_strategies.md",5,3,"Cross-Validation Strategies","Model Evaluation",["kfold","stratified-kfold","cross-val-score"],"intermediate"),
    ("_10_05_model_evaluation","_10_05_04_hyperparameter_tuning.md",5,4,"Hyperparameter Tuning","Model Evaluation",["grid-search","random-search","optuna","bayesian"],"intermediate"),
    ("_10_05_model_evaluation","_10_05_05_calibration_threshold_tuning.md",5,5,"Calibration and Threshold Tuning","Model Evaluation",["platt-scaling","brier-score","threshold"],"advanced"),
    ("_10_05_model_evaluation","_10_05_06_model_comparison_statistical_testing.md",5,6,"Model Comparison and Statistical Testing","Model Evaluation",["mcnemar-test","wilcoxon","bootstrap-ci"],"advanced"),
    ("_10_06_supervised_learning/_10_06_01_regression","_10_06_01_01_linear_regression_simple_multiple.md",6,1,"Simple and Multiple Linear Regression","Supervised - Regression",["linear-regression","ols","residuals"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_01_regression","_10_06_01_02_polynomial_regression.md",6,2,"Polynomial Regression","Supervised - Regression",["polynomial-features","overfitting","degree"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_01_regression","_10_06_01_03_ridge_lasso_elastic_net.md",6,3,"Ridge, Lasso, and Elastic Net","Supervised - Regression",["ridge","lasso","elastic-net","l1","l2"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_01_regression","_10_06_01_04_decision_tree_regression.md",6,4,"Decision Tree Regression","Supervised - Regression",["cart","mse-split","max-depth","pruning"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_01_regression","_10_06_01_05_random_forest_extratrees_regression.md",6,5,"Random Forest and Extra Trees Regression","Supervised - Regression",["random-forest","extra-trees","bagging","oob"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_01_regression","_10_06_01_06_gradient_boosting_regression.md",6,6,"Gradient Boosting Regression","Supervised - Regression",["gradient-boosting","hist-gb","functional-gradient"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_01_regression","_10_06_01_07_xgboost_regression.md",6,7,"XGBoost Regression","Supervised - Regression",["xgboost","early-stopping","gpu","reg-alpha"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_01_regression","_10_06_01_08_lightgbm_regression.md",6,8,"LightGBM Regression","Supervised - Regression",["lightgbm","goss","efb","leaf-wise"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_01_regression","_10_06_01_09_catboost_regression.md",6,9,"CatBoost Regression","Supervised - Regression",["catboost","ordered-boosting","symmetric-trees"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_01_regression","_10_06_01_10_support_vector_regression.md",6,10,"Support Vector Regression (SVR)","Supervised - Regression",["svr","epsilon-insensitive","kernel","rbf"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_01_regression","_10_06_01_11_bayesian_regression.md",6,11,"Bayesian Regression","Supervised - Regression",["bayesian-ridge","ard","gaussian-process","uncertainty"],"advanced"),
    ("_10_06_supervised_learning/_10_06_01_regression","_10_06_01_12_sgd_online_learning.md",6,12,"SGD and Online Learning","Supervised - Regression",["sgd-regressor","partial-fit","online-learning"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_02_classification","_10_06_02_01_logistic_regression.md",7,1,"Logistic Regression","Supervised - Classification",["logistic-regression","sigmoid","multiclass"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_02_classification","_10_06_02_02_knn_classification.md",7,2,"K-Nearest Neighbors (KNN)","Supervised - Classification",["knn","distance-metrics","ball-tree"],"beginner"),
    ("_10_06_supervised_learning/_10_06_02_classification","_10_06_02_03_naive_bayes.md",7,3,"Naive Bayes Classification","Supervised - Classification",["naive-bayes","gaussian-nb","laplace-smoothing"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_02_classification","_10_06_02_04_decision_tree_classification.md",7,4,"Decision Tree Classification","Supervised - Classification",["cart","gini","entropy","plot-tree"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_02_classification","_10_06_02_05_random_forest_classification.md",7,5,"Random Forest Classification","Supervised - Classification",["random-forest","oob-score","predict-proba"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_02_classification","_10_06_02_06_support_vector_machine.md",7,6,"Support Vector Machine (SVM)","Supervised - Classification",["svm","svc","kernel","soft-margin"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_02_classification","_10_06_02_07_perceptron_mlp.md",7,7,"Perceptron and MLP Classifier","Supervised - Classification",["perceptron","mlp","hidden-layers","adam"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_02_classification","_10_06_02_08_gradient_boosting_classification.md",7,8,"Gradient Boosting Classification","Supervised - Classification",["gradient-boosting","hist-gb","log-loss"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_02_classification","_10_06_02_09_xgboost_classification.md",7,9,"XGBoost Classification","Supervised - Classification",["xgboost","binary-logistic","dmatrix","dart"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_02_classification","_10_06_02_10_lightgbm_classification.md",7,10,"LightGBM Classification","Supervised - Classification",["lightgbm","dart","leaf-wise","scale-pos-weight"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_02_classification","_10_06_02_11_catboost_classification.md",7,11,"CatBoost Classification","Supervised - Classification",["catboost","ordered-boosting","symmetric-trees"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_02_classification","_10_06_02_12_adaboost_classification.md",7,12,"AdaBoost Classification","Supervised - Classification",["adaboost","stumps","samme","sample-weighting"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_02_classification","_10_06_02_13_sgd_online_classification.md",7,13,"SGD and Online Classification","Supervised - Classification",["sgd-classifier","partial-fit","hinge-loss"],"intermediate"),
    ("_10_06_supervised_learning/_10_06_02_classification","_10_06_02_14_multilabel_multioutput.md",7,14,"Multi-Label and Multi-Output Classification","Supervised - Classification",["multi-label","classifier-chain","hamming-loss"],"advanced"),
    ("_10_07_unsupervised_learning","_10_07_01_kmeans_clustering.md",8,1,"K-Means Clustering","Unsupervised Learning",["kmeans","elbow","silhouette","inertia"],"intermediate"),
    ("_10_07_unsupervised_learning","_10_07_02_dbscan_density_clustering.md",8,2,"DBSCAN and Density-Based Clustering","Unsupervised Learning",["dbscan","hdbscan","optics","noise"],"intermediate"),
    ("_10_07_unsupervised_learning","_10_07_03_hierarchical_clustering.md",8,3,"Hierarchical Clustering","Unsupervised Learning",["agglomerative","dendrogram","ward","scipy"],"intermediate"),
    ("_10_07_unsupervised_learning","_10_07_04_gaussian_mixture_models.md",8,4,"Gaussian Mixture Models (GMM)","Unsupervised Learning",["gmm","em-algorithm","bic","aic"],"advanced"),
    ("_10_07_unsupervised_learning","_10_07_05_spectral_clustering.md",8,5,"Spectral Clustering","Unsupervised Learning",["spectral","graph-laplacian","affinity"],"advanced"),
    ("_10_07_unsupervised_learning","_10_07_06_pca_applied.md",8,6,"PCA Applied","Unsupervised Learning",["pca","explained-variance","incremental-pca"],"intermediate"),
    ("_10_07_unsupervised_learning","_10_07_07_tsne_umap_applied.md",8,7,"t-SNE and UMAP Applied","Unsupervised Learning",["tsne","umap","perplexity","manifold"],"intermediate"),
    ("_10_07_unsupervised_learning","_10_07_08_anomaly_detection.md",8,8,"Anomaly Detection","Unsupervised Learning",["isolation-forest","lof","one-class-svm","novelty"],"intermediate"),
    ("_10_07_unsupervised_learning","_10_07_09_association_rule_mining.md",8,9,"Association Rule Mining","Unsupervised Learning",["apriori","fpgrowth","support","lift","mlxtend"],"intermediate"),
    ("_10_07_unsupervised_learning","_10_07_10_topic_modeling_classical.md",8,10,"Topic Modeling Classical","Unsupervised Learning",["lda","nmf","lsa","gensim","pyldavis"],"intermediate"),
    ("_10_08_semi_supervised_learning","_10_08_01_semi_supervised_foundations.md",9,1,"Semi-Supervised Learning Foundations","Semi-Supervised Learning",["ssl","pseudo-labeling","cluster-assumption"],"intermediate"),
    ("_10_08_semi_supervised_learning","_10_08_02_self_training.md",9,2,"Self-Training","Semi-Supervised Learning",["self-training","pseudo-labels","threshold"],"intermediate"),
    ("_10_08_semi_supervised_learning","_10_08_03_label_propagation_spreading.md",9,3,"Label Propagation and Spreading","Semi-Supervised Learning",["label-propagation","label-spreading","graph-based"],"intermediate"),
    ("_10_08_semi_supervised_learning","_10_08_04_generative_semi_supervised.md",9,4,"Generative Semi-Supervised Models","Semi-Supervised Learning",["em-ssl","gmm-ssl","unlabeled-data"],"advanced"),
    ("_10_09_reinforcement_learning","_10_09_01_rl_foundations_mdp.md",10,1,"RL Foundations and MDP","Reinforcement Learning",["mdp","bellman","value-function","policy","reward"],"intermediate"),
    ("_10_09_reinforcement_learning","_10_09_02_dynamic_programming_methods.md",10,2,"Dynamic Programming Methods","Reinforcement Learning",["policy-iteration","value-iteration","policy-evaluation"],"intermediate"),
    ("_10_09_reinforcement_learning","_10_09_03_q_learning_sarsa.md",10,3,"Q-Learning and SARSA","Reinforcement Learning",["q-learning","sarsa","td-learning","q-table","epsilon-greedy"],"intermediate"),
    ("_10_09_reinforcement_learning","_10_09_04_multi_armed_bandit.md",10,4,"Multi-Armed Bandit","Reinforcement Learning",["bandit","ucb","thompson-sampling","exploration"],"intermediate"),
    ("_10_09_reinforcement_learning","_10_09_05_gymnasium_stable_baselines3.md",10,5,"Gymnasium and Stable-Baselines3","Reinforcement Learning",["gymnasium","stable-baselines3","ppo","dqn","a2c"],"intermediate"),
    ("_10_10_ensemble_learning","_10_10_01_bagging_random_subspaces.md",11,1,"Bagging and Random Subspaces","Ensemble Learning",["bagging","bootstrap","oob"],"intermediate"),
    ("_10_10_ensemble_learning","_10_10_02_boosting_adaboost_gradient.md",11,2,"Boosting AdaBoost and Gradient Boosting","Ensemble Learning",["boosting","adaboost","gradient-boosting"],"intermediate"),
    ("_10_10_ensemble_learning","_10_10_03_xgboost_lightgbm_catboost_deepdive.md",11,3,"XGBoost LightGBM CatBoost Deep Dive","Ensemble Learning",["xgboost","lightgbm","catboost","comparison"],"advanced"),
    ("_10_10_ensemble_learning","_10_10_04_stacking_blending.md",11,4,"Stacking and Blending","Ensemble Learning",["stacking","blending","meta-learner","oof"],"advanced"),
    ("_10_10_ensemble_learning","_10_10_05_voting_ensembles.md",11,5,"Voting Ensembles","Ensemble Learning",["voting-classifier","soft-voting","hard-voting"],"intermediate"),
    ("_10_10_ensemble_learning","_10_10_06_cascade_ensembles.md",11,6,"Cascade Ensembles","Ensemble Learning",["cascade","deep-forest","mixture-of-experts"],"advanced"),
    ("_10_10_ensemble_learning","_10_10_07_ensemble_competition_strategies.md",11,7,"Ensemble Competition Strategies","Ensemble Learning",["rank-averaging","greedy-selection","kaggle"],"advanced"),
    ("_10_11_explainable_ai","_10_11_01_explainability_foundations.md",12,1,"Explainability Foundations","Explainable AI",["xai","gdpr","eu-ai-act","interpretable"],"intermediate"),
    ("_10_11_explainable_ai","_10_11_02_shap_explainability.md",12,2,"SHAP Explainability","Explainable AI",["shap","shapley-values","tree-explainer","summary-plot"],"intermediate"),
    ("_10_11_explainable_ai","_10_11_03_lime_explainability.md",12,3,"LIME Explainability","Explainable AI",["lime","local-surrogate","lime-tabular","lime-image"],"intermediate"),
    ("_10_11_explainable_ai","_10_11_04_permutation_partial_dependence.md",12,4,"Permutation and Partial Dependence","Explainable AI",["permutation-importance","pdp","ice","ale"],"intermediate"),
    ("_10_11_explainable_ai","_10_11_05_counterfactual_explanations.md",12,5,"Counterfactual Explanations","Explainable AI",["counterfactual","dice","algorithmic-recourse"],"advanced"),
    ("_10_11_explainable_ai","_10_11_06_model_cards_transparency.md",12,6,"Model Cards and AI Transparency","Explainable AI",["model-cards","fairlearn","fairness","bias-audit"],"intermediate"),
    ("_10_12_automl","_10_12_01_automl_foundations.md",13,1,"AutoML Foundations","AutoML",["automl","cash","meta-learning","nas"],"intermediate"),
    ("_10_12_automl","_10_12_02_autosklearn.md",13,2,"Auto-Sklearn","AutoML",["auto-sklearn","smac3","ensemble-selection","openml"],"intermediate"),
    ("_10_12_automl","_10_12_03_flaml_autogluon.md",13,3,"FLAML and AutoGluon","AutoML",["flaml","autogluon","tabular-predictor","stacking"],"intermediate"),
    ("_10_12_automl","_10_12_04_optuna.md",13,4,"Optuna Hyperparameter Optimization","AutoML",["optuna","tpe","pruners","multi-objective","pareto"],"intermediate"),
    ("_10_12_automl","_10_12_05_feature_engineering_automation.md",13,5,"Feature Engineering Automation","AutoML",["featuretools","tsfresh","feature-engine","tpot"],"intermediate"),
    ("_10_13_mlops_for_ml","_10_13_01_experiment_tracking_mlflow.md",14,1,"Experiment Tracking with MLflow","MLOps for ML",["mlflow","tracking","model-registry","autolog"],"intermediate"),
    ("_10_13_mlops_for_ml","_10_13_02_data_versioning_dvc.md",14,2,"Data Versioning with DVC","MLOps for ML",["dvc","data-versioning","pipeline","remote-storage"],"intermediate"),
    ("_10_13_mlops_for_ml","_10_13_03_model_serialization.md",14,3,"Model Serialization and Persistence","MLOps for ML",["joblib","pickle","onnx","sklearn-onnx"],"intermediate"),
    ("_10_13_mlops_for_ml","_10_13_04_sklearn_pipelines_production.md",14,4,"Sklearn Pipelines for Production","MLOps for ML",["pipeline","production","batch-inference","unit-testing"],"intermediate"),
    ("_10_13_mlops_for_ml","_10_13_05_model_serving_fastapi.md",14,5,"Model Serving with FastAPI","MLOps for ML",["fastapi","model-serving","pydantic","health-check"],"intermediate"),
    ("_10_13_mlops_for_ml","_10_13_06_model_monitoring_drift.md",14,6,"Model Monitoring and Drift Detection","MLOps for ML",["data-drift","evidently","alibi-detect","psi","ks-test"],"advanced"),
    ("_10_13_mlops_for_ml","_10_13_07_cicd_for_ml.md",14,7,"CI/CD for ML Models","MLOps for ML",["github-actions","cml","dvc-repro","model-promotion"],"advanced"),
    ("_10_13_mlops_for_ml","_10_13_08_feature_stores.md",14,8,"Feature Stores","MLOps for ML",["feast","hopsworks","online-store","point-in-time"],"advanced"),
    ("_10_14_industry_projects","_10_14_01_customer_churn_prediction.md",15,1,"Customer Churn Prediction","Industry Projects",["churn","xgboost","shap","fastapi","mlflow"],"advanced"),
    ("_10_14_industry_projects","_10_14_02_credit_risk_scoring.md",15,2,"Credit Risk Scoring System","Industry Projects",["credit-risk","scorecard","woe","iv","fairlearn"],"advanced"),
    ("_10_14_industry_projects","_10_14_03_demand_forecasting_pipeline.md",15,3,"Demand Forecasting Pipeline","Industry Projects",["forecasting","lightgbm","prophet","arima","m5"],"advanced"),
    ("_10_14_industry_projects","_10_14_04_fraud_detection_system.md",15,4,"Fraud Detection System","Industry Projects",["fraud","isolation-forest","threshold-tuning","psi"],"advanced"),
    ("_10_14_industry_projects","_10_14_05_recommendation_engine.md",15,5,"Recommendation Engine","Industry Projects",["collaborative-filtering","svd","content-based","ndcg"],"advanced"),
    ("_10_14_industry_projects","_10_14_06_iot_anomaly_detection.md",15,6,"IoT Anomaly Detection","Industry Projects",["iot","isolation-forest","onnx","edge-deployment"],"advanced"),
]

created = 0
skipped = 0

for folder, fname, mod, les, title, mod_title, tags, diff in LESSONS:
    dirpath = os.path.join(BASE, folder)
    os.makedirs(dirpath, exist_ok=True)
    fpath = os.path.join(dirpath, fname)
    if not os.path.exists(fpath):
        lid = f"10_{mod:02d}_{les:02d}"
        tag_str = ", ".join('"' + t + '"' for t in tags)
        content = f'---\nid: "{lid}"\ntitle: "{title}"\ncourse: "Machine Learning"\nmodule: {mod}\nmodule_title: "{mod_title}"\nlesson: {les}\nversion: "2.0"\ndifficulty: "{diff}"\nduration_minutes: 60\ntags: [{tag_str}]\nprerequisites: []\nlab_required: true\n---\n\n# {title}\n\n> **Status**: Syllabus stub. Full lesson content to be authored.\n\n---\n\n## Topics Covered\n\n*(See Phase 1 ML Syllabus for full topic and subtopic breakdown)*\n\n---\n\n## Learning Objectives\n\n- To be defined during content authoring.\n'
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[CREATE] {fname}")
        created += 1
    else:
        print(f"[SKIP]   {fname}")
        skipped += 1

print(f"\nDONE — Created: {created}  Skipped: {skipped}  Total: {created+skipped}")

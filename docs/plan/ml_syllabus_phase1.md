# Phase 1: Machine Learning — Enterprise Syllabus
## Learning OS Enterprise Standard | Curriculum Architecture v2.0

**Classification**: Chief Curriculum Architect — Syllabus Design Document  
**Phase**: 1 of 8  
**Domain**: Machine Learning  
**Required Previous Courses**: DS-Math (_08_ds_math), Python Data Science (_09_python_data_science)  
**Folder Root**: `docs/curriculum/_10_machine_learning/`  
**Last Updated**: 2026-07-28

---

## Dependency Graph (Required Before This Phase)

```
_08_ds_math  (Linear Algebra, Calculus, Probability, Statistics)
    └─> _09_python_data_science  (NumPy, Pandas, Matplotlib, Seaborn, SciPy, Statsmodels)
            └─> _10_machine_learning   ◄── THIS PHASE
```

Cross-course reuse nodes (zero duplication):
- `Python.OOP`, `Python.Functions`, `Python.DataStructures`
- `MySQL.Queries`, `MySQL.Joins` (for SQL-based feature stores)
- `GIT-FND-001`, `GIT-FND-005` (model versioning)
- `FastAPI.Endpoints`, `FastAPI.Pydantic` (model serving)
- `DS-MOD-1.1` → `DS-MOD-1.3` (math prerequisites)
- `DS-MOD-2.1` → `DS-MOD-3.2` (NumPy / Pandas / Visualization)

---

## Skills Gained (This Phase)

- Design and execute full ML pipelines from raw data to deployed model
- Apply feature engineering, scaling, encoding, and selection techniques
- Train, tune, and evaluate 40+ supervised and unsupervised algorithms
- Build ensemble models with XGBoost, LightGBM, and CatBoost
- Implement model explainability with SHAP and LIME
- Automate model selection with AutoML frameworks
- Forecast time series with ARIMA, Prophet, and LSTM wrappers
- Architect recommender systems (collaborative + content-based)
- Version experiments with MLflow and DVC
- Deploy scikit-learn pipelines as REST endpoints

---

## Industry Applications (This Phase)

- Customer churn prediction
- Fraud detection pipelines
- Price forecasting
- Medical diagnosis classification
- Retail demand forecasting
- Recommendation engines
- Anomaly detection in IoT streams
- Credit risk scoring

---

## Course Structure

```
_10_machine_learning/
├── _10_01_foundations/
├── _10_02_mathematics_for_ml/
├── _10_03_data_preparation/
├── _10_04_feature_engineering/
├── _10_05_model_evaluation/
├── _10_06_supervised_learning/
│   ├── _10_06_01_regression/
│   └── _10_06_02_classification/
├── _10_07_unsupervised_learning/
├── _10_08_semi_supervised_learning/
├── _10_09_reinforcement_learning/
├── _10_10_ensemble_learning/
├── _10_11_explainable_ai/
├── _10_12_automl/
├── _10_13_mlops_for_ml/
└── _10_14_industry_projects/
```

---

## MODULE 01 — ML Foundations

**Folder**: `_10_01_foundations/`  
**Lesson Count**: 6  
**Learning Order**: 1st

### Lessons

#### Lesson 01.01 — What is Machine Learning?
**File**: `_10_01_01_what_is_machine_learning.md`

| Topics | Subtopics |
|---|---|
| AI vs ML vs DL hierarchy | Narrow AI, General AI, Superintelligence |
| Types of learning | Supervised, Unsupervised, Semi-supervised, Reinforcement, Self-supervised |
| ML problem taxonomy | Regression, Classification, Clustering, Ranking, Generation |
| The ML workflow | Data → Features → Model → Evaluation → Deployment |
| When NOT to use ML | Rule-based vs. learned systems, cost-benefit analysis |

---

#### Lesson 01.02 — The Scikit-Learn Ecosystem
**File**: `_10_01_02_scikit_learn_ecosystem.md`

| Topics | Subtopics |
|---|---|
| Scikit-learn architecture | Estimator API, fit/predict/transform, BaseEstimator |
| Core modules overview | `sklearn.linear_model`, `sklearn.tree`, `sklearn.ensemble`, `sklearn.cluster`, `sklearn.preprocessing`, `sklearn.pipeline`, `sklearn.metrics` |
| Consistent API design | Estimators, Transformers, Predictors, Meta-estimators |
| Data types in sklearn | Dense arrays, sparse matrices, DataFrames |
| Ecosystem integrations | XGBoost, LightGBM, Imbalanced-learn, SHAP, LIME |

---

#### Lesson 01.03 — Data Splitting and Leakage
**File**: `_10_01_03_data_splitting_and_leakage.md`

| Topics | Subtopics |
|---|---|
| Train / validation / test split | Holdout strategy, ratios (60/20/20, 70/15/15, 80/20) |
| `train_test_split` | `stratify`, `random_state`, `shuffle` |
| Cross-validation | K-Fold, Stratified K-Fold, Leave-One-Out (LOO), Group K-Fold |
| Data leakage | Target leakage, train-test leakage, temporal leakage |
| Leakage prevention | Fit transformers only on train, pipeline-first design |

---

#### Lesson 01.04 — The Bias-Variance Tradeoff
**File**: `_10_01_04_bias_variance_tradeoff.md`

| Topics | Subtopics |
|---|---|
| Bias | Underfitting, high train error, model too simple |
| Variance | Overfitting, high test error, model too complex |
| The tradeoff | Total error = Bias² + Variance + Irreducible noise |
| Diagnosing with learning curves | `validation_curve`, `learning_curve` |
| Remedies | Regularization (bias-reducer), more data (variance-reducer), ensemble methods |

---

#### Lesson 01.05 — The No Free Lunch Theorem
**File**: `_10_01_05_no_free_lunch_theorem.md`

| Topics | Subtopics |
|---|---|
| NFL theorem statement | No universally best algorithm across all distributions |
| Practical implications | Algorithm selection is problem-specific |
| Inductive bias | Every algorithm makes assumptions about data |
| Model selection strategy | Baseline → Domain knowledge → Empirical tuning |

---

#### Lesson 01.06 — ML Environment Setup
**File**: `_10_01_06_ml_environment_setup.md`

| Topics | Subtopics |
|---|---|
| Python environment | `conda`, `venv`, `uv`, `pyproject.toml` |
| Core ML stack | scikit-learn, numpy, pandas, matplotlib, seaborn |
| GPU environment | CUDA, cuDNN, nvidia-smi verification |
| Jupyter ecosystem | JupyterLab, VS Code notebooks, Google Colab, Kaggle kernels |
| Project structure | `data/`, `notebooks/`, `src/`, `models/`, `reports/` |
| Version pinning | `requirements.txt`, `environment.yml`, lockfiles |

---

## MODULE 02 — Mathematics for ML (Bridge Module)

**Folder**: `_10_02_mathematics_for_ml/`  
**Lesson Count**: 4  
**Strategy**: Targeted bridge — reuses `_08_ds_math` nodes; covers ONLY ML-specific math not in DS-Math course  
**Learning Order**: 2nd

### Lessons

#### Lesson 02.01 — Information Theory for ML
**File**: `_10_02_01_information_theory_for_ml.md`

| Topics | Subtopics |
|---|---|
| Entropy | Shannon entropy, formula H(X) = -Σ p(x) log p(x) |
| Cross-entropy | Binary cross-entropy loss, categorical cross-entropy |
| KL Divergence | Forward / reverse KL, asymmetry |
| Mutual Information | Feature relevance scoring |
| Gini Impurity vs Entropy | Decision tree split criteria |

---

#### Lesson 02.02 — Optimization Theory for ML
**File**: `_10_02_02_optimization_theory_for_ml.md`

| Topics | Subtopics |
|---|---|
| Cost function landscape | Convex vs non-convex, local/global minima |
| Gradient Descent variants | Batch GD, Stochastic GD, Mini-batch GD |
| Learning rate | Fixed LR, LR scheduling, warm restarts |
| Momentum & adaptive methods | SGD + Momentum, RMSProp, Adam (preview for DL course) |
| Convergence conditions | Wolfe conditions, stopping criteria |

---

#### Lesson 02.03 — Linear Algebra in ML (Applied)
**File**: `_10_02_03_linear_algebra_applied_ml.md`

| Topics | Subtopics |
|---|---|
| PCA math | Covariance matrix, eigenvectors as principal components |
| SVD in recommender systems | Low-rank factorization, latent factors |
| Matrix norms | L1, L2, Frobenius norm, their role in regularization |
| Kernel trick | Mercer's theorem, implicit high-dimensional mapping |
| Distance metrics | Euclidean, Manhattan, Cosine, Mahalanobis |

---

#### Lesson 02.04 — Probabilistic Foundations for ML
**File**: `_10_02_04_probabilistic_foundations_ml.md`

| Topics | Subtopics |
|---|---|
| MLE vs MAP | Maximum Likelihood Estimation, Maximum A Posteriori |
| Bayesian inference | Prior, Likelihood, Posterior, Bayes' theorem in ML |
| Generative vs Discriminative | P(x,y) vs P(y|x), Naive Bayes vs Logistic Regression |
| Probabilistic graphical models | Bayes Networks (intro concept) |
| Monte Carlo methods | Sampling, bootstrapping, confidence intervals for ML |

---

## MODULE 03 — Data Preparation

**Folder**: `_10_03_data_preparation/`  
**Lesson Count**: 7  
**Learning Order**: 3rd

### Lessons

#### Lesson 03.01 — Exploratory Data Analysis (EDA)
**File**: `_10_03_01_exploratory_data_analysis.md`

| Topics | Subtopics |
|---|---|
| EDA workflow | Shape, dtypes, describe(), info(), head/tail |
| Univariate analysis | Distributions, skewness, kurtosis, outlier flags |
| Bivariate analysis | Correlation matrix, scatter plots, pair plots |
| Multivariate analysis | Heatmaps, 3D scatter, parallel coordinates |
| Target variable analysis | Class imbalance detection, regression target distribution |
| Automated EDA | `ydata-profiling` (pandas-profiling), `sweetviz`, `dtale` |

---

#### Lesson 03.02 — Handling Missing Values
**File**: `_10_03_02_handling_missing_values.md`

| Topics | Subtopics |
|---|---|
| Missing data mechanisms | MCAR, MAR, MNAR |
| Detection | `isnull()`, `missingno` library, pattern analysis |
| Deletion strategies | Listwise, pairwise, threshold-based column removal |
| Imputation: Simple | Mean, median, mode, constant fill |
| Imputation: Advanced | KNN Imputer, Iterative Imputer (MICE), `HistGradientBoosting` native NaN support |
| Indicator variables | Missing-as-feature: `MissingIndicator` |
| Pipeline integration | `SimpleImputer` in `Pipeline`, avoid leakage |

---

#### Lesson 03.03 — Handling Outliers
**File**: `_10_03_03_handling_outliers.md`

| Topics | Subtopics |
|---|---|
| Outlier types | Point, contextual, collective outliers |
| Detection: Statistical | Z-score (>3σ), IQR method, Modified Z-score |
| Detection: Visual | Boxplots, violin plots, scatter plots |
| Detection: ML-based | Isolation Forest, LOF, One-Class SVM, DBSCAN |
| Treatment strategies | Cap (Winsorize), log transform, remove, bin |
| When to keep outliers | Fraud detection, anomaly detection scenarios |

---

#### Lesson 03.04 — Data Encoding
**File**: `_10_03_04_data_encoding.md`

| Topics | Subtopics |
|---|---|
| Ordinal encoding | `OrdinalEncoder`, natural order preservation |
| One-hot encoding | `OneHotEncoder`, `pd.get_dummies`, dummy variable trap |
| Label encoding | `LabelEncoder`, limitations for tree vs linear models |
| Target encoding | Mean target encoding, smoothing, cross-validation scheme |
| Binary encoding | `category_encoders.BinaryEncoder` |
| Frequency / Count encoding | High-cardinality features |
| Embedding encoding | Concept preview for DL/NLP courses |
| Hashing trick | `FeatureHasher`, memory-efficient encoding |

---

#### Lesson 03.05 — Data Scaling and Normalization
**File**: `_10_03_05_data_scaling_normalization.md`

| Topics | Subtopics |
|---|---|
| Why scaling matters | Distance-based models, gradient descent convergence |
| StandardScaler | Z-score normalization, mean=0, std=1 |
| MinMaxScaler | [0,1] range, sensitivity to outliers |
| RobustScaler | IQR-based, outlier-resistant |
| MaxAbsScaler | Sparse data, preserves zero |
| Normalizer | Row-wise L1/L2 normalization |
| QuantileTransformer | Uniform / Gaussian output |
| PowerTransformer | Box-Cox, Yeo-Johnson transforms |
| When NOT to scale | Tree-based models (invariant to scaling) |

---

#### Lesson 03.06 — Handling Class Imbalance
**File**: `_10_03_06_handling_class_imbalance.md`

| Topics | Subtopics |
|---|---|
| Imbalance problem | Why accuracy is misleading on imbalanced data |
| Resampling: Under-sampling | Random undersampling, Tomek Links, NearMiss |
| Resampling: Over-sampling | Random oversampling, SMOTE, ADASYN, Borderline-SMOTE |
| Combined approaches | SMOTEENN, SMOTETomek |
| Algorithm-level strategies | `class_weight="balanced"`, `scale_pos_weight` in XGBoost |
| Evaluation under imbalance | Precision, Recall, F1, ROC-AUC, PR-AUC, Matthews Correlation |
| `imbalanced-learn` library | Pipeline integration, imblearn Pipeline vs sklearn Pipeline |

---

#### Lesson 03.07 — Data Splitting Strategies
**File**: `_10_03_07_data_splitting_strategies.md`

| Topics | Subtopics |
|---|---|
| Standard holdout | `train_test_split`, stratification |
| Time-series splits | `TimeSeriesSplit`, walk-forward validation, embargo |
| Group splits | `GroupKFold`, `GroupShuffleSplit` (patient data, user data) |
| Stratified multi-label split | `MultilabelStratifiedKFold` (via `iterative-stratification`) |
| Nested CV | Outer loop (generalization), inner loop (hyperparameter tuning) |
| Benchmark datasets | MNIST, CIFAR-10, Iris, Boston, OpenML datasets |

---

## MODULE 04 — Feature Engineering

**Folder**: `_10_04_feature_engineering/`  
**Lesson Count**: 7  
**Learning Order**: 4th

### Lessons

#### Lesson 04.01 — Feature Creation and Transformation
**File**: `_10_04_01_feature_creation_transformation.md`

| Topics | Subtopics |
|---|---|
| Domain-driven features | Date/time decomposition, lag features, ratio features |
| Mathematical transforms | Log, square root, Box-Cox, polynomial expansion |
| Interaction features | Multiplication, ratio, sum of feature pairs |
| Binning | `pd.cut`, `pd.qcut`, `KBinsDiscretizer` |
| Text-to-feature (basic) | Character count, word count, special char count |
| `FunctionTransformer` | Custom sklearn-compatible transforms |

---

#### Lesson 04.02 — Feature Selection: Filter Methods
**File**: `_10_04_02_feature_selection_filter.md`

| Topics | Subtopics |
|---|---|
| Variance threshold | `VarianceThreshold`, remove near-zero variance |
| Correlation filter | Pearson, Spearman, Kendall; multicollinearity removal |
| Statistical tests | `SelectKBest` with `f_classif`, `chi2`, `mutual_info_classif` |
| `f_regression` | For regression targets |
| Mutual information | `mutual_info_regression`, `mutual_info_classif` |

---

#### Lesson 04.03 — Feature Selection: Wrapper Methods
**File**: `_10_04_03_feature_selection_wrapper.md`

| Topics | Subtopics |
|---|---|
| Recursive Feature Elimination | `RFE`, `RFECV` with cross-validation |
| Forward selection | Greedy stepwise addition |
| Backward elimination | Greedy stepwise removal |
| Exhaustive search | `ExhaustiveFeatureSelector` (mlxtend) |
| Computational cost | Why wrappers are expensive, when to use |

---

#### Lesson 04.04 — Feature Selection: Embedded Methods
**File**: `_10_04_04_feature_selection_embedded.md`

| Topics | Subtopics |
|---|---|
| L1 regularization (Lasso) | Automatic zero-coefficient sparsity |
| `SelectFromModel` | Threshold-based model selection |
| Tree-based importance | `feature_importances_`, MDI impurity, permutation |
| Permutation importance | `permutation_importance` (model-agnostic) |
| Elastic Net selection | Combined L1+L2 for correlated features |

---

#### Lesson 04.05 — Dimensionality Reduction (Unsupervised)
**File**: `_10_04_05_dimensionality_reduction_unsupervised.md`

| Topics | Subtopics |
|---|---|
| PCA | Algorithm, explained variance ratio, scree plot, `n_components` |
| Truncated SVD | Sparse data, `TruncatedSVD`, text/NLP applications |
| Kernel PCA | Non-linear dimensionality reduction |
| t-SNE | Visualization of high-dimensional data, perplexity |
| UMAP | Faster than t-SNE, topology preservation, `umap-learn` |
| Autoencoders (preview) | Concept only; implementation in DL Phase |
| ICA | Independent Component Analysis, signal separation |

---

#### Lesson 04.06 — Feature Engineering for Time Series
**File**: `_10_04_06_feature_engineering_time_series.md`

| Topics | Subtopics |
|---|---|
| Lag features | `shift()`, lookback windows |
| Rolling statistics | `rolling().mean()`, `rolling().std()`, `rolling().min()` |
| Expanding windows | `expanding().mean()` |
| Date/time features | Day of week, month, quarter, is_weekend, is_holiday |
| Fourier features | Seasonal sinusoidal encoding |
| Target encoding over time | `tsfresh` library features |
| `featuretools` | Automated deep feature synthesis |

---

#### Lesson 04.07 — Sklearn Pipelines and ColumnTransformer
**File**: `_10_04_07_sklearn_pipelines_columntransformer.md`

| Topics | Subtopics |
|---|---|
| `Pipeline` | Step chaining, fit/transform/predict in one object |
| `ColumnTransformer` | Different transforms per feature group |
| `make_pipeline` / `make_column_transformer` | Shorthand constructors |
| `set_output` API | Pandas output from transformers (sklearn 1.2+) |
| Custom transformers | `BaseEstimator`, `TransformerMixin`, `fit_transform` |
| `FunctionTransformer` | Stateless functions as pipeline steps |
| Persistence | `joblib.dump`, `joblib.load`, `pickle` |
| Pipeline + GridSearchCV | Hyperparameter naming convention (`step__param`) |

---

## MODULE 05 — Model Evaluation

**Folder**: `_10_05_model_evaluation/`  
**Lesson Count**: 6  
**Learning Order**: 5th

### Lessons

#### Lesson 05.01 — Regression Metrics
**File**: `_10_05_01_regression_metrics.md`

| Topics | Subtopics |
|---|---|
| MAE | Mean Absolute Error, interpretation |
| MSE / RMSE | Squared penalties, scale sensitivity |
| MAPE / SMAPE | Percentage errors, division-by-zero edge case |
| R² (Coefficient of Determination) | Range, interpretation, negative R² |
| Adjusted R² | Penalty for extra features |
| Huber Loss | Robust to outliers, δ parameter |
| `sklearn.metrics` functions | `mean_absolute_error`, `mean_squared_error`, `r2_score` |

---

#### Lesson 05.02 — Classification Metrics
**File**: `_10_05_02_classification_metrics.md`

| Topics | Subtopics |
|---|---|
| Confusion matrix | TP, FP, TN, FN, `confusion_matrix`, `ConfusionMatrixDisplay` |
| Accuracy | Limitations on imbalanced data |
| Precision | Positive Predictive Value |
| Recall (Sensitivity) | True Positive Rate |
| F1 Score | Harmonic mean, `f1_score(average=...)` |
| Fbeta Score | Weighing precision vs recall |
| Specificity | True Negative Rate |
| ROC Curve & AUC | `roc_curve`, `roc_auc_score`, threshold selection |
| Precision-Recall Curve | Better for imbalanced data, `average_precision_score` |
| Matthews Correlation Coefficient | Balanced metric for imbalance |
| Cohen's Kappa | Inter-rater agreement for classification |
| Log Loss | Probabilistic classifier evaluation |
| Multi-class strategies | OvO, OvR, micro/macro/weighted averaging |

---

#### Lesson 05.03 — Cross-Validation Strategies
**File**: `_10_05_03_cross_validation_strategies.md`

| Topics | Subtopics |
|---|---|
| K-Fold CV | `KFold`, variance of estimates |
| Stratified K-Fold | Class-proportion preservation |
| Leave-One-Out | When to use, computational cost |
| Repeated K-Fold | `RepeatedKFold`, `RepeatedStratifiedKFold` |
| `cross_val_score` | `scoring` parameter, multiple metrics |
| `cross_validate` | Multiple metric evaluation |
| CV with pipelines | Correct fit/transform scoping |
| Nested CV | Unbiased generalization estimate with tuning |

---

#### Lesson 05.04 — Hyperparameter Tuning
**File**: `_10_05_04_hyperparameter_tuning.md`

| Topics | Subtopics |
|---|---|
| Grid Search | `GridSearchCV`, `param_grid`, exhaustive |
| Random Search | `RandomizedSearchCV`, `n_iter`, `param_distributions` |
| Bayesian Optimization | `optuna`, `scikit-optimize`, Tree Parzen Estimators |
| HalvingGridSearchCV | Successive halving, resource-efficient |
| `HalvingRandomSearchCV` | Same as above, randomized |
| Hyperopt | Hyperopt library, `fmin`, `hp.*` distributions |
| Ray Tune | Distributed hyperparameter search |
| Early stopping integration | XGBoost, LightGBM early stopping in CV |
| `best_params_`, `best_score_` | Reading results |
| Warm starting | `warm_start=True`, `n_jobs=-1` |

---

#### Lesson 05.05 — Calibration and Threshold Tuning
**File**: `_10_05_05_calibration_threshold_tuning.md`

| Topics | Subtopics |
|---|---|
| Probability calibration | Why raw scores may not be probabilities |
| Platt Scaling | `CalibratedClassifierCV(method="sigmoid")` |
| Isotonic Regression | `CalibratedClassifierCV(method="isotonic")` |
| Reliability diagrams | `CalibrationDisplay`, `calibration_curve` |
| Brier Score | Probability accuracy metric |
| Threshold optimization | Precision-Recall tradeoff, F1-optimized threshold |
| Business-driven thresholds | Cost-sensitive classification |

---

#### Lesson 05.06 — Model Comparison and Statistical Testing
**File**: `_10_05_06_model_comparison_statistical_testing.md`

| Topics | Subtopics |
|---|---|
| Paired t-test for models | McNemar's test for classifiers |
| Friedman test | Multi-model, multi-dataset comparison |
| Wilcoxon signed-rank | Non-parametric model comparison |
| DeLong test | Comparing ROC-AUC between models |
| Confidence intervals for metrics | Bootstrap CI, `scipy.stats.bootstrap` |
| Multiple comparisons | Holm correction, Nemenyi post-hoc |

---

## MODULE 06 — Supervised Learning

**Folder**: `_10_06_supervised_learning/`  
**Learning Order**: 6th (Regression first, then Classification)

---

### SUB-MODULE 06.01 — Regression

**Folder**: `_10_06_supervised_learning/_10_06_01_regression/`  
**Lesson Count**: 12

#### Lesson 06.01.01 — Simple and Multiple Linear Regression
**File**: `_10_06_01_01_linear_regression_simple_multiple.md`

| Topics | Subtopics |
|---|---|
| OLS estimator | Normal equation: β = (XᵀX)⁻¹Xᵀy |
| Assumptions | Linearity, homoscedasticity, independence, normality |
| `LinearRegression` | `fit_intercept`, `coef_`, `intercept_` |
| Multiple features | Design matrix, feature matrix X shape |
| Residual analysis | Plotting residuals, Q-Q plot |
| Inference | t-statistics, p-values via `statsmodels` (reuse from DS Math) |

---

#### Lesson 06.01.02 — Polynomial Regression
**File**: `_10_06_01_02_polynomial_regression.md`

| Topics | Subtopics |
|---|---|
| `PolynomialFeatures` | `degree`, `interaction_only`, `include_bias` |
| Overfitting risk | Degree too high → memorization |
| Regularization remedy | Combined with Ridge/Lasso |
| Bias-variance at degree | Visualizing with learning curves |

---

#### Lesson 06.01.03 — Ridge, Lasso, and Elastic Net Regression
**File**: `_10_06_01_03_ridge_lasso_elastic_net.md`

| Topics | Subtopics |
|---|---|
| Ridge (L2) | `Ridge`, `alpha`, weight shrinkage, no sparsity |
| Lasso (L1) | `Lasso`, automatic feature selection, coordinate descent |
| Elastic Net (L1+L2) | `ElasticNet`, `l1_ratio`, correlated features |
| `RidgeCV`, `LassoCV`, `ElasticNetCV` | Built-in cross-validated alpha |
| `alpha` path | Regularization path, coefficient paths |
| `MultiTaskLasso` | Multi-output sparse regression |

---

#### Lesson 06.01.04 — Decision Tree Regression
**File**: `_10_06_01_04_decision_tree_regression.md`

| Topics | Subtopics |
|---|---|
| CART algorithm | Recursive binary splitting on MSE |
| Hyperparameters | `max_depth`, `min_samples_split`, `min_samples_leaf`, `max_features` |
| `DecisionTreeRegressor` | `.feature_importances_`, `plot_tree` |
| Pros/Cons | Interpretable, no scaling, prone to overfitting |
| Pruning | `cost_complexity_pruning_path`, `ccp_alpha` |

---

#### Lesson 06.01.05 — Random Forest and Extra Trees Regression
**File**: `_10_06_01_05_random_forest_extratrees_regression.md`

| Topics | Subtopics |
|---|---|
| Bagging intuition | Bootstrap aggregation, variance reduction |
| `RandomForestRegressor` | `n_estimators`, `max_features`, `oob_score` |
| Feature importance | MDI vs permutation importance |
| `ExtraTreesRegressor` | Extreme randomization, lower variance |
| Out-of-bag (OOB) estimate | Free validation set from bagging |

---

#### Lesson 06.01.06 — Gradient Boosting Regression (sklearn)
**File**: `_10_06_01_06_gradient_boosting_regression.md`

| Topics | Subtopics |
|---|---|
| Gradient boosting concept | Sequential residual fitting, functional gradient descent |
| `GradientBoostingRegressor` | `n_estimators`, `learning_rate`, `subsample`, `max_depth` |
| `HistGradientBoostingRegressor` | Histogram-based, fast, native NaN support |
| Stagewise additive modeling | F_m(x) = F_{m-1}(x) + h_m(x) |
| Loss functions | `squared_error`, `absolute_error`, `huber`, `quantile` |

---

#### Lesson 06.01.07 — XGBoost Regression
**File**: `_10_06_01_07_xgboost_regression.md`

| Topics | Subtopics |
|---|---|
| XGBoost architecture | Regularized boosting, second-order gradients |
| `XGBRegressor` | `n_estimators`, `max_depth`, `learning_rate`, `subsample`, `colsample_bytree` |
| Regularization | `reg_alpha` (L1), `reg_lambda` (L2), `gamma` |
| Early stopping | `eval_set`, `early_stopping_rounds` |
| GPU acceleration | `device="cuda"` |
| Native missing value handling | `missing` parameter |

---

#### Lesson 06.01.08 — LightGBM Regression
**File**: `_10_06_01_08_lightgbm_regression.md`

| Topics | Subtopics |
|---|---|
| GOSS and EFB | Gradient-based One-Side Sampling, Exclusive Feature Bundling |
| `LGBMRegressor` | `num_leaves`, `max_depth`, `learning_rate`, `n_estimators` |
| Categorical features | `categorical_feature` parameter, no encoding needed |
| Speed comparison | LightGBM vs XGBoost benchmark |
| Large-scale training | `nthread`, distributed training |

---

#### Lesson 06.01.09 — CatBoost Regression
**File**: `_10_06_01_09_catboost_regression.md`

| Topics | Subtopics |
|---|---|
| Ordered boosting | Target leakage prevention in gradient estimation |
| `CatBoostRegressor` | `iterations`, `learning_rate`, `depth`, `l2_leaf_reg` |
| Native categorical support | `cat_features`, target statistics |
| `Pool` object | CatBoost data format |
| Overfitting detection | Built-in validation, `od_type`, `od_wait` |

---

#### Lesson 06.01.10 — Support Vector Regression (SVR)
**File**: `_10_06_01_10_support_vector_regression.md`

| Topics | Subtopics |
|---|---|
| ε-insensitive loss | Tube concept, ε parameter |
| Kernel functions | Linear, RBF, Polynomial, Sigmoid |
| `SVR` | `C`, `epsilon`, `kernel`, `gamma` |
| `LinearSVR` | Faster for linear kernel, large n |
| Scaling requirement | SVR is not scale-invariant |

---

#### Lesson 06.01.11 — Bayesian Regression
**File**: `_10_06_01_11_bayesian_regression.md`

| Topics | Subtopics |
|---|---|
| Bayesian linear regression | Weight posterior, predictive distribution |
| `BayesianRidge` | `alpha_1`, `alpha_2`, `lambda_1`, `lambda_2`, automatic relevance determination |
| `ARDRegression` | Automatic Relevance Determination |
| Gaussian Processes | `GaussianProcessRegressor`, kernel selection |
| GP kernels | `RBF`, `Matern`, `RationalQuadratic`, `DotProduct` |
| Uncertainty quantification | Confidence intervals from GP |

---

#### Lesson 06.01.12 — SGD and Online Learning
**File**: `_10_06_01_12_sgd_online_learning.md`

| Topics | Subtopics |
|---|---|
| `SGDRegressor` | `loss`, `penalty`, `alpha`, `eta0`, `learning_rate` |
| Online learning | `partial_fit`, streaming/incremental learning |
| `PassiveAggressiveRegressor` | Online regression variant |
| When to use SGD | Huge datasets, online streams |

---

### SUB-MODULE 06.02 — Classification

**Folder**: `_10_06_supervised_learning/_10_06_02_classification/`  
**Lesson Count**: 14

#### Lesson 06.02.01 — Logistic Regression
**File**: `_10_06_02_01_logistic_regression.md`

| Topics | Subtopics |
|---|---|
| Sigmoid function | S(z) = 1/(1+e⁻ᶻ), probability output |
| Decision boundary | Linear boundary in feature space |
| `LogisticRegression` | `C`, `penalty` (L1/L2/Elastic), `solver`, `multi_class` |
| Multi-class strategies | OvR, Multinomial (Softmax) |
| Regularization path | `LogisticRegressionCV` |
| Interpretability | Log-odds interpretation of coefficients |

---

#### Lesson 06.02.02 — K-Nearest Neighbors (KNN)
**File**: `_10_06_02_02_knn_classification.md`

| Topics | Subtopics |
|---|---|
| KNN intuition | Majority vote from k closest neighbors |
| `KNeighborsClassifier` | `n_neighbors`, `weights`, `metric`, `algorithm` |
| Distance metrics | Euclidean, Manhattan, Minkowski, Hamming |
| Choosing k | Elbow method on validation error |
| Curse of dimensionality | KNN degrades in high dimensions |
| `BallTree`, `KDTree` | Efficient nearest-neighbor data structures |

---

#### Lesson 06.02.03 — Naive Bayes Classification
**File**: `_10_06_02_03_naive_bayes.md`

| Topics | Subtopics |
|---|---|
| Bayes theorem applied | P(y|X) ∝ P(X|y) P(y) |
| Conditional independence assumption | "Naive" assumption, when it holds |
| `GaussianNB` | Continuous features, normal distribution |
| `MultinomialNB` | Count features (text classification) |
| `BernoulliNB` | Binary features |
| `ComplementNB` | Complement of class distribution |
| Laplace smoothing | `var_smoothing`, `alpha` |

---

#### Lesson 06.02.04 — Decision Tree Classification
**File**: `_10_06_02_04_decision_tree_classification.md`

| Topics | Subtopics |
|---|---|
| CART for classification | Gini impurity vs entropy split |
| `DecisionTreeClassifier` | `criterion`, `max_depth`, `min_samples_split` |
| Visualization | `plot_tree`, `export_graphviz`, dtreeviz |
| Decision rules | `export_text`, rule extraction |
| Pruning | `ccp_alpha`, `min_impurity_decrease` |

---

#### Lesson 06.02.05 — Random Forest Classification
**File**: `_10_06_02_05_random_forest_classification.md`

| Topics | Subtopics |
|---|---|
| `RandomForestClassifier` | Core hyperparameters, `predict_proba` |
| OOB score | Free validation estimate |
| Feature importance | MDI, permutation importance, SHAP comparison |
| `ExtraTreesClassifier` | Extreme randomization |
| Class balancing | `class_weight`, sample weights |

---

#### Lesson 06.02.06 — Support Vector Machine (SVM)
**File**: `_10_06_02_06_support_vector_machine.md`

| Topics | Subtopics |
|---|---|
| Maximum margin hyperplane | Support vectors, margin, functional margin |
| Soft margin SVM | Slack variable ξ, C parameter |
| Kernel SVM | Feature map φ(x), kernel trick |
| `SVC` | `C`, `kernel`, `gamma`, `degree`, `coef0` |
| `LinearSVC` | For large n, linear kernel |
| `NuSVC` | ν-SVM variant, bound on support vectors |
| Multiclass SVM | OvO (default), OvR |

---

#### Lesson 06.02.07 — Perceptron and MLP Classifier
**File**: `_10_06_02_07_perceptron_mlp.md`

| Topics | Subtopics |
|---|---|
| Perceptron | `Perceptron`, linear threshold unit |
| MLP architecture | Hidden layers, `hidden_layer_sizes`, `activation` |
| `MLPClassifier` | `solver` (adam, sgd, lbfgs), `alpha` (L2), `batch_size` |
| Backpropagation (sklearn level) | Loss curves, `loss_curve_` |
| Early stopping | `early_stopping`, `validation_fraction` |
| Limitations | Not for deep learning (use PyTorch in DL Phase) |

---

#### Lesson 06.02.08 — Gradient Boosting Classification (sklearn)
**File**: `_10_06_02_08_gradient_boosting_classification.md`

| Topics | Subtopics |
|---|---|
| `GradientBoostingClassifier` | Loss functions: `log_loss`, `exponential` |
| `HistGradientBoostingClassifier` | Fast histogram-based, native NaN |
| Feature importance | `feature_importances_` |
| Staged predictions | `staged_predict`, tracking convergence |

---

#### Lesson 06.02.09 — XGBoost Classification
**File**: `_10_06_02_09_xgboost_classification.md`

| Topics | Subtopics |
|---|---|
| `XGBClassifier` | `objective`, `eval_metric`, `use_label_encoder` |
| Binary classification | `objective="binary:logistic"` |
| Multi-class | `objective="multi:softmax"`, `num_class` |
| `DMatrix` | XGBoost native data format |
| Feature importance types | `weight`, `gain`, `cover`, `total_gain` |
| DART booster | Dropout regularization for boosting |

---

#### Lesson 06.02.10 — LightGBM Classification
**File**: `_10_06_02_10_lightgbm_classification.md`

| Topics | Subtopics |
|---|---|
| `LGBMClassifier` | `objective`, `num_class`, `metric` |
| Dart mode | Dropout for gradient boosting |
| Leaf-wise growth | vs. depth-wise (XGBoost) |
| `lgb.Dataset` | LightGBM data format |
| Class imbalance | `is_unbalance`, `scale_pos_weight` |

---

#### Lesson 06.02.11 — CatBoost Classification
**File**: `_10_06_02_11_catboost_classification.md`

| Topics | Subtopics |
|---|---|
| `CatBoostClassifier` | `loss_function`, `eval_metric`, `cat_features` |
| Symmetric trees | Oblivious trees, fast prediction |
| `CatBoostPool` | Data loading with metadata |
| Multiclass support | `MultiClass`, `MultiClassOneVsAll` |

---

#### Lesson 06.02.12 — AdaBoost Classification
**File**: `_10_06_02_12_adaboost_classification.md`

| Topics | Subtopics |
|---|---|
| AdaBoost algorithm | Exponential loss, sample weighting scheme |
| `AdaBoostClassifier` | `base_estimator`, `n_estimators`, `learning_rate`, `algorithm` (SAMME / SAMME.R) |
| Decision stumps | Default base learner |
| Sensitivity to outliers | Noisy labels destroy AdaBoost |

---

#### Lesson 06.02.13 — SGD and Online Classification
**File**: `_10_06_02_13_sgd_online_classification.md`

| Topics | Subtopics |
|---|---|
| `SGDClassifier` | `loss` (hinge, log_loss, modified_huber), `penalty`, `alpha` |
| `partial_fit` | Incremental/online learning |
| `PassiveAggressiveClassifier` | Online learning, no learning rate |
| Stream classification | `River` library preview |

---

#### Lesson 06.02.14 — Multi-Label and Multi-Output Classification
**File**: `_10_06_02_14_multilabel_multioutput.md`

| Topics | Subtopics |
|---|---|
| Multi-label definition | Multiple binary labels per sample |
| `MultiLabelBinarizer` | Encoding multi-label targets |
| `OneVsRestClassifier` | OvR for multi-label |
| `MultiOutputClassifier` | Wrapper for independent per-label classifiers |
| `ClassifierChain` | Sequential label dependency modelling |
| Metrics | `hamming_loss`, `jaccard_score`, `subset_accuracy` |

---

## MODULE 07 — Unsupervised Learning

**Folder**: `_10_07_unsupervised_learning/`  
**Lesson Count**: 10  
**Learning Order**: 7th

### Lessons

#### Lesson 07.01 — K-Means Clustering
**File**: `_10_07_01_kmeans_clustering.md`

| Topics | Subtopics |
|---|---|
| Algorithm | Lloyd's algorithm, centroid update, convergence |
| `KMeans` | `n_clusters`, `init` (k-means++, random), `n_init`, `max_iter` |
| Elbow method | Inertia vs k, `KElbowVisualizer` |
| Silhouette score | `silhouette_score`, `silhouette_samples` |
| `MiniBatchKMeans` | Faster, large datasets |
| Limitations | Spherical clusters assumption, sensitive to scale |

---

#### Lesson 07.02 — DBSCAN and Density-Based Clustering
**File**: `_10_07_02_dbscan_density_clustering.md`

| Topics | Subtopics |
|---|---|
| DBSCAN algorithm | Core points, border points, noise, reachability |
| `DBSCAN` | `eps`, `min_samples`, `metric` |
| `HDBSCAN` | Hierarchical variant, varying density |
| `OPTICS` | Ordering-based, variable epsilon |
| Cluster validity | No need to specify k, arbitrary shapes |

---

#### Lesson 07.03 — Hierarchical Clustering
**File**: `_10_07_03_hierarchical_clustering.md`

| Topics | Subtopics |
|---|---|
| Agglomerative | Bottom-up, `AgglomerativeClustering` |
| Linkage criteria | Ward, complete, average, single |
| Dendrogram | `scipy.cluster.hierarchy.dendrogram` |
| Divisive clustering | Top-down concept |
| Cutting the dendrogram | Number of clusters selection |

---

#### Lesson 07.04 — Gaussian Mixture Models (GMM)
**File**: `_10_07_04_gaussian_mixture_models.md`

| Topics | Subtopics |
|---|---|
| GMM generative model | Mixture of Gaussians, soft assignments |
| EM algorithm | E-step (responsibilities), M-step (parameter update) |
| `GaussianMixture` | `n_components`, `covariance_type` (full, tied, diag, spherical) |
| BIC / AIC | Model order selection |
| `BayesianGaussianMixture` | Automatic component pruning |

---

#### Lesson 07.05 — Spectral Clustering
**File**: `_10_07_05_spectral_clustering.md`

| Topics | Subtopics |
|---|---|
| Graph Laplacian | Affinity matrix, normalized cuts |
| `SpectralClustering` | `n_clusters`, `affinity`, `assign_labels` |
| When spectral works | Non-convex, manifold-shaped clusters |
| Computational cost | O(n³) eigendecomposition |

---

#### Lesson 07.06 — Principal Component Analysis (Applied)
**File**: `_10_07_06_pca_applied.md`

| Topics | Subtopics |
|---|---|
| `PCA` | Full decomposition, `n_components`, `whiten` |
| Explained variance | `explained_variance_ratio_`, cumulative sum |
| Reconstruction | `inverse_transform`, reconstruction error |
| Incremental PCA | `IncrementalPCA` for large datasets |
| Sparse PCA | `SparsePCA`, `MiniBatchSparsePCA` |
| PCA + classification pipeline | Preprocessing into modeling |

---

#### Lesson 07.07 — t-SNE and UMAP (Applied Visualization)
**File**: `_10_07_07_tsne_umap_applied.md`

| Topics | Subtopics |
|---|---|
| t-SNE applied | `TSNE`, `perplexity`, `n_iter`, `learning_rate` |
| UMAP applied | `UMAP`, `n_neighbors`, `min_dist`, `metric` |
| Comparison | t-SNE vs UMAP speed, global structure |
| Downstream use | Cluster visualization, label verification |

---

#### Lesson 07.08 — Anomaly Detection
**File**: `_10_07_08_anomaly_detection.md`

| Topics | Subtopics |
|---|---|
| Problem types | Novelty detection vs outlier detection |
| `IsolationForest` | `n_estimators`, `contamination`, `max_samples` |
| `LocalOutlierFactor` | `n_neighbors`, `novelty`, LOF score |
| `OneClassSVM` | `nu`, `kernel`, novelty detection |
| `EllipticEnvelope` | Gaussian assumption, `contamination` |
| Statistical methods | Z-score, IQR, Grubbs test |
| Time series anomaly | ADTK library, rolling statistics |

---

#### Lesson 07.09 — Association Rule Mining
**File**: `_10_07_09_association_rule_mining.md`

| Topics | Subtopics |
|---|---|
| Market basket analysis | Transactions, itemsets |
| Support | Frequency of itemset |
| Confidence | Conditional probability |
| Lift | Improvement over random |
| `mlxtend` | `TransactionEncoder`, `apriori`, `association_rules` |
| FP-Growth | `fpgrowth`, faster than Apriori |

---

#### Lesson 07.10 — Topic Modeling (Classical)
**File**: `_10_07_10_topic_modeling_classical.md`

| Topics | Subtopics |
|---|---|
| Bag of Words | `CountVectorizer`, `TfidfVectorizer` |
| LSA / LSI | `TruncatedSVD` on TF-IDF, latent semantic structure |
| NMF | `NMF`, non-negative factorization, interpretable topics |
| LDA (sklearn) | `LatentDirichletAllocation`, `n_components`, `max_iter` |
| LDA (Gensim) | `gensim.models.LdaModel`, coherence score |
| pyLDAvis | Interactive topic visualization |

---

## MODULE 08 — Semi-Supervised Learning

**Folder**: `_10_08_semi_supervised_learning/`  
**Lesson Count**: 4  
**Learning Order**: 8th

### Lessons

#### Lesson 08.01 — Semi-Supervised Learning Foundations
**File**: `_10_08_01_semi_supervised_foundations.md`

| Topics | Subtopics |
|---|---|
| Problem definition | Small labeled + large unlabeled data |
| Assumptions | Smoothness, cluster, manifold assumption |
| Real-world scenarios | Medical imaging, NLP, remote sensing |
| Evaluation | How to measure on labeled test set |

---

#### Lesson 08.02 — Self-Training
**File**: `_10_08_02_self_training.md`

| Topics | Subtopics |
|---|---|
| Algorithm | Train on labeled → pseudo-label high-confidence → retrain |
| `SelfTrainingClassifier` | `base_estimator`, `threshold`, `k_best`, `max_iter` |
| Pseudo-labeling | Confidence threshold selection |
| Error accumulation | Risk of incorrect pseudo-labels |

---

#### Lesson 08.03 — Label Propagation and Spreading
**File**: `_10_08_03_label_propagation_spreading.md`

| Topics | Subtopics |
|---|---|
| Graph-based methods | Similarity graph, label propagation on graph |
| `LabelPropagation` | `kernel`, `n_neighbors`, `max_iter` |
| `LabelSpreading` | `alpha` (clamping factor), smoother propagation |
| When to use | Small label count, cluster-structured data |

---

#### Lesson 08.04 — Generative Semi-Supervised Models
**File**: `_10_08_04_generative_semi_supervised.md`

| Topics | Subtopics |
|---|---|
| Expectation-Maximization for SSL | M-step includes unlabeled |
| GMM-based SSL | Soft label assignment |
| Consistency regularization | Concept for DL/modern SSL |
| `semisupervised-learn` | Community libraries |

---

## MODULE 09 — Reinforcement Learning (Classical)

**Folder**: `_10_09_reinforcement_learning/`  
**Lesson Count**: 5  
**Learning Order**: 9th  
**Note**: Deep RL (Policy Gradients, PPO, SAC) is covered in the Deep Learning Phase

### Lessons

#### Lesson 09.01 — RL Foundations and MDP
**File**: `_10_09_01_rl_foundations_mdp.md`

| Topics | Subtopics |
|---|---|
| RL framework | Agent, Environment, State, Action, Reward, Policy |
| MDP definition | (S, A, P, R, γ) formalism |
| Value functions | V(s), Q(s,a), Bellman equations |
| Policy types | Deterministic, stochastic, ε-greedy |
| Exploration vs Exploitation | ε-greedy, UCB, Thompson sampling |

---

#### Lesson 09.02 — Dynamic Programming Methods
**File**: `_10_09_02_dynamic_programming_methods.md`

| Topics | Subtopics |
|---|---|
| Policy evaluation | Iterative Bellman backup |
| Policy iteration | Evaluation → Improvement cycle |
| Value iteration | Direct optimal value computation |
| Assumptions | Known transition model required |
| Gym environments | `gymnasium`, GridWorld setup |

---

#### Lesson 09.03 — Q-Learning and SARSA
**File**: `_10_09_03_q_learning_sarsa.md`

| Topics | Subtopics |
|---|---|
| TD learning | Temporal Difference, bootstrapping |
| Q-Learning | Off-policy, Q-table update rule |
| SARSA | On-policy TD control |
| ε-greedy exploration | Decaying epsilon schedule |
| Tabular Q-table | Dictionary/numpy array, FrozenLake |
| Convergence conditions | Learning rate α, discount γ |

---

#### Lesson 09.04 — Multi-Armed Bandit
**File**: `_10_09_04_multi_armed_bandit.md`

| Topics | Subtopics |
|---|---|
| Bandit formulation | K arms, stationary vs non-stationary |
| ε-greedy bandit | Sample mean estimate |
| UCB (Upper Confidence Bound) | Optimism under uncertainty |
| Thompson Sampling | Bayesian bandit algorithm |
| Applications | A/B testing, recommendation, clinical trials |

---

#### Lesson 09.05 — OpenAI Gymnasium and Stable-Baselines3
**File**: `_10_09_05_gymnasium_stable_baselines3.md`

| Topics | Subtopics |
|---|---|
| `gymnasium` API | `make`, `reset`, `step`, `render`, `close` |
| Observation/action spaces | `Discrete`, `Box`, `MultiDiscrete` |
| Custom environments | `Env` subclass, `observation_space`, `action_space` |
| Stable-Baselines3 | `PPO`, `DQN`, `A2C` from SB3 (intro only) |
| Wrappers | `TimeLimit`, `Monitor`, `VecEnv` |

---

## MODULE 10 — Ensemble Learning

**Folder**: `_10_10_ensemble_learning/`  
**Lesson Count**: 7  
**Learning Order**: 10th

### Lessons

#### Lesson 10.01 — Bagging and Random Subspaces
**File**: `_10_10_01_bagging_random_subspaces.md`

| Topics | Subtopics |
|---|---|
| Bagging theory | Bootstrap sampling, variance reduction proof |
| `BaggingClassifier` / `BaggingRegressor` | `base_estimator`, `n_estimators`, `max_samples`, `max_features` |
| Random Subspace Method | Feature bagging, `max_features < 1.0` |
| OOB estimation | Free validation set |
| Pasting | Sampling without replacement |

---

#### Lesson 10.02 — Boosting: AdaBoost, Gradient Boosting
**File**: `_10_10_02_boosting_adaboost_gradient.md`

| Topics | Subtopics |
|---|---|
| Boosting theory | Sequential error correction, weak learner to strong |
| AdaBoost algorithm | Weighted sample update, α_m computation |
| Gradient Boosting theory | Functional gradient descent, residuals |
| Stagewise additive models | Forward stage-wise fitting |
| Loss function choice | MSE, MAE, Huber, Log-loss |

---

#### Lesson 10.03 — XGBoost, LightGBM, CatBoost Deep Dive
**File**: `_10_10_03_xgboost_lightgbm_catboost_deepdive.md`

| Topics | Subtopics |
|---|---|
| Comparison table | Speed, accuracy, categorical, GPU, memory |
| XGBoost internals | Newton boosting, approximate tree split |
| LightGBM internals | Histogram binning, leaf-wise growth |
| CatBoost internals | Ordered boosting, symmetric trees |
| Unified tuning guide | Key hyperparameters for each |
| Benchmark datasets | Kaggle leaderboard patterns |

---

#### Lesson 10.04 — Stacking and Blending
**File**: `_10_10_04_stacking_blending.md`

| Topics | Subtopics |
|---|---|
| Stacking architecture | Level-0 base learners → Level-1 meta-learner |
| `StackingClassifier` / `StackingRegressor` | `estimators`, `final_estimator`, `cv`, `passthrough` |
| OOF predictions | Out-of-fold stacking to prevent leakage |
| Blending | Holdout-based simple weighted average |
| Deep stacking | Multi-layer stacking |
| Meta-learner choice | Ridge, Logistic Regression, LightGBM |

---

#### Lesson 10.05 — Voting Ensembles
**File**: `_10_10_05_voting_ensembles.md`

| Topics | Subtopics |
|---|---|
| Hard voting | Majority class vote |
| Soft voting | Averaged probabilities, `VotingClassifier(voting="soft")` |
| `VotingClassifier` / `VotingRegressor` | `estimators`, `weights`, `voting` |
| Diversity in ensembles | Different algorithms + different feature views |
| Optimal weight search | Via optuna / grid search on weights |

---

#### Lesson 10.06 — Cascade Ensembles and Multi-Level Stacks
**File**: `_10_10_06_cascade_ensembles.md`

| Topics | Subtopics |
|---|---|
| Cascade generalization | Layer-by-layer feature augmentation |
| Deep forest (gcForest) | Forest-based stacking alternative to DL |
| Mixture of Experts | Gating network + expert networks |
| Snapshot ensembles | Single model trained with cyclic LR |
| Knowledge distillation concept | Preview for DL course |

---

#### Lesson 10.07 — Ensemble Competition Strategies
**File**: `_10_10_07_ensemble_competition_strategies.md`

| Topics | Subtopics |
|---|---|
| Kaggle ensemble tactics | Post-processing, rank averaging |
| Correlation between models | Diversity measurement |
| Greedy ensemble selection | Caruana's algorithm |
| Time-limited ensembles | Allocation of compute budget |
| Reproducibility | Seeds, version control for models |

---

## MODULE 11 — Explainable AI (XAI)

**Folder**: `_10_11_explainable_ai/`  
**Lesson Count**: 6  
**Learning Order**: 11th

### Lessons

#### Lesson 11.01 — Explainability Foundations
**File**: `_10_11_01_explainability_foundations.md`

| Topics | Subtopics |
|---|---|
| Why XAI? | Regulatory (GDPR Art. 22), trust, debugging |
| Interpretable vs Explainable | White-box models, post-hoc methods |
| Global vs Local explanations | Population-level vs per-prediction |
| Model-agnostic vs Model-specific | LIME vs SHAP vs rule extraction |
| EU AI Act requirements | High-risk AI transparency obligations |

---

#### Lesson 11.02 — SHAP (SHapley Additive exPlanations)
**File**: `_10_11_02_shap_explainability.md`

| Topics | Subtopics |
|---|---|
| Shapley values | Game theory, fair contribution attribution |
| `shap.TreeExplainer` | XGBoost, LightGBM, Random Forest |
| `shap.LinearExplainer` | Linear models |
| `shap.KernelExplainer` | Model-agnostic, any sklearn model |
| `shap.DeepExplainer` | Neural networks (preview DL) |
| Visualization | `force_plot`, `summary_plot`, `beeswarm`, `dependence_plot`, `waterfall_plot` |
| Global feature importance | Mean |SHAP| across test set |
| Interaction values | SHAP interaction effects |

---

#### Lesson 11.03 — LIME (Local Interpretable Model-Agnostic Explanations)
**File**: `_10_11_03_lime_explainability.md`

| Topics | Subtopics |
|---|---|
| LIME algorithm | Local surrogate linear model |
| `lime.lime_tabular.LimeTabularExplainer` | Regression and classification modes |
| `lime.lime_text.LimeTextExplainer` | Text classification |
| `lime.lime_image.LimeImageExplainer` | Image segmentation superpixels |
| LIME vs SHAP | Approximation vs exact Shapley, stability |

---

#### Lesson 11.04 — Permutation and Partial Dependence
**File**: `_10_11_04_permutation_partial_dependence.md`

| Topics | Subtopics |
|---|---|
| Permutation importance | `permutation_importance`, global model-agnostic |
| Partial Dependence Plot (PDP) | `PartialDependenceDisplay`, marginal effect |
| Individual Conditional Expectation (ICE) | Per-sample PDP, heterogeneous effects |
| 2D PDP | Joint feature interaction |
| Accumulated Local Effects (ALE) | Corrected for correlated features |

---

#### Lesson 11.05 — Counterfactual Explanations
**File**: `_10_11_05_counterfactual_explanations.md`

| Topics | Subtopics |
|---|---|
| Counterfactual definition | "What would need to change to flip prediction?" |
| `DiCE` library | Diverse Counterfactual Explanations |
| Actionability constraints | Feature mutability, plausibility |
| Wachter counterfactuals | Closest point crossing decision boundary |
| Algorithmic recourse | User-facing explanations for denied applications |

---

#### Lesson 11.06 — Model Cards and AI Transparency
**File**: `_10_11_06_model_cards_transparency.md`

| Topics | Subtopics |
|---|---|
| Model cards | Google Model Card format |
| Datasheets for datasets | Gebru et al. framework |
| Fairness metrics | Demographic parity, equalized odds, calibration |
| `Fairlearn` | `MetricFrame`, mitigation algorithms |
| Bias auditing | Disparate impact, disaggregated metrics |

---

## MODULE 12 — AutoML

**Folder**: `_10_12_automl/`  
**Lesson Count**: 5  
**Learning Order**: 12th

### Lessons

#### Lesson 12.01 — AutoML Foundations
**File**: `_10_12_01_automl_foundations.md`

| Topics | Subtopics |
|---|---|
| AutoML problem | CASH: Combined Algorithm Selection & Hyperparameter |
| Search spaces | Algorithm space + hyperparameter space |
| Meta-learning | Warm-starting from similar datasets |
| Neural Architecture Search | Concept only; implementation in DL Phase |
| Evaluation strategies | Successive halving, multi-fidelity |

---

#### Lesson 12.02 — Auto-Sklearn
**File**: `_10_12_02_autosklearn.md`

| Topics | Subtopics |
|---|---|
| `AutoSklearnClassifier` / `AutoSklearnRegressor` | `time_left_for_this_task`, `per_run_time_limit` |
| Bayesian optimization backend | SMAC3 |
| Ensemble construction | Post-hoc ensemble selection |
| Meta-learning | Warm-starting from 140+ OpenML datasets |
| Limitations | No GPU, no DL pipelines |

---

#### Lesson 12.03 — FLAML and AutoGluon
**File**: `_10_12_03_flaml_autogluon.md`

| Topics | Subtopics |
|---|---|
| FLAML | `AutoML`, resource-efficient, cost-frugal search |
| AutoGluon | `TabularPredictor`, `fit()`, stacking by default |
| AutoGluon presets | `best_quality`, `high_quality`, `medium_quality`, `fast_ai` |
| Feature importance | AutoGluon built-in importance |
| Multi-modal AutoML | Tabular + text + image (AutoGluon) |

---

#### Lesson 12.04 — Optuna (Hyperparameter Optimization Framework)
**File**: `_10_12_04_optuna.md`

| Topics | Subtopics |
|---|---|
| `optuna` API | `create_study`, `optimize`, `Trial`, `suggest_*` |
| Samplers | TPE, CmaEs, GridSampler, RandomSampler |
| Pruners | MedianPruner, HyperbandPruner, SuccessiveHalvingPruner |
| Visualization | `optuna.visualization.*` (plotly-based) |
| Integration | `OptunaSearchCV`, XGBoost, LightGBM callbacks |
| Multi-objective | Pareto front optimization |

---

#### Lesson 12.05 — Feature Engineering Automation
**File**: `_10_12_05_feature_engineering_automation.md`

| Topics | Subtopics |
|---|---|
| `featuretools` | `EntitySet`, `dfs`, `DeepFeatureSynthesis` |
| `tsfresh` | Automated time series feature extraction |
| `feature_engine` | Sklearn-compatible FE transformers |
| `AutoFeat` | Regression feature generation |
| TPOT | Genetic programming for pipeline optimization |

---

## MODULE 13 — MLOps for ML

**Folder**: `_10_13_mlops_for_ml/`  
**Lesson Count**: 8  
**Learning Order**: 13th  
**Note**: Full MLOps Platform Engineering is Phase 8; this module covers ML-specific experiment management

### Lessons

#### Lesson 13.01 — Experiment Tracking with MLflow
**File**: `_10_13_01_experiment_tracking_mlflow.md`

| Topics | Subtopics |
|---|---|
| MLflow architecture | Tracking Server, Model Registry, Artifacts |
| `mlflow.start_run` | `log_param`, `log_metric`, `log_artifact` |
| Autologging | `mlflow.sklearn.autolog()`, `mlflow.xgboost.autolog()` |
| MLflow UI | Experiment comparison, metric curves |
| Model Registry | Stage transitions (Staging → Production → Archived) |
| `mlflow.pyfunc` | Custom model flavors |

---

#### Lesson 13.02 — Data Versioning with DVC
**File**: `_10_13_02_data_versioning_dvc.md`

| Topics | Subtopics |
|---|---|
| DVC concepts | `.dvc` files, cache, remote storage |
| `dvc init`, `dvc add`, `dvc push/pull` | Core commands |
| Git + DVC workflow | Code in Git, data in DVC |
| `dvc.yaml` | Pipeline definition, stages |
| Metrics tracking | `dvc metrics show`, `dvc plots` |
| Remote storage | S3, GCS, Azure, SSH |

---

#### Lesson 13.03 — Model Serialization and Persistence
**File**: `_10_13_03_model_serialization.md`

| Topics | Subtopics |
|---|---|
| `joblib` | `dump`, `load`, compression levels |
| `pickle` | Limitations, security risks |
| ONNX export | `sklearn-onnx`, `onnxruntime` inference |
| Model versioning | Semantic versioning for models |
| Large model files | Git LFS, DVC for binaries |

---

#### Lesson 13.04 — Sklearn Pipelines for Production
**File**: `_10_13_04_sklearn_pipelines_production.md`

| Topics | Subtopics |
|---|---|
| Production-ready pipeline | Feature engineering + model in one object |
| `pipeline.predict` | Consistent inference interface |
| Online vs batch inference | Single row vs batch of rows |
| Pipeline testing | Unit tests for transform steps |
| Custom transformers | `BaseEstimator` + `TransformerMixin` for production |

---

#### Lesson 13.05 — Model Serving with FastAPI
**File**: `_10_13_05_model_serving_fastapi.md`

| Topics | Subtopics |
|---|---|
| Serving architecture | Load model → API endpoint → JSON prediction |
| Reuses `FastAPI.Endpoints` | (No duplication; reference only) |
| Input validation | Pydantic schema from feature schema |
| Batch inference endpoint | List input, list prediction |
| Health check endpoint | `/health`, `/model/info` |
| Async inference | Background tasks for slow models |

---

#### Lesson 13.06 — Model Monitoring and Drift Detection
**File**: `_10_13_06_model_monitoring_drift.md`

| Topics | Subtopics |
|---|---|
| Types of drift | Data drift, concept drift, label drift, prediction drift |
| Statistical tests | KS test, chi-square, PSI (Population Stability Index) |
| `evidently` | `Report`, `TestSuite`, `DataDriftPreset` |
| `alibi-detect` | `MMDDrift`, `TabularDrift`, `KSDrift` |
| Monitoring dashboards | Grafana + Prometheus integration concept |
| Alerting strategy | Drift threshold → retrain trigger |

---

#### Lesson 13.07 — CI/CD for ML Models
**File**: `_10_13_07_cicd_for_ml.md`

| Topics | Subtopics |
|---|---|
| ML CI/CD principles | Code + data + model versioning together |
| GitHub Actions for ML | `.github/workflows/train.yml` |
| CML (Continuous Machine Learning) | `cml run`, metric reporting in PRs |
| Automated model evaluation | Gate on test metric threshold |
| Model promotion | Staging → Production gate |
| DVC in CI | `dvc repro`, `dvc pull` in pipeline |

---

#### Lesson 13.08 — Feature Stores
**File**: `_10_13_08_feature_stores.md`

| Topics | Subtopics |
|---|---|
| Feature store concept | Centralized feature repository |
| Online vs Offline store | Real-time serving vs batch training |
| `Feast` | `FeatureStore`, `Entity`, `FeatureView` |
| `Hopsworks` | Managed feature store |
| Point-in-time correct joins | Avoiding training-serving skew |
| Feature reuse | Share features across models/teams |

---

## MODULE 14 — Industry Projects

**Folder**: `_10_14_industry_projects/`  
**Lesson Count**: 6  
**Learning Order**: 14th (Capstone)

### Lessons

#### Lesson 14.01 — End-to-End Customer Churn Prediction
**File**: `_10_14_01_customer_churn_prediction.md`

| Topics | Subtopics |
|---|---|
| Business framing | Retention cost vs acquisition cost |
| Dataset | Telco churn dataset |
| Pipeline | EDA → Feature Eng → Imbalance handling → XGBoost → SHAP |
| Deployment | FastAPI endpoint, MLflow tracking |
| Business output | Churn probability scores, risk segments |

---

#### Lesson 14.02 — Credit Risk Scoring System
**File**: `_10_14_02_credit_risk_scoring.md`

| Topics | Subtopics |
|---|---|
| Regulatory context | Basel III, IFRS 9, scorecard methodology |
| Feature engineering | WoE (Weight of Evidence), IV (Information Value) |
| Logistic regression scorecard | Points-based scoring |
| LightGBM challenger model | Comparison with scorecard |
| Fairlearn audit | Demographic parity check |
| Model cards | Documentation for compliance |

---

#### Lesson 14.03 — Demand Forecasting Pipeline
**File**: `_10_14_03_demand_forecasting_pipeline.md`

| Topics | Subtopics |
|---|---|
| Dataset | Retail sales / M5 competition data |
| Time series feature engineering | Lag, rolling, calendar features |
| Models compared | LightGBM, Prophet, ARIMA |
| Hierarchical forecasting | Store → Department → Item level |
| Evaluation | WRMSSE metric (M5) |
| Production pipeline | Scheduled retraining with DVC |

---

#### Lesson 14.04 — Fraud Detection System
**File**: `_10_14_04_fraud_detection_system.md`

| Topics | Subtopics |
|---|---|
| Class imbalance | Severe imbalance (0.1% fraud rate) |
| Features | Transaction velocity, merchant risk, device fingerprint |
| Models | Isolation Forest + XGBoost ensemble |
| Threshold tuning | Cost-sensitive threshold optimization |
| Real-time scoring | FastAPI + Redis feature cache |
| Monitoring | PSI drift detection, daily scoring |

---

#### Lesson 14.05 — Recommendation Engine
**File**: `_10_14_05_recommendation_engine.md`

| Topics | Subtopics |
|---|---|
| Collaborative filtering | User-item matrix, `surprise` library |
| Matrix Factorization | SVD, NMF, `implicit` (ALS) |
| Content-based filtering | TF-IDF item similarity |
| Hybrid system | Weighted blend |
| Cold start problem | Popular items, demographic |
| Evaluation | NDCG, MAP, Precision@k, Recall@k |

---

#### Lesson 14.06 — IoT Anomaly Detection (Bridge to IoT Path)
**File**: `_10_14_06_iot_anomaly_detection.md`

| Topics | Subtopics |
|---|---|
| Sensor data characteristics | Non-stationary, noisy, missing readings |
| Feature engineering | Rolling statistics, FFT features |
| Models | Isolation Forest, LSTM Autoencoder (preview DL) |
| Edge deployment | `scikit-learn` → ONNX → microcontroller |
| Reuses IoT course | ESP32 MQTT streaming data (reference) |
| MLflow tracking | Anomaly model versioning |

---

## Full Folder Structure

```
docs/curriculum/_10_machine_learning/
│
├── _10_01_foundations/
│   ├── _10_01_01_what_is_machine_learning.md
│   ├── _10_01_02_scikit_learn_ecosystem.md
│   ├── _10_01_03_data_splitting_and_leakage.md
│   ├── _10_01_04_bias_variance_tradeoff.md
│   ├── _10_01_05_no_free_lunch_theorem.md
│   └── _10_01_06_ml_environment_setup.md
│
├── _10_02_mathematics_for_ml/
│   ├── _10_02_01_information_theory_for_ml.md
│   ├── _10_02_02_optimization_theory_for_ml.md
│   ├── _10_02_03_linear_algebra_applied_ml.md
│   └── _10_02_04_probabilistic_foundations_ml.md
│
├── _10_03_data_preparation/
│   ├── _10_03_01_exploratory_data_analysis.md
│   ├── _10_03_02_handling_missing_values.md
│   ├── _10_03_03_handling_outliers.md
│   ├── _10_03_04_data_encoding.md
│   ├── _10_03_05_data_scaling_normalization.md
│   ├── _10_03_06_handling_class_imbalance.md
│   └── _10_03_07_data_splitting_strategies.md
│
├── _10_04_feature_engineering/
│   ├── _10_04_01_feature_creation_transformation.md
│   ├── _10_04_02_feature_selection_filter.md
│   ├── _10_04_03_feature_selection_wrapper.md
│   ├── _10_04_04_feature_selection_embedded.md
│   ├── _10_04_05_dimensionality_reduction_unsupervised.md
│   ├── _10_04_06_feature_engineering_time_series.md
│   └── _10_04_07_sklearn_pipelines_columntransformer.md
│
├── _10_05_model_evaluation/
│   ├── _10_05_01_regression_metrics.md
│   ├── _10_05_02_classification_metrics.md
│   ├── _10_05_03_cross_validation_strategies.md
│   ├── _10_05_04_hyperparameter_tuning.md
│   ├── _10_05_05_calibration_threshold_tuning.md
│   └── _10_05_06_model_comparison_statistical_testing.md
│
├── _10_06_supervised_learning/
│   ├── _10_06_01_regression/
│   │   ├── _10_06_01_01_linear_regression_simple_multiple.md
│   │   ├── _10_06_01_02_polynomial_regression.md
│   │   ├── _10_06_01_03_ridge_lasso_elastic_net.md
│   │   ├── _10_06_01_04_decision_tree_regression.md
│   │   ├── _10_06_01_05_random_forest_extratrees_regression.md
│   │   ├── _10_06_01_06_gradient_boosting_regression.md
│   │   ├── _10_06_01_07_xgboost_regression.md
│   │   ├── _10_06_01_08_lightgbm_regression.md
│   │   ├── _10_06_01_09_catboost_regression.md
│   │   ├── _10_06_01_10_support_vector_regression.md
│   │   ├── _10_06_01_11_bayesian_regression.md
│   │   └── _10_06_01_12_sgd_online_learning.md
│   │
│   └── _10_06_02_classification/
│       ├── _10_06_02_01_logistic_regression.md
│       ├── _10_06_02_02_knn_classification.md
│       ├── _10_06_02_03_naive_bayes.md
│       ├── _10_06_02_04_decision_tree_classification.md
│       ├── _10_06_02_05_random_forest_classification.md
│       ├── _10_06_02_06_support_vector_machine.md
│       ├── _10_06_02_07_perceptron_mlp.md
│       ├── _10_06_02_08_gradient_boosting_classification.md
│       ├── _10_06_02_09_xgboost_classification.md
│       ├── _10_06_02_10_lightgbm_classification.md
│       ├── _10_06_02_11_catboost_classification.md
│       ├── _10_06_02_12_adaboost_classification.md
│       ├── _10_06_02_13_sgd_online_classification.md
│       └── _10_06_02_14_multilabel_multioutput.md
│
├── _10_07_unsupervised_learning/
│   ├── _10_07_01_kmeans_clustering.md
│   ├── _10_07_02_dbscan_density_clustering.md
│   ├── _10_07_03_hierarchical_clustering.md
│   ├── _10_07_04_gaussian_mixture_models.md
│   ├── _10_07_05_spectral_clustering.md
│   ├── _10_07_06_pca_applied.md
│   ├── _10_07_07_tsne_umap_applied.md
│   ├── _10_07_08_anomaly_detection.md
│   ├── _10_07_09_association_rule_mining.md
│   └── _10_07_10_topic_modeling_classical.md
│
├── _10_08_semi_supervised_learning/
│   ├── _10_08_01_semi_supervised_foundations.md
│   ├── _10_08_02_self_training.md
│   ├── _10_08_03_label_propagation_spreading.md
│   └── _10_08_04_generative_semi_supervised.md
│
├── _10_09_reinforcement_learning/
│   ├── _10_09_01_rl_foundations_mdp.md
│   ├── _10_09_02_dynamic_programming_methods.md
│   ├── _10_09_03_q_learning_sarsa.md
│   ├── _10_09_04_multi_armed_bandit.md
│   └── _10_09_05_gymnasium_stable_baselines3.md
│
├── _10_10_ensemble_learning/
│   ├── _10_10_01_bagging_random_subspaces.md
│   ├── _10_10_02_boosting_adaboost_gradient.md
│   ├── _10_10_03_xgboost_lightgbm_catboost_deepdive.md
│   ├── _10_10_04_stacking_blending.md
│   ├── _10_10_05_voting_ensembles.md
│   ├── _10_10_06_cascade_ensembles.md
│   └── _10_10_07_ensemble_competition_strategies.md
│
├── _10_11_explainable_ai/
│   ├── _10_11_01_explainability_foundations.md
│   ├── _10_11_02_shap_explainability.md
│   ├── _10_11_03_lime_explainability.md
│   ├── _10_11_04_permutation_partial_dependence.md
│   ├── _10_11_05_counterfactual_explanations.md
│   └── _10_11_06_model_cards_transparency.md
│
├── _10_12_automl/
│   ├── _10_12_01_automl_foundations.md
│   ├── _10_12_02_autosklearn.md
│   ├── _10_12_03_flaml_autogluon.md
│   ├── _10_12_04_optuna.md
│   └── _10_12_05_feature_engineering_automation.md
│
├── _10_13_mlops_for_ml/
│   ├── _10_13_01_experiment_tracking_mlflow.md
│   ├── _10_13_02_data_versioning_dvc.md
│   ├── _10_13_03_model_serialization.md
│   ├── _10_13_04_sklearn_pipelines_production.md
│   ├── _10_13_05_model_serving_fastapi.md
│   ├── _10_13_06_model_monitoring_drift.md
│   ├── _10_13_07_cicd_for_ml.md
│   └── _10_13_08_feature_stores.md
│
└── _10_14_industry_projects/
    ├── _10_14_01_customer_churn_prediction.md
    ├── _10_14_02_credit_risk_scoring.md
    ├── _10_14_03_demand_forecasting_pipeline.md
    ├── _10_14_04_fraud_detection_system.md
    ├── _10_14_05_recommendation_engine.md
    └── _10_14_06_iot_anomaly_detection.md
```

---

## Learning Order (Strict Dependency Chain)

```
01 Foundations
    ↓
02 Mathematics for ML (bridge)
    ↓
03 Data Preparation
    ↓
04 Feature Engineering
    ↓
05 Model Evaluation
    ↓
06 Supervised Learning
    ├── 06.01 Regression (Linear → Tree → Boosting → SVR → Bayesian)
    └── 06.02 Classification (Logistic → KNN → NB → DT → RF → SVM → Boosting)
    ↓
07 Unsupervised Learning
    ↓
08 Semi-Supervised Learning
    ↓
09 Reinforcement Learning (Classical)
    ↓
10 Ensemble Learning (Deep Dive)
    ↓
11 Explainable AI
    ↓
12 AutoML
    ↓
13 MLOps for ML
    ↓
14 Industry Projects (Capstone)
```

---

## Summary Statistics

| Module | Lessons |
|---|---|
| 01 Foundations | 6 |
| 02 Mathematics for ML | 4 |
| 03 Data Preparation | 7 |
| 04 Feature Engineering | 7 |
| 05 Model Evaluation | 6 |
| 06 Supervised Learning — Regression | 12 |
| 06 Supervised Learning — Classification | 14 |
| 07 Unsupervised Learning | 10 |
| 08 Semi-Supervised Learning | 4 |
| 09 Reinforcement Learning | 5 |
| 10 Ensemble Learning | 7 |
| 11 Explainable AI | 6 |
| 12 AutoML | 5 |
| 13 MLOps for ML | 8 |
| 14 Industry Projects | 6 |
| **TOTAL** | **107 lessons** |

---

## Phase 2 Handoff (Deep Learning)

The following nodes are introduced conceptually in Phase 1 and fully implemented in Phase 2:
- Neural networks (MLP classifier — intro only)
- Autoencoders (dimensionality reduction — concept only)
- LSTM for time series (reference in forecasting)
- Knowledge distillation (cascade ensembles — concept only)
- Deep RL (policy gradients, PPO, SAC)
- Deep forest (gcForest — concept bridge)

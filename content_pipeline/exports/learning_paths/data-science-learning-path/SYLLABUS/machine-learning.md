                                                                                               # Machine Learning — Master Syllabus

**Target Role:** ML Engineer / Data Scientist  
**Difficulty Level:** Intermediate → Advanced  
**Estimated Duration:** 80 Hours  
**Prerequisites:** Core Python, Statistics, Engineering Mathematics, NumPy, Pandas  

---

## Study Flow

---

### Module 1 — ML Foundations & Ecosystem

#### 1.1. Introduction to Machine Learning

1. **What is Machine Learning?**
    - **Course Coverage:** 🟢 Covered in Class
    1. Supervised, Unsupervised, Reinforcement Learning
    2. AI vs ML vs Deep Learning hierarchy
    3. ML project lifecycle
    4. Lab Exercise

2. **The Scikit-Learn Ecosystem**
    - **Course Coverage:** 🟢 Covered in Class
    1. Estimator API pattern
    2. Pipelines and transformers
    3. Model selection utilities
    4. Lab Exercise

3. **Data Splitting and Leakage**
    - **Course Coverage:** 🟢 Covered in Class
    1. Train/Validation/Test split
    2. Stratified splits
    3. Data leakage — detection and prevention
    4. Lab Exercise

4. **Data Preprocessing**
    - **Course Coverage:** 🟢 Covered in Class
    1. Handling missing values — imputation strategies
    2. Encoding categorical features (OHE, ordinal, target encoding)
    3. Feature scaling — StandardScaler, MinMaxScaler, RobustScaler
    4. Outlier detection and treatment
    5. Lab Exercise

5. **Feature Engineering Fundamentals**
    - **Course Coverage:** 🟢 Covered in Class
    1. Feature creation and transformation
    2. Interaction features and polynomial features
    3. Feature selection methods — filter, wrapper, embedded
    4. Dimensionality reduction — PCA, LDA
    5. Lab Exercise

---

### Module 2 — Supervised Learning: Regression

#### 2.1. Regression Models

1. **Linear Regression**
    - **Course Coverage:** 🟢 Covered in Class
    1. Ordinary Least Squares
    2. Assumptions of linear regression
    3. Ridge, Lasso, ElasticNet regularization
    4. Polynomial regression
    5. Lab Exercise

2. **Regression Evaluation Metrics**
    - **Course Coverage:** 🟢 Covered in Class
    1. MSE, RMSE, MAE, MAPE, R², Adjusted R²
    2. Residual analysis
    3. Lab Exercise

3. **Decision Tree Regressor**
    - **Course Coverage:** 🟢 Covered in Class
    1. CART algorithm
    2. Splitting criteria, depth, leaf controls
    3. Overfitting and pruning
    4. Lab Exercise

4. **Ensemble Regression**
    - **Course Coverage:** 🟢 Covered in Class
    1. Random Forest Regressor
    2. Gradient Boosting — XGBoost, LightGBM, CatBoost
    3. Stacking and blending
    4. Lab Exercise

---

### Module 3 — Supervised Learning: Classification

#### 3.1. Classification Models

1. **Logistic Regression**
    - **Course Coverage:** 🟢 Covered in Class
    1. Sigmoid function and decision boundary
    2. Multinomial logistic regression
    3. Regularization — L1, L2
    4. Lab Exercise

2. **Classification Evaluation Metrics**
    - **Course Coverage:** 🟢 Covered in Class
    1. Confusion matrix
    2. Precision, Recall, F1-Score
    3. ROC-AUC, PR Curve
    4. Handling class imbalance — SMOTE, class_weight
    5. Lab Exercise

3. **Support Vector Machines**
    - **Course Coverage:** 🟢 Covered in Class
    1. Maximum margin classifier
    2. Kernel trick — RBF, polynomial
    3. SVC vs SVR
    4. Lab Exercise

4. **K-Nearest Neighbours**
    - **Course Coverage:** 🟢 Covered in Class
    1. Distance metrics — Euclidean, Manhattan, Cosine
    2. Choosing optimal K
    3. KD-Tree and Ball Tree
    4. Lab Exercise

5. **Naive Bayes Classifiers**
    - **Course Coverage:** 🟢 Covered in Class
    1. Gaussian, Multinomial, Bernoulli variants
    2. Laplace smoothing
    3. Text classification use case
    4. Lab Exercise

6. **Ensemble Classification**
    - **Course Coverage:** 🟢 Covered in Class
    1. Random Forest Classifier
    2. Gradient Boosting — XGBoost, LightGBM
    3. Voting and Bagging ensembles
    4. Lab Exercise

---

### Module 4 — Unsupervised Learning

#### 4.1. Clustering

1. **K-Means Clustering**
    - **Course Coverage:** 🟢 Covered in Class
    1. K-Means++ initialization
    2. Elbow method and silhouette score
    3. Mini-batch K-Means
    4. Lab Exercise

2. **Hierarchical Clustering**
    - **Course Coverage:** 🟢 Covered in Class
    1. Agglomerative vs Divisive
    2. Dendrograms and linkage methods
    3. Lab Exercise

3. **Density-Based Clustering**
    - **Course Coverage:** 🟢 Covered in Class
    1. DBSCAN — eps, min_samples
    2. Handling noise and outliers
    3. HDBSCAN overview
    4. Lab Exercise

4. **Dimensionality Reduction**
    - **Course Coverage:** 🟢 Covered in Class
    1. PCA — principal components and variance explained
    2. t-SNE for visualization
    3. UMAP
    4. Lab Exercise

5. **Anomaly Detection**
    - **Course Coverage:** 🟢 Covered in Class
    1. Isolation Forest
    2. One-Class SVM
    3. Autoencoder-based anomaly detection
    4. Lab Exercise

---

### Module 5 — Model Selection, Tuning & Validation

#### 5.1. Hyperparameter Tuning

1. **Cross-Validation Strategies**
    - **Course Coverage:** 🟢 Covered in Class
    1. K-Fold, Stratified K-Fold, Leave-One-Out
    2. TimeSeriesSplit
    3. Lab Exercise

2. **Hyperparameter Search**
    - **Course Coverage:** 🟢 Covered in Class
    1. GridSearchCV and RandomizedSearchCV
    2. Bayesian optimization — Optuna
    3. Successive halving
    4. Lab Exercise

3. **Bias-Variance Tradeoff**
    - **Course Coverage:** 🟢 Covered in Class
    1. Overfitting vs underfitting
    2. Learning curves
    3. Regularization strategies
    4. Lab Exercise

4. **Model Explainability**
    - **Course Coverage:** 🟢 Covered in Class
    1. SHAP values
    2. LIME
    3. Permutation importance
    4. Partial dependence plots
    5. Lab Exercise

---

### Module 6 — Time Series & Specialized Topics

#### 6.1. Time Series Analysis

1. **Time Series Foundations**
    - **Course Coverage:** 🟢 Covered in Class
    1. Trend, seasonality, stationarity
    2. ACF and PACF
    3. ADF test
    4. Lab Exercise

2. **Classical Forecasting Models**
    - **Course Coverage:** 🟢 Covered in Class
    1. ARIMA and SARIMA
    2. Prophet
    3. Exponential smoothing
    4. Lab Exercise

3. **ML-Based Forecasting**
    - **Course Coverage:** 🟡 Optional Discussion
    1. Feature engineering for time series
    2. XGBoost for forecasting
    3. LSTM overview
    4. Lab Exercise

---

### Module 7 — ML Pipelines & Production

#### 7.1. Production-Ready ML

1. **Scikit-Learn Pipelines**
    - **Course Coverage:** 🟢 Covered in Class
    1. ColumnTransformer
    2. Pipeline with cross-validation
    3. Custom transformers
    4. Lab Exercise

2. **Model Serialization**
    - **Course Coverage:** 🟢 Covered in Class
    1. Joblib and Pickle
    2. ONNX format
    3. Model versioning
    4. Lab Exercise

3. **ML API with FastAPI**
    - **Course Coverage:** 🟢 Covered in Class
    1. Serving predictions via REST API
    2. Input validation with Pydantic
    3. Async prediction endpoints
    4. Lab Exercise

4. **Capstone — End-to-End ML Project**
    - **Course Coverage:** 🟢 Covered in Class
    1. Dataset selection and EDA
    2. Feature engineering pipeline
    3. Model training, tuning, evaluation
    4. API deployment
    5. Lab Exercise

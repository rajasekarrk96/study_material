# Enterprise Data Science, AI, & Agent Engineering Master Syllabus

## Executive Overview & Architectural Strategy

This master syllabus defines the enterprise learning path for **Data Science, Artificial Intelligence, Large Language Models (LLMs), and Autonomous Agent Engineering**.

### Reusable Platform Core Courses
The Enterprise Learning OS maintains a pre-authored foundation of core courses. This syllabus **strictly reuses** these modules as prerequisites to eliminate redundancy:

- **✓ Git Course**: Repository management, branching, versioning.
- **✓ Python Course**: Variables, control flow, functions, OOP, exceptions, file I/O.
- **✓ MySQL Course**: Relational schema, SQL queries, joins, indexes, transactions.
- **✓ HTML Course**: Web document structure, DOM elements.
- **✓ CSS Course**: Styling, layouts, UI components.
- **✓ JavaScript Course**: Async execution, ES6+, Web APIs.
- **✓ Flask Course**: Lightweight WSGI microframework.
- **✓ FastAPI Course**: Asynchronous ASGI RESTful APIs, Pydantic, OpenAPI.

---

# Course 1: Mathematics, Statistics, & Foundations for Data Science

## Module 1.1: Linear Algebra & Matrix Calculus
- **Required Previous Courses**: Python (Functions, Lists, Loops)
- **Reusable Dependencies**: `Python.Functions`, `Python.Lists`, `Python.Math`
- **Skills Gained**: Vector spaces, matrix transformations, eigenvalues, partial differentiation, gradient vectors.
- **Industry Usage**: Foundation for neural network weight matrices, PCA dimension reduction, and graphics embeddings.

### Lessons & Topics
1. **Lesson 1.1.1: Vectors, Matrices, & Vector Spaces**
   - Topics: Vector Operations, Dot Product, Cross Product, Matrix Multiplication, Matrix Transposition, Vector Spaces, Subspaces, Span, Linear Independence.
2. **Lesson 1.1.2: Matrix Inversion, Determinants, & Systems of Equations**
   - Topics: Determinants, Matrix Inverse, Rank of a Matrix, Gaussian Elimination, Solving Systems of Linear Equations $Ax = b$, Condition Numbers.
3. **Lesson 1.1.3: Eigenvalues, Eigenvectors, & Matrix Decompositions**
   - Topics: Eigenvalues and Eigenvectors, Characteristic Equation, Eigendecomposition, Singular Value Decomposition (SVD), Principal Component Analysis (PCA) Math.
4. **Lesson 1.1.4: Multivariable Calculus & Gradient Vectors**
   - Topics: Partial Derivatives, Directional Derivatives, Gradient Vector $\nabla f$, Hessian Matrix, Jacobian Matrix, Chain Rule in Multivariable Calculus, Taylor Series Expansion.

---

## Module 1.2: Probability Theory & Random Variables
- **Required Previous Courses**: Python (Functions, Control Flow)
- **Reusable Dependencies**: `Python.Functions`, `Python.ControlFlow`
- **Skills Gained**: Probability rules, Bayes' Theorem, discrete & continuous probability distributions, joint distributions.
- **Industry Usage**: Risk modeling, A/B testing inference, Naive Bayes classification, generative model probabilities.

### Lessons & Topics
1. **Lesson 1.2.1: Probability Fundamentals & Axioms**
   - Topics: Sample Spaces, Events, Probability Axioms, Conditional Probability, Independence, Bayes' Theorem, Law of Total Probability.
2. **Lesson 1.2.2: Discrete & Continuous Probability Distributions**
   - Topics: Random Variables, PMF, PDF, CDF, Bernoulli, Binomial, Poisson, Uniform, Gaussian (Normal), Exponential, Beta, Gamma Distributions.
3. **Lesson 1.2.3: Joint, Marginal, & Conditional Distributions**
   - Topics: Joint PDFs, Marginal Probabilities, Conditional Expectations, Covariance, Correlation, Covariance Matrix, Law of Large Numbers (LLN), Central Limit Theorem (CLT).

---

## Module 1.3: Inferential Statistics & Hypothesis Testing
- **Required Previous Courses**: Course 1 (Module 1.2)
- **Reusable Dependencies**: `Course1.Module1.2`
- **Skills Gained**: Hypothesis testing, $p$-value analysis, confidence intervals, ANOVA, non-parametric statistical tests.
- **Industry Usage**: Product feature validation, A/B/n experiment analysis, medical research trial evaluation.

### Lessons & Topics
1. **Lesson 1.3.1: Estimation & Confidence Intervals**
   - Topics: Point Estimation, Bias, Variance, Mean Squared Error (MSE), Maximum Likelihood Estimation (MLE), Confidence Intervals for Means and Proportions.
2. **Lesson 1.3.2: Parametric Hypothesis Testing**
   - Topics: Null and Alternative Hypotheses, Type I & Type II Errors, Significance Level ($\alpha$), $p$-values, One-Sample and Two-Sample $t$-Tests, Paired $t$-Test, $z$-Test.
3. **Lesson 1.3.3: Analysis of Variance (ANOVA) & Chi-Square Tests**
   - Topics: One-Way ANOVA, Two-Way ANOVA, Post-Hoc Tests (Tukey HSD), Chi-Square Goodness-of-Fit Test, Chi-Square Test of Independence.
4. **Lesson 1.3.4: Non-Parametric Statistical Methods**
   - Topics: Mann-Whitney U Test, Wilcoxon Signed-Rank Test, Kruskal-Wallis Test, Spearman Rank Correlation, Bootstrapping, Resampling Techniques.

---

# Course 2: Data Manipulation & Exploratory Data Analysis (NumPy & Pandas)

## Module 2.1: Numerical Computing with NumPy
- **Required Previous Courses**: Python (Variables, Lists, Loops, Functions)
- **Reusable Dependencies**: `Python.Variables`, `Python.Lists`, `Python.Loops`, `Python.Functions`
- **Skills Gained**: Multi-dimensional ndarray operations, vectorization, broadcasting, linear algebra in NumPy.
- **Industry Usage**: High-performance numerical computations, image array representations, feature matrix prep.

### Lessons & Topics
1. **Lesson 2.1.1: NumPy Ndarray Architecture & Creation**
   - Topics: `np.ndarray` Data Structure, Array Creation (`zeros`, `ones`, `arange`, `linspace`), Data Types (`dtype`), Memory Layout (C-contiguous vs Fortran-contiguous).
2. **Lesson 2.1.2: Array Indexing, Slicing, & Reshaping**
   - Topics: Multi-dimensional Slicing, Fancy Indexing, Boolean Masking, `reshape`, `ravel`, `flatten`, `transpose`, `swapaxes`.
3. **Lesson 2.1.3: Vectorized Operations & Broadcasting**
   - Topics: Element-wise Operations, Universal Functions (ufuncs), Broadcasting Rules, Vectorized Linear Algebra (`np.dot`, `np.matmul`, `@` operator, `np.linalg.inv`, `np.linalg.svd`).
4. **Lesson 2.1.4: Random Sampling & Universal Math Aggregations**
   - Topics: `np.random` Generator, Seed Reproducibility, Normal/Uniform Distributions, Aggregations (`sum`, `mean`, `std`, `var`, `min`, `max`, `argmin`, `argmax`, `axis` parameters).

---

## Module 2.2: Data Analysis & Manipulation with Pandas
- **Required Previous Courses**: Course 2 (Module 2.1), Python (File Handling, Exception Handling)
- **Reusable Dependencies**: `Course2.Module2.1`, `Python.FileHandling`, `Python.ExceptionHandling`
- **Skills Gained**: DataFrames, Data Series, indexing (`loc`/`iloc`), missing data handling, group aggregation, merging.
- **Industry Usage**: ETL pipeline construction, tabular dataset wrangling, financial data preprocessing.

### Lessons & Topics
1. **Lesson 2.2.1: Pandas Series & DataFrame Core Mechanics**
   - Topics: Series & DataFrame Structures, Indexing & Selection (`loc`, `iloc`), Reindexing, Axis Management, Data Ingestion (CSV, JSON, Excel, Parquet, Feather).
2. **Lesson 2.2.2: Data Cleaning, Missing Values, & Transformation**
   - Topics: Handling Null Values (`isna`, `fillna`, `dropna`), Duplicate Removal, String Methods (`.str`), Data Type Casting (`astype`), Categorical Data Types.
3. **Lesson 2.2.3: GroupBy, Aggregations, & Pivot Tables**
   - Topics: Split-Apply-Combine Strategy, `groupby()`, Custom Aggregations (`agg`), Transforming Data (`transform`), `apply()`, Pivot Tables (`pivot_table`), Crosstabulation (`crosstab`).
4. **Lesson 2.2.4: Merging, Joining, & Time-Series Pandas**
   - Topics: `concat()`, `merge()` (Inner, Outer, Left, Right, Cross Joins), MultiIndex DataFrames, `DatetimeIndex`, Resampling (`resample`), Rolling Windows (`rolling`), Shift/Lag Operations.

---

# Course 3: Data Visualization & Interactive Dashboards

## Module 3.1: Static Visualization with Matplotlib & Seaborn
- **Required Previous Courses**: Course 2 (Module 2.2)
- **Reusable Dependencies**: `Course2.Module2.2`
- **Skills Gained**: Figure & Axes hierarchy, statistical distribution plots, heatmaps, categorical plots.
- **Industry Usage**: Exploratory analysis reports, academic papers, executive metric charts.

### Lessons & Topics
1. **Lesson 3.1.1: Matplotlib Architecture & Customization**
   - Topics: Object-Oriented Interface (`fig`, `ax`), Line Plots, Scatter Plots, Bar Charts, Histograms, Subplots Layouts, Spines, Grid lines, Annotations, Exporting High-Res Visuals.
2. **Lesson 3.1.2: Statistical Visualization with Seaborn**
   - Topics: Distribution Plots (`displot`, `kdeplot`, `ecdfplot`), Categorical Plots (`catplot`, `boxplot`, `violinplot`, `stripplot`), Relationship Plots (`relplot`, `pairplot`).
3. **Lesson 3.1.3: Matrix Plots & Color Theory**
   - Topics: Correlation Matrices, Heatmaps (`heatmap`), Cluster Maps (`clustermap`), Diverging vs Sequential Color Maps, Colorblind-Friendly Palettes.

---

## Module 3.2: Interactive Dashboards with Plotly & Dash
- **Required Previous Courses**: Course 3 (Module 3.1)
- **Reusable Dependencies**: `Course3.Module3.1`
- **Skills Gained**: Interactive charts, 3D plots, geo-spatial maps, web dashboard deployment.
- **Industry Usage**: Live operational dashboards, client analytics portals, interactive ML feature evaluation.

### Lessons & Topics
1. **Lesson 3.2.1: Interactive Plotly Express & Graph Objects**
   - Topics: Plotly Express API, Hover Tooltips, Zooming/Panning Controls, 3D Scatter Plots, Choropleth Geo Maps, Sunburst & Treemap Visuals.
2. **Lesson 3.2.2: Building Web Dashboards with Dash / Streamlit**
   - Topics: Dash Layout Components, Callbacks, State Management, Streamlit Quick Apps, Interactive Widgets, Live Telemetry Visualizations.

---

# Course 4: SQL & Database Querying for Data Science

## Module 4.1: Advanced SQL for Data Analysis
- **Required Previous Courses**: MySQL Course (All Modules)
- **Reusable Dependencies**: `MySQL.Schema`, `MySQL.Queries`, `MySQL.Joins`, `MySQL.Indexes`
- **Skills Gained**: Window functions, Common Table Expressions (CTEs), analytical aggregations, performance profiling.
- **Industry Usage**: Extracting data from enterprise data warehouses (Snowflake, BigQuery, Redshift).

### Lessons & Topics
1. **Lesson 4.1.1: Analytical Window Functions**
   - Topics: `OVER()` Clause, `PARTITION BY`, `ORDER BY`, Ranking Functions (`ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`), Value Functions (`LAG`, `LEAD`, `FIRST_VALUE`, `LAST_VALUE`), Running Totals.
2. **Lesson 4.1.2: Common Table Expressions (CTEs) & Subqueries**
   - Topics: WITH Clause (Non-Recursive CTEs), Recursive CTEs for Hierarchical Data, Correlated Subqueries, Subqueries in SELECT, FROM, WHERE Clauses.
3. **Lesson 4.1.3: Advanced Data Transformation in SQL**
   - Topics: Pivoting & Unpivoting Rows/Columns, Conditional Aggregations (`CASE WHEN`), String Manipulation, Date/Time Analytics (`DATE_TRUNC`, `EXTRACT`, `INTERVAL`).
4. **Lesson 4.1.4: Query Optimization & Execution Plans**
   - Topics: `EXPLAIN ANALYZE`, Index Optimization (B-Tree, Hash, GIN), Partitioning Strategies, Query Plan Diagnostics, Reducing Table Scans.

---

# Course 5: Classical Machine Learning & Statistical Modeling

## Module 5.1: Data Preprocessing, Feature Engineering, & EDA
- **Required Previous Courses**: Course 2 (Module 2.2), Course 3 (Module 3.1)
- **Reusable Dependencies**: `Course2.Module2.2`, `Course3.Module3.1`
- **Skills Gained**: Feature scaling, categorical encoding, missing value imputation, outlier detection, leakage prevention.
- **Industry Usage**: ML pipeline preprocessing, tabular dataset preparation.

### Lessons & Topics
1. **Lesson 5.1.1: Exploratory Data Analysis (EDA) Frameworks**
   - Topics: Automated EDA, Univariate Analysis, Bivariate Analysis, Multivariate Analysis, Feature Distribution Analysis, Target Variable Profiling.
2. **Lesson 5.1.2: Feature Scaling & Encoding Techniques**
   - Topics: StandardScaler, MinMaxScaler, RobustScaler, Normalizer, One-Hot Encoding, Ordinal Encoding, Target Encoding, Frequency Encoding, High-Cardinality Handling.
3. **Lesson 5.1.3: Missing Data Imputation & Outlier Handling**
   - Topics: Mean/Median/Mode Imputation, KNN Imputer, Iterative Imputer (MICE), Outlier Detection (Z-Score, IQR, Isolation Forest), Trimming vs Winsorization.
4. **Lesson 5.1.4: Feature Engineering & Data Leakage**
   - Topics: Polynomial Features, Interaction Terms, Binning/Discretization, Box-Cox & Yeo-Johnson Power Transforms, Identifying and Preventing Data Leakage in Pipelines.

---

## Module 5.2: Supervised Learning — Regression Algorithms
- **Required Previous Courses**: Course 1 (Module 1.1, 1.3), Course 5 (Module 5.1)
- **Reusable Dependencies**: `Course1.Module1.1`, `Course1.Module1.3`, `Course5.Module5.1`
- **Skills Gained**: Linear regression, Regularization (Ridge, Lasso, ElasticNet), Polynomial regression, Evaluation metrics.
- **Industry Usage**: Price forecasting, continuous value prediction, risk scoring.

### Lessons & Topics
1. **Lesson 5.2.1: Simple & Multiple Linear Regression**
   - Topics: Ordinary Least Squares (OLS) Formulation, Normal Equation, Cost Function (MSE), Gradient Descent Optimization, Assumptions of Linear Regression (Linearity, Homoscedasticity, Normality, Multicollinearity / VIF).
2. **Lesson 5.2.2: Regularized Regression (Ridge, Lasso, ElasticNet)**
   - Topics: L2 Regularization (Ridge), L1 Regularization (Lasso & Feature Selection), ElasticNet (L1 + L2 Mix), Hyperparameter Tuning ($\alpha$ / $\lambda$).
3. **Lesson 5.2.3: Non-Linear Regression & Splines**
   - Topics: Polynomial Regression, Step Functions, Generalized Additive Models (GAMs), Regression Evaluation Metrics ($R^2$, Adjusted $R^2$, MAE, MSE, RMSE, MAPE).

---

## Module 5.3: Supervised Learning — Classification Algorithms
- **Required Previous Courses**: Course 5 (Module 5.2)
- **Reusable Dependencies**: `Course5.Module5.2`
- **Skills Gained**: Logistic regression, K-NN, Naive Bayes, Support Vector Machines (SVM), Decision Trees, Confusion matrices.
- **Industry Usage**: Churn prediction, spam filtering, credit default classification.

### Lessons & Topics
1. **Lesson 5.3.1: Logistic Regression & Odds Ratios**
   - Topics: Sigmoid Function, Log-Odds (Logit), Binary & Multinomial Cross-Entropy Loss, Decision Boundaries, Multiclass Classification (One-vs-Rest, One-vs-One).
2. **Lesson 5.3.2: K-Nearest Neighbors (K-NN) & Naive Bayes**
   - Topics: Distance Metrics (Euclidean, Manhattan, Minkowski, Cosine), K Selection, Naive Bayes Classifier (Gaussian, Multinomial, Bernoulli NB), Laplace Smoothing.
3. **Lesson 5.3.3: Support Vector Machines (SVM)**
   - Topics: Hyperplane Margin Maximization, Hard vs Soft Margin (C parameter), Kernel Trick (Linear, Polynomial, RBF, Sigmoid Kernels), Support Vector Regressor (SVR).
4. **Lesson 5.3.4: Decision Trees & Information Theory**
   - Topics: Decision Tree Classifier/Regressor, Entropy, Information Gain, Gini Impurity, Variance Reduction, Pruning (Cost-Complexity Pruning $\alpha$).

---

## Module 5.4: Ensemble Methods & Advanced Tree Algorithms
- **Required Previous Courses**: Course 5 (Module 5.3)
- **Reusable Dependencies**: `Course5.Module5.3`
- **Skills Gained**: Bagging, Random Forests, Boosting (AdaBoost, Gradient Boosting, XGBoost, LightGBM, CatBoost), Stacking.
- **Industry Usage**: Kaggle-winning tabular models, credit scoring, fraud detection.

### Lessons & Topics
1. **Lesson 5.4.1: Ensemble Principles & Bagging**
   - Topics: Wisdom of the Crowd, Bias-Variance Trade-Off in Ensembles, Bootstrap Aggregating (Bagging), Out-of-Bag (OOB) Error Estimation.
2. **Lesson 5.4.2: Random Forests**
   - Topics: Random Forest Architecture, Feature Subsampling (`max_features`), Feature Importance (Gini Importance, Permutation Importance), Hyperparameter Tuning.
3. **Lesson 5.4.3: Gradient Boosting Machines (GBM) & AdaBoost**
   - Topics: Adaptive Boosting (AdaBoost) Principles, Gradient Boosting Architecture, Loss Functions, Learning Rate, Shrinkage, Subsampling.
4. **Lesson 5.4.4: High-Performance Boosting Frameworks (XGBoost, LightGBM, CatBoost)**
   - Topics: XGBoost (Second-Order Gradient, Regularization, Tree Pruning), LightGBM (Leaf-wise Tree Growth, GOSS, EFB), CatBoost (Ordered Boosting, Native Categorical Handling).
5. **Lesson 5.4.5: Stacking & Blending Ensembles**
   - Topics: Meta-Learners, Stacked Generalization, Multi-Layer Ensembles, Blending Datasets without Leakage.

---

## Module 5.5: Unsupervised Learning — Clustering & Dimensionality Reduction
- **Required Previous Courses**: Course 1 (Module 1.1), Course 5 (Module 5.1)
- **Reusable Dependencies**: `Course1.Module1.1`, `Course5.Module5.1`
- **Skills Gained**: K-Means, Hierarchical clustering, DBSCAN, PCA, t-SNE, UMAP.
- **Industry Usage**: Customer segmentation, anomaly detection, high-dimensional visualization.

### Lessons & Topics
1. **Lesson 5.5.1: Partitioning & Density-Based Clustering**
   - Topics: K-Means Clustering, K-Means++, Elbow Method, Silhouette Score, DBSCAN (Density-Based Spatial Clustering of Applications with Noise), HDBSCAN, Mean Shift.
2. **Lesson 5.5.2: Hierarchical Clustering & Gaussian Mixture Models**
   - Topics: Agglomerative Hierarchical Clustering, Dendrograms, Linkage Criteria (Single, Complete, Average, Ward), Gaussian Mixture Models (GMM), Expectation-Maximization (EM) Algorithm.
3. **Lesson 5.5.3: Linear Dimensionality Reduction (PCA & Truncated SVD)**
   - Topics: Principal Component Analysis (PCA) Variance Maximization, Scree Plots, Cumulative Explained Variance, Truncated SVD for Sparse Data.
4. **Lesson 5.5.4: Non-Linear Dimensionality Reduction (t-SNE & UMAP)**
   - Topics: t-Distributed Stochastic Neighbor Embedding (t-SNE), Perplexity Hyperparameter, Uniform Manifold Approximation and Projection (UMAP), Local vs Global Structure Preservation.

---

## Module 5.6: Model Evaluation, Validation, & Scikit-Learn Pipelines
- **Required Previous Courses**: Course 5 (Modules 5.2 - 5.5)
- **Reusable Dependencies**: `Course5.Module5.2`, `Course5.Module5.3`, `Course5.Module5.4`, `Course5.Module5.5`
- **Skills Gained**: Cross-validation, Hyperparameter tuning (GridSearch, RandomizedSearch, Optuna), Metrics, Scikit-Learn Pipelines.
- **Industry Usage**: Production ML pipeline development, rigorous validation frameworks.

### Lessons & Topics
1. **Lesson 5.6.1: Cross-Validation & Resampling Strategies**
   - Topics: K-Fold CV, Stratified K-Fold CV, TimeSeries Split, GroupKFold, Leave-One-Out CV (LOOCV), Data Leakage Avoidance in Resampling.
2. **Lesson 5.6.2: Comprehensive Classification & Regression Metrics**
   - Topics: Confusion Matrix, Precision, Recall, $F_1$-Score, $F_\beta$-Score, ROC Curve, AUC-ROC, Precision-Recall Curve (PR-AUC), Log-Loss, Balanced Accuracy.
3. **Lesson 5.6.3: Hyperparameter Optimization Frameworks**
   - Topics: Grid Search CV, Randomized Search CV, Bayesian Optimization (Optuna, Hyperopt), Tree-structured Parzen Estimator (TPE).
4. **Lesson 5.6.4: Scikit-Learn Pipeline & ColumnTransformer Architecture**
   - Topics: Custom Transformers (`BaseEstimator`, `TransformerMixin`), `Pipeline`, `FeatureUnion`, `ColumnTransformer`, Serializing Pipelines (`joblib`, `pickle`).

---

# Course 6: Advanced Machine Learning, Time Series, & Recommendation Systems

## Module 6.1: Time Series Forecasting & Sequential Data
- **Required Previous Courses**: Course 5 (Module 5.2, 5.6)
- **Reusable Dependencies**: `Course5.Module5.2`, `Course5.Module5.6`
- **Skills Gained**: Stationarity, ARIMA, SARIMAX, Prophet, Deep Learning for Time Series, Evaluation metrics (MAE, RMSE, MAPE).
- **Industry Usage**: Sales forecasting, stock market prediction, demand forecasting, IoT anomaly detection.

### Lessons & Topics
1. **Lesson 6.1.1: Time Series Decompositions & Stationarity**
   - Topics: Trend, Seasonality, Residual Components, Additive vs Multiplicative Models, Stationarity Tests (Augmented Dickey-Fuller Test, KPSS Test), Differencing, Autocorrelation (ACF) & Partial Autocorrelation (PACF).
2. **Lesson 6.1.2: Classical Statistical Forecasting (ARIMA / SARIMAX)**
   - Topics: Auto-Regressive (AR) Models, Moving Average (MA) Models, ARMA, ARIMA $(p,d,q)$, Seasonal ARIMA (SARIMAX with Exogenous Variables), Auto-ARIMA Tuning.
3. **Lesson 6.1.3: Scalable & ML-Based Time Series Forecasting**
   - Topics: Facebook Prophet Architecture, XGBoost/LightGBM for Time Series (Lag Features, Rolling Window Features), Hierarchical Time Series Forecasting, NeuralProphet.

---

## Module 6.2: Recommendation Systems Engine Architecture
- **Required Previous Courses**: Course 5 (Module 5.3, 5.5)
- **Reusable Dependencies**: `Course5.Module5.3`, `Course5.Module5.5`
- **Skills Gained**: Content-based filtering, Collaborative filtering, Matrix Factorization (SVD), Two-Tower Neural Recommenders.
- **Industry Usage**: E-commerce product recommendations, streaming service content suggestions (Netflix/Spotify).

### Lessons & Topics
1. **Lesson 6.2.1: Content-Based Filtering Systems**
   - Topics: Item Profiles, User Profiles, TF-IDF Vectorization, Cosine Similarity Recommendations, Cold-Start Problem in Content-Based Systems.
2. **Lesson 6.2.2: Collaborative Filtering Methods**
   - Topics: User-Item Interaction Matrix, User-Based Collaborative Filtering, Item-Based Collaborative Filtering, Similarity Metrics, Memory-Based Limitations.
3. **Lesson 6.2.3: Matrix Factorization & Deep Learning Recommenders**
   - Topics: Singular Value Decomposition (SVD), Alternating Least Squares (ALS), Implicit Feedback, Deep Learning Two-Tower Recommender Architectures, Evaluation Metrics (Precision@K, Recall@K, MAP@K, NDCG).

---

# Course 7: Deep Learning Foundations & Neural Networks (TensorFlow & PyTorch)

## Module 7.1: Deep Learning Fundamentals & Perceptrons
- **Required Previous Courses**: Course 1 (Module 1.1), Course 5 (Module 5.6)
- **Reusable Dependencies**: `Course1.Module1.1`, `Course5.Module5.6`
- **Skills Gained**: Artificial Neural Networks (ANN), Activation Functions, Backpropagation, Gradient Descent Variants.
- **Industry Usage**: Core building block for vision, audio, text, and multimodal AI models.

### Lessons & Topics
1. **Lesson 7.1.1: Biological vs Artificial Neurons & The Perceptron**
   - Topics: Linear Threshold Units, Single-Layer Perceptron, XOR Problem, Multi-Layer Perceptron (MLP) Architecture, Forward Propagation.
2. **Lesson 7.1.2: Activation Functions & Non-Linearity**
   - Topics: Sigmoid, Tanh, ReLU, Leaky ReLU, ELU, GELU, Swish, Softmax, Vanishing & Exploding Gradient Problems.
3. **Lesson 7.1.3: Backpropagation & Computational Graphs**
   - Topics: Chain Rule Computations, Computational Graphs, Partial Derivatives of Loss, Automatic Differentiation, Weights & Biases Initialization (Xavier/Glorot, He Initialization).
4. **Lesson 7.1.4: Optimization Algorithms & Regularization**
   - Topics: Stochastic Gradient Descent (SGD) with Momentum, RMSprop, Adam, AdamW, Learning Rate Schedules (Cosine Annealing, Warmup), L1/L2 Weight Decay, Dropout, Batch Normalization, Layer Normalization.

---

## Module 7.2: PyTorch Framework Deep Dive
- **Required Previous Courses**: Course 7 (Module 7.1), Python (OOP)
- **Reusable Dependencies**: `Course7.Module7.1`, `Python.OOP`
- **Skills Gained**: PyTorch Tensors, `nn.Module`, `Dataset`, `DataLoader`, Custom Training Loops, GPU Acceleration (`cuda`/`mps`).
- **Industry Usage**: AI Research engineering, model deployment in PyTorch environments.

### Lessons & Topics
1. **Lesson 7.2.1: PyTorch Tensors & Autograd Engine**
   - Topics: PyTorch Tensors, Tensor Operations, GPU Memory Allocation (`.to('cuda')`), `requires_grad=True`, `backward()`, Computational Graph Inspection.
2. **Lesson 7.2.2: Building Models with `torch.nn.Module`**
   - Topics: `nn.Module` Subclassing, `nn.Linear`, `nn.Sequential`, Loss Functions (`nn.MSELoss`, `nn.CrossEntropyLoss`), Optimizers (`torch.optim`).
3. **Lesson 7.2.3: Data Ingestion with `Dataset` & `DataLoader`**
   - Topics: Custom `torch.utils.data.Dataset`, `DataLoader` (Batch Size, Shuffling, Parallel Multiprocessing Workers), Data Transformations (`torchvision.transforms`).
4. **Lesson 7.2.4: Writing Custom PyTorch Training Loops**
   - Topics: Training Loop Lifecycle, Validation Loop, Gradient Zeroing (`optimizer.zero_grad()`), Model Evaluation Mode (`model.eval()`, `torch.no_grad()`), Checkpointing & Model Saving (`torch.save`, `torch.load`).

---

## Module 7.3: TensorFlow 2.x & Keras Deep Dive
- **Required Previous Courses**: Course 7 (Module 7.1)
- **Reusable Dependencies**: `Course7.Module7.1`
- **Skills Gained**: Keras Sequential/Functional API, `tf.data` Pipeline, Custom Layers/Losses, TensorBoard.
- **Industry Usage**: Enterprise production deep learning, mobile/edge deployment.

### Lessons & Topics
1. **Lesson 7.3.1: Keras Sequential & Functional APIs**
   - Topics: `tf.keras.Sequential`, Keras Functional API (Complex Topologies, Multi-Input/Multi-Output Models), Model Summary & Compilation.
2. **Lesson 7.3.2: High-Performance Data Pipelines (`tf.data`)**
   - Topics: `tf.data.Dataset.from_tensor_slices`, Mapping, Batching, Prefetching (`tf.data.AUTOTUNE`), Parallel Processing, TFRecords Format.
3. **Lesson 7.3.3: Callbacks, TensorBoard, & Custom Training**
   - Topics: Keras Callbacks (`EarlyStopping`, `ModelCheckpoint`, `ReduceLROnPlateau`), TensorBoard Profiling, `tf.GradientTape` Custom Training Loops.

---

# Course 8: Modern Computer Vision & Visual Intelligence

## Module 8.1: Convolutional Neural Networks (CNNs) & Image Processing
- **Required Previous Courses**: Course 7 (Module 7.2 or 7.3), OpenCV basics
- **Reusable Dependencies**: `Course7.Module7.2`
- **Skills Gained**: Image convolutions, pooling, CNN architectures (ResNet, EfficientNet), Transfer Learning, OpenCV.
- **Industry Usage**: Automated visual inspection, medical diagnostics, autonomous driving.

### Lessons & Topics
1. **Lesson 8.1.1: Image Processing Fundamentals with OpenCV**
   - Topics: Image Matrix Representation, Color Spaces (RGB, BGR, HSV, LAB), Thresholding, Edge Detection (Canny, Sobel), Morphological Operations (Erosion, Dilation), Contours.
2. **Lesson 8.1.2: Convolutional Layer Mechanics**
   - Topics: Convolution Operation, Filters/Kernels, Stride, Padding (Valid vs Same), Feature Maps, Pooling Layers (Max Pooling, Average Pooling), Global Average Pooling.
3. **Lesson 8.1.3: Classic & Modern CNN Architectures**
   - Topics: LeNet-5, AlexNet, VGG, Inception/GoogLeNet, ResNet (Residual Connections & Skip Links), DenseNet, MobileNet, EfficientNet.
4. **Lesson 8.1.4: Transfer Learning & Fine-Tuning**
   - Topics: Pre-trained Weights (ImageNet), Feature Extraction vs Full Fine-Tuning, Layer Freezing, Data Augmentation Strategies (Albumentations, `torchvision.transforms.v2`).

---

## Module 8.2: Object Detection, Segmentation, & Advanced Vision Tasks
- **Required Previous Courses**: Course 8 (Module 8.1)
- **Reusable Dependencies**: `Course8.Module8.1`
- **Skills Gained**: YOLO object detection, Semantic/Instance segmentation (U-Net, Mask R-CNN), Pose estimation, OCR, Face recognition, Medical imaging.
- **Industry Usage**: Real-time video surveillance, medical MRI segmentation, automatic document parsing, sports biomechanics.

### Lessons & Topics
1. **Lesson 8.2.1: Object Detection Frameworks (YOLO & Faster R-CNN)**
   - Topics: Bounding Box Regression, Anchor Boxes, Intersection over Union (IoU), Non-Maximum Suppression (NMS), Mean Average Precision (mAP@50, mAP@50-95), Two-Stage (Faster R-CNN) vs One-Stage Detectors (YOLOv8/YOLOv10/YOLOv11).
2. **Lesson 8.2.2: Image Segmentation (Semantic & Instance)**
   - Topics: Semantic Segmentation (U-Net Architecture for Medical Imaging, FCN), Instance Segmentation (Mask R-CNN), Panoptic Segmentation, Dice Loss, Jaccard Index (IoU).
3. **Lesson 8.2.3: Optical Character Recognition (OCR) & Document AI**
   - Topics: Tesseract OCR, EasyOCR, PaddleOCR, LayoutLM for Document Understanding, Text Detection (EAST, CRAFT) & Recognition Pipelines.
4. **Lesson 8.2.4: Pose Estimation, Face Recognition, & Medical Imaging**
   - Topics: Keypoint Detection, MediaPipe, OpenPose, Face Detection (MTCNN, RetinaFace), Face Recognition (Siamese Networks, Triplet Loss, ArcFace), Medical Image Analysis (DICOM Files, 3D U-Net).

---

# Course 9: Natural Language Processing (NLP) & Speech Processing

## Module 9.1: Classical NLP, Text Preprocessing, & Embeddings
- **Required Previous Courses**: Course 2 (Module 2.2), Course 7 (Module 7.1)
- **Reusable Dependencies**: `Course2.Module2.2`, `Course7.Module7.1`
- **Skills Gained**: Tokenization, Stemming/Lemmatization, TF-IDF, Word2Vec, FastText, GloVe, Recurrent Neural Networks (RNN/LSTM/GRU).
- **Industry Usage**: Search indexing, sentiment classification, spam detection.

### Lessons & Topics
1. **Lesson 9.1.1: Text Preprocessing Pipeline & Tokenization**
   - Topics: Text Normalization, Lowercasing, Stopword Removal, RegEx Cleaning, Stemming (Porter, Snowball), Lemmatization (WordNet), Subword Tokenization (BPE, WordPiece, Unigram).
2. **Lesson 9.1.2: Vector Space Models (Bag-of-Words & TF-IDF)**
   - Topics: Document-Term Matrix, N-Grams, Term Frequency-Inverse Document Frequency (TF-IDF), Cosine Similarity for Text Search, Scikit-Learn Vectorizers.
3. **Lesson 9.1.3: Distributed Word Embeddings (Word2Vec, FastText, GloVe)**
   - Topics: Word Embedding Concept, Word2Vec Architecture (CBOW vs Skip-Gram), Negative Sampling, FastText (Subword n-gram Embeddings), GloVe (Global Vectors), Gensim Framework.
4. **Lesson 9.1.4: Sequential Modeling with Recurrent Networks (RNN / LSTM / GRU)**
   - Topics: Recurrent Neural Network (RNN) Architecture, Vanishing Gradient in Sequences, Long Short-Term Memory (LSTM) Cell Gates (Input, Forget, Output Gates), Gated Recurrent Unit (GRU), Bidirectional LSTMs.

---

## Module 9.2: Transformer Architecture & Modern NLP Tasks
- **Required Previous Courses**: Course 9 (Module 9.1)
- **Reusable Dependencies**: `Course9.Module9.1`
- **Skills Gained**: Self-Attention, Multi-Head Attention, Transformers (Encoder-Decoder), BERT, Text Classification, NER, Summarization, Translation.
- **Industry Usage**: Enterprise document classification, automated summarization, machine translation.

### Lessons & Topics
1. **Lesson 9.2.1: The Transformer Architecture & Self-Attention**
   - Topics: "Attention Is All You Need" Paper, Scaled Dot-Product Attention $Query, Key, Value$, Multi-Head Attention, Positional Encoding (Absolute vs Rotary RoPE), Feed-Forward Layers, Residual Connections & LayerNorm.
2. **Lesson 9.2.2: Encoder-Based Models (BERT, RoBERTa, DeBERTa)**
   - Topics: Masked Language Modeling (MLM), Next Sentence Prediction (NSP), BERT Architecture, RoBERTa, DeBERTa, Sentence Transformers (`sentence-transformers` library) for Dense Embeddings.
3. **Lesson 9.2.3: Core NLP Applications (NER, Classification, Summarization, Translation)**
   - Topics: Named Entity Recognition (NER), Intent Classification, Sequence Labeling, Abstractive vs Extractive Summarization, Sequence-to-Sequence Models (T5, BART), Neural Machine Translation.

---

## Module 9.3: Speech Recognition & Speech Synthesis
- **Required Previous Courses**: Course 9 (Module 9.2)
- **Reusable Dependencies**: `Course9.Module9.2`
- **Skills Gained**: Audio Spectrograms, Automatic Speech Recognition (ASR with Whisper), Text-to-Speech (TTS), Speech Synthesis.
- **Industry Usage**: Voice assistants, automated call center transcription, voice cloning.

### Lessons & Topics
1. **Lesson 9.3.1: Audio Signal Processing Fundamentals**
   - Topics: Waveforms, Sampling Rate, Fast Fourier Transform (FFT), Spectrograms, Mel-Frequency Cepstral Coefficients (MFCCs), Librosa Library.
2. **Lesson 9.3.2: Automatic Speech Recognition (ASR)**
   - Topics: Speech-to-Text Architecture, OpenAI Whisper Model Architecture, Connectionist Temporal Classification (CTC) Loss, Fine-Tuning Whisper for Custom Domains.
3. **Lesson 9.3.3: Text-to-Speech (TTS) & Voice Synthesis**
   - Topics: TTS Pipeline (Text Analysis $\to$ Acoustic Model $\to$ Vocoder), Tacotron2, FastSpeech2, Neural Vocoders (HiFi-GAN), Voice Cloning Techniques.

---

# Course 10: Large Language Models (LLMs), Fine-Tuning, & RAG Systems

## Module 10.1: Large Language Model (LLM) Architectures & Generation
- **Required Previous Courses**: Course 9 (Module 9.2)
- **Reusable Dependencies**: `Course9.Module9.2`
- **Skills Gained**: Decoder-only LLMs (GPT, Llama, Mistral), Token Decoding Strategies (Greedy, Top-$K$, Top-$p$, Temperature), Context Window Scaling.
- **Industry Usage**: Building generative AI features, foundation model integration.

### Lessons & Topics
1. **Lesson 10.1.1: Decoder-Only Architecture (GPT, Llama, Mistral)**
   - Topics: Causal Language Modeling, Auto-regressive Generation, Llama Architecture Modifications (SwiGLU, RMSNorm, RoPE), Mistral Sliding Window Attention, FlashAttention v1/v2/v3.
2. **Lesson 10.1.2: Decoding Strategies & Sampling Parameters**
   - Topics: Greedy Search, Beam Search, Temperature Scaling, Top-$K$ Sampling, Top-$p$ (Nucleus) Sampling, Repetition Penalty, Min-$P$ Sampling, Frequency/Presence Penalties.
3. **Lesson 10.1.3: Context Window Scaling & Long-Context LLMs**
   - Topics: Attention Complexity $O(N^2)$, Linear Attention, Ring Attention, KV-Cache Optimization, PagedAttention (vLLM Architecture), Context Extension Techniques (YaRN, ALiBi).

---

## Module 10.2: Advanced Prompt Engineering & In-Context Learning
- **Required Previous Courses**: Course 10 (Module 10.1)
- **Reusable Dependencies**: `Course10.Module10.1`
- **Skills Gained**: System prompts, Few-shot prompting, Chain-of-Thought (CoT), Tree-of-Thoughts (ToT), Directional Stimulus, Structured Output Parsing.
- **Industry Usage**: Prompt optimization for production LLM APIs (OpenAI, Anthropic, Gemini).

### Lessons & Topics
1. **Lesson 10.2.1: Core Prompt Engineering Patterns**
   - Topics: System Prompts vs User Prompts, Zero-Shot, Few-Shot In-Context Learning, Persona Pattern, Output Formatting Instructions, Delimiters and Guarding.
2. **Lesson 10.2.2: Advanced Reasoning Prompting**
   - Topics: Chain-of-Thought (CoT) Prompting, Automatic CoT, Self-Consistency Sampling, Tree-of-Thoughts (ToT), Graph-of-Thoughts (GoT), RePhrase and Respond (RaR).
3. **Lesson 10.2.3: Structured Output Generation & Validation**
   - Topics: JSON Mode Enforcement, Pydantic Schema Validation, Instructor Library, Outlines Library (Guided Decoding with RegEx & Grammars), TypeChat.

---

## Module 10.3: Parameter-Efficient Fine-Tuning (PEFT, LoRA, QLoRA)
- **Required Previous Courses**: Course 7 (Module 7.2), Course 10 (Module 10.1)
- **Reusable Dependencies**: `Course7.Module7.2`, `Course10.Module10.1`
- **Skills Gained**: Full Fine-Tuning vs PEFT, LoRA, QLoRA (4-bit Quantization), Unsloth, Hugging Face `peft` & `trl` libraries.
- **Industry Usage**: Domain-adapting open-source LLMs (Llama 3, Mistral) on private company data.

### Lessons & Topics
1. **Lesson 10.3.1: Parameter-Efficient Fine-Tuning (PEFT) Foundations**
   - Topics: Full Fine-Tuning Memory Requirements, PEFT Taxonomy (Adapter Layers, Prefix Tuning, Prompt Tuning), Parameter Efficiency vs Accuracy Trade-Offs.
2. **Lesson 10.3.2: Low-Rank Adaptation (LoRA) Deep Dive**
   - Topics: Matrix Rank Decomposition $W = W_0 + \Delta W = W_0 + B \cdot A$, Rank $r$, Alpha Scaling Factor $\alpha$, Target Modules Selection, Merging LoRA Weights into Base Model.
3. **Lesson 10.3.3: Quantized LoRA (QLoRA) & 4-bit Quantization**
   - Topics: Quantization Fundamentals (FP16, INT8, INT4), NF4 (NormalFloat4) Data Type, Double Quantization, Paged Optimizers, QLoRA Training Pipeline.
4. **Lesson 10.3.4: Practical Fine-Tuning Pipeline (Hugging Face TRL & Unsloth)**
   - Topics: Instruction Dataset Preparation (ShareGPT, Alpaca formats), `SFTTrainer` (Supervised Fine-Tuning Trainer), Unsloth Fast Training Acceleration, Model Merging & GGUF/ExLlamaV2 Export.

---

## Module 10.4: Preference Alignment (RLHF, DPO, ORPO)
- **Required Previous Courses**: Course 10 (Module 10.3)
- **Reusable Dependencies**: `Course10.Module10.3`
- **Skills Gained**: RLHF, Reward Modeling, PPO, Direct Preference Optimization (DPO), ORPO, Alignment Evaluation.
- **Industry Usage**: Aligning fine-tuned LLMs for safety, helpfulness, and style adherence.

### Lessons & Topics
1. **Lesson 10.4.1: Reinforcement Learning from Human Feedback (RLHF)**
   - Topics: Alignment Problem (HHH: Helpful, Honest, Harmless), Reward Model Training, Proximal Policy Optimization (PPO) for LLMs, KL-Divergence Penalty.
2. **Lesson 10.4.2: Direct Preference Optimization (DPO) & Alignment Alternatives**
   - Topics: DPO Math Formulation (Eliminating the Reward Model), Odds Ratio Preference Optimization (ORPO), KTO (Kahneman-Tversky Optimization), Direct Alignment Frameworks.

---

## Module 10.5: Retrieval-Augmented Generation (RAG) & Vector Databases
- **Required Previous Courses**: Course 9 (Module 9.2), Course 10 (Module 10.1), FastAPI Course
- **Reusable Dependencies**: `Course9.Module9.2`, `Course10.Module10.1`, `FastAPI.All`
- **Skills Gained**: RAG Architecture, Vector Embeddings, Chunking Strategies, Vector DBs (FAISS, ChromaDB, Milvus, Pinecone), Hybrid Search, Re-ranking.
- **Industry Usage**: Building enterprise knowledge base QA systems over internal PDFs, Notion, and databases.

### Lessons & Topics
1. **Lesson 10.5.1: Naive RAG Architecture & Pipeline**
   - Topics: RAG Pipeline Overview, Document Loading, Text Chunking (Fixed-size, Recursive Character, Semantic Chunking, Sentence Splitting), Embedding Models, Vector Search.
2. **Lesson 10.5.2: Vector Database Systems (FAISS, ChromaDB, Milvus, Pinecone)**
   - Topics: Vector Search Indexing (Flat, IVF, HNSW - Hierarchical Navigable Small World), Distance Metrics (Cosine, Inner Product, L2), Local Vector DBs (FAISS, ChromaDB), Cloud Vector DBs (Pinecone, Milvus, Qdrant, Weaviate).
3. **Lesson 10.5.3: Advanced RAG: Hybrid Search & Re-ranking**
   - Topics: Keyword/BM25 Search + Dense Vector Search (Hybrid Search), Reciprocal Rank Fusion (RRF), Cross-Encoder Re-rankers (Cohere Rerank, BGE-Reranker).
4. **Lesson 10.5.4: Advanced RAG Query Transformations & Multi-Document RAG**
   - Topics: Query Rewriting, Sub-Query Decomposition, Step-Back Prompting, HyDE (Hypothetical Document Embeddings), Parent-Child Chunking, Sentence Window Retrieval, Contextual Compression.

---

## Module 10.6: Orchestration Frameworks (LangChain & LlamaIndex)
- **Required Previous Courses**: Course 10 (Module 10.5)
- **Reusable Dependencies**: `Course10.Module10.5`
- **Skills Gained**: LangChain Expression Language (LCEL), LlamaIndex Data Framework, Knowledge Graphs, Semantic Search.
- **Industry Usage**: Enterprise LLM application development, multi-source knowledge integration.

### Lessons & Topics
1. **Lesson 10.6.1: LangChain Framework & LCEL**
   - Topics: Components (PromptTemplates, Models, OutputParsers), LangChain Expression Language (LCEL) Piping `|`, Chains, Memory Persistence, Runnable Interfaces.
2. **Lesson 10.6.2: LlamaIndex Data Framework Deep Dive**
   - Topics: `VectorStoreIndex`, `SummaryIndex`, `TreeIndex`, `KnowledgeGraphIndex`, Node Parsers, Query Engines, Router Query Engine, Sub-Question Query Engine.
3. **Lesson 10.6.3: Knowledge Graphs & Graph RAG**
   - Topics: Property Graphs, Entity-Relation Extraction, Graph Databases (Neo4j), GraphRAG Architecture (Combining Knowledge Graphs with Vector Search).

---

## Module 10.7: LLM Evaluation, Benchmarking, & Guardrails
- **Required Previous Courses**: Course 10 (Module 10.6)
- **Reusable Dependencies**: `Course10.Module10.6`
- **Skills Gained**: LLM Benchmarks (MMLU, HumanEval), LLM-as-a-Judge, Ragas Framework, Guardrails (NeMo Guardrails, Llama Guard).
- **Industry Usage**: Production LLM quality assurance, safety filtering, hallucination prevention.

### Lessons & Topics
1. **Lesson 10.7.1: Standard LLM Benchmarks & Metric Datasets**
   - Topics: MMLU, GSM8K, HumanEval, MATH, Chatbot Arena (Elo Rating System), LMSYS Evaluation Framework.
2. **Lesson 10.7.2: LLM-as-a-Judge & Ragas Evaluation Framework**
   - Topics: Pairwise Comparison, Single-Answer Grading, Ragas Metrics (Faithfulness, Answer Relevance, Context Recall, Context Precision), DeepEval Framework.
3. **Lesson 10.7.3: LLM Guardrails & Safety Enforcement**
   - Topics: Input/Output Guardrails, NeMo Guardrails (Canonical Forms, Rails), Llama Guard, Guardrails AI, PII Redaction, Hallucination Detection & Interception.

---

# Course 11: Enterprise AI Agents, Multi-Agent Systems, & Agentic Workflows

## Module 11.1: Single AI Agent Architecture & Core Mechanics
- **Required Previous Courses**: Course 10 (Module 10.2, 10.6), Python (Asyncio)
- **Reusable Dependencies**: `Course10.Module10.2`, `Course10.Module10.6`, `Python.Asyncio`
- **Skills Gained**: ReAct Framework, Tool Calling, Function Calling, Planning, Reflection, Short-term & Long-term Memory.
- **Industry Usage**: Building autonomous coding agents, customer support agents, research assistants.

### Lessons & Topics
1. **Lesson 11.1.1: ReAct Framework & Tool Calling Mechanics**
   - Topics: Reasoning and Acting (ReAct) Loop (Thought $\to$ Action $\to$ Observation), Native Function Calling (OpenAI, Anthropic Tools API), Tool Registration and Pydantic Parameter Parsing.
2. **Lesson 11.1.2: Agent Planning & Self-Reflection**
   - Topics: Plan-and-Solve Prompting, Goal Decomposition, Self-Reflection (Reflexion Architecture), Self-Correction Loops, Dynamic Plan Revision.
3. **Lesson 11.1.3: Agent Memory Systems**
   - Topics: Short-Term Working Memory (Buffer, Summary), Long-Term Episodic/Semantic Memory (Vector Search Memory), Entity Memory, External Memory Stores (Redis, Mem0).

---

## Module 11.2: Multi-Agent Systems & Frameworks (CrewAI, AutoGen, LangGraph)
- **Required Previous Courses**: Course 11 (Module 11.1)
- **Reusable Dependencies**: `Course11.Module11.1`
- **Skills Gained**: Multi-agent orchestration, CrewAI, Microsoft AutoGen, LangGraph stateful agent graphs.
- **Industry Usage**: Enterprise workflow automation, complex multi-step software development agents.

### Lessons & Topics
1. **Lesson 11.2.1: Multi-Agent Collaboration Patterns**
   - Topics: Manager-Worker Pattern, Hierarchical Teams, Peer-to-Peer Discussion, Sequential Workflows, Consensus Mechanisms, Role-Playing Agents.
2. **Lesson 11.2.2: CrewAI Framework Architecture**
   - Topics: Agents, Tasks, Crews, Tools, Processes (Sequential vs Hierarchical), Memory Integration, Custom Tool Development.
3. **Lesson 11.2.3: Microsoft AutoGen Framework**
   - Topics: `ConversableAgent`, `UserProxyAgent`, Group Chat Manager, Code Execution Environment (Docker Sandboxing), Multi-Agent Conversation Patterns.
4. **Lesson 11.2.4: State Graph Agents with LangGraph**
   - Topics: Stateful Graph Architecture, Nodes, Edges, Conditional Edges, State Schema (`TypedDict`/Pydantic), Human-in-the-Loop Approval, Time Travel & State Rewinding.

---

## Module 11.3: Advanced Protocols & Agent Tooling (MCP, OpenAI Agents SDK, A2A)
- **Required Previous Courses**: Course 11 (Module 11.2), FastAPI Course
- **Reusable Dependencies**: `Course11.Module11.2`, `FastAPI.All`
- **Skills Gained**: Model Context Protocol (MCP), OpenAI Agents SDK, Agent-to-Agent (A2A) Protocols, AI Security & Sandboxing.
- **Industry Usage**: Building standardized enterprise agent tools, inter-agent communication services.

### Lessons & Topics
1. **Lesson 11.3.1: Model Context Protocol (MCP) Integration**
   - Topics: MCP Architecture (Client, Host, Server), Resources, Prompts, Tools, Building Custom MCP Servers (Python/TypeScript SDK), Local & Remote Server Connections.
2. **Lesson 11.3.2: OpenAI Agents SDK & Handoff Mechanics**
   - Topics: Agent Objects, Instructions, Tools, Agent Handoffs (`transfer_to_agent`), Guardrails Integration, Tracing and Inspection.
3. **Lesson 11.3.3: Agent-to-Agent (A2A) Communication Protocols**
   - Topics: Standardized Inter-Agent REST/gRPC Protocols, Agent Discovery Registries, Agent Authentication, Distributed Agent Execution.
4. **Lesson 11.3.4: Agent Security, Sandboxing, & Prompt Injection Defense**
   - Topics: Indirect Prompt Injection Attacks, Tool Abuse Prevention, Code Execution Sandboxing (E2B, Modal, Docker Container Isolation), Least Privilege Tool Permissions.

---

# Course 12: MLOps, Cloud AI, Edge AI, & Production Deployment

## Module 12.1: ML Experiment Tracking, Artifact Management, & Versioning (MLflow, DVC)
- **Required Previous Courses**: Course 5 (Module 5.6), Git Course
- **Reusable Dependencies**: `Course5.Module5.6`, `Git.All`
- **Skills Gained**: MLflow Tracking, Model Registry, Data Version Control (DVC), Artifact Repositories.
- **Industry Usage**: Reproducible ML research, model lineage tracking.

### Lessons & Topics
1. **Lesson 12.1.1: Experiment Tracking & Model Registry with MLflow**
   - Topics: MLflow Tracking (Runs, Parameters, Metrics, Artifacts), Autologging, MLflow Model Registry (Staging, Production, Archiving States), Model Serving.
2. **Lesson 12.1.2: Data & Pipeline Versioning with DVC**
   - Topics: Data Version Control (DVC) Concepts, `.dvc` Files, Remote Storage Integration (S3, GCS, Azure Blob), DVC Pipelines (`dvc.yaml`), Data Lineage Tracking.

---

## Module 12.2: Containerization & Cloud MLOps (Docker, Kubernetes, Kubeflow)
- **Required Previous Courses**: Course 12 (Module 12.1)
- **Reusable Dependencies**: `Course12.Module12.1`
- **Skills Gained**: Dockerizing ML/DL workloads, Kubernetes deployment, Kubeflow pipelines.
- **Industry Usage**: Scalable production model training and deployment infrastructure.

### Lessons & Topics
1. **Lesson 12.2.1: Docker for Data Science & Deep Learning**
   - Topics: Writing Production `Dockerfile` for ML, Multi-Stage Builds, CUDA Base Images (`nvidia/cuda`), Containerizing PyTorch/FastAPI Services, `docker-compose`.
2. **Lesson 12.2.2: Kubernetes Foundations for ML Services**
   - Topics: Pods, Deployments, Services, Ingress, Horizontal Pod Autoscaling (HPA), Resource Requests/Limits (GPU Resource Allocation).
3. **Lesson 12.2.3: End-to-End Orchestration with Kubeflow Pipelines**
   - Topics: Kubeflow Architecture, Building Kubeflow Pipeline Components, DAG Execution, Hyperparameter Tuning with Katib.

---

## Module 12.3: GPU Computing, Distributed Training, & High-Performance Inference
- **Required Previous Courses**: Course 7 (Module 7.2), Course 12 (Module 12.2)
- **Reusable Dependencies**: `Course7.Module7.2`, `Course12.Module12.2`
- **Skills Gained**: CUDA Architecture, Distributed Data Parallel (DDP), FSDP, DeepSpeed, vLLM High-Performance Serving.
- **Industry Usage**: Multi-GPU LLM training, ultra-low latency production inference.

### Lessons & Topics
1. **Lesson 12.3.1: GPU Architecture & CUDA Fundamentals**
   - Topics: NVIDIA GPU Architecture (Streaming Multiprocessors, CUDA Cores, Tensor Cores), Memory Hierarchy (Global, Shared, Registers), PyTorch CUDA Streams.
2. **Lesson 12.3.2: Distributed Training Strategies (DDP, FSDP, DeepSpeed)**
   - Topics: Data Parallelism vs Model Parallelism, Distributed Data Parallel (DDP), Fully Sharded Data Parallel (FSDP), DeepSpeed ZeRO Stages (ZeRO-1, ZeRO-2, ZeRO-3), Tensor/Pipeline Parallelism.
3. **Lesson 12.3.3: High-Performance LLM Serving (vLLM, TGI, TensorRT-LLM)**
   - Topics: vLLM PagedAttention Server Engine, Hugging Face Text Generation Inference (TGI), NVIDIA TensorRT-LLM Optimizations, Continuous Batching, Speculative Decoding.

---

## Module 12.4: Cloud AI Platforms (AWS SageMaker, Azure ML, Vertex AI, Hugging Face)
- **Required Previous Courses**: Course 12 (Module 12.3)
- **Reusable Dependencies**: `Course12.Module12.3`
- **Skills Gained**: AWS SageMaker, Google Cloud Vertex AI, Microsoft Azure ML, Hugging Face Hub & Inference Endpoints.
- **Industry Usage**: Enterprise cloud AI deployment and automated model operations.

### Lessons & Topics
1. **Lesson 12.4.1: AWS SageMaker End-to-End MLOps**
   - Topics: SageMaker Training Jobs, SageMaker Processing Jobs, Hyperparameter Tuning, Real-Time & Asynchronous Endpoints, SageMaker Model Monitor.
2. **Lesson 12.4.2: GCP Vertex AI & Azure Machine Learning**
   - Topics: Vertex AI Pipelines, AutoML, Custom Training Containers, Azure ML Workspaces, Automated ML, Managed Endpoints.
3. **Lesson 12.4.3: Hugging Face Ecosystem & Production Deployment**
   - Topics: Hugging Face Hub, Datasets Library, Transformers Library, Inference Endpoints (Dedicated GPU Hosting), Spaces for Demos.

---

## Module 12.5: High-Performance API Serving (FastAPI AI APIs) & Model Monitoring
- **Required Previous Courses**: FastAPI Course (All Modules), Course 12 (Module 12.4)
- **Reusable Dependencies**: `FastAPI.All`, `Course12.Module12.4`
- **Skills Gained**: Asynchronous AI API endpoints, Model Drift Monitoring, Evidently AI.
- **Industry Usage**: Serving production AI microservices with real-time health and drift tracking.

### Lessons & Topics
1. **Lesson 12.5.1: Building Asynchronous AI APIs with FastAPI**
   - Topics: Async Inference Handlers, Batch Inference Queuing, Streaming Responses (`EventSourceResponse` / SSE), WebSocket Streaming for Real-Time AI.
2. **Lesson 12.5.2: Production Model Monitoring & Drift Detection**
   - Topics: Data Drift vs Concept Drift, Data Quality Monitoring, Evidently AI Framework, Monitoring Metrics (KS Test, PSI - Population Stability Index), Automated Alerting.

---

## Module 12.6: Edge AI, Model Optimization, & TinyML (ONNX, TensorRT)
- **Required Previous Courses**: Course 8 (Module 8.1), Course 12 (Module 12.5)
- **Reusable Dependencies**: `Course8.Module8.1`, `Course12.Module12.5`
- **Skills Gained**: Model Pruning, Quantization (Post-Training Quantization), ONNX Runtime, NVIDIA TensorRT, OpenVINO, TinyML.
- **Industry Usage**: Deploying AI models to mobile devices, IoT microcontrollers, and edge gateways.

### Lessons & Topics
1. **Lesson 12.6.1: Model Compression: Pruning & Quantization**
   - Topics: Structured vs Unstructured Pruning, Post-Training Quantization (PTQ) vs Quantization-Aware Training (QAT), INT8 Precision Conversion.
2. **Lesson 12.6.2: Open Neural Network Exchange (ONNX) & TensorRT**
   - Topics: Exporting PyTorch/TensorFlow Models to ONNX, ONNX Runtime Execution, NVIDIA TensorRT Engine Optimization (FP16/INT8 Precision Calibration).
3. **Lesson 12.6.3: Edge AI & TinyML Deployment**
   - Topics: TensorFlow Lite (TFLite) for Microcontrollers, OpenVINO for Intel Edge Hardware, ARM Cortex-M Deployments, Battery/Power-Constrained AI Execution.

---

## Module 12.7: AI Ethics, Governance, & Responsible AI
- **Required Previous Courses**: Course 10 (Module 10.7)
- **Reusable Dependencies**: `Course10.Module10.7`
- **Skills Gained**: Algorithmic Bias Audit, Explainable AI (SHAP, LIME), Fairlearn, EU AI Act Compliance.
- **Industry Usage**: Ensuring corporate AI compliance, legal audit, and transparent decision-making.

### Lessons & Topics
1. **Lesson 12.7.1: Explainable AI (XAI) Frameworks (SHAP & LIME)**
   - Topics: Model Transparency, Local vs Global Explainability, LIME (Local Interpretable Model-agnostic Explanations), SHAP (Shapley Additive exPlanations), TreeSHAP, Summary & Waterfall Plots.
2. **Lesson 12.7.2: Fairness, Bias, & Responsible AI Governance**
   - Topics: Demographic Parity, Equalized Odds, Disparate Impact Ratio, IBM AI Fairness 360, Fairlearn, EU AI Act Risk Categories, Watermarking Generated Media.

---

## Module 12.8: Enterprise Capstone Industry Projects
- **Required Previous Courses**: All Previous Courses (Courses 1 - 12)
- **Reusable Dependencies**: `All.Previous.Courses`
- **Skills Gained**: End-to-end architecture, multi-agent workflows, production MLOps deployment.
- **Industry Usage**: Portfolio demonstration of senior AI/LLM Research & Systems Engineering capabilities.

### Lessons & Topics
1. **Lesson 12.8.1: Autonomous Software Engineering Agent System**
   - Topics: Building a Multi-Agent System (LangGraph + MCP) that reads GitHub issues, inspects codebases, writes tests, modifies files, and submits pull requests autonomously.
2. **Lesson 12.8.2: Enterprise Multimodal GraphRAG System for Technical Support**
   - Topics: Hybrid Vector + Knowledge Graph RAG over technical manuals, PDF schematics, and audio logs with vLLM serving, Cohere re-ranking, and BGE embeddings.
3. **Lesson 12.8.3: Real-Time Edge Vision & Telemetry Anomaly Detection**
   - Topics: High-speed YOLOv11 + ONNX Runtime pipeline on edge gateway with MQTT streaming and real-time Evidently AI drift monitoring dashboard.

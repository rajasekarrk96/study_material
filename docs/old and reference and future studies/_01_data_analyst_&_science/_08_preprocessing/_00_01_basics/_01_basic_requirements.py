# Data Cleaning:

# Handling missing data:

# Notes: Missing data can significantly impact the performance of machine learning models. Various techniques can be employed to handle missing data, including imputation, removal, or advanced methods like K-nearest neighbors imputation.
# Example: If you have missing values in a dataset, you can use mean imputation to fill in the missing values with the mean of the available data in that column.

# Handling outliers:

# Notes: Outliers are data points that significantly differ from other observations in the dataset. They can affect the mean and standard deviation and thus influence model performance. Techniques such as Z-score or IQR can be used to identify and treat outliers.
# Example: Using the Z-score method, you can identify outliers by calculating the Z-score for each data point and considering those with a Z-score above a certain threshold as outliers.

# Removing duplicates:

# Notes: Duplicate records in a dataset can skew analysis results and model performance. It's essential to identify and remove duplicates to maintain data integrity.
# Example: You can identify duplicate records by comparing all columns in the dataset and removing records with identical values in all columns.

# Data Transformation:

# Normalization:

# Notes: Normalization scales numerical features to a standard range, making them comparable and preventing features with larger scales from dominating the model.
# Example: Scaling numerical features such as age, income, and years of experience to a range between 0 and 1 using min-max normalization.

# Standardization:

# Notes: Standardization transforms numerical features to have a mean of 0 and a standard deviation of 1, making them suitable for algorithms that assume normally distributed data.
# Example: Standardizing numerical features like height, weight, and temperature using z-score standardization.

# Encoding categorical variables:

# Notes: Categorical variables need to be converted into numerical format for machine learning algorithms. Common encoding techniques include one-hot encoding, label encoding, and binary encoding.
# Example: Converting categorical variables like gender (male, female) into numerical format using one-hot encoding, where two binary variables (e.g., male = 1, female = 0) represent gender.

# Feature Engineering:

# Creating new features:

# Notes: Feature engineering involves creating new features from existing ones to capture more information or patterns in the data, potentially improving model performance.
# Example: Creating a new feature "total_income" by adding together the "salary" and "bonus" features in a dataset.

# Dimensionality reduction:

# Notes: Dimensionality reduction techniques like Principal Component Analysis (PCA) or feature selection methods aim to reduce the number of features while preserving most of the information, thus reducing computational complexity and overfitting.
# Example: Applying PCA to reduce the dimensionality of a dataset containing multiple correlated features into a smaller set of orthogonal features.

# Data Integration:

# Combining multiple datasets:

# Notes: Data integration involves merging or joining datasets based on common attributes or keys to create a unified dataset for analysis.
# Example: Merging two datasets containing customer information (e.g., demographics, purchase history) based on a common customer ID to create a comprehensive customer database.

# Reshaping data:

# Notes: Reshaping data involves transforming data from wide to long format or vice versa to meet the requirements of specific analysis or modeling tasks.
# Example: Reshaping a dataset containing sales data in wide format (each column represents a product category) into long format (each row represents a sales transaction for a specific product category).

# Data Preprocessing for Specific Tasks:

# Text data preprocessing:

# Notes: Text data often requires preprocessing to convert unstructured text into a format suitable for analysis or modeling.Common preprocessing steps include tokenization, stemming, lemmatization, and removing stopwords.
# Example: Preprocessing a corpus of text documents by btokenizing each document into individual words, removing punctuation, and converting all words to lowercase.

# Image data preprocessing:

# Notes: Image data preprocessing involves various transformations to prepare images for computer vision tasks.Techniques include resizing, normalization, augmentation, and feature extraction.
# Example: Preprocessing a  dataset of images by  resizing  all images to a  standard size, normalizing  pixel  values  to a  range  between  0 and 1, and augmenting  the  dataset  by  applying  random transformations like rotation and flipping.

# Time series data preprocessing:

# Notes: Time series data preprocessing includes handling missing values, smoothing, and feature extraction to prepare time series data for forecasting or analysis.
# Example: Preprocessing a time series dataset by imputing missing values using forward or backward filling, smoothing noisy data using moving averages, and extracting features like trend and seasonality.

# Data Preprocessing Libraries:

# Pandas(Python):

# Notes: Pandas is a powerful library for data manipulation and analysis in Python.It provides data structures like DataFrame and Series, as well as functions for data preprocessing, cleaning, and transformation.
# Example: Using  Pandas to load a CSV file into a DataFrame, perform data cleaning operations like removing missing values and duplicates

# NumPy(Python):

# Notes: NumPy is a fundamental library for numerical computing in Python.It provides support for multi-dimensional arrays and mathematical functions, making it useful for data preprocessing tasks.
# Example: Using NumPy to perform operations like normalization or standardization on numerical data arrays.

# Scikit - learn(Python):

# Notes: Scikit - learn is a popular machine learning library in Python that provides tools for data preprocessing, modeling, and evaluation.It includes modules for preprocessing techniques such as scaling, encoding, and feature selection.
# Example: Using Scikit - learn 's preprocessing module to scale numerical features using MinMaxScaler or StandardScaler.

# Best Practices and Techniques:

# Notes: Best practices in data preprocessing include understanding the impact of preprocessing on model performance, experimenting with different techniques, and documenting preprocessing steps for reproducibility.
# Example: Conducting experiments to compare the performance of different preprocessing pipelines(e.g., with or without feature scaling) using cross-validation and selecting the pipeline with the best performance based on evaluation metrics.
# Validation and Evaluation:

# Notes: Proper validation and evaluation of preprocessing techniques are essential to ensure the effectiveness of preprocessing pipelines.Techniques include using appropriate validation methods and metrics to evaluate model performance.
# Example: Splitting the dataset into training and testing sets, applying preprocessing techniques to the training set only, and evaluating model performance on the testing set to assess the generalization ability of the model.
# Ethical Considerations:

# Notes: Ethical considerations in data preprocessing involve addressing issues such as bias in data, privacy concerns, and unintended consequences of preprocessing techniques.
# Example: Identifying and mitigating biase in training data that may lead to unfair or discriminatory outcomes in machine learning models.
# Practical Application:

# Notes: Practical application involves applying data preprocessing techniques to real - world datasets and projects to gain hands - on experience and solve real - world problems.
# Example: Working on Kaggle competitions, industry projects, or personal projects that involve collecting, preprocessing, and analyzing data to derive insights or build predictive models.


import pandas as pd
import numpy as np

data_set=pd.read_csv("C:/Users/rajas/OneDrive/_12_DATA_ANALYST/_99_data_sets/Data_Set.csv")

print(data_set)

data_set2=pd.read_csv("C:/Users/rajas/OneDrive/_12_DATA_ANALYST/_99_data_sets/Data_Set.csv",header=2)

print(data_set2)

d3=data_set2.rename(columns={"Temperature":"Temp"})

print(d3)

d4=d3.drop("No. Occupants",axis=1)

print(d4)




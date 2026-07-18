# 03_01_ Removing_Null_and_Duplicate_Values

import pandas as pd
import numpy as np

# Create example DataFrame with null and duplicate values
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', None, 'Frank', 'Bob'],  # 'Bob' duplicated, one None
    'age': [25, 30, np.nan, 40, 35, np.nan, 30],                        # np.nan represents missing values
    'city': ['NY', 'LA', 'NY', None, 'Chicago', 'LA', 'LA']             # Some missing cities
}
df = pd.DataFrame(data)

# Display initial data
print("Original DataFrame:\n", df)

# ----- Removing Null Values -----

# Drop any rows containing null values
df_dropna = df.dropna()
print("\nDataFrame after dropping rows with any nulls:\n", df_dropna)

# Drop rows where all values are null (rare but possible)
df_dropna_all = df.dropna(how='all')
print("\nDataFrame after dropping rows where all columns are null:\n", df_dropna_all)

# Drop rows where null appears in specific columns only
df_dropna_subset = df.dropna(subset=['age'])  # Drop rows with null in 'age' only
print("\nDataFrame after dropping rows with null in 'age':\n", df_dropna_subset)

# Drop columns containing null values
df_dropna_cols = df.dropna(axis=1)
print("\nDataFrame after dropping columns with any null values:\n", df_dropna_cols)

# ----- Replacing Null Values -----

# Replace null values with a specified value (e.g., fill NaN in 'age' with mean age)
mean_age = df['age'].mean(skipna=True)
df_filled = df.fillna({'age': mean_age, 'city': 'Unknown'})
print("\nDataFrame after filling nulls in 'age' with mean and 'city' with 'Unknown':\n", df_filled)

# ----- Removing Duplicate Values -----

# Drop duplicate rows, keeping the first occurrence by default
df_no_duplicates = df.drop_duplicates()
print("\nDataFrame after removing duplicate rows:\n", df_no_duplicates)

# Drop duplicates based on specific columns (e.g., name and city)
df_no_dup_subset = df.drop_duplicates(subset=['name', 'city'])
print("\nDataFrame after dropping duplicates based on 'name' and 'city' columns:\n", df_no_dup_subset)

# Drop duplicates and keep last occurrence
df_no_dup_last = df.drop_duplicates(keep='last')
print("\nDataFrame after removing duplicates keeping last occurrence:\n", df_no_dup_last)

# Note: These techniques help clean datasets for accurate analysis and machine learning.

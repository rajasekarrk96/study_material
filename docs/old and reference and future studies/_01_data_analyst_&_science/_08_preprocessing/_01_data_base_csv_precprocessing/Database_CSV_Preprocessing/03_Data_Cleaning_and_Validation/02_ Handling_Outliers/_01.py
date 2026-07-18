# Outliers: Definition and Handling in Python with pandas

# Outliers are data points that are significantly different from other observations in the dataset.
# They can arise from various causes such as measurement errors, natural variability, or experimental errors.
# Outliers can skew statistical analyses and machine learning models, so detecting and handling them is essential.

import pandas as pd                      # Data handling library
import numpy as np                       # Numerical computations
from scipy import stats                  # Statistical functions for Z-score computation

# Sample data including outliers
data = {'value': [10, 12, 14, 15, 1000, 16, 18, 20, -300, 22, 24]}
df = pd.DataFrame(data)                  # Create DataFrame from data

print("Original Data:")                  # Display original data with outliers
print(df)

# Outlier detection using Interquartile Range (IQR) method:
Q1 = df['value'].quantile(0.25)          # Calculate 25th percentile (Q1)
Q3 = df['value'].quantile(0.75)          # Calculate 75th percentile (Q3)
IQR = Q3 - Q1                            # Interquartile range (IQR)

lower_bound = Q1 - 1.5 * IQR              # Lower bound, values below considered outliers
upper_bound = Q3 + 1.5 * IQR              # Upper bound, values above considered outliers

# Filter data within bounds, exclude outliers outside these limits
df_iqr_filtered = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]
print("\nData after IQR filtering (outliers removed):")
print(df_iqr_filtered)

# Outlier detection using Z-score method:
z_scores = np.abs(stats.zscore(df['value']))   # Compute absolute Z-scores for each value
threshold = 3                                  # Common threshold for outliers (3 standard deviations)
df_z_filtered = df[(z_scores < threshold)]    # Retain values with Z-score below threshold

print("\nData after Z-score filtering (outliers removed):")
print(df_z_filtered)

# Optional: Replace outliers with median to maintain dataset size
median_val = df['value'].median()              # Calculate median value
df['value_no_outliers'] = df['value']          # Create new column for cleaned data
df.loc[(z_scores >= threshold), 'value_no_outliers'] = median_val   # Replace outliers with median

print("\nData with outliers replaced by median value:")
print(df)

# Summary:
# - Outliers can distort data insights and model performance.
# - IQR and Z-score are common statistical methods to identify outliers.
# - Once detected, outliers can be removed or replaced depending on analysis needs.

import seaborn as sns
import pandas as pd


# Load Titanic dataset from Seaborn
titanic_df = sns.load_dataset('titanic')

# Data Cleaning:
#
# Handling missing data:

# Check for missing values
titanic_df.isnull().sum()

# Fill missing age values with mean

# Use the recommended approach:
titanic_df.fillna({'age': titanic_df['age'].mean()}, inplace=True)

# Handling outliers:

# Outlier detection using Z-score
from scipy import stats
z_scores = stats.zscore(titanic_df['fare'])
outliers = titanic_df[(z_scores > 3) | (z_scores < -3)]
print(outliers)

# Removing duplicates:

# Remove duplicate records
titanic_df.drop_duplicates(inplace=True)

# Data Transformation:
#
# Normalization:

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
titanic_df[['fare', 'age']] = scaler.fit_transform(titanic_df[['fare', 'age']])

# Standardization:

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
titanic_df[['fare', 'age']] = scaler.fit_transform(titanic_df[['fare', 'age']])
# Encoding categorical variables:

# Using pandas' get_dummies for one-hot encoding
titanic_df_encoded = pd.get_dummies(titanic_df, columns=['sex', 'embarked'])
# Feature Engineering:

# Creating new features:

# Create a new feature 'family_size' by combining 'sibsp' and 'parch'
titanic_df['family_size'] = titanic_df['sibsp'] + titanic_df['parch'] + 1
# Dimensionality reduction:

# Perform PCA for dimensionality reduction
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
titanic_pca = pca.fit_transform(titanic_df[['fare', 'age', 'family_size']])
# Data Integration:

# Combining multiple datasets:
# Note: In this example, we're not combining multiple datasets as the Titanic dataset is already a single dataset.

# Reshaping data:
# Note: In this example, we're not reshaping data as it's not applicable for the Titanic dataset.

# Data Preprocessing Libraries:

# Pandas:


# Load Titanic dataset into a DataFrame
titanic_df = sns.load_dataset('titanic')
# NumPy (not applicable for these examples).

# Scikit-learn:

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(titanic_df[['fare', 'age']])
# Dplyr (R) (not applicable for these examples).
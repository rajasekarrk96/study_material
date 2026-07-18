# 01_ Reading_CSV_in_Python_(Pandas)

# Pandas provides a convenient function read_csv() to load CSV files into DataFrames for analysis.

import pandas as pd

# Basic CSV reading
df = pd.read_csv('data/sample.csv')  # Load CSV located at specified path
print(df.head())                    # Display first 5 rows for quick data preview

# Common useful parameters:

# index_col: Specify column(s) to use as row index
df = pd.read_csv('data/sample.csv', index_col='id')

# usecols: Load only specified columns to save memory
df = pd.read_csv('data/sample.csv', usecols=['name', 'age', 'city'])

# nrows: Load only a subset of rows (e.g. for testing)
df = pd.read_csv('data/sample.csv', nrows=100)

# skiprows: Skip initial rows if file contains metadata or comments
df = pd.read_csv('data/sample.csv', skiprows=1)

# na_values: Define additional strings to recognize as NaN (missing data)
df = pd.read_csv('data/sample.csv', na_values=['n/a', '--'])

# dtype: Specify data types of columns to optimize memory and prevent errors
df = pd.read_csv('data/sample.csv', dtype={'age': int, 'salary': float})

# Encoding: Use encoding if CSV contains special characters
df = pd.read_csv('data/sample.csv', encoding='utf-8')

# Handling large files:
# Use chunksize to iterate over file in smaller chunks efficiently
chunks = pd.read_csv('data/large_file.csv', chunksize=5000)
for chunk in chunks:
    # Process or filter each chunk independently
    process(chunk)

# Summary:
# read_csv() is versatile to handle many file formats, encodings, and performance optimizations.
# Understanding these options improves efficiency and robustness in data preparation workflows.

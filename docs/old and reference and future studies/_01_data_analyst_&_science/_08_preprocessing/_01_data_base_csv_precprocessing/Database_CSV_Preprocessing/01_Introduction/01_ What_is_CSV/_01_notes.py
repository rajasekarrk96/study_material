# 01_ What_is_CSV

# CSV stands for Comma-Separated Values, a plain text file format to store tabular data.
# Each line represents a data record consisting of fields separated by commas (or other delimiters).
# CSV files store data in rows (records) and columns (fields), making them simple and widely used.

# Features of CSV files:
# - Human-readable and easy to edit with any text editor or spreadsheet software.
# - Supported by almost all data processing and database systems.
# - Fields can be optionally enclosed in double quotes.
# - If a field contains commas, double quotes, or newlines, it should be quoted.
# - The first line can optionally serve as a header with column names.
# - Often uses UTF-8 encoding but can be any text encoding.

# Example CSV content:
# name,age,city
# Alice,30,New York
# Bob,25,Los Angeles

# This format is excellent for simple data exchange and intermediate data storage.

# Common uses:
# - Exchanging data between heterogeneous systems.
# - Input to data analysis and machine learning pipelines.
# - Intermediate storage during Extract, Transform, Load (ETL) processes.

# Python example: loading CSV using pandas
import pandas as pd

# Read a CSV file into a pandas DataFrame
df = pd.read_csv('data/sample.csv')

# Display first few rows
print(df.head())

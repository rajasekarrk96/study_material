# 03_ Overview_of_Pandas_and_SQL

# Pandas is a powerful Python library for data manipulation and analysis.
# It provides DataFrame data structures to efficiently handle tabular datasets.
# It excels at reading and preprocessing CSV and other tabular data.

# SQL (Structured Query Language) is a standardized language for querying and managing relational databases.
# SQL allows filtering, joining, aggregating, and transforming data stored in tables.

# Combining Pandas and SQL workflows:
# - Use Pandas for reactive data manipulation and cleaning.
# - Use SQL for persistent structured storage and complex querying.

# Example: Loading CSV into Pandas DataFrame
import pandas as pd
df = pd.read_csv('data/sample.csv')    # Read CSV file
print(df.head())                        # Show first 5 rows

# Example: Querying SQL database with pandas
from sqlalchemy import create_engine
engine = create_engine('sqlite:///mydatabase.db')           # Create SQL engine (SQLite example)
query = "SELECT * FROM customers WHERE age > 25;"           # SQL query string
result_df = pd.read_sql_query(query, con=engine)            # Read SQL query into DataFrame
print(result_df.head())                                      # Display query results

# Pandas also supports writing DataFrames back to SQL databases easily
df.to_sql('table_name', con=engine, if_exists='replace', index=False)

# Summary:
# - Pandas and SQL together enable flexible, powerful data workflows.
# - Pandas excels in-memory manipulation.
# - SQL excels in data storage and optimized querying.

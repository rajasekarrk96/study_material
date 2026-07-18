# 02_ Applications_of_CSV_in_Databases

# CSV files are frequently used in database contexts due to their simplicity and compatibility.

# Common applications:
# 1. Data Import: Uploading CSV files to populate database tables.
# 2. Data Export: Extracting query results or tables for offline use or sharing.
# 3. Data Migration: Transferring data across different systems or platforms.
# 4. Backup & Archival: Storing database snapshots in CSV format for safety.
# 5. ETL Processes: CSV files serve as intermediate format in Extract, Transform, Load pipelines.
# 6. Bulk Data Operations: Many database systems allow bulk import/export using CSV files for efficiency.

# Advantages in database usage:
# - Simple format easily generated or parsed by most tools.
# - Easy to inspect and edit manually if needed.
# - Supports large scale data exchange.

# Example: importing CSV data into a SQL database using pandas and SQLAlchemy
import pandas as pd
from sqlalchemy import create_engine

# Load CSV file into DataFrame
df = pd.read_csv('data/customers.csv')

# Create database engine (example: SQLite)
engine = create_engine('sqlite:///mydatabase.db')

# Write data to SQL table "customers", replace if exists
df.to_sql('customers', con=engine, if_exists='replace', index=False)

# Now data from CSV is stored in the database 'customers' table

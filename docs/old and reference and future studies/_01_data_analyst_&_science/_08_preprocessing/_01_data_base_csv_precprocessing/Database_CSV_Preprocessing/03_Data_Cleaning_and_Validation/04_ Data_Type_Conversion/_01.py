# 04_ Data_Type_Conversion

# Data type conversion involves changing the data types of columns in a DataFrame.
# This is useful for optimizing memory, fixing data inconsistencies, or preparing data for analysis.

import pandas as pd

# Sample data with object (string) dtype
data = {
    'id': ['001', '002', '003', '004'],    # IDs as strings
    'score': ['85', '90', '78', '88']      # Scores as strings
}
df = pd.DataFrame(data)

# Print original data types
print("Original data types:\n", df.dtypes)

# Convert 'id' to integer
df['id'] = df['id'].astype(int)

# Convert 'score' to float
df['score'] = df['score'].astype(float)

# Print updated data types
print("\nUpdated data types:\n", df.dtypes)

# Handling missing or invalid data:
# If some conversions might fail due to invalid values, use pd.to_numeric()
df2 = pd.DataFrame({
    'score': ['85', 'ninety', '78', '88']
})
# Convert with error handling, invalid parsing results in NaN
df2['score'] = pd.to_numeric(df2['score'], errors='coerce')

print("\nData after safe conversion with errors='coerce':")
print(df2)

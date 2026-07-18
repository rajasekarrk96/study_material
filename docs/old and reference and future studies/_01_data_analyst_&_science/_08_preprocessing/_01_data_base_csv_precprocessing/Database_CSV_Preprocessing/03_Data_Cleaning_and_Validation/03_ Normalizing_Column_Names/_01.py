# 03_03_ Normalizing_Column_Names

# Normalizing column names means standardizing them for consistency and ease of use.
# This typically involves:
# - Converting all column names to lowercase or uppercase.
# - Replacing spaces with underscores.
# - Removing special characters or punctuation.
# - Fixing typos or synonym column names to a standard form.

import pandas as pd

# Sample dataframe with inconsistent column names
data = {
    'First Name': ['Alice', 'Bob'],
    'LAST name': ['Smith', 'Jones'],
    ' E-mail ': ['alice@example.com', 'bob@example.com'],
    'Phone#': ['123-456', '789-012']
}

df = pd.DataFrame(data)

# Print original columns
print("Original Columns:", df.columns)

# Normalize column names
df.columns = df.columns.str.strip()              # Remove leading/trailing whitespace
df.columns = df.columns.str.lower()               # Convert to lowercase
df.columns = df.columns.str.replace(' ', '_')    # Replace spaces with underscore
df.columns = df.columns.str.replace('[^0-9a-zA-Z_]', '', regex=True)  # Remove special characters

# Print normalized columns
print("Normalized Columns:", df.columns)

# Additional method: Rename specific columns mapping different names to a standard name
rename_map = {
    'first_name': 'firstname',
    'last_name': 'lastname',
    'email': 'email_address',
    'phone': 'phone_number'
}

df = df.rename(columns=rename_map)  # Rename according to mapping

print("Final Columns after renaming:", df.columns)

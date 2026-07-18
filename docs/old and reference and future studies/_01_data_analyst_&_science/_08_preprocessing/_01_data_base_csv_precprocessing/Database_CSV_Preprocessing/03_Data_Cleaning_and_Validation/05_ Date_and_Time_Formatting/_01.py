# 05_ Date_and_Time_Formatting

# Handling date and time data is crucial as they often come in various formats
# and need to be converted to pandas datetime objects for effective analysis.

import pandas as pd

# Sample data with date and time as strings in different formats
data = {
    'date_str': ['2025-01-15', '15/02/2025', 'March 3, 2025', '2025-04-04 13:45:00'],
    'time_str': ['13:30', '1:45 PM', '07:15:30', None]
}
df = pd.DataFrame(data)

# Print original data types (all are objects - strings)
print("Original data types:")
print(df.dtypes)

# Convert 'date_str' column to datetime, infer format automatically
df['date'] = pd.to_datetime(df['date_str'], errors='coerce', dayfirst=False)

# Convert 'time_str' column to timedelta (time of day), errors='coerce' converts invalid to NaT
df['time'] = pd.to_timedelta(df['time_str'].fillna('00:00:00'), errors='coerce')

# Alternatively, for full datetime conversion, combine date and time columns:
df['datetime'] = pd.to_datetime(df['date_str'] + ' ' + df['time_str'].fillna('00:00:00'), errors='coerce')

# Print the converted datetime and timedelta columns
print("\nConverted date, time and datetime columns:")
print(df[['date', 'time', 'datetime']])

# Extract useful components like year, month, day, hour
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

print("\nExtracted year, month, day:")
print(df[['year', 'month', 'day']])

# Summary:
# - Use pd.to_datetime() to parse various date/time string formats.
# - Use errors='coerce' to handle parsing errors gracefully.
# - Extract datetime components easily using dt accessor.

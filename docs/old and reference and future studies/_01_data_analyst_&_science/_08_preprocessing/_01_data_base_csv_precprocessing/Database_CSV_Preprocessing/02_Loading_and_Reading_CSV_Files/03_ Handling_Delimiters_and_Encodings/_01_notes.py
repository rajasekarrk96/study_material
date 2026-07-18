# 03_ Handling_Delimiters_and_Encodings

import pandas as pd

# CSV files can use delimiters other than commas, such as tabs, semicolons, or pipes.
# pandas.read_csv() accepts 'sep' or 'delimiter' argument to specify the custom delimiter.

# Example 1: Reading CSV with default comma delimiter
df_default = pd.read_csv('data/sample.csv')  # Defaults to comma ','

# Example 2: Reading CSV with semicolon delimiter
df_semicolon = pd.read_csv('data/sample_semicolon.csv', sep=';')  # Use semicolon as delimiter

# Example 3: Reading a tab-separated file
df_tab = pd.read_csv('data/sample.tsv', sep='\t')  # Tab delimiter

# Example 4: Reading CSV with pipe delimiter
df_pipe = pd.read_csv('data/sample_pipe.csv', sep='|')

# When delimiter is more complex (e.g., multiple characters or regex), specify the 'engine' parameter as 'python'
df_complex = pd.read_csv('data/complex_delim.csv', sep=r';|,|\t', engine='python')  # Regex separator example

# Handling Encoding:
# CSV files may have different encodings. Default is 'utf-8', but others like 'ISO-8859-1' (latin1) are common.
df_utf8 = pd.read_csv('data/utf8_file.csv', encoding='utf-8')
df_latin1 = pd.read_csv('data/latin1_file.csv', encoding='ISO-8859-1')

# Practical tips:
# - Always inspect the delimiter and encoding of your CSV before loading.
# - Use 'engine="python"' for complex delimiters with regex.
# - Use appropriate encoding matching file format to avoid decode errors.
# - For files with irregular delimiters or inconsistent formats, pre-process or clean files if necessary.

# Example: Preview data
print(df_semicolon.head())

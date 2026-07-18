# 02_ Reading_Large_Files_in_Chunks

# Reading very large CSV files at once can overwhelm your system memory.
# Pandas provides chunksize parameter in read_csv() to read the file in smaller, manageable chunks.

import pandas as pd

# Read CSV file in chunks of 10,000 rows
chunk_iter = pd.read_csv('data/large_file.csv', chunksize=10000)

# Process chunks one by one to save memory
for chunk in chunk_iter:
    # Example: print the shape of each chunk
    print(chunk.shape)
    # You could filter, clean, or aggregate data per chunk here
    # and save or append results gradually to new files or databases.

# After processing, you may concatenate or analyze aggregated data as needed:
# combined_df = pd.concat(processed_chunks)

# Benefits of chunking:
# - Avoids loading entire large file into memory.
# - Enables processing massive datasets on limited resource systems.
# - Useful for ETL pipelines: transform and write results incrementally.

# Additional memory optimization tips when reading large files:
# - Specify data types with dtype parameter.
# - Load only necessary columns with usecols.
# - Skip irrelevant rows with skiprows.
# - Use appropriate file encoding.

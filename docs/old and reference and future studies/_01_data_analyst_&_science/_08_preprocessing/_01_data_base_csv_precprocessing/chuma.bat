@echo off
:: Create the main folder for Database CSV Preprocessing
mkdir "Database_CSV_Preprocessing"

:: Change to the Database CSV Preprocessing directory
cd "Database_CSV_Preprocessing"

:: 1. Introduction to CSV and Databases
mkdir "01_Introduction"
mkdir "01_Introduction\01_ What_is_CSV"
mkdir "01_Introduction\02_ Applications_of_CSV_in_Databases"
mkdir "01_Introduction\03_ Overview_of_Pandas_and_SQL"

:: 2. Loading and Reading CSV Files
mkdir "02_Loading_and_Reading_CSV_Files"
mkdir "02_Loading_and_Reading_CSV_Files\01_ Reading_CSV_in_Python_(Pandas)"
mkdir "02_Loading_and_Reading_CSV_Files\02_ Reading_Large_Files_in_Chunks"
mkdir "02_Loading_and_Reading_CSV_Files\03_ Handling_Delimiters_and_Encodings"

:: 3. Data Cleaning and Validation
mkdir "03_Data_Cleaning_and_Validation"
mkdir "03_Data_Cleaning_and_Validation\01_ Removing_Null_and_Duplicate_Values"
mkdir "03_Data_Cleaning_and_Validation\02_ Handling_Outliers"
mkdir "03_Data_Cleaning_and_Validation\03_ Normalizing_Column_Names"
mkdir "03_Data_Cleaning_and_Validation\04_ Data_Type_Conversion"
mkdir "03_Data_Cleaning_and_Validation\05_ Date_and_Time_Formatting"

:: 4. Data Transformation
mkdir "04_Data_Transformation"
mkdir "04_Data_Transformation\01_ Adding_and_Removing_Columns"
mkdir "04_Data_Transformation\02_ Merging_and_Splitting_Columns"
mkdir "04_Data_Transformation\03_ Sorting_and_Filtering_Data"
mkdir "04_Data_Transformation\04_ Mapping_and_Encoding_Values"

:: 5. Advanced Preprocessing Techniques
mkdir "05_Advanced_Preprocessing_Techniques"
mkdir "05_Advanced_Preprocessing_Techniques\01_ Pivot_Tables_and_Groupby"
mkdir "05_Advanced_Preprocessing_Techniques\02_ Aggregation_and_Summary_Statistics"
mkdir "05_Advanced_Preprocessing_Techniques\03_ Reshaping_DataFrames"
mkdir "05_Advanced_Preprocessing_Techniques\04_ Handling_Multilevel_Indexes"

:: 6. CSV to Database Integration
mkdir "06_CSV_to_Database_Integration"
mkdir "06_CSV_to_Database_Integration\01_ Importing_CSV_into_SQL_Database"
mkdir "06_CSV_to_Database_Integration\02_ Using_Python_with_SQLAlchemy"
mkdir "06_CSV_to_Database_Integration\03_ Bulk_Data_Insertion_from_CSV"
mkdir "06_CSV_to_Database_Integration\04_ Exporting_Data_from_Database_to_CSV"

:: 7. Error Handling and Debugging
mkdir "07_Error_Handling_and_Debugging"
mkdir "07_Error_Handling_and_Debugging\01_ Handling_File_Not_Found_Errors"
mkdir "07_Error_Handling_and_Debugging\02_ Dealing_with_Corrupted_Files"
mkdir "07_Error_Handling_and_Debugging\03_ Debugging_Data_Type_Issues"

:: 8. Performance Optimization
mkdir "08_Performance_Optimization"
mkdir "08_Performance_Optimization\01_ Optimizing_Large_File_Processing"
mkdir "08_Performance_Optimization\02_ Memory_Management_in_Pandas"
mkdir "08_Performance_Optimization\03_ Efficient_Storage_Formats_(Parquet_Feather)"
mkdir "08_Performance_Optimization\04_ Indexing_and_Chunk_Processing"

:: 9. Real-World Projects and Case Studies
mkdir "09_Real_World_Projects_and_Case_Studies"
mkdir "09_Real_World_Projects_and_Case_Studies\01_ Data_Cleansing_for_ETL"
mkdir "09_Real_World_Projects_and_Case_Studies\02_ Data_Transformation_for_Analytics"
mkdir "09_Real_World_Projects_and_Case_Studies\03_ Building_Dashboards_with_Cleaned_Data"
mkdir "09_Real_World_Projects_and_Case_Studies\04_ CSV_Data_to_ML_Model_Integration"

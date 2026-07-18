@echo off
:: Create the main Power BI directory
mkdir "Power_BI"
cd "Power_BI"

:: 1. Introduction
mkdir "01_Introduction"
cd "01_Introduction"
mkdir "01_What_is_Power_BI"
mkdir "02_Power_BI_Components"
mkdir "03_Installation_and_Setup"
mkdir "04_Power_BI_Desktop_vs_Service"
mkdir "05_Power_BI_Licensing"
cd ..

:: 2. Data Connections
mkdir "02_Data_Connections"
cd "02_Data_Connections"
mkdir "01_Connecting_to_Excel"
mkdir "02_Connecting_to_SQL_Database"
mkdir "03_Connecting_to_SharePoint"
mkdir "04_Connecting_to_Cloud_Services"
mkdir "05_Connecting_to_Web_APIs"
mkdir "06_Connecting_to_Google_Sheets"
cd ..

:: 3. Data Transformation
mkdir "03_Data_Transformation"
cd "03_Data_Transformation"
mkdir "01_Power_Query_Editor"
cd "01_Power_Query_Editor"
mkdir "01_Remove_Columns"
mkdir "02_Rename_Columns"
mkdir "03_Change_Data_Type"
mkdir "04_Replace_Null_Values"
mkdir "05_Split_and_Merge_Columns"
mkdir "06_Remove_Duplicates"
mkdir "07_Pivot_and_Unpivot"
mkdir "08_Grouping_and_Aggregation"
mkdir "09_Extract_Year_Month_Day"
mkdir "10_Append_and_Merge_Queries"
mkdir "11_Creating_Custom_Columns"
cd ..
mkdir "02_Data_Modeling"
cd "02_Data_Modeling"
mkdir "01_Creating_Relationships"
mkdir "02_Star_vs_Snowflake_Schema"
mkdir "03_Cardinality_and_Cross_Filter_Direction"
mkdir "04_Creating_Hierarchy"
cd ..
cd ..

:: 4. DAX Expressions
mkdir "04_DAX_Expressions"
cd "04_DAX_Expressions"
mkdir "01_Introduction_to_DAX"
mkdir "02_Calculated_Columns_vs_Measures"
mkdir "03_DAX_Aggregate_Functions"
mkdir "04_DAX_Filter_Functions"
mkdir "05_DAX_Time_Intelligence_Functions"
mkdir "06_DAX_Logical_Functions"
mkdir "07_DAX_Iterator_Functions"
mkdir "08_DAX_Performance_Optimization"
cd ..

:: 5. Data Visualization
mkdir "05_Data_Visualization"
cd "05_Data_Visualization"
mkdir "01_Creating_Charts_and_Graphs"
cd "01_Creating_Charts_and_Graphs"
mkdir "01_Bar_and_Column_Charts"
mkdir "02_Line_and_Area_Charts"
mkdir "03_Pie_and_Donut_Charts"
mkdir "04_Scatter_Plots"
mkdir "05_Treemaps"
mkdir "06_Funnel_and_Waterfall_Charts"
cd ..
mkdir "02_Custom_Visuals"
mkdir "03_Interactive_Dashboards"
mkdir "04_Conditional_Formatting"
mkdir "05_Bookmarks_and_Tooltips"
cd ..

:: 6. Advanced Topics
mkdir "06_Advanced_Topics"
cd "06_Advanced_Topics"
mkdir "01_Row-Level_Security"
mkdir "02_Performance_Optimization"
mkdir "03_Incremental_Refresh"
mkdir "04_Power_BI_Service_Features"
mkdir "05_AI_and_Machine_Learning_in_Power_BI"
cd ..

:: 7. Real-World Projects
mkdir "07_Real_World_Projects"
cd "07_Real_World_Projects"
mkdir "01_Sales_Analysis_Dashboard"
mkdir "02_Financial_Reporting"
mkdir "03_Customer_Insights"
mkdir "04_HR_Analytics"
cd ..

:: 8. Deployment and Integration
mkdir "08_Deployment_and_Integration"
cd "08_Deployment_and_Integration"
mkdir "01_Publishing_to_Power_BI_Service"
mkdir "02_Sharing_Reports_and_Dashboards"
mkdir "03_Embedding_in_Apps"
mkdir "04_Power_BI_and_Azure_Integration"
mkdir "05_Power_BI_and_Python_Integration"
cd ..

:: 9. Additional Resources
mkdir "09_Additional_Resources"
cd "09_Additional_Resources"
mkdir "01_Power_BI_Keyboard_Shortcuts"
mkdir "02_Best_Practices"
mkdir "03_Community_and_Forums"
cd ..

echo Power BI folder structure with numbered topics created successfully!
pause

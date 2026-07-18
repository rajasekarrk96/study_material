import  pandas as pd
from pathlib import Path

p=Path("C:/Users/Rajasekar/OneDrive/_12_DATA_ANALYST/_03_mysql_in_python___/_data_preprocessing/coviddeaths.csv")

k=pd.read_csv(p)

print(k)


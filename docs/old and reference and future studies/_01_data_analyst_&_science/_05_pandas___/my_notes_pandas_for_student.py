# Python Pandas Series
# The Pandas Series can be defined as a one-dimensional array that is capable of storing various data types. We can easily convert the list, tuple, and dictionary into series using "series' method. The row labels of series are called the index. A Series cannot contain multiple columns. It has the following parameter:
#
# data: It can be any list, dictionary, or scalar value.
# index: The value of the index should be unique and hashable. It must be of the same length as data. If we do not pass any index, default np.arrange(n) will be used.
# dtype: It refers to the data type of series.
# copy: It is used for copying the data.
import pandas as pd
from numpy.distutils.system_info import amd_info

x = pd.Series()
print (x)
# _________________________________________________________
import pandas as pd
import numpy as np
info = np.array(['P','a','n','d','a','s'])
print(info,type(info))
a = pd.Series(info)
print(a,type(a))
# --------------------------------------------------------
#import the pandas library
import pandas as pd
import numpy as np
info = {'x' : 0., 'y' : 1., 'z' : 2.}
a = pd.Series(info)
y=pd.Series(info,index=['x','y'])
print(y)
print(pd.__version__)
print (a)
# ----------------------------------------------
import pandas as pd
import numpy as np
x = pd.Series(4, index=[ 1, 2, 3,4])
print (x)
# -----------------------------
import pandas as pd
import numpy as np
x = pd.Series(4, index=['name', 'age', 'phone', 'mail'])
print (x)
# ------------------------------------------------------------
import pandas as pd
x = pd.Series([1,2,3],index = ['a','b','c'])
#retrieve the first element
print (x[0])
print(x['a'])
#-----------------------------------------------------
import numpy as np
import pandas as pd
x=pd.Series(data=[2,4,6,8])
print(x.index)
print(x.values)
x=pd.Series(data=[2,4,6,8],index=[0,2,4,6])
print(x.index)
print(x.values)
y=pd.Series(data=[11.2,18.6,22.5], index=['a','b','c'])
print(y.index)
print(y.values)
print(y)
# -----------------------------
import numpy as np
import pandas as pd
a=pd.Series(data=[1,2,3,4])
b=pd.Series(data=[4.9,8.2,5.6],index=['x','y','z'])
print(a.dtype)
# itemsize->each size of element
print(a.values.itemsize)#error
print(b.dtype)
print(b.values.itemsize)
#-0----------------------------------------
import numpy as np
import pandas as pd
a=pd.Series(data=[1,2,3,4])
b=pd.Series(data=[4.9,8.2,5.6],index=['x','y','z'])
print(a.shape)
print(b.shape)
#--------------------
import numpy as np
import pandas as pd
a=pd.Series(data=[1,2,3,4])
b=pd.Series(data=[4.9,8.2,5.6],index=['x','y','z'])
print(a.ndim, b.ndim)
print(a.size, b.size)
print(a.nbytes, b.nbytes)
#----------------------------------
import numpy as np
import pandas as pd
a=pd.Series(data=[1,2,3,np.nan])
b=pd.Series(data=[4.9,8.2,5.6],index=['x','y','z'])
c=pd.Series()
print(a.empty,b.empty,c.empty)
print(a.hasnans,b.hasnans,c.hasnans)
print(len(a),len(b))
print(a.count( ),b.count( ))
# ------------------------------------------------------
import pandas as pd
import numpy as np
a = pd.Series(['Java', 'C', 'C++', np.nan])
a.map('I like {}'.format)
a.map('I like {}'.format, na_action='ignore')
# ----------------------
import pandas as pd
# Create a DataFrame
info = {
    'Name': ['Parker', 'Smith', 'John', 'William'],
    'sub1_Marks': [52, 38, 42, 37],
    'sub2_Marks': [41, 35, 29, 36]}
data = pd.DataFrame(info)
print(data)
# standard deviation of the dataframe
x=data["sub1_Marks"].std()
print(x)
# ----------------------------------
s = pd.Series(["a", "b", "c"],name="vals")
print(s)
s.to_frame()
# ------------------------------
import pandas as pd
import matplotlib.pyplot as plt
emp = ['Parker', 'John', 'Smith', 'William']
id = [102, 107, 109, 114]
emp_series = pd.Series(emp)
id_series = pd.Series(id)
frame = { 'Emp': emp_series, 'ID': id_series }
result = pd.DataFrame(frame)
print(result)
# -------------------------------
import pandas as pd
pd.unique(pd.Series([2, 1, 3, 3]))
pd.unique(pd.Series([pd.Timestamp('20160101'),pd.Timestamp('20160101')]))
# -----------------------------------
import pandas as pd
import numpy as np
pd.unique(pd.Index([pd.Timestamp('20160101', tz='US/Eastern'),pd.Timestamp('20160101', tz='US/Eastern')]))
# ----------------------------------
import pandas as pd
import numpy as np
ind = pd.Index([2, 1, 1, np.nan, 3])
ind.value_counts()
# ---------------------------------
import pandas as pd
import numpy as np
#split by ratio
a = pd.Series([2, 1, 1, np.nan, 3])
a.value_counts(normalize=True)

a = pd.Series([2, 1,1, 1, np.nan, 3,4,5])
a.value_counts(normalize=True)
# ---------------------
import pandas as pd
index = pd.Index([1, 3, 2, 2, 1, np.nan])
index.value_counts()
a = pd.Series([1, 3, 2, 2, 1, np.nan])
a = pd.Series([3, 2, 4,1])

#auto ranged sorted count
#bins->divides into equal half of the dataset, it show 0.997 because it has to count from 1, if it starts from 1->it cant count 1 so 0.997.
a.value_counts(bins=2)
a.value_counts(bins=3)
# ----------------------
import pandas as pd
index = pd.Index([1, 3, 2, 2, 1, np.nan])
index.value_counts()
a = pd.Series([1, 3, 2, 2, 1, np.nan])
a.value_counts(dropna=False)
a.value_counts(dropna=True)
# ----------------------------------------------
'''data frames'''
import pandas as pd
df = pd.DataFrame()
print (df)
#----------------------------
import pandas as pd

# a list of strings
x = ['Python', 'Pandas']

# Calling DataFrame constructor on list
df = pd.DataFrame(x)
print(df)
#---------------------
import pandas as pd
info = {'ID' :[101, 102, 103],'Department' :['B.Sc','B.Tech','M.Tech',]}
df = pd.DataFrame(info)
print(df)
#-------------------------
import pandas as pd

info = {'one': pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f']),
        'two': pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])}

d1 = pd.DataFrame(info)
print(d1)
#-------------------------
import pandas as pd

info = {'one': pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f']),
        'two': pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])}

d1 = pd.DataFrame(info)
print(d1['one'])
#----------------------------
import pandas as pd

info = {'one': pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
        'two': pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])}

df = pd.DataFrame(info)

# Add a new column to an existing DataFrame object

print("Add new column by passing series")
df['three'] = pd.Series([20, 40, 60], index=['a', 'b', 'c'])
print(df)

print("Add new column using existing DataFrame columns")
df['four'] = df['one'] + df['three']

print(df)
#-------------------------------
import pandas as pd

info = {'one': pd.Series([1, 2], index=['a', 'b']),
        'two': pd.Series([1, 2, 3], index=['a', 'b', 'c'])}

df = pd.DataFrame(info)
print("The DataFrame:")
print(df)

# using del function
print("Delete the first column:")
del df['one']
print(df)
# using pop function
print("Delete the another column:")
df.pop('two')
print(df)
#----------------------------------
import pandas as pd

info = {'one': pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
        'two': pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])}
df = pd.DataFrame(info)
print(df.loc['b'])
print(df.loc[0])#not possible
print(df.iloc[0])
#-----------------------------------

import pandas as pd
info = {'one' : pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
   'two' : pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])}
df = pd.DataFrame(info)
print (df.iloc[3])

#-----------------------------------
import pandas as pd
info = {'one' : pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
   'two' : pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])}
df = pd.DataFrame(info)
print (df[2:5])
#---------------------------------
import pandas as pd
d = pd.DataFrame([[7, 8], [9, 10]], columns = ['x','y'])
d2 = pd.DataFrame([[11, 12], [13, 14]], columns = ['x','y'])
d = d._append(d2)
print (d)
#----------------------
import pandas as pd

a_info = pd.DataFrame([[4, 5], [6, 7]], columns=['x', 'y'])
b_info = pd.DataFrame([[8, 9], [10, 11]], columns=['x', 'y'])

a_info = a_info._append(b_info)
print(a_info)
# Drop rows with label 0
a_info = a_info.drop(0)
print(a_info)
#-------------------------------------------
# Pandas DataFrame.apply()
import pandas as pd
import numpy as np
info = pd.DataFrame([[2, 7]] * 4, columns=['P', 'Q'])
print(info)
info.apply(np.sqrt)
info.apply(np.sum, axis=0)
info.apply(np.sum, axis=1)
info.apply(lambda x: [1, 2], axis=1)
info.apply(lambda x: [1, 2], axis=1, result_type='expand')
info.apply(lambda x: pd.Series([1, 2], index=['foo', 'bar']), axis=1)
info.apply(lambda x: [1, 2], axis=1, result_type='broadcast')
info
#------------------------------
# Pandas DataFrame.aggregate()

import pandas as pd
import numpy as np
info=pd.DataFrame([[1,5,7],[10,12,15],[18,21,24],[np.nan,np.nan,np.nan]],columns=['X','Y','Z'])
info.agg(['sum','min'])

import pandas as pd
import numpy as np
info=pd.DataFrame([[1,5,7],[10,12,15],[18,21,24],[np.nan,np.nan,np.nan]],columns=['X','Y','Z'])
info.agg({'X' : ['sum', 'min'], 'Y' : ['min', 'max']})
#---------------------------------
# Pandas DataFrame.assign()

import pandas as pd

# Create an empty dataframe
info = pd.DataFrame()

# Create a column
info['ID'] = [101, 102, 103]

# View the dataframe
info
# Assign a new column to dataframe called 'age'
info.assign(Name=['Smith', 'Parker', 'John'])

import pandas as pd
index=(['Canada', 'Australia'])
# Create a dataframe
info = pd.DataFrame({'temp_c': [17.0, 25.0]},index)
# Create an index that consist some values

# View the dataframe
info
info.assign(temp_f=lambda x: x.temp_c * 7 / 2 + 24)
info
info=info.assign(temp_f=lambda x: x['temp_c'] * 6 / 2 + 21)
info
temp_k=lambda x: (x['temp_f'] +  342.27) * 6 / 4
info=info.assign(temp_k=temp_k)
info
#------------------------
# Pandas DataFrame.astype()

import pandas as pd
a = {'col1': [1, 2], 'col2': [3, 4]}
info = pd.DataFrame(data=a)
info.dtypes
# We convert it into 'int64' type.
info.astype('int32').dtypes
info.astype({'col1': 'int64'}).dtypes
x = pd.Series([1, 2], dtype='int64')
x.astype('category')
cat_dtype = pd.api.types.CategoricalDtype(categories=[2, 1], ordered=True)
print(cat_dtype)
x.astype(cat_dtype)
x1 = pd.Series([1,2])
x2 = x1.astype('int64', copy=False)
x2[0] = 10
x1  # note that x1[0] has changed too
#-------------------
# count
import pandas as pd
import numpy as np
info = pd.DataFrame({"Person":["Parker", "Smith", "William", "John"],"Age": [27., 29, np.nan, 32]})
info.count()

import pandas as pd
import numpy as np
info = pd.DataFrame({"Person":["Parker", "Smith", "William", "John"],"Age": [27., 29, np.nan, 32]})
info
info.count(axis='columns')
#------------------------------------------------------------
import pandas as pd
import numpy as np
a1 = pd.Series([1, 2, 3])
a1.describe()
#-------------------------------------
import pandas as pd
import numpy as np
a1 = pd.Series(['p', 'q', 'q', 'r'])
a1.describe()
#--------------------------
import pandas as pd
import numpy as np

info = pd.DataFrame({'categorical': pd.Categorical(['s','t','u']),'numeric': [1, 2, 3],'object': ['p', 'q', 'r'] })
info
info.describe()
info.describe(include='all')
info.numeric.describe()
info = pd.DataFrame({'categorical': pd.Categorical(['s','t','u']),'numeric': [1, 2, 3],'object': ['p', 'q', 'r'] ,'age':[18,25,28]})
info.describe(include=[np.number])
info.describe(include=[np.object_])
info.describe(include=['category'])
info.describe(exclude=[np.number])
info.describe(exclude=[np.object_])
#------------------------
import pandas as pd
emp = {"Name": ["Parker", "Smith", "William", "Parker"],"Age": [21, 32, 29, 21]}
info = pd.DataFrame(emp)
info
info = info.drop_duplicates()
print(info)

#---------------------------------
import pandas as pd
import numpy as np

data = {'Name': ['Parker', 'Smith', 'John', 'William','Rajasekar'],
        'Percentage': [82, 98, 91, 95,100],
        'Course': ['B.Sc', 'B.Sc','B.A', 'M.Phill', 'B.A']}
df = pd.DataFrame(data)
df
grouped = df.groupby('Course')["Percentage"].sum()
print(grouped)
grouped = df.groupby('Course')#["Percentage"].sum()
print(grouped['Percentage'].agg(np.mean))
#------------------
info = pd.DataFrame({'language':['C', 'C++', 'Python', 'Java','PHP']})
info.head()
info.head(3)
#---------------------
import pandas as pd
import numpy as np

info = pd.DataFrame(np.random.randn(4, 2), columns=['col1', 'col2'])
info
for row_index, row in info.iterrows():
    print(row_index, row)

#-----------------------------

import pandas as pd
# Define a dictionary containing information of employees
info = {'name': ['Parker', 'Smith', 'William', 'Robert'],
              'age': [38, 47, 44, 34],
               'language': ['Java', 'Python', 'JavaScript', 'Python']}
# Convert dictionary into DataFrame
info_pd = pd.DataFrame(info)
# Before renaming columns
print(info_pd)
info_pd.rename(columns = {'name':'Name'}, inplace = True)
# After renaming columns
print("\nAfter modifying first column:\n", info_pd.columns)
#----------------------------
import pandas as pd
# Define a dictionary containing information of employees
info = {'name': ['Parker', 'Smith', 'William', 'Robert'],
              'age': [38, 47, 44, 34],
               'language': ['Java', 'Python', 'JavaScript', 'Python']}
# Convert dictionary into DataFrame
info_pd = pd.DataFrame(info)
# Before renaming columns
print(info_pd)
info_pd.rename(columns = {'name':'Name', 'age':'Age', 'language':'Language'}, inplace = True)
# After renaming columns
print(info_pd.columns)
#---------------------------
import pandas as pd
info = pd.DataFrame({'data1': [2, 4, 8, 0],'data2': [2, 0, 0, 0],  'data3': [10, 2, 1, 8]}, index=['John', 'Parker', 'Smith', 'William'])
info
#random_state->fix the value till the program ends
info['data1'].sample(n=3, random_state=1)
info
info.sample(frac=0.5, replace=True, random_state=1)
info.sample(n=2, weights='data3', random_state=1)
#-----------------------------------------
import pandas as pd
info= pd.DataFrame({'a_data': [45, 28, 39, 32, 18],
'b_data': [26, 37, 41, 35, 45],
'c_data': [22, 19, 11, 25, 16]})
info
info.shift(periods=2)
#---------------------
import pandas as pd
info= pd.DataFrame({'a_data': [45, 28, 39, 32, 18],
'b_data': [26, 38, 41, 35, 45],
'c_data': [22, 19, 11, 25, 16]})
info.shift(periods=2)
info.shift(periods=2,axis=1)
info.shift(periods=2,axis=1,fill_value= 70)
#--------------------------------
import pandas as pd
import numpy as np

info = pd.DataFrame(np.random.randn(10, 2), index=[1, 3, 7, 2, 4, 5, 9, 8, 0, 6], columns=['col2', 'col1'])
print(info)
#-----------------------------
import pandas as pd
import numpy as np
info=pd.DataFrame(np.random.randn(10,2),index=[1,2,5,4,8,7,9,3,0,6],columns = ['col4','col3'])
info=info.sort_index()
print(info)
#----------------
import pandas as pd
import numpy as np

info = pd.DataFrame(np.random.randn(10, 2), index=[1, 4, 7, 2, 5, 3, 0, 8, 9, 6], columns=['col4', 'col5'])
info
info_2 = info.sort_index(ascending=False)
print(info_2)
#--------------------
import pandas as pd
import numpy as np

info = pd.DataFrame(np.random.randn(10, 2), index=[1, 4, 8, 2, 0, 6, 7, 5, 3, 9], columns=['col4', 'col7'])
info_2 = info.sort_index(axis=1)
print(info_2)
#------------------
import pandas as pd
import numpy as np
info = pd.DataFrame({'col1':[7,1,8,3],'col2':[8,12,4,9]})
info_2 = info.sort_values(by='col2')
print(info_2)
info_2 = info.sort_values(by='col1')
print(info_2)

#-------------------------------

import pandas as pd
# Creating the DataFrame
info = pd.DataFrame({'Weight':[27, 44, 38, 10, 67],
                   'Name':['William', 'John', 'Smith', 'Parker', 'Jones'],
                   'Age':[22, 17, 19, 24, 27]})
# Create the index
index_ = pd.date_range('2010-10-04 06:15', periods = 5, freq ='h')
# Set the index
info.index = index_
# Print the DataFrame
print(info)

# Create the index
index_ = pd.date_range('2010-10-04 06:15', periods = 5, freq ='ME')#MONTH
# Set the index
info.index = index_
# Print the DataFrame
print(info)

# return the transpose
result = info.transpose()
# Print the result
print(result)
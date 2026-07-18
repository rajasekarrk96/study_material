# importing libraries
import pandas as pd
import numpy as np
# import scipy
#
from sklearn.preprocessing import MinMaxScaler,LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("C:/Users/Rajasekar/OneDrive/_12_DATA_ANALYST/_data_preprocessing/_02_preprocessing/Data.csv")
# print(data.head())
# data.info()
# data.columns()
# data.isnull().sum()
data.count()

x=data[['Country','Age','Salary']].values
y=data['Purchased'].values

# print(x)
imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
x[:,1:]=imputer.fit_transform(x[:,1:])
data=pd.DataFrame(x)
# print(data.isnull().sum())
#_labelencoder, onehot encoder
t=LabelEncoder()
x[:,0] = t.fit_transform(x[:,0])
# print(x)
y=t.fit_transform(y)
print(y)
#standard
# d scalar->feature scaling(largest dataset)
#------------- model training
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

from sklearn.linear_model import LogisticRegression

lr=LogisticRegression()

lr.fit(x_train,y_train)

predict=lr.predict(x_test)
print(predict)
print(y_test)
# Evaluate the model
accuracy = accuracy_score(y_test, predict)
print("Accuracy:", accuracy)
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 22:00:02 2022

@author: rajas
"""
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt 

Year = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]


Temp_I = [0.72,0.61,0.65,0.68,0.75,0.90,1.02,0.93,0.85,0.99,1.02]
#____________________________________________________________________

plt.plot(Year,Temp_I)
plt.xlabel("year")
plt.ylabel("temp_index")
plt.title("line graph",{"fontsize":12,"horizontalalignment":"center"})
plt.show()
#____________________________________________________________________

Month = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] 

Customer1 = [12,13,9,8,7,8,8,7,6,5,8,10]

Customer2 = [14,16,11,7,6,6,7,6,5,8,9,12]

#____________________________________________________________________

plt.plot(Month,Customer1)

plt.plot(Month,Customer2)

plt.show()

#____________________________________________________________________

#can get color from matplot color website
plt.plot(Month,Customer1,color="red")

plt.plot(Month,Customer2,color='orange')

plt.show()

#____________________________________________________________________

#can choose marker from matplot marker site

plt.plot(Month,Customer1,color="red",label="Customer1",marker="o")

plt.plot(Month,Customer2,color='orange',label="Customer2",marker="*")

plt.xlabel("month")

plt.ylabel("unit")

plt.title("bill graph")

#gives label side color works only if we give labels
plt.legend()

plt.show()

#____________________________________________________________________


plt.plot(Month,Customer1,color="red",label="Customer1",marker="o")

plt.plot(Month,Customer2,color='orange',label="Customer2",marker="*")

plt.xlabel("month")

plt.ylabel("unit")

plt.title("bill graph")

#can choose location from matplot legend loaction stie
plt.legend(loc="lower left")

plt.show()

#____________________________________________________________________

plt.subplot(1,2,1)

plt.plot(Month,Customer1,color="red",label="Customer1",marker="o")

plt.xlabel("month")

plt.ylabel("unit")

plt.title("bill graph 1")

plt.legend(loc="lower left")

plt.show()

plt.subplot(1,2,2)

plt.plot(Month,Customer2,color='orange',label="Customer2",marker="*")

plt.xlabel("month")

plt.ylabel("unit")

plt.title("bill graph 2")

plt.legend(loc="lower left")

plt.show()

#____________________________________________________________________

plt.scatter(Month,Customer1,color="red",label="customer1")

plt.scatter(Month,Customer2,color="blue",label="customer2")

plt.xlabel("month")

plt.ylabel("power")

plt.title("scatter plot")

plt.grid()

plt.legend(loc="best")

plt.show()

#____________________________________________________________________

plt.hist(Customer1,bins=20,color="green")

plt.xlabel("Month")

plt.ylabel("power")

plt.title("histogram")

plt.show()

#____________________________________________________________________

plt.bar(Month,Customer1,width =0.8,color="b")

plt.show()

#____________________________________________________________________

plt.bar(Month,Customer1,color="red",label="customer1")

plt.bar(Month,Customer2,color="blue",label="customer2")

plt.xlabel("month")

plt.ylabel("power")

plt.title("scatter plot")

plt.legend(loc="best")

plt.show()


#____________________________________________________________________

bar_w=0.4

Month_b=np.arange(12)

plt.bar(Month_b,Customer1,bar_w,color="green",label="cus")

plt.bar(Month_b+bar_w,Customer2,bar_w,color="blue",label="cus2")

plt.show()

#____________________________________________________________________

plt.xticks(Month_b+(bar_w)/12,('Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

bar_w=0.4

Month_b=np.arange(12)

plt.bar(Month_b,Customer1,bar_w,color="green",label="cus")

plt.bar(Month_b+bar_w,Customer2,bar_w,color="blue",label="cus2")

plt.show()

#____________________________________________________________________

plt.boxplot(Customer1,notch=True, vert=False)

#____________________________________________________________________

plt.boxplot(Customer1,notch=False, vert=False)

#____________________________________________________________________

plt.boxplot(Customer1,notch=False, vert=True)

#____________________________________________________________________

plt.boxplot([Customer1,Customer2],patch_artist=True,
            boxprops=dict(facecolor="red",color="red"),
            whiskerprops=dict(color="green"),
            capprops=dict(color="blue"),
            medianprops=dict(color="yellow"))

plt.show()
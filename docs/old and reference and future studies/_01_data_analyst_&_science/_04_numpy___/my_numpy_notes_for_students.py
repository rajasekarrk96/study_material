#can view array in console variable explorer and click the varibale name to view it graphical
np1=np.array([[1,3],[4,5]])

np2=np.array([[3,4],[6,7]])

#numpy array multiplication(matrix)
np3=np1@np2

print(np3)

#-------------------------------------------------

#normal multiple with cell values
np4=np1*np2

print(np4)
#-------------------------------------------------
#numpy array multiplication(matrix)
np5=np.dot(np1,np2)

print(np5)

#-------------------------------------------------
#normal multiple with cell values
np6=np.multiply(np1,np2)

print(np6)
#-------------------------------------------------

sub2=np.subtract(np1,np2)
print(sub2)
#-------------------------------------------------
sum2=np.sum(np1)
print(sum2)
#-------------------------------------------------
bnp=np1+3

print(bnp)
#-------------------------------------------------

d=np.divide([12,14,15],5)

print(d)
#-------------------------------------------------
d2=np.floor_divide([12,14,15],5)

print(d2)

#-------------------------------------------------
no=np.random.standard_normal((3,4))

print(no)
#-------------------------------------------------
uo=np.random.uniform(1,12,(3,4))

print(uo)
#-------------------------------------------------
randf=np.random.rand()
print(randf)
#-------------------------------------------------
#random integer
randi=np.random.randint(1,50,(2,5))
print(randi)
#-------------------------------------------------
ze=np.zeros((3,4))
print(ze)
#-------------------------------------------------
one=np.ones((3,4))
print(one)
#-------------------------------------------------
f_a=np.logical_and(randi>30,randi<50)
print(f_a)
#-------------------------------------------------
f_r=randi[f_a]
print(f_r)
#___________________________________________
num=np.array([[1,2,3],[4,6,7]])
va=np.var(num,axis=1)#axis does it by rows sepereately
print(va)
#-------------------------------------------------
num=np.array([[1,2,3],[4,6,7]])
va=np.var(num,axis=0)#axis does it by COLUMN sepereately
print(va)
#___________________________________________
num=np.array([[1,2,3],[4,6,7]])
va=np.var(num)
print(va)
#________________________________________________
# Array Concatenation

# The numpy provides us with the vertical stacking and horizontal stacking which allows us to concatenate two multi-dimensional arrays vertically or horizontally.

# Consider the following example.

# Example
import numpy as np
a = np.array([[1,2,30],[10,15,4]])
b = np.array([[1,2,3],[12, 19, 29]])
c=np.vstack((a,b))
print("Arrays vertically concatenated\n",c)
d=np.hstack((a,b))
print("Arrays horizontally concatenated\n",d)

#___________________________________________
import numpy as np
print("Concatenating two string arrays:")
print(np.char.add(['welcome','Hi'], [' to Javatpoint', ' read python'] ))

#___________________________________________

import numpy as np
print("Printing a string multiple times:")
print(np.char.multiply("hello ",3))
#___________________________________________

import numpy as np
print("Padding the string through left and right with the fill char *");
#np.char.center(string, width, fillchar)
print(np.char.center("Javatpoint", 20, '-'))

#___________________________________________

import numpy as np
print("Splitting the String word by word..")
print(np.char.split("Welcome To Javatpoint"),sep = " ")
#___________________________________________

import numpy as np
print("Splitting the String line by line..")
print(np.char.splitlines("Welcome\nTo\nJavatpoint"))
#___________________________________________

import numpy as np
print(np.char.join(':','HM'))
#___________________________________________
import numpy as np
str = "Welcome to Javatpoint"
print("Original String:",str)
print("Modified String:",end=" ")
print(np.char.replace(str, "Welcome to","www."))
#___________________________________________
import numpy as np
enstr = np.char.encode("welcome to javatpoint", 'cp500')
dstr =np.char.decode(enstr, 'cp500')
print(enstr)
print(dstr)
# | Encoding       | Description & Use Case                                                                |
# | -------------- | ------------------------------------------------------------------------------------- |
# | `'utf-8'`      | Most common encoding. Variable-length. Supports all Unicode characters. Web standard. |
# | `'ascii'`      | Old standard. Only supports 128 characters. Fast but very limited.                    |
# | `'latin1'`     | Also called ISO-8859-1. Supports Western European languages.                          |
# | `'utf-16'`     | Fixed-size (mostly 2 bytes). Used by Windows and some older systems.                  |
# | `'cp1252'`     | Microsoft variant of latin1. Used on many Windows systems.                            |
# | `'utf-32'`     | Fixed 4-byte encoding. Simple but large in size.                                      |
# | `'cp037'`      | Another EBCDIC variant used in U.S. mainframes.                                       |
# | `'big5'`       | Encoding for Traditional Chinese.                                                     |
# | `'shift_jis'`  | Encoding for Japanese.                                                                |
# | `'gb2312'`     | Simplified Chinese encoding.                                                          |
# | `'iso-8859-x'` | Variants for many regional languages (e.g., `-5` for Cyrillic, `-7` for Greek).       |

enstr1 = np.char.encode("welcome to javatpoint", 'big5')
dstr1 =np.char.decode(enstr1, 'cp037')
print(enstr1)
print(dstr1)

#___________________________________________
import numpy as np
arr = np.array([0, 30, 60, 90, 120, 150, 180])
print(np.pi)
print("\nThe sin value of the angles",end = " ")
print(np.sin(arr * np.pi/180))
print("\nThe cosine value of the angles",end = " ")
print(np.cos(arr * np.pi/180))
print("\nThe tangent value of the angles",end = " ")
print(np.tan(arr * np.pi/180))
print(np.pi)
#___________________________________________
import numpy as np

arr = np.array([0, 30, 60, 90])
print("printing the sin values of different angles")

sinval = np.sin(arr * np.pi / 180)

print(sinval)
print("printing the inverse of the sin")
cosec = np.arcsin(sinval)

print(cosec)

print("printing the values in degrees")
print(np.degrees(cosec))

print("\nprinting the cos values of different angles")
cosval = np.cos(arr * np.pi / 180)

print(cosval)
print("printing the inverse of the cos")
sec = np.arccos(cosval)
print(sec)

print("\nprinting the values in degrees")
print(np.degrees(sec))

print("\nprinting the tan values of different angles")
tanval = np.tan(arr * np.pi / 180)

print(tanval)
print("printing the inverse of the tan")
cot = np.arctan(tanval)
print(cot)

print("\nprinting the values in degrees")
print(np.degrees(cot))
#___________________________________________
import numpy as np
arr = np.array([12.202, 90.23120, 123.020, 23.202])
print("printing the original array values:",end = " ")
print(arr)
print("Array values rounded off to 2 decimal position",np.around(arr, 2))
print("Array values rounded off to -1 decimal position",np.around(arr, -1))
print("Array values rounded off to -1 decimal position",np.around(arr, -2 ))
#___________________________________________

import numpy as np
arr = np.array([12.202, 90.23120, 123.020, 23.202])
print(np.floor(arr))

#___________________________________________

import numpy as np
arr = np.array([12.202, 90.23120, 123.020, 23.202])
print(np.ceil(arr))

#___________________________________________
'''statistical'''
import numpy as np

a = np.array([[2, 10, 20], [80, 43, 31], [22, 43, 10]])

print("The original array:\n")
print(a)

print("\nThe minimum element among the array:", np.amin(a))
print("The maximum element among the array:", np.amax(a))

print("\nThe minimum element among the rows of array", np.amin(a, 0))
print("The maximum element among the rows of array", np.amax(a, 0))

print("\nThe minimum element among the columns of array", np.amin(a, 1))
print("The maximum element among the columns of array", np.amax(a, 1))
#___________________________________________
#peak to peak

import numpy as np

a = np.array([[2, 10, 20], [80, 43, 31], [22, 43, 10]])

print("Original array:\n", a)

print("\nptp value along axis 1:", np.ptp(a, 1))

print("ptp value along axis 0:", np.ptp(a, 0))

#___________________________________________
import numpy as np

a = np.array([[2, 10, 20], [80, 43, 31], [22, 43, 10]])

print("Array:\n", a)

print("\nPercentile along axis 0", np.percentile(a, 10, 0))

print("Percentile along axis 1", np.percentile(a, 10, 1))
print(a)
#------------------------------------------------------------

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Array:\n", a)

print("\nMedian of array along axis 0:", np.median(a, 0))
print("Mean of array along axis 0:", np.mean(a, 0))
print("Average of array along axis 1:", np.average(a, 0))
print("Average of array along axis 1:", np.average(a, 1))

#___________________________________________
'''sorting & searching'''
import numpy as np

a = np.array([[10, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Sorting along the columns:")
print(np.sort(a))

print("Sorting along the rows:")
print(np.sort(a, 0))

data_type = np.dtype([('name', 'S10'), ('marks', int)])

arr = np.array([('Mukesh', 200), ('John', 251)], dtype=data_type)

print("Sorting data ordered by name")

print(np.sort(arr, order='name'))

print(np.sort(arr, order='marks'))
#___________________________________________

import numpy as np
#displays the index of element when it is sorted
a = np.array([90, 29, 89, 12])

print("Original array:\n", a)

sort_ind = np.argsort(a)

print("Printing indices of sorted data\n", sort_ind)

sort_a = a[sort_ind]

print("printing sorted array")

for i in sort_ind:
    print(a[i], end=" ")


#___________________________________________

import numpy as np

a = np.array(['a', 'b', 'c', 'z', 'e'])

b = np.array([12, 90, 380, 12, 211])

ind = np.lexsort((a, b))

print("printing indices of sorted data",ind)

ind = np.lexsort(( b,a))

print(ind)

print("using the indices to sort the array")

for i in ind:
    print(a[i], b[i])
#------------------------------------------------------------

import numpy as np

b = np.array([12, 90, 380, 0, 211])

print("printing original array", b)

print("printing location of the non-zero elements")

print(b.nonzero())

#___________________________________________

import numpy as np

b = np.array([12, 90, 380, 12, 211])

print(np.where(b > 12))

c = np.array([[20, 24], [21, 23]])

print(np.where(c > 20))
#___________________________________________

import numpy as np

a = np.array([[1, 2, 3, 4], [9, 0, 2, 3], [1, 2, 3, 19]])

print("Original Array:\n", a)

print("\nID of array a:", id(a))

b = a

print("\nmaking copy of the array a")

print("\nID of b:", id(b))


b.shape = 4, 3

print("\nChanges on b also reflect to a:")
print(a)
a[0,0]=4
print(b)

#___________________________________________
import numpy as np

a = np.array([[1, 2, 3, 4], [9, 0, 2, 3], [1, 2, 3, 19]])

print("Original Array:\n", a)

print("\nID of array a:", id(a))

b = a.view()

print("\nID of b:", id(b))

print("\nprinting the view b")
print(b)

b.shape = 4, 3;

print("\nChanges made to the view b do not reflect a")
print("\nOriginal array \n", a)
print("\nview\n", b)

#------------------------------------------------------------

import numpy as np

a = np.array([[1, 2, 3, 4], [9, 0, 2, 3], [1, 2, 3, 19]])
print("Original Array:\n", a)
print("\nID of array a:", id(a))
b = a.copy()
print("\nID of b:", id(b))
print("\nprinting the deep copy b")
print(b)
b.shape = 4, 3;
print("\nChanges made to the copy b do not reflect a")
print("\nOriginal array \n", a)
print("\nCopy\n", b)
#___________________________________________
'''determinent'''
import numpy as np
a = np.array([[1,2],[3,4]])
print(np.linalg.det(a))
#___________________________________________
'''solve'''
import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[1,2],[3,4]])
print(np.linalg.solve(a, b))
#___________________________________________
import pandas as pd
import numpy as np
f=pd.read_excel("C:/Users/rajas/OneDrive/_12_01_DATA_ANALYST/_99_data_sets/AmazingMartEU2Geo.xlsx")
h=f.head()
print(h)
# convert single col
n=np.array(h["lat"])
print(n)
# full excel to numpy
fn=np.array(h)
print(fn)
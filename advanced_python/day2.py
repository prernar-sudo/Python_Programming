import numpy as np

# dimensionality
#0D, 1D, 2D ,3D , Multidimensional

#ndarray is homogeneous or heterogenous
#ndarray is homogeneous, but we can  give different data type as well 

#In NumPy, an ndarray (n-dimensional array) is homogeneous
# If you want an array that holds different types (heterogeneous), 
# you can create an ndarray with dtype=object, but then it loses many performance benefits.

arr1 = np.array([1,2,3,4,'cybrom'])
print(arr1)

#data type of an array

#python datatype: integer(int), string(str), 
#complex , boolean, float

#string - S
#integer - i
#float - f
#boolean - b
#complex -c 
#timedelta - m/u
#datetime - M/U
#unicode string - s

arr1 = np.array([1,2,3,4,5])
print(arr1)
print(arr1.dtype) 
# conversion of datatype -> 
#
arr2 = np.array([1,2,3,4,5], dtype='int32')
print(arr2)
print(arr2.dtype) 

#UNEVEN RESPONSE
#when we convert integer data to string then , it shows uneven behaviour of array
arr3 = np.array([1,2,3,4,5], dtype='S')#
print(arr3)
print(arr3.dtype) 

arr2 = np.array([1,2,3,4,5])
print(arr2)
print(arr2.dtype) 

arr2 = np.array([1,2,3,4,5], dtype='i2')
print(arr2)
print(arr2.dtype) 

arr2 = np.array([1,2,3,4,5], dtype='i4')
print(arr2)
print(arr2.dtype) 

arr2 = np.array([1,2,3,4,5], dtype='i8')#try with other unicode as well 
print(arr2)
print(arr2.dtype) 

# arr2 = np.array([1,2,3,4,5], dtype='i16') #----------------------depriciated
# print(arr2)
# print(arr2.dtype) 

arr2 = np.array([1,2,3,4,5], dtype='G')
print(arr2)
print(arr2.dtype) 

# indexing with array

list1 = [1,2,3,4,5]
print(list1[0])

#indexing of a 1D array
#indexing works on posit
arr1 = np.array






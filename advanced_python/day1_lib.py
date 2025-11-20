import numpy as np
arr = np.array([1,2,3,4])
print(arr)
print(type(arr))

#0D -> Dimension
#1D -> 
#2D ->
#3D -> multidimension
#json: java search -> dict

arr2 = np.array((1,2,3,4,5,6))
print(arr2)

#Dimension of an array
#0D array ----- single element
arr3 = np.array(42)
print(arr3)
#differnce in method and attribute
#ndim ---->attribute

list1=[1,2,3,[4,5,6,[7,8,9]]]
print(list1)
print(type(list1))
list2 = list1[3][3][2]
print(list2)
print(type(list2))

#1d array
arr5 = np.array([1,2,3,4,5])
print(arr5)
print("Dimensionality of array: ",arr5.ndim) #n dimension -> it tells dimensionality of array -> ndim is attribute

# 2D array
arr5 = np.array([[1,2,3],[4,5,6]])
print(arr5)
print(type(arr5))
print(arr5.ndim)


# 3D array
arr6 =np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr6)
print(type(arr6))
print('3D ARRAY: ',arr6.ndim)

#creation of an multi -dimensional array
arr7 =np.array([1],ndmin=10)
print(arr7)
print(arr7.ndim)



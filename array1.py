import numpy as np


a=np.array(10)#Zero dimension array
print(a)

print(a.ndim)
print(a.size)

print()
a1=np.array([1,2,3])#One dimension array
print(a1)


print()
a2=np.array([[1,2,3],[4,5,6]])#Two dimension array
print(a2)
print(a2.ndim)#tells dimension
print(a2.size)#no. of element
print(a2.shape)#no. of rows and columns
print(a2.reshape(3,2))
print()
a3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])#Multi dimension array
print(a3)
print(a3.ndim)
print(a3.size)
print(a3.shape)

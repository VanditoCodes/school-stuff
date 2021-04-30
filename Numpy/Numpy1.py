import numpy as np

a = np.array([1,2,3], dtype = int, order = 'c')
print(a, "\n")
#Order can be:
#   'c': row
#   'f': column
#   'a': major
print()
print()


b = np.array([2,3,4])
print(b)
print()

c = np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])
print(c)
print()
print()


d = np.arange(1,10)
print(d)
print()
print()


#object.shape
print(b.shape)
print(c.shape)
print(d.shape)
#Outputs shape of array in (y,x) form (or, in matrices terms, (i,j) form
print()

#object.ndim
print(b.ndim)
print(c.ndim)
print(d.ndim)
#Outputs number of dimensions of array, i.e. 1D, 2D, 3D
print()

#object.dtype and object.itemsize
print(b.dtype)
print(b.itemsize)
print(c.dtype)
print(c.itemsize)
print(d.dtype)
print(d.itemsize)
#object.dtype outputs type of data (int32 or int8)
#object.itemsize outputs size of data (i.e, int[n]/8)
print()
print()
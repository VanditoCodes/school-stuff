import random 
import numpy as np
a = np.array([[1,2,3],[4,5,66],[5,55,-7]], dtype = int, )
print(a)
b = np.arange(1,10)
print(b)
print(a.shape)
print(a.ndim)
print(b.dtype)
print(b.itemsize)
print(a[1,1])
print(a[:0])
a[0,1]=6


l = np.zeros((7,5))
m = np.ones((9,5))
k= np.full((3,3),77)
n = np.identity(33)
print('\n',n)
print('\n',l)
print('\n',m)
print('\n',k)

x = np.random.rand(5,5)
print(x)

y = np.random.randint(5,25, size = (4,5))
print(y)

u = np.array([[2,3]])
r = np.repeat(a,7,axis=0) #notesnotesbrohaha
print ('\n',u,'\n',r)

det = np.linalg.det(a)
print('\n',det)

inv = np.linalg.inv(a)
print('\n',inv)
print(np.median(a))

sort = np.sort(y)
print(sort)
print(np.unique(y))
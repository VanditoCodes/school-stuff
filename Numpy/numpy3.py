#Types of Arrays
import numpy as np

#Zeros Matrix
#np.zeros((y,x))
a = np.zeros((2,3))
print(a)
print()

#Ones matrix
#np.ones((y,x))
b = np.ones((2,3))
print(b)
print()

#Filled matrix (a(ij) = k)
#np.full((y,x),k)
c = np.full((2,3),47)
print(c)
print()

#Identity matrix
#np.identity(order)
d = np.identity(4)
print(d)
print()

#Random number matrix w values between 0 & 1.
e = np.random.rand(2,3)
print(e)
print()

#Random number matrix between given a1 and a2
#np.random.randint(a1,a2, size = (y,x))
f = np.random.randint(-4,3, size = (2,4))
print(f)
print()

#Repeat Array
g = np.array([[2,3]])
g1 = np.repeat(g, 2, axis = 0)
g2 = np.repeat(g, 2, axis = 1)
print(g1)
print(g2)
print()


#Copy Matrix
h = np.array([1,2,3,4])
h1= h.copy()
h1[0] = 100
print("Original: \n", h)
print("Copy: \n", h1)
#Maths
import numpy as np

a = np.array([1,2,3,4])
b = np.array([10,10,10,10])

print(b+a)
print(b-a)
print(a+1)
print(a-1)
print(a*2)
print(a/2)
print("\n\n")

#Matrix Multiplication
a = np.full((2,3),5)
b = np.identity(3)
product = np.matmul(a,b)
print(product)
print("\n")


#Determinant
c = np.identity(4)
#det = np.linalg.det(object)
determinant = np.linalg.det(c)
print(determinant)
print("\n")

#Inverse
d = np.random.randint(1,5, (2,2))
#np.linalg.inv(object)
inverse = np.linalg.inv(d)
print(d)
print(inverse)
print("\n")
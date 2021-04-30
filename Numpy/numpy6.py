#Reshaping
import numpy as np

before = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(before)
after = np.reshape(before, (4,3))
print(after)
a = np.reshape(before, (6,2))
print(a)
print("\n\n")

#Vertical Stacks
v1 = np.ones((2,4))
v2 = np.zeros((2,4))
print(np.vstack((v1,v2)))

#Horizontal Stacks
print(np.hstack((v1,v2)))
#Statistics
import numpy as np

a = np.array([[1,2,3,4],[4,6,7,8]])

#Basic Statistics
print(np.min(a))
print(np.max(a))
print(np.sum(a))
print(np.median(a))
print("\n\n")

#Sorting
b = np.random.randint(1,10, (2,5))
print(b)
sort = np.sort(b)
print(sort)
#arranges each row in ascending order
print("\n")

#Unique Elements
print(np.unique(a))

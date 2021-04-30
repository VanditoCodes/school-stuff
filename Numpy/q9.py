import numpy as np

array = np.random.randint(10, size=(5,5))
max = 0

print(array)
print("Maximum value:", np.max(array))
print("Minimum value:", np.min(array))

for i in array:
    if np.bincount(i).argmax()>max:
        max = np.bincount(i).argmax()

v = int(input("Enter scalar value: "))
def closestToScalar(array, v):
    i = np.abs(array - v).argmin()
    return array.flat[i]
        
print("Most frequently occuring:", max)
print("Closest value to scalar in array:", closestToScalar(array, v))
import numpy as np

x = np.random.randint(10, size=(5,5))
max = 0

print(x)
print("Maximum value:", np.max(x))
print("Minimum value:", np.min(x))

for i in x:
    if np.bincount(i).argmax()>max:
        max = np.bincount(i).argmax()

value = int(input("Enter scalar value: "))
def closestToScalar(array, value):
    i = np.abs(array - value).argmin()
    return x.flat[i]
        
print("Most frequently occuring:", max)
print("Closest value to scalar in array:", closestToScalar(x, value))
import numpy as np

f = np.array([[1,2,3,4,5,6,7,8,9],[11,12,13,14,15,16,17,18,19],[21,22,23,24,25,26,27,28,29]])
print(f)
print()

#f[y,x]
print(f[0,3])
print(f[1,3])
print(f[2,3])
print()
print()


#print row
print(f[2,:])

#print column
print(f[: , 3])
#prints in row form
print()
print()

#modify values
f[0,8],f[1,8],f[2,8] = 8999,9000,9001
print(f)
print()
print()
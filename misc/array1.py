import numpy as np
a = np.array([[1,2,3,7,6],[7,64,41,4,6],[96,4,5,3,5]], dtype= float, order='F')

c = np.array([[7,4,6,4,7],[12,343,4,454,0]], dtype=float, order='A')
print(a,"\n","\n")

l = np.arange(1,17)
a[0,1]=4

print(a[1,:],"\n")

g = np.random.randint(3,9, size=(3,3))
print(g)


f = np.repeat(a,4,axis=0)
print(f)


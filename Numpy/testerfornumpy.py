import numpy as np
a =  np.ones((6,6),dtype = 'int32')
b = np.zeros((4,4),dtype = 'int32')
print(a,'\n',b)
c = np.ones((1,1))
b[1:3,1:3] = c
a[1:5,1:5] = b
print(a)
    
d = b.copy()
d[3]=5
print(d)
print(b,'\n')

e  = np.array([1,1,2], dtype = 'int32')
f  = np.array([2,1,2], dtype = 'int32')
result = np.matmul(e,f)
print(result)   

print(np.linalg.inv(    ))
#Bar charts
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0,3.14*3,0.5)
b = np.cos(a)

plt.bar(a,b, width = 0.1, color = 'black', orientation = 'vertical')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cos function')
plt.show()

#histogram
plt.hist(b,a)
#Demonstration
import numpy as np
import matplotlib.pyplot as plt
import math


#Example 1
x = np.arange((-2*math.pi),(2*math.pi), 0.01)

y = np.sin(x)

plt.plot(x,y, linestyle = '--', linewidth = 2)

plt.show()


#Example 2
a = np.arange(-4,4,0.1)
b = 2*a**3 - 3*a**2 + 2*a + 3

plt.plot(a,b, marker = "x")
plt.title('Functions!')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.show()
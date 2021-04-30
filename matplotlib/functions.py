import numpy as np
import matplotlib.pyplot as plt
import math

a = np.arange(0,2*(math.pi),0.1)
b = np.sin(a)

plt.plot(a,b, linestyle = '--', linewidth = 1)
plt.grid(True)
plt.show()


y = np.arange(0,80,5)
x = 5*y**4 -3*y**2 + +4*y**3 -16*y +8

plt.plot(y,x, marker = 'x', linewidth = 1, label)
plt.legend()
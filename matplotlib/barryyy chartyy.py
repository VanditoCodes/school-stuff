import numpy as np
import matplotlib.pyplot as plt
from math import pi

a = np.arange(0,2*pi,0.1)
b= np.cos(a)

plt.bar(a,b, width = 0.1, color ='pink', orientation = 'vertical')

plt.show()

plt.hist(b,a)
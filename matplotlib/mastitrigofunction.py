import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0,3.14*3,0.5)
b = np.cos(a)

plt.plot(a,b)
plt.bar(a,b, width=0.1, color = 'black')
plt.show()
plt.hist(b,a)

plt.show()

x = np.arange(0,10)
y = 5*((1-0.33))**x

plt.plot(x,y, marker = '.', label = 'vandit ki zindagi')
plt.xlabel('Time(per 2 years)')
plt.ylabel('Happiness(out of 10)')
plt.legend()
plt.savefig('zindagi.png')
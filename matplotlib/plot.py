import numpy as np
import matplotlib.pyplot as plt

a = np.random.randint(1,10, (100))
b = np.arange(0,10,0.1)

plt.plot(b,a)
plt.show()

plt.plot(b,a, label = "Original")
plt.plot(a,b,label="90 degree")

plt.xlabel("Numberx")
plt.ylabel("Numbyrs")
plt.grid(True)
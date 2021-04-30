import numpy as np
import matplotlib.pyplot as plt

a = np.random.randint(1,500, (10))
b = np.arange(1,11)


plt.plot(a,b, alpha = 1, antialiased = 'True', color = 'Black', label = 'Blacky boi', linestyle = "-", linewidth = 2, marker = '.')

plt.legend()
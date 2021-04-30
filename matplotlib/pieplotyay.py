import numpy as np
import matplotlib.pyplot as plt

a = np.arange(20,30,2)
b = ["10%","20%","30%","5%","23%"]
c = ['c','m','y','k','r']

plt.pie(a, labels =b, explode = [0,0.1,0,0,0], colors = c, shadow = 0)

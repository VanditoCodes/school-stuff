import numpy as np
import matplotlib.pyplot as plt

b = np.arange(0.1,0.5,0.1)
a = ["10%","30%","20%","40%"]
colors = ['c','m','yellow','k']
plt.pie(b,labels=a, explode = [0.01,0.01,0.01,0.01], colors = colors, shadow = 0)
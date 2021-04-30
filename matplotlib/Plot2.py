import numpy as np
import matplotlib.pyplot as plt

a = np.random.randint(1,10, (100))
b = np.arange(0,10,0.1)

plt.plot(b,a, alpha = 5,  antialiased = 'True', color = 'red', label = 'Black line', linestyle = "--", linewidth = 1, marker = 's')
plt.legend()
#Most attributes are self explanatory, and yet
'''
alpha: transperency
antialiased: antialiasing
marker: point markers, basically whatever character you want. e.g x,+,.,^,v,o,s,<,>
color: color of line
label: label of line
linestyle: ':','--','-.','-'
linewidth: thickness of line
'''

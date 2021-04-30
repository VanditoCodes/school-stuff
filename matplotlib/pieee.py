import matplotlib.pyplot as plt
import numpy as np
a = np.arange(40,50,2)
b = ['10%','20%','30%','40%','10%']
c = ['c','m','y','k','r']
plt.pie(a,labels=b, explode = [0,0.01,0.1,1,0], colors = c, shadow = 2)
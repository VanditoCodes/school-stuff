import numpy as np
import matplotlib.pyplot as plt

a = np.random.randint(0,125, (125))
b = np.arange(125)

#line graph
plt.plot(b,a, label = "Original")

#renderer
plt.show()

#save
plt.savefig('nice.png')
#will give blank image in this case, since renderer has alreadybeen used for show. Same plot no longer in mem.

#Text
#
plt.plot(b,a, label = "Original")
plt.plot(a,b,label="90 degree")
#consecutive plt.plot()s plot two lines on same graph

plt.xlabel("Numberx")
plt.ylabel("Numbyrs")

plt.legend()
#plt.legend() shows line labels and colours

plt.title("A Graph")

#Axis limits
#plt.axis(xmin,xmax,ymin,ymax)

#Grid
plt.grid(True)

plt.savefig('bhaiya.png')
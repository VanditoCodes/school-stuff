import matplotlib.pyplot as mlt
import numpy as np

a = np.random.randint(1,10, (100))
b = np.arange(0,10,0.1)
c = np.random.randint(20,31)
mlt.plot(b,a)

mlt.savefig('hallo kween graph.png')
mlt.xlabel('hello')
mlt.ylabel('ok')
mlt.plot(a,c)
mlt.title('naam likh lo')

mlt.axis()

mlt.show()


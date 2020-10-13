import numpy as np
import pylab as pl

def loiES(β, **kwargs):
    AC = kwargs.get('AC')
    AB = kwargs.get('BC')
    dem = (AB-AC*np.cos(β))
    if dem != 0:
        return -np.arctan(AC*np.sin(β)/dem)+np.pi/4.8
    return 0


Y=[]
X =  np.linspace(np.pi/3, np.pi*1.6, 1000)
for i in X:
    Y.append(loiES(i, AC=8, BC=13))

pl.plot(X, Y)
pl.show()
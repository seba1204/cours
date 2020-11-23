import numpy as np
import matplotlib.pyplot as pl
from matplotlib.animation import FuncAnimation

def loiES(β, **kwargs):
    AC = kwargs.get('AC')
    AB = kwargs.get('BC')
    dem = (AB-AC*np.cos(β))
    if dem != 0:
        return -np.arctan(AC*np.sin(β)/dem)+np.pi
    return 0



Y=[]
X =  np.linspace(0, np.pi*2, 1000)
for i in X:
    Y.append(loiES(i, AC=8, BC=13))

pl.plot(X, Y)
pl.show()
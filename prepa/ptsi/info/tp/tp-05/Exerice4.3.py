import pylab as pl
import numpy as np

nbCotes=100
diam=1
angle=(2*np.pi)/nbCotes
x=[]
y=[]
for i in range(0, nbCotes+1):
    x.append(diam*(np.cos(i*angle)))
    y.append(diam*(np.sin(i*angle)))

pl.xlim(-1,8)
pl.ylim(-1,6)
pl.plot(x,y)
pl.show()
pl.close()

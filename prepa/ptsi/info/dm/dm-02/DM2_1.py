import numpy as np
import pylab as pl

def Euler(m:float, k:float, n:int = 1000, Tf:float=10, Ti:float=0):
    if m<=0:
        raise ValueError('mass has to be positive')
    h = (Tf-Ti)/n
    g = 9.81
    f = lambda x, y: -(k/m)* x *np.sqrt((x**2)+(y**2))
    
    X,Y = [0],[1]
    for i in range(n):
        X.append(X[i] + h * (f(X[i],Y[i])))
        Y.append(Y[i] + h * (-g-f(Y[i],X[i])))
    return (X,Y)

def traceResult(X,Y):
    pl.plot(X,Y)
    pl.show()

m=0.45
k = 8.9E-3


print(Euler(m,k))
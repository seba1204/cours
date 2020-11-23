import pylab as pl
import numpy as np

def g(x:float):
    if x >=0 and x<1:
        x=x**2
    elif x>=1 and x<=2:
        x=-(x**2)+x+1
    else:
        x=0
    return x


def Traceg(borneMin:float, borneMax:float, pas:float):
    xlabel="x"
    ylabel="g(x)"
    
    X = np.linspace(borneMin,borneMax,int((borneMax-borneMin)/pas))
    Y = [g(n)for n in X]
    
    pl.xlabel(xlabel)
    pl.ylabel(ylabel)
    pl.plot(X,Y,color="red", linewidth=2, label="g(x)")
    pl.legend()
    pl.show()
    pl.close() 
    

Traceg(0,2,0.01)
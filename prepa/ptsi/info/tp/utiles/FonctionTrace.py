import pylab as pl
import numpy as np
from scipy import misc 

def g(x:float):
    if x >=0 and x<1:
        x=x**2
    elif x>=1 and x<=2:
        x=-(x**2)+x+1
    else:
        x=0
    return x


def FonctionTrace(borneMin:float, borneMax:float, pas:float, fonction, optional_name="f(x)", optional_traceDerivee=False):
    xlabel="x"
    ylabel="f(x)"
    
    X = np.linspace(borneMin,borneMax,int((borneMax-borneMin)/pas))
    Y = [fonction(n)for n in X]
    Ynd = [misc.derivative(fonction, n) for n in X]
    
    pl.xlabel(xlabel)
    pl.ylabel(ylabel)
    pl.plot(X,Y,color="red", linewidth=2, label=optional_name)
    if optional_traceDerivee:
        pl.plot(X,Ynd,color="blue", linewidth=2, label=optional_name)    
    pl.legend()
    pl.show()
    pl.close() 
    

FonctionTrace(0, 2, 0.01, g, "", True)
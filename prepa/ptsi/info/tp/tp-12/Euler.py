# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np
import pylab as pl
import scipy.integrate as sc
import time
E=6
t=0.1
U0=0
def UVraie(x):
    return E*(1-np.exp(-x/t))

def UEulerExp(X:list):
    n=len(X)
    Tf=X[n-1]
    h=(Tf-0)/n
    Y=[U0]
    for k in range (1,n):
        Y.append(((h/t)*(E-Y[k-1]))+Y[k-1])
    return Y
def UEulerImp(X:list):
    n=len(X)
    Tf=X[n-1]
    h=(Tf-0)/n
    Y=[U0]
    for k in range (1,n):
        Y.append(1/(t+h)*(t*Y[k-1]+h*E))
    return Y
def Uodeint(x):
    return sc.odeint(f, U0, x)
    
def f(u,x):
    return ((E/t)-(1/t)*u)


def tracerFnEuler(Ti:float, Tf:float, n:float):
    X=np.linspace(Ti, Tf, n)
    
    pl.plot(X,Uodeint(X))
    pl.plot(X,UVraie(X))
    pl.plot(X,UEulerExp(X))
    pl.plot(X,UEulerImp(X))
    
    pl.ylim(0,E+1)
    pl.show()


def traceComplexite(mini:int,maxi:int,n:int,*args):
    X=np.linspace(mini,maxi,n)
    for f in args:
        Y=[]
        for i in range(n):
            t1=time.clock()
            f(X)
            Y.append(time.clock()-t1)
        pl.plot(X,Y,'*',label=str("coucou"))

traceComplexite(0,1,100,UEulerImp,UEulerExp,Uodeint,UVraie)
#pl.show()
#tracerFnEuler(0,1,100)

# -*- coding: utf-8 -*-
"""
Created on Fri May 24 15:00:42 2019

@author: ptsi
"""
import numpy as np
import pylab as pl

f= lambda x : np.exp(-x**(2))
g= lambda x : np.exp(x**(1/2))
I= lambda x : 1/(1+x)


def rect(f,a,b,n):
    S=0
    h=(b-a)/n
    for i in range (n):
        S+=h*f(a+h*i)
    return S
        
def trap(f,a,b,n):
    h=(b-a)/(2*n)
    S=h*(f(a)+f(b))
    
    for i in range (1,n):
        S+=2*h*f(a+2*h*i)
    return S

def Erreur(methode, n):    
    return abs(np.log(2)-methode(I,0,1,n))

def traceErreur(nmax):
    Ytrap=[]
    Yrect=[]
    X=[]
    for i in range(1, nmax):
        X.append(i)
        Ytrap.append(Erreur(trap,i))
        Yrect.append(Erreur(rect,i))
    pl.plot(X,Ytrap)
    pl.plot(X,Yrect)
    pl.show()

def traceErreurLog(nmax):
    Ytrap=[]
    Yrect=[]
    X=[]
    for i in range(1, nmax):
        X.append(np.log(i))
        Ytrap.append(np.log(Erreur(trap,i)))
        Yrect.append(np.log(Erreur(rect,i)))
    pl.plot(X,Ytrap)
    pl.plot(X,Yrect)
    print("alpha trap = ", determinAlpha(X, Ytrap))
    print("alpha rect = ", determinAlpha(X, Yrect))
    pl.show()
    
def determinAlpha(X, Y):
    alpha = (Y[len(Y)-1]-Y[0])/X[len(X)-1]-X[0]
    return alpha


traceErreur(100)
traceErreurLog(100)
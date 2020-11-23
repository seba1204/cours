# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np
import pylab as pl

def UEulerExp(X:list,k1,k2,A0,B0,C0):
    n=len(X)
    Tf=X[n-1]
    h,A,B,C=(Tf-0)/n,[A0],[B0],[C0]
    for k in range (1,n):
        A.append(A[k-1]*(1-h*k1))
        B.append(B[k-1]*(1-h*k2)+h*k1*A[k-1])
        C.append(C[k-1]+(h*k2*B[k-1]))
    return (A,B,C)



def tracerFnEuler(Ti:float, Tf:float, n:float,k1,k2,A0,B0,C0):
    X=np.linspace(Ti, Tf, n)
    Courbes=UEulerExp(X,k1,k2,A0,B0,C0)
    for courbe in Courbes:        
        pl.plot(X,courbe)
    pl.legend('ABC')
    pl.xlabel("Temps(s)")
    pl.ylabel("Concentration en (mol/L)")
    pl.show()
    
    
    
k=((0.2,0.2),
   (0.2,0.01),
   (0.01,0.02))
   
for a in k:
    tracerFnEuler(Ti=0,Tf=300,n=1000,k1=a[0],k2=a[1],A0=1,B0=0,C0=0)


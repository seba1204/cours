# -*- coding: utf-8 -*-
import numpy as np
import random
import time
import pylab as plt


def produit(A,X):
    Y=[]    
    n=np.shape(A)[0]
    Y=np.zeros((n,n))
    for i in range(n):
        for k in range(n):
            for j in range(n):            
                Y[i,j]=Y[i,j]+A[i,k]*X[k,0]
    return Y







def COLONNE(n):
    X=np.zeros((n,1))
    for i in range(n):
        X[i]=random.random()
    return X


def MATRICE(n):
    Y=np.zeros((n,n))    
     
    for i in range(n):
        for k in range(n):
            Y[i,k]=random.random()
    return Y
    
Temps=[]

N=[k for k in range(10,200,5)]
for k in N:
    A=MATRICE(k)
    X=COLONNE(k)
    t1=time.clock()
    produit(A,X)
    t2=time.clock()
    Temps.append(t2-t1)
    
plt.plot(np.log(N),np.log(Temps),'*')
plt.plot(np.log(N),np.log(N)-9)#vert
plt.plot(np.log(N),2*np.log(N)-12)#rouge
plt.plot(np.log(N),3*np.log(N)-14)#bleu
plt.xlabel('nombre de ligne de la matrice carree A')
plt.ylabel("temps d'execution de produit(a,X)")
plt.show()
plt.close()
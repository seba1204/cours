# -*- coding: utf-8 -*-
import numpy as np

C=np.array([[1,1,1,1],[1,2,3,1],[1,3,4,2]])


def permutation(C,i,j):    
   D=np.copy(C)  
   C[i]=D[j]
   C[j]=D[i]
   return (C)
   
def combinaison(D,i,j,m):
    D[i]=D[i]-m*D[j]
    return D
    
def multiplication(E,i,m):
    E[i]=m*E[i]
    return E
    
def Gauss(C):
    n=len(C[0])
    for j in range (0,n-1):
        k=j        
        while C[k,j]==0:
            k=k+1
        m=C[k,j]    
        permutation(C,j,k)
        multiplication(C,j,1/m)
        for k in range (j+1,n-1):
            combinaison(C,k,j,C[k,j])
    return C


def Jordan(C):
    n=np.shape(C)[0] #nombre de ligne de la matrice C = 3
    Y=np.zeros((n,1))
    Y[n-1]=C[n-1,(np.shape(C)[1])-1] #Défnition de la 3 ème ligne de Y
    for i in range (n-2,0,-1): #pour i allant de n-2
        somme=C[i,np.shape(C)[1]-1] 
        for k in (i+1,n):
            somme=somme-C[i,k-1]*Y[k-1]  
        Y[i]=somme
    return Y


print(Jordan(Gauss(C)))

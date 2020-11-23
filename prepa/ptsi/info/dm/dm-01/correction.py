import numpy as np
import random as random
import time
import matplotlib.pylab as plt

M=np.array([[1,0,1,3],[-1,2,2,-4],[1,2,1,1],[1,-2,-1,5]])  # MATRICE A INVERSER

def permutation(C,i,j): # C est la matrice augmentee, i et j deux indices de lignes
    D=np.copy(C)
    D[i,:]=C[j,:]  
    D[j,:]=C[i,:]  
    return D
    
def combinaison(C,i,j,mu): 
    D=np.copy(C)
    D[i,:]=C[i,:]-mu*C[j,:]  
    return D
    
def multiplication(C,i,mu):# C est la matrice augmentee, i l'indice d une ligne, mu un coefficient non nul, code Li remplacee par mu Li
    D=np.copy(C)
    D[i,:]=mu*C[i,:]  
    return D

def gauss(C): # C est la matrice augmentee, en retour la matrice reduite echelonnee par lignes
    n=np.shape(C)[0]
    for j in range(n):
        k=j
        while C[k,j]==0:
            k=k+1
        C=permutation(C,j,k)
        C=multiplication(C,j,1/C[j,j])
        for i in range(j+1,n):
            C=combinaison(C,i,j,C[i,j])
    return C


def jordan(C): # C est la matrice augmentee, en retour le resultat de AX=B
    n=np.shape(C)[0]
    D=gauss(C) # D est donc la la matrice reduite echelonnee par lignes
    X=np.zeros((n,1)) # le resultat final
    X[n-1,0]=D[n-1,n]
    for j in range(n-2,-1,-1):
        for k in range(j+1,n):
            X[j]=X[j]-D[j,k]*X[k]
        X[j]=D[j,n]+X[j]
    return X

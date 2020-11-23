import random as rd
import numpy as np
import time
import pylab as plt

def Produit(A,B):
    if (np.shape(A)[1] == np.shape(B)[0]):        
        n=np.shape(A)[0]
        p=np.shape(B)[1]
        Y=np.zeros((n,p))
        for i in range(np.shape(A)[0]):
            for j in range(np.shape(B)[1]):
                for k in range(np.shape(B)[0]):
                    Y[i,j]=Y[i,j]+A[i,k]*B[k,j]
        return Y
    else:
        return "error"

def Matrice(n:int, p:int):
    X=np.zeros((n,p))
    for i in range (n):
        for j in range (p):
            X[i,j]=rd.random()
    return X
def Permutation(C:type(np.array), i:int, j:int):
    C[i],C[j]=np.copy(C[j]),np.copy(C[i])
    return C
def Combinaison(C:type(np.array), i:int, j:int,µ:float):
    C[i]=np.copy(C[i])-µ*np.copy(C[j])
    return C  
def Multiplication (C:type(np.array),i:int,µ:float):  
    C[i]=µ*np.copy(C[i])
    return C


print(Multiplication(A,2,4))
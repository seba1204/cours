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
    if i==j:
        return C
    elif i in range(np.shape(C)[0]) or j in range(np.shape(C)[0]): 
        C[i],C[j]=np.copy(C[j]),np.copy(C[i])
        return C
    else:
        return "erreur"
def Combinaison(C:type(np.array), i:int, j:int,µ:float):
    C[i]=np.copy(C[i])-µ*np.copy(C[j])
    return C  
def Multiplication (C:type(np.array),i:int,µ:float):  
    C[i]=µ*np.copy(C[i])
    return C


Temps=[]
N=[k for k in range (10,1000,30)]
for n in N:
    A=Matrice(n,n)
    t1=time.clock()
    Permutation(A,1,3)
    t2=time.clock()
    Temps.append(t2-t1)

plt.plot(N,Temps)
#plt.plot(np.log(N), np.log(Temps),'bo')#linéarisation de la complexité
#plt.plot(np.log(N), 2*np.log(N)-12,'r')#modèle matrice colonne
plt.show()
plt.close()

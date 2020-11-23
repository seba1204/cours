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

def Colonne(n:int):
    X=np.zeros((n,1))
    for i in range (n):
        X[i]=rd.random()
    return X
def Matrice(n:int, p:int):
    X=np.zeros((n,p))
    for i in range (n):
        for j in range (p):
            X[i,j]=rd.random()
    return X
Temps=[]
N=[k for k in range (10,105,5)]
for n in N:
    A,B=Matrice(n,n),Matrice(n,n)
    t1=time.clock()
    Produit(A,B)
    t2=time.clock()
    Temps.append(t2-t1)

#plt.plot(N,Temps)
plt.plot(np.log(N), np.log(Temps),'bo')#linéarisation de la complexité
plt.plot(np.log(N), 3*np.log(N)-14,'r')#modèle matrice carrée
#plt.plot(np.log(N), 2*np.log(N)-12,'r')#modèle matrice colonne
plt.xlabel('Nombre de lignes de la matrice carrée')
plt.ylabel("Temps d'exécution de produit A*X")
plt.show()
plt.close()

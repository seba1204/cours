import numpy as np
#Necessaire pour générer des np.array inversibles (Python ne prends pas en compte les imports de dossier parents proprement)
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
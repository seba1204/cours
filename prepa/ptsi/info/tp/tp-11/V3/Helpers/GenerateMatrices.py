import numpy as np
import random as rd
import Shape as sp

def GenerateIdentity(shape, dtype):
    if (dtype!=float or dtype!=int):
        raise ValueError('Veuiller spécifier un type int ou float uniquement.')
        return
    if (not sp.isSqaure(shape)):
        raise ValueError('L\'identité doit être de dimension carrée, et non : {0}x{1}'.format(shape[0], shape[1]))
        return
    
    buffer = np.zeros(shape)
    for i in range (shape[0]):
        for j in range (shape[1]):
            if (i==j):
                buffer[i,j]=1
    return np.array(object=buffer, dtype=dtype)
            
def GenerateRandomArray(shape, dtype):
    if (dtype!=float and dtype!=int):
        raise ValueError('Veuiller spécifier un type int ou float uniquement.')
        return       
    buffer = np.zeros(shape)
    for i in range (shape[0]):
        for j in range (shape[1]):
            if (dtype==int):
                rand=rd.randint(0,100)
            elif (dtype==float):
                rand=rd.uniform(0.,100.)
            buffer[i,j]=rand
    return np.array(object=buffer, dtype=dtype)

def GenerateReversibleArray(shape, dtype):
    #buffer = GenerateIdentity(shape, dtype)
    """L'idée et de partir de l'identité puis de générer des opérations aléatoires (permautation, ...) pour arriver à une matrice inversible"""
    return np.array([[1,0,1,3],[-1,2,2,-4],[1,2,1,1],[1,-2,-1,5]])  # MATRICE A INVERSER
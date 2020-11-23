import numpy as np
import random as rd
from Helpers import Shape as sp
from Helpers import OperationsElementaires as op

def GenerateIdentity(shape, dtype=float):
    if (dtype!=float and dtype!=int):
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
    '''Il s'avère que cet algorythme ne marche pas... il génère parfois des matrices non inversibles'''
    buffer = GenerateIdentity(shape, dtype)
    n = rd.randint(10,30)
    for i in range(n):
        k=rd.randint(0,6)
        if k <= 2:
            buffer = op.multiplication(buffer, rd.randint(0,shape[0]-1), rd.randint(-8,-1))
        if k==3:
            buffer = op.permutation(buffer, rd.randint(0,shape[0]-1), rd.randint(0,shape[0]-1))
        if k>=4:
            buffer = op.combinaison(buffer, rd.randint(0,shape[0]-1), rd.randint(0,shape[0]-1), rd.randint(1,8))
    return buffer
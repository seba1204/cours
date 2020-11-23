# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:16:48 2019

@author: Chap
"""
def calculateNewInterval(L:list, n:int):
    """Retourne une liste d'entier allant de 0 à n-1 sans les entiers de la liste L"""
    A=[]
    contains=False
    for i in range(n):
        for j in L:
            if type(j)==int:
                if i==j:contains=True
        if not contains:
            A.append(i)
        contains=False
    return A
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:55:35 2019

@author: ptsi
"""
import numpy as np
import matplotlib.pyplot as pl

def dergreToRadian(i):
    return i * np.pi / 180 + np.pi/2


def extractNotes(path:str):
    X, Y=[], []
    try:
        file = open(path, "r")
        for row in file.readlines():
            try:
                X.append(dergreToRadian(float(row.split(',')[0].replace('\n', ''))))
                Y.append(dergreToRadian(float(row.split(',')[1].replace('\n', ''))))
            except:
                pass
    finally:
        file.close()
    return (X, Y)

def loiES(β, **kwargs):
    AC = kwargs.get('AC')
    AB = kwargs.get('BC')
    dem = (AB-AC*np.cos(β))
    if dem != 0:
        return -np.arctan(AC*np.sin(β)/dem)+np.pi
    return 0



Y=[]
A = extractNotes('Ressources/Loi_E S - Th & Ex.csv')
B = extractNotes('Ressources/Loi_E-S - Meca3D.csv')
X =  A[0]
pas = 1
for j in range(1):
    Y=[]
    for i in X:
        Y.append(loiES(i, AC=13+j*pas, BC=18+j*pas))
    pl.plot(X, Y, label=j)
    
        
    
pl.plot(A[0], A[1], label='expérimentale')
pl.legend()
pl.show()

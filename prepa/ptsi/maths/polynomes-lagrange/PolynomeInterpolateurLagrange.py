import numpy as np
import matplotlib.pyplot as pl


def extractNotes(path:str):
    Notes=[]
    try:
        file = open(path, "r")
        for row in file.readlines():
            try:
                Notes.append(float(row.split(';')[3].replace(',','.')))
            except:
                pass
    finally:
        file.close()
    return Notes


def polynomesLagrange(listOfPoints:list, nbPtsCourbeFinale:int):
    x,y=listOfPoints[0],listOfPoints[1]
    h = (max(x)-min(x))/ nbPtsCourbeFinale
    X=[h*k for k in range(nbPtsCourbeFinale)]
    pll = L(X, x, y)
    return (X, pll)
def li(X:float, i:int, x:list):
    L=1
    l=[]
    for j in range(len(x)):
        if (j != i):
            L*=(X-x[j])/(x[i]-x[j])
            l.append((X-x[j])/(x[i]-x[j]))
    return L
def L(X:float, x:list, y:list):
    if (len(x)!=len(y)):
        raise Error('x and y must have same dimension')
    else:
        Y=[]
        for xi in X:
            P=0
            for j in range(len(x)):
                P+=y[j]*li(xi, j, x)
            Y.append(P)
        return Y





Notes=extractNotes("notes.csv")
listPt = ([k for k in range(len(Notes))],Notes)
pl.plot(listPt[0], listPt[1], 'ro')
plLgr = polynomesLagrange(listPt, 1000)
pl.plot(plLgr[0], plLgr[1])
#pl.ylim((0,50))
pl.show()
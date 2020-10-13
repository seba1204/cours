import matplotlib.pyplot as plt
import numpy as np
import sys


a = 69.5
b = 82
l = 80
L = 290
p = 4
m = 0.65
g = 9.81

n = 1000
maxAngle = np.pi/2


def openCSV(path):
    X, Y = [], []
    file = open(path, "r")
    try:
        file = open(path, "r")
        for row in file.readlines():
            try:
                X.append(float(row.split(';')[0].replace(',', '.')))
                Y.append(float(row.split(';')[1].replace(',', '.')))
            except:
                pass
    finally:
        file.close()
    return (X, Y)


def lisser(X, Y, pres):
    pass


def convertRadToDeg(Y):
    converted = []
    for i in Y:
        converted.append(i * 180/np.pi)
    return converted


def geo(t):
    return np.arctan((l * np.cos(t) + a) / (l * np.sin(t) - b))


def statique(X):
    result = []
    for i in X:
        t = i * np.pi/180
        result.append((-p * m * g * L * l * np.cos(t) /
                       (2 * np.pi * np.sin(geo(t))))/1000)
    return result


exp01 = openCSV('Courbe_001_exp.csv')
mod01 = openCSV('Courbe_001_th1.csv')
X1 = exp01[0]
Y1 = exp01[1]
X2 = exp01[0]
Y2 = statique(X2)
X3 = mod01[0]
Y3 = mod01[1]
plt.plot(X1, Y1, label='exp')
#plt.plot(X2, Y2, label='th mod')
plt.plot(X3, Y3, label='th logiciel')
plt.legend()
plt.show()

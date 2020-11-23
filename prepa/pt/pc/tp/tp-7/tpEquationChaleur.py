import numpy as np
import os
import time
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors

N = 30


def initTab(dim):
    temp = np.array([[0 for k in range(dim)] for l in range(dim)])
    for i in range(0, dim):
        temp[i][0] = 10 * i
        temp[i][dim-1] = -10 * i
        temp[dim-1][i] = 100 - 20 * i
    return temp


def oneLoop(temp):
    dim = np.shape(temp)[0]-1
    newTemp = np.array(temp)
    delta = 0
    for line in range(1, dim):
        for row in range(1, dim):
            oldValue = newTemp[line][row]
            newValue = temp[line-1][row] + \
                temp[line+1][row] + \
                temp[line][row - 1] + \
                temp[line][row + 1]
            newValue /= 4
            newTemp[line][row] = newValue
            if (delta < abs(oldValue - newValue)):
                delta = abs(oldValue - newValue)
    return (delta, newTemp)


def allLoop(temp):
    i = 0
    delta = 2
    plt.pcolor(temp, cmap='RdBu_r')
    plt.colorbar(extend='max')
    plt.title('Equation de la chaleur')
    plt.draw()
    plt.pause(7)
    plt.clf()
    while(delta > 1):
        i += 1
        A = oneLoop(temp)
        delta = A[0]
        temp = A[1]
        plt.pcolor(temp, cmap='RdBu_r')
        plt.colorbar(extend='max')
        plt.title('Equation de la chaleur')
        plt.draw()
        plt.pause(0.0001)
        plt.clf()
    time.sleep(5)
    return temp


allLoop(initTab(N))

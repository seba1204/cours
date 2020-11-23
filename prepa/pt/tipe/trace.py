import os.path as Path
import matplotlib.pylab as plt
import numpy as np

from constants import STORAGE_PATH, LIST_MAXI_FILENAME

storagePath = Path.join(STORAGE_PATH, LIST_MAXI_FILENAME)
listOfPoints = open(storagePath).read().split(';')
listOfPointsBis = []
for point in listOfPoints:
    point = point.split(',')
    pointInt = []
    try:
        for coord in point:
            pointInt.append(int(coord))
        listOfPointsBis.append(pointInt)
    except:
        pass
l = len(listOfPointsBis)
lb = np.unique(np.array([listOfPointsBis[i][2] for i in range(l)])).tolist()
lbb = len(lb)-1
j = 0

C = []
xMin, xMax, yMin, yMax = 10000, 0, 10000, 0
for k in lb:
    A = np.array([listOfPointsBis[i][2] for i in range(l)])
    B = np.where(A == k)[0].tolist()

    X = [listOfPointsBis[i][0] for i in B]
    Y = [listOfPointsBis[i][1] for i in B]

    A = np.nonzero(np.array(Y))[0].tolist()

    X = [X[i] for i in A]
    Y = [Y[i] for i in A]

    if (min(X) < xMin):
        xMin = min(X)
    if (max(X) > xMax):
        xMax = max(X)
    if (min(Y) < yMin):
        yMin = min(Y)
    if (max(Y) > yMax):
        yMax = max(Y)

    C.append([X, Y])
xMax -= xMin
yMax -= yMin

plt.ion()
for X, Y in C:
    # print(str(j) + '/' + str(lbb), end="\r")

    X = [x - xMin for x in X]
    Y = [y - yMin for y in Y]

    axes = plt.gca()
    axes.set_xlim([0, xMax])
    axes.set_ylim([0, yMax])
    plt.plot(X, Y)
    plt.draw()
    plt.pause(0.004)
    plt.clf()
    j += 1

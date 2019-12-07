import numpy as np
import cv2.cv2 as cv
import time as t
import pylab as pl

FILE_NAME = 'test2.png'
NB_POINTS = 100
EPSILON = 10


def lineatize(frame):
    img = cv.imread(FILE_NAME)

    INTER_POINT = int(len(img[0]) / NB_POINTS)

    X = [k * INTER_POINT for k in range(NB_POINTS)]
    Y = []

    for x in X:
        maxi = 0
        indexMax = 0
        for y in range(0, len(img) - EPSILON):
            k = []  # Element dans Epsilon
            for e in range(y, y + EPSILON):
                if(img[y][x] == [255, 255, 255]).all():
                    k.append(1)
                else:
                    k.append(0)
            sk = sum(k)
            if(sk > maxi):
                maxi = sk
                indexMax = -y
        Y.append(indexMax)

    Y[0] = Y[1]
    # Y.append(Y[-1])

    pl.plot(X, Y)
    pl.show()

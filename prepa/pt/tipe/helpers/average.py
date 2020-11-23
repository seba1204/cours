import numpy as np
import cv2.cv2 as cv
import time


def average(frame, n):
    moy = ''
    frame = np.transpose(frame)
    x, y, z = 0, 0, 0
    for i in range(len(frame)):
        if (cv.countNonZero(frame[i])):
            # on fait la moyenne des points non nuls
            points = np.where(frame[i] == 255)[0]
            x, y, z = i, int(sum(points)/len(points)), n
        moy += '{}, {}, {};\n'.format(x, y, z)
    return moy


def createMaskFromPoints(width, height, listOfPoints):
    # On crée un mask vide en inversant longeur et largeur
    maskBis = np.zeros((height, width), np.uint8)

    # On récupère les coordonnées du point
    for x, y, z in listOfPoints:
        y = int(y)

        if (y >= width):
            y = width - 4
        elif (y <= 4):
            y = 4

        maskBis[x] = [0] * (y-4) + [255] * 4 + [0] * (width - y)
    return np.transpose(maskBis)


# DEPRECIATED
def getImageOfMasks(width, height, mask, listOfPoints):
    # On crée une image de couleur unie
    red = np.zeros((width, height, 3), np.uint8)
    red[:] = (0, 0, 255)

    blue = np.zeros((width, height, 3), np.uint8)
    blue[:] = (255, 0, 0)

    averageMask = createMaskFromPoints(width, height, listOfPoints)

    first = cv.bitwise_and(blue, blue, mask=mask)
    sec = cv.bitwise_and(red, red, mask=averageMask)
    return cv.add(sec, first)

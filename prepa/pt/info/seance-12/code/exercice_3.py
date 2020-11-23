import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as im


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                                Exercice 3                                 ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

from ressources.helpers import plotImage, img
from exercice_2 import geryScale, arrayToImage

# Question 1 ──────────────────────────────────────────────────────────────────


def hSymetry(greyScaleArray):
    reversedArray = np.empty_like(greyScaleArray)
    l = len(reversedArray)-1
    for i in range(l, -1, -1):
        reversedArray[l-i] = greyScaleArray[i]
    return reversedArray


def vSymetry(greyScaleArray):
    return (np.transpose((hSymetry(np.transpose(greyScaleArray)))))


# plotImage(geryScale(img), (1, 2))
# plotImage(vSymetry(geryScale(img)), show=True)


# Question 2 ──────────────────────────────────────────────────────────────────
# plotImage(geryScale(img), (2, 1))
# plotImage(vSymetry(geryScale(img)), show=True)


# Question 3 ──────────────────────────────────────────────────────────────────
def cos(x): return np.cos(x)


def sin(x): return np.sin(x)


def rotation(greyScaleArray, percentage):
    height, width = greyScaleArray.shape
    alpha = (percentage / 100) * (np.pi / 2)
    c, s = cos(alpha), sin(alpha)
    w = int(width * c + height * s)
    h = int(height * c + width * s)
    newArray = np.full((h, w), 255)
    rMatrix = np.array(np.array(((c, -s), (s, c))))
    for y in range(height):
        for x in range(width):
            try:
                nY, nX = np.dot(rMatrix, np.array((y, x)))
                nY = nY + width * s
                newArray[int(nY), int(nX)] = greyScaleArray[y][x]
            except IndexError:
                pass
    return (newArray)


# plotImage(rotation(geryScale(img), 30), show=True)
# arrayToImage(rotation(geryScale(img), 30)).save('Ressources/rotatedCat.jpg')

# Question 4 ──────────────────────────────────────────────────────────────────


def negative(greyScaleArray):
    return -greyScaleArray


# plotImage(negative(geryScale(img)), show=True)


# Question 5 ──────────────────────────────────────────────────────────────────
def seuil(greyScaleArray, seuil):
    return np.where(greyScaleArray < seuil, 0, 255)


plotImage(seuil(geryScale(img), 127), show=True)

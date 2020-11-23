import cv2.cv2 as cv
import numpy as np
import platform


def resizeFrame(windowsName, frame, returnRatio=False):

    # On n'a besoin de resize que sur windows
    if (platform.system() == 'Linux'):
        if (returnRatio):
            return (frame, 1)
        return frame

    # On récupère la taille de la fenêtre
    x, y, w, h = cv.getWindowImageRect(windowsName)

    # On récupère la taille de l'image
    width = len(frame[0])
    height = len(frame)
    # On regarde la taille limitante

    # On calcule la hauteur en supposant que la largeur est limitante
    ratio = getRatio(height, width)
    newHeight = w * height / width
    # Si la nouvelle hauteur est plus petit => ca passe
    # l'hyopthèse était juste
    if(newHeight < h):
        # largeur limitante
        dim = (w, newHeight)
    else:
        # print('hauteur limitante')
        ratio = getRatio(width, height)
        dim = (int(h * width / height), h)
    if(returnRatio):
        return (cv.resize(frame, dim), ratio)
    return cv.resize(frame, dim)


def addBackground(windowsName, frame, color=(36, 34, 33), returnOrigin=False):

    # On n'a besoin de resize que sur windows
    if (platform.system() == 'Linux'):
        if (returnOrigin):
            return (frame, (0,0))
        return frame

    # On récupère la taille de la fenêtre
    x, y, w, h = cv.getWindowImageRect(windowsName)

    # On récupère la taille de l'image
    width = len(frame[0])
    height = len(frame)

    # On crée une image vide de la taille de la fenêtre
    background = np.zeros((h, w, 3), np.uint8)

    # On la colore
    background[:] = color

    # On regarde quelle dimmension il faut centrer
    if (h == height):
        ax, ay = (w-width)//2, 0
    else:
        ax, ay = (w-width)//2, 0

    # On copie la frame dans l'image colorée
    background[ay:ay+height, ax:ax+width] = frame

    if(returnOrigin):
        return (background, (ax, ay))
    return background


def getRatio(a, b):
    return abs(a / b)

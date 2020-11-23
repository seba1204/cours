import cv2.cv2 as cv
import numpy as np
import os
from storage import getCroping, saveCroping
from helpers.resize import resizeFrame, addBackground
from constants import CROPING_ALPHA_ORIGINAL as ALPHA_ORIGINAL, CROPING_ALPHA_MASK as ALPHA_MASK, CROPING_BACKGROUND, CROPING_MASK_COLOR as MASK_COLOR
from storage import getCalibration


def addFrames(path):
    video = cv.VideoCapture(path)
    _, frame = video.read()

    calibration = getCalibration(path)
    if (calibration):
        h, s, v, step = calibration

        LOWER = np.array([h, s, v])
        UPPER = np.array([h + step, s + step, v + step])

    im = np.zeros(shape=[len(frame), len(frame[0]), 3], dtype=np.uint8)
    while _:

        if (calibration):
            # On transforme la frame en matrice de couleurs HSV
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            # On crée un masque => on enlève tous les pixels
            # en hors des couleurs extrêmes
            mask = cv.inRange(hsv, LOWER, UPPER)

            # On crée son inverse
            maskReversed = cv.bitwise_not(mask)

            # On crée un image toute verte
            green = np.zeros(frame.shape, np.uint8)
            green[:] = MASK_COLOR

            # On ne garde que la bonne partie de l'image verte
            greenMask = cv.bitwise_and(green, green, mask=mask)

            # On met du noir sur l'image originale à la place du mask
            maskedFrame = cv.bitwise_and(frame, frame, mask=maskReversed)

            # On combine les deux en mettant l'originale transparente
            frame = cv.addWeighted(
                greenMask, ALPHA_MASK, maskedFrame, ALPHA_ORIGINAL, 0)
        im = cv.addWeighted(im, 1., frame, 1., 0)
        _, frame = video.read()
    return im


def crop(fileName, forceUpdate=False):
    check = getCroping(fileName)
    if (not check or forceUpdate):
        # On crée une fenêtre
        cv.namedWindow('crop', cv.WND_PROP_FULLSCREEN)
        # On la déplace pour qu'elle soit dans le second écran
        cv.moveWindow('crop', -1936, -10)
        # On la met en plein écran
        cv.setWindowProperty(
            'crop', cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)

        # On aditionne toutes les images de la vidéo
        image = addFrames(fileName)

        # Paramètres du ROI
        showCrosshair = False
        fromCenter = False
        image, ratio = resizeFrame('crop', image, returnRatio=True)
        image, point = addBackground(
            'crop', image, CROPING_BACKGROUND, returnOrigin=True)

        # On sélectionne une partie de l'image
        x, y, w, h = cv.selectROI('crop', image, fromCenter, showCrosshair)

        # Mise à l'échelle
        x = int((x - point[0]) / ratio)
        y = int((y - point[1]) / ratio)
        w = int(w / ratio)
        h = int(h / ratio)

        a, b, c, d = y, y + h, x, x + w

        # On enregistre les données
        saveCroping(fileName, a, b, c, d)

        # On supprime la fennêtre
        cv.destroyAllWindows()
    else:
        a, b, c, d = check
    return (a, b, c, d)

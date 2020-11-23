import cv2.cv2 as cv
import numpy as np
import os
import helpers.keymap as key
from helpers.resize import resizeFrame, addBackground
from storage import getCalibration, saveCalibration
from constants import CALIBRATION_FRAME_RATE as FRAME_RATE, CALIBRATION_ALPHA as ALPAH, CALIBRATION_MASK_COLOR as MASK_COLOR, CALIBRATION_BACKGROUND as BACKGROUND


# ----------------------------------------------- <<- SETTINGS ->>

# time to wait between each frame (ms)
FRAME_RATE = 100

# opacity of original video [0 - 1]
ALPAH = 0.2

# color of mask (blue, green, red)
MASK_COLOR = (0, 255, 0)

# ----------------------------------------------- <<- SETTINGS ->>


def nothing(x):
    pass


def calibration(videoFile, forceUpdate=False):
    #              <<- Getting old data -->
    oldCalibration = getCalibration(videoFile)
    if (not oldCalibration or forceUpdate):
        if (isinstance(oldCalibration, tuple)):
            return calibrate(videoFile, oldCalibration)
        return calibrate(videoFile)
    else:
        return oldCalibration


def calibrate(videoFile, oldCalibration=(255, 255, 255, 50)):

    h, s, v, step = oldCalibration

    #                <<- Windows handle -->
    # On crée une fenêtre
    cv.namedWindow('calibration', cv.WND_PROP_FULLSCREEN)
    # On la déplace pour qu'elle soit dans le second écran
    cv.moveWindow('calibration', -1936, -10)
    # On la met en plein écran
    cv.setWindowProperty(
        'calibration', cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
    # On lui rajoute trois trackBar pour controller la calibration

    # On ajoute les trackBar
    cv.createTrackbar('H', 'calibration', h, 255, nothing)
    cv.createTrackbar('S', 'calibration', s, 255, nothing)
    cv.createTrackbar('V', 'calibration', v, 255, nothing)
    cv.createTrackbar('step', 'calibration', step, 100, nothing)

    #             <<- Video play & calibrate -->

    # Tant qu'on veut pas s'arrêter
    # (pour s'arrêter : appuyer sur échap)
    while(True):

        k = 0   # Keyboard var

        # On ouvre la vidéo
        video = cv.VideoCapture(videoFile)

        # On lit la première frame
        # _ = true si on a réussi à la lire
        _, frame = video.read()
        while _:

            # Avant tout, on redimensionne l'image à la taille de la fenêtre
            # Remarque : on pourrait ne le faire qu'au début, mais
            # si on redimmensionne la fenêtre ca marche plus de ouf...😑
            frame = resizeFrame('calibration', frame)

            # On lit les valeurs des trackBar
            h = cv.getTrackbarPos('H', 'calibration')
            s = cv.getTrackbarPos('S', 'calibration')
            v = cv.getTrackbarPos('V', 'calibration')
            step = cv.getTrackbarPos('step', 'calibration')

            # On créer les couleurs extrêmes
            lower = np.array([h, s, v])
            upper = np.array([h+step, s+step, v+step])

            # On transforme la frame en matrice de couleurs HSV
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

            # On crée un masque => on enlève tous les pixels
            # en hors des couleurs extrêmes
            mask = cv.inRange(hsv, lower, upper)

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
            output = cv.addWeighted(greenMask, 1, maskedFrame, ALPAH, 0)

            # On rajoute un background
            output = addBackground('calibration', output, BACKGROUND)

            # On lit le clavier pendant FRAME_RATE ms
            k = cv.waitKey(FRAME_RATE) & 0xFF

            # Si on appuie sur échappe on quitte tout
            if(k == key.ESCAPE):
                break

            # Sinon on affiche le résultat
            cv.imshow('calibration', output)

            # On lit la frame suivante
            _, frame = video.read()

        # On libère la vidéo
        video.release()

        if(k == key.ESCAPE):
            break

    # On enregistre les (nouvelles) valeurs de calibration
    saveCalibration(videoFile, h, s, v, step)

    cv.destroyAllWindows()
    video.release()

    return (h, s, v, step)

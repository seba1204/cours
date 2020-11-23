import cv2.cv2 as cv
import numpy as np
import os
import helpers.keymap as key
from datetime import datetime
from helpers.average import average as moy, createMaskFromPoints, getImageOfMasks
from crop import crop
from calibrate import calibration
from storage import saveList, saveStream
from constants import MAIN_FRAME_RATE as FRAME_RATE

# ----------------------------------------------- <<- SETTINGS ->>

VIDEO_FILE_NAME = "sources/set-1/car_to_track.mp4"

FORCE_CALIBRATING = True

FORCE_CROPING = False

# ----------------------------------------------- <<- SETTINGS ->>


# Calibrate
h, s, v, step = calibration(VIDEO_FILE_NAME, FORCE_CALIBRATING)


# Crop
a, b, c, d = crop(VIDEO_FILE_NAME, FORCE_CROPING)


# On crée la fenêtre
# cv.namedWindow('mask')
# On la déplace sur le second écran
# cv.moveWindow('mask', -1920, 0)

lastListOfPoints = []   # list of points of last frame
k = 0                   # keyboard key
i = 0                   # n° frame

# Couleurs extrêmes
LOWER = np.array([h, s, v])
UPPER = np.array([h + step, s + step, v + step])

# On lit la vidéo
video = cv.VideoCapture(VIDEO_FILE_NAME)

# Première frame
_, frame = video.read()

# Initialisation de la première ligne
lastListOfPoints = [[0, 0, 0]] * len(frame[a:b, c:d])


now = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

# Tant qu'il y a des frame, on lit
while _:
    # On incrémente le n° des frame
    i += 1

    # On ne garde que la partie intéressante
    frame = frame[a:b, c:d]

    # On convertit et on ne garde que les pixels rouge
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, LOWER, UPPER)

    # On vérifie que l'utilisateur ne veuille pas tout stoper
    k = cv.waitKey(FRAME_RATE) & 0xFF
    if(k == key.ESCAPE):
        break

    # Maintenant on fait la moyenne des pixels.
    # S'il n'y a assez de pixels on enregistre les anciens
    if (cv.countNonZero(mask) > 100):
        # On ajoute les points de la ligne laser
        lastListOfPoints = moy(mask, i)
    # On enregistre les points
    saveStream(lastListOfPoints, now)

    # On passe à la suite
    _, frame = video.read()


# On ferme les fenêtre
cv.destroyAllWindows()
video.release()

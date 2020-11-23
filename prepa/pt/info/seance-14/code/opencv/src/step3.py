# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                                 IMPORTS                                   ║
# ╚═══════════════════════════════════════════════════════════════════════════╝
import numpy as np
import cv2.cv2 as cv
import random as rd
from . import helper, constants as cte

# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                                  TRACK                                    ║
# ╚═══════════════════════════════════════════════════════════════════════════╝


def nothing(x):
    pass


def outline(videoPath):

    cv.namedWindow('calibration', cv.WND_PROP_FULLSCREEN)
    # On la déplace pour qu'elle soit dans le second écran
    cv.moveWindow('calibration', -1936, -10)
    # On la met en plein écran
    cv.setWindowProperty(
        'calibration', cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
    # On lui rajoute trois trackBar pour controller la calibration

    # On ajoute les trackBar
    cv.createTrackbar('1', 'calibration', 1, 100, nothing)
    cv.createTrackbar('2', 'calibration', 100, 100, nothing)

    # Tant qu'il y a une image de la vidéo à lire

    # backSub = cv.createBackgroundSubtractorKNN(history, history, detectShadows)
    backSub = cv.createBackgroundSubtractorMOG2(
        history=1, varThreshold=100, detectShadows=True)

    k = 0

    while True:
        video = cv.VideoCapture(videoPath)
        _, frame = video.read()
        while _:
            t1 = cv.getTrackbarPos('1', 'calibration')
            t2 = cv.getTrackbarPos('2', 'calibration')

            backSub.setHistory(t1)
            backSub.setVarThreshold(t2)

            fgMask = backSub.apply(frame)

            # edges = cv.Canny(fgMask, 0, 255)

            # contours, hierarchy = cv.findContours(
            #     edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
            # cv.drawContours(frame, contours, -1, (0, 255, 0), 3)
            frame = cv.bitwise_and(frame, frame, mask=fgMask)
            # On affiche l'image
            cv.imshow('calibration', frame)

            # On attends 10ms avant d'afficher la prochaine image
            k = cv.waitKey(10) & 0xff

            # Si l'utilisateur appuie sur échap, on s'arrête, et on lance la vidéo suivante
            if k == 27:
                break

            # On lit l'image suivante de la vidéo
            _, frame = video.read()
        video.release()
        if (k == 27):
            break

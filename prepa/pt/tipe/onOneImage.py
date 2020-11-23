import cv2.cv2 as cv
import numpy as np
import os
import helpers.keymap as key
from crop import addFrames, crop
import time

PATH = "sources/set-1"
videoFile = "better.mp4"

videoFile = os.path.join(PATH, videoFile)

LOWER_RED = np.array([170, 200, 90])
UPPER_RED = np.array([180, 255, 100])


def first_nonzero(arr, axis, invalid_val=-1):
    mask = arr != 0
    return np.where(mask.any(axis=axis), mask.argmax(axis=axis), invalid_val)


def average(mask):
    maskBis = np.transpose(mask)
    maskTirece = maskBis.copy()
    l = len(maskBis)
    for i in range(l):
        if (cv.countNonZero(maskBis[i])):
            p = int(np.average(np.where(maskBis[i] == 255)[0]))
            maskTirece[i] = [0] * (p) + [255]*4 + [0] * (l-p-4)
    return np.transpose(maskTirece)


# On crée la fenêtre
cv.namedWindow('mask')
cv.moveWindow('mask', -1936, -50)

# Crop
a, b, c, d = crop(videoFile, 'mask')

# On déplace la fenêtre cropée
cv.moveWindow('mask', -1600, 350)


k = 0

# On lit la vidéo
video = cv.VideoCapture(videoFile)

# Première frame
_, frame = video.read()

x = True

# Tant qu'il y a des frame, on lit
while x:
    frame = frame[a:b, c:d]
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, LOWER_RED, UPPER_RED)
    k = cv.waitKey(1) & 0xFF
    if(k == key.ESCAPE):
        break
    if (not cv.countNonZero(mask) < 1000):
        x = False
    cv.imshow('mask', mask)
    _, frame = video.read()

red = np.zeros((b-a, d-c, 3), np.uint8)
red[:] = (0, 0, 255)
blue = np.zeros((b-a, d-c, 3), np.uint8)
blue[:] = (255, 0, 0)
maskBis = average(mask)
first = cv.bitwise_and(blue, blue, mask=mask)
sec = cv.bitwise_and(red, red, mask=maskBis)
dst = cv.add(sec, first)
while True:
    k = cv.waitKey(10) & 0xFF
    if(k == key.ESCAPE):
        break
    cv.imshow('mask', dst)

# On ferme les fenêtre
cv.destroyAllWindows()
video.release()

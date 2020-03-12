import cv2
import numpy as np

import _filter as f

# FILE_NAME = 'test.mp4'
FILE_NAME = 0
MAXI = 256
EPSILON = 20
BIG_EPSILON = 5
TIME_SETTING_LOOP = 30

hsvLow = np.array([0, 0, 0])
hsvHigh = np.array([255, 255, 255])
k = 0

SPACE_KEY = 32
BACKSPACE_KEY = 8
ACCELERATE_KEY = 9
DECELERATE_KEY = 13
ESCAPE_KEY = 27

value = 0


def calibrate():
    global value, k
    video = cv2.cv2.VideoCapture(FILE_NAME)
    for index in range(3):
        k = 0
        value = -1
        while k != SPACE_KEY and k != ESCAPE_KEY:
            if value >= MAXI + 1:
                value = -1
            value += 1
            if type(FILE_NAME) == str:
                video = cv2.cv2.VideoCapture(FILE_NAME)

            hsvLow[index] = value
            hsvHigh[index] = value + EPSILON

            def loopVideo():
                global value, k, hsvHigh, hsvLow
                # on lit la vidéo frame par frame
                _, frame = video.read()
                if not _:
                    return False
                # on filtre

                # res = f.filter_Calibr(frame, (hsvLow, hsvHigh))

                # on affiche frame par frame
                cv2.cv2.imshow('frame', frame)
                # cv2.cv2.imshow('res', res)
                k = cv2.cv2.waitKey(1) & 0xFF
                if k == ACCELERATE_KEY:
                    value += BIG_EPSILON
                    return False
                if k == DECELERATE_KEY:
                    value -= BIG_EPSILON
                    return False
                if k == ESCAPE_KEY:
                    return False
                if k == SPACE_KEY:
                    return False
                if k == BACKSPACE_KEY:
                    value = -1
                    return False
                return True

            if(type(FILE_NAME) == str):
                while True:
                    if(not loopVideo()):
                        break
            else:
                for i in range(TIME_SETTING_LOOP):
                    if(not loopVideo()):
                        break
        if k == ESCAPE_KEY:
            break

    cv2.cv2.destroyAllWindows()
    video.release()

    return (hsvLow, hsvHigh)

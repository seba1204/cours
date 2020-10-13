import numpy as np
import cv2.cv2 as cv
import _filter as f
import _Calibrate as c


# FILE_NAME = 0
FILE_NAME = 'test.mp4'

(LOW_COLOR, HIGH_COLOR) = c.calibrate()

while(True):
    video = cv.VideoCapture(FILE_NAME)
    _, frame = video.read()

    while _:
        cv.imshow('Original', frame)
        cv.imshow('Mask', f.filter_realtime(
            frame, (LOW_COLOR, HIGH_COLOR)))

        k = cv.waitKey(10) & 0xFF
        if(k == 27):
            break
        _, frame = video.read()

cv.destroyAllWindows()
video.release()

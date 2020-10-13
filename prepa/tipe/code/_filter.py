import cv2.cv2 as cv


def filter_Calibr(frame, params):
    hsvLow, hsvHigh = params
    frameHSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(frameHSV, hsvLow, hsvHigh)
    res = cv.bitwise_and(frame, frame, mask=mask)

    return res


def filter_realtime(frame, params):
    hsvLow, hsvHigh = params
    frameHSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(frameHSV, hsvLow, hsvHigh)

    return mask

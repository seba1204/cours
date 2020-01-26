import numpy as np

REGULAR = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])

GAUSSIAN = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
])


def filtre(img, fType='REGULAR'):
    img1 = np.zeros_like(img)
    h, w = np.shape(img)
    f, n = REGULAR, 9
    if fType == 'REGULAR':
        f, n = GAUSSIAN, 16

    for i in range(1, h-1):
        for j in range(1, w-1):
            a = img[i-1: i+2, j-1: j+2]
            img1[i][j] = np.sum((a * f))/n
    return img1

import numpy as np


def decomposeRGB(A):
    h, w, p = A.shape
    R = np.zeros_like(A)
    G = np.zeros_like(A)
    B = np.zeros_like(A)
    for i in range(h):
        for j in range(w):
            R[i][j][0] = A[i][j][0]
            G[i][j][1] = A[i][j][1]
            B[i][j][2] = A[i][j][2]
    return R, G, B


def seuillage(i, r, g, b, p):

    SEUIL_MAX = [r+p, g+p, b+p]
    SEUIL_MIN = [r-p, g-p, b-p]

    plus = np.where(np.any(i > SEUIL_MAX, axis=-1), 255, 0)
    moins = np.where(np.any(i < SEUIL_MIN, axis=-1), 255, 0)

    return np.logical_or(plus, moins)


def position(mask):
    Ymax, Xmax = np.max(np.where(mask == 0), axis=-1)
    Ymin, Xmin = np.min(np.where(mask == 0), axis=-1)

    # Pour tracer le rectangle
    X = [Xmax, Xmax, Xmin, Xmin, Xmax]
    Y = [Ymax, Ymin, Ymin, Ymax, Ymax]

    # Pour placer le point par rapport a l'origni
    x, y = (Xmin + Xmax) / 2, (Ymin + Ymax)/2

    # Point par rapport au centre de l'image
    h, w = mask.shape
    xi, yi = x-w/2, y-h/2
    return X, Y, x, y, xi, yi


def recenter(h, w, x, y, O):
    Lp, Lm, Hp, Hm = False, False, False, False
    if (x > O*w):
        Lp = True
    elif (x < -O*w):
        Lm = True

    if (y > O*h):
        Hp = True
    elif (y < -O*h):
        Hm = True

    return Lp, Lm, Hp, Hm


def crop(i, xi, yi):
    h, w, p = i.shape

    # coordonnees de la nouvelle origine
    x, y = xi, yi

    # si l'excentration est trop grande, il ne faut pas deborder
    if(xi > w/4):
        x = w/4
    if(xi < -w/4):
        x = -w/4
    if(yi > h/4):
        y = h/4
    if(yi > h/4):
        y = h/4

    a = int(w/4 + x)
    b = int(3*w/4 + x)
    c = int(h/4 + y)
    d = int(3*h/4 + y)

    return i[c:d, a:b]

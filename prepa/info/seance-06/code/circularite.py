import matplotlib.pylab as plt
import numpy as np
import os


def openCSV(path):

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, path)

    f = open(filename, 'r')
    X = []
    Y = []
    for line in f.readlines():
        try:
            a, b = line.split(',')
            a = float(a)
            b = float(b)
            X.append(a)
            Y.append(b)
        except:
            pass
    return (X, Y)


def array(doubleTable):
    return (np.array(doubleTable[0]), np.array(doubleTable[1]))


def roger(X, Y):
    Sxi = np.sum(X)
    Syi = np.sum(Y)
    Sxiyi = np.dot(X, Y)
    Sxi2 = np.sum(X**2)
    Syi2 = np.sum(Y**2)
    Sxiyi2 = np.dot(X, Y**2)
    Sxi2yi = np.dot(X**2, Y)
    Sxi3 = np.sum(X**3)
    Syi3 = np.sum(Y**3)
    n = len(X)
    return(Sxi, Syi, Sxiyi, Sxi2, Syi2, Sxiyi2, Sxi2yi, Sxi3, Syi3, n)


def cercle(X, Y):
    Sxi, Syi, Sxiyi, Sxi2, Syi2, Sxiyi2, Sxi2yi, Sxi3, Syi3, n = roger(X, Y)

    a = Sxi2 - ((Sxi)**2) / n
    b = Sxiyi - (Sxi * Syi) / n
    c = Syi2 - (Syi)**2 / n
    d = (1/2)*(Sxi3+Sxiyi2 - (1/n)*(Sxi*(Sxi2 + Syi2)))
    e = (1/2)*(Syi3+Sxi2yi - (1/n)*(Syi*(Sxi2 + Syi2)))

    xc = (c*d-b*e)/(a*c-b**2)
    yc = (a*e-b*d)/(a*c-b**2)

    R = np.sqrt((1/n)*(Sxi2+Syi2-2*(xc*Sxi+yc*Syi))+xc**2+yc**2)

    return (xc, yc, R, n)


def traceCercle(Xc, Yc, R, n):
    X, Y = [], []
    h = (2*np.pi+1)/n
    for i in range(0, n):
        X.append(R * np.cos(i*h) + Xc)
        Y.append(R * np.sin(i*h) + Yc)
    return (X, Y)


def circularite(Xc, Yc, R, X, Y):
    # On calcule la norme de CM_i
    R_mes = np.sqrt((Xc-X)**2 + (Yc-Y)**2)

    E_min = R - np.min(R_mes)
    E_max = np.max(R_mes) - R

    dc = E_max + E_min
    return(E_max, E_min, dc)


X, Y = array(openCSV('ressources/fichier_point.csv'))
Xc, Yc, R, n = cercle(X, Y)
E_max, E_min, dc = circularite(Xc, Yc, R, X, Y)
Xmax, Ymax = traceCercle(Xc, Yc, R + E_max, 1000)
Xmin, Ymin = traceCercle(Xc, Yc, R - E_min, 1000)
plt.plot(X, Y, 'rx')
plt.plot(Xmax, Ymax, 'g')
plt.plot(Xmin, Ymin, 'g')
plt.text(0, 0, f'dc = {dc:.2f}')
plt.show()

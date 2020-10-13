# Imports
import numpy as np
import matplotlib.pylab as plt

# Données
from ressources.Data import *

# Fonctions circulaires


def cos(a):
    return np.cos(a)


def sin(a):
    return np.sin(a)


def temporalData(wm, Tm):
    A = 2 * (a * d - b * c - d * l * cos(Tm) - c * l * sin(Tm))
    B = 2 * ((-1) * a * c - b * d - d * l * sin(Tm) + c * l * cos(Tm))
    C = a**2 + b**2 + c**2 + d**2 + 2 * l * (b * sin(Tm) - a * cos(Tm))

    Ap = 2 * l * wm * (d * sin(Tm) - c * cos(Tm))
    Bp = 2 * l * wm * ((-1) * d * cos(Tm) - c * sin(Tm))
    Cp = 2 * l * wm * (a * sin(Tm) + b * cos(Tm))

    return (A, B, C, Ap, Bp, Cp)


def Tpv(Tm, Tv, wm):
    A, B, C, Ap, Bp, Cp = temporalData(wm, Tm)
    return (Ap * cos(Tv) + Bp * sin(Tv) + Cp) / (A * sin(Tv) - B * cos(Tv))


def angle(wm, Tmmax, N):
    _Tm = np.linspace(0, Tmmax, N)
    h = Tmmax / (wm * N)
    _Tpv = [Tpv(0, 0, wm)]
    _Tv = [0]
    for i in range(1, N):
        _Tv.append(_Tv[i-1] + _Tpv[i-1] * h)
        _Tpv.append(Tpv(_Tm[i-1], _Tv[i-1], wm))
    return (_Tm, _Tpv)


def degTorad(deg):
    return deg * np.pi / 180


def getMaxSpeed(borneMin, borneMax, pas, N):
    Vd, wm = 0, borneMin

    # Pour sauvegarder les anciennes valeurs
    Vd_o, wm_o = 0, borneMin

    while (Vd < Vmax and wm <= borneMax):

        # On sauvegarde les anciennes valeurs
        # Sinon on fait un tour de trop
        Vd_o, wm_o = Vd, wm

        TpvMax = abs(max(angle(wm, Tmmax, N)[1]))
        Vd = L * TpvMax
        wm += pas

    return (Vd_o, wm_o)


print(getMaxSpeed(0.1, 0.3, 0.01, 1000))

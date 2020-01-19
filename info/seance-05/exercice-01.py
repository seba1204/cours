# Imports 
import numpy as np
import matplotlib.pylab as plt

# Données
from Ressources.Data import *

# Fonctions circulaires
def cos(a):
    return np.cos(a)

def sin(a):
    return np.sin(a)


def motorSpeed(wm, Tm):
    A = 2 * (a * d - b * c - d * l * cos(Tm) - c * l * sin(Tm))
    B = 2 * (-a * c - b * d - d * l * sin(Tm) + c * l * cos(Tm))
    C =  a**2 + b**2 + c**2 + d**2 + 2 * l * (b * sin(Tm) - a * cos(Tm))
    
    Ap = 2 * l * wm * (d * sin(Tm) - c * cos(Tm))
    Bp = 2 * l * wm * (- d * cos(Tm) - c * sin(Tm))
    Cp = 2 * l * wm * (a * sin(Tm) + b * cos(Tm))

    return (A, B, C, Ap, Bp, Cp)

def Tpv(Tm, Tv, wm):
    T = motorSpeed(wm, Tm)
    A, B, Ap, Bp, Cp = T[0], T[1], T[3], T[4], T[5]
    return (Ap * cos(Tv) + Bp * sin(Tv) + Cp * sin(Tv)) / (A * sin(Tv) - B * cos(Tv))

def angle(wm, Tmmax, N):
    _Tm = np.linspace(0, Tmmax, N)
    h = Tmmax / N
    _Tpv = [0]
    _Tv = [0]
    for i in range(1, len(_Tm)):
        _Tpv.append(Tpv(_Tm[i], _Tv[i-1], wm))
        _Tv.append(_Tv[i-1] + _Tpv[i-1] * h)
    return (_Tm, _Tpv)

def degTorad(deg):
    return deg * np.pi / 180

G, H = angle(0.1, degTorad(118.2), 1000)

plt.plot(G, H)
plt.show()

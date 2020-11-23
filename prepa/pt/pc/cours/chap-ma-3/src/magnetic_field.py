from src.constants import (a, b, mu_0, N, I)
from numpy import pi


def rInInterval(r): return r > b and r < b+a


def zInInterval(z): return z > 0 and z < a


def magneticField(r): return (mu_0 * N * I) / (2 * pi * r)


def f(r, z):
    if(rInInterval(r) and zInInterval(z)):
        return magneticField(r)
    else:
        return 0.

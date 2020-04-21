import numpy as np


def resoudre(f, pas, x0, borne):
    bp = x0 + borne
    bm = x0 - borne
    m = x0
    fm = f(m)
    print(fm)
    while(abs(fm) > pas):

        if(fm * f(bp) >= 0):
            bp = m
        elif(fm * f(bm) > 0):
            bm = m

        print(m)
        m = (bm + bp) / 2
        fm = f(m)

    return m


print(resoudre(lambda x: x**2-3, 0.00001, 1, 1))

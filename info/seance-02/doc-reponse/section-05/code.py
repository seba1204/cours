def zeroFunction(f, a, b, eps):
    moy = (a + b) / 2
    while abs(f(moy)) > abs(eps):
        moy = (a + b) / 2
        if f(moy) > 0:
            b = moy
        else:
            a = moy
    return (a)

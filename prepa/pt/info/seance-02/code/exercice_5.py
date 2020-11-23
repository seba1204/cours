def zeroFunction(f, a, b, eps):
    moy = (a + b) / 2
    while abs(f(moy)) > abs(eps):
        moy = (a + b) / 2
        if f(moy) > 0:
            b = moy
        else:
            a = moy
    return (a)


if __name__ == '__main__':
    def f(x): return 3*x+2
    a = -1
    b = 5.75
    eps = 0.001
    print('{:+.3f}'.format(zeroFunction(f, a, b, eps)))

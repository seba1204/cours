import numpy as np
import matplotlib.pylab as plt
import time as t

phi = (1 + np.sqrt(5)) / 2


def firec(n):
    if (n == 0 or n == -1):
        return 1
    return firec(n-1) + firec(n-2)


def firecTime(n):
    T = []
    X = []
    for i in range(1, n+1):
        t1 = t.time()
        firec(i)
        T.append(t.time() - t1)
        X.append(i)
    return (X, T)


def traceTimeFirect(n):
    X, T = firecTime(n)
    Xp = [phi ** k for k in X]
    plt.plot(Xp, T)
    plt.show()


def moindreCarre(n):
    X, T = firecTime(n)
    # On utilise numpy pour plus de simplicite
    X = np.array(X)
    T = np.array(T)

    # On linearise
    X = phi ** X

    # On calcule les variables des moindres carres
    n = X.shape[0]

    Sx = np.sum(X)
    St = np.sum(T)
    Sxt = np.sum(X * T)
    Sx2 = np.sum(X**2)

    # Formule des moindres carres
    a = (n*Sxt-Sx*St)/(n * Sx2 - Sx**2)
    b = (St - a * Sx) / n

    return a, b


def mesureAB(n, m):
    a, b = np.zeros(m), np.zeros(m)
    for i in range(m):
        # On calcule les parametres a et b
        a[i], b[i] = moindreCarre(n)

        # On affiche le pourcentage fait
        print(f'{(i+1)/m*100:.2f}%')

    # On calcule la moyenne des parametres
    a = np.average(a)
    b = np.average(b)

    # On les affiche
    print(a, b)

    # On calcule les temps
    X, T = firecTime(n)

    # On linearise
    X = phi ** X

    # On calcule les points de la droite
    Y = a*X + b

    # On affiche tout ca
    plt.plot(X, T, 'rx', label='temps mesures')
    plt.plot(X, Y, label='modele lineaire')
    plt.legend()
    plt.show()


def fibo(n):
    a, b = 1, 1
    for i in range(n):
        c = a + b
        b = a
        a = c
    return c


def firecrapB(n):
    if (n == 1):
        return ([1, 1])
    l = firecrapB(n-1)
    return [l[1], sum(l)]


def firecrap(n):
    A = firecrapB(n)
    return (A[0] + A[1])


print(firecrap(30))

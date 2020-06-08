import numpy as np
import matplotlib.pylab as plt


def dicho(f, a, b, eps):
    if(abs(a-b) < 2*eps):
        return((a+b)/2)
    m = (a+b)/2
    if(f(a)*f(m) < 0):
        return (dicho(f, a, m, eps))
    return (dicho(f, m, b, eps))


def f(x): return x**3 - 3 * x - 1


def Trace(f, borneMin, borneMax):
    X = np.linspace(borneMin, borneMax, 1000)
    Y = f(X)
    plt.plot(X, Y)
    plt.grid(True, which='both')
    plt.show()


def getRooth(intervals, eps):
    racines = []
    for a, b in intervals:
        racines.append(dicho(f, a, b, eps))

    return racines


def getRPowN(racines, n):
    # On definit D grace aux valeurs propres
    D = np.array([
        [racines[0], 0, 0],
        [0, racines[1], 0],
        [0, 0, racines[2]]
    ])

    # On definit la matrice de passage P grace aux racines
    P = np.array([[1, 1, 1],
                  [racines[0]**2, racines[1]**2, racines[2]**2],
                  [racines[0], racines[1], racines[2]]])

    # On cacule l'inverse de P grace a numpy
    P1 = np.linalg.inv(P)

    return np.dot(np.dot(P, D**n), P1)


def puiss(A, n):
    U = np.eye(3)
    for i in range(n):
        U = np.dot(U, A)
    return U


def getError(n):
    # On definit R
    R = np.array([[0, 0, 1], [1, 0, 3], [0, 1, 0]])

    # On cherche les valeurs propres de R
    racines = getRooth(INTERVAL, PRES)

    # On calcule les matrices à la puissance 10
    Mn = getRPowN(racines, n)
    Rn = puiss(R, n)

    # On calcule l'erreur absolue :
    Er_abs = np.abs(Mn - Rn)

    # On calcule l'erreur relative :
    A = np.max(Rn)
    B = np.max(Er_abs)

    # On calcule le pourcentage :
    per = B / A / PRES

    return float(f'{per:.2f}')


def TraceError(N):
    X, Y = [], []

    for n in N:
        er = getError(n)
        X.append(n)
        Y.append(er)
    plt.plot(X, Y, 'rx')
    plt.show()


# Parametres
INTERVAL = [(-2, -1), (-1, 1), (1, 2)]
PRES = 10**(-5)

TraceError([20, 50, 100, 1000])

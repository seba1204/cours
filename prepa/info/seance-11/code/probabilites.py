import numpy as np
import matplotlib.pylab as plt
import random as rd


def espe(X):
    return sum([i*X[i] for i in range(len(X))])


def varia(X):
    E2 = sum([i**2*X[i] for i in range(len(X))])
    E = espe(X) ** 2
    return (E2 - E)


def tcheb(d, p):
    if (d == 1):
        return [[0] + [1/6] * 6 + [0] * (p-7)]
    t = tcheb(d-1, p)
    newline = [0] + [1/6*sum(t[-1][max(0, k-6):k]) for k in range(1, p)]
    t.append(newline)
    return t


def S(d):
    return tcheb(d, 6*d+1)[-1]


def repartition(Z, T):
    A = []
    for t in T:
        q = min(len(Z), int(t*espe(Z)) + 1)
        A.append(sum(Z[:q]))
    return A


def TraceRepartition():
    X = np.linspace(0.4, 1.6, 1000)

    params = [
        (5, 'r'),
        (20, 'g'),
        (100, 'b')
    ]

    for d, color in params:
        Z = S(d)
        Y = repartition(Z, X)
        plt.plot(X, Y, color, label=str(d))
    plt.show()


def Des_3(N):
    X = [0] * (6*3+1)

    for i in range(N):
        # On lance les 3 des
        des = [rd.randint(1, 6) for k in range(3)]

        # Somme des 3 des
        k = sum(des)

        # On enregistre le resultat
        X[k] += 1/N
    return X


def TraceExp(e, l):
    X = [k for k in range(1, e + 1)]
    Y = []

    # Les valeurs theoriques
    Th = np.array(S(3))

    er = []
    # On fait e experiences
    for k in range(1, e+1):

        # Les valeurs experimentales
        Xp = np.array(Des_3(l))

        # Les erreurs
        dif = np.abs(Xp - Th)
        er.append(np.max(dif)/np.max(Th))

        # On rajoute la moyenne des erreurs
        Y.append(sum(er)/len(er))
    plt.plot(X, Y, 'rx')
    plt.show()

    return (max(Y))


print(TraceExp(50, 8000))

import numpy as np
import matplotlib.pylab as plt


def prime(n):
    """Returns the list of the n first n prime numbers,
    and and the number of loop turns"""

    count = 0  # loop counter

    nb = [k for k in range(2, n+1)]
    for i in range(2, n+1):
        for el in nb:
            if el % i == 0 and el != i:
                count += 1  # On compte combien de tours de boucle on fait
                nb.remove(el)
    return (count, nb)


def listeNombresPremiers(n):
    nb = [k for k in range(2, n+1)]
    for i in range(2, n+1):
        for el in nb:
            if el % i == 0 and el != i:
                nb.remove(el)
    return nb


def Euler(n):
    return (n**2)/(n**2-1)


E = listeNombresPremiers(10000)


def picarre(pres):
    k, eps, P, oP, oeps = 0, 1, 1, 1, 1

    while (eps > pres):
        oP = P
        P *= Euler(E[k])
        oeps = eps
        eps = abs(oP - P)
        k += 1

    return (k-1, oeps)


def pres():
    # On definit la liste de precisions
    M = np.linspace(50, 10**5, 13)

    K, Eps = [], []

    # On recupere tous les k et eps pour ces 13 precisions differentes
    for m in M:
        k, eps = picarre(1/m)
        K.append(k)
        Eps.append(eps)

    # On calcule la fonction 1/kln(k)
    kMaxi = max(K)
    kMini = min(K)
    X = np.linspace(kMini, kMaxi, 1000)
    Y = 1/(X * np.log(X))

    # On trace tout ca
    plt.plot(X, Y)
    plt.plot(K, Eps, 'rx')
    plt.show()


pres()

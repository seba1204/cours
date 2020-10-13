import time as t
import random as r
import numpy as np
import matplotlib.pyplot as plt


def echange(A, i, j):
    A[i], A[j] = A[j], A[i]


def partition(A, g, d):
    V, c = A[g], 0
    for i in range(g+1, d):
        if (A[i] < V):
            c += 1
            echange(A, i, g+c)
    echange(A, g, g+c)
    return g+c


def tri_rec(A, n, p):
    if n < p:
        # le pivot V=A[n] devient V=A[m] a la bonne place m dans A
        m = partition(A, n, p)
        tri_rec(A, n, m)  # On trie avant A[m]
        tri_rec(A, m+1, p)  # On trie apres A[m]


def tri_rapide(A):
    tri_rec(A, 0, len(A))


def temps_rapide(n):
    A = [r.randint(0, 50) for k in range(n)]
    t1 = t.time()
    tri_rapide(A)
    return t.time()-t1


def traceTemps(N):
    Y = []
    for n in N:
        Y.append(temps_rapide(n))
    plt.plot(N*np.log(N), Y, 'rx')
    plt.show()


N = [200, 500, 1000, 2000, 5000, 10000]
traceTemps(N)

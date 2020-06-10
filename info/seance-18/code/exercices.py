import matplotlib.pyplot as plt
from time import perf_counter
import random as r
import numpy as np


# -------------------- Tri rapide par r´ecursivit´e et partition de la liste --------------
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
# -------------------- Tri par insertion avec boucle for --------------------------------


def tri_debut(A, i):
    V = A[i]
    j = i-1
    while A[j] > V and j >= 0:
        A[j+1] = A[j]
        j = j-1
    A[j+1] = V


def tri_insertion(A):
    for i in range(1, len(A)):
        tri_debut(A, i)


def temps(n):
    A = [r.randint(0, 50) for k in range(n)]
    B = A[:]
    t1 = perf_counter()
    tri_rapide(A)
    t_rap = perf_counter() - t1

    t1 = perf_counter()
    tri_insertion(B)
    t_ins = perf_counter() - t1

    return (t_ins/t_rap)


def graphe():
    x = np.array([300, 700, 800, 1000, 1500, 2000, 3000])
    y = [temps(n)*np.log(n)/n for n in x]
    plt.plot(x, y, 'x')  # donne la constante C
    plt.show()


def tri_insertion_inv(T):
    tri_insertion(T)
    return T.reverse()


def pascal(n):
    A = np.zeros((n, n), int)
    for k in range(n-1):
        A[k, 0] = 1
        for j in range(1, n):
            A[k+1, j] = A[k, j]+A[k, j-1]
    A[n-1, 0] = 1
    return A


def tri_insertion_tab(A):
    n = np.shape(A)[0]
    T = []
    for k in range(n):
        T.extend(A[k])
    tri_insertion_inv(T)
    B = np.zeros((n, n), int)
    for d in range(2*n-1):
        for j in range(0, n):
            i = d-j
            if i >= 0 and i <= n-1:
                B[i, j] = T[0]
                T.remove(T[0])
    return B


print(tri_insertion_tab(pascal(10)))

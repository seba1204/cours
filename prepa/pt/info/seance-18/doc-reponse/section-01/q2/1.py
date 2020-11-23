def partition(A, g, d):
    V, c = A[g], 0
    for i in range(g+1, d):
        if (A[i] < V):
            c += 1
            echange(A, i, g+c)
    echange(A, g, g+c)
    return c

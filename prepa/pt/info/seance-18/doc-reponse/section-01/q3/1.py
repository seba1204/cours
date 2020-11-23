def partition(A, g, d):
    c = 0
    for i in range(g+1, d):
        if (A[i] < A[g]):
            echange(A, i, g+c)
            c += 1
    echange(A, g+c, d+1)
    return c

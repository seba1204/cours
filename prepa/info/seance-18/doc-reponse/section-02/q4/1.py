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

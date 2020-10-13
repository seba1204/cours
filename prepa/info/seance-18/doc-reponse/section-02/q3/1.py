def pascal(n):
    A = np.zeros((n, n), int)
    for k in range(n-1):
        A[k, 0] = 1
        for j in range(1, n):
            A[k+1, j] = A[k, j]+A[k, j-1]
    A[n-1, 0] = 1
    return A

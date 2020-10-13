def puiss(A, n):
    U = np.eye(3)
    for i in range(n):
        U = np.dot(U, A)
    return U

def points(n, pas, x, y):
    A = [np.array([x, y])]
    k = f(A[0])
    for i in range(n-1):
        Tx, Ty = Vunit(nabla(A[i]))
        T = np.array([-Ty, Tx])
        Bi = A[i] + pas * T
        Vn = nabla(Bi)
        Lambda = (k-f(Bi))/(Vn[0]**2+Vn[1]**2)
        Ai = Bi + Lambda * Vn
        A.append(list(Ai))
    A[0] = list(A[0])
    return A

def moindreCarre(n):
    X, T = firecTime(n)
    # On utilise numpy pour plus de simplicite
    X = np.array(X)
    T = np.array(T)

    # On linearise
    X = phi ** X

    # On calcule les variables des moindres carres
    n = X.shape[0]

    Sx = np.sum(X)
    St = np.sum(T)
    Sxt = np.sum(X * T)
    Sx2 = np.sum(X**2)

    # Formule des moindres carres
    a = (n*Sxt-Sx*St)/(n * Sx2 - Sx**2)
    b = (St - a * Sx) / n

    return a, b

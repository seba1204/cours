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

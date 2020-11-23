def TraceExp(e, l):
    X = [k for k in range(1, e + 1)]
    Y = []

    # Les valeurs theoriques
    Th = np.array(S(3))

    er = []
    # On fait e experiences
    for k in range(1, e+1):

        # Les valeurs experimentales
        Xp = np.array(Des_3(l))

        # Les erreurs
        dif = np.abs(Xp - Th)
        er.append(np.max(dif)/np.max(Th))

        # On rajoute la moyenne des erreurs
        Y.append(sum(er)/len(er))
    plt.plot(X, Y, 'rx')
    plt.show()

    return (max(Y))

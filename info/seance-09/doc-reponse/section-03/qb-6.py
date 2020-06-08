def mesureAB(n, m):
    a, b = np.zeros(m), np.zeros(m)
    for i in range(m):
        # On calcule les parametres a et b
        a[i], b[i] = moindreCarre(n)

        # On affiche le pourcentage fait
        print(f'{(i+1)/m*100:.2f}%')

    # On calcule la moyenne des parametres
    a = np.average(a)
    b = np.average(b)

    # On les affiche
    print(a, b)

    # On calcule les temps
    X, T = firecTime(n)

    # On linearise
    X = phi ** X

    # On calcule les points de la droite
    Y = a*X + b

    # On affiche tout ca
    plt.plot(X, T, 'rx', label='temps mesures')
    plt.plot(X, Y, label='modele lineaire')
    plt.legend()
    plt.show()

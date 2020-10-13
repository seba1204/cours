def getRPowN(racines, n):
    # On definit D grace aux valeurs propres
    Dn = np.array([
        [racines[0]**n, 0, 0],
        [0, racines[1]**n, 0],
        [0, 0, racines[2]**n]
    ])

    # On definit la matrice de passage P grace aux racines
    P = np.array([[1, 1, 1],
                  [racines[0]**2, racines[1]**2, racines[2]**2],
                  [racines[0], racines[1], racines[2]]])

    # On cacule l'inverse de P grace a numpy
    P1 = np.linalg.inv(P)

    # On retourne M puissance n
    return np.dot(np.dot(P, Dn), P1)

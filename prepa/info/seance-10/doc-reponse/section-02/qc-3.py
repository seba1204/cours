def getError(n):
    # On definit R
    R = np.array([[0, 0, 1], [1, 0, 3], [0, 1, 0]])

    # On cherche les valeurs propres de R
    racines = getRooth(INTERVAL, PRES)

    # On calcule les matrices a la puissance 10
    Mn = getRPowN(racines, n)
    Rn = puiss(R, n)

    # On calcule l'erreur absolue :
    Er_abs = np.abs(Mn - Rn)

    # On calcule l'erreur relative :
    A = np.max(Rn)
    B = np.max(Er_abs)

    # On calcule le pourcentage :
    per = B / A / PRES

    return float(f'{per:.2f}')

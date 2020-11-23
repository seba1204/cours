def Des_3(N):
    X = [0] * (6*3+1)

    for i in range(N):
        # On lance les 3 des
        des = [rd.randint(1, 6) for k in range(3)]

        # Somme des 3 des
        k = sum(des)

        # On enregistre le resultat
        X[k] += 1/N
    return X

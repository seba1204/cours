def listeNombresPremiers(n):
    nb = [k for k in range(2, n+1)]
    for i in range(2, n+1):
        for el in nb:
            if el % i == 0 and el != i:
                nb.remove(el)
    return nb

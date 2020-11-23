def picarre(pres):
    k, eps, P, oP, oeps = 0, 1, 1, 1, 1

    while (eps > pres):
        oP = P
        P *= Euler(E[k])
        oeps = eps
        eps = abs(oP - P)
        k += 1

    return (k-1, oeps)

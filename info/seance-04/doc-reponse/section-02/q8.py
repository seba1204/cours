def young(sigma, epsilon):
    sigma, epsilon = select(sigma, epsilon)
    Sxi, Syi, Sxiyi, Sxi2, n = somme(sigma, epsilon)
    E = ((n * Sxiyi) - (Sxi * Syi)) / ((n * Sxi2) - (Sxi ** 2))
    sigm0 = (Syi - E * Sxi) / (n)

    return (E, sigm0)

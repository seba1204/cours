def select(sigma, epsilon):
    # C'est pas optimise... mais c'est pour se servir de la fonction rupture

    # Limite a la rupture
    Rm = rupture(sigma)

    # Index a partir duquel on le depasse
    i = sigma.index(Rm)

    # On coupe les listes
    sigma = sigma[:i]
    epsilon = epsilon[:i]

    # Maintenant on selectionne les bonnes valeurs
    mini = ind(sigma, 0.08 * Rm)
    maxi = ind(sigma, 0.45 * Rm)

    # On coupe les listes
    sigma = sigma[mini:maxi]
    epsilon = epsilon[mini:maxi]

    return (sigma, epsilon)

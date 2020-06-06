def prime(n):
    """Returns the list of the n first n prime numbers,
    and and the number of loop turns"""

    count = 0  # loop counter

    nb = [k for k in range(2, n+1)]
    for i in range(2, n+1):
        for el in nb:
            if el % i == 0 and el != i:
                count += 1  # On compte combien de tours de boucle on fait
                nb.remove(el)
    return (count, nb)

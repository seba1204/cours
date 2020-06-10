def dicho(g, a, b):
    if (g(a)*g(b) <= 0):
        return None

    PRES = 10**(-6)

    # On remet dans l'ordre au cas ou
    if (a > b):
        a, b = b, a

    while(b-a > PRES):
        m = (a+b)/2
        if(g(a)*g(m) <= 0):
            b = m
        else:
            a = m
    return m

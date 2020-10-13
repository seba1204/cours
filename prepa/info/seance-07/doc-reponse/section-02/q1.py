def h(P, x):
    """P : liste des coefficients du polynome"""
    y = P[0]
    for i in P[1:]:
        y = y * x + i
    return y

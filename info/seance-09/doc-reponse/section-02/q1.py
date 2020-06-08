def pgcd(a, b):
    if (a < b):
        return pgcd(a, b)
    r = a % b
    if (r == 0):
        return b
    return pgcd(b, r)

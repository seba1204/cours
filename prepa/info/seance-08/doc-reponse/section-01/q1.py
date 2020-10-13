def tata(n, p):
    while n and n > 0:
        n = n - p
    return not(n)


val = tata(111, 3)
vap = tata(152, 90)

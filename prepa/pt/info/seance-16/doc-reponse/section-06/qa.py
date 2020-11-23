def racine(f, a, b):
    if (a > b):
        a, b = b, a
    r, i = None, 0
    while (r == None):
        c = a + (b-a)*i/100
        d = a + (b-a)*(i+1)/100
        r = dicho(f, c, d)
        i += 1
    if (r != None):
        return r

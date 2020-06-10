def crop(i, xi, yi):
    h, w, p = i.shape

    # coordonnees de la nouvelle origine
    x, y = xi, yi

    # si l'excentration est trop grande, il ne faut pas deborder
    if(xi > w/4):
        x = w/4
    if(xi < -w/4):
        x = -w/4
    if(yi > h/4):
        y = h/4
    if(yi > h/4):
        y = h/4

    a = int(w/4 + x)
    b = int(3*w/4 + x)
    c = int(h/4 + y)
    d = int(3*h/4 + y)

    return i[c:d, a:b]

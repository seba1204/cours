def cercle(X, Y):
    Sxi, Syi, Sxiyi, Sxi2, Syi2, Sxiyi2, Sxi2yi, Sxi3, Syi3, n = S(X, Y)

    a = Sxi2 - ((Sxi)**2) / n
    b = Sxiyi - (Sxi * Syi) / n
    c = Syi2 - (Syi)**2 / n
    d = (1/2)*(Sxi3+Sxiyi2 - (1/n)*(Sxi*(Sxi2 + Syi2)))
    e = (1/2)*(Syi3+Sxi2yi - (1/n)*(Syi*(Sxi2 + Syi2)))

    xc = (c*d-b*e)/(a*c-b**2)
    yc = (a*e-b*d)/(a*c-b**2)

    R = np.sqrt((1/n)*(Sxi2+Syi2-2*(xc*Sxi+yc*Syi))+xc**2+yc**2)

    return (xc, yc, R, n)

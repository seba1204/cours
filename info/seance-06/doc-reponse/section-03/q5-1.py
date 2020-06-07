def traceCercle(Xc, Yc, R, n):
    X, Y = [], []
    h = (2*np.pi+1)/n
    for i in range(0, n):
        X.append(R * np.cos(i*h) + Xc)
        Y.append(R * np.sin(i*h) + Yc)
    return (X, Y)

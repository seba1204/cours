def S(X, Y):
    Sxi = np.sum(X)
    Syi = np.sum(Y)
    Sxiyi = np.dot(X, Y)
    Sxi2 = np.sum(X**2)
    Syi2 = np.sum(Y**2)
    Sxiyi2 = np.dot(X, Y**2)
    Sxi2yi = np.dot(X**2, Y)
    Sxi3 = np.sum(X**3)
    Syi3 = np.sum(Y**3)
    n = len(X)
    return(Sxi, Syi, Sxiyi, Sxi2, Syi2, Sxiyi2, Sxi2yi, Sxi3, Syi3, n)

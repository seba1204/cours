def somme(sigma, epsilon):
    sigma = np.array(sigma)
    epsilon = np.array(epsilon)
    n = sigma.shape[0]
    Sxi = np.sum(epsilon)
    Syi = np.sum(sigma)
    Sxiyi = np.sum(epsilon * sigma)
    Sxi2 = np.sum(epsilon**2)
    return (Sxi, Syi, Sxiyi, Sxi2, n)

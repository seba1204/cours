def outline(img, threshold):
    n, m = np.shape(img)
    Gx = Gy = np.zeros((n-2, m-2))
    for i in range(n-2):
        for j in range(m-2):
            Gx[i][j] = img[i][j+2] - img[i][j-2]
            Gy[i][j] = img[i+2][j] - img[i-2][j]

    N = np.sqrt(Gx ** 2 + Gy ** 2)
    N /= np.amax(N)
    N *= 255
    N = N.astype(int)
    N = seuil(N, threshold)

    return N

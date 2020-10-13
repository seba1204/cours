def position(mask):
    Ymax, Xmax = np.max(np.where(mask == 0), axis=-1)
    Ymin, Xmin = np.min(np.where(mask == 0), axis=-1)

    # Pour tracer le rectangle
    X = [Xmax, Xmax, Xmin, Xmin, Xmax]
    Y = [Ymax, Ymin, Ymin, Ymax, Ymax]

    # Pour placer le point par rapport a l'origni
    x, y = (Xmin + Xmax) / 2, (Ymin + Ymax)/2

    # Point par rapport au centre de l'image
    h, w = mask.shape
    xi, yi = x-w/2, y-h/2
    return X, Y, x, y, xi, yi

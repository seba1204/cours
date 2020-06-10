def seuillage(i, r, g, b, p):

    SEUIL_MAX = [r+p, g+p, b+p]
    SEUIL_MIN = [r-p, g-p, b-p]

    plus = np.where(np.any(i > SEUIL_MAX, axis=-1), 255, 0)
    moins = np.where(np.any(i < SEUIL_MIN, axis=-1), 255, 0)

    return np.logical_or(plus, moins)

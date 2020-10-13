def seuil(greyScaleArray, seuil):
    return np.where(greyScaleArray < seuil, 0, 255)

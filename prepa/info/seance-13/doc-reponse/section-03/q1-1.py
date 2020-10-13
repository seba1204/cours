def seuil(greyScaleArray, threshold):
    return np.where(greyScaleArray < threshold, 0, 255)

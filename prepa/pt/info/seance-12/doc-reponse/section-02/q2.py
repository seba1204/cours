def geryScale(image):
    # On definit les valeurs de luminance
    R, G, B, = 0.299, 0.587, 0.114

    # On recupere les couleurs de l'image separemment
    r, g, b, = image.split()

    # On les ajoute dans la nouvelle image
    return r * np.array(R) + g * np.array(G) + b * np.array(B)

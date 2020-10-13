# Preparatifs --------------------------------------------------------------
# On ouvre l'image
i = np.array(im.open(IMAGE_1_PATH))

# On decompose l'image
R, G, B = decomposeRGB(i)

# On determine sa taille
h, w = R.shape[0], R.shape[1]

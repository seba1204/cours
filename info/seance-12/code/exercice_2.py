import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as im
import os.path

# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                                Exercice 2                                 ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

from ressources.helpers import plotImage, img


# Question 1 ──────────────────────────────────────────────────────────────────

# On crée l'image en noir et blanc
greyImg = img.convert('L')

# On affiche les images
# plotImage(greyImg, (1, 2))
# plotImage(img, show=True)

# Question 2 ──────────────────────────────────────────────────────────────────


def geryScale(image):
    # On définit les valeurs de luminance
    R, G, B, = 0.299, 0.587, 0.114

    # On récupère les couleurs de l'image séparemment
    r, g, b, = image.split()

    # On les ajoute dans la nouvelle image
    return r * np.array(R) + g * np.array(G) + b * np.array(B)


# On affiche le tout
# plotImage(img, (1, 2))
# plotImage(geryScale(img), show=True)


# Question 3 ──────────────────────────────────────────────────────────────────
def arrayToImage(array):
    s = array.shape
    if len(s) == 3:
        mode = 'RGB'
        array = array.reshape(s[0] * s[1], 3)
        array = [(r, g, b) for r, g, b in array]
    else:
        mode = 'L'
        array = array.flat
    newIm = im.new(mode, (s[1], s[0]))
    data = list(array)
    newIm.putdata(data)
    return newIm


# greyScaleImg = arrayToImage(geryScale(img))


# Question 4 ──────────────────────────────────────────────────────────────────
# greyScaleImg.save('Ressources/image_grise.jpg')

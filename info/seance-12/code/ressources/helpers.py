import matplotlib.pyplot as plt
import numpy as np
import os.path
import PIL.Image as im

# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                                 HELPERS                                   ║
# ╚═══════════════════════════════════════════════════════════════════════════╝


# On définit les variables globales permettant de gérer les subplot
numberOfPlots = 1
size = (1, 1)


# On crée une fonction qui affiche l'image dans une figure pyplot
def plotImage(image, s=None, show=False):
    global numberOfPlots
    global size
    if s:
        size = s
    plt.subplot(size[0], size[1], numberOfPlots)
    plt.axis('off')
    mode = 'L'
    if type(image) == np.ndarray:
        if len(image) == 3:
            mode = 'RGB'
    else:
        if image.mode == 'RGB':
            mode = 'RGB'
    if mode == 'L':
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(image)

    numberOfPlots += 1
    if show:
        plt.show()


# Chemin
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "originale.jpg")

# On ouvre l'image
img = im.open(filename)

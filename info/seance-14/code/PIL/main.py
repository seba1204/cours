import PIL.Image as im
import numpy as np
import matplotlib.pyplot as plt

from helpers.plotter import Plotter as pltr

from helpers.path import r
from helpers.image import decomposeRGB, seuillage, position, recenter, crop


IMAGE_1_PATH = r('ressources/im1.png')
IMAGE_2_PATH = r('ressources/im2.png')

# Preparatifs ------------------------------------------------------------------
# On ouvre l'image
i = np.array(im.open(IMAGE_1_PATH))

# On decompose l'image
R, G, B = decomposeRGB(i)

# On determine sa taille
h, w = R.shape[0], R.shape[1]


# Recherche de la couleur ------------------------------------------------------
# On crer le plot
P = pltr()

# On ajoute les images
# P.addSubplot(i)
# P.addSubplot(R)
# P.addSubplot(G)
# P.addSubplot(B)

# On affiche le tout
# P.show()

# On trouve : R = 132, G = 25, B = 47

# Seuillage --------------------------------------------------------------------
r, g, b, p = 132, 25, 47, 20
mask = seuillage(i, r, g, b, p)

# P.addSubplot(mask)
# P.show()

# Position ---------------------------------------------------------------------
X, Y, x, y, xi, yi = position(mask)

# plt.plot(X, Y, 'b')
# plt.plot(x, y, 'bx')
# plt.imshow(i, alpha=0.3)
# plt.show()


# Recentrage -------------------------------------------------------------------
# O = 0.25
# Lp, Lm, Hp, Hm = recenter(h, w, xi, yi, O)
# print(Lp, Lm, Hp, Hm)

# plt.plot([(w/2)*(1-O), (w/2)*(1+O), (w/2)*(1+O), (w/2)*(1-O), (w/2)*(1-O)],
#          [(h/2)*(1+O), (h/2)*(1+O), (h/2)*(1-O), (h/2)*(1-O), (h/2)*(1+O)], 'g')
# plt.show()

# Recadrage --------------------------------------------------------------------
B = crop(i, xi, yi)
plt.imshow(B, alpha=0.6)
plt.show()

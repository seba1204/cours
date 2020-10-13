# Imports ------------------------------------------------------------------
from helpers.image import decomposeRGB

# Recherche de la couleur --------------------------------------------------
# On cree le plot
P = pltr()

# On ajoute les images
P.addSubplot(i)
P.addSubplot(R)
P.addSubplot(G)
P.addSubplot(B)

# On affiche le tout
P.show()

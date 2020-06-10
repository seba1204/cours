# On cree l'image en noir et blanc
greyImg = img.convert('L')

# On affiche les images
plotImage(greyImg, (1, 2))
plotImage(img, show=True)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "ressources/originale.jpg")

img = im.open("ressources/original.jpg")

imSize = img.size
imMode = img.mode
imFormat = img.format

print("size:\t{}\nmode:\t{}\nformat:\t{}".format(imSize, imMode, imFormat))

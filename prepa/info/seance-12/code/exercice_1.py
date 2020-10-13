import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as im
import os.path


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                                Exercice 1                                 ║
# ╚═══════════════════════════════════════════════════════════════════════════╝
# Question 1 ──────────────────────────────────────────────────────────────────
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "ressources/originale.jpg")

img = im.open(filename)

imSize = img.size
imMode = img.mode
imFormat = img.format

# print("size:\t{}\nmode:\t{}\nformat:\t{}".format(imSize, imMode, imFormat))

# Question 2 ──────────────────────────────────────────────────────────────────

# Open with the default image viewer of the PC
img.show()

# Open into a matplotlib graph
plt.imshow(img)
plt.show()

# Question 3 ──────────────────────────────────────────────────────────────────
# pixelArray = np.array(img)

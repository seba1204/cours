import numpy as np
import sys
import traceback
import PIL.Image as im
from colorama import Fore, Style
from helpers.plotter import Plotter as pltr
from exercice_4 import contraste
from exercice_5 import filtre
from exercice_6 import outline


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                                CONSTANTS                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════╝
# Images ──────────────────────────────────────────────────────────────────────
GREY_CAT = 'Ressources/image_grise.jpg'
LENA = 'Ressources/lena.jpg'
PHOTO = 'Ressources/photographer.jpg'

# Exercice 4 ───────────────────────────────────────────────────────────────────
RATE_1 = 2              # contraste rate of the first image
RATE_2 = -2             # contraste rate of the second image

# Exercice 6 ───────────────────────────────────────────────────────────────────
THRESHOLD_1 = 100       # contraste rate of the first image
THRESHOLD_2 = 200       # contraste rate of the second image

# exercice nb to exec ──────────────────────────────────────────────────────────
EXEC_NB = 6


# ╔═════════════════════════════════════════════════════════════════════════════════╗
# ║                                   Exercice 4                                    ║
# ╚═════════════════════════════════════════════════════════════════════════════════╝
def Exercice_4():
    # image import ────────────────────────────────────────────────────────────────
    i = np.array(im.open(GREY_CAT))

    # plot creation ───────────────────────────────────────────────────────────────
    P = pltr('Exercice 4')

    # contrasted images ───────────────────────────────────────────────────────────
    c1 = contraste(i, RATE_1)
    c2 = contraste(i, RATE_2)

    # plot images ─────────────────────────────────────────────────────────────────
    P.addSubplot(i, "contrast=0")
    P.addSubplot(c1, "contrast={}".format(RATE_1))
    P.addSubplot(c2, "contrast={}".format(RATE_2))

    # show plot ───────────────────────────────────────────────────────────────────
    P.show()


# ╔═════════════════════════════════════════════════════════════════════════════════╗
# ║                                   Exercice 5                                    ║
# ╚═════════════════════════════════════════════════════════════════════════════════╝
def Exercice_5():
    # plot creation ───────────────────────────────────────────────────────────────
    P = pltr('Exercice 5')

    # image import ────────────────────────────────────────────────────────────────
    i = np.array(im.open(LENA).convert('L'))

    # filtered images ─────────────────────────────────────────────────────────────
    f1 = filtre(i)
    f1 = filtre(i, 'GAUSSIAN')

    # plot images ─────────────────────────────────────────────────────────────────
    P.addSubplot(i, "without filter")
    P.addSubplot(f1, "regular filter")
    P.addSubplot(f1, "gaussian filter")

    # show plot ───────────────────────────────────────────────────────────────────
    P.show()


# ╔═════════════════════════════════════════════════════════════════════════════════╗
# ║                                   Exercice 6                                    ║
# ╚═════════════════════════════════════════════════════════════════════════════════╝
def Exercice_6():
    # plot creation ───────────────────────────────────────────────────────────────
    P = pltr('Exercice 6')

    # image import ────────────────────────────────────────────────────────────────
    i = np.array(im.open(PHOTO).convert('L'))

    # filtered images ─────────────────────────────────────────────────────────────
    o1 = outline(i, THRESHOLD_1)
    o2 = outline(i, THRESHOLD_2)

    # plot images ─────────────────────────────────────────────────────────────────
    P.addSubplot(i, "original")
    P.addSubplot(o1, f"outlined: {THRESHOLD_1}")
    P.addSubplot(o2, f"outlined: {THRESHOLD_2}")

    # show plot ───────────────────────────────────────────────────────────────────
    P.show()


try:
    locals()[f"Exercice_{EXEC_NB}"]()


# This is just to have some colors on console.
except:
    e = sys.exc_info()
    print(f'{Fore.RED}ERROR{Fore.YELLOW}')

    for trace in traceback.extract_tb(e[2]):
        print(trace)

    print(f'{Fore.RED}{e[1]}{Style.RESET_ALL}')

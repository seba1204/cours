# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                                 IMPORTS                                   ║
# ╚═══════════════════════════════════════════════════════════════════════════╝
import numpy as np
import cv2.cv2 as cv
from . import helper, constants as cte
import time

# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                                  TRACK                                    ║
# ╚═══════════════════════════════════════════════════════════════════════════╝


def track(imagePath, trackColor):
    """
    Parameters
    ----------
    imagePath:  str OR list of str
                path to the image you want to track
    trackColor: tuple of int
                color of the object you want to track
    """

    # On transforme imagePath et trackColor en liste d'un élément si besoin
    data = helper.listify(imagePath, trackColor)

    for image, color in data:
        h, s, v, step = color

        LOWER = np.array([h, s, v])
        UPPER = np.array([h + step, s + step, v + step])

        # On ouvre l'image
        frame = cv.imread(image)

        # On convertit l'image lue en BGR en HSV
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # On crée un masque qui ne garde que les pixels des bonnes couleurs
        mask = cv.inRange(hsv, LOWER, UPPER)

        # On récupère tous la position de tous les pixels restants

        x, y = np.nonzero(mask)
        firstPoint = (np.max(y), np.max(x))
        lastPoint = (np.min(y), np.min(x))

        # On rajoute un rectangle à l'image pour localiser la voiture
        c, t = cte.LINE_COLOR, cte.LINE_THICKNESS
        image = cv.rectangle(frame, firstPoint, lastPoint, c, t)
        font = cv.FONT_HERSHEY_SIMPLEX
        image = cv.putText(image, 'Appuyer sur Echap',
                           (0, 30), font, 0.9, c, 2, cv.LINE_AA)
        while True:
            # On affiche l'image
            cv.imshow('image', image)

            # On attends 10ms avant de rafficher l'image
            k = cv.waitKey(10) & 0xff

            # Si l'utilisateur appuie sur échap, on s'arrête, et on passe à l'image suivante
            if k == 27:
                break

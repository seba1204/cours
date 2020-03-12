# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                                 IMPORTS                                   ║
# ╚═══════════════════════════════════════════════════════════════════════════╝
import numpy as np
import cv2.cv2 as cv
from . import helper, constants as cte

# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                                  TRACK                                    ║
# ╚═══════════════════════════════════════════════════════════════════════════╝


def track(videoPath, trackColor):
    """
    Parameters
    ----------
    videoPath:  str OR list of str
                path to the video you want to track
    trackColor: tuple of int
                color of the object you want to track
    """

    # On transforme videoPath et trackColor en liste d'un élément si besoin
    data = helper.listify(videoPath, trackColor)

    # Pour chaque vidéo à analyser
    for video, color in data:
        # On ouvre la vidéo
        video = cv.VideoCapture(video)

        # La fonction read() retourne un tuple de deux éléments
        # Le premier est un bool : True si la vidéo n'est pas finie
        # Le second est un ndarray : l'image nième de la vidéo
        _, frame = video.read()

        # On définit la plage de couleur que l'on veut garder
        # en spécifiant les couleurs de départ et la largeur de
        # lintervalle (step)
        h, s, v, step = color

        # Les couleurs extrêmes
        LOWER = np.array([h, s, v])
        UPPER = np.array([h + step, s + step, v + step])

        # Tant qu'il y a une image de la vidéo à lire
        while _:

            # On convertit l'image lue en BGR en HSV
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

            # On crée un masque qui ne garde que les pixels des bonnes couleurs
            mask = cv.inRange(hsv, LOWER, UPPER)

            # On récupère la position de tous les pixels restants
            x, y = np.nonzero(mask)

            # Si le mask contient des pixels, on récupère le point en haut à droite et en bas à gauche
            try:
                X = int(np.average(y))
                Y = int(np.average(x))
            except:
                pass
            # On rajoute le rectangle entourant la voiture sur l'image
            l, c, t = cte.CROSS_LENGHT, cte.LINE_COLOR, cte.LINE_THICKNESS
            p1, p2 = (X, Y+l), (X, Y-l)
            image = cv.line(frame, p1, p2, c, t)

            p1, p2 = (X+l, Y), (X-l, Y)
            image = cv.line(image, p1, p2, c, t)

            # On affiche l'image
            cv.imshow('frame', image)

            # On attends 10ms avant d'afficher la prochaine image
            k = cv.waitKey(10) & 0xff

            # Si l'utilisateur appuie sur échap, on s'arrête, et on lance la vidéo suivante
            if k == 27:
                break

            # On lit l'image suivante de la vidéo
            _, frame = video.read()

        video.release()

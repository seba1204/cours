# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                                 IMPORTS                                   ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

from src.step1 import track as trackImage
from src.step2 import track as trackVideo
from src.step3 import outline as trackVideoEdges


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                               PARAMETRES                                  ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

IMAGES_PATH = ['media/im1.png', 'media/im2.png']
VIDEO_PATH = 'media/car_to_track.mp4'
CAR_PARAMS_1 = [(0, 170, 100, 200)]*2
CAR_PARAMS_2 = (45, 16, 84, 23)  # h, s, v, precision


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                                  CODE                                     ║
# ╚═══════════════════════════════════════════════════════════════════════════╝


# 1. On track la voiture sur une image
# trackImage(IMAGES_PATH, CAR_PARAMS_1)

# 2. On track la voiture sur une vidéo
# trackVideo(VIDEO_PATH, CAR_PARAMS_2)

# 3. On track la voiture sur une vidéo grace aux contours
trackVideoEdges(VIDEO_PATH)

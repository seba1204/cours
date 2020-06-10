import numpy as np


def around(A):
    B = np.around(A, 2)
    return [list(a) for a in B]

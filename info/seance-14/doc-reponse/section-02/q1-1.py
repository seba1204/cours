import numpy as np

def decomposeRGB(A):
    h, w, p = A.shape
    R = np.zeros_like(A)
    G = np.zeros_like(A)
    B = np.zeros_like(A)
    for i in range(h):
        for j in range(w):
            R[i][j][0] = A[i][j][0]
            G[i][j][1] = A[i][j][1]
            B[i][j][2] = A[i][j][2]
    return R, G, B

# Imports ------------------------------------------------------------------
import numpy as np
import matplotlib.pylab as plt
import time

# Classe Liste -------------------------------------------------------------
class Liste(list):
    def __init__(self, liste=[]):
        self.A = liste

    def _triDebut(self, i):
        V = self.A[i]
        while _plusPetitQue(V, self.A[i-1]) and i-1 >= 0:
            self.A[i] = self.A[i-1]
            i -= 1
        self.A[i] = V

# Helpers ------------------------------------------------------------------
def _plusPetitQue(a, b):
    if type(a) == list:
        return a[1] < b[1] or (a[1] == b[1] and a[0] < b[0])
    else:
        return a < b

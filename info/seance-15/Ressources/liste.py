import numpy as np
import matplotlib.pylab as plt
import time


class Liste(list):

    def __init__(self, liste=[]):
        self.A = liste

    def generateRadomList(self, n):
        """n: lenght of list to generate"""
        self.A = [np.random.randint(n) for k in range(n)]

    def _triDebut(self, i):
        V = self.A[i]
        while _plusPetitQue(V, self.A[i-1]) and i-1 >= 0:
            self.A[i] = self.A[i-1]
            i -= 1
        self.A[i] = V

    def trier(self):
        for i in range(1, len(self.A)):
            self._triDebut(i)

    def time(self, n, show=False):
        X, T = [], []
        for i in range(1, n):
            self.generateRadomList(i)
            start = time.time()
            self.trier()
            end = time.time()

            X.append(i)
            T.append((end - start) / i ** 2)
        if (show):
            plt.plot(X, T, label='temps / $n^2')
            plt.show()

    def separate(self):
        X, Y = [], []
        for a in self.A:
            X.append(a[0])
            Y.append(a[1])
        return (X, Y)


def _plusPetitQue(a, b):
    if type(a) == list:
        return a[1] < b[1] or (a[1] == b[1] and a[0] < b[0])
    else:
        return a < b

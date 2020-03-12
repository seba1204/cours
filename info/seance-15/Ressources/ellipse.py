import numpy as np
import matplotlib.pylab as plt
from Ressources.liste import Liste


class Ellipse():
    def __init__(self):
        self.X = []
        self.Y = []
        self.Filled = []
        self.conditionInitales = (0, 0)
        self.Eulerized = False

    def Eulerize(self, n):
        h = 2*np.pi/n
        self.X = [self.conditionInitales[0]]
        self.Y = [self.conditionInitales[1]]

        for i in range(n):
            self.X.append(self.X[i] + h * (2*self.X[i]-5*self.Y[i]))
            self.Y.append(self.Y[i] + h * (self.X[i]-2*self.Y[i]))
        self.Eulerized = True

    def Tracer(self):
        if (self.Eulerized):
            l = len(self.Filled)
            if (l > 0):
                colonne = int(np.sqrt(l))
                ligne = l // colonne
                ligne = ligne if l % colonne == 0 else ligne + 1
                for i in range(l):
                    plt.subplot(colonne, ligne, i+1)
                    plt.plot(self.Filled[i][0], self.Filled[i][1])
                    plt.plot(self.X, self.Y)
            plt.show()
        else:
            raise NameError('Veuillez d\'abord lancer la procédeure d\'Euler')

    def GetListOfPoint(self, n, inverted=False, radial=False):
        A = []
        l = len(self.X)
        for i in range(0, l, l//n):
            if inverted:
                A.append([self.Y[i], self.X[i]])
            else:
                A.append([self.X[i], self.Y[i]])
        return A

    def Fill(self, pas, methode):
        if (methode == 1):
            A = Liste(self.GetListOfPoint(pas))
            A.trier()
            X, Y = A.separate()
        elif (methode == 2):
            A = Liste(self.GetListOfPoint(pas, True))
            A.trier()
            Y, X = A.separate()
        self.Filled.append([X, Y])

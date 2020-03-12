# Tri pas insertion

## 1. Présentation

```Python
def tri_debut(A, i):
    V = A[i]
    while V < A[i-1] and i-1 >=0:
        A[i] = A[i-1]
        i-=1
    A[i] = V
```

Pour des raisons de praticité, on décide de créer une classe qui aura comme méthode publique triInsertion et comme méthode privée triDebut.

```Python
import numpy as np
import matplotlib.pylab as plt
import time


class Liste(list):

    def __init__(self):
        self.A = []

    def generateRadomList(self, n):
        """n: lenght of list to generate"""
        self.A = [np.random.randint(n) for k in range(n)]

    def _triDebut(self, i):
        V = self.A[i]
        while V < self.A[i-1] and i-1 >= 0:
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
```

## 2. Tri insertion

```Python
def triInsertion(A, i):
   for i in range(1, len(self.A)):
            self._triDebut(i)
```

## 3. Complexité

La complexité et c = O(n²)

## 4. Complexité

```Python
from Ressources.list import Liste
A = Liste()
A.time(1000, True)
```

## 5. Remplissage d'ellipse

```Python
import numpy as np

class Ellipse():
    def __init__(self):
        self.X = []
        self.Y = []
        self.x0 = 1
        self.y0 = 2

    def conditionInitales(self, x, y):
        self.x0 = x
        self.y0 = y

    def Eulerize(self, n):
        t = np.linspace(0, 2*np.pi, n)
        h = 2*np.pi/n
        self.X = [1]
        self.Y = [2]

        for i in range(n):
            self.X.append(self.X[i] + h * (2*self.X[i]-5*self.Y[i]))
            self.Y.append(self.Y[i] + h * (self.X[i]-2*self.Y[i]))
```

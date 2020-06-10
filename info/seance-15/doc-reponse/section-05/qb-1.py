class Ellipse():
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
        if (methode == 0):
            X, Y = [0], [0]
        elif (methode == 1):
            A = Liste(self.GetListOfPoint(pas))
            A.trier()
            X, Y = A.separate()
        elif (methode == 2):
            A = Liste(self.GetListOfPoint(pas, True))
            A.trier()
            Y, X = A.separate()
        elif (methode == 3):
            A = Liste()
            for i in range(0, len(self.X), pas):
                r, tetha = cmath.polar(complex(self.X[i], self.Y[i]))
                A.append([tetha, r])
            A.trier()
            X, Y = [], []
            for a in A:
                X.append(a[1] * np.cos(a[0]))
                Y.append(a[1] * np.sin(a[0]))
                X.append(0)
                Y.append(0)
        self.Filled.append([X, Y])

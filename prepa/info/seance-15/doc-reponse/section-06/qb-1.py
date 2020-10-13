class Ellipse():
    def Rotate(self, t):
        X, Y = rotate(self.X, self.Y, t)
        self.Filled.append([X, Y])

    def GetPetitRayon(self, t):
        X, Y = rotate(self.X, self.Y, t)
        return(min(np.sqrt(X**2 + Y**2)))

# Helpers ------------------------------------------------------------------


def rotate(Xa, Ya, t):
    R = np.array([
        [np.cos(t), -np.sin(t)],
        [np.sin(t), np.cos(t)]
    ])
    X, Y = [], []
    for i in range(len(Xa)):
        u = np.array([Xa[i], Ya[i]])
        v = np.dot(R, u)
        X.append(v[0])
        Y.append(v[1])
    return np.array(X), np.array(Y)

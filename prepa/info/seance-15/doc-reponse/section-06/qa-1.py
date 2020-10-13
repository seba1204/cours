class Ellipse():
    def GetPolar(self):
        rMax = 0
        phiMax = 0
        for i in range(len(self.X)):
            r, phi = cmath.polar(complex(self.X[i], self.Y[i]))
            if r > rMax:
                rMax = r
                phiMax = phi
        return (rMax, phiMax)

  def GetGrandRayon(self):
        X = np.array(self.X)
        Y = np.array(self.Y)
        return(max(np.sqrt(X**2 + Y**2)))

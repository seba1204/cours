from ressources.ellipse import Ellipse
from ressources.liste import Liste
import numpy as np

# A = Liste([9, 11, 3, 7, 8, 6, 1, 3])
# A.trier()
# print(A.A)

# A.time(500, show=True)

E = Ellipse()
E.conditionInitales = (1, 2)
E.Eulerize(10000)

# E.Fill(30, 3)
# E.Tracer()

a = E.GetGrandRayon()
r, t = E.GetPolar()
b = E.GetPetitRayon(-t)

A1 = E.GetAire(-t)
A2 = np.pi*a*b

print(abs(A2-A1)/A2*100)

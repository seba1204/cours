from Ressources.ellipse import Ellipse
import numpy as np
E = Ellipse()

E.conditionInitales = (1, 2)

E.Eulerize(1000)

a = E.GetGrandRayon()
b = E.GetPetitRayon()

r, t = E.GetPolar()
A1 = E.GetAire(-t)
A2 = np.pi*a*b

print(A1)
print(A2)
print(abs(A2-A1)/A2)

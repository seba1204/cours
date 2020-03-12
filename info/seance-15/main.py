from Ressources.ellipse import Ellipse
import matplotlib.pylab as plt

E = Ellipse()

E.conditionInitales = (1, 2)

E.Eulerize(1000)
E.Fill(25, methode=1)
E.Fill(25, methode=2)
E.Fill(25, methode=3)
E.Tracer()

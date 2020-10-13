# Pour pouvoir faire de la 3D
from mpl_toolkits.mplot3d import Axes3D

# Les indispensables
import matplotlib.pyplot as plt
import numpy as np

# On créer notre canvas où on va plotter la courbe
ax = plt.figure().gca(projection='3d')

# Les paramètres de l'hyperboloïde
a, b, c = 1., 1., 1.

# Les paramètres des équations paramétrées
u = np.linspace(-10, 10, 100)
v = np.linspace(-10, 10, 100)

# Il faut les projeter en 2D pour crée la 3D
u, v = np.meshgrid(u, v)

# On applique les éuqations paramétrées
X = a * np.sqrt(1+u**2) * np.cos(v)
Y = b * np.sqrt(1+u**2) * np.sin(v)
Z = c * u

# On plot
ax.plot_wireframe(Y, Z, X)

# On affiche
plt.show()

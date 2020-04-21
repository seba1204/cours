import numpy as np
import matplotlib.pylab as plt
from test.exceptedOutput import pointsOuput
from helpers.help import extract, resoudre
# ═════════════════════════════════════════════════
#                   Question 1
# ═════════════════════════════════════════════════


def f(u):
    x, y = u[0], u[1]
    return x**2 + 2*y**2 + 2*x*y


def nabla(u):
    x, y = u[0], u[1]
    a = 2*x + 2*y
    b = 4*y + 2*x
    return np.array([a, b])


def Vunit(u):
    x, y = u[0], u[1]
    norme = np.sqrt(x**2+y**2)
    return np.array([x/norme, y/norme])

# ═════════════════════════════════════════════════
#                   Question 2
# ═════════════════════════════════════════════════

# f(OBi + lamb * nabla(Bi)) = k
# Obi = [x, y]
# f([x, y] + lamb * nabla[x, y]) = k
# nabla[x, y] = [2*x + 2*y, 4*y + 2x]
# xp = (2x+2y)*lamb + x
# yp = y + lamb * (4*y + 2*x)
# f(x, y) = x**2 + 2*y**2 + 2*x*y
#   = ((2x+2y)*lamb + x)**2 + 2*(y + lamb * (4*y + 2*x))**2 + 2*(y + lamb * (4*y + 2*x))*((2x+2y)*lamb + x) = k


def points(n, pas, x, y):
    A = [np.array([x, y])]
    k = f(A[0])
    for i in range(n):

        Ty, Tx = Vunit(nabla(A[i]))
        Ty *= -1

        Ax, Ay = A[i]
        Bx = Ax + pas * Tx
        By = Ay + pas * Ty

        f = lambda x:

        Ob = np.array([Bx, By])
        A.append(Ob)
    return A


A = points(3000, 1/100, 1, 0)
X, Y = extract(A)
plt.plot(X, Y)
plt.show()

print(A)

# ═════════════════════════════════════════════════
#                   Question 3
# ═════════════════════════════════════════════════

import numpy as np
import matplotlib.pylab as plt
from test.exceptedOutput import pointsOuput
from helpers.help import around
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


def points(n, pas, x, y):
    A = [np.array([x, y])]
    k = f(A[0])
    for i in range(n-1):
        Tx, Ty = Vunit(nabla(A[i]))
        T = np.array([-Ty, Tx])
        Bi = A[i] + pas * T
        Vn = nabla(Bi)
        Lambda = (k-f(Bi))/(Vn[0]**2+Vn[1]**2)
        Ai = Bi + Lambda * Vn
        A.append(list(Ai))

    A[0] = list(A[0])
    return A


A = points(10, 0.5, 1, 0)
print(around(A) == pointsOuput)

# ═════════════════════════════════════════════════
#                   Question 3
# ═════════════════════════════════════════════════


def traceLigne(A):
    A = np.array(A)
    X, Y = A[:, 0], A[:, 1]
    plt.plot(X, Y)


A = points(3000, 0.1, 1, 0)
# traceLigne(A)


# ═════════════════════════════════════════════════
#                   Question 4
# ═════════════════════════════════════════════════

def dicho(g, a, b):
    if (g(a)*g(b) > 0):
        return None

    PRES = 10**(-6)

    # On remet dans l'ordre au cas ou
    if (a > b):
        a, b = b, a

    while(b-a > PRES):
        m = (a+b)/2
        if(g(a)*g(m) <= 0):
            b = m
        else:
            a = m
    return m


# ═════════════════════════════════════════════════
#                   Question 5
# ═════════════════════════════════════════════════
def TraceFunction(f, borneMax, borneMin, nbPoints):
    X = np.linspace(borneMin, borneMax, nbPoints)
    Y = [f(x) for x in X]
    plt.plot(X, Y)
    plt.grid()
    plt.show()


# def h(x): return np.exp(x)-3*x**2


# TraceFunction(h, -2, 4, 1000)

# def resoudre():
#     a = dicho(h, -1, 0)
#     b = dicho(h, 0, 1)
#     c = dicho(h, 3, 4)
#     return a, b, c


# a, b, c = resoudre()
# A = int(a*b*c*10**6)/10**6
# print(A == -1.559156)

# ═════════════════════════════════════════════════
#                   Question 6
# ═════════════════════════════════════════════════


def racine(f, a, b):
    if (a > b):
        a, b = b, a
    r, i = None, 0
    while (r == None):
        c = a + (b-a)*i/100
        d = a + (b-a)*(i+1)/100
        r = dicho(f, c, d)
        i += 1
    if (r != None):
        return r

# ═════════════════════════════════════════════════
#                   Question 7
# ═════════════════════════════════════════════════


def lignes(n, k0, k1):
    pas = 0.01
    k = k0
    while(k <= k1):
        def g(x):
            return f([x, x]) - k
        c = racine(g, -10, 10)
        if (c != None):
            plt.plot(c, c, 'b.')
            traceLigne(points(n, pas, c, c))
        k += 1


# lignes(3000, 1, 8)
# plt.show()

# ═════════════════════════════════════════════════
#                   Question 8
# ═════════════════════════════════════════════════


def h(u):
    x, y = u[0], u[1]
    return x**4 + y**4 - 4*x*y


def nablah(u):
    x, y = u[0], u[1]
    a = 4*x**3 - 4*y
    b = 4*y**3 - 4*x
    return np.array([a, b])


def pointsh(n, pas, x, y):
    A = [np.array([x, y])]
    k = h(A[0])
    for i in range(n-1):
        Tx, Ty = Vunit(nablah(A[i]))
        T = np.array([-Ty, Tx])
        Bi = A[i] + pas * T
        Vn = nablah(Bi)
        Lambda = (k-h(Bi))/(Vn[0]**2+Vn[1]**2)
        Ai = Bi + Lambda * Vn
        A.append(list(Ai))

    A[0] = list(A[0])
    return A


def lignesh(n, k0, k1):
    pas = 0.01
    k = k0
    while(k <= k1):
        def g(x):
            return h([x, x]) - k
        c = racine(g, -10, 10)
        if (c != None and (c < -0.1 or c > 0.1)):
            plt.plot(c, c, 'b.')
            traceLigne(pointsh(n, pas, c, c))
        k += 0.5


lignesh(3000, -1.5, 2.5)
plt.show()

from numpy import sin, exp, cos
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def deriveekieme(Y, X, k):
    if k == 0:
        return Y
    else:
        Z = [(Y[i+1]-Y[i])/(X[i+1]-X[i]) for i in range(len(Y)-1)]
        return deriveekieme(Z, X, k-1)


def f(x):
    return np.sin(x)


def TraceDerivk(f, a, b, n, k):
    X = np.linspace(a, b, n+1)
    yk = deriveekieme(f(X), X, k)
    c = 'g' if k % 2 == 0 else 'r'
    plt.plot(X[:-k], np.abs(yk), color=c, label=f'k={k}')


def TraceDeriv(f, a, b, n):
    for k in range(1, 7):
        TraceDerivk(f, a, b, n, k)
    plt.legend()
    plt.show()


# TraceDeriv(f, 0, 6, 1000)


def g(x):
    return np.exp(-x**2)*np.sin(x**3)


TraceDerivk(g, 0, 6, 1000, 4)
# plt.show()
X = np.linspace(0, 6, 1001)
M = max(deriveekieme(g(X), X, 4))


def simpson(f, n, a, b, M):
    """ Méthode de simpson en divisant [a,b] en n pas  """
    pas = (b-a)/n
    S = 0
    for k in range(n):
        S += pas*(f(a+k*pas)+4*f(a+(k+1/2)*pas)+f(a+(k+1)*pas))/6
    return int(S*10**16)/10**16, (b-a)*pas**4*M/2880


# print(simpson(g, 5726, 0, 6, M))


def optim(M, p):
    """ valeur optimale de n pour erreur inférieur à 10**(-p)"""
    x = 6*(6*M/2880)**(1/4)*10**(p/4)
    return int(x)+1


# print(optim(M, 12))


res, err = quad(g, 0, 6)
print(res, err)

import numpy as np
import PIL.Image as im
import matplotlib.pylab as plt


def f(x): return 0.5 + 0.5 * np.sin(np.pi * (x - 0.5))


def f_reciproque(x): return np.arcsin(2 * x - 1) / np.pi + 0.5


def f_compose(n, x):
    if (n <= 1):
        return f(x)
    return f(f_compose(n-1, x))


def traceF():
    X = np.linspace(0, 1, 100)
    Y1 = [f(x) for x in X]
    Y2 = [f_compose(3, x) for x in X]

    plt.plot(X, Y1, label='$f(x)$')
    plt.plot(X, Y2, label='$f(f(f(x)))$')
    plt.legend()
    plt.show()


def _g(f, x, n):
    if (n == 1):
        return f(x/256)
    return f(_g(f, x, n-1))


def g(x, n):
    return _g(f, x, n) * 256 if n > 0 else _g(f_reciproque, x, abs(n))


def contraste(img, rate):
    return g(img, rate)

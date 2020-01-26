import numpy as np
import PIL.Image as im


def f(x): return 0.5 + 0.5 * np.sin(np.pi * (x - 0.5))


def f_reciproque(x): return np.arcsin(2 * x - 1) / np.pi + 0.5


def _g(f, x, n):
    if (n == 1):
        return f(x/256)
    return f(_g(f, x, n-1))


def g(x, n):
    return _g(f, x, n) * 256 if n > 0 else _g(f_reciproque, x, abs(n))


def contraste(img, rate):
    return g(img, rate)

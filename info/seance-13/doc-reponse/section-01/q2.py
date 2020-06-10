def _g(f, x, n):
    if (n == 1):
        return f(x/256)
    return f(_g(f, x, n-1))


def g(x, n):
    return _g(f, x, n) * 256 if n > 0 else _g(f_reciproque, x, abs(n))

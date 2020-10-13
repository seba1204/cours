p = [1, 2, 3, 4]


def f(p):
    p[0] = 5
    return p


s = f(p)
q = p
p = [1, 2, 3, 4]


def g(p):
    p = p[::-1]
    p[0] = 5
    return p


r = g(p)
u = p

def f_compose(n, x):
    if (n <= 1):
        return f(x)
    return f(f_compose(n-1, x))

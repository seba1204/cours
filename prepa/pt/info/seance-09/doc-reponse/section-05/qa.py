def pascal(n, p):
    if (n == 0):
        return [[1] + [0]*p]
    t = pascal(n-1, p)
    newline = [[1] + [t[-1][k] + t[-1][k-1] for k in range(1, p+1)]]
    t.extend(newline)
    return t

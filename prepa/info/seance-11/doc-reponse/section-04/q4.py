def tcheb(d, p):
    if (d == 1):
        return [[0] + [1/6] * 6 + [0] * (p-7)]
    t = tcheb(d-1, p)
    newline = [0] + [1/6*sum(t[-1][max(0, k-6):k]) for k in range(1, p)]
    t.append(newline)
    return t

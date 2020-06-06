def qb(x):
    up = x
    results = [up]
    while up > 1:
        up = S(up)
        results.append(up)
    return results


def qd():
    X = [k for k in range(3, 301)]
    volMax = 0
    result = []
    for x in X:
        a = qb(x)
        vol = len(a)
        if vol > volMax:
            result = []
            volMax = vol
            result.append(x)
        elif vol == volMax:
            result.append(x)
    return result, volMax

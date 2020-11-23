def S(n):
    if n % 2 == 0:
        return int(n/2)
    elif n != 1:
        return int(3*n+1)
    else:
        return 1


def qb(x):
    up = x
    results = [up]
    while up > 1:
        up = S(up)
        results.append(up)
    return results


def qc():
    X = [2, 7, 19, 23, 29]
    for x in X:
        qb(x)


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


def contains(small, big):
    for i in range(len(big)-len(small)+1):
        for j in range(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return i, i+len(small)
    return False


def interSyracuse(i1, i2):
    i1, i2 = qb(i1), qb(i2)
    grande, petite = [], []
    # On sélectionne la plus petite liste
    if max(len(i1), len(i2)) == len(i1):
        grande, petite = i1, i2
    else:
        grande, petite = i2, i1
    for k in range(len(petite), 1, -1):
        subPetite = petite[-k:]
        if contains(subPetite, grande):
            if subPetite == petite:
                return (1j)
            else:
                maxi = subPetite[0]
                o = petite.index(maxi)
                p = grande.index(maxi)
                return(len(subPetite), petite[:o][-1], grande[:p][-1])


if __name__ == '__main__':
    qc()
    a = qd()
    print(
        'Liste des x pour lesquels le vol est le plus long ({}) :\n{}'
        .format(a[1], a[0])
    )
    print(interSyracuse(7, 320))

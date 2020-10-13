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
    # On selectionne la plus petite liste
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

def nummerHorner(chaine):
    p = [alphabet.index(k) for k in chaine]
    return horner(p, 26)


def numer(s):
    n = 0
    for a in s[:-1:]:
        n = (n + alphabet.index(a)) * 26
    return n + alphabet.index(s[-1])

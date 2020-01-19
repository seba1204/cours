alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphab(n):
    word = ''
    while n !=  0:
        word += alphabet[n % 26]
        n = n // 26
    return word[::-1]

def horner(P, x):
    """P : liste des coefficients du polynome"""
    y = P[0]
    for i in P[1:]:
        y = y * x + i
    return y

def nummerHorner(chaine):
    p = [alphabet.index(k) for k in chaine]
    return horner(p, 26)

def numer(s):
    n=0
    for a in s[:-1:]:
        n = (n + alphabet.index(a)) * 26
    return n+ alphabet.index(s[-1])

print(nummerHorner('math'))

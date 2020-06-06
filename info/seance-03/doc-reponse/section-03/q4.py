def displayIt(pile):
    a, i = '', 0
    iMax = pile.lenght() % 4
    while not pile.isEmpty():
        if (i == iMax):
            a += ' '
            iMax, i = 4, 0
        a += str(pile.unstack())
        i += 1
    return a

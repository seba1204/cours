from exercice_1 import Pile


def div2(x):
    return (x//2, x % 2)


def stackBinary(decimalNumber):
    pile = Pile()
    while decimalNumber >= 1:
        a = div2(decimalNumber)
        decimalNumber = a[0]
        pile.stack(a[1])
    return pile


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


if __name__ == '__main__':
    print(displayIt(stackBinary(525)))

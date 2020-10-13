def stackBinary(decimalNumber):
    pile = Pile()
    while decimalNumber >= 1:
        a = div2(decimalNumber)
        decimalNumber = a[0]
        pile.stack(a[1])
    return pile

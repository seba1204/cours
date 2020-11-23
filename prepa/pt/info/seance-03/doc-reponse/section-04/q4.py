def polonaise(chaine):
    pile = Pile()
    for char in listWords(chaine):
        if isOperator(char):
            if pile.lenght() >= 2:
                a = pile.unstack()
                b = pile.unstack()
                pile.stack(calculOp(a, b, char))
            else:
                raise 'Error ! (oups)'
        elif char.isnumeric():
            pile.stack(float(char))
        else:
            raise 'A non numeric character has been found ({})'.format(char)
    if pile.lenght() == 1:
        return pile.unstack()
    else:
        raise 'Error (oups) !'

def parenthesisTest(chaine):
    pile = Pile()
    for char in chaine:
        if char == '(':
            pile.stack(1)
        elif char == ')':
            if not pile.isEmpty():
                pile.unstack()
            else:
                return False
    if pile.isEmpty():
        return True
    else:
        return False

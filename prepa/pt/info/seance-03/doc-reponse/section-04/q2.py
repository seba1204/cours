def calculOp(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '/':
        return a / b
    elif op == '*':
        return a * b
    else:
        raise '{} ne fait pas partie de la liste des operateurs'.format(op)

from exercice_1 import Pile


def isOperator(char):
    op = [
        '+',
        '-'
        '/',
        '*'
    ]
    return char in op


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
        raise '{} ne fait pas partie de la liste des opérateurs'.format(op)


def listWords(chaine):
    return [a for a in chaine.replace(' ', '')]


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
            raise 'Error, a non numeric character has been found ({})'.format(
                char)
    if pile.lenght() == 1:
        return pile.unstack()
    else:
        raise 'Error (oups) !'


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def test(chaine, exceptedResult):
    try:
        a = polonaise(chaine)
        if a == exceptedResult:
            color = bcolors.OKGREEN
        else:
            color = bcolors.FAIL
        print(color + str(int(a)) + bcolors.ENDC)
    except:
        print(bcolors.FAIL + 'Error' + bcolors.ENDC)


if __name__ == '__main__':
    test('34+', 7)
    test('723+*', 35)
    test('23+7*', 35)

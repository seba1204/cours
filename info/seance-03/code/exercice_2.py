from exercice_1 import Pile


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


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__ == '__main__':
    c = [
        '((3*5-7)+1',
        '((3*5)-7)+1',
        '(3*5)-(7)+1)',
        '(3*(5-7)+(1'
    ]
    color = ''
    for ci in c:
        if parenthesisTest(ci):
            color = bcolors.OKGREEN
        else:
            color = bcolors.FAIL
        print(color + ci + bcolors.ENDC)

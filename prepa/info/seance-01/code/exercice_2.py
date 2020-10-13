import time


def prime(n):
    """Returns the list of the n first n prime numbers,
    and and the number of loop turns"""

    count = 0  # loop counter

    nb = [k for k in range(2, n+1)]
    for i in range(2, n+1):
        for el in nb:
            if el % i == 0 and el != i:
                count += 1  # On compte combien de tours de boucle on fait
                nb.remove(el)
    return (count, nb)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def printResult(n, toursMax):
    t1 = time.time()
    i, result = prime(n)
    t = time.time() - t1
    color = ''
    if i > toursMax:
        color = bcolors.FAIL
    else:
        color = bcolors.OKGREEN
    print(
        bcolors.HEADER +
        '========= Test pour n = {}========='.format(n) +
        '\n' +
        color +
        'Le programme fait {} tours (max : {} tours).'.format(i, toursMax) +
        '\n' +
        bcolors.OKBLUE +
        'Temps d\'execution : {}{:.3f}s{}\n'.format(bcolors.ENDC, t, bcolors.OKBLUE) +
        'Nombre de resultats : {}{}\n{}'.format(bcolors.ENDC, len(result), bcolors.OKBLUE) +
        'Resultats :' + bcolors.ENDC + str(result[:4] + ['...'] + result[-2:])
    )


if __name__ == '__main__':
    n, t = 1000, 1500
    printResult(n, t)

    n, t = 10000, 20000
    printResult(n, t)

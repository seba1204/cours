alphabet = 'abcdefghijklmnopqrstuvwxyz'


def alphab(n):
    word = ''
    while n != 0:
        word += alphabet[n % 26]
        n = n // 26
    return word[::-1]

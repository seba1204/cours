def toto(L):
    while L:
        L.remove(L[-1])
        print(L)


L = [8, 3, 5, 3, 9]
toto(L)

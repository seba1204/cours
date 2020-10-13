
def pascal(n, p):
    if (n == 0):
        return [[1] + [0]*p]
    t = pascal(n-1, p)
    newline = [[1] + [t[-1][k] + t[-1][k-1] for k in range(1, p+1)]]
    t.extend(newline)
    return t


def Triangle(n):
    # On recupere les lignes du triangle de Pascal
    P = pascal(n, n)
    LignesTemp = []
    # Mettre en forme 1 par 1
    for ligne in P:
        # On commence par suppimer tous les zéros
        while (0 in ligne):
            ligne.remove(0)

        # On transforme les listes en chaîne de caracteres
        a = ''
        for num in ligne:
            a += f'{num} '
        LignesTemp.append(a)

    # On recupere la longueur de la derniere ligne (la plus longue)
    h = len(LignesTemp[n]) + 1

    # Maintenant on va rajouter les espaces en debut de lignes pour centrer
    for ligne in LignesTemp:
        L = len(ligne) + 1

        # Si la ligne est paire, on rajoute d'abord un underscore au milieu
        if (L % 2 == 0):
            ligne = ligne[:L//2-1] + '_' + ligne[L//2-1:]

        # Nombre d'espace a rajouter
        nbSpaces = (h - L) // 2

        # On rajoute les espaces
        ligne = ' ' * nbSpaces + ligne

        # On affiche la ligne
        print(ligne)


Triangle(12)

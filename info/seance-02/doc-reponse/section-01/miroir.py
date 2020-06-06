def miroir(chaine):
    result = ''
    for i in range(len(chaine)-1, -1, -1):
        result += chaine[i]
    return result

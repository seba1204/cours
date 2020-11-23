def listSentence(sentence):
    result, a = [], ''
    for char in sentence:
        if char == ' ':
            result.append(a)
            a = ''
        else:
            a += char
    return result


def motMaj(text):
    result = []
    for word in listSentence(text):
        if word[0].isupper():
            result.append(word)
    return (result)


if __name__ == '__main__':
    print(listSentence('Bonjour Sébastien kdfh qsdkfjh, q:qfg !q'))
    print(motMaj('Une Phrase avec des Majusculej sdHkjhd sJKhbKJJHKKHJ .'))

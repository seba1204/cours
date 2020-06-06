def listSentence(sentence):
    result, a = [], ''
    for char in sentence:
        if char == ' ':
            result.append(a)
            a = ''
        else:
            a += char
    return result

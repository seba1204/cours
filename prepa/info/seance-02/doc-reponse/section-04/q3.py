def motMaj(text):
    result = []
    for word in listSentence(text):
        if word[0].isupper():
            result.append(word)
    return (result)

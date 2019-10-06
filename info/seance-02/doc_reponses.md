# TD - Révisions

## I - Fonction miroir

```Python
def miroir(chaine):
    result = ''
    for i in range(len(chaine)-1, -1, -1):
        result += chaine[i]
    return result
```

## II - Définition par compréhension

* Les entiers de 10 à 20 inclus :

```Python
A = [i for i in range(10, 21)]
```

* Les entiers pairs de 10 à 40 inclus :

```Python
B = [i*2 for i in range(10, 21)]
```

* Les 20 premiers carrés :

```Python
C = [i**2 for i in range(20)]
```

## III - Mise au carré

```Python
def listeAuCarre(L):
    return ([a**2 for a in L])
```

## IV - Liste de mots

### Question 1

```Python
isupper()
```

### Question 2

```Python
def listSentence(sentence):
    result, a = [], ''
    for char in sentence:
        if char == ' ':
            result.append(a)
            a = ''
        else:
            a += char
    return result
```

### Question 3

```Python
def motMaj(text):
    result = []
    for word in listSentence(text):
        if word[0].isupper():
            result.append(word)
    return (result)
```

## V - Zéro d'une fonction

```Python
def zeroFunction(f, a, b, eps):
    moy = (a + b) / 2
    while abs(f(moy)) > abs(eps):
        moy = (a + b) / 2
        if f(moy) > 0:
            b = moy
        else:
            a = moy
    return (a)
```

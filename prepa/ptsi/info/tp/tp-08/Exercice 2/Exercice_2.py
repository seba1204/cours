from Exercice_2_Q0 import randomPhrase
f=open("MonFichier.txt","w")
f.write(randomPhrase(2) + ". " + randomPhrase(5) + ". " + randomPhrase(4))
f.close()


def phrasePlusLongue(chaine:str):
    L=chaine.split(". ")
    phraselongue=""
    for phrase in L:
        if (len(phrase) > len(phraselongue)):
            phraselongue = phrase
    return phraselongue
    
def transformFichier(nomFichier:str):
    fi=open(nomFichier,"r")
    phraseRetour = ""
    for ligne in fi:
        phraseRetour+=ligne
    fi.close()
    return phraseRetour

print(phrasePlusLongue(transformFichier("MonFichier.txt")))
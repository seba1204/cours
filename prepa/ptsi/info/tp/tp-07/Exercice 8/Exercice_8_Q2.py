from Exercice_8_Q0 import randomPhrase

text = str(open("../../Utiles/LADISPARITION.txt", "r").read())


def Vinegre(chaine:str,clef:str):
    Cle=[ord(k)-96 for k in clef] #Liste des positions des lettres de la clé
    charReturned="" #Chaine codée retournée qu'on implémente
    n=Cle[0] #clé qui change à chaque tour
    p=0 #savoir où on en est (par rapport à la taille de la clé)
    for char in chaine:
        n=Cle[p%len(Cle)]
        charReturned+=chr((((ord(char)-97)+n)%26)+97)
        p+=1
    return charReturned

textACoder = "oralensam"
def Afficher(texteACoder:str, clef:str):
    print ("Texte en clair : " + texteACoder)
    print ("Clé : " + clef)
    print ("============================")
    print ("Texte codé : " + Vinegre(texteACoder, clef))
    
    
Afficher("oralensam", "pyhton")
print ("\n\n----------------------\nClé et mot au hasard :\n----------------------")

Afficher(randomPhrase(1), randomPhrase(1))
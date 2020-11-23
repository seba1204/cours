from Exercice_6_Q0 import randomPhrase

'''renvoi un tableau contenant le nombre
 d'occurence de chaque lettres de l'alphabet'''
def compteCaraDansChaine(chaine:str):
    Min="abcdefghijklmnopqrstuvwxyz"
    chaine = chaine.lower()
    Compte=[]
    C=0
    for a in Min:        
        for i in chaine:
            if (i==a):
                C+=1
        Compte.append(C)
        C=0
    return Compte

'''renvoie une chaine de charactère contenant le nombre
 d'occurence de chaque lettres de l'alphabet par lignes '''
def nbLettresDansChaine(chaine:str):
    Min="abcdefghijklmnopqrstuvwxyz"
    tableauRetour = ""
    tableauNombre = []
    tableauNombre = compteCaraDansChaine(chaine)
    i=0
    for char in Min:
        tableauRetour+= char + "  :  " + str(tableauNombre[i]) + "\n"
        i+=1
    return tableauRetour

print ("Occurences de chaque lettre de l'alphabet dans La Disparition : ")
text = str(open("../../Utiles/LADISPARITION.txt", "r").read())
print (nbLettresDansChaine(text))

text = randomPhrase(5)
print ("Occurences de chaque lettre de l'alphabet dans la phrase : \n" + chr(34) + text + chr(34) +"\n" + nbLettresDansChaine(text))

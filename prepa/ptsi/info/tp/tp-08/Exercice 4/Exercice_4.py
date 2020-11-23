f=open("../Exercice 2/Monfichier.txt", "r")
NouveauTexte=""
for ligne in f:
    NouveauTexte=ligne.upper() + "\n"
f.close()
f=open("MonfichierExo2Copie.txt", "w")
f.write(NouveauTexte)
f.close()
#Importation des modules externes

import os.path
# Données
from Ressources.donnees import *

# Question 1



def openCSV(path):
  if (os.path.exists(path)):
    try:
      file = open(path, 'r')
      for row in file.readlines():
        try:
          print(row.split(';'))
        except:
            pass
    finally:
      file.close()

  else:
    raise ('Le fichier {} n\'existe pas'.format(path))

openCSV('Ressources/essai_1.csv')
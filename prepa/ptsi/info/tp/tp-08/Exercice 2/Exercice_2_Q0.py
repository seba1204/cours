import random as rnd
import linecache


dicoPath = "../../Utiles/dico.txt"


def readLine(index:int, filePath:str):
	lign = linecache.getline(dicoPath, index).strip()
	return lign

def randomPhrase(nbMots:int, case:str = "lower"):
    text = ""
    for i in range(nbMots):
        text+= readLine(rnd.randint(0, 323576), dicoPath) + " "
    if (case.lower() == "lower"):
        text = text.lower()
    elif (case.lower() == "upper"):
        text = text.upper()    
    return text
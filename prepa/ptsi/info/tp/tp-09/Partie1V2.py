import matplotlib.pyplot as plt  
import numpy as np

#Liste des coordonnées que l'on va traiter tout au long du TP
_pointList=[[],[]] 


#==============================================Cahier des charges à respecter==============================================
#--------------------------------Temps en minutes--------------------------------
maxDelay=range(19,21)
#--------------------------------Distance maximale en m--------------------------------
maxDistance=335

def DisplayPointInFile(pathFile:str, colorLine="blue"):   
    f=open(pathFile,"r")
    DonneeTemp=[]
    LX,LY=[],[]
    for ligne in f:                 
        DonneeTemp=ligne.split(";")
        LX.append(float(DonneeTemp[0]))
        LY.append(float(DonneeTemp[1]))
    f.close()
    L2X=[0, 17.71, 35.42]            
    L2Y=[0, 30.67, 0]
    plt.plot(LX,LY,colorLine)      
    plt.plot(L2X,L2Y, "red")       
    plt.axis('equal')
    plt.show()

def FillList(pathFile:str):
    f=open(pathFile,"r")
    DonneeTemp=[]
    for ligne in f:                 
        DonneeTemp=ligne.split(";")
        _pointList[0].append(float(DonneeTemp[0]))
        _pointList[1].append(float(DonneeTemp[1]))
    f.close()

#==============================================Q1==============================================
#--------------------------------Affichage du parcours du robot--------------------------------
DisplayPointInFile("../Utiles/PL.txt")
#--------------------------------Remplissage des liste à étudier--------------------------------
FillList("../Utiles/PL.txt")

#==============================================Q2==============================================
def TimeCalcul():
    temps=(len(_pointList[0])-1)*7.4 #Temps en secondes /!\ on ne compte pas le 1er point
    return float(temps)
    
    
def ConvertTime(MyTime:float):
    minutes=int(MyTime//60)
    secondes=MyTime%minutes
    return [minutes, secondes]

#--------------------------------Affichage du temps de parcours--------------------------------
_time= ConvertTime(TimeCalcul())
print("Temps mis au robot pour nettoyer : ",_time[0], "min et ",  _time[1], "sec")


#--------------------------------Respect du cahier des charges--------------------------------


if (_time[0] in maxDelay):
    print("Le temps est bon !\nCahier des charges respécté")
else:
    print("Le temps n'est pas bon !\nCahier des charges non respécté")
    

#==============================================Q3==============================================

#--------------------------------Calcul de la distance--------------------------------
#Distance parcourue : Somme de la distance entre chaque points : racin ((Xa-Xb²)+(Ya-Yb)²)
def RunDistance(liste:list):
    _distance=0
    for i in range(0,(len(liste[0])-1)):
        _distance += np.sqrt((liste[0][i]-liste[0][i+1])**2 + (liste[1][i]-liste[1][i+1])**2)
    return _distance

#--------------------------------Affichage de la distance parcourue--------------------------------
_distance =  RunDistance(_pointList)
print("La distance parcourue est : ",_distance, "m")


#--------------------------------Respect du cahier des charges--------------------------------
if (_distance > maxDistance ):
    print("La distance parcourue est trop grande !\nCahier des charges non respécté")
else:
    print("La distance parcourue est bonne !\nCahier des charges respécté")


#==============================================Q4==============================================
#---------------------------Modification du parcours---------------------------
newFile=open("../Utiles/PL_V2.txt","w")
_coordonnées=""
for i in range(0,len(_pointList[1])):
    if (_pointList[1][i] <= 27.3):
        _coordonnées+=str(_pointList[0][i]) + ";" + str(_pointList[1][i]) + "\n"
    else:
        _coordonnées+=str(_pointList[0][i]) + ";" + "27.3" + "\n"
newFile.write(_coordonnées)
newFile.close()

#---------------------------Affichage du nouveau parcours---------------------------
DisplayPointInFile("../Utiles/PL_V2.txt", "green")

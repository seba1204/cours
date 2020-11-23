import matplotlib.pyplot as plt
f=open("../../Utiles/FichierNumerique.txt","r")
LX,LY=[],[]
DonneeTemp=[]
for ligne in f:
    DonneeTemp=ligne.split(";")
    LX.append(float(DonneeTemp[0]))
    LY.append(float(DonneeTemp[1]))

plt.plot(LX,LY)
plt.axis('equal')
plt.show()
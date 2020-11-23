def Compter(L:list):
    p=0
    for element in L:
        if element != 0:
            p+=1
    return p
    

print ("creation de la liste des 7 premiers nombres entiers " )
L=[0,1,2,3,4,5,6]
print ("appel de la fonction Compter" )
print ("Retour de la fonction : ", Compter(L))
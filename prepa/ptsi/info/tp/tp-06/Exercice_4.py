def maxi(Liste:list):
    p=0
    for element in Liste:
        if int(element) > p:
            p=int(element)
    return p
    
L1=(input("rentrer une liste : ")).split(",")
print ("Le max est : ", maxi(L1))
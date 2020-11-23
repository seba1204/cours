def maxi(Liste:list):
    p=0
    for element in Liste:
        if (element) > p:
            p=(element)
    return p
def moyenne(Liste:list):
    s=0
    for element in Liste:
        s+=element
    return s/len(Liste)
    
def variance(Liste:list):
    s=0
    m=moyenne(Liste)
    for element in Liste:
        s+=(element-m)**2
    return ((1/len(Liste))*s)

def separation(Liste:list):
    Lpaire=[]
    Limpaire=[]
    for element in Liste:
        if element%2 == 0:
            Lpaire.append(element)
        else:
            Limpaire.append(element)
    return [Limpaire,Lpaire]
#L1=(input("rentrer une liste : ")).split(",")
#print ("Le max est : ", maxi(L1))
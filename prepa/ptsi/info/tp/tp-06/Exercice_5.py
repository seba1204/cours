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
#L1=(input("rentrer une liste : ")).split(",")
#print ("Le max est : ", maxi(L1))
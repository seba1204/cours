
def Alphabet():
    l=""
    for a in range(97,123):        
        l+=chr(a)
    return l

def  decalage(n:int):
    chaine=Alphabet()
    charReturned=""
    for char in chaine:
        charReturned+=chr(((ord(char)-97)+n)%26+97)
    return charReturned
    
def indices(x:chr,phrase:str):
    L=[]
    n=0
    for a in phrase:
        if a==x:
            L.append(n)
        n+=1
    return L
def codage(n:int,chaine:str):
    charReturned=""
    for char in chaine:
        charReturned+=chr(((ord(char)-97)+n)%26+97)
    return charReturned
    
def decodage(n:int,chaine:str):
    return (codage(-n,chaine))
    
print (codage(3,"oralensam"))
print (decodage(3,codage(3,"oralensam")))
text = str(open("G:\Info\LADISPARITION.txt", "r").read())
def Alphabet():
    l=""
    for a in range(97,123):        
        l+=chr(a)
    return l

def codage(chaine:str):
    charReturned=""
    n=0
    for char in chaine:
        n=(n+1)%26
        charReturned+=chr(((ord(char)-97)+n)%26+97)
    return charReturned
print(codage("oralensam"))
def d(n):
    L=[1]
    for nombre in range (2,n+1):
        if n%nombre==0:
            L.append(nombre)
    return L
    
def DNT(n:int):
    L=[]    
    for nombre in range (2,n):
        if n%nombre==0:
            L.append(nombre)
    return L
        
def SommeCarreDNT(n:int):
    s=0
    for element in DNT(n):
        s+=element**2
    return s
    
L=[]
for n in range(1000):
    if n == SommeCarreDNT(n):
        L.append(n)

print (L)
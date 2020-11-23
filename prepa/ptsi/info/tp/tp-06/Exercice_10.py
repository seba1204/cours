import numpy as np
def pgcd(x:int, y:int):
    if x!=0 and y!=0:
        if y>x:
            a=y
            y=x
            x=a
        b=x
        r=x%y
        q=x//y
        while r!=0:
            x=y
            y=r
            r=x%y
            q=x//y
    else:
        b=1
        q=1
    return y
            
def estupremier(n:int):
    for i in range(1, n):
        p = pgcd(i,n)
        if p != 1 and p !=n:
            return False
    return True 

def Erathostene1(n:int):
    L=[]
    for i in range(n):
        if estupremier(i) == True:
            L.append(i)
    return L
    
def Erathostene2(n:int):
    L=[k for k in range(2,n+1)]
    k=2
    for n in range(2,n+1):
        while n*k in L:
            L.remove(n*k)
            k+=1
        k=2
    return L
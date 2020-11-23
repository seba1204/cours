import time
import random as rd
def sort(L:list):    
    L1=[L[0]]
    del L[0]
    for e in L:
        i=0      
        if e >= max(L1):
            L1.append(e)
        else:                
            while e>L1[i]:
                i+=1
            L1.insert(i,e)
    L=[]
    return L1
t0=time.clock()
n=int(input("Nombre terme suite : "))
L=[rd.randint(0,2*n) for k in range(n)]
print (L)
print(sort(L))
print (time.clock() - t0)
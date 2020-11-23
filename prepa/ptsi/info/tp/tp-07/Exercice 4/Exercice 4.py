# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 10:15:44 2018

@author: PONTS
"""

def Reverse(chaine:str):
    r=""
    for i in chaine:
        r = i + r
    return r
    
def palindrome(chaine:str):
    b=False
    if (chaine == Reverse(chaine)):
        b=True
    return b 

def palindromeChiffre(n:int):
    return palindrome(str(n))
n,a,b=0,0,0


for i in range(100,1000):
    for j in range(100,1000):
        if palindromeChiffre(i*j):
            if i*j > n:
                a=i
                b=j
                n=i*j

print (Reverse("engagelejeuquejelegagne"))
print (palindrome("engagelejeuquejelegagne"))
print (a,b,n) #913*993=906609
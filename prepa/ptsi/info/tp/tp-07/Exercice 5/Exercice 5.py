# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 10:15:44 2018

@author: PONTS
"""

def PaquetChaine(chaine:str):
    L=[]
    n=0
    chain=""
    for i in chaine:
        if n<5:            
            n+=1
            chain+=i
        if n==5:
            L.append(chain)
            chain=""
            n=0
    if chain!="":
        L.append(chain)
    return L

def PaquetChaineInverse(chaine:str):
    ci=""
    L=PaquetChaine(chaine)
    for i in L:
        ci = i + ci
    return ci


print(PaquetChaine("12345123451234512345123"))

print(PaquetChaineInverse("12345123451234512345123"))
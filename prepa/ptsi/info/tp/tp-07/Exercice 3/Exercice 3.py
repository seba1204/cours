# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 10:15:44 2018

@author: PONTS
"""

def compteCaradansChaine(chaine:str, cara:chr):
    C=0
    for i in chaine:
        if (i==cara):
            C+=1
    return C
    
text = str(open("G:\Info\LADISPARITION.txt", "r").read())
print (compteCaradansChaine(text, "e"))

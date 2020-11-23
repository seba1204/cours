# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 20:22:12 2019

@author: Sébastien PONT
"""

import random as rd
import numpy as np

class Matrice():
    """Objet matrice permettant de manipuler facilement des matrices."""
    _nbLignes=0
    _nbColonnes=0
    def __init__(self, n:int, p:int, _optionalData:np.array=np.zeros((0))):
        """Constructeur : 
            n->nb de lignes de la matrice
            p->nb de colonnes de la matrice
            optionalData->Tableau de la matrice"""
        if not _optionalData.any():            
            X=np.zeros((n,p))
            for i in range (n):
                for j in range (p):
                    X[i,j]=int(rd.randint(0,100))
            self._matrice=X
        else:
            self._matrice=_optionalData
        self._nbLignes=np.shape(self._matrice)[0]
        self._nbColonnes=np.shape(self._matrice)[1]
    def __str__(self):
        return  str(self._matrice)
    def __len__(self):
        return str("{0},x,{1}".format(self._nbLignes,self._nbColonnes))
    def _get_nbLignes(self):
        """Affiche le nombre de lignes de la matrice"""
        return self._nbLignes
    def _nbColonnes(self):
        """Affiche le nombre de colonnes de la matrice"""
        return self._nbColonnes
    def permuter(self, i:int, j:int):
        """Fonction qui permet de permuter deux lignes entre elles : 
            i,j compris entre 0 et (nbLignes-1)"""
        if i==j:
            pass
        elif i in range(self._nbLignes) or j in range(self._nbLignes): 
            self._matrice[i],self._matrice[j]=np.copy(self._matrice[j]),np.copy(self._matrice[i])
        else:
            raise ValueError('Impossible de permuter les lignes {0} et {1} dans une matrice de taille {2}x{3}'.format(i, j, self._nbLignes, self._nbColonnes))
    def combiner(self, i:int, j:int,µ:float):
        """Fonction qui affecte à la ligne i <- i-µ*j 
            i,j compris entre 0 et (nbLignes-1)"""
        if i in range(self._nbLignes) or j in range(self._nbLignes): 
            self._matrice[i]=np.copy(self._matrice[i])-µ*np.copy(self._matrice[j]) 
        else:
            raise ValueError('Impossible de combiner les lignes {0} et {1} dans une matrice de taille {2}x{3}'.format(i, j, self._nbLignes, self._nbColonnes))        
    def multiplier (self,i:int,µ:float):
        """Fonction qui affecte à la ligne i<-µ*i
            i compris entre 0 et (nbLignes-1)"""
        if i in range(self._nbLignes):
            self._matrice[i]=µ*np.copy(self._matrice[i])
        else:
            raise ValueError('Impossible de multiplier la ligne {0} dans une matrice de taille {1}x{2}'.format(i, self._nbLignes, self._nbColonnes)) 
        


print("On définit la matrice A")
A=Matrice(4,4)
print("A = \n",A)
print("On permute la ligne 1 et 2 de A")
A.permuter(0,1)
print("A = \n",A)
print("On combine la ligne 1 avec 5 fois la ligne 2 de A")
A.combiner(0,1,5)
print("A = \n",A)
print("On multiplie la ligne 3, 4 fois")
A.multiplier(2,4)
print("A = \n",A)
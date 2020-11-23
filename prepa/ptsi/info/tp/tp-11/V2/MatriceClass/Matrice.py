# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 20:22:12 2019

@author: Sébastien PONT
"""

import random as rd
import numpy as np

class Matrice(np.array):
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
        return int("{0},x,{1}".format(self._nbLignes,self._nbColonnes))
    def _get_nbLignes(self):
        """Affiche le nombre de lignes de la matrice"""
        return self._nbLignes
    def _get_nbColonnes(self):
        """Affiche le nombre de colonnes de la matrice"""
        return self._nbColonnes
    def __mul__(self,other):
        if (self.nbColonnes == other.nbLignes):
            m=self.nbColonnes
            n=self.nbLignes
            p=other.nbColonnes
            Y=np.zeros((n,p))
            A,B=self._matrice,other._matrice
            for i in range(n):
                for j in range(p):
                    for k in range(m):
                        Y[i,j]=Y[i,j]+A[i,k]*B[k,j]
            return Y
        else:
            raise ValueError('Impossible de multiplier une matrice de taille {0}x{1} et une matrice de taille {2}x{3}'.format(self._nbLignes, self._nbColonnes, other.nbLignes, other._nbColonnes))      
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
    nbLignes = property(_get_nbLignes)
    nbColonnes = property(_nbColonnes)
    def isMagic(self):
        liste=[]
        sommeDiag,sommeAntiDiag=0,0
        for i in range(self.nbLignes):
            sommeLigne=0
            for j in range(self.nbColonnes):
                sommeLigne+=self._matrice[i,j]
                if (i==j):
                    sommeDiag+=self._matrice[i,j]
                if (i==self.nbColonnes-j-1):
                    sommeAntiDiag+=self._matrice[i,j]
                if (type(self._matrice[i,j])!=np.int32):
                    return False
            liste.append(sommeLigne)
        print(sommeDiag,sommeAntiDiag)
        if (sommeDiag==sommeAntiDiag):
            for a in liste:
                if a!=sommeDiag:
                    return False
        else:
            return False
        return True
    def Gauss(self):
        C=Matrice(self.nbLignes,self.nbColonnes,self._matrice)
        n=C.nbColonnes
        for j in range (0,n-1):
            k=j        
            while C._matrice[k,j]==0:
                k=k+1
            m=C._matrice[k,j]    
            C.permuter(j,k)
            C.multiplier(j,1/m)
            for k in range (j+1,n-1):
                C.combiner(k,j,C._matrice[k,j])
        return C
    
    def Resoudre(self):
        C=self.Gauss()
        n=C.nbLignes #nombre de ligne de la matrice C = 3
        Y=np.zeros((n,1))
        Y[n-1]=C._matrice[n-1,C.nbColonnes-1] #Défnition de la 3 ème ligne de Y
        for i in range (n-2,0,-1): #pour i allant de n-2
            somme=C._matrice[i,C.nbColonnes-1] 
            for k in (i+1,n):
                somme=somme-C._matrice[i,k-1]*Y[k-1]  
            Y[i]=somme
        return Y
    
def test1():
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
def test2():
    print("On définit la matrice A")
    A=Matrice(1,2)
    print("A = \n",A)
    print("On définit la matrice B")
    B=Matrice(2,2)
    print("B = \n",B)
    print("C=A*B")
    C=A*B
    print("C = \n",C)    
def test3():
    print("On définit la matrice A")
    A=Matrice(2,3)
    print("A = \n",A)
    print("A a {0} ligne(s) et {1} colonne(s)".format(A.nbLignes, A.nbColonnes))
def test4():
    print("On définit la matrice A")
    A=Matrice(2,3, np.array([[8,1,6],
                             [3,5,7],
                             [4,9,2]]))
    print("A = \n",A)
    print("A est elle magique ? {0}".format(A.isMagic()))
def test5():
    print("On définit la matrice A")
    A=Matrice(3,4, np.array([[1,1,1,1],
                             [1,2,3,1],
                             [1,3,4,1]]))
    print("A = \n",A)
    print("Résoluion du système linéaire {0}".format(A.Resoudre()))
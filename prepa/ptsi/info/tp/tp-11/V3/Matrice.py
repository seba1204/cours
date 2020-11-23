import numpy as np
from Helpers import GenerateMatrices as gm


class Matrice(np.ndarray):   
    
    def __new__(subtype, shape, dtype=int, buffer=None, inversible=False, offset=0, strides=None, order=None):
        if (buffer==None and inversible is False):
            buffer=gm.GenerateRandomArray(shape,dtype)
        elif (buffer==None and inversible is True):
            buffer=gm.GenerateReversibleArray(shape, dtype)             
        obj = super(Matrice, subtype).__new__(subtype, shape, dtype,buffer, offset, strides,order)
        # add the new attribute to the created instance
        obj.inversible = inversible
        # Finally, we must return the newly created object:
        return obj

    def __array_finalize__(self, obj):
        # see InfoArray.__array_finalize__ for comments
        if obj is None: return
        self.inversible = getattr(obj, 'inversible', None)
    @property
    def linesNb(self):
        """Affiche le nombre de lignes de la matrice"""
        return self.shape[0]
    @property
    def columnsNb(self):
        """Affiche le nombre de colonnes de la matrice"""
        return self.shape[1]
    
    def __mul__(self,other):
        """Retourne le produit deux matrices"""
        if (self.columnsNb == other.linesNb):
            m=self.columnsNb
            n=self.linesNb
            p=other.columnsNb
            Y=np.zeros((n,p))
            for i in range(n):
                for j in range(p):
                    for k in range(m):
                        Y[i,j]=Y[i,j]+self[i,k]*other[k,j]
            return np.array(object=Y, dtype=self.dtype)
        else:
            raise ValueError('Impossible de multiplier une matrice de taille {0}x{1} et une matrice de taille {2}x{3}'.format(self._nbLignes, self._nbColonnes, other.nbLignes, other._nbColonnes))      
    def copy(self, dtype):        
        C=np.array(self, dtype=dtype, copy=True)
        return C.view(Matrice)
    def multiplier(self,i:int,µ:float):
        """Fonction qui affecte à la ligne i<-µ*i
           i compris entre 0 et (linesNb-1)"""
        if i in range(self.linesNb):
            self[i]=µ*np.copy(self[i])
        else:
            raise ValueError('Impossible de multiplier la ligne {0} dans une matrice de taille {1}x{2}'.format(i+1, self.linesNb, self.columnsNb))
    def combiner(self, i:int, j:int,µ:float):
        """Fonction qui affecte à la ligne i <- i-µ*j 
           i,j compris entre 0 et (linesNb-1)"""
        if (i in range(self.linesNb)) and (j in range(self.linesNb)):
            self[i]=np.copy(self[i])-µ*np.copy(self[j])
        else:
            raise ValueError('Impossible de combiner les lignes {0} et {1} dans une matrice de taille {2}x{3}'.format(i+1, j+1, self.linesNb, self.columnsNb))
    def permuter(self, i:int, j:int):
        """Fonction qui permet de permuter deux lignes entre elles : 
            i,j compris entre 0 et (linesNb-1)"""
        if i==j:
            pass
        elif i in range(self.linesNb) and j in range(self.linesNb): 
            self[i],self[j]=np.copy(self[j]),np.copy(self[i])
        else:
            raise ValueError('Impossible de permuter les lignes {0} et {1} dans une matrice de {2} lignes'.format(i+1, j+1, self.linesNb))

    def gaussJordan(self):
        """Renvoie la matrice après l'algorythme de GJ à une matrice quelconque"""
        C=self.copy(float)
        n,p=C.linesNb,C.columnsNb
        #1. On teste s'il y a les 1eres colonnes sont totalement nulles, et on retient leur index
        j,z,k=0,-1,n
        while j<p and k==n:
            k=0
            while (k<n) and (C[k,j]==0):k+=1
            if (k==n):z=j
            j+=1
            
        #2. on range les lignes dans l'ordre selon leur nb de zéros en début de ligne
        i,D=0,np.zeros(C.shape)
        pivot=[]
        for j in range(z+1,min(n,p)):
            k=0
            while (k<n):
                if (C[k,j]!=0): 
                    C.multiplier(k,(1/C[k,j]))
                    D[i]=C[k]
                    i+=1
                    C[k]=np.zeros((1,p))
                    pivot.append(j)
                k+=1
        D=D.view(Matrice)
        #---fin de Gauss
        #3. on part du dernier pivot et on enlève à toutes les lignes se trouvant au-dessus
        # x fois la ligne contenant ce pivot
        """for i in range(0,len(pivot)-1):
            for j in range (len(pivot)-2,-1,-1):
                D.combiner(j,len(pivot)-i,D[len(pivot)-i,pivot[i]])"""
        return D

"""==================================Tests unitaires=================================="""
def testOperationsElementaires():
    print("On définit la matrice A")
    A=Matrice(shape=(4,4))
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
def testMultiplication():
    print("On définit la matrice A")
    A=Matrice(shape=(2,3))
    print("A = \n",A)
    print("On définit la matrice B")
    B=Matrice(shape=(3,2))
    print("B = \n",B)
    print("On multiplie A par B : AB=\n{0}".format(A*B))
def gaussJordan():
    print("On définit la matrice (augmentée) A")
    A=Matrice(shape=(4,5))
    print("A = \n",A)
    print("On applique GJ à A : \n{0}".format(A.gaussJordan()))
def gaussJordan2():
    print("On définit la matrice (augmentée) A")
    B=np.array([[0,0,0,0,0,0],
                [0,0,2,3,4,5],
                [0,0,5,0,0,0],
                [0,0,8,9,7,4],
                [0,1,0,0,0,0]])
    A=B.view(Matrice)
    print("A = \n",A)
    print("On applique GJ à A : \n{0}".format(A.gaussJordan()))
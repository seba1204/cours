import numpy as np
import time
import matplotlib.pylab as pl
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
    def __eq__(self, other):
        if str(self) == str(other):
            return True
        return False
    def c_(*args):
        C=np.c_[args]
        return C.view(Matrice)
    def copy(self, dtype):        
        C=np.array(self, dtype=dtype, copy=True)
        return C.view(Matrice)
    def multiplier(self,i:int,µ:float):
        """Fonction qui affecte à la ligne i<-µ*i
           i compris entre 0 et (linesNb-1)"""
        if i in range(self.linesNb):
            a=µ*np.copy(self[i])
            B=[]
            for b in a:
                if str(b)=="-0.0":b=0.
                B.append(b)
            a=np.array(B)
            self[i]=a
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
        #1. On teste si les 1eres colonnes sont totalement nulles, et on retient leur index
        j,z,k=0,-1,n
        while j<p and k==n:
            k=0
            while (k<n) and (C[k,j]==0):k+=1
            if (k==n):z=j
            j+=1
        #2. On range les lignes dans l'ordre selon leur nb de zéros en début de ligne
        i,D=0,np.zeros(C.shape)
        pivot=[]
        for j in range(z+1,min(n,p)):
            k=0
            while (k<n):
                if (C[k,j]!=0): 
                    C.multiplier(k,(1/C[k,j]))
                    for l in range (k+1,n):
                        C.combiner(l, k, C[l,j])
                    D[i]=C[k]
                    i+=1
                    C[k]=np.zeros((1,p))
                    pivot.append(j)
                k+=1
        D=D.view(Matrice)
        #---fin de Gauss
        #3. on part du dernier pivot et on enlève à toutes les lignes se trouvant au-dessus
        # x fois la ligne contenant ce pivot
        a=len(pivot)-1
        for j in range(pivot[a],0,-1):
            for i in range(pivot.index(j)-1,-1,-1):
                D.combiner(i, pivot.index(j), D[i,j])
        return D
    def isInversible(self):
        A=self.gaussJordan()
        print("A=\n", A)
        B=gm.GenerateIdentity(self.shape)
        print("B=\n", B)
        if A==B:
            return True
        return False
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
    C=np.array([[1,1,1,1],
                [1,2,3,1],
                [1,3,4,2]])
    
    D=np.array([[0,1,2],
                [3,4,5],
                [6,9,8],
                [7,4,1]])
    A=D.view(Matrice)
    print("A = \n",A)
    print("On applique GJ à A : \n{0}".format(A.gaussJordan()))
def Complexité(n:int):
    T=[]
    L=[]
    for i in range(200,n+1):
        A=Matrice(shape=(i,i))
        X=Matrice(shape=(i,1))
        B=np.array(A*X).view(Matrice)
        C=np.c_[A,B].view(Matrice)
        t1=time.time()
        C.gaussJordan()
        T.append(time.time()-t1)
        L.append(i)
        print(i)
    Y=[np.log(x) for x in T]
    L2=[np.log(x) for x in L]
    pl.plot(L2,Y, color="blue")
    pl.show()

def compZeros():
    i=-1
    e=10**i
    A=np.linalg.solve(np.array([[1, 1-e],[1,1]]),np.array([[1],[1]]))
    B=np.array([[1, 0,5-4/e],[0,1,4/e]])
    while ( i >(-20)):
        i-=1
        e=10**i
        A=np.linalg.solve(np.array([[1, 1-e],[1,1]]),np.array([[1],[1]]))
        B=np.array([[1, 0,5-4/e],[0,1,4/e]])
        print("e=",e,"\nA= : \n",str(A),"\nB= :\n", str(B))
    return -i
def tesInversibilité():
    M=np.array([[1,0,1,3],[-1,2,2,-4],[1,2,1,1],[1,-2,-1,5]], dtype=float).view(Matrice)
    print(M.dtype)
    return M.isInversible()
print(tesInversibilité())
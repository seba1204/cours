import pylab as pl
import numpy as np

def SuiteSyracuse(n:int, u0:int):    
    if (u0==0):
        u0=1
        
        
    listPoints = [[],[]]
    listPoints[0] = np.linspace(0,n,n)
    listPoints[1].append(u0)
    un=u0
    for i in range(n-1):
        if (un%2==0):
            un=un//2
        else:
            un=3*un+1        
        listPoints[1].append(un)
        
    return listPoints
   
def TraceSyracuse(n:int, u0:int):      
    xlabel="n"
    ylabel="Un"
    
    
    listPoints = SuiteSyracuse(n,u0)   
    
    pl.xlabel(xlabel)
    pl.ylabel(ylabel)
    pl.xlim=(min(listPoints[0]) - 2, max(listPoints[0])+2)
    pl.ylim=(min(listPoints[1]), max(listPoints[1]))
    pl.plot(listPoints[0],listPoints[1],color="red", linewidth=2, label="Syracuse")
    pl.legend()
    pl.show()
    pl.close() 
    
TraceSyracuse(10, 1000)
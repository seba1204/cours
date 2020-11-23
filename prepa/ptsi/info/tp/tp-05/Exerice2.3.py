import time

def puiss(x:float, n:int):    
    r = 1
    compt = 0
    if(n>=2):
        for i in range(n):
            r=r*x
            compt+=1
        return r
    elif(n==1):
        return x
    else:
        return 0
    

def puissrapide(x:float, n:int):
    if(n>=2):
        if (n%2==0):
            r=(x**2)**(n/2)
        else:
             r=x*(x**2)**((n-1)/2)   
        return r
    else:
        return 0
        

t1=time.clock()
puiss(2,123)
t1=time.clock()-t1
t2=time.clock()
puissrapide(2,123)
t2=time.clock()-t2


print("t1= ", t1, " t= ", t2)

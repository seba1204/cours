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
    
def puiss(x:float, n:int):    
    r = 1
    if(n>=2):
        for i in range(n):
            r=r*x
        return r
    elif(n==1):
        return x
    else:
        return 0
    
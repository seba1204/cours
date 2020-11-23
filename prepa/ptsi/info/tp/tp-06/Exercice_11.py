def search(L:list, element:int):
    g,d=0,len(L)
    m = (g+d)//2
    while ((abs(d-g))>1):
        if (element < L[m]):
            d=m
        elif (element > L[m]):
            g=m
        else:
            g=m
            d=m+1
        m=int((g+d)//2)
    
    if L[m-1]==element:        
        while (L[m-1]==element):
            m-=1
    if element != L[m]:
        raise ValueError('{0} n\'existe pas'.format(element))
    else:
        return m
            
        
while 1:
    L=[k for k in range(1,12)]
    #L=[1,1,2,3,4,5]
    print("L = ",end="")
    for i in L:
        print(i,", ",end="")
    a=int(input("\nVeuillez rentrer un élément à chercher dans L : "))
    try:
        print (search(L,a))
    except ValueError as err:
        print(err.args)
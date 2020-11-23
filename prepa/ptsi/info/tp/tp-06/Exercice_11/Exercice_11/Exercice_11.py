import sys
def search(L:list, element:int):
    g,d=0,len(L)-1
    m = (g+d)//2
    while ((abs(g-d))>1):
        if (element < L[m]):
            d=m
        else:
            g=m
        m=int((g+d)//2)
    if element != L[m]:
        raise ValueError('{0} n\'existe pas'.format(element))
    else:
        return m
while 1:
    L=[k for k in range(1,12)]
    print("L = ",end="")
    for i in L:
        print(i,", ",end="")
    a=int(input("\nVeuillez rentrer un élément à chercher dans L : "))
    try:
        print (search(L,a))
    except ValueError as err:
        print(err.args)
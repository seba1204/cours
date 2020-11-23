def pgcd(x:int, y:int):
    if x!=0 and y!=0:
        if y>x:
            a=y
            y=x
            x=a
        b=x
        r=x%y
        q=x//y
        while r!=0:
            x=y
            y=r
            r=x%y
            q=x//y
    else:
        b=1
        q=1
    return y
            
def estupremier(n:int):
    for i in range(1, n):
        p = pgcd(i,n)
        if p != 1 and p !=n:
            return False
    return True 
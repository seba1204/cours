
ML = [1,3,5,7,8,10,12]
MC = [2, 4, 5, 9, 11]


B = lambda a : not(a%400) or (not(a%4) and bool(a%100))

def sumYears(begin, end):
    A= [k for k in range(begin, end +1) if B(k)]
    return (A, sum(A))

def nbOfDaysInMonth(month, isBissextile):
    if  (month in MC):
        if month == 2:
            if isBissextile:
                return 29
            return 28
        else:
            return 30
    return 31

def nbOfDays(date):
    S = 0
    for i in range(1, date[1]):
        S += nbOfDaysInMonth(i, B(date[2]))
    return S + date[0]
def synodique(start,end, lunaisons):
    S = 0
    for a in range(start, end  +1):
        S+= 365 + B(a)
    return S / lunaisons
def isFullMoonMdr(date):
       #15 janvier 1900 est une plein lune
    S=0
    if date[1] < 1900:
        for a in range(date[2], 1900):
            S +=  365 + B(a)
        S = S + 15 - nbOfDays(date)
        return S % synodique(1900, 2019, 1484) < 1

def eratosthene(n):
    firstNb = []
    isANewFirst = False
    for i in range(2, n+1):
        for alreadyFirst in firstNb:
            if i % alreadyFirst:
                isANewFirst *= True
        
            
print(isFullMoonMdr([4,8,1789]))

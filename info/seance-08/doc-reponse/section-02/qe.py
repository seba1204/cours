def isFullMoonMdr(date):
       # 15 janvier 1900 est une plein lune
    S = 0
    if date[1] < 1900:
        for a in range(date[2], 1900):
            S += 365 + bissextile(a)
        S = S + 15 - nbOfDays(date)
        return S % synodique(1900, 2019, 1484) < 1

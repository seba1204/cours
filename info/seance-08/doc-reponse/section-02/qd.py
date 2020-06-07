def synodique(start, end, lunaisons):
    S = 0
    for a in range(start, end + 1):
        S += 365 + bissextile(a)
    return S / lunaisons

def nbOfDaysInMonth(month, isBissextile):
    if (month in MC):
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
        S += nbOfDaysInMonth(i, bissextile(date[2]))
    return S + date[0]

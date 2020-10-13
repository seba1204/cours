def getRooth(intervals, eps):
    racines = []
    for a, b in intervals:
        racines.append(dicho(f, a, b, eps))

    return racines


getRooth(INTERVAL, PRES)

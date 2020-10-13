def getError(n):
    R = np.array([[0, 0, 1], [1, 0, 3], [0, 1, 0]])
    racines = getRooth(INTERVAL, PRES)
    Mn = getRPowN(racines, n)
    Rn = np.linalg.matrix_power(R, n)
    Er_abs = np.abs(Mn - Rn)
    A = np.max(Rn)
    B = np.max(Er_abs)
    return float(f'{B / A / PRES:.2f}')

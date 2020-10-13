def nablah(u):
    x, y = u[0], u[1]
    a = 4*x**3 - 4*y
    b = 4*y**3 - 4*x
    return np.array([a, b])

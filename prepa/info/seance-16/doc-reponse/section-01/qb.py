def nabla(u):
    x, y = u[0], u[1]
    a = 2*x + 2*y
    b = 4*y + 2*x
    return np.array([a, b])

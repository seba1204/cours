def Vunit(u):
    x, y = u[0], u[1]
    norme = np.sqrt(x**2+y**2)
    return np.array([x/norme, y/norme])

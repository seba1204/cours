def Trace(f, borneMin, borneMax):
    X = np.linspace(borneMin, borneMax, 1000)
    Y = f(X)
    plt.plot(X, Y)
    plt.grid(True, which='both')
    plt.show()


Trace(f, -3, 3)

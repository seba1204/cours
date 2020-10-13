def TraceFunction(f, borneMax, borneMin, nbPoints):
    X = np.linspace(borneMin, borneMax, nbPoints)
    Y = [f(x) for x in X]
    plt.plot(X, Y)
    plt.grid()
    plt.show()

def h(x): return np.exp(x)-3*x**2

TraceFunction(h, -2, 4, 1000)

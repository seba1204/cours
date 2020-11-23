def Trace(T):
    x = np.linspace(-10*T, 10*T, 1200)
    y = [omega(k) for k in x]
    plt.plot(x, y)
    plt.show()

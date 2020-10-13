def TraceRepartition():
    X = np.linspace(0.4, 1.6, 1000)

    params = [
        (5, 'r'),
        (20, 'g'),
        (100, 'b')
    ]

    for d, color in params:
        Z = S(d)
        Y = repartition(Z, X)
        plt.plot(X, Y, color, label=str(d))
    plt.show()

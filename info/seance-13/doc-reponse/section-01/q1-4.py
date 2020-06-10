def traceF():
    X = np.linspace(0, 1, 100)
    Y1 = [f(x) for x in X]
    Y2 = [f_compose(3, x) for x in X]

    plt.plot(X, Y1, label='$f(x)$')
    plt.plot(X, Y2, label='$f(f(f(x)))$')
    plt.legend()
    plt.show()

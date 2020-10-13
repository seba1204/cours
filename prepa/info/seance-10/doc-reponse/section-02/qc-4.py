def TraceError(N):
    X, Y = [], []

    for n in N:
        er = getError(n)
        X.append(n)
        Y.append(er)
    plt.plot(X, Y, 'rx')
    plt.show()
